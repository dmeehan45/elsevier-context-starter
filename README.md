# Elsevier Context Starter

A low-administration context base that humans and many kinds of agents can read, improve, and carry between environments.

In plain English: **put useful material in, let agents organize it, keep the evidence trail, and make the resulting knowledge easy for the next person or agent to use.**

The durable core is intentionally boring:

- **Git is the memory.**
- **Markdown is the interchange format.**
- **`knowledge/` is the canonical library.**
- **`intake/` is allowed to be messy.**
- **Agents do most filing, linking, deduplication, and maintenance.**
- **Humans review consequential ambiguity and conflicts instead of administering the library every day.**
- **Generated indexes are disposable views, never the source of truth.**

> **Public boundary:** this repository is public. Add public information only. Do not add confidential, proprietary, personal, customer, employee, non-public product, strategy, or other internal company information. Use an approved private/internal copy before ingesting internal material. Making a public repository private later does not retract copies, forks, caches, or prior public history.

## If you are a person

You should not need to learn the filing system. Point an agent at this repository and use ordinary language:

- **"Explain this context base and how I should use it."**
- **"Push this into the knowledge base."**
- **"Sweep these notes/documents/conversations and add what is durable."**
- **"What does the context base currently say about X?"**
- **"QA the context base for conflicts, stale material, and duplicates."**

The agent should handle filenames, metadata, links, and routine cleanup. See `CONTRIBUTING.md` if you want to edit by hand.

## If you are an agent

Start with `AGENTS.md`. It is the universal operating contract.

Do not assume you are Claude Code, ChatGPT, Codex, Copilot, a Microsoft agent, Hermes, or any other specific runtime. First determine what you can actually do: read files, search the repository, edit files, run commands, commit, or open pull requests. Then produce the same semantic result with the capabilities available to you.

If asked what this repository is, explain it simply before discussing the ontology. If you cannot write to the repository, do not pretend that you did: return the proposed changes or tell the user what permission/capability is missing.

See `docs/agent-interop.md` for the cross-agent contract.

## How the information model works

This is not a graph database. It is a structured corpus that can later feed a graph, vector index, search service, site, or agent retrieval layer.

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

Read `docs/ontology.md` only when you need the detailed rules.

## The two normal ingestion paths

**Conversational capture:** tell an agent to "push this into the knowledge base." The agent follows `skills/capture.md`, retrieves existing material first, and updates before creating duplicates.

**Batch/automated sweep:** give an agent a bounded set of conversations, interviews, documents, feeds, or alerts. The agent follows `skills/sweep.md`, groups related evidence, and promotes only durable material.

Both paths use the same canonical library and conflict rules.

## Repository map

```text
.
├── README.md                 plain-language entry point
├── AGENTS.md                 universal agent contract
├── CONTRIBUTING.md           simple contribution guide
├── docs/
│   ├── ontology.md           meaning of object types and relationships
│   ├── lifecycle.md          intake → canonical knowledge → maintenance
│   ├── agent-interop.md      behavior across different agent runtimes
│   └── portability.md        clone, mirror, and private-copy guidance
├── intake/                   raw or lightly processed inputs
├── knowledge/                canonical knowledge
├── skills/                   reusable workflows for agents
├── templates/                optional authoring templates
├── automation/               runner-agnostic recurring-job examples
├── scripts/                  dependency-free maintenance helpers
└── generated/                rebuildable navigation/review views
```

## Portable by design

There is no required database, hosted memory service, agent vendor, or GitHub-only runtime. Canonical references use repository-relative files and stable IDs. The helper scripts use the Python standard library.

A normal clone, a local working copy, a GitHub/GitLab/enterprise mirror, or a future private internal copy should preserve the semantics. Platform-specific adapters may be added, but they should point back to `AGENTS.md` and `skills/` rather than redefine the system.

See `docs/portability.md` before mirroring or moving the repository.

## Self-check

When a shell and Python are available:

```bash
python scripts/doctor.py
python scripts/build_indexes.py
```

`doctor.py` checks the core repository contract and canonical knowledge structure without external packages. An agent without a shell should perform the equivalent checks described in `AGENTS.md` and `skills/maintain.md`.

The design goal is not a perfectly administered taxonomy. It is a context base that becomes more useful as the team learns while imposing as little clerical work as possible.