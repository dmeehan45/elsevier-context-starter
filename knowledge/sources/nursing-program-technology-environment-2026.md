---
id: source-nursing-program-technology-environment-2026
type: source
source_type: public-web-research
created: 2026-09-17
last_reviewed: 2026-09-17
contribution_ids:
  - contribution-2026-09-17-nursing-program-technology-environment
---

# Nursing program and faculty technology environment — 2026

## Purpose

Research bundle for understanding the technology backdrop into which nursing educational technology is deployed: faculty/staff endpoints, learning platforms, assessment systems, clinical-placement/compliance systems, simulation-center infrastructure, authentication/security, support and integration patterns.

The central finding is that a nursing program rarely has one coherent technology stack. It operates a **federated set of institution-wide, school-specific and nursing-specific systems owned by different teams**.

## Representative end-user / faculty computing layer

### Duke School of Nursing TECH Hub
Source: https://nursing.duke.edu/student-resources/technical-support

Duke School of Nursing maintains a dedicated SON-IT function supporting faculty, staff and students. The service covers device/connectivity issues, enterprise resources such as Canvas, presentations, video creation/editing, classroom recording, transcription, proctoring/polling and after-hours student support.

### Penn Nursing IT
Sources:
- https://www.nursing.upenn.edu/its/resources/learning-technology-services/
- https://www.nursing.upenn.edu/its/services/service-desk/

Penn Nursing exposes a school-level technology layer covering Canvas, Zoom, Panopto, Poll Everywhere, Qualtrics, REDCap, Respondus, cloud storage, Office 365, service desk support and desktop services.

### Washington State University College of Nursing
Source: https://nursing.wsu.edu/college-of-nursing-it-support/

WSU is a particularly clear example of the stack split:
- Desktop IT: computer/laptop issues, Office 365, Okta;
- Learning IT: Canvas, Panopto, ATI, Exxat;
- Simulation: dedicated SimCapture service desk for skill validation, lab practice, OSCE evaluation and simulation.

This is a useful reference architecture for the number of ownership domains a vendor may encounter at one school.

## Learning-management and teaching layer

### Johns Hopkins School of Nursing
Sources:
- https://nursing.jhu.edu/faculty-research/faculty/instructional-design-technology-and-support/keep-teaching-at-jhson/
- https://canvas.jhu.edu/faculty-resources/third-party-tools/

Johns Hopkins identifies Canvas as the School of Nursing LMS for every course/section and uses Zoom, Respondus and Panopto/other integrated tools for synchronous teaching, assessment and video. JHU's Canvas environment supports a broad set of third-party integrations and notes that integrated tools are institutionally vetted for accessibility/privacy.

### CU Denver / Anschutz example
Source: https://www.ucdenver.edu/offices/office-of-information-technology/tools-services/for-staff/detail-page/academic-technology

Canvas course shells are created from the institutional student-information system and official enrollments are provisioned automatically. Panopto, Zoom and Respondus sit around that LMS. This illustrates an important architecture principle: the LMS is often downstream of the authoritative SIS/registrar roster rather than the primary system of record.

## Clinical placement, compliance and experience-tracking layer

### University of Washington — Exxat migration
Source: https://students.nursing.uw.edu/clinicals-compliance/compliance-onboarding/

UW is moving incoming cohorts from CastleBranch/DISA to Exxat beginning Fall 2026. Exxat is used for compliance requirements, clinical placements, evaluations, timesheets and related clinical-learning activity.

### UMass Amherst — consolidation into Exxat Prism
Source: https://www.umass.edu/nursing/student-services/exxat

UMass describes Exxat Prism as a comprehensive clinical education management system used for health/preclinical requirements, placement, learning activities, course management and accreditation compliance. As courses transition, UMass is retiring Typhon/CastleBranch use for those workflows.

### Rutgers — Exxat and Typhon
Sources:
- https://nursing.rutgers.edu/students/clinical/clinical-clearance-requirements/
- https://nursing.rutgers.edu/typhon/

Rutgers uses Exxat for clinical placements, compliance, eligibility and program requirements, while NP/Nurse Midwifery learners use Typhon to document patient encounters, diagnoses/procedures, medications and clinical notes. A complete log may later support certification/licensure/credentialing.

### CastleBranch examples
Sources:
- https://nursing.uic.edu/about/college-insider/student-resources/student-compliance/
- https://nursing.uiowa.edu/academics/undergraduate-clinical-simulation-course-policies

CastleBranch/DISA remains widely used for immunization, background-check, drug-screen and compliance-document workflows. Faculty can receive compliance notifications and clinical participation can be blocked when requirements lapse.

## Simulation-center technology layer

### University of Michigan Clinical Learning Center
Source: https://nursing.umich.edu/academics/clinical-learning-center

Michigan's nursing Clinical Learning Center combines high-fidelity simulation suites, mid-fidelity skills spaces, real clinical equipment and bedside computers for electronic-health-record access.

### Duke Center for Nursing Discovery
Source: https://nursing.duke.edu/centers-and-institutes/center-nursing-discovery/cnd-team-directory

Duke's simulation technical-operations role maintains high-fidelity manikins, computer stations, telepresence robots and video-recording equipment and supports an electronic-health-record training environment. This makes clear that simulation is an operational technology environment, not just course content.

### SimCapture examples
Sources:
- https://health.stthomas.edu/nursing/clinical-experience/center-for-simulation/
- https://www.liberty.edu/nursing/simulation-center/facilities/
- https://nursing.emory.edu/degrees-programs/simulation-and-clinical-experience/emory-nursing-learning-center
- https://nursing.wsu.edu/college-of-nursing-it-support/

Simulation centers commonly pair high/mid-fidelity manikins and/or standardized patients with networked cameras, microphones, observation/control rooms, A/V capture, debriefing and assessment software. SimCapture is one prominent platform for session management, recording, review and evaluation. Emory describes PTZ-camera recording with faculty annotation/timestamps for debriefing. Liberty describes camera-equipped rooms, telepresence and SimCapture. St. Thomas uses SimCapture for managing, recording and assessing simulation/debrief activity.

Other simulation-center technology can include virtual reality, telepresence robots, task trainers, medication-dispensing systems, EHR training environments, anatomage tables and specialized clinical equipment.

## Identity, security, accessibility and institutional governance

The nursing stack generally inherits institution-wide identity and security controls such as NetID, SSO, Okta/Duo/two-factor authentication, VPN, role-based access and centrally vetted third-party applications.

Examples:
- WSU nursing supports Okta alongside Office 365 and nursing applications.
- Stony Brook SimCapture uses institutional SSO plus Duo authentication.
- Johns Hopkins notes security/privacy review for third-party Canvas tools.
- Prior research in `source-nursing-edtech-governance-procurement-2026` shows institutional software purchases can also trigger cybersecurity, accessibility, privacy, procurement and legal review.

## Faculty digital competence and adoption constraints

### Large U.S. nursing faculty survey
Source: https://pubmed.ncbi.nlm.nih.gov/38884499/

A survey of 1,761 faculty in prelicensure nursing programs found that technology adoption was influenced by financial support, organizational commitment and administrative support. Faculty buy-in and time were material barriers, and respondents identified training needs in both classroom and simulation contexts.

### International educator competence study
Source: https://pubmed.ncbi.nlm.nih.gov/41646084/

A four-country study of 290 nurse educators found self-assessed overall digital competence to be moderate, with the lowest scores in safe/responsible technology use. This should not be treated as a U.S. prevalence estimate, but it supports the broader point that nursing faculty technology capability is heterogeneous.

### 2026 Delphi on nursing-faculty digital competence
Source: https://pubmed.ncbi.nlm.nih.gov/42385435/

Faculty experts identified competence domains spanning professional engagement, digital resources, teaching/learning, assessment, learner empowerment and learner digital competence. Basic digital skills were stronger than advanced content creation/problem solving, and technology integration was perceived as more mature in theoretical teaching than in clinical/lab education.

## Current Shadow Health integration position

### LTI 1.3 / LMS integration
Sources:
- https://service.elsevier.com/app/answers/detail/a_id/40014/c/18925/supporthub/evolve/
- https://evolve.elsevier.com/education/wp-content/uploads/sites/2/2024/10/LTI-Customer-One-Pager-Guide-2.pdf

Current Elsevier guidance supports LTI 1.3 for supported LMSs. Shadow Health LTI 1.3 can provide deep linking, automatic account/course creation, LMS-to-Shadow Health course templates, section support and grade passing. The Shadow Health guide identifies Canvas, Blackboard, Brightspace and Moodle as compatible with certified deep-linking workflows.

### Faculty workflow
Sources:
- https://service.elsevier.com/app/answers/detail/a_id/34855/supporthub/shadow-health/
- https://service.elsevier.com/app/answers/detail/a_id/34839/supporthub/shadow-health/
- https://service.elsevier.com/app/answers/detail/a_id/34866/supporthub/shadow-health/

Faculty configure assignment lists, dates, options, sections and syllabus information, then review student performance in Shadow Health's Results Book/Practice Readiness tools. Where integrations are absent or incomplete, results can be exported to CSV for calculations or LMS import. Elsevier also recommends/uses implementation planning and faculty training during adoption.

## Durable observations

1. **The LMS is the front door, not the whole stack.** Faculty commonly expect courseware to appear inside Canvas/another LMS and coexist with roster, gradebook, video and assessment tools.
2. **Clinical education runs a parallel operational stack.** Exxat, CastleBranch, Typhon and similar systems govern placement, compliance, hours, encounters and evaluations that are not naturally represented in a conventional LMS.
3. **Simulation centers are technology operations environments.** They include hardware, A/V capture, control rooms, manikin software, EHR training, debriefing and dedicated technical staff.
4. **Data fragmentation is normal.** Student identity, course rosters, grades, simulation traces, compliance status, placement, clinical encounters and competency evidence may live in different systems.
5. **Faculty are integrators.** In many implementations they manually align course dates, assignments, grades, simulation results, clinical evidence and curricular outcomes across systems.
6. **Technology capability varies across faculty and institutions.** Training, time, administrative support and technical support are part of product adoption, not ancillary concerns.
7. **A new product is evaluated as another system dependency.** Integration, SSO/LTI, accessibility, security, support burden, grade transfer and lifecycle maintenance matter alongside pedagogical quality.
