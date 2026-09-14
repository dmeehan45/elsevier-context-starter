# Skill: Capture to Knowledge Base

Use this workflow when a human wants material considered for durable team context.

## Core principle

For interactive work, **teach before writing**. Low administration means the agent handles filing and metadata; it does not mean removing the user from deciding what is relevant.

The default manual loop is:

```text
INVESTIGATE → TEACH → CURATE → COMMIT
```

If the user has already explicitly approved a specific item for capture, that approval can satisfy the curate step.

## Procedure

1. **Understand the input.** Identify source, subject, time, scope, and whether the material is direct evidence, a report, synthesis, hypothesis, decision, question, or entity context.
2. **Retrieve before writing.** Search existing canonical material, source provenance, contribution history, and semantic equivalents.
3. **Teach first when the user is still learning.** Explain the important findings, why they matter, how they connect to existing context, and what remains uncertain. Keep source citations visible for externally derived claims when the runtime supports them.
4. **Recommend what is worth preserving.** Separate candidate knowledge into: recommend preserving, optional, and do not preserve. Explain relevance briefly; do not ask the user to choose filenames or metadata.
5. **Ask for a lightweight decision.** Accept shorthand such as "push recommended," "A and C," "all," or "none."
6. **Identify the contributor.** For a material write, preserve the person, team, or automated process whose contribution this represents. Use reliable session/platform context when available. If a human contributor is unknown, ask once before the first durable write rather than guessing.
7. **Check the information boundary.** Before writing non-public or potentially sensitive material anywhere in the repository, follow `skills/check-information-boundary.md`. A human curation decision does not automatically mean the destination/audience is appropriate.
8. **Preserve source provenance.** Save useful source material under `intake/` or `knowledge/sources/` only after the destination check passes.
9. **Extract only durable information.** Ignore conversational filler, research scaffolding, and redundant wording.
10. **Update before creating.** Amend existing canonical material when the information belongs there.
11. **Keep assertions appropriately atomic.** Put volatile/disputable assertions in claims and broader explanations in concepts/summaries.
12. **Assign freshness when useful.** For current-state knowledge that can become stale, set or update `last_reviewed`, `volatility`, and `review_after` using `skills/review-freshness.md`. Do not add freshness churn to purely historical objects.
13. **Link sources.** Never manufacture a source ID, citation, URL, author, or date.
14. **Check conflicts.** Compare new assertions with existing claims, sources, and contribution history. Use `skills/conflicts.md` for meaningful mismatches.
15. **Create one contribution event.** For the approved semantic write, create a `contribution` object under `knowledge/contributions/`. Record who contributed, when, which agent/tool recorded it, relevant source IDs, and every canonical object materially created or changed. If the information-boundary gate required explicit human destination confirmation, preserve that lightweight handling decision in the contribution record.
16. **Validate and rebuild views.** Run `scripts/validate_kb.py` and `scripts/build_indexes.py` when the environment permits.

## Contribution event rule

A single approved conversational push normally creates **one** contribution event even when it updates several canonical objects. A later material interaction creates another contribution event.

Do not create contribution events for typo fixes, formatting changes, generated indexes, safe file renames with no semantic change, or other non-semantic maintenance.

See `docs/provenance.md` and `templates/contribution.md`.

## When the input is a URL

A dropped link is a request to work with the source, not automatic permission to canonicalize everything on the page.

1. Open/read the page when your environment permits it.
2. Identify publisher/organization, title, author if available, publication/update date if available, and URL.
3. Prefer an original/primary source when reasonable.
4. Teach the user what the source contributes, with citations close to material sourced claims.
5. Compare it with relevant existing context and contribution history.
6. Recommend the small set of durable additions or updates worth preserving.
7. Ask before writing unless the user explicitly authorized automatic capture.
8. Run the information-boundary check if the page is authenticated, non-public, or otherwise sensitive.
9. On approval, preserve the page as source provenance and create the contribution event for the approved push.

If the page cannot be accessed, say so; do not infer its contents from the URL or title.

## Expected response before writing

The user should receive value even if nothing is committed. A good manual response includes the important findings, visible citations/links, relevant conflicts or changes to prior understanding, a concise recommendation of what should enter the context base, and one lightweight approval question.

## After approval

Canonicalize the approved set and its contribution event, then tell the user succinctly what was added or updated and surface only unresolved consequential conflicts/questions.

## Automated exception

Scheduled or unattended sweeps follow `skills/sweep.md`. Their contribution record should identify the automation as contributor and the executing agent/tool separately. Automation cannot self-approve a sensitivity gate that requires human confirmation.

## Guardrail

This repository is public. Only capture clearly public information here. Human confirmation does not override the public boundary.
