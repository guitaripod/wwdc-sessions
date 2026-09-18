# WWDC Sessions — Agent-Native Knowledge Base

[![sessions](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fguitaripod%2Fwwdc-sessions%2Fmaster%2Fcatalog.json&query=%24.counts.sessions&label=sessions&color=007aff&style=flat-square)](catalog.json) [![transcripts](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fguitaripod%2Fwwdc-sessions%2Fmaster%2Fcatalog.json&query=%24.counts.transcripts&label=transcripts&color=34c759&style=flat-square)](catalog.json) [![events](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fguitaripod%2Fwwdc-sessions%2Fmaster%2Fcatalog.json&query=%24.counts.events&label=events&color=5856d6&style=flat-square)](catalog.json) [![updated](https://img.shields.io/github/last-commit/guitaripod/wwdc-sessions/master?label=updated&color=8e8e93&style=flat-square)](https://github.com/guitaripod/wwdc-sessions/commits/master)

An **agent-native** index of Apple **WWDC** developer sessions (2014 onward, plus Tech Talks and
Meet with Apple): clean transcripts, structured metadata, inline code snippets, and links to the
documentation each session references. Built so AI agents (and humans) can consume WWDC content
without scraping JavaScript-rendered pages.

- Every session Apple publishes, all the way back to WWDC14, almost all of them with a full
  transcript. A scheduled build picks up new events as Apple posts them; per-event coverage lives
  in [`AGENTS.md`](AGENTS.md).
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
pip install -r requirements.txt
python3 scripts/build.py        # resolves Apple's rotating feeds dynamically; skips if unchanged (--force to override)
python3 scripts/validate.py     # catalog <-> filesystem integrity + JSON Schema validation
```

A scheduled GitHub Action refreshes the data and runs validation.

## Provenance & license

Session transcripts, metadata, and code snippets are **© Apple Inc.**, sourced from Apple's public
developer-video feeds for indexing and developer convenience. This project is free, non-commercial,
and complementary; every session links back to its source. WWDC and Apple are trademarks of Apple
Inc.; this is an independent index, not affiliated with or endorsed by Apple. The tooling in
`scripts/` is MIT licensed (see [LICENSE](LICENSE) and [NOTICE](NOTICE)).
