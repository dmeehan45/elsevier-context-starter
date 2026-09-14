# Agent Interoperability

The context base defines **semantic behavior**, not a required agent runtime.

Any agent should be able to use it if the agent can read repository files. Write access, shell access, connectors, external-source access, browsers, sandboxes, and Git operations improve what the agent can do but do not change what the knowledge means.

## Universal contract

`AGENTS.md` is the source of truth for agent behavior. `skills/` contains portable knowledge workflows. Platform-specific instructions may help a runtime discover or invoke those workflows, but must not redefine the ontology, conflict rules, contribution provenance, manual learning loop, or external-task handoff boundary.

This keeps the repository usable by coding agents, conversational agents, enterprise platforms, autonomous harnesses, and open-source models.

## Runtime inheritance principle

When an agent uses this repository from another execution environment, the agent inherits that environment's controls.

The runtime owns:

- authenticated identity;
- credentials and secrets;
- available tools/connectors;
- browser/shell/network/filesystem access;
- sandbox/isolation policy;
- model/orchestration configuration;
- approval and human-in-the-loop rules;
- compliance controls;
- scheduling, retries, checkpoints, and resumability.

The repository must not assume, recreate, weaken, or override those controls.

Repository instructions describe **what context means and how knowledge should be handled**, not what external systems the agent is authorized to access.

See `docs/external-tasking.md`.

## Manual interaction contract

When a human is actively researching with an agent, runtimes should preserve the same semantic flow:

```text
INVESTIGATE → TEACH → CURATE → COMMIT
```

The exact UI can vary, but the agent should retrieve relevant context, investigate permitted sources, teach before writing, keep evidence traceable, recommend durable additions, ask for a lightweight relevance decision, and canonicalize only the approved set unless advance authorization was explicit.

## Link/source behavior

A URL is a source candidate. An agent with browsing or connector access should read it, explain its contribution, cite material claims, compare it against relevant canonical context, and propose what should be preserved.

An agent without external-source access should say that it cannot inspect the link in its current runtime and should not invent the source contents.

Citation rendering may differ by platform. Preserve the principle rather than a vendor-specific citation syntax: source-derived claims should remain traceable to the source.

## External task handoff

An agent may use this repository to prepare context for work that executes in another runtime.

The portable flow is:

```text
repository context
      ↓
prepare-task-context
      ↓
derived context packet
      ↓
external runtime under its own controls
      ↓
run report / evidence
      ↓
ingest-task-results
      ↓
canonical knowledge
```

The context packet is an input, not authorization. The external runtime decides whether it has the tools and permissions needed to execute the objective.

Returned findings should separate direct observation, evidence, inference, unresolved/access-limited areas, and proposed context changes. Vendor-specific traces may remain in the runtime; only durable interpretation/provenance needs to cross the boundary.

## Capability modes

### Read-only agent

The agent can retrieve and explain knowledge or prepare a context packet. It may propose exact updates but must not claim it wrote them.

### Repository-writing conversational agent

The agent may perform approved capture through repository APIs. During interactive research it should teach and curate before canonical writes.

### Local coding agent

The agent can work from a normal clone, search/edit files, use whatever tools its environment permits, run `scripts/doctor.py`, rebuild indexes, and use normal Git workflow.

### Enterprise workflow/agent

The platform may expose approved document, meeting, search, web, browser, or repository connectors. Those capabilities belong to the platform. Connector-specific credentials/configuration should not become required canonical infrastructure.

### Autonomous/external agent

An autonomous worker may receive a derived context packet and return evidence/findings. It should operate only within its runtime controls and should not interpret the packet as permission to access systems the environment has not granted.

Autonomy is not permission to silently reverse established claims or delete provenance.

## Optional adapters

It is reasonable to add a Claude skill, Copilot instruction, MCP adapter, Microsoft agent configuration, or another runtime-specific bridge.

An adapter should be thin:

1. point the agent to `README.md` and `AGENTS.md`;
2. map actions to workflows under `skills/`;
3. expose only capabilities supplied by the host runtime;
4. preserve the manual learning and external-task handoff contracts;
5. preserve source/contribution traceability;
6. optionally invoke standard validation scripts;
7. keep vendor-specific operational state outside canonical knowledge.

If removing an adapter would make the knowledge base unintelligible or unusable, the adapter has become too important.

## Retrieval rule

Do not require every agent to load the entire corpus into context. Start with search/generated navigation when useful, retrieve relevant canonical objects and provenance, then expand only as the task requires.

## Writing rule

Agent memory, chat history, vector indexes, task packets, and model summaries are caches or derived views. They are not authoritative merely because an agent produced them. Durable team knowledge belongs in the canonical repository only through the applicable source, conflict, contribution, and review workflow.
