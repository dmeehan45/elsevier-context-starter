# Skill: Check Information Boundary

Use this before durable ingestion or before sending repository context to another agent/runtime when the material could contain sensitive, confidential, regulated, or narrowly shared information.

## Goal

Prevent the context base from becoming an accidental oversharing layer.

This skill is an additional repository guardrail. It does **not** replace the runtime's permissions, enterprise data-governance controls, access policy, or legal/compliance requirements.

Human confirmation can approve a repository-level ambiguity; it cannot override a technical or organizational restriction.

## Apply this gate before

- adding material from meetings, chats, email, private documents, connectors, internal systems, or authenticated websites;
- automated sweeps over non-public sources;
- copying raw excerpts into `intake/` or `knowledge/sources/`;
- preparing a task context packet that will leave the current runtime/repository boundary;
- widening the audience for existing knowledge.

Public-source research with clearly public content can normally pass without a separate human confirmation.

## Sensitivity signals

Treat material as potentially sensitive when it includes or may reveal:

- credentials, tokens, passwords, keys, authentication/session material, or secret configuration;
- personal, customer, learner, patient, employee, or other identifiable private data;
- protected health, financial, legal, or regulated information;
- attorney-client privileged or legal-strategy material;
- unreleased product plans, strategy, pricing, financial performance, forecasts, M&A, negotiations, or executive deliberation;
- security vulnerabilities, incident details, internal access architecture, or exploitable operational information;
- confidential customer/partner terms, contracts, datasets, or proprietary research;
- content explicitly marked confidential/restricted or obtained from a source whose sharing boundary is unclear;
- information that would materially change audience or risk if summarized into a broadly shared team knowledge base.

This list is intentionally broad and non-exhaustive.

## Decision states

### CLEAR

The material is clearly appropriate for the destination and intended audience under the current environment's rules.

Proceed with the normal capture/handoff workflow.

### HUMAN_CONFIRM

The content appears potentially highly confidential, restricted, or ambiguously shareable, and no environment-level rule already blocks it.

Before storing or exporting the material, ask one focused question such as:

> This appears to contain non-public product strategy and may become visible to everyone with access to this context repository. Please confirm that this repository and audience are an appropriate destination for this material.

The confirmation should identify the destination/audience being approved, not merely say "yes, save it."

Until confirmation is received:

- do not write the sensitive candidate into canonical knowledge;
- do not place the raw content in `intake/` as a workaround;
- do not include it in an external task context packet;
- do not create a review artifact that itself leaks the sensitive content.

If approved, preserve lightweight handling confirmation in the contribution record when practical:

```yaml
handling_confirmation: human-confirmed
handling_confirmed_by: person:example
handling_confirmed_at: 2026-09-14T15:00:00-06:00
```

These fields record the repository-level decision. They do not represent RBAC or legal authorization.

### BLOCK

Do not persist or export the material when:

- the runtime/environment says the destination or action is not allowed;
- the content contains credentials/secrets that should not be stored in team context;
- policy, contract, law, or explicit source restrictions prohibit the destination/use;
- a required human confirmation is declined or cannot be obtained.

Report the limitation without reproducing unnecessary sensitive detail.

## Automated sweeps

Automation cannot self-approve a `HUMAN_CONFIRM` case.

For an ambiguous/sensitive candidate:

1. leave the candidate outside the repository's durable context;
2. surface a minimal, non-sensitive notice to an authorized human through whatever review mechanism the runtime provides;
3. continue processing unrelated safe material when possible;
4. ingest the candidate only after explicit destination confirmation.

A sweep's ability to read a source does not imply permission to make that source broadly retrievable in this repository.

## External task handoff

Before including context in a task packet for another runtime, consider both:

- **source sensitivity** — what kind of information is this?
- **destination/runtime audience** — who or what will gain access by receiving it?

If the runtime's authorization to receive the material is unclear and the material is potentially highly confidential, use `HUMAN_CONFIRM` rather than assuming portability equals permission.

## Minimize exposure

Even when material is approved for the destination:

- preserve only what is useful;
- prefer references to approved source systems over copying large raw documents;
- avoid unnecessary personal identifiers or secrets;
- summarize sensitive source material when full reproduction adds no retrieval value;
- keep source provenance sufficient to recover context without duplicating the entire source.

## Public repository rule

This repository is public. For this public starter, only clearly public material is eligible for durable ingestion. Human confirmation does not convert internal/confidential information into public-safe content.

A future approved private/internal copy may permit more categories, but the same gate should remain in place for highly confidential or ambiguously shareable information.
