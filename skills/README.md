# Skills

Skills are reusable reasoning/workflow contracts for humans and agents using this context base.

They describe **what good work looks like**. They do not grant permissions, select models, configure tools, or define the runtime that executes the work.

## Core context-base workflows

These maintain the knowledge substrate itself.

| Intent | Skill |
| --- | --- |
| Capture approved durable knowledge | `capture.md` |
| Check whether information is appropriate for the destination/runtime | `check-information-boundary.md` |
| Resolve contradictions/supersession | `conflicts.md` |
| Keep current-state knowledge reviewed at an appropriate cadence | `review-freshness.md` |
| Sweep bounded sources | `sweep.md` |
| QA and maintain the corpus | `maintain.md` |
| Prepare context for work in another runtime | `prepare-task-context.md` |
| Reconcile external task findings back into the corpus | `ingest-task-results.md` |

## Retrieval behavior

See `docs/retrieval-architecture.md` before inventing a new storage partition or loading the whole repository into an agent context.

The default retrieval pattern is progressive disclosure:

```text
context map → orientation objects → specific claims/questions/decisions → evidence/provenance
```

`generated/CONTEXT_MAP.md` is the compact derived routing view. `generated/INDEX.md` remains the complete listing.

## Example product-management support workflows

These show how domain workflows can use the context base without becoming part of its core infrastructure.

| User intent | Skill |
| --- | --- |
| "What five questions about our hypotheses should we answer this week?" | `weekly-hypothesis-questions.md` |
| "Where do we need a sharper understanding of our core product questions?" | `core-product-questions.md` |

### Weekly Hypothesis Questions

Uses the current hypothesis graph, evidence quality, freshness, unresolved questions, and decision context to select five high-value questions that are worth trying to answer in the coming week.

It prioritizes **learning value + decision impact + realistic answerability**, not generic discovery ideas.

### Core Product Questions

Audits how well the context base can currently answer five durable product questions:

1. What jobs does our product do for users?
2. How well can we measure our primary success metrics?
3. What are the primary reasons users buy our product?
4. What are the primary reasons users stop using our product?
5. How aligned are our product investments/roadmap with our business objectives?

It distinguishes what is known from what is assumed, assesses answer quality, and identifies the investigations that would most improve product judgment.

## Pattern for future domain skills

A good domain skill should usually:

1. start from relevant canonical context rather than generic model knowledge;
2. preserve epistemic distinctions and source freshness;
3. define a repeatable reasoning procedure;
4. define a useful output contract;
5. expose uncertainty and evidence gaps;
6. avoid assuming environment-specific tools or permissions;
7. pass sensitive material through `check-information-boundary.md` before widening access;
8. use `prepare-task-context.md` when a selected gap should be investigated in another runtime;
9. use `ingest-task-results.md` before returned evidence changes canonical knowledge.

Domain skills should not quietly become a second ontology, runner configuration system, or source of canonical truth.
