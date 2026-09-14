# Skill: Sweep Sources

Use this for periodic ingestion across a bounded set of conversations, interviews, notes, documents, feeds, or alerts.

## Goal

Find durable new knowledge and changed knowledge without creating duplicate pages, turning repeated language into false certainty, or broadening access to sensitive information by accident.

## Procedure

1. Define the sweep boundary: sources, date range, or changed material since the previous sweep.
2. Check that the destination repository is appropriate for every source in the sweep. A public repository may ingest public information only.
3. Apply `skills/check-information-boundary.md` to non-public, authenticated, or potentially sensitive sources before durable ingestion. Automation cannot self-approve a `HUMAN_CONFIRM` case.
4. For each eligible source, identify candidate observations, claims, concepts, hypotheses, decisions, questions, and entities.
5. Batch candidates by subject before writing. This makes cross-source agreement and conflict visible.
6. Search the canonical corpus for existing equivalents and relevant contribution history.
7. Prefer updates to existing objects over new files.
8. Treat multiple mentions from the same upstream origin as one evidence lineage, not independent confirmation.
9. Preserve meaningful source provenance. Record source IDs and dates when available.
10. Run the conflict workflow for contradictions and supersession.
11. Assign or update freshness metadata for current-state knowledge using `skills/review-freshness.md` when the sweep genuinely verifies it.
12. Create contribution provenance for material writes. Use a stable automation contributor label such as `automation:market-scan` or `automation:weekly-conversation-sweep`, record the executing agent/tool separately, and link every materially changed object through `contribution_ids`.
13. Do not create contribution events for generated indexes, formatting, or other non-semantic maintenance.
14. Do not rewrite stable content merely to harmonize style.
15. Finish with ontology maintenance and regenerate indexes when the environment permits it.

## Automation behavior

A routine sweep should be safe to run unattended within the permissions and information boundary of its destination repository. It may automatically:

- add clearly eligible, non-conflicting observations and source records;
- enrich existing concepts and summaries;
- add provisional claims/hypotheses;
- resolve obvious aliases;
- mark clear time-based supersession;
- close a question when evidence clearly answers it;
- confirm or refresh current-state objects when the evidence is direct and the information boundary is clear.

It should queue review rather than guess when:

- authoritative sources materially conflict;
- a proposed update reverses an established claim;
- two apparently duplicate concepts may encode a meaningful distinction;
- source authority materially affects the result;
- the operation would delete unique evidence;
- the source or candidate content is potentially highly confidential, restricted, or ambiguously shareable.

A sweep's ability to read a source is not permission to make that source retrievable to everyone who can access the destination context base.

## Contribution granularity

Prefer one contribution event per coherent sweep run or bounded ingestion batch. If a large sweep spans unrelated domains or materially different source sets, split contribution events so a later human can understand which run changed which objects.

See `docs/provenance.md`.

## Freshness sweeps

A freshness sweep is a special case. Start from `generated/FRESHNESS_QUEUE.md`, then use `skills/review-freshness.md` to verify only the due objects and related evidence needed to evaluate them.

Do not treat the freshness queue itself as a schedule; cadence belongs to the external runner.

## External alerts

Market scans, press releases, regulatory updates, and similar external alerts should enter as sources first. Extract claims with dates and scope. External publication does not make a claim automatically true; preserve who said it.

## Public repository guardrail

If the destination repository is public, sweep public sources only. Do not ingest private conversations, internal meeting notes, confidential documents, restricted connector data, personal data, or other non-public company information. Route those sweeps to the approved private/internal copy instead. Human approval cannot override this public boundary.
