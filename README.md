# Elsevier Context Starter

A low-administration, agent-friendly internal context base for a team that learns continuously from conversations, documents, research, market signals, and decisions.

This repository is intentionally simple:

- **Git is the durable memory.**
- **Markdown is the interchange format.**
- **Agents handle filing, linking, deduplication, and maintenance.**
- **Humans review ambiguity and consequential conflicts instead of administering the library every day.**
- **Provenance and epistemic state stay visible.**
- **Generated indexes are disposable views, never the source of truth.**

> **Public-starter boundary:** this repository is currently public. Do not add confidential, proprietary, personal, customer, employee, product, strategy, or other internal Elsevier information here. Clone or transfer the framework into an approved private/internal environment before ingesting internal material. Making a public repository private later does not retract copies, forks, caches, or prior public history.

## What this is

This is not a graph database and it does not require one. It is a structured corpus that humans can browse and agents can retrieve directly. A graph, vector index, search service, or internal site can later be generated from the same corpus without changing the canonical knowledge.

The model is deliberately non-linear:

```text
Sources ───────┐
Observations ──┼──> Claims <──> Concepts
               │       │            │
               │       ├──> Summaries
               │       ├──> Hypotheses
               │       ├──> Decisions
               │       └──> Questions
               └────────────> Entities
```

A **fact is not a permanent object type**. It is a claim whose evidence, scope, freshness, and review state justify treating it as established. Claims can later be disputed, narrowed, superseded, or become stale.

## Two ingestion modes

### Conversational capture

Say something equivalent to:

> Push this into the knowledge base.

The agent follows `skills/capture.md`: preserve the input when useful, inspect relevant canonical material, extract durable knowledge, update rather than duplicate, identify conflicts, and leave only genuinely ambiguous or consequential questions for human review.

### Automated sweeps

Run `skills/sweep.md` over a bounded set of conversations, interviews, notes, documents, or external alerts. Sweeps are incremental: add what is durable, update what changed, and avoid rewriting stable knowledge merely for stylistic reasons.

## Repository map

```text
.
├── AGENTS.md
├── docs/
│   ├── ontology.md
│   └── lifecycle.md
├── intake/
├── knowledge/
│   ├── sources/
│   ├── observations/
│   ├── claims/
│   ├── concepts/
│   ├── summaries/
│   ├── hypotheses/
│   ├── decisions/
│   ├── questions/
│   └── entities/
├── skills/
│   ├── capture.md
│   ├── sweep.md
│   ├── maintain.md
│   └── conflicts.md
├── templates/
├── scripts/
│   ├── validate_kb.py
│   └── build_indexes.py
└── generated/
```

## Start here

1. Read `AGENTS.md`.
2. Read `docs/ontology.md` and `docs/lifecycle.md`.
3. Before internal use, clone or move this starter into an approved private environment.
4. Configure your agent so that **"push this into the knowledge base"** invokes `skills/capture.md`.
5. Add source-specific automation around `skills/sweep.md` only after the relevant internal sources and permissions are available.
6. Run `python scripts/validate_kb.py` and `python scripts/build_indexes.py` as lightweight maintenance steps.

The design goal is not a perfectly administered taxonomy. It is a context base that gets more useful as the team learns while imposing as little clerical work as possible.