# Skill: Weekly Hypothesis Questions

Use this when a product team asks questions such as:

- "What are five questions about our hypotheses we should answer this week?"
- "Where should we focus discovery this week?"
- "Which unknowns are most worth resolving next?"

## Goal

Turn the current hypothesis set and surrounding product context into **five high-value, realistically answerable learning questions** for the coming week.

This is a prioritization skill, not a generic brainstorming exercise. Start from what the context base already knows, what remains uncertain, and which answers could change a meaningful product decision.

## Inputs

Retrieve the smallest relevant set of:

- active/open hypotheses;
- related claims and observations;
- unresolved questions;
- recent decisions;
- relevant product, customer, workflow, and business entities;
- source freshness and confidence;
- known contradictions or weakly supported assumptions;
- contribution history when it helps explain why an assumption exists.

Scope to the named product, product area, or decision context. If scope is genuinely ambiguous and materially changes the result, surface the ambiguity instead of silently combining unrelated hypotheses.

## Procedure

1. **Inventory the live hypotheses.** Identify which hypotheses are active, supported, weakened, stale, disputed, or poorly evidenced.
2. **Connect hypotheses to decisions.** Ask what decision, investment, roadmap choice, positioning choice, measurement choice, or user-experience choice could change if each hypothesis were answered.
3. **Find the evidence gaps.** Separate unknowns from questions that already have enough evidence. Check freshness as well as quantity of evidence.
4. **Generate candidate learning questions.** Phrase questions so an answer could materially strengthen, weaken, split, or retire one or more hypotheses.
5. **Test weekly answerability.** Prefer questions for which meaningful evidence could plausibly be obtained within roughly one work week in the executing environment. Do not assume specific tools or permissions.
6. **Rank by expected learning value.** Prioritize questions that combine high decision impact, high uncertainty, and realistic answerability.
7. **Select five.** Avoid five variants of the same underlying unknown. Prefer a portfolio of questions that attacks the most consequential uncertainty from different angles.
8. **Identify follow-on investigation.** When a question requires evidence outside the repository, describe the evidence needed in capability-neutral terms. Use `skills/prepare-task-context.md` if handing the investigation to another runtime.

## Ranking heuristic

Use judgment rather than a rigid score, but consider:

- **decision impact** — would the answer change what we do?
- **uncertainty** — is this genuinely unresolved?
- **evidence weakness** — are current claims thin, stale, indirect, or contradictory?
- **answerability this week** — can useful evidence plausibly be gathered now?
- **breadth of learning** — could the answer resolve several connected hypotheses?
- **cost of being wrong** — is the current assumption driving meaningful investment or risk?

Do not prioritize a question merely because it is interesting.

## Expected output

Return exactly five prioritized questions unless the user asks for a different number.

For each question include:

### N. The question

**Hypotheses touched:** canonical hypothesis IDs or names.

**Why this matters now:** the decision or uncertainty it affects.

**What we currently believe:** a concise statement of the relevant context and confidence.

**What is missing:** the specific evidence gap, contradiction, or freshness problem.

**What evidence would answer it:** describe observations, data, interviews, workflow evidence, product behavior, commercial evidence, or other signals needed without prescribing environment-specific tooling.

**Likely knowledge-base impact:** which claims, hypotheses, questions, summaries, or entities would likely be confirmed, refined, disputed, superseded, or created.

## Quality bar

A strong weekly question is:

- falsifiable or meaningfully discriminating;
- connected to a real product decision;
- grounded in current context rather than generic PM advice;
- narrow enough to make progress this week;
- broad enough that the answer changes understanding;
- explicit about what evidence would count.

Avoid:

- questions already answered by current evidence;
- vague prompts such as "what do users want?";
- research with no plausible decision consequence;
- assuming access to analytics, customers, production systems, or internal tools the runtime may not have;
- treating five questions as five tasks that must all be executed automatically.

## Relationship to tasking

This skill chooses **what is worth learning next**. It does not decide how the environment will execute the investigation.

If one or more questions are selected for autonomous follow-up:

1. use `skills/prepare-task-context.md` to prepare the relevant context and verification target;
2. let the external runtime inherit its own tools, permissions, and controls;
3. return findings through the normal run-report/evidence contract;
4. use `skills/ingest-task-results.md` before updating canonical knowledge.
