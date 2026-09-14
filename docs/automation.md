# Automation Model

Automation should reduce knowledge administration, not create a second system to administer.

This starter does not assume a scheduler, LLM vendor, transcript system, document store, or market-data provider. Inside the approved environment, any runner can implement the same job contract.

## Job contract

Each recurring job needs only:

- a stable job ID;
- a bounded source or query;
- a cursor or time window so the job can be incremental;
- the skill to run (`capture`, `sweep`, or `maintain`);
- a destination repository/branch;
- a review policy;
- sensitivity/permission constraints.

See `automation/sweeps.example.json`.

## Recommended operating modes

### User-initiated capture

Trigger: a human says "push this into the knowledge base."

Behavior: run `skills/capture.md` immediately. Low-risk updates may be committed directly because a human initiated the action. Material conflicts are surfaced in the response and review queue.

### Recent-conversation sweep

Trigger: daily or every few days, depending on source volume.

Behavior: inspect only conversations since the previous successful cursor. Batch findings by topic, then run `skills/sweep.md`. Do not treat repetition across conversations as independent evidence unless the underlying sources are independent.

### Interview/onboarding sweep

Trigger: new notes/transcripts arrive, or a daily batch catches them.

Behavior: preserve the meeting as a source when permitted; extract observations and durable knowledge; update existing concepts/claims/summaries; preserve unresolved questions.

### Document sweep

Trigger: changed/new documents in approved stores.

Behavior: process the delta, not the entire corpus. Capture source version/date. If a new document version supersedes an old one, prefer temporal supersession over contradiction.

### External signal sweep

Trigger: alert, monthly/quarterly market scan, scheduled search, press release feed, regulatory update, competitor release notes, or similar.

Behavior: external items enter as sources first. Extract dated, attributed claims. Publication is not proof. Keep company assertions distinguishable from independent evidence.

### Ontology/quality sweep

Trigger: weekly, after a large import, or before a major planning/research cycle.

Behavior: run `skills/maintain.md`, then validation/indexing. This is where duplicates, stale claims, orphaned concepts, unsupported established claims, and unresolved contradictions are surfaced.

## Review policy

Automation should not create a daily approval inbox.

Use three write classes:

- **auto-apply:** additive, well-sourced, non-conflicting changes; obvious aliases; clear temporal updates; generated index changes.
- **apply + flag:** safe canonical update where a human may care about the change, but work should not block.
- **review-required:** material contradictions, destructive merges/deletes, unclear authoritative source, or reversal of consequential established knowledge.

A team can implement these as direct commits, branches, pull requests, an agent task queue, or another approved workflow. The semantic contract matters more than the mechanism.

## Cursors and idempotency

Recurring jobs should store enough state to know what they processed previously. Prefer source-native immutable IDs/version IDs when available; otherwise use timestamps plus content hashes.

A rerun over the same input should not create duplicate canonical objects or repeatedly strengthen confidence.

## Security boundary

Source connectors, tokens, transcripts, internal documents, and automation state belong only in the approved internal environment. This public starter contains contracts and example configuration, not live credentials or internal source identifiers.