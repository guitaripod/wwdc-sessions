#!/usr/bin/env python3
"""Validate the WWDC sessions knowledge base — gates CI.

Checks (exits non-zero on any failure):
  - catalog <-> filesystem integrity (every record's files exist and parse)
  - a transcript floor, so a feed outage cannot commit a mass-wipe
  - catalog summary <-> metadata drift (shared scalars and derived counts agree)
  - JSON Schema conformance of catalog.json, every metadata.json, events.json, topics.json,
    and every transcript.json (skipped with a warning if `jsonschema` is not installed)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPT_FLOOR = 1400
SESSION_REQUIRED = {"schemaVersion", "id", "event", "title", "url", "hasTranscript", "path", "files"}
DRIFT_FIELDS = ("event", "title", "url", "path", "hasTranscript", "duration", "year")


def load_json(path):
    return json.loads(path.read_text())


def load_validators():
    """Return {name: validator} for each schema, or {} if jsonschema is unavailable."""
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        print("  warning: jsonschema not installed — skipping schema validation (pip install -r requirements.txt)")
        return {}
    validators = {}
    for name in ("catalog", "session", "events", "topics", "transcript"):
        schema = load_json(ROOT / "schema" / f"{name}.schema.json")
        validators[name] = Draft202012Validator(schema)
    return validators


def schema_errors(validator, instance, label):
    return [f"{label}: schema: {e.json_path}: {e.message}" for e in validator.iter_errors(instance)]


def main():
    errors = []
    validators = load_validators()

    catalog = load_json(ROOT / "catalog.json")
    sessions = catalog["sessions"]
    summary_by_id = {s["id"]: s for s in sessions}

    if catalog["counts"]["sessions"] != len(sessions):
        errors.append(f"counts.sessions {catalog['counts']['sessions']} != {len(sessions)} records")
    declared_transcripts = sum(1 for s in sessions if s["hasTranscript"])
    if catalog["counts"]["transcripts"] != declared_transcripts:
        errors.append(f"counts.transcripts {catalog['counts']['transcripts']} != {declared_transcripts}")
    if declared_transcripts < TRANSCRIPT_FLOOR:
        errors.append(f"transcript count {declared_transcripts} below floor {TRANSCRIPT_FLOOR} — possible wipe")

    if len(summary_by_id) != len(sessions):
        errors.append("duplicate session ids in catalog")
    if len({s["path"] for s in sessions}) != len(sessions):
        errors.append("duplicate session paths in catalog")

    if validators:
        errors += schema_errors(validators["catalog"], catalog, "catalog.json")
        for name in ("events", "topics"):
            errors += schema_errors(validators[name], load_json(ROOT / f"{name}.json"), f"{name}.json")

    for summary in sessions:
        directory = ROOT / summary["path"]
        meta_path = directory / "metadata.json"
        if not meta_path.exists():
            errors.append(f"{summary['id']}: missing {meta_path}")
            continue
        try:
            meta = load_json(meta_path)
        except Exception as error:
            errors.append(f"{summary['id']}: metadata.json invalid JSON ({error})")
            continue
        missing = SESSION_REQUIRED - meta.keys()
        if missing:
            errors.append(f"{summary['id']}: metadata missing keys {sorted(missing)}")
        if validators:
            errors += schema_errors(validators["session"], meta, f"{summary['id']}/metadata.json")
        for field in DRIFT_FIELDS:
            if meta.get(field) != summary.get(field):
                errors.append(f"{summary['id']}: drift on '{field}' (catalog={summary.get(field)!r} meta={meta.get(field)!r})")
        if summary.get("resourceCount") != len(meta.get("resources", [])):
            errors.append(f"{summary['id']}: resourceCount drift")
        if summary.get("codeSnippetCount") != len(meta.get("codeSnippets", [])):
            errors.append(f"{summary['id']}: codeSnippetCount drift")
        if not (directory / "README.md").exists():
            errors.append(f"{summary['id']}: missing README.md")
        if summary["hasTranscript"]:
            for name in ("transcript.md", "transcript.json"):
                if not (directory / name).exists():
                    errors.append(f"{summary['id']}: hasTranscript but missing {name}")
            tjson = directory / "transcript.json"
            if tjson.exists():
                try:
                    transcript = load_json(tjson)
                    if not transcript.get("segments"):
                        errors.append(f"{summary['id']}: transcript.json has no segments")
                    elif validators:
                        errors += schema_errors(validators["transcript"], transcript, f"{summary['id']}/transcript.json")
                except Exception as error:
                    errors.append(f"{summary['id']}: transcript.json invalid JSON ({error})")

    for name in ("schema/catalog.schema.json", "schema/session.schema.json",
                 "schema/events.schema.json", "schema/topics.schema.json", "schema/transcript.schema.json"):
        try:
            load_json(ROOT / name)
        except Exception as error:
            errors.append(f"{name}: invalid or missing ({error})")

    for event in catalog["events"]:
        for key in ("index", "indexJSON"):
            if not (ROOT / event[key]).exists():
                errors.append(f"event {event['id']}: missing {event[key]}")

    if errors:
        print(f"VALIDATION FAILED — {len(errors)} error(s):")
        for error in errors[:60]:
            print(f"  - {error}")
        if len(errors) > 60:
            print(f"  ... and {len(errors) - 60} more")
        sys.exit(1)

    schema_note = "" if validators else " (schema validation skipped)"
    print(f"VALIDATION PASSED — {len(sessions)} sessions, {declared_transcripts} transcripts, "
          f"{len(catalog['events'])} events{schema_note}.")


if __name__ == "__main__":
    main()
