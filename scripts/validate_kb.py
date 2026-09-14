#!/usr/bin/env python3
"""Dependency-free structural validation for the Markdown knowledge base."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge"
VALID_TYPES = {"source", "observation", "claim", "concept", "summary", "hypothesis", "decision", "question", "entity"}


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    data = {}
    for line in text[4:end].splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return data


def main() -> int:
    errors = []
    ids = {}
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
        if not object_id:
            errors.append(f"{rel}: missing id")
        elif not re.fullmatch(r"[a-z0-9][a-z0-9-]*", object_id):
            errors.append(f"{rel}: id must be kebab-case: {object_id}")
        elif object_id in ids:
            errors.append(f"{rel}: duplicate id {object_id} also used by {ids[object_id]}")
        else:
            ids[object_id] = rel
        if object_type not in VALID_TYPES:
            errors.append(f"{rel}: unknown type {object_type!r}")

    if errors:
        print("Knowledge-base validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Knowledge-base validation passed ({len(ids)} canonical objects).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
