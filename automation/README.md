# Automation

This directory holds runner-agnostic job definitions for recurring knowledge ingestion and maintenance.

`automation/sweeps.example.json` demonstrates the contract. Copy it to an internal environment and replace example sources with approved connectors or source queries.

The configuration is intentionally boring JSON so agents and ordinary scripts can read it without an additional dependency. The actual scheduler may be an internal agent platform, CI, cron, workflow engine, or another approved system.

Do not commit credentials, tokens, or confidential source identifiers.