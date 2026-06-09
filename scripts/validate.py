#!/usr/bin/env python3
"""Validate catalog <-> filesystem integrity for the WWDC sessions knowledge base.

Exits non-zero on any inconsistency so it can gate CI. Checks that every catalog record points at
files that exist and parse, that counts are accurate, and that transcripts are present and
well-formed wherever `hasTranscript` is true.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SESSION_REQUIRED = {"schemaVersion", "id", "event", "title", "url", "hasTranscript", "path", "files"}


def load_json(path):
    return json.loads(path.read_text())


def main():
    errors = []

    catalog = load_json(ROOT / "catalog.json")
    sessions = catalog["sessions"]

    if catalog["counts"]["sessions"] != len(sessions):
        errors.append(f"counts.sessions {catalog['counts']['sessions']} != {len(sessions)} records")
    declared_transcripts = sum(1 for s in sessions if s["hasTranscript"])
    if catalog["counts"]["transcripts"] != declared_transcripts:
        errors.append(f"counts.transcripts {catalog['counts']['transcripts']} != {declared_transcripts}")

    ids = [s["id"] for s in sessions]
    if len(ids) != len(set(ids)):
        errors.append("duplicate session ids in catalog")
    paths = [s["path"] for s in sessions]
    if len(paths) != len(set(paths)):
        errors.append("duplicate session paths in catalog")

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
        if meta.get("id") != summary["id"]:
            errors.append(f"{summary['id']}: metadata id mismatch ({meta.get('id')})")
        if not (directory / "README.md").exists():
            errors.append(f"{summary['id']}: missing README.md")
        if summary["hasTranscript"]:
            for name in ("transcript.md", "transcript.json"):
                if not (directory / name).exists():
                    errors.append(f"{summary['id']}: hasTranscript but missing {name}")
            tjson = directory / "transcript.json"
            if tjson.exists():
                try:
                    segments = load_json(tjson).get("segments")
                    if not isinstance(segments, list) or not segments:
                        errors.append(f"{summary['id']}: transcript.json has no segments")
                except Exception as error:
                    errors.append(f"{summary['id']}: transcript.json invalid JSON ({error})")

    for name in ("events.json", "topics.json", "schema/catalog.schema.json", "schema/session.schema.json"):
        try:
            load_json(ROOT / name)
        except Exception as error:
            errors.append(f"{name}: invalid or missing ({error})")

    for event in catalog["events"]:
        if not (ROOT / event["index"]).exists():
            errors.append(f"event {event['id']}: missing index {event['index']}")

    if errors:
        print(f"VALIDATION FAILED — {len(errors)} error(s):")
        for error in errors[:50]:
            print(f"  - {error}")
        if len(errors) > 50:
            print(f"  ... and {len(errors) - 50} more")
        sys.exit(1)

    print(f"VALIDATION PASSED — {len(sessions)} sessions, "
          f"{declared_transcripts} transcripts, {len(catalog['events'])} events.")


if __name__ == "__main__":
    main()
