---
id: nursing-student-technology-environment-2026
type: summary
status: active
created: 2026-09-17
last_reviewed: 2026-09-17
source_ids:
  - source-nursing-student-technology-access-2026
  - source-nursing-student-population-demographics-2026
  - source-nurse-postlicensure-education-lifecycle-2026
contribution_ids:
  - contribution-2026-09-17-nursing-student-technology-environment
related:
  - nursing-learner-career-lifecycle
  - nursing-learner-population-and-career-lifecycle-2026
  - shadow-health
---

# Nursing student technology environment — 2026

## Orientation

The most useful technology model is not “nursing students are mobile-first.” It is a **multi-device ecology with different devices serving different jobs**.

For most learners, the practical stack is:

- **laptop:** academic workhorse;
- **smartphone:** always-present companion and point-of-care reference device;
- **tablet:** optional or institution-specific secondary device;
- **desktop:** backup or home/online-program workstation for some learners;
- **VR/simulation/telehealth hardware:** usually institution-provided rather than personally owned.

This distinction matters because device familiarity does not equal device suitability. A learner may be highly fluent on a smartphone but still need a full Windows/macOS laptop for secure exams, simulations, statistical software and other required applications.

## What students are likely carrying

Broader higher-education research consistently shows laptop + smartphone as the dominant pair. EDUCAUSE's 2021 QuickPoll found 81% of respondents using a laptop as the primary academic device and 56% using a smartphone as the secondary device. Earlier access studies found smartphone/laptop access near universal among undergraduates.

Nursing-specific evidence points in the same direction. One undergraduate nursing survey found smartphone ownership at 87.6%, laptop ownership at 76% and tablet ownership at 47.1%, with devices used for academic tasks, communication and electronic-resource access. The study is not a current U.S. census, so the exact percentages should not be generalized nationally.

## The laptop is still the safest product baseline

Current nursing-school requirements repeatedly converge on full laptops:

- Johns Hopkins: laptop required; Windows/macOS; Chromebooks and many tablets do not meet requirements;
- Duke: all nursing students require a functioning laptop;
- Michigan: all undergraduate and graduate nursing students need laptop access;
- Chamberlain: computer/laptop required, with mobile access incomplete and iPads excluded from some exam workflows;
- Rutgers: BYOD model with laptop-compatible secure testing requirements;
- Maryland: laptop required for most programs, iPads not supported for exams;
- Texas A&M: traditional/second-degree BSN students require laptops for coursework/testing;
- Duquesne: laptop required, iPad optional companion, smartphone recommended.

The compatibility constraint is often **assessment software rather than ordinary coursework**. Examplify/ExamSoft and related secure-testing platforms commonly exclude Chromebooks, mobile operating systems and unsupported processors/OS versions.

For a simulation provider, “works in a modern browser” is therefore necessary but insufficient. The product enters an already constrained device stack.

## Tablets are a meaningful but inconsistent secondary surface

Tablets should not be ignored, but they are not yet a universal primary platform.

Three patterns exist:

1. **optional companion:** Duquesne frames iPad as an optional device for ebooks and point-of-care apps;
2. **accepted primary device:** Binghamton allows laptop or iPad for papers, presentations, video and testing subject to platform requirements;
3. **institution-provisioned:** Rochester provides configured iPads to ABSN and RN-to-BS learners through its iROC initiative.

This suggests that tablet support could create value for selected workflows, but a tablet-only product strategy would not fit the broad nursing-program environment.

## Smartphone use changes by context

### Outside clinical practice

The smartphone is the most portable surface for:

- messaging/email;
- checking LMS/course status;
- quick reference/search;
- scanning/uploading documents;
- short-form study/review;
- notifications;
- authentication/2FA;
- backup connectivity through cellular data.

### In clinical practice

Smartphone use becomes heavily contextual.

NYU explicitly requires clinical-sequence students to have a smartphone/PDA for email and point-of-care clinical/drug resources. Other schools permit smartphones for educational purposes only. Many programs defer to clinical-site policy, prohibit personal use, ban photography/recording and forbid storing patient-identifying information.

The product implication is important: **the phone may be the most familiar device in a learner's life and still be unavailable at the exact moment of clinical care.**

A product intended for in-clinical use therefore needs a deployment model compatible with facility policy, privacy expectations, infection-control/workflow norms and possibly hospital-provided workstations/devices.

## Program pathway changes the technology setup

### Traditional BSN / ABSN

Likely environment:

- personal laptop brought to class and testing;
- smartphone carried daily;
- campus Wi-Fi and LMS;
- secure exam software;
- institution simulation/lab hardware;
- occasional tablet use;
- tightly constrained personal-device use in clinical settings.

### ADN / community-college learner

Same core stack, but affordability/device age may matter more. Programs frequently operate BYOD with institution labs/loaners as backstops. We should not assume that “owns a laptop” means a current high-performance laptop.

### RN-to-BSN / online graduate learner

More home/work-based use:

- laptop or desktop;
- home broadband;
- webcam/headset;
- LMS/video-conferencing;
- employer/hospital network as a possible access point but also a possible firewall constraint;
- smartphone for communication and quick tasks.

The working learner's technology problem is often **reliability and interoperability across home, employer and university environments**, not device unfamiliarity.

### APRN / graduate clinical learner

Adds more professional tools:

- clinical-reference apps;
- telehealth platforms;
- EHR exposure;
- video-based skills/OSCE workflows;
- institution-provided simulation/telehealth equipment;
- possible remote proctoring and synchronous class tools.

## Connectivity is part of the device environment

A compatible computer is not enough.

Current nursing programs commonly require reliable broadband. Hospital and workplace networks can introduce restrictive firewalls that prevent video, conferencing or browser-based educational tools. EDUCAUSE research also shows that unstable Internet and device failures create measurable student stress and coursework disruption.

For working nurses, the real technical journey can span:

**home Wi-Fi → cellular phone → employer/hospital network → campus Wi-Fi → clinical site network**.

A robust education product should therefore be designed for network variability, graceful recovery and transparent compatibility checks rather than assuming a stable residential-broadband session.

## What this means for Shadow Health today

Current Shadow Health DCEs are browser-based WebGL/JavaScript applications delivered primarily to desktop/laptop computers running Windows/macOS. Continuous Internet access is required; current support guidance gives 3 Mbps as the minimum download speed. There is no native iOS/Android application. Headphones are recommended for audio fidelity and supported browsers can use a microphone for speech-to-text.

This means the current product's primary surface matches the **formal nursing-school workhorse** well: the laptop.

But it does not fully inhabit the learner's broader device ecology. The smartphone is the always-present secondary surface and tablets are meaningful at some institutions. That creates possible roles for companion workflows without implying that the entire simulation should be moved to mobile.

Possible companion-surface jobs include:

- preparation/prebrief;
- reminders and assignment status;
- short remediation;
- flash review;
- reflection/debrief follow-up;
- progress/competency views;
- faculty/learner notifications;
- continuation between school and clinical experiences where policy permits.

These are product hypotheses, not evidence that learners currently want Shadow Health on phones.

## The highest-value next data source is internal

Shadow Health's current public IT/legal documentation says the platform already collects non-personally-identifiable hardware/client information including browser, operating system/version, CPU, RAM, GPU/video memory and related graphics characteristics. Elsevier says it uses this to set development hardware targets and support customers.

That creates an unusually strong opportunity to replace generic higher-education proxies with **actual Shadow Health hardware distributions**.

The internal analysis should answer:

- Windows vs macOS share;
- Chrome/Edge/Safari/Firefox share;
- RAM distribution;
- CPU generation/performance distribution;
- integrated vs discrete GPU prevalence where identifiable;
- low-end or unsupported-device failure rate;
- hardware differences by institution/program geography if permissible;
- correlation between hardware/network class and support tickets, load failures, session abandonment or assignment completion time.

Public documentation confirms telemetry exists but not whether all of these dimensions are retained/queryable in a form suitable for product analytics. That should be verified internally.

## Design guardrails

### Do not equate smartphone familiarity with mobile-primary learning

Students may use phones constantly while preferring laptops for complex academic work and being restricted from phone use in clinical settings.

### Do not equate device ownership with technical readiness

Age of device, memory, browser support, GPU/WebGL support, battery life and connectivity materially change whether a learner can complete a simulation successfully.

### Do not design only for the median device

Nursing education includes community-college learners, working adults and distributed learners for whom replacing a laptop or upgrading broadband may be a meaningful financial cost.

### Do not require specialized learner-owned hardware without a strong reason

VR headsets, telehealth carts and high-fidelity simulation technology are much more naturally institution-provided resources.

### Treat accessibility as part of the technology stack

Input method, keyboard navigation, audio fidelity, captions/transcripts, assistive technology compatibility and screen design can be as important as CPU/RAM support. Hardware compatibility alone is not access.