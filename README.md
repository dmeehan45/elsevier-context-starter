# Elsevier Context Starter

A low-administration context base that humans and many kinds of agents can read, improve, and carry between environments.

In plain English: **learn together first, decide what matters, then let agents organize and preserve the durable context.**

The durable core is intentionally boring:

- **Git is the memory.**
- **Markdown is the interchange format.**
- **`knowledge/` is the canonical library.**
- **`intake/` is allowed to be messy.**
- **Agents do most filing, linking, deduplication, and maintenance.**
- **Humans stay involved in learning, relevance, ambiguity, and consequential conflicts.**
- **Material writes preserve who contributed them and when.**
- **Generated indexes are disposable views, never the source of truth.**

> **Public boundary:** this repository is public. Add public information only. Do not add confidential, proprietary, personal, customer, employee, non-public product, strategy, or other internal company information. Use an approved private/internal copy before ingesting internal material.

## If you are a person

You should not need to learn the filing system. Point an agent at this repository and use ordinary language:

- **"Explain this context base and how I should use it."**
- **"Research Elsevier's leadership and teach me what matters."**
- **"Here's a link — help me understand what it adds to our context."**
- **"What should we preserve from this?"**
- **"Push the recommended items."**
- **"What does the context base currently say about X?"**
- **"QA the context base for conflicts, stale material, and duplicates."**

The normal interactive pattern is:

```text
INVESTIGATE → TEACH → CURATE → COMMIT
```

That means the agent should explain what it found **before** growing the repository. It should keep useful source citations visible, recommend the small set of durable findings worth preserving, and ask you for a lightweight decision. You should not need to choose filenames, metadata, folders, or ontology types.

If you already reviewed something and say **"push this"**, that can count as approval to write it.

For material writes, the agent also preserves contribution provenance: who contributed the knowledge, when, which agent/tool recorded it, and which canonical objects changed. This is separate from source provenance, so the system can distinguish "Jeff said this Tuesday" from "David added it Wednesday through ChatGPT." See `docs/provenance.md`.

See `CONTRIBUTING.md` if you want to edit by hand.

## Working from a link

You can drop a public URL into the conversation without preparing anything else.

A capable agent should:

1. read the page;
2. explain the important findings and why they matter;
3. cite externally derived claims;
4. compare the page with relevant existing context;
5. distinguish what the source says from the agent's interpretation;
6. recommend what is worth preserving and what is incidental;
7. ask for approval before canonical writes unless you already authorized automatic capture.

If the page is inaccessible, the agent should say so rather than guessing from the URL or page title.

## If you are an agent

Start with `AGENTS.md`. It is the universal operating contract.

Do not assume you are Claude Code, ChatGPT, Codex, Copilot, a Microsoft agent, Hermes, or any other specific runtime. First determine what you can actually do: read files, search the repository, access external sources, edit files, run commands, commit, or open pull requests. Then produce the same semantic result with the capabilities available to you.

If asked what this repository is, explain it simply before discussing the ontology. If you cannot write to the repository, do not pretend that you did: return the proposed changes or tell the user what capability is missing.

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

Contributions ─────> record who materially changed canonical objects and when
```

A **fact is not a permanent object type**. It is a claim whose evidence, scope, freshness, and review state justify treating it as established. Claims can later be disputed, narrowed, superseded, or become stale.

Read `docs/ontology.md` only when you need the detailed rules.

## The two normal ingestion paths

**Interactive research/capture:** the human and agent learn together. The agent teaches first, recommends what should enter the library, gets lightweight approval, then follows `skills/capture.md` to canonicalize the approved set.

**Batch/automated sweep:** an agent processes a bounded set of conversations, interviews, documents, feeds, or alerts using `skills/sweep.md`. Because no human may be present, low-risk updates can be applied under the configured review policy.

Both paths use the same canonical library, provenance rules, and conflict handling.

## Repository map

```text
.
├── README.md                 plain-language entry point
├── AGENTS.md                 universal agent contract
├── CONTRIBUTING.md           simple contribution guide
├── docs/
│   ├── ontology.md           meaning of object types and relationships
│   ├── lifecycle.md          intake → canonical knowledge → maintenance
│   ├── provenance.md         source vs contribution lineage
│   ├── agent-interop.md      behavior across different agent runtimes
│   └── portability.md        clone, mirror, and private-copy guidance
├── intake/                   raw or lightly processed inputs
├── knowledge/                canonical knowledge + contribution events
├── skills/                   reusable workflows for agents
├── templates/                optional authoring templates
├── automation/               runner-agnostic recurring-job examples
├── scripts/                  dependency-free maintenance helpers
└── generated/                rebuildable navigation/review views
```

## Portable by design

There is no required database, hosted memory service, agent vendor, or GitHub-only runtime. Canonical references use repository-relative files and stable IDs. The helper scripts use the Python standard library.

A normal clone, a local working copy, a GitHub/GitLab/enterprise mirror, or a future private internal copy should preserve the semantics. Platform-specific adapters may be added, but they should point back to `AGENTS.md` and `skills/` rather than redefine the system.

Contribution events make important contributor lineage portable even when a future copy does not carry complete Git history.

See `docs/portability.md` before mirroring or moving the repository.

## Self-check

When a shell and Python are available:

```bash
python scripts/doctor.py
python scripts/build_indexes.py
```

`doctor.py` checks the core repository contract and canonical knowledge structure without external packages. An agent without a shell should perform the equivalent checks described in `AGENTS.md` and `skills/maintain.md`.

The design goal is not a perfectly administered taxonomy. It is a context base that becomes more useful as the team learns while keeping the user engaged in the learning and judgment that actually matter.