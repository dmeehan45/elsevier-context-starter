# Skill: Ingest External Task Results

Use this when an external agent/runtime returns findings, evidence, or a run report that may change the context base.

## Goal

Turn external task results into durable knowledge without treating the external worker as automatically authoritative and without depending on that worker's runtime-specific trace format.

## Procedure

1. **Identify the run.** Capture a run ID if provided, runtime/agent identity when available, execution date/window, and any material access limitations.
2. **Separate observation from inference.** Distinguish what the worker directly inspected or verified from what it concluded.
3. **Check evidence.** Preserve or link evidence that is permitted and useful. Do not convert unsupported agent assertions directly into established claims.
4. **Retrieve existing context.** Search the relevant canonical objects, source provenance, freshness, conflicts, and contribution history.
5. **Classify each candidate change.** Determine whether the result confirms, refines, supersedes, contradicts, reframes, or is orthogonal to existing knowledge.
6. **Create source/observation records when appropriate.** A durable external run report may be represented as a source; direct findings may be observations derived from that source.
7. **Apply the normal knowledge rules.** Use `skills/conflicts.md`, ontology status rules, and update-before-create behavior.
8. **Preserve contribution provenance.** For material writes, create a contribution event recording who/what authorized or initiated the knowledge update and which repository-aware agent performed the write. The external investigating agent belongs in the run/source provenance unless it also directly performs the canonical write.
9. **Validate.** Run the repository validation/index steps when the environment permits.
10. **Report what changed.** State what was confirmed, updated, disputed, left unresolved, or rejected from canonicalization.

## Return-report expectations

A useful result from an external worker should provide, when available:

- task/run identifier;
- execution timestamp or window;
- runtime/agent identity;
- systems/sources actually inspected;
- direct observations;
- evidence references;
- inferred conclusions kept separate from observations;
- unresolved questions or access gaps;
- proposed changes to existing canonical IDs or proposed new knowledge.

Do not fail merely because a runtime cannot provide every field. Preserve what is known and do not invent missing provenance.

## Runtime limitations are evidence about the run

If the worker could not inspect part of the task because of permissions, inaccessible pages, missing tools, or other environmental constraints, retain that limitation in the run/source record when it affects interpretation.

Do not treat "not observed" as "does not exist."

## Direct writeback

If a future trusted runner can write directly to this repository, it should still follow this semantic workflow before canonicalizing results. Runtime write permission does not grant epistemic permission to silently reverse established knowledge, delete provenance, or collapse contradictory evidence.

## Manual vs unattended ingestion

When a human is actively reviewing the returned report, use the normal teach/curate behavior before consequential writes.

For an approved unattended workflow, low-risk confirmations and additive observations may be applied according to the configured external policy, while material contradictions and destructive changes should remain reviewable.

See `docs/external-tasking.md` and `docs/provenance.md`.
