# Automation

This directory holds **runner-agnostic examples** for recurring knowledge ingestion and maintenance.

`automation/sweeps.example.json` demonstrates scheduling/task intent only. It is not an execution environment, permission profile, sandbox definition, connector configuration, or compliance policy.

The actual runner may be an enterprise agent platform, CI system, cron job, workflow engine, local autonomous agent, or another approved system. That runner inherits and enforces its own identity, credentials, tool access, browser/shell/network/filesystem permissions, sandbox rules, approvals, checkpoints, and compliance controls.

A runner should invoke the referenced workflows under `skills/` rather than invent a parallel knowledge-ingestion policy.

For work that is prepared from this context base but executes elsewhere, see `docs/external-tasking.md`, `skills/prepare-task-context.md`, and `skills/ingest-task-results.md`.

## Public vs private destinations

This public repository may run sweeps over public sources for testing and public research. Do not point a public-repository job at private conversations, internal documents, confidential connectors, personal data, or non-public company sources.

When this framework is copied into an approved private/internal environment, the runner may use whatever approved sources/connectors that environment supplies. Their credentials/configuration should remain outside canonical knowledge.

## Secrets and state

Do not commit credentials, tokens, private connector identifiers, machine-specific paths, browser profiles, or permission policies here.

Scheduler credentials, access policy, retries, checkpoints, and resumability belong in the execution environment. They are operational state, not the source of truth for team knowledge.
