# WWDC26 Sessions — Agent-Native Knowledge Base

An **agent-native** index of every Apple **WWDC26** developer session: clean transcripts,
structured metadata, inline code snippets, and links to the official documentation each session
references. Built so that AI agents (and humans) can consume WWDC content without scraping
JavaScript-rendered pages.

- **116** sessions indexed · **112** with full transcripts
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
