#!/usr/bin/env python3
"""Dependency-free structural validation for the Markdown knowledge base."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge"
VALID_TYPES = {"source", "observation", "claim", "concept", "summary", "hypothesis", "decision", "question", "entity", "contribution"}
TYPE_DIRS = {t: f"{t}s" for t in VALID_TYPES}
TYPE_DIRS.update({"hypothesis": "hypotheses", "summary": "summaries", "entity": "entities"})
VALID_CONFIDENCE = {"low", "medium", "high"}
STATUS_BY_TYPE = {
    "claim": {"provisional", "active", "established", "disputed", "superseded", "stale", "rejected"},
    "hypothesis": {"open", "supported", "weakened", "rejected", "promoted"},
    "question": {"open", "partial", "answered", "parked"},
    "decision": {"active", "revisited", "superseded", "reversed"},
    "observation": {"active", "superseded", "stale", "archived"},
    "concept": {"active", "superseded", "stale", "archived"},
    "summary": {"active", "superseded", "stale", "archived"},
    "entity": {"active", "superseded", "stale", "archived"},
}
REFERENCE_FIELDS = {"source_ids", "related", "supports", "contradicts", "supersedes", "derived_from", "informs", "answers", "part_of", "contribution_ids", "object_ids"}
DATE_FIELDS = {"created", "last_reviewed", "source_date", "decision_date"}


def scalar(value: str):
    value = value.strip()
    if value in {"", "null", "~"}:
        return None
    if value == "[]":
        return []
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [] if not inner else [scalar(part) for part in inner.split(",")]
    return value


def frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    data = {}
    current = None
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")) and raw.strip().startswith("-") and current:
            item = scalar(raw.strip()[1:].strip())
            if not isinstance(data.get(current), list):
                data[current] = []
            data[current].append(item)
            continue
        if raw.startswith((" ", "\t")) or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        current = key.strip()
        parsed = scalar(value)
        data[current] = [] if parsed is None and value.strip() == "" else parsed
    return data


def as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value if v is not None]
    return [str(value)]


def valid_timestamp(value: str) -> bool:
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return True
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:\d{2})", value))


def main() -> int:
    errors = []
    warnings = []
    records = {}

    for path in KB.rglob("*.md"):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        rel = path.relative_to(ROOT)
        if not fm:
            errors.append(f"{rel}: missing or unreadable frontmatter")
            continue

        object_id = fm.get("id")
        object_type = fm.get("type")
        created = fm.get("created")
        if not object_id:
            errors.append(f"{rel}: missing id")
            continue
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(object_id)):
            errors.append(f"{rel}: id must be kebab-case: {object_id}")
        if object_id in records:
            errors.append(f"{rel}: duplicate id {object_id} also used by {records[object_id]['path']}")
        if object_type not in VALID_TYPES:
            errors.append(f"{rel}: unknown type {object_type!r}")
        else:
            expected_dir = TYPE_DIRS[object_type]
            parts = rel.parts
            if len(parts) < 3 or parts[1] != expected_dir:
                errors.append(f"{rel}: type {object_type!r} belongs under knowledge/{expected_dir}/")
        if not created:
            errors.append(f"{rel}: missing created date")

        for field in DATE_FIELDS:
            value = fm.get(field)
            if value and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(value)):
                errors.append(f"{rel}: {field} must use YYYY-MM-DD, got {value!r}")

        contributed_at = fm.get("contributed_at")
        if contributed_at and not valid_timestamp(str(contributed_at)):
            errors.append(f"{rel}: contributed_at must use YYYY-MM-DD or ISO 8601 with timezone, got {contributed_at!r}")

        status = fm.get("status")
        allowed = STATUS_BY_TYPE.get(object_type)
        if status and allowed and status not in allowed:
            errors.append(f"{rel}: invalid status {status!r} for {object_type}; expected one of {sorted(allowed)}")

        confidence = fm.get("confidence")
        if confidence and confidence not in VALID_CONFIDENCE:
            errors.append(f"{rel}: invalid confidence {confidence!r}; use low, medium, or high")

        if object_type == "contribution":
            for required in ("contributor", "contributed_at", "recorded_by"):
                if not fm.get(required):
                    errors.append(f"{rel}: contribution missing required field {required}")
            if not as_list(fm.get("object_ids")):
                errors.append(f"{rel}: contribution must reference at least one object_id")

        records[object_id] = {"path": rel, "fm": fm, "type": object_type}

    ids = set(records)
    for record in records.values():
        rel = record["path"]
        fm = record["fm"]
        for field in REFERENCE_FIELDS:
            for target in as_list(fm.get(field)):
                if target and target not in ids:
                    errors.append(f"{rel}: {field} references unknown id {target!r}")
        for target in as_list(fm.get("source_ids")):
            if target in records and records[target]["type"] != "source":
                errors.append(f"{rel}: source_ids target {target!r} is type {records[target]['type']!r}, not source")
        for target in as_list(fm.get("contribution_ids")):
            if target in records and records[target]["type"] != "contribution":
                errors.append(f"{rel}: contribution_ids target {target!r} is type {records[target]['type']!r}, not contribution")
        if record["type"] == "claim" and fm.get("status") == "established" and not as_list(fm.get("source_ids")):
            warnings.append(f"{rel}: established claim has no source_ids; verify provenance is explicit in the body")

    if errors:
        print("Knowledge-base validation failed:\n")
        for error in errors:
            print(f"- ERROR: {error}")
    if warnings:
        print("\nWarnings:\n")
        for warning in warnings:
            print(f"- WARNING: {warning}")
    if errors:
        return 1

    print(f"Knowledge-base validation passed ({len(records)} canonical objects, {len(warnings)} warnings).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
