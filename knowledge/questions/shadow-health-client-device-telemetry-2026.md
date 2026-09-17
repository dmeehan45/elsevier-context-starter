---
id: shadow-health-client-device-telemetry-2026
type: question
status: open
created: 2026-09-17
last_reviewed: 2026-09-17
source_ids:
  - source-nursing-student-technology-access-2026
contribution_ids:
  - contribution-2026-09-17-nursing-student-technology-environment
related:
  - nursing-student-technology-environment-2026
  - shadow-health
---

# What devices and technical environments do actual Shadow Health learners use?

Public Shadow Health documentation states that the platform already collects non-personally-identifiable client information including browser, operating system/version, CPU, RAM, video-card details and video memory for development targeting and support.

The public evidence does **not** reveal the actual distribution among current learners.

## Internal questions to resolve

1. What proportion of current assignment sessions run on Windows versus macOS?
2. What is the browser distribution, and how is it changing over time?
3. What proportion of learners are near minimum CPU/RAM/GPU specifications?
4. How old/low-powered is the long tail of supported hardware?
5. Which hardware/browser combinations generate disproportionate support tickets, WebGL failures, load failures or session abandonment?
6. Can device characteristics be aggregated by program type, institution archetype, geography or learner level without creating privacy or contractual issues?
7. Do working graduate/RN learners have a meaningfully different device mix from traditional prelicensure learners?
8. Is screen size/resolution captured or inferable? If not, should it be?
9. Is network quality captured beyond support-side diagnostics? Can we measure connection-related interruption/recovery in product analytics?
10. What proportion of learners attempt to access Shadow Health from unsupported tablets/phones/Chromebooks before switching devices or seeking support?
11. Which accessibility/assistive-technology configurations are most common, and where do current compatibility gaps occur?

## Why this matters

These answers should inform browser support, performance budgets, rendering targets, compatibility testing, graceful-degradation strategy and whether mobile/tablet companion experiences are worth prioritizing.

The existing telemetry means this question should be answered from first-party product evidence before making major device-strategy decisions from external market proxies.