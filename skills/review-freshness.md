# Skill: Review Knowledge Freshness

Use this workflow to keep current-state knowledge accurate without repeatedly re-researching durable history.

## Goal

Review information at a cadence proportional to how quickly the underlying reality can change.

The repository records **when something should be reconsidered**. The external runtime decides when and how to execute the review.

## Freshness metadata

Current-state canonical objects may use:

```yaml
last_reviewed: 2026-09-14
volatility: fast
review_after: 2026-09-21
```

`review_after` is the operative review target. `volatility` is a portable hint for selecting a reasonable cadence.

Recommended defaults when no better domain-specific cadence is known:

- `fast` — about 7 days; leadership roles, current product availability, active initiatives, market or regulatory conditions.
- `moderate` — about 30 days; active product positioning, operational ownership, evolving workflows, near-term plans.
- `slow` — about 90 days; established product structures, stable customer/buyer patterns, mature processes.
- `durable` — about 365 days or event-driven; historical acquisitions, durable definitions, settled background facts.

These are defaults, not guarantees. Set `review_after` directly when the appropriate date is known.

Do not assign volatility based only on object type. Two claims can have radically different rates of change.

## Procedure

1. **Find due objects.** Start with `generated/FRESHNESS_QUEUE.md` when available, then retrieve the canonical objects.
2. **Check materiality.** Prioritize objects that are actively used, decision-relevant, or likely to mislead if stale.
3. **Retrieve prior evidence.** Inspect the existing sources, confidence, scope, conflicts, and contribution lineage before re-verifying.
4. **Verify narrowly.** Determine whether the current assertion is still accurate and relevant. Avoid broad research when a targeted verification is sufficient.
5. **Classify the result.** The review should normally produce one of:
   - confirmed with newer evidence;
   - refined in scope;
   - superseded because reality changed;
   - disputed because credible evidence conflicts;
   - stale because it cannot currently be verified;
   - still relevant with no semantic change.
6. **Update dates.** When genuinely reviewed, update `last_reviewed` and choose a new `review_after` based on observed volatility and usefulness.
7. **Preserve provenance.** Material semantic changes follow normal source/contribution rules. A review that confirms an object with new evidence may also add source provenance when useful.
8. **Do not create churn.** A freshness review is successful even when the underlying text does not change.

## Review priority

When several objects are due, prefer:

1. fast-moving and overdue;
2. decision-critical;
3. frequently retrieved or referenced;
4. weakly evidenced or contradicted;
5. broad summaries that could misroute future retrieval;
6. lower-impact durable background.

## External verification

When the repository itself cannot verify an item, use `skills/prepare-task-context.md` to hand a narrow verification target to an authorized runtime.

The context packet should include the current claim, source lineage, last review date, known conflicts, and what evidence would count as confirmation or change.

Returned findings flow through `skills/ingest-task-results.md`.

## Generated queue

`scripts/build_indexes.py` should generate `generated/FRESHNESS_QUEUE.md` from canonical objects with `review_after` dates.

The queue is derived navigation, not a scheduler. A future runner may use it to decide what to review, but scheduling remains outside this repository.

## Anti-patterns

Avoid:

- declaring information fresh merely because a file was recently edited;
- resetting `last_reviewed` without actually checking accuracy;
- treating repeated copies of an old source as fresh evidence;
- using one cadence for every object;
- deleting historically useful but outdated claims instead of superseding/staling them;
- repeatedly reviewing low-value durable facts while high-impact fast-moving context goes stale.
