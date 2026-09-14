#!/usr/bin/env python3
"""Build lightweight Markdown navigation from canonical knowledge. No dependencies."""

from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge"
OUT = ROOT / "generated"


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


def title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def main() -> None:
    OUT.mkdir(exist_ok=True)
    grouped = defaultdict(list)
    open_questions = []

    for path in sorted(KB.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if not fm:
            continue
        object_type = fm.get("type", "unknown")
        object_id = fm.get("id", path.stem)
        item = (title(text, object_id), path.relative_to(ROOT), fm)
        grouped[object_type].append(item)
        if object_type == "question" and fm.get("status", "open") in {"open", "partial"}:
            open_questions.append(item)

    lines = ["# Knowledge Index", "", "Generated from canonical Markdown. Do not edit manually.", ""]
    for object_type in sorted(grouped):
        lines.extend([f"## {object_type.title()}s", ""])
        for name, path, fm in grouped[object_type]:
            status = fm.get("status")
            suffix = f" — `{status}`" if status else ""
            lines.append(f"- [{name}](../{path.as_posix()}){suffix}")
        lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    qlines = ["# Open Questions", "", "Generated from canonical questions. Do not edit manually.", ""]
    if not open_questions:
        qlines.append("_No open questions._")
    else:
        for name, path, fm in open_questions:
            qlines.append(f"- [{name}](../{path.as_posix()}) — `{fm.get('status', 'open')}`")
    (OUT / "OPEN_QUESTIONS.md").write_text("\n".join(qlines) + "\n", encoding="utf-8")

    print(f"Built indexes for {sum(len(v) for v in grouped.values())} canonical objects.")


if __name__ == "__main__":
    main()
