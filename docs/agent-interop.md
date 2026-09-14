# Agent Interoperability

The context base defines **semantic behavior**, not a required agent runtime.

Any agent should be able to use it if the agent can read repository files. Write access, shell access, search, connectors, and Git operations improve what the agent can do but do not change what the knowledge means.

## Universal contract

`AGENTS.md` is the source of truth for agent behavior. `skills/` contains task workflows. Platform-specific instructions may help a particular runtime discover those files, but must not redefine the ontology, conflict rules, or canonicalization behavior.

This keeps the repository usable by coding agents, conversational agents, enterprise platforms, autonomous harnesses, and open-source models.

## Capability modes

### Read-only agent

The agent can retrieve and explain knowledge. It may propose exact updates, but must not claim it wrote them.

### Repository-writing agent

The agent can perform capture/sweep/maintenance by editing files through Git hosting APIs. If it cannot execute Python, it should perform the documented checks semantically and disclose that executable validation was not run.

### Local coding agent

The agent can work from a normal clone, search/edit files, run `scripts/doctor.py`, rebuild indexes, and use the repository's normal Git workflow.

### Enterprise workflow/agent

The platform may expose approved document, meeting, search, or repository connectors. Those connectors are inputs/outputs around `skills/capture.md` and `skills/sweep.md`; connector-specific IDs and credentials should not become required canonical infrastructure.

### Autonomous agent

An autonomous runner should use bounded sweeps, retrieve before writing, validate after writes when possible, and escalate only consequential ambiguity. Autonomy is not permission to silently reverse established claims or delete provenance.

## Optional adapters

It is reasonable to add files for a specific platform, such as a Claude skill, Copilot instructions, an MCP server, Microsoft agent configuration, or another adapter.

An adapter should be thin:

1. point the agent to `README.md` and `AGENTS.md`;
2. map user phrases/actions to the workflows in `skills/`;
3. expose repository read/write/search capabilities;
4. optionally invoke the standard scripts;
5. keep vendor-specific state outside canonical knowledge.

If removing an adapter would make the knowledge base unintelligible or unusable, the adapter has become too important.

## Retrieval rule

Do not require every agent to load the entire corpus into context. Start with `generated/INDEX.md` when available or search by subject, then retrieve the relevant canonical objects and their provenance. Expand only as the question requires.

## Writing rule

Agent memory, chat history, vector indexes, and model summaries are caches or retrieval aids. They are not authoritative merely because an agent produced them. If information should persist for the team, write it into the canonical repository with the appropriate epistemic type and provenance.