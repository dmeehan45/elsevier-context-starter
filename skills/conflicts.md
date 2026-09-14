# Skill: Resolve Knowledge Conflicts

Conflicts are expected. The repository should become more accurate over time without pretending earlier knowledge never existed.

## First retrieve lineage

Before deciding whether two statements conflict, retrieve both:

- **source provenance**: where each assertion came from, who said/published it, and when;
- **contribution provenance**: who added or materially changed the canonical object, when, and through which agent/tool.

Use `source_ids`, `contribution_ids`, source dates, and contribution records. Legacy objects may not have contribution metadata; do not invent it.

## Classify the mismatch

Determine whether the new information:

- **confirms** the existing claim;
- **refines** its scope or precision;
- **supersedes** it because the underlying reality changed;
- **contradicts** it within the same scope/time;
- **reframes** an over-broad or misleading claim;
- or is actually **orthogonal**.

Do not label two statements contradictory until scope, time, definitions, entity identity, source lineage, and contribution lineage have been checked.

## Authority assessment

Compare:

- primary vs secondary source;
- direct observation vs hearsay;
- accountable owner/expert vs casual report;
- current vs stale information;
- scoped evidence vs generalized assertion;
- independent evidence lineages vs repeated copies of the same origin.

Authority is contextual. A senior title alone does not make someone authoritative on every subject. Contributor identity is provenance, not authority by itself.

## Human-facing conflict prompt

When a human needs to resolve a material conflict, give them the lineage first. Prefer something like:

> Existing claim: Jeff contributed this last Tuesday from an onboarding conversation. New evidence: a product document updated this Monday says something different about the same scope. Should we treat the new information as a supersession, keep both as scope-specific, or mark the claim disputed?

If the source speaker and contributor are different, say so. For example: "Jeff reported this Tuesday; David added it Wednesday through ChatGPT."

Do not reduce the question to a context-free "overwrite?" when provenance can make the decision easier.

## Update rules

### Clear supersession

If the world clearly changed and a newer authoritative source establishes the new state:

- update the canonical active claim;
- mark the old claim `superseded` when a separate historical claim is retained;
- link old and new with `supersedes` when applicable;
- preserve both source trails;
- create a new contribution event for the semantic change and append its ID to affected objects.

No human review is required unless the change is consequential or authority is ambiguous.

### Refinement

Narrow or expand the claim's scope while preserving supporting sources. Avoid creating two claims if one scoped claim is clearer. Record a material refinement as a new contribution event.

### Material contradiction

When credible sources disagree and the conflict cannot be safely resolved:

- mark the claim `disputed` when appropriate;
- record the contradicting source/claim;
- preserve existing contribution history;
- add a concise item to `generated/REVIEW_QUEUE.md`;
- ask the user one targeted, lineage-aware question if user input can actually resolve it.

Do not average contradictory claims into vague prose.

## Overwrite principle

The current canonical view is allowed to change. The historical evidence and contribution trail should not be silently destroyed. "Overwrite" means replace what agents should currently rely on while preserving enough provenance to explain what changed, who contributed each understanding, and why.