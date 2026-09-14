# Automation

This directory holds **runner-agnostic** job definitions for recurring knowledge ingestion and maintenance.

`automation/sweeps.example.json` demonstrates the contract. The actual runner may be an enterprise agent platform, CI, cron, a workflow engine, a local autonomous agent, or another approved system.

The configuration is intentionally plain JSON so agents and ordinary scripts can read it without an additional dependency. A runner should invoke the referenced workflow under `skills/` rather than invent a parallel ingestion policy.

## Public vs private destinations

This public repository may run sweeps over public sources for testing and public research. Do not point a public-repository job at private conversations, internal documents, confidential connectors, personal data, or non-public company sources.

When this framework is copied into an approved private/internal environment, replace the example source names with approved connectors or source queries for that environment.

## Secrets and state

Do not commit credentials, tokens, private connector identifiers, or machine-specific paths. Scheduler credentials and access policy belong in the execution environment, not in canonical knowledge.

Cursor/checkpoint state may live in the approved runner when necessary. It should be treated as operational state, not as the source of truth for team knowledge.