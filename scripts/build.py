#!/usr/bin/env python3
"""Generate the agent-native WWDC knowledge base from Apple's live developer-video feeds.

Covers every scrapable event (WWDC 2014-2026, Tech Talks, Meet with Apple). Output is a
flat, self-describing corpus designed for direct consumption by AI agents:

    catalog.json            Master machine index (entrypoint): provenance, counts, every session
    events.json             Per-event summaries with date ranges and counts
    topics.json             Topic -> sessions across all years
    llms.txt                llms.txt-format index
    AGENTS.md / README.md   Agent + human guides
    schema/*.schema.json    JSON Schema for catalog.json and session metadata
    sessions/<event>/<id>/  metadata.json, README.md, transcript.md, transcript.json
    events/<event>/index.md Per-event session list grouped by topic
    topics/<slug>.md        Per-topic index across events
    platforms/<slug>.md     Per-platform index

Run: python3 scripts/build.py
"""
import gzip
import html
import json
import re
import shutil
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

CONFIG_URL = "https://api2024.wwdc.io/config.json"
ROOT = Path(__file__).resolve().parent.parent
REPO = "guitaripod/wwdc-sessions"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/master"
SCHEMA_VERSION = 1
EXTRA_EVENTS = {"tech-talks", "meet-with-apple"}
INCLUDE_TYPES = {"Video", "Special Event", "Article"}


def fetch(url, attempts=4):
    """Fetch a URL with retry/backoff, transparently decompressing gzip responses."""
    req = urllib.request.Request(
        url, headers={"Accept-Encoding": "gzip", "User-Agent": "wwdc-sessions/2.0"}
    )
    for attempt in range(attempts):
        try:
            data = urllib.request.urlopen(req, timeout=90).read()
            return gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data
        except Exception:
            if attempt == attempts - 1:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"unreachable: fetch exhausted retries for {url}")


def fetch_json(url):
    return json.loads(fetch(url))


def is_session_event(event_id):
    """Whether an event holds developer sessions worth indexing."""
    return bool(re.match(r"^wwdc\d{4}$", event_id)) or event_id in EXTRA_EVENTS


def event_year(event):
    """Best-effort calendar year for an event."""
    match = re.match(r"^wwdc(\d{4})$", event["id"])
    if match:
        return int(match.group(1))
    start = event.get("startTime") or ""
    return int(start[:4]) if start[:4].isdigit() else None


def strip_html(text):
    """Convert Apple's HTML-highlighted code spans into plain source text."""
    return html.unescape(re.sub(r"<[^>]+>", "", text or ""))


def normalize_code(raw):
    """Strip Apple's uniform wrapper indent from a code snippet, preserving relative nesting."""
    lines = strip_html(raw).split("\n")
    if len(lines) > 1:
        body = [line for line in lines[1:] if line.strip()]
        base = min((len(line) - len(line.lstrip(" ")) for line in body), default=0)
        lines = [lines[0]] + [line[base:] if line.strip() else "" for line in lines[1:]]
    return "\n".join(lines).rstrip()


def docc_json_url(url):
    """Map a developer.apple.com documentation URL to its machine-readable DocC JSON endpoint."""
    match = re.match(r"https?://developer\.apple\.com/documentation/(.+)", url or "")
    if not match:
        return None
    path = match.group(1).split("#")[0].split("?")[0].rstrip("/")
    return f"https://developer.apple.com/tutorials/data/documentation/{path}.json" if path else None


def sosumi_url(url):
    """Map any developer.apple.com URL to its sosumi.ai Markdown mirror for agent consumption."""
    if not url or "developer.apple.com/" not in url:
        return None
    return re.sub(r"^https?://developer\.apple\.com/", "https://sosumi.ai/", url)


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-") or "untitled"


def format_timestamp(seconds):
    minutes, secs = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:d}:{minutes:02d}:{secs:02d}" if hours else f"{minutes:d}:{secs:02d}"


def yaml_scalar(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value).replace('"', '\\"')
    return f'"{text}"'


def frontmatter(fields):
    """Serialize a flat dict of scalars and scalar-lists as YAML frontmatter."""
    lines = ["---"]
    for key, value in fields.items():
        if value is None or value == [] or value == "":
            continue
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(yaml_scalar(v) for v in value)}]")
        else:
            lines.append(f"{key}: {yaml_scalar(value)}")
    lines.append("---")
    return "\n".join(lines)


def fetch_transcript_segments(url):
    """Return [{start, text}] segments for a transcript feed entry."""
    data = fetch_json(url)
    raw = next(iter(data.values())).get("transcript", [])
    return [{"start": round(float(ts), 3), "text": text.strip()} for ts, text in raw if text.strip()]


def render_transcript_markdown(segments, chunk_seconds=45):
    """Render transcript segments into timestamped Markdown paragraphs."""
    if not segments:
        return ""
    paragraphs, buffer, start = [], [], segments[0]["start"]
    for segment in segments:
        if buffer and segment["start"] - start >= chunk_seconds:
            paragraphs.append((start, " ".join(buffer).strip()))
            buffer, start = [], segment["start"]
        buffer.append(segment["text"])
    if buffer:
        paragraphs.append((start, " ".join(buffer).strip()))
    return "\n\n".join(f"**[{format_timestamp(ts)}]** {body}" for ts, body in paragraphs if body)


def resolve_resources(related, resources_by_id):
    """Resolve related-resource ids into structured link records with Markdown/DocC endpoints."""
    records = []
    for resource_id in (related or {}).get("resources", []):
        resource = resources_by_id.get(resource_id)
        if not resource:
            continue
        url = resource.get("url", "")
        record = {
            "title": resource.get("title"),
            "url": url,
            "type": resource.get("resource_type"),
            "description": resource.get("description"),
        }
        sosumi = sosumi_url(url)
        if sosumi:
            record["sosumiURL"] = sosumi
        docc = docc_json_url(url)
        if docc:
            record["doccJSON"] = docc
        records.append(record)
    return records


def clean_snippets(snippets):
    return [
        {
            "title": snippet.get("title"),
            "language": snippet.get("language", "swift"),
            "startTimeSeconds": snippet.get("startTimeSeconds"),
            "code": normalize_code(snippet.get("code", "")),
        }
        for snippet in snippets or []
    ]


def media_record(media):
    keys = ["hls", "downloadHLS", "downloadSD", "downloadHD", "duration", "tnsURL"]
    return {key: media[key] for key in keys if key in (media or {})}


def build_session(content, event, topics_by_id, resources_by_id, segments, languages):
    """Assemble a normalized, richly structured record for one session."""
    media = media_record(content.get("media"))
    duration = media.get("duration")
    if not duration and segments:
        duration = int(segments[-1]["start"])
    word_count = sum(len(s["text"].split()) for s in segments) if segments else 0
    session_id = content["id"]
    return {
        "schemaVersion": SCHEMA_VERSION,
        "id": session_id,
        "event": content.get("eventId"),
        "eventName": event.get("name"),
        "year": event_year(event),
        "eventContentId": content.get("eventContentId"),
        "title": content.get("title"),
        "description": content.get("description"),
        "url": content.get("webPermalink"),
        "sosumiURL": sosumi_url(content.get("webPermalink")),
        "type": content.get("type"),
        "publishedAt": content.get("originalPublishingDate"),
        "platforms": content.get("platforms", []),
        "keywords": content.get("keywords", []),
        "topics": [topics_by_id[t] for t in content.get("topicIds", []) if t in topics_by_id],
        "primaryTopic": topics_by_id.get(content.get("primaryTopicID")),
        "duration": duration,
        "hasTranscript": bool(segments),
        "transcriptWordCount": word_count,
        "availableLanguages": languages,
        "media": media,
        "codeSnippets": clean_snippets(content.get("codeSnippets")),
        "resources": resolve_resources(content.get("related"), resources_by_id),
    }


def assign_paths(sessions):
    """Assign each session a stable repo path mirroring Apple's video URL: sessions/<event>/<n>/.

    Uses Apple's numeric eventContentId as the leaf (so a developer.apple.com/videos/play/<event>/<n>
    URL maps directly to a repo path), falling back to the full id if that id is missing or collides.
    """
    counts = {}
    for session in sessions:
        counts[(session["event"], session.get("eventContentId"))] = (
            counts.get((session["event"], session.get("eventContentId")), 0) + 1)
    for session in sessions:
        ecid = session.get("eventContentId")
        unique = ecid is not None and counts[(session["event"], ecid)] == 1
        leaf = str(ecid) if unique else session["id"]
        session["path"] = f"sessions/{session['event']}/{leaf}/"
        files = {"metadata": session["path"] + "metadata.json", "readme": session["path"] + "README.md"}
        if session["hasTranscript"]:
            files["transcript"] = session["path"] + "transcript.md"
            files["transcriptJSON"] = session["path"] + "transcript.json"
        session["files"] = files


def relative_path(session, depth):
    """Path to a session README from an index file `depth` directories below the repo root."""
    return ("../" * depth) + session["path"] + "README.md"


def render_session_readme(session):
    head = frontmatter({
        "id": session["id"],
        "event": session["event"],
        "year": session["year"],
        "title": session["title"],
        "type": session["type"],
        "url": session["url"],
        "topics": session["topics"],
        "platforms": session["platforms"],
        "hasTranscript": session["hasTranscript"],
    })
    lines = [head, "", f"# {session['title']}", ""]
    facts = [f"**Event:** {session['eventName']}"]
    if session.get("primaryTopic"):
        facts.append(f"**Topic:** {session['primaryTopic']}")
    if session.get("platforms"):
        facts.append(f"**Platforms:** {', '.join(session['platforms'])}")
    if session.get("publishedAt"):
        facts.append(f"**Published:** {session['publishedAt'][:10]}")
    facts.append(f"**Session:** [{session['id']}]({session['url']})")
    lines += [" · ".join(facts), ""]
    if session.get("description"):
        lines += [session["description"], ""]
    if session.get("keywords"):
        lines += ["**Keywords:** " + ", ".join(f"`{kw}`" for kw in session["keywords"]), ""]

    if session["hasTranscript"]:
        lines += ["## Transcript", "",
                  "[Read the transcript](transcript.md) · [Structured JSON](transcript.json)",
                  f"({session['transcriptWordCount']:,} words)", ""]

    if session.get("resources"):
        lines += ["## Documentation & Resources", ""]
        for resource in session["resources"]:
            label = resource["title"] or resource["url"]
            kind = f" _{resource['type']}_" if resource.get("type") else ""
            lines.append(f"- [{label}]({resource['url']}){kind}")
            if resource.get("sosumiURL"):
                lines.append(f"  - Markdown (sosumi.ai): {resource['sosumiURL']}")
            if resource.get("doccJSON"):
                lines.append(f"  - DocC JSON: {resource['doccJSON']}")
        lines.append("")

    if session.get("codeSnippets"):
        lines += ["## Code Snippets", ""]
        for snippet in session["codeSnippets"]:
            stamp = (
                f" — [{format_timestamp(snippet['startTimeSeconds'])}]"
                if snippet.get("startTimeSeconds") is not None else ""
            )
            lines += [f"### {snippet.get('title') or 'Snippet'}{stamp}", "",
                      f"```{snippet.get('language', 'swift')}", snippet["code"].rstrip(), "```", ""]

    if session.get("media", {}).get("hls"):
        lines += ["## Video", "", f"- HLS stream: {session['media']['hls']}"]
        if session["media"].get("downloadHLS"):
            lines.append(f"- Download: {session['media']['downloadHLS']}")
        lines.append("")

    lines += ["---", "",
              f"_Source: [Apple Inc.]({session['url']}) — developer.apple.com. Indexed for agent consumption._"]
    return "\n".join(lines)


def render_transcript_markdown_page(session, segments):
    head = frontmatter({
        "id": session["id"], "event": session["event"], "title": session["title"],
        "url": session["url"], "language": "eng", "words": session["transcriptWordCount"],
    })
    body = render_transcript_markdown(segments)
    return (f"{head}\n\n# {session['title']} — Transcript\n\n"
            f"[Session page]({session['url']}) · [Metadata](metadata.json) · "
            f"[Structured JSON](transcript.json)\n\n{body}\n")


def write_sessions(sessions, transcripts):
    for session in sessions:
        session_dir = ROOT / session["path"]
        session_dir.mkdir(parents=True, exist_ok=True)
        (session_dir / "metadata.json").write_text(json.dumps(session, indent=2, ensure_ascii=False))
        (session_dir / "README.md").write_text(render_session_readme(session))
        if session["hasTranscript"]:
            segments = transcripts[session["id"]]
            (session_dir / "transcript.md").write_text(render_transcript_markdown_page(session, segments))
            (session_dir / "transcript.json").write_text(json.dumps(
                {"id": session["id"], "language": "eng", "source": session["url"],
                 "wordCount": session["transcriptWordCount"], "segments": segments},
                ensure_ascii=False))


def catalog_record(session):
    return {
        "id": session["id"], "event": session["event"], "year": session["year"],
        "eventContentId": session["eventContentId"], "title": session["title"],
        "type": session["type"], "url": session["url"], "sosumiURL": session["sosumiURL"],
        "duration": session["duration"], "publishedAt": session["publishedAt"],
        "platforms": session["platforms"], "primaryTopic": session["primaryTopic"],
        "topics": session["topics"], "keywords": session["keywords"],
        "hasTranscript": session["hasTranscript"],
        "transcriptWordCount": session["transcriptWordCount"],
        "availableLanguages": session["availableLanguages"],
        "resourceCount": len(session["resources"]),
        "codeSnippetCount": len(session["codeSnippets"]),
        "path": session["path"], "description": session["description"],
    }


def write_catalog(sessions, events, generated_at, source_updated):
    by_event = {}
    for session in sessions:
        by_event.setdefault(session["event"], []).append(session)
    event_summaries = [
        {
            "id": event["id"], "name": event.get("name"), "year": event_year(event),
            "startTime": event.get("startTime"),
            "sessionCount": len(by_event.get(event["id"], [])),
            "transcriptCount": sum(1 for s in by_event.get(event["id"], []) if s["hasTranscript"]),
            "index": f"events/{event['id']}/index.md",
        }
        for event in sorted(events, key=lambda e: (event_year(e) or 0, e["id"]), reverse=True)
        if by_event.get(event["id"])
    ]
    catalog = {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": generated_at,
        "sourceUpdated": source_updated,
        "source": "Apple WWDC developer-video feeds (resolved via api2024.wwdc.io)",
        "license": "Content © Apple Inc. Tooling under MIT (see LICENSE).",
        "counts": {
            "events": len(event_summaries),
            "sessions": len(sessions),
            "transcripts": sum(1 for s in sessions if s["hasTranscript"]),
        },
        "links": {
            "events": "events.json", "topics": "topics.json", "agents": "AGENTS.md",
            "catalogSchema": "schema/catalog.schema.json", "sessionSchema": "schema/session.schema.json",
        },
        "events": event_summaries,
        "sessions": [catalog_record(s) for s in
                     sorted(sessions, key=lambda s: (-(s["year"] or 0), s["event"], s["id"]))],
    }
    (ROOT / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False))
    (ROOT / "events.json").write_text(json.dumps(
        {"schemaVersion": SCHEMA_VERSION, "generatedAt": generated_at, "events": event_summaries},
        indent=2, ensure_ascii=False))
    return catalog, event_summaries, by_event


def write_event_indexes(by_event, events_by_id):
    events_dir = ROOT / "events"
    for event_id, rows in by_event.items():
        event = events_by_id[event_id]
        by_topic = {}
        for session in rows:
            for topic in session["topics"] or ["Uncategorized"]:
                by_topic.setdefault(topic, []).append(session)
        lines = [f"# {event.get('name', event_id)} Sessions", "",
                 f"{len(rows)} sessions · {sum(1 for s in rows if s['hasTranscript'])} with transcripts.", ""]
        for topic in sorted(by_topic):
            lines += [f"## {topic}", ""]
            for session in sorted(by_topic[topic], key=lambda s: s["title"] or ""):
                flag = " · 📝" if session["hasTranscript"] else ""
                lines.append(f"- [{session['title']}]({relative_path(session, 2)}){flag}")
            lines.append("")
        (events_dir / event_id).mkdir(parents=True, exist_ok=True)
        (events_dir / event_id / "index.md").write_text("\n".join(lines))


def write_topic_indexes(sessions):
    topics_dir = ROOT / "topics"
    topics_dir.mkdir(exist_ok=True)
    by_topic = {}
    for session in sessions:
        for topic in session["topics"]:
            by_topic.setdefault(topic, []).append(session)
    manifest = []
    for topic in sorted(by_topic):
        rows = sorted(by_topic[topic], key=lambda s: (-(s["year"] or 0), s["title"] or ""))
        lines = [f"# {topic}", "", f"{len(rows)} sessions across all events.", ""]
        current_year = None
        for session in rows:
            if session["year"] != current_year:
                current_year = session["year"]
                lines += ["", f"### {session['eventName'] or current_year}", ""]
            lines.append(f"- [{session['title']}]({relative_path(session, 1)})")
        (topics_dir / f"{slugify(topic)}.md").write_text("\n".join(lines) + "\n")
        manifest.append({"topic": topic, "slug": slugify(topic), "sessionCount": len(rows),
                         "sessionIds": [s["id"] for s in rows]})
    (ROOT / "topics.json").write_text(json.dumps(
        {"schemaVersion": SCHEMA_VERSION, "topics": manifest}, indent=2, ensure_ascii=False))
    return by_topic


def write_platform_indexes(sessions):
    platforms_dir = ROOT / "platforms"
    platforms_dir.mkdir(exist_ok=True)
    by_platform = {}
    for session in sessions:
        for platform in session["platforms"]:
            by_platform.setdefault(platform, []).append(session)
    for platform in sorted(by_platform):
        rows = sorted(by_platform[platform], key=lambda s: (-(s["year"] or 0), s["title"] or ""))
        lines = [f"# {platform} Sessions", "", f"{len(rows)} sessions.", ""]
        for session in rows:
            lines.append(f"- [{session['title']}]({relative_path(session, 1)}) — {session['eventName']}")
        (platforms_dir / f"{slugify(platform)}.md").write_text("\n".join(lines) + "\n")


def write_llms_txt(catalog, event_summaries):
    counts = catalog["counts"]
    lines = [
        "# WWDC Sessions",
        "",
        "> Agent-native knowledge base of Apple WWDC developer sessions (2014-2026, plus Tech Talks "
        "and Meet with Apple): clean transcripts, structured metadata, code snippets, and links to "
        "official documentation. Generated from Apple's public developer-video feeds.",
        "",
        f"{counts['sessions']} sessions across {counts['events']} events · "
        f"{counts['transcripts']} with full transcripts. The machine entrypoint is catalog.json: "
        "one record per session with stable id, topics, platforms, languages, and file paths. "
        "Each session lives at sessions/<event>/<id>/ with metadata.json, README.md, transcript.md, "
        "and transcript.json.",
        "",
        "## Start here",
        "- [Master catalog (JSON)](catalog.json): every session, with provenance and counts",
        "- [Events (JSON)](events.json): per-event summaries and counts",
        "- [Topics (JSON)](topics.json): sessions grouped by topic across years",
        "- [Agent guide](AGENTS.md): access patterns, path templates, conventions",
        "- [Catalog schema](schema/catalog.schema.json) · [Session schema](schema/session.schema.json)",
        "",
        "## Events",
    ]
    for event in event_summaries:
        lines.append(f"- [{event['name']}](events/{event['id']}/index.md): "
                     f"{event['sessionCount']} sessions, {event['transcriptCount']} transcripts")
    (ROOT / "llms.txt").write_text("\n".join(lines) + "\n")


def write_agents_md(catalog, event_summaries):
    counts = catalog["counts"]
    topic_count = len({t for s in catalog["sessions"] for t in s["topics"]})
    rows = "\n".join(
        f"| {e['name']} | {e['id']} | {e['sessionCount']} | {e['transcriptCount']} |"
        for e in event_summaries)
    content = f"""# Agent Guide

A knowledge base of **Apple WWDC developer sessions** (WWDC 2014-2026, plus Tech Talks and Meet
with Apple), structured for direct consumption by AI agents. Free, non-commercial, and
complementary to Apple's official material — every session links back to developer.apple.com.

**{counts['sessions']} sessions · {counts['transcripts']} transcripts · {counts['events']} events ·
{topic_count} topics.**

## Layout

```
catalog.json                     Master index — START HERE. Provenance, counts, every session.
events.json                      Per-event summaries and counts.
topics.json                      Topic -> session ids across all years.
llms.txt                         llms.txt-format index.
schema/catalog.schema.json       JSON Schema for catalog.json.
schema/session.schema.json       JSON Schema for sessions/*/metadata.json.
sessions/<event>/<id>/
  metadata.json                  Structured: platforms, topics, keywords, code snippets,
                                 resources (with sosumi.ai + DocC endpoints), media, languages.
  README.md                      Rendered page with YAML frontmatter.
  transcript.md                  Timecoded transcript prose (when available).
  transcript.json                Machine transcript: {{ "segments": [{{ "start", "text" }}] }}.
events/<event>/index.md          Per-event sessions grouped by topic.
topics/<slug>.md                 Per-topic index across events.
platforms/<slug>.md              Per-platform index.
```

## Path templates

Every path is derivable from a session `id` (Apple's stable `wwdc<year>-<n>` form):

```
sessions/<event>/<id>/metadata.json
sessions/<event>/<id>/transcript.json
```

`<event>` is the `event` field on each catalog record (e.g. `wwdc2026`, `tech-talks`). Do not
guess paths — every catalog record carries an exact `path`, and each metadata.json carries a
`files` map.

## Recommended access patterns

1. **Whole map:** fetch `catalog.json`. Filter `sessions[]` by `year`, `event`, `topics`,
   `platforms`, `keywords`, or `hasTranscript`.
2. **One talk:** read `sessions/<event>/<id>/transcript.md` (prose) or `transcript.json`
   (`segments[]` with second-precise `start` times for citation).
3. **Structured detail:** `sessions/<event>/<id>/metadata.json` — code snippets carry full source;
   resources carry `url`, `sosumiURL`, and `doccJSON`.
4. **Apple docs behind a session:** prefer each resource's `sosumiURL` (clean Markdown). See below.
5. **Subject filtering:** `topics.json` / `topics/`, or the `keywords` array per session.

## Apple documentation as Markdown (Sosumi)

Apple's docs are JavaScript-rendered and mostly invisible to agents. To read any
`developer.apple.com` page as Markdown, swap the host to `sosumi.ai`:

- `https://developer.apple.com/documentation/swiftui/observable`
  -> `https://sosumi.ai/documentation/swiftui/observable`

Each resource in `metadata.json` precomputes this as `sosumiURL`, and every session has its own
`sosumiURL`. Sosumi also exposes an MCP server at `https://sosumi.ai/mcp`. It is an on-demand
renderer — fetch pages as needed; do not bulk-crawl it.

## Languages

Transcripts are materialized in English. Each session's `availableLanguages` lists every language
Apple publishes (e.g. `eng`, `zho`, `jpn`, `kor`, `spa`, `por`, `fra`); fetch other languages via
the session's `sosumiURL` or Apple's feed.

## Coverage

| Event | id | Sessions | Transcripts |
|---|---|---|---|
{rows}

## Raw fetch base

`{RAW_BASE}/<path>` — e.g. `{RAW_BASE}/catalog.json`.

## Provenance

All session content is © Apple Inc., sourced from Apple's public developer-video feeds. This index
is regenerated by `scripts/build.py` and validated by `scripts/validate.py`.
"""
    (ROOT / "AGENTS.md").write_text(content)


def write_readme(catalog):
    counts = catalog["counts"]
    content = f"""# WWDC Sessions — Agent-Native Knowledge Base

An **agent-native** index of Apple **WWDC** developer sessions (2014-2026, plus Tech Talks and Meet
with Apple): clean transcripts, structured metadata, inline code snippets, and links to the
documentation each session references. Built so AI agents (and humans) can consume WWDC content
without scraping JavaScript-rendered pages.

- **{counts['sessions']}** sessions across **{counts['events']}** events · **{counts['transcripts']}** with full transcripts
- Machine entrypoint: [`catalog.json`](catalog.json) · also [`events.json`](events.json) · [`topics.json`](topics.json) · [`llms.txt`](llms.txt)
- JSON Schemas: [`schema/`](schema/) · Agent guide: [`AGENTS.md`](AGENTS.md)
- Per session: `metadata.json`, `README.md`, `transcript.md`, `transcript.json`

## Quick start (agents)

```
GET catalog.json                                   # full index, filter by year/topic/platform
GET sessions/<event>/<id>/transcript.md            # the talk, timecoded
GET sessions/<event>/<id>/transcript.json          # {{ segments: [{{ start, text }}] }}
GET sessions/<event>/<id>/metadata.json            # structured + resource links
```

Each linked Apple doc includes a `sosumiURL` (clean Markdown) so an agent can fetch documentation
on demand. See [`AGENTS.md`](AGENTS.md) for path templates and conventions.

## Regenerate & validate

```
python3 scripts/build.py        # resolves Apple's rotating feeds dynamically
python3 scripts/validate.py     # checks catalog ↔ filesystem integrity
```

A scheduled GitHub Action refreshes the data and runs validation.

## Provenance & license

Session transcripts, metadata, and code snippets are **© Apple Inc.**, sourced from Apple's public
developer-video feeds for indexing and developer convenience. This project is free, non-commercial,
and complementary; every session links back to its source. The tooling in `scripts/` is MIT
licensed (see [LICENSE](LICENSE)).
"""
    (ROOT / "README.md").write_text(content)


def main():
    print("Resolving Apple feed URLs...")
    cfg = fetch_json(CONFIG_URL)
    feeds = cfg["feeds"]
    contents_url = feeds["en"]["contents"]["url"]
    language_manifest_urls = {lang: feeds[lang]["transcripts"]["url"] for lang in feeds}

    print("Fetching contents.json...")
    data = fetch_json(contents_url)
    topics_by_id = {t["id"]: t["title"] for t in data["topics"]}
    resources_by_id = {r["id"]: r for r in data["resources"]}
    events_by_id = {e["id"]: e for e in data["events"]}
    source_updated = data.get("updated")

    print(f"Fetching {len(language_manifest_urls)} language manifests...")
    languages_by_id, english_urls = {}, {}
    for lang, url in language_manifest_urls.items():
        individual = fetch_json(url).get("individual", {})
        for session_id in individual:
            languages_by_id.setdefault(session_id, set()).add("eng" if lang == "en" else lang)
        if lang == "en":
            english_urls = {sid: meta["url"] for sid, meta in individual.items()}

    included = [
        content for content in data["contents"]
        if is_session_event(content.get("eventId", ""))
        and (content.get("type") in INCLUDE_TYPES or content["id"] in languages_by_id)
    ]
    print(f"consumable sessions: {len(included)} across "
          f"{len({c['eventId'] for c in included})} events")

    transcript_targets = {c["id"]: english_urls[c["id"]] for c in included if c["id"] in english_urls}
    print(f"english transcripts to fetch: {len(transcript_targets)}")
    transcripts = {}

    def load(item):
        session_id, url = item
        try:
            return session_id, fetch_transcript_segments(url)
        except Exception as error:
            print(f"  transcript failed {session_id}: {error}")
            return session_id, None

    with ThreadPoolExecutor(max_workers=12) as pool:
        for session_id, segments in pool.map(load, transcript_targets.items()):
            if segments:
                transcripts[session_id] = segments
    print(f"transcripts fetched: {len(transcripts)}")

    sessions = [
        build_session(
            content, events_by_id[content["eventId"]], topics_by_id, resources_by_id,
            transcripts.get(content["id"], []),
            sorted(languages_by_id.get(content["id"], set())),
        )
        for content in included
    ]
    assign_paths(sessions)

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    for stale in ("sessions", "events", "topics", "platforms"):
        shutil.rmtree(ROOT / stale, ignore_errors=True)
    write_sessions(sessions, transcripts)
    catalog, event_summaries, by_event = write_catalog(
        sessions, list(events_by_id.values()), generated_at, source_updated)
    write_event_indexes(by_event, events_by_id)
    write_topic_indexes(sessions)
    write_platform_indexes(sessions)
    write_llms_txt(catalog, event_summaries)
    write_agents_md(catalog, event_summaries)
    write_readme(catalog)

    print("\nDONE")
    print(f"  events: {catalog['counts']['events']}")
    print(f"  sessions: {catalog['counts']['sessions']}")
    print(f"  transcripts: {catalog['counts']['transcripts']}")


if __name__ == "__main__":
    main()
