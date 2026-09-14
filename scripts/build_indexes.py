#!/usr/bin/env python3
"""Build lightweight Markdown navigation from canonical knowledge. No dependencies."""

from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge"
OUT = ROOT / "generated"
INACTIVE_STATUSES = {"superseded", "rejected", "archived", "reversed"}


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


def parse_date(value: str | None):
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def main() -> None:
    OUT.mkdir(exist_ok=True)
    grouped = defaultdict(list)
    open_questions = []
    records = []

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
        records.append(item)
        if object_type == "question" and fm.get("status", "open") in {"open", "partial"}:
            open_questions.append(item)

    # Complete canonical index.
    lines = ["# Knowledge Index", "", "Generated from canonical Markdown. Do not edit manually.", ""]
    for object_type in sorted(grouped):
        lines.extend([f"## {object_type.title()}s", ""])
        for name, path, fm in grouped[object_type]:
            status = fm.get("status")
            suffix = f" — `{status}`" if status else ""
            lines.append(f"- [{name}](../{path.as_posix()}){suffix}")
        lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    # Open-question view.
    qlines = ["# Open Questions", "", "Generated from canonical questions. Do not edit manually.", ""]
    if not open_questions:
        qlines.append("_No open questions._")
    else:
        for name, path, fm in open_questions:
            qlines.append(f"- [{name}](../{path.as_posix()}) — `{fm.get('status', 'open')}`")
    (OUT / "OPEN_QUESTIONS.md").write_text("\n".join(qlines) + "\n", encoding="utf-8")

    # Compact progressive-disclosure routing map.
    counts = {kind: len(items) for kind, items in grouped.items()}
    cmap = [
        "# Context Map",
        "",
        "Generated routing view. Start here when you need context; do not load the full corpus by default.",
        "",
        "## Retrieval paths",
        "",
        f"- **Orient to a topic:** summaries ({counts.get('summary', 0)}) → concepts ({counts.get('concept', 0)}) → entities ({counts.get('entity', 0)}).",
        f"- **Answer a current factual question:** claims ({counts.get('claim', 0)}) → sources ({counts.get('source', 0)}) → freshness/provenance.",
        f"- **Product/discovery reasoning:** hypotheses ({counts.get('hypothesis', 0)}) + questions ({counts.get('question', 0)}) + decisions ({counts.get('decision', 0)}) → supporting claims.",
        "- **Verify or reconcile:** specific object → sources → contradiction/supersession → contribution lineage.",
        "- **Prepare external work:** retrieve only task-relevant objects, then use `skills/prepare-task-context.md`.",
        "",
        "## Useful derived views",
        "",
        "- [Complete knowledge index](INDEX.md)",
        "- [Open questions](OPEN_QUESTIONS.md)",
        "- [Freshness queue](FRESHNESS_QUEUE.md)",
        "",
    ]

    summaries = [item for item in grouped.get("summary", []) if item[2].get("status") not in INACTIVE_STATUSES]
    if summaries:
        cmap.extend(["## Orientation summaries", ""])
        for name, path, _ in summaries[:12]:
            cmap.append(f"- [{name}](../{path.as_posix()})")
        if len(summaries) > 12:
            cmap.append(f"- _{len(summaries) - 12} more; use the complete index._")
        cmap.append("")

    cmap.extend([
        "## Rule",
        "",
        "Expand context progressively: routing view → canonical object → evidence/provenance. Retrieve again when the task changes rather than carrying unrelated context forward.",
        "",
        "See `docs/retrieval-architecture.md` for the retrieval contract.",
        "",
    ])
    (OUT / "CONTEXT_MAP.md").write_text("\n".join(cmap), encoding="utf-8")

    # Freshness queue from explicit review targets.
    today = date.today()
    upcoming_cutoff = today + timedelta(days=14)
    due = []
    upcoming = []
    unscheduled_volatile = []

    for name, path, fm in records:
        object_type = fm.get("type")
        status = fm.get("status")
        if object_type in {"source", "observation", "contribution"} or status in INACTIVE_STATUSES:
            continue
        review_after = parse_date(fm.get("review_after"))
        volatility = fm.get("volatility")
        if review_after:
            item = (review_after, name, path, fm)
            if review_after <= today:
                due.append(item)
            elif review_after <= upcoming_cutoff:
                upcoming.append(item)
        elif volatility in {"fast", "moderate"}:
            unscheduled_volatile.append((name, path, fm))

    due.sort(key=lambda item: item[0])
    upcoming.sort(key=lambda item: item[0])

    flines = [
        "# Freshness Queue",
        "",
        f"Generated on {today.isoformat()} from canonical freshness metadata. This is a review queue, not a scheduler.",
        "",
        "## Due / overdue",
        "",
    ]
    if not due:
        flines.append("_No objects are currently due._")
    else:
        for review_after, name, path, fm in due:
            flines.append(
                f"- [{name}](../{path.as_posix()}) — `{fm.get('type', 'unknown')}`; "
                f"volatility `{fm.get('volatility', 'unspecified')}`; review after `{review_after.isoformat()}`; "
                f"last reviewed `{fm.get('last_reviewed', 'unknown')}`"
            )

    flines.extend(["", "## Due in the next 14 days", ""])
    if not upcoming:
        flines.append("_No scheduled reviews in this window._")
    else:
        for review_after, name, path, fm in upcoming:
            flines.append(
                f"- [{name}](../{path.as_posix()}) — `{fm.get('type', 'unknown')}`; "
                f"volatility `{fm.get('volatility', 'unspecified')}`; review after `{review_after.isoformat()}`"
            )

    flines.extend(["", "## Volatile but unscheduled", ""])
    if not unscheduled_volatile:
        flines.append("_No fast/moderate objects are missing an explicit review target._")
    else:
        for name, path, fm in unscheduled_volatile:
            flines.append(
                f"- [{name}](../{path.as_posix()}) — `{fm.get('type', 'unknown')}`; volatility `{fm.get('volatility')}`"
            )

    flines.extend(["", "See `skills/review-freshness.md` before reviewing or updating these objects.", ""])
    (OUT / "FRESHNESS_QUEUE.md").write_text("\n".join(flines), encoding="utf-8")

    print(f"Built indexes for {sum(len(v) for v in grouped.values())} canonical objects.")


if __name__ == "__main__":
    main()
