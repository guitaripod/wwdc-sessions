# Contributing

Almost everything in this repository is **generated** and will be overwritten on
the next build. Do not edit generated artifacts by hand:

- `sessions/`, `events/`, `topics/`, `platforms/`
- `catalog.json`, `events.json`, `topics.json`, `llms.txt`, `AGENTS.md`, `README.md`

Edit only:

- `scripts/build.py` — the generator
- `scripts/validate.py` — the integrity/schema checker
- `schema/*.schema.json` — the machine contracts
- `LICENSE`, `NOTICE`, `CONTRIBUTING.md`, `.gitattributes`, `.github/`

## Workflow

```
pip install -r requirements.txt
python3 scripts/build.py --force   # regenerate from Apple's live feeds
python3 scripts/validate.py        # must pass before committing
```

`build.py` resolves Apple's rotating feed URLs dynamically and skips work when the
upstream feed is unchanged (override with `--force`). Bump `BUILDER_VERSION` in
`build.py` whenever the output format changes so the next scheduled run rebuilds.

All indexed content is © Apple Inc.; see [NOTICE](NOTICE).
