#!/usr/bin/env python3
"""Generate the agent-native WWDC26 knowledge base from Apple's live WWDC feeds.

Run: python3 scripts/build.py
Output is written into the repository root: sessions/, topics/, platforms/,
catalog.json, topics.json, llms.txt, AGENTS.md, README.md.
"""
import gzip
import html
import json
import re
import shutil
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CONFIG_URL = "https://api2024.wwdc.io/config.json"
EVENT_ID = "wwdc2026"
EVENT_LABEL = "WWDC26"
INCLUDE_TYPES = {"Video", "Special Event", "Article"}
ROOT = Path(__file__).resolve().parent.parent
RAW_BASE = "https://raw.githubusercontent.com/guitaripod/wwdc26-sessions/master"


def fetch(url, attempts=4):
    """Fetch a URL with retry/backoff, transparently decompressing gzip responses."""
    req = urllib.request.Request(
        url, headers={"Accept-Encoding": "gzip", "User-Agent": "wwdc26-sessions/1.0"}
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


def resolve_feeds():
    """Resolve the current contents and English transcript feed URLs from Apple's rotating config."""
    cfg = fetch_json(CONFIG_URL)
    en = cfg["feeds"]["en"]
    return en["contents"]["url"], en["transcripts"]["url"]


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


def fetch_transcript_segments(url):
    """Return the list of [seconds, text] segments for a session transcript feed."""
    data = fetch_json(url)
    return next(iter(data.values())).get("transcript", [])


def render_transcript(segments, chunk_seconds=45):
    """Render transcript segments into timestamped markdown paragraphs."""
    if not segments:
        return ""
    paragraphs, buffer, start = [], [], segments[0][0]
    for timestamp, text in segments:
        if buffer and timestamp - start >= chunk_seconds:
            paragraphs.append((start, " ".join(buffer).strip()))
            buffer, start = [], timestamp
        buffer.append(text.strip())
    if buffer:
        paragraphs.append((start, " ".join(buffer).strip()))
    return "\n\n".join(f"**[{format_timestamp(ts)}]** {body}" for ts, body in paragraphs if body)


def resolve_resources(related, resources_by_id):
    """Resolve related-resource ids into structured link records with DocC JSON endpoints."""
    records = []
    for resource_id in (related or {}).get("resources", []):
        resource = resources_by_id.get(resource_id)
        if not resource:
            continue
        record = {
            "title": resource.get("title"),
            "url": resource.get("url"),
            "type": resource.get("resource_type"),
            "description": resource.get("description"),
        }
        sosumi = sosumi_url(resource.get("url", ""))
        if sosumi:
            record["sosumiURL"] = sosumi
        docc = docc_json_url(resource.get("url", ""))
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


def build_session(content, topics_by_id, resources_by_id, transcript_path):
    """Assemble a normalized metadata record for one session."""
    topic_ids = content.get("topicIds", [])
    return {
        "id": content["id"],
        "eventContentId": content.get("eventContentId"),
        "title": content.get("title"),
        "description": content.get("description"),
        "url": content.get("webPermalink"),
        "sosumiURL": sosumi_url(content.get("webPermalink")),
        "type": content.get("type"),
        "publishedAt": content.get("originalPublishingDate"),
        "platforms": content.get("platforms", []),
        "keywords": content.get("keywords", []),
        "topics": [topics_by_id.get(tid) for tid in topic_ids if tid in topics_by_id],
        "primaryTopic": topics_by_id.get(content.get("primaryTopicID")),
        "media": media_record(content.get("media")),
        "codeSnippets": clean_snippets(content.get("codeSnippets")),
        "resources": resolve_resources(content.get("related"), resources_by_id),
        "hasTranscript": transcript_path is not None,
        "transcript": transcript_path,
    }


def render_session_readme(session):
    """Render the human- and agent-readable session page."""
    lines = [f"# {session['title']}", ""]
    facts = []
    if session.get("primaryTopic"):
        facts.append(f"**Topic:** {session['primaryTopic']}")
    if session.get("platforms"):
        facts.append(f"**Platforms:** {', '.join(session['platforms'])}")
    if session.get("publishedAt"):
        facts.append(f"**Published:** {session['publishedAt'][:10]}")
    facts.append(f"**Session:** [{session['id']}]({session['url']})")
    lines.append(" · ".join(facts))
    lines.append("")
    if session.get("description"):
        lines += [session["description"], ""]
    if session.get("keywords"):
        lines += ["**Keywords:** " + ", ".join(f"`{kw}`" for kw in session["keywords"]), ""]

    if session.get("hasTranscript"):
        lines += ["## Transcript", "", "[Read the full transcript](transcript.md)", ""]

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
                if snippet.get("startTimeSeconds") is not None
                else ""
            )
            lines.append(f"### {snippet.get('title') or 'Snippet'}{stamp}")
            lines += ["", f"```{snippet.get('language', 'swift')}", snippet["code"].rstrip(), "```", ""]

    if session.get("media", {}).get("hls"):
        lines += ["## Video", "", f"- HLS stream: {session['media']['hls']}"]
        if session["media"].get("downloadHLS"):
            lines.append(f"- Download: {session['media']['downloadHLS']}")
        lines.append("")

    lines += ["---", "", "_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._"]
    return "\n".join(lines)


def write_sessions(sessions, transcripts):
    sessions_dir = ROOT / "sessions"
    for session in sessions:
        session_dir = sessions_dir / session["id"]
        session_dir.mkdir(parents=True, exist_ok=True)
        (session_dir / "metadata.json").write_text(json.dumps(session, indent=2, ensure_ascii=False))
        (session_dir / "README.md").write_text(render_session_readme(session))
        if session["id"] in transcripts:
            body = render_transcript(transcripts[session["id"]])
            page = f"# {session['title']} — Transcript\n\n[Session page]({session['url']}) · [Metadata](metadata.json)\n\n{body}\n"
            (session_dir / "transcript.md").write_text(page)


def write_catalog(sessions, event):
    catalog = {
        "event": event,
        "sessionCount": len(sessions),
        "transcriptCount": sum(1 for s in sessions if s["hasTranscript"]),
        "sessions": [
            {
                "id": s["id"],
                "title": s["title"],
                "url": s["url"],
                "type": s["type"],
                "platforms": s["platforms"],
                "topics": s["topics"],
                "primaryTopic": s["primaryTopic"],
                "keywords": s["keywords"],
                "hasTranscript": s["hasTranscript"],
                "resourceCount": len(s["resources"]),
                "path": f"sessions/{s['id']}/",
                "description": s["description"],
            }
            for s in sorted(sessions, key=lambda x: x["id"])
        ],
    }
    (ROOT / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False))
    return catalog


def write_topic_indexes(sessions):
    topics_dir = ROOT / "topics"
    topics_dir.mkdir(exist_ok=True)
    by_topic = {}
    for session in sessions:
        for topic in session["topics"]:
            by_topic.setdefault(topic, []).append(session)
    topics_manifest = []
    for topic in sorted(by_topic):
        slug = slugify(topic)
        rows = sorted(by_topic[topic], key=lambda s: s["title"] or "")
        lines = [f"# {topic} — {EVENT_LABEL} Sessions", "", f"{len(rows)} sessions.", ""]
        for session in rows:
            flag = " · 📝 transcript" if session["hasTranscript"] else ""
            lines.append(f"- [{session['title']}](../sessions/{session['id']}/README.md){flag}")
        (topics_dir / f"{slug}.md").write_text("\n".join(lines) + "\n")
        topics_manifest.append({"topic": topic, "slug": slug, "sessionCount": len(rows),
                                "sessionIds": [s["id"] for s in rows]})
    (ROOT / "topics.json").write_text(json.dumps(topics_manifest, indent=2, ensure_ascii=False))
    return by_topic


def write_platform_indexes(sessions):
    platforms_dir = ROOT / "platforms"
    platforms_dir.mkdir(exist_ok=True)
    by_platform = {}
    for session in sessions:
        for platform in session["platforms"]:
            by_platform.setdefault(platform, []).append(session)
    for platform in sorted(by_platform):
        rows = sorted(by_platform[platform], key=lambda s: s["title"] or "")
        lines = [f"# {platform} — {EVENT_LABEL} Sessions", "", f"{len(rows)} sessions.", ""]
        for session in rows:
            lines.append(f"- [{session['title']}](../sessions/{session['id']}/README.md)")
        (platforms_dir / f"{slugify(platform)}.md").write_text("\n".join(lines) + "\n")
    return by_platform


def write_llms_txt(catalog, by_topic):
    lines = [
        f"# {EVENT_LABEL} Sessions",
        "",
        "> Agent-native knowledge base of Apple WWDC26 developer sessions: clean transcripts, "
        "structured metadata, code snippets, and links to official documentation. "
        "Generated from Apple's public WWDC feeds.",
        "",
        f"{catalog['sessionCount']} sessions · {catalog['transcriptCount']} with transcripts. "
        "Start with catalog.json for the full machine-readable index. Each session lives at "
        "sessions/<id>/ with metadata.json, README.md, and transcript.md.",
        "",
        "## Index",
        "- [Full catalog (JSON)](catalog.json): every session with metadata, topics, and paths",
        "- [Topics manifest (JSON)](topics.json): sessions grouped by topic",
        "- [Agent guide](AGENTS.md): how to consume this repository",
        "",
    ]
    for topic in sorted(by_topic):
        lines.append(f"## {topic}")
        for session in sorted(by_topic[topic], key=lambda s: s["title"] or ""):
            summary = (session["description"] or "").split(". ")[0][:140]
            lines.append(f"- [{session['title']}](sessions/{session['id']}/README.md): {summary}")
        lines.append("")
    (ROOT / "llms.txt").write_text("\n".join(lines))


def write_agents_md(catalog):
    content = f"""# Agent Guide

This repository is a knowledge base of **Apple {EVENT_LABEL} (WWDC 2026)** developer sessions,
structured for direct consumption by AI agents. It is free, non-commercial, and complementary to
Apple's official material — every session links back to its source on developer.apple.com.

## How it is organized

```
catalog.json              Machine-readable index of all {catalog['sessionCount']} sessions (START HERE)
topics.json               Sessions grouped by Apple's {len(set(t for s in catalog['sessions'] for t in s['topics']))} topics
llms.txt                  llms.txt-format index with one-line summaries
sessions/<id>/
  metadata.json           Structured: title, description, platforms, keywords, topics,
                          code snippets, resources (with DocC JSON endpoints), media URLs
  README.md               Rendered session page (human + agent readable)
  transcript.md           Full timecoded transcript (present for {catalog['transcriptCount']} sessions)
topics/<slug>.md          Per-topic session lists
platforms/<slug>.md       Per-platform session lists
```

## Recommended access patterns

1. **Need the whole map?** Fetch `catalog.json`. Every entry has `id`, `title`, `topics`,
   `platforms`, `keywords`, `hasTranscript`, `resourceCount`, and `path`.
2. **Need one session's content?** Read `sessions/<id>/transcript.md` for the talk and
   `sessions/<id>/metadata.json` for everything structured.
3. **Need Apple's documentation behind a session?** Each resource in `metadata.json` carries the
   canonical `url` plus a `sosumiURL` (clean Markdown via sosumi.ai) and, for API reference, a
   `doccJSON` field. Prefer `sosumiURL` — it returns AI-readable Markdown instead of
   JavaScript-rendered HTML or raw render JSON.
4. **Filtering by subject?** Use `topics.json` / `topics/` or the `keywords` array on each session.

## Apple documentation as Markdown (Sosumi)

Apple's docs are JavaScript-rendered and mostly invisible to agents. To read any
`developer.apple.com` page as Markdown, swap the host to `sosumi.ai`:

- `https://developer.apple.com/documentation/swiftui/observable`
  -> `https://sosumi.ai/documentation/swiftui/observable`

Every session's `metadata.json` precomputes this as `sosumiURL` (per resource and for the session
itself). Sosumi also exposes an MCP server at `https://sosumi.ai/mcp` (search Apple docs; fetch
docs, HIG, and video transcripts). Sosumi is an on-demand renderer — fetch pages as needed; do not
bulk-crawl it.

## Raw fetch base

Files are fetchable raw at:
`{RAW_BASE}/<path>` — e.g. `{RAW_BASE}/catalog.json`.

## Provenance

All session content is © Apple Inc. and sourced from Apple's public WWDC feeds
(`developer.apple.com`). This index is regenerated by `scripts/build.py`.
"""
    (ROOT / "AGENTS.md").write_text(content)


def write_readme(catalog):
    content = f"""# {EVENT_LABEL} Sessions — Agent-Native Knowledge Base

An **agent-native** index of every Apple **WWDC26** developer session: clean transcripts,
structured metadata, inline code snippets, and links to the official documentation each session
references. Built so that AI agents (and humans) can consume WWDC content without scraping
JavaScript-rendered pages.

- **{catalog['sessionCount']}** sessions indexed · **{catalog['transcriptCount']}** with full transcripts
- Machine-readable [`catalog.json`](catalog.json) · [`topics.json`](topics.json) · [`llms.txt`](llms.txt)
- Per session: [`metadata.json`](sessions/), [`README.md`](sessions/), [`transcript.md`](sessions/)
- See [`AGENTS.md`](AGENTS.md) for how agents should navigate this repo

## Quick start (agents)

```
GET catalog.json                          # full index
GET sessions/<id>/transcript.md           # the talk, timecoded
GET sessions/<id>/metadata.json           # structured metadata + resource links
```

Each resource in a session's metadata includes a `doccJSON` endpoint when it links to Apple
documentation, so an agent can fetch machine-readable docs on demand.

## Regenerate

```
python3 scripts/build.py
```

The build resolves Apple's rotating feed URLs dynamically from `api2024.wwdc.io/config.json`,
so it keeps working as Apple rotates CDN paths. A scheduled GitHub Action refreshes the data.

## Provenance & license

Session transcripts, metadata, and code snippets are **© Apple Inc.**, sourced from Apple's public
WWDC feeds for indexing and developer convenience. This project is free, non-commercial, and
complementary to Apple's official material; every session links back to its source. The tooling in
`scripts/` is released under the MIT License (see [LICENSE](LICENSE)).
"""
    (ROOT / "README.md").write_text(content)


def main():
    print("Resolving Apple feed URLs...")
    contents_url, transcripts_url = resolve_feeds()
    print("Fetching contents.json...")
    data = fetch_json(contents_url)
    topics_by_id = {t["id"]: t["title"] for t in data["topics"]}
    resources_by_id = {r["id"]: r for r in data["resources"]}
    events_by_id = {e["id"]: e for e in data["events"]}

    print("Fetching transcript manifest...")
    manifest = fetch_json(transcripts_url).get("individual", {})
    event_items = [c for c in data["contents"] if c.get("eventId") == EVENT_ID]
    contents = [c for c in event_items if c.get("type") in INCLUDE_TYPES or c["id"] in manifest]
    print(f"{EVENT_ID} items: {len(event_items)}; consumable: {len(contents)}")
    wanted = {c["id"]: manifest[c["id"]]["url"] for c in contents if c["id"] in manifest}
    print(f"transcripts available: {len(wanted)}")

    transcripts = {}

    def load(item):
        session_id, url = item
        try:
            return session_id, fetch_transcript_segments(url)
        except Exception as error:
            print(f"  transcript failed {session_id}: {error}")
            return session_id, None

    with ThreadPoolExecutor(max_workers=12) as pool:
        for session_id, segments in pool.map(load, wanted.items()):
            if segments:
                transcripts[session_id] = segments
    print(f"transcripts fetched: {len(transcripts)}")

    sessions = [
        build_session(c, topics_by_id, resources_by_id,
                      "transcript.md" if c["id"] in transcripts else None)
        for c in contents
    ]

    event = events_by_id.get(EVENT_ID, {"id": EVENT_ID, "name": EVENT_LABEL})
    for stale in ("sessions", "topics", "platforms"):
        shutil.rmtree(ROOT / stale, ignore_errors=True)
    write_sessions(sessions, transcripts)
    catalog = write_catalog(sessions, {"id": event.get("id"), "name": event.get("name"),
                                       "startTime": event.get("startTime"), "endTime": event.get("endTime")})
    by_topic = write_topic_indexes(sessions)
    write_platform_indexes(sessions)
    write_llms_txt(catalog, by_topic)
    write_agents_md(catalog)
    write_readme(catalog)

    types = {}
    for session in sessions:
        types[session["type"]] = types.get(session["type"], 0) + 1
    print("\nDONE")
    print(f"  sessions: {len(sessions)}  by type: {types}")
    print(f"  transcripts: {len(transcripts)}")
    print(f"  topics: {len(by_topic)}")


if __name__ == "__main__":
    main()
