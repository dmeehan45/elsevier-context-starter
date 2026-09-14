# Skill: Core Product Questions

Use this when a product team wants to sharpen its understanding of the durable questions that should anchor product judgment.

The default questions are:

1. What jobs does our product do for users?
2. How well can we measure our primary success metrics?
3. What are the primary reasons users buy our product?
4. What are the primary reasons users stop using our product?
5. How aligned are our product investments and roadmap with our business objectives?

## Goal

Assess how strong the context base's current answers are to these questions, identify where the answers are weak or stale, and recommend the highest-value investigations that would materially sharpen product understanding.

This is a **knowledge-quality and decision-support skill**, not a request to invent an answer from general product-management heuristics.

## Inputs

Retrieve the smallest relevant set of:

- product and user/customer entities;
- product concepts and summaries;
- claims and observations about user behavior, buying, retention, outcomes, workflows, and value;
- hypotheses and unresolved questions;
- measurement definitions, success metrics, and evidence about observability;
- strategy, business-objective, roadmap, investment, and decision records;
- source dates, confidence, contradictions, and contribution lineage when material.

Scope to the named product or product area. If several products or customer segments have materially different answers, keep those distinctions visible rather than averaging them into one narrative.

## Procedure

For each of the five core questions:

1. **State the best current answer.** Summarize only what the repository can support.
2. **Show the evidence basis.** Identify the strongest canonical claims, observations, summaries, and sources behind the answer.
3. **Assess answer quality.** Judge completeness, confidence, freshness, segmentation, directness of evidence, and contradictions.
4. **Identify what we are assuming.** Separate supported knowledge from plausible inference, inherited belief, or untested hypothesis.
5. **Find the sharpest gap.** Ask what missing information most prevents the team from acting confidently.
6. **Turn the gap into an investigable question.** Phrase a narrower question whose answer would materially improve the core answer.
7. **Describe the evidence needed.** State what observations, data, interviews, commercial evidence, product behavior, decision records, or other signals would resolve it without prescribing environment-specific tooling.
8. **Connect to decisions.** Explain what roadmap, investment, positioning, measurement, adoption, retention, or strategy decision could change if the gap were resolved.

## Question-specific guidance

### 1. What jobs does our product do for users?

Look beyond feature descriptions. Distinguish:

- functional jobs;
- workflow jobs;
- emotional/social jobs when evidence exists;
- buyer jobs from end-user jobs;
- intended jobs from jobs actually observed;
- different jobs by segment or role.

Ask whether evidence shows what users are trying to accomplish, not merely what the product enables.

### 2. How well can we measure our primary success metrics?

Separate **having a metric name** from **being able to measure success reliably**.

Inspect:

- metric definition and ownership;
- whether the metric captures the intended outcome;
- instrumentation/data availability;
- baseline and target availability;
- segmentation;
- latency between product behavior and outcome;
- known proxies and their limitations;
- evidence that the team actually uses the measure in decisions.

A strong answer can be "we cannot currently measure this well" if that is what the evidence supports.

### 3. What are the primary reasons users buy our product?

Distinguish:

- buyer from user;
- stated purchase rationale from observed purchase behavior;
- acquisition trigger from longer-term value;
- institutional/commercial reasons from learner/user reasons;
- current evidence from historical positioning or marketing claims.

Look for evidence from purchasing, sales, customer research, implementation, adoption, and product usage rather than assuming marketing language equals buyer motivation.

### 4. What are the primary reasons users stop using our product?

Do not reduce this to formal churn if the product is institutional or episodic.

Consider:

- abandonment;
- non-renewal;
- low adoption after purchase;
- workflow substitution;
- completion/seasonality;
- implementation friction;
- poor outcome/value realization;
- changes in role, curriculum, policy, budget, or environment;
- product defects or experience friction.

Separate known causal evidence from correlation and anecdote.

### 5. How aligned are product investments/roadmap with business objectives?

Trace both directions:

```text
business objective → product investment → expected mechanism → product/user outcome → measurable signal
```

and:

```text
roadmap item → intended user/business effect → objective served → evidence/metric
```

Identify investments with no clear objective linkage, objectives with no meaningful product investment, and places where the connection exists only as narrative rather than evidence.

## Answer-quality rubric

Use a simple qualitative rating for each core question:

- **Strong** — current, reasonably complete, supported by direct evidence, and usable for decisions.
- **Partial** — useful answer exists but important segments, evidence, freshness, or causal understanding are missing.
- **Weak** — mostly inference, stale evidence, indirect evidence, conflicting claims, or major unanswered gaps.
- **Unknown** — the repository does not yet support a meaningful answer.

Do not turn this into false quantitative precision.

## Expected output

Start with a compact overview:

| Core product question | Current answer quality | Biggest gap | Why it matters |
| --- | --- | --- | --- |
| Jobs | Strong / Partial / Weak / Unknown | ... | ... |
| Success metrics | ... | ... | ... |
| Buy reasons | ... | ... | ... |
| Stop-using reasons | ... | ... | ... |
| Roadmap/business alignment | ... | ... | ... |

Then provide one section per question containing:

- **Current best answer**
- **Evidence and canonical references**
- **What we know vs. assume**
- **Sharpest unresolved question**
- **Evidence that would sharpen it**
- **Decision unlocked**

Finish with **Top investigations to run next**, ranked by expected decision value and the degree to which they improve multiple core product questions.

## Relationship to tasking

This skill identifies the gaps; it does not assume how they will be investigated.

For gaps selected for autonomous or external follow-up:

1. use `skills/prepare-task-context.md` to create a narrow context packet;
2. let the executing environment supply its own tools, identity, permissions, and controls;
3. require evidence and limitations in the returned run report;
4. reconcile results through `skills/ingest-task-results.md` before canonical writes.

## Anti-patterns

Avoid:

- filling gaps with generic product-management frameworks;
- presenting product or marketing documentation as proof of actual user behavior;
- combining buyers and users when they differ;
- calling a metric measurable merely because a KPI name exists;
- treating churn as the only form of product discontinuation;
- asserting roadmap alignment because strategy language and roadmap language sound similar;
- recommending external investigations without first checking what the context base already contains.
