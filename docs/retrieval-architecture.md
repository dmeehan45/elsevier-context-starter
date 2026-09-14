# Retrieval Architecture

This repository is organized for durable meaning first and retrieval second.

Canonical knowledge remains partitioned by epistemic type (`claims`, `concepts`, `entities`, `hypotheses`, `decisions`, and so on). Do not reorganize canonical files around one agent, one product workflow, one search engine, or one temporary use case.

Instead, optimize usability through **progressive disclosure and derived retrieval views**.

## Why

Strong agent systems do not load every available fact into working context. They expose a compact map first, then retrieve narrower material as the task becomes clearer.

This repository follows the same pattern:

```text
entry contract
    ↓
compact context map
    ↓
relevant summaries / entities / concepts
    ↓
specific claims / hypotheses / questions / decisions
    ↓
sources + contribution lineage
```

The deeper layers remain available without polluting every task with the full corpus.

## Design rationale from leading agent systems

This pattern is deliberately aligned with approaches already used by leading labs/platforms rather than inventing a repository-specific retrieval theory:

- Anthropic's Agent Skills use **progressive disclosure**: lightweight skill metadata is visible first, the main skill is loaded only when relevant, and deeper reference files are opened only as needed. See [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
- Anthropic's context-engineering guidance argues that agent performance depends on curating the useful subset of context, not maximizing tokens, and recommends progressive retrieval, compaction, and structured external notes. See [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- Microsoft's Azure SRE Agent keeps a compact `overview.md` loaded for orientation and links outward to topic-specific knowledge files, separating always-needed routing context from deeper detail. See [Memory and knowledge in Azure SRE Agent](https://learn.microsoft.com/en-us/azure/sre-agent/memory).
- OpenAI vector-store retrieval supports metadata attributes and filters so runtimes can narrow retrieval before adding chunks to model context. See [Search vector store](https://developers.openai.com/api/reference/python/resources/vector_stores/methods/search).
- OpenAI's published Consensus architecture describes a structured **research context pack** assembled before synthesis, reinforcing the pattern of preparing the right evidence rather than giving one agent the entire corpus. See [Consensus uses GPT-5 and the Responses API](https://openai.com/index/consensus/).
- Microsoft's agentic retrieval decomposes complex questions into focused subqueries, runs them across relevant knowledge sources, reranks results, and returns source references rather than relying on one static corpus dump. See [Agentic Retrieval Overview](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview).

The portable lesson is not to copy any vendor's runtime. It is to keep canonical knowledge stable while giving future runtimes enough structure to **route, filter, retrieve, and cite selectively**.

## Stable canonical partition

The physical `knowledge/` layout answers: **what kind of knowledge is this?**

That partition is intentionally stable because epistemic type affects how an agent should interpret a record.

Do not create new canonical folder trees for each retrieval use case. The same claim may matter to product strategy, onboarding, research, and implementation.

## Derived retrieval layer

`generated/CONTEXT_MAP.md` is the compact routing layer. It is rebuildable and non-authoritative.

It should help a human or agent decide where to look next without reading the entire repository.

`generated/INDEX.md` remains the complete object listing. `generated/OPEN_QUESTIONS.md` and `generated/FRESHNESS_QUEUE.md` provide narrower operational views.

A future vector, graph, hybrid, or agentic-retrieval service may index the same corpus, but it remains a derived retrieval layer rather than canonical truth.

## Primary recall paths

### Orientation / "help me understand this area"

Prefer:

```text
summaries → concepts → entities → key claims → sources when needed
```

Start broad, then descend only where the task requires evidence.

### Current factual question

Prefer:

```text
specific active/established claims → relevant entity → source provenance → freshness
```

Do not answer a current-state question from a stale summary when a more specific claim exists.

### Product judgment / strategy

Prefer:

```text
summaries + entities
→ hypotheses + questions + decisions
→ supporting/contradicting claims
→ sources
```

Preserve segment and role distinctions rather than averaging them away.

### Hypothesis/discovery planning

Prefer:

```text
open hypotheses → unresolved questions → evidence gaps → recent decisions → relevant claims
```

Use domain skills such as `skills/weekly-hypothesis-questions.md` when appropriate.

### Decision history / "why are we doing this?"

Prefer:

```text
decision → rationale/context → related hypotheses/claims → contribution lineage
```

### Verification / conflict / freshness

Prefer:

```text
claim/entity/summary → last_reviewed + review_after
→ sources → contradicts/supersedes → contribution lineage
```

### External task handoff

Retrieve only the objects needed to prevent rediscovery or missed conflicts, then use `skills/prepare-task-context.md`.

## Retrieval metadata

Use metadata only when it improves retrieval or interpretation.

Useful portable fields include:

- `type`
- `status`
- `confidence`
- `last_reviewed`
- `volatility`
- `review_after`
- stable relationship IDs such as `related`, `supports`, `contradicts`, `supersedes`, and `part_of`

A future runtime may use these fields as filters, ranking signals, graph edges, or query-planning hints.

Do not add large tag taxonomies merely because a retrieval engine supports them. Prefer stable entity/concept relationships first.

## Progressive disclosure rule

A normal agent task should not begin by reading the entire corpus.

1. Read `AGENTS.md` / the relevant skill contract.
2. Use `generated/CONTEXT_MAP.md` or targeted repository search to locate likely objects.
3. Read the smallest useful set of canonical objects.
4. Expand to provenance/evidence only when needed.
5. If the task changes, retrieve again rather than carrying unrelated context forward.

## Retrieval quality over completeness

A large corpus can become less useful if stale, duplicative, or weakly routed knowledge crowds out relevant material.

Maintenance should therefore consider:

- whether summaries still point toward the right canonical objects;
- whether stale objects are clearly marked or queued for review;
- whether duplicate concepts/entities make retrieval ambiguous;
- whether commonly used questions have an obvious retrieval path;
- whether generated routing views remain compact enough to be useful.

The goal is not to make every fact immediately visible. The goal is to make the **next relevant layer easy to find**.
