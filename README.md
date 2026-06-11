# WWDC Sessions — Agent-Native Knowledge Base

An **agent-native** index of Apple **WWDC** developer sessions (2014-2026, plus Tech Talks and Meet
with Apple): clean transcripts, structured metadata, inline code snippets, and links to the
documentation each session references. Built so AI agents (and humans) can consume WWDC content
without scraping JavaScript-rendered pages.

- **1616** sessions across **15** events · **1528** with full transcripts
- Machine entrypoint: [`catalog.json`](catalog.json) · also [`events.json`](events.json) · [`topics.json`](topics.json) · [`llms.txt`](llms.txt)
- JSON Schemas: [`schema/`](schema/) · Agent guide: [`AGENTS.md`](AGENTS.md)
- Per session: `metadata.json`, `README.md`, `transcript.md`, `transcript.json`

## Quick start (agents)

```
GET catalog.json                                   # full index; has rawBase + a `path` per session
GET <rawBase>/<path>transcript.md                  # the talk, timecoded
GET <rawBase>/<path>transcript.json                # { id, language, source, wordCount, segments:[{start,text}] }
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
