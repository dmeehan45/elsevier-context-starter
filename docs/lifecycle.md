# Knowledge Lifecycle

The system separates **cheap capture** from **careful canonicalization**.

```text
conversation / document / interview / alert
                    │
                    ▼
                 intake
                    │
                    ▼
         retrieve existing context
                    │
                    ▼
       extract durable information
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   update existing        create new
          │                   │
          └─────────┬─────────┘
                    ▼
            conflict check
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      clear update      ambiguous/material
          │                   │
          ▼                   ▼
   canonicalize          review queue
                    
                    ▼
          regenerate indexes
```

## Intake

Raw intake may include incomplete notes, transcripts, URLs, pasted messages, meeting notes, or agent output. Intake is not canonical truth.

Preserve raw material when it has future evidentiary value. Ephemeral conversational instructions do not need to be saved merely because they were said.

## Promotion

Promote information when it is likely to be useful beyond the current interaction. Typical signals include:

- it changes or sharpens understanding;
- it is a reusable definition or concept;
- it records a meaningful assertion about product, users, market, workflow, strategy, evidence, or history;
- it creates or resolves an open question;
- it records a hypothesis or actual decision;
- it is likely to matter to another human or agent later.

Do not promote small talk, duplicated wording, speculative filler, or transient execution details unless they have enduring relevance.

## Update before create

Before creating a canonical page, search for the entity/concept/claim and semantic equivalents. Add to or revise an existing page when the information belongs there.

Do not let automated sweeps create parallel pages such as `clinical-judgment.md`, `clinical-judgement.md`, and `judgment-clinical.md`.

## Conflict lifecycle

A new assertion can:

- **confirm** existing knowledge;
- **refine** it by adding scope or precision;
- **supersede** it because the world changed;
- **contradict** it because sources disagree;
- **reframe** it because the old claim was too broad;
- or be **orthogonal** despite superficial similarity.

Clear temporal supersession can be handled automatically. Material semantic conflicts should be surfaced using `skills/conflicts.md`.

## Review queue

The review queue is for exceptions, not routine approvals. Add items only when an agent cannot safely resolve the issue from sources and scope.

Good review items include:

- two authoritative sources materially disagree;
- merging two concepts could erase a meaningful distinction;
- a newer claim would reverse an important established belief;
- deletion would remove unique provenance;
- the authority or scope of a source is unclear and matters to interpretation.

## Maintenance

Periodic maintenance should do work that humans otherwise forget: stale checks, orphan detection, duplicate candidates, broken links, unsupported established claims, unresolved contradictions, and index regeneration.

The maintenance process should not churn prose or reorder files merely to create activity.