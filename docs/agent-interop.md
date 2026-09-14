# Agent Interoperability

The context base defines **semantic behavior**, not a required agent runtime.

Any agent should be able to use it if the agent can read repository files. Write access, shell access, search, connectors, external-source access, and Git operations improve what the agent can do but do not change what the knowledge means.

## Universal contract

`AGENTS.md` is the source of truth for agent behavior. `skills/` contains task workflows. Platform-specific instructions may help a particular runtime discover those files, but must not redefine the ontology, conflict rules, manual learning loop, or canonicalization behavior.

This keeps the repository usable by coding agents, conversational agents, enterprise platforms, autonomous harnesses, and open-source models.

## Manual interaction contract

When a human is actively researching with the agent, all runtimes should aim for the same semantic flow:

```text
INVESTIGATE → TEACH → CURATE → COMMIT
```

The exact UI can vary, but the agent should:

1. retrieve relevant existing context;
2. investigate the supplied or requested sources;
3. teach the user what matters before writing;
4. keep external-source citations visible when the runtime supports citations or links;
5. recommend the durable items worth preserving and explain why;
6. ask for a lightweight relevance decision;
7. canonicalize only the approved set unless advance authorization was explicit.

This keeps the user engaged in learning and judgment while leaving clerical work to the agent.

## Link/source behavior

A URL is a source candidate. An agent with browsing or connector access should read it, explain its contribution, cite material claims, compare it against relevant canonical context, and propose what should be preserved.

An agent without external-source access should say that it cannot inspect the link in its current runtime and should not invent the source contents. If the user supplies the text or another accessible representation, the agent can continue from that material.

Citation rendering may differ by platform. Preserve the principle rather than a vendor-specific citation syntax: source-derived claims should remain traceable to the source.

## Capability modes

### Read-only agent

The agent can retrieve and explain knowledge. It may investigate external sources if its runtime permits and can propose exact repository updates, but must not claim it wrote them.

### Repository-writing conversational agent

The agent may perform approved capture through repository APIs. During interactive research it should teach and curate before canonical writes rather than treating write capability as permission to save everything it finds.

### Local coding agent

The agent can work from a normal clone, search/edit files, inspect websites or other sources when its environment allows, run `scripts/doctor.py`, rebuild indexes, and use the repository's normal Git workflow. Manual research still follows the same teach-first contract.

### Enterprise workflow/agent

The platform may expose approved document, meeting, search, web, or repository connectors. Those connectors are inputs/outputs around the repository workflows; connector-specific IDs and credentials should not become required canonical infrastructure. Interactive enterprise agents should preserve the teach/curate step for human sessions.

### Autonomous agent

An autonomous runner should use bounded sweeps, retrieve before writing, validate after writes when possible, and escalate only consequential ambiguity. When there is no human present, it may follow the automated review policy in `skills/sweep.md` rather than simulating a teaching conversation.

Autonomy is not permission to silently reverse established claims or delete provenance.

## Optional adapters

It is reasonable to add files for a specific platform, such as a Claude skill, Copilot instructions, an MCP server, Microsoft agent configuration, or another adapter.

An adapter should be thin:

1. point the agent to `README.md` and `AGENTS.md`;
2. map user phrases/actions to the workflows in `skills/`;
3. expose repository read/write/search and approved external-source capabilities;
4. preserve the manual investigate → teach → curate → commit loop;
5. preserve source traceability/citations in whatever form the platform supports;
6. optionally invoke the standard scripts;
7. keep vendor-specific state outside canonical knowledge.

If removing an adapter would make the knowledge base unintelligible or unusable, the adapter has become too important.

## Retrieval rule

Do not require every agent to load the entire corpus into context. Start with `generated/INDEX.md` when available or search by subject, then retrieve the relevant canonical objects and their provenance. Expand only as the question requires.

## Writing rule

Agent memory, chat history, vector indexes, and model summaries are caches or retrieval aids. They are not authoritative merely because an agent produced them. If information should persist for the team, write it into the canonical repository with the appropriate epistemic type and provenance after the applicable approval/review step.