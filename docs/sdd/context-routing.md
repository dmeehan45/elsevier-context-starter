# Context routing for SDD

This repository is a shared context source for SDD, not an OpenSpec artifact store and not a prompt that should be loaded in full.

The operating principle is:

> One large shared memory, many small working contexts.

Use the repository's existing epistemic structure and progressive disclosure to retrieve only what is relevant to the current product decision.

## Start with the decision, not the folder

Before retrieving context, identify:

- the product/capability or problem area;
- the user/customer/client scope;
- the current SDD activity;
- the decision or uncertainty the PM is trying to resolve.

Then use `generated/CONTEXT_MAP.md`, `generated/SDD_CONTEXT_MAP.md` when available, or targeted repository search.

Do not begin by reading all files under `knowledge/`.

## Existing canonical data is already usable

No migration is required for the current corpus.

Interpret existing objects according to their epistemic type:

- `summaries` — orientation and synthesis;
- `concepts` — durable vocabulary, mechanisms, and models;
- `entities` — stable product/person/team/standard/customer referents;
- `claims` — scoped assertions that may be supported, disputed, or stale;
- `observations` — minimally interpreted evidence;
- `hypotheses` — propositions still being tested;
- `questions` — unresolved knowledge gaps;
- `decisions` — choices the team has actually made;
- `sources` — provenance and evidence;
- `contributions` — who changed shared context and when.

For old records that do not have an explicit `authority` field, apply the defaults in `../ontology.md#authority-and-sdd-interpretation`.

## Retrieval patterns by PM activity

These are search heuristics, not fixed stage tags on every knowledge object.

### Explore a product problem

Prefer:

```text
summaries + concepts + entities
-> relevant claims / observations
-> hypotheses + questions
-> prior decisions
-> sources when evidence quality matters
```

Goal: understand the problem, known variation, and uncertainty before specifying behavior.

### Review proposed scope

Prefer:

```text
current product/user summaries
+ active decisions
+ open hypotheses/questions
+ claims about affected clients/segments
+ known constraints
```

Goal: detect hidden outcomes, conflicting client needs, or unresolved questions that should change the proposed boundary.

### Create/review requirements

Prefer:

```text
active decisions
+ high-confidence current claims that define external reality
+ standards/regulatory/client constraints
+ relevant concepts
+ contradictory evidence
```

Descriptive evidence informs requirements; it does not become a requirement automatically.

### Review design / implementation approach

Prefer:

```text
accepted decisions
+ advisory concepts/patterns
+ system/product entities
+ known implementation constraints
+ client variation
+ evaluation / observability guidance
```

If implementation-specific guidance does not yet exist in this context base, inspect the target codebase rather than inventing a team standard here.

### Prepare PM acceptance

Prefer:

```text
OpenSpec requirements/scenarios from the target project
+ client/user context from this repository
+ accepted product decisions
+ evaluation/measurement concepts
+ known environment/client constraints
```

Acceptance criteria should primarily come from the approved change artifacts. This repository provides contextual validity and known variation.

## Retrieval should change when the task changes

Do not carry a large Explore context into Apply just because it is already in the conversation.

Re-retrieve for the next decision.

Example:

```text
Explore
  learner journey + faculty needs + evidence + hypotheses

Proposal review
  strongest problem evidence + decisions + client variation + unresolved scope questions

Design review
  product contract + architecture/design guidance + integration constraints

Acceptance
  requirements/scenarios + client context + environment/evaluation constraints
```

## Authority matters

An SDD agent must not flatten all Markdown into equal instructions.

The interpretation order is:

1. controlling user/runtime/OpenSpec workflow instructions;
2. active normative team decisions/constraints within their stated scope;
3. advisory team patterns;
4. descriptive evidence and research;
5. open hypotheses/questions.

If two applicable normative records conflict, surface the conflict rather than choosing silently.

If descriptive evidence conflicts with an accepted decision, explain the tension; do not silently rewrite the decision.

## Search before adding metadata

Prefer existing entity/concept relationships and targeted search before creating broad tag taxonomies.

If repeated SDD usage demonstrates that agents cannot reliably retrieve a class of context, add the minimum stable metadata needed to solve that observed retrieval problem. Do not pre-classify every knowledge object by OpenSpec stage.

## Context packet shape

When a bounded packet is useful, provide:

```text
Objective / decision being made

Current understanding
- canonical ID — concise relevant point

Accepted constraints / decisions
- ...

Evidence and uncertainty
- established/current claims
- hypotheses/questions
- known conflicts/freshness concerns

Relevant client/user variation
- ...

What the agent should not assume
- ...

Canonical references to retrieve more deeply if needed
- ...
```

Keep the packet derived. Canonical truth remains under `knowledge/` and in the target project's approved OpenSpec artifacts.
