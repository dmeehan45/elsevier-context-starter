#!/usr/bin/env python3
"""Portable repository smoke test. Uses only the Python standard library."""

from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs/ontology.md",
    "docs/lifecycle.md",
    "docs/agent-interop.md",
    "docs/portability.md",
    "docs/provenance.md",
    "docs/external-tasking.md",
    "docs/retrieval-architecture.md",
    "skills/README.md",
    "skills/capture.md",
    "skills/sweep.md",
    "skills/maintain.md",
    "skills/conflicts.md",
    "skills/review-freshness.md",
    "skills/check-information-boundary.md",
    "skills/prepare-task-context.md",
    "skills/ingest-task-results.md",
    "templates/contribution.md",
    "templates/task-context-packet.md",
    "templates/run-report.md",
    "knowledge/contributions/README.md",
    "generated/README.md",
    "scripts/validate_kb.py",
    "scripts/build_indexes.py",
]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {raw_target}")
                continue
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link: {raw_target}")


def main() -> int:
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required path: {rel}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_symlink():
            errors.append(f"symlink found (avoid for cross-platform portability): {path.relative_to(ROOT)}")

    config = ROOT / "automation" / "sweeps.example.json"
    if config.exists():
        try:
            json.loads(config.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"automation/sweeps.example.json is invalid JSON: {exc}")

    check_links(errors)

    validation = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_kb.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if validation.returncode != 0:
        errors.append("knowledge validation failed:\n" + validation.stdout + validation.stderr)

    if errors:
        print("Repository doctor found problems:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository doctor passed.")
    if validation.stdout.strip():
        print(validation.stdout.strip())
    print("Core files, relative links, JSON config, symlink policy, provenance/task-handoff/freshness/retrieval contracts, and knowledge structure look portable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
