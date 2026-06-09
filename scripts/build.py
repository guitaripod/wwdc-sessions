#!/usr/bin/env python3
"""Generate the agent-native WWDC knowledge base from Apple's live developer-video feeds.

Covers every scrapable event (WWDC 2014-2026, Tech Talks, Meet with Apple). Output is a
flat, self-describing corpus designed for direct consumption by AI agents.

Run: python3 scripts/build.py [--force]
  --force rebuilds even when Apple's feed is unchanged since the last build.
"""
import gzip
import html
import json
import re
import shutil
import sys
import textwrap
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

CONFIG_URL = "https://api2024.wwdc.io/config.json"
ROOT = Path(__file__).resolve().parent.parent
REPO = "guitaripod/wwdc-sessions"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/master"
SCHEMA_VERSION = 1
BUILDER_VERSION = 2
TRANSCRIPT_FLOOR = 1400
EXTRA_EVENTS = {"tech-talks", "meet-with-apple"}
INCLUDE_TYPES = {"Video", "Special Event", "Article", "Session"}


def fetch(url, attempts=4):
    """Fetch a URL with retry/backoff, transparently decompressing gzip responses.

    Retries transient failures; does not retry 4xx other than 429, and honors Retry-After.
    """
    req = urllib.request.Request(
        url, headers={"Accept-Encoding": "gzip", "User-Agent": "wwdc-sessions/2.0"}
    )
    for attempt in range(attempts):
        try:
            data = urllib.request.urlopen(req, timeout=90).read()
            return gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data
        except urllib.error.HTTPError as error:
            retryable = error.code == 429 or error.code >= 500
            if not retryable or attempt == attempts - 1:
                raise
            delay = float(error.headers.get("Retry-After") or 0) or 1.5 * (attempt + 1)
            time.sleep(delay + 0.3 * attempt)
        except Exception:
            if attempt == attempts - 1:
                raise
            time.sleep(1.5 * (attempt + 1) + 0.3 * attempt)
    raise RuntimeError(f"unreachable: fetch exhausted retries for {url}")


def fetch_json(url):
    return json.loads(fetch(url))


def write_json(path, obj, compact=False):
    """Serialize JSON with a trailing newline (POSIX text files)."""
    text = json.dumps(obj, ensure_ascii=False) if compact else json.dumps(obj, indent=2, ensure_ascii=False)
    path.write_text(text + "\n")


def is_session_event(event_id):
    """Whether an event holds developer sessions worth indexing."""
    return bool(re.match(r"^wwdc\d{4}$", event_id)) or event_id in EXTRA_EVENTS


def event_year(event):
    """Calendar year for an event, used for event-level summaries."""
    match = re.match(r"^wwdc(\d{4})$", event["id"])
    if match:
        return int(match.group(1))
    start = event.get("startTime") or ""
    return int(start[:4]) if start[:4].isdigit() else None


def session_year(content, event):
    """Year for an individual session: its publishing year for multi-year events, else the event year."""
    match = re.match(r"^wwdc(\d{4})$", event["id"])
    if match:
        return int(match.group(1))
    published = content.get("originalPublishingDate") or ""
    if published[:4].isdigit():
        return int(published[:4])
    return event_year(event)


def clean_text(value):
    """Unescape HTML entities and collapse whitespace in prose; return None when empty."""
    if not value:
        return None
    return re.sub(r"\s+", " ", html.unescape(value)).strip() or None


def strip_html(text):
    """Convert Apple's HTML-highlighted code spans into plain source text.

    Handles double-escaped entities (e.g. `&amp;lt;`) that survive a single unescape, while
    leaving lone ampersands (address-of, `&copy`) untouched.
    """
    stripped = re.sub(r"<[^>]+>", "", text or "")
    stripped = re.sub(r"&amp;(lt|gt|quot|nbsp|amp|#x?[0-9A-Fa-f]+);", r"&\1;", stripped)
    return html.unescape(stripped)


def normalize_code(raw):
    """Render a code snippet as plain source: strip HTML, remove zero-width spaces, dedent.

    Uses textwrap.dedent, which removes only the common leading whitespace and therefore never
    flattens relative nesting. U+200C/U+200D (ZWNJ/ZWJ) are preserved — they are load-bearing
    inside emoji grapheme clusters in some samples.
    """
    text = strip_html(raw).replace("​", "").replace("﻿", "")
    return textwrap.dedent(text).rstrip()


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


def with_scheme(url):
    """Ensure a resource URL is absolute so it never renders as a relative repo link."""
    if url and not re.match(r"^(https?://|mailto:)", url, re.I):
        return "https://" + url
    return url


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
    text = (str(value).replace("\\", "\\\\").replace('"', '\\"')
            .replace("\n", " ").replace("\r", " ").replace("\t", " "))
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
    """Return cleaned [{start, text}] segments for a transcript feed entry."""
    data = fetch_json(url)
    raw = next(iter(data.values())).get("transcript", [])
    segments = []
    for timestamp, text in raw:
        cleaned = re.sub(r"\s+", " ", html.unescape(text)).strip()
        if cleaned:
            segments.append({"start": round(float(timestamp), 3), "text": cleaned})
    return segments


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
        url = with_scheme(resource.get("url", "") or "")
        record = {
            "title": clean_text(resource.get("title")),
            "url": url,
            "type": resource.get("resource_type"),
            "description": clean_text(resource.get("description")),
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
            "title": clean_text(snippet.get("title")),
            "language": snippet.get("language", "swift"),
            "startTimeSeconds": snippet.get("startTimeSeconds"),
            "code": normalize_code(snippet.get("code", "")),
        }
        for snippet in snippets or []
    ]


def media_record(media):
    keys = ["hls", "downloadHLS", "downloadSD", "downloadHD", "duration", "tnsURL"]
    return {key: media[key] for key in keys if key in (media or {})}


def normalized_type(raw_type):
    """Collapse Apple's legacy `Session` label into `Video` so type filtering is era-consistent."""
    return "Video" if raw_type in {"Session", "Video"} else raw_type


def build_session(content, event, topics_by_id, resources_by_id, segments, languages):
    """Assemble a normalized, richly structured record for one session."""
    media = media_record(content.get("media"))
    duration = media.get("duration")
    if not duration and segments:
        duration = int(segments[-1]["start"])
    word_count = sum(len(s["text"].split()) for s in segments) if segments else 0
    return {
        "schemaVersion": SCHEMA_VERSION,
        "id": content["id"],
        "event": content.get("eventId"),
        "eventName": event.get("name"),
        "year": session_year(content, event),
        "eventContentId": content.get("eventContentId"),
        "title": clean_text(content.get("title")),
        "description": clean_text(content.get("description")),
        "url": content.get("webPermalink"),
        "sosumiURL": sosumi_url(content.get("webPermalink")),
        "type": normalized_type(content.get("type")),
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
    """Assign each session a stable, readable repo path: sessions/<event>/<eventContentId>-<title-slug>/.

    The numeric prefix is Apple's stable session id (mirroring developer.apple.com/videos/play/<event>/<n>
    and guaranteeing uniqueness); the slug makes the path human- and agent-readable. Falls back to the
    full id when eventContentId is missing or collides.
    """
    counts = {}
    for session in sessions:
        counts[(session["event"], session.get("eventContentId"))] = (
            counts.get((session["event"], session.get("eventContentId")), 0) + 1)
    seen = set()
    for session in sessions:
        ecid = session.get("eventContentId")
        unique = ecid is not None and counts[(session["event"], ecid)] == 1
        stem = str(ecid) if unique else session["id"]
        slug = slugify(session["title"])[:60].rstrip("-")
        leaf = f"{stem}-{slug}" if slug else stem
        session["path"] = f"sessions/{session['event']}/{leaf}/"
        if session["path"] in seen:
            raise RuntimeError(f"path collision: {session['path']}")
        seen.add(session["path"])
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
        "id": session["id"], "event": session["event"], "year": session["year"],
        "title": session["title"], "type": session["type"], "url": session["url"],
        "topics": session["topics"], "platforms": session["platforms"],
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
    return "\n".join(lines) + "\n"


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
    session_schema = f"{RAW_BASE}/schema/session.schema.json"
    transcript_schema = f"{RAW_BASE}/schema/transcript.schema.json"
    for session in sessions:
        session_dir = ROOT / session["path"]
        session_dir.mkdir(parents=True, exist_ok=True)
        write_json(session_dir / "metadata.json", {"$schema": session_schema, **session})
        (session_dir / "README.md").write_text(render_session_readme(session))
        if session["hasTranscript"]:
            segments = transcripts[session["id"]]
            (session_dir / "transcript.md").write_text(render_transcript_markdown_page(session, segments))
            write_json(session_dir / "transcript.json", {
                "$schema": transcript_schema, "id": session["id"], "language": "eng",
                "source": session["url"], "wordCount": session["transcriptWordCount"],
                "segments": segments,
            }, compact=True)


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


def event_summaries(sessions, events):
    by_event = {}
    for session in sessions:
        by_event.setdefault(session["event"], []).append(session)
    summaries = [
        {
            "id": event["id"], "name": event.get("name"), "year": event_year(event),
            "startTime": event.get("startTime"),
            "sessionCount": len(by_event.get(event["id"], [])),
            "transcriptCount": sum(1 for s in by_event.get(event["id"], []) if s["hasTranscript"]),
            "index": f"events/{event['id']}/index.md",
            "indexJSON": f"events/{event['id']}/index.json",
        }
        for event in sorted(events, key=lambda e: (event_year(e) or 0, e["id"]), reverse=True)
        if by_event.get(event["id"])
    ]
    return summaries, by_event


def write_catalog(sessions, summaries, generated_at, source_updated):
    catalog = {
        "$schema": f"{RAW_BASE}/schema/catalog.schema.json",
        "schemaVersion": SCHEMA_VERSION,
        "builderVersion": BUILDER_VERSION,
        "generatedAt": generated_at,
        "sourceUpdated": source_updated,
        "source": "Apple WWDC developer-video feeds (resolved via api2024.wwdc.io)",
        "rawBase": RAW_BASE,
        "license": "Content © Apple Inc. Tooling under MIT (see LICENSE/NOTICE).",
        "counts": {
            "events": len(summaries),
            "sessions": len(sessions),
            "transcripts": sum(1 for s in sessions if s["hasTranscript"]),
        },
        "links": {
            "events": "events.json", "topics": "topics.json", "agents": "AGENTS.md",
            "catalogSchema": "schema/catalog.schema.json", "sessionSchema": "schema/session.schema.json",
            "eventsSchema": "schema/events.schema.json", "topicsSchema": "schema/topics.schema.json",
            "transcriptSchema": "schema/transcript.schema.json",
        },
        "events": summaries,
        "sessions": [catalog_record(s) for s in
                     sorted(sessions, key=lambda s: (-(s["year"] or 0), s["event"], s["id"]))],
    }
    write_json(ROOT / "catalog.json", catalog)
    write_json(ROOT / "events.json", {
        "$schema": f"{RAW_BASE}/schema/events.schema.json",
        "schemaVersion": SCHEMA_VERSION, "generatedAt": generated_at, "events": summaries,
    })
    return catalog


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
        (events_dir / event_id / "index.md").write_text("\n".join(lines) + "\n")
        write_json(events_dir / event_id / "index.json", {
            "event": event_id, "name": event.get("name"), "year": event_year(event),
            "sessionCount": len(rows),
            "sessions": [catalog_record(s) for s in sorted(rows, key=lambda s: s["id"])],
        })


def write_topic_indexes(sessions):
    topics_dir = ROOT / "topics"
    topics_dir.mkdir(exist_ok=True)
    by_topic = {}
    for session in sessions:
        for topic in session["topics"]:
            by_topic.setdefault(topic, []).append(session)
    manifest = []
    for topic in sorted(by_topic):
        rows = sorted(by_topic[topic], key=lambda s: (-(s["year"] or 0), s["event"], s["title"] or ""))
        lines = [f"# {topic}", "", f"{len(rows)} sessions across all events.", ""]
        current_event = None
        for session in rows:
            if session["event"] != current_event:
                current_event = session["event"]
                lines += ["", f"### {session['eventName'] or session['event']}", ""]
            lines.append(f"- [{session['title']}]({relative_path(session, 1)})")
        (topics_dir / f"{slugify(topic)}.md").write_text("\n".join(lines) + "\n")
        manifest.append({
            "topic": topic, "slug": slugify(topic), "sessionCount": len(rows),
            "sessions": [{"id": s["id"], "path": s["path"], "title": s["title"],
                          "event": s["event"], "hasTranscript": s["hasTranscript"]} for s in rows],
        })
    write_json(ROOT / "topics.json", {
        "$schema": f"{RAW_BASE}/schema/topics.schema.json",
        "schemaVersion": SCHEMA_VERSION, "topics": manifest,
    })
    return by_topic


def write_platform_indexes(sessions):
    platforms_dir = ROOT / "platforms"
    platforms_dir.mkdir(exist_ok=True)
    by_platform = {}
    for session in sessions:
        for platform in session["platforms"]:
            by_platform.setdefault(platform, []).append(session)
    for platform in sorted(by_platform):
        rows = sorted(by_platform[platform], key=lambda s: (-(s["year"] or 0), s["event"], s["title"] or ""))
        lines = [f"# {platform} Sessions", "", f"{len(rows)} sessions.", ""]
        for session in rows:
            lines.append(f"- [{session['title']}]({relative_path(session, 1)}) — {session['eventName']}")
        (platforms_dir / f"{slugify(platform)}.md").write_text("\n".join(lines) + "\n")


def write_llms_txt(catalog):
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
        "one record per session, each carrying an exact `path` (e.g. "
        "sessions/wwdc2026/298-meet-the-evaluations-framework/). Read `path` + filename to fetch a "
        "session's metadata.json, README.md, transcript.md, or transcript.json — do not derive paths "
        "from the id.",
        "",
        "## Start here",
        "- [Master catalog (JSON)](catalog.json): every session, with provenance, counts, and `rawBase`",
        "- [Events (JSON)](events.json): per-event summaries; each event also has events/<id>/index.json",
        "- [Topics (JSON)](topics.json): sessions grouped by topic across years",
        "- [Agent guide](AGENTS.md): access patterns, conventions, sosumi docs",
        "- [Schemas](schema/): catalog, session, events, topics, transcript",
        "",
        "## Events",
    ]
    for event in catalog["events"]:
        lines.append(f"- [{event['name']}](events/{event['id']}/index.md): "
                     f"{event['sessionCount']} sessions, {event['transcriptCount']} transcripts")
    (ROOT / "llms.txt").write_text("\n".join(lines) + "\n")


def write_agents_md(catalog):
    counts = catalog["counts"]
    topic_count = len({t for s in catalog["sessions"] for t in s["topics"]})
    rows = "\n".join(
        f"| {e['name']} | {e['id']} | {e['sessionCount']} | {e['transcriptCount']} |"
        for e in catalog["events"])
    content = f"""# Agent Guide

A knowledge base of **Apple WWDC developer sessions** (WWDC 2014-2026, plus Tech Talks and Meet
with Apple), structured for direct consumption by AI agents. Free, non-commercial, and
complementary to Apple's official material — every session links back to developer.apple.com.

**{counts['sessions']} sessions · {counts['transcripts']} transcripts · {counts['events']} events ·
{topic_count} topics.**

## Layout

```
catalog.json                     Master index — START HERE. Provenance, counts, rawBase, every session.
events.json                      Per-event summaries and counts.
topics.json                      Topic -> sessions (id, path, title) across all years.
llms.txt                         llms.txt-format index.
schema/                          JSON Schema for catalog, session, events, topics, transcript.
sessions/<event>/<n>-<title-slug>/
  metadata.json                  Structured: platforms, topics, keywords, code snippets,
                                 resources (with sosumi.ai + DocC endpoints), media, languages.
  README.md                      Rendered page with YAML frontmatter.
  transcript.md                  Timecoded transcript prose (when available).
  transcript.json                {{ id, language, source, wordCount, segments:[{{start, text}}] }}.
events/<event>/index.md          Per-event sessions grouped by topic.
events/<event>/index.json        Per-event machine slice (full records) — fetch one year without the full catalog.
topics/<slug>.md                 Per-topic index across events.
platforms/<slug>.md              Per-platform index.
```

## Locating a session — do not derive paths from the id

Every catalog/events record carries an exact relative `path` (e.g.
`sessions/wwdc2026/298-meet-the-evaluations-framework/`); the leaf is `<eventContentId>-<title-slug>`.
To fetch a file, join the catalog's `rawBase` with `path` + filename:

```
<rawBase>/<path>metadata.json
<rawBase>/<path>transcript.json
```

`metadata.json` also carries a `files` map with every relative file path. The numeric prefix of the
leaf is Apple's stable session id, mirroring the video URL `developer.apple.com/videos/play/<event>/<n>`.

## Recommended access patterns

1. **Whole map:** fetch `catalog.json`. Filter `sessions[]` by `year`, `event`, `topics`,
   `platforms`, `keywords`, or `hasTranscript`.
2. **One year/topic without the full catalog:** `events/<event>/index.json` or `topics.json`.
3. **One talk:** read `<path>transcript.md` (prose) or `transcript.json` (`segments[]` with
   second-precise `start` times for citation; `source` is the canonical Apple URL).
4. **Structured detail:** `<path>metadata.json` — code snippets carry full source; resources carry
   `url`, `sosumiURL`, and `doccJSON`.
5. **Apple docs behind a session:** prefer each resource's `sosumiURL` (clean Markdown). See below.

## Apple documentation as Markdown (Sosumi)

Apple's docs are JavaScript-rendered and mostly invisible to agents. To read any
`developer.apple.com` page as Markdown, swap the host to `sosumi.ai`:

- `https://developer.apple.com/documentation/swiftui/state`
  -> `https://sosumi.ai/documentation/swiftui/state`

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

`rawBase` in catalog.json = `{RAW_BASE}`. Join as `{RAW_BASE}/<path>`.

## Provenance

All session content is © Apple Inc., sourced from Apple's public developer-video feeds. This index
is regenerated by `scripts/build.py` and validated by `scripts/validate.py`. WWDC and Apple are
trademarks of Apple Inc.; this project is an independent index and is not affiliated with,
authorized, or endorsed by Apple Inc.
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
GET catalog.json                                   # full index; has rawBase + a `path` per session
GET <rawBase>/<path>transcript.md                  # the talk, timecoded
GET <rawBase>/<path>transcript.json                # {{ id, language, source, wordCount, segments:[{{start,text}}] }}
GET <rawBase>/<path>metadata.json                  # structured + resource links
```

Each linked Apple doc includes a `sosumiURL` (clean Markdown) so an agent can fetch documentation
on demand. See [`AGENTS.md`](AGENTS.md) for path/locator conventions.

## Regenerate & validate

```
python3 scripts/build.py        # resolves Apple's rotating feeds dynamically; skips if unchanged (--force to override)
pip install -r requirements.txt
python3 scripts/validate.py     # catalog <-> filesystem integrity + JSON Schema validation
```

A scheduled GitHub Action refreshes the data and runs validation.

## Provenance & license

Session transcripts, metadata, and code snippets are **© Apple Inc.**, sourced from Apple's public
developer-video feeds for indexing and developer convenience. This project is free, non-commercial,
and complementary; every session links back to its source. WWDC and Apple are trademarks of Apple
Inc.; this is an independent index, not affiliated with or endorsed by Apple. The tooling in
`scripts/` is MIT licensed (see [LICENSE](LICENSE) and [NOTICE](NOTICE)).
"""
    (ROOT / "README.md").write_text(content)


def load_existing_catalog():
    path = ROOT / "catalog.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def main():
    force = "--force" in sys.argv
    print("Resolving Apple feed URLs...")
    cfg = fetch_json(CONFIG_URL)
    feeds = cfg["feeds"]

    print("Fetching contents.json...")
    data = fetch_json(feeds["en"]["contents"]["url"])
    source_updated = data.get("updated")

    existing = load_existing_catalog()
    if (existing and not force
            and existing.get("sourceUpdated") == source_updated
            and existing.get("builderVersion") == BUILDER_VERSION):
        print("No change since last build (use --force to rebuild). Skipping.")
        return

    topics_by_id = {t["id"]: t["title"] for t in data["topics"]}
    resources_by_id = {r["id"]: r for r in data["resources"]}
    events_by_id = {e["id"]: e for e in data["events"]}

    print(f"Fetching {len(feeds)} language manifests...")
    languages_by_id, english_urls = {}, {}
    for lang in feeds:
        url = feeds[lang]["transcripts"]["url"]
        try:
            individual = fetch_json(url).get("individual", {})
        except Exception as error:
            if lang == "en":
                raise RuntimeError(f"english transcript manifest is load-bearing and failed: {error}")
            print(f"  warning: {lang} manifest failed ({error}); continuing")
            continue
        for session_id in individual:
            languages_by_id.setdefault(session_id, set()).add("eng" if lang == "en" else lang)
        if lang == "en":
            english_urls = {sid: meta["url"] for sid, meta in individual.items()}
    if not english_urls:
        raise RuntimeError("english transcript manifest empty — refusing to wipe transcripts")

    included = [
        content for content in data["contents"]
        if content.get("id") and content.get("eventId") in events_by_id
        and is_session_event(content["eventId"])
        and content.get("webPermalink") and clean_text(content.get("title"))
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

    transcript_total = sum(1 for s in sessions if s["hasTranscript"])
    if transcript_total < TRANSCRIPT_FLOOR:
        raise RuntimeError(f"transcript count {transcript_total} below floor {TRANSCRIPT_FLOOR}; aborting")
    if existing:
        prev = existing.get("counts", {})
        for key, value in (("sessions", len(sessions)), ("transcripts", transcript_total)):
            if prev.get(key) and value < prev[key] * 0.9:
                raise RuntimeError(f"{key} dropped {prev[key]} -> {value} (>10%); aborting")

    summaries, by_event = event_summaries(sessions, list(events_by_id.values()))
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    for stale in ("sessions", "events", "topics", "platforms"):
        shutil.rmtree(ROOT / stale, ignore_errors=True)
    write_sessions(sessions, transcripts)
    catalog = write_catalog(sessions, summaries, generated_at, source_updated)
    write_event_indexes(by_event, events_by_id)
    write_topic_indexes(sessions)
    write_platform_indexes(sessions)
    write_llms_txt(catalog)
    write_agents_md(catalog)
    write_readme(catalog)

    print("\nDONE")
    print(f"  events: {catalog['counts']['events']}")
    print(f"  sessions: {catalog['counts']['sessions']}")
    print(f"  transcripts: {catalog['counts']['transcripts']}")


if __name__ == "__main__":
    main()
