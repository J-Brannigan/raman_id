# Business Case: Automated Raman Mineral Identification

## Title Page
- **Document owner:** Product and Commercial Team  
- **Version:** 0.1  
- **Date:** 15 Feb 2026

## Executive Summary
The business objective is to increase instrument win rates, grow recurring software revenue, and improve customer outcomes by introducing an Automated Raman Mineral Identification capability that accelerates and standardises mineral interpretation for both expert and non-expert users.

The timing is right for three reasons. First, customer teams are under pressure to increase sample throughput without expanding headcount. Second, many operators in field and industrial settings do not have deep spectroscopy expertise on every shift. Third, buyers increasingly evaluate instrument purchases as software-led workflow decisions, not hardware-only decisions.

The proposed capability combines fast candidate suggestions, confidence-aware guidance, and auditable reporting in a way that supports, rather than replaces, human judgement. It is designed for mixed deployment contexts including cloud-connected laboratories and offline field operations.

Today, most customers are not using machine learning models in routine Raman interpretation. They are using manual spectrum comparison, library search and match scores, and expert judgement to decide final identification.

**North Star outcome:** Enable customers to make faster, more consistent, and defensible mineral identification decisions at scale, while growing software attach and long-term account value.

## Market and Customer Landscape
### Segment Overview
| Segment | Primary users | Typical environment | Main purchase driver | Definition of success |
|---|---|---|---|---|
| Mining and exploration | Field geologists, project geochemists, central lab teams | Field camps and regional labs | Faster go or no-go decisions on samples | More samples processed per shift with fewer expert escalations |
| Commercial labs | Lab managers, spectroscopy analysts | High-throughput laboratory | Turnaround time and report consistency | Predictable SLA delivery and lower rework rates |
| Academic labs | Principal investigators, PhD students, lab technicians | University laboratories | Usability for mixed-skill users and teaching value | Reproducible outputs and easier onboarding of new students |
| Gemmology and jewellery | Gemmologists, authenticity specialists | Retail labs and specialist labs | Reliable screening and defensible documentation | Faster screening with clear escalation path for difficult stones |
| Industrial QA | QA managers, production technicians | Factory QC labs and line-side stations | Repeatability and reduced production delays | Consistent pass or hold decisions and fewer batch disputes |
| Government and forensics | Forensic analysts, technical officers | Controlled labs, occasional field deployment | Traceability, chain-of-custody support, auditability | Transparent evidence trail and reproducible interpretations |

### Segment Detail
#### Mining and Exploration
Primary jobs-to-be-done include rapid mineral phase checks during drilling campaigns, anomaly triage, and prioritisation of samples for further lab work. Work alternates between constrained field conditions and central lab verification. Constraints include intermittent connectivity, variable sample quality, operator fatigue, and pressure to make decisions quickly. Success means quicker geological interpretation cycles, fewer unnecessary follow-up tests, and less dependence on one senior spectroscopist.

#### Commercial Labs
Commercial testing labs are measured on throughput and turnaround agreements. They need repeatable operation across multiple technicians and shifts. Constraints include high daily sample volume, mixed sample provenance, and commercial penalties for delays. Success means lower median time-to-report, fewer report amendments, and stronger confidence when presenting findings to paying clients.

#### Academic Labs
Academic settings are diverse, with expert and novice users sharing instruments. Jobs-to-be-done include research-grade identification, student training, and method development. Constraints include turnover of student operators, limited budget, and varying instrument care practices. Success means fewer failed runs, smoother training, and publishable confidence in reported identifications.

#### Gemmology and Jewellery
Teams need fast screening for likely composition and treatment indicators, with clear escalation when spectra are ambiguous. Environments are usually controlled, but time pressure is high in high-value transactions. Constraints include liability concerns, reputational risk, and high scrutiny of documentation. Success means rapid first-pass classification with robust evidence packaging for second opinion and certification workflows.

#### Industrial QA
QA teams run repeatable checks on incoming materials, intermediates, and finished products. Their job is to prevent non-conforming material from moving downstream. Constraints include line speed, non-expert operators, and integration with existing quality systems. Success means fewer line stoppages, fewer false rejects, and standardised records that withstand audits.

#### Government and Forensics
Forensics and government labs require strong chain-of-custody discipline, controlled SOP compliance, and clear rationale for analytical conclusions. Constraints include strict documentation standards, legal scrutiny, and conservative adoption criteria. Success means traceable, reproducible decisions and reduced time spent preparing explanatory documentation for reviews.

### Competitive and Alternative Workflows
Current alternatives are often a blend of manual expert interpretation, conventional library search tools, generic spectroscopy software, and outsourcing to specialist labs. These approaches can work, but they typically struggle with speed, consistency, and scalability. Manual interpretation does not scale with sample volume. Generic software can be powerful but difficult for non-specialists. Outsourcing adds delay, cost, and loss of operational control.

## Current State Problems Grounded in Workflows
### End-to-End Workflow Today
1. Sample receipt and preparation.
2. Instrument setup and calibration checks.
3. Spectrum capture and basic pre-processing.
4. Library search and match review against reference spectra.
5. Manual spectrum comparison by operator, including peak-by-peak checks.
6. Expert escalation for uncertain cases.
7. Report drafting and quality check.
8. Final sign-off and distribution.

In most accounts, this workflow is rules-based and human-led. Customers generally are not using machine learning models for day-to-day mineral identification decisions.

### Where Time Is Spent
- Repeated captures caused by weak signal quality.
- Manual review of candidate matches and peak comparisons.
- Waiting for expert review on ambiguous spectra.
- Report revisions when decisions are challenged.

### Where Errors Occur
- Inconsistent sample prep and focus quality.
- Under-recognised calibration drift.
- Overconfidence in weak or ambiguous library matches.
- Incomplete capture of acquisition context in final reports.

### Typical Failure Modes in Routine Use
- **Fluorescence background:** obscures diagnostic peaks and creates false confidence in partial matches.
- **Noisy spectra:** low signal-to-noise complicates interpretation, especially for junior operators.
- **Instrument calibration drift:** subtle shift affects match quality and comparability over time.
- **Mixed samples:** overlapping signatures reduce certainty and increase disagreement between reviewers.
- **Operator variability:** different levels of skill produce different outcomes from the same sample.
- **Ambiguous matches:** multiple plausible candidates with no clear workflow guidance for next step.

### Operational Bottleneck: Expert Dependence
Most organisations rely on a small number of spectroscopy experts to resolve difficult cases. This creates a queue, especially during peak demand or staff absence. The business impact includes longer turnaround times, uneven quality between shifts, and risk concentration in a few individuals.

## Proposed Capability in Product Terms
### Feature Definition: Automated Raman Mineral Identification
The proposed feature provides guided identification support as a native workflow within instrument software.

1. User captures a spectrum or uploads an existing file.
2. System returns an immediate top-N candidate list.
3. Each candidate includes a confidence score and fit rationale.
4. Interface highlights key spectral regions that most influenced the suggestion.
5. If confidence is low, the user receives clear next-step guidance.

### What Changes from Today
Today, operators manually compare spectra and interpret library matches with limited decision support, and most teams do not use machine learning models in routine workflows. With the new capability, the software provides immediate ranked candidates, confidence-aware guidance, and structured review steps while preserving human sign-off. This shifts teams from ad hoc manual comparison toward a standardised, auditable identification workflow.

### Low-Confidence Guidance Workflow
When confidence is below threshold, the software should propose practical actions:
- recapture spectrum with adjusted integration time,
- verify calibration status,
- retry with alternate laser wavelength where available,
- improve sample positioning or preparation,
- escalate to expert review with full context packaged.

### Human in the Loop by Design
The system recommends, the operator decides. Final interpretation remains a human responsibility with software support. The UI should make approval, override, and comment workflows explicit. Any override should be recorded with reason codes to preserve learning and traceability.

### Deployment and Operational Constraints
- **Offline mode required** for field exploration teams and restricted facilities.
- **On-device execution required** for low-latency use and disconnected operation.
- **Latency expectations:** candidate results should appear within a few seconds in routine operation.
- **Device constraints:** software must perform reliably on embedded hardware and rugged laptops.
- **Auditability:** every identification should retain method version, instrument metadata, and user actions.

## Value Proposition and Business Outcomes
### Customer Value by Workflow Stage
| Workflow stage | Current issue | Expected improvement with capability |
|---|---|---|
| Capture and first pass interpretation | High variability in non-expert interpretation | Standardised candidate ranking and confidence display |
| Ambiguous cases | Frequent expert escalation | Better triage through confidence gating and guided recapture |
| Reporting | Inconsistent rationale quality | Structured, exportable evidence trail |
| Team onboarding | Long time to operator competence | Guided workflow that reduces dependency on tacit expert knowledge |

### Quantified Outcome Ranges
These ranges are conservative, scenario-dependent, and intended for business planning:
- **Time saved per sample:** 20 to 45 percent reduction in interpretation time.
- **Throughput increase:** 15 to 35 percent more samples per operator per shift in routine cases.
- **Training time reduction:** 25 to 50 percent faster onboarding to independent first-pass operation.
- **Rework reduction:** 10 to 30 percent fewer repeat analyses caused by avoidable interpretation errors.

### Revenue Impact
- Higher **software attach rate** on new instrument deals due to differentiated workflow value.
- Tiered **licensing expansion** from basic library match to advanced identification and audit features.
- Improved **instrument conversion** in competitive bids where software usability is a deciding factor.
- Increased **renewal resilience** through deeper workflow integration and perceived switching cost.

### Cost Impact
- Lower support burden from basic interpretation questions.
- Fewer escalations to specialist application scientists.
- Reduced time spent by customer success teams troubleshooting avoidable workflow errors.

### Customer Outcome Impact
- Faster turnaround from spectrum capture to report-ready interpretation.
- More consistent cross-operator outputs.
- Better defensibility in regulated or high-liability contexts through traceable records.

## Buyer Personas and Decision Drivers
### Persona Table
| Persona | What they care about | Typical objections | Evidence they need |
|---|---|---|---|
| Lab Manager | Throughput, staffing efficiency, consistency | Fear of false confidence and rework | Throughput benchmarks, repeatability studies, pilot results |
| Principal Investigator | Scientific credibility, reproducibility, publishable rigour | Concern about black-box behaviour | Validation documentation, explainability views, version traceability |
| Field Geologist | Speed, offline reliability, practical guidance | Connectivity and ruggedness concerns | Offline demos, latency evidence, field pilot references |
| QA Manager | Standard work, auditability, deviation control | Integration complexity with existing SOPs | Audit log examples, SOP mapping, qualification package |
| Procurement | Total cost of ownership, vendor stability, ROI | Subscription fatigue and unclear value realisation | ROI model, packaging clarity, reference customers |
| Compliance Officer | Traceability, access control, governance | Unclear accountability for final decision | Audit trail design, role-based permissions, quality controls |

## User Research Summary
### Research Activities Conducted
#### 1. Contextual Inquiry in a High-Throughput Commercial Lab
Two-day on-site observation of sample intake, measurement, interpretation, and reporting. Included shadowing two senior analysts and three junior operators across day and evening shifts.

#### 2. Ride-Along with Exploration Field Team
Three-day field observation during active drill campaign support. Focused on connectivity constraints, device handling, and decision pressure during shift handovers.

#### 3. Four-Week Operator Diary Study
Ten operators across mining, academic, and industrial QA contexts logged uncertain identifications, escalation triggers, and time spent per sample.

### Key Findings
- Operators use library match scores differently by seniority, leading to inconsistent decision thresholds.
- Uncertainty handling is often undocumented, creating weak handover quality.
- Field users prioritise reliability and clarity over advanced configurability.
- Junior operators need explicit guidance on what to do when confidence is low.
- Experts spend significant time reviewing cases that could be triaged earlier.
- Report writing quality is strongly affected by whether acquisition metadata is captured automatically.
- Teams want top-N options with rationale, not a single definitive answer.
- Confidence indicators must be intuitive and avoid implying certainty where ambiguity exists.
- Accessibility matters, especially contrast, text clarity, and predictable interaction flow on shared workstations.
- In mixed-sample contexts, users want the software to acknowledge ambiguity rather than force a brittle answer.
- Trust improves when users can see highlighted spectral regions tied to candidate suggestions.
- Adoption risk increases when users believe software output cannot be challenged or annotated.

### Paraphrased User Feedback
> Paraphrased user feedback: "In the field I need an answer quickly, but I also need to know when not to trust it."

> Paraphrased user feedback: "Our best analyst is becoming the bottleneck for every difficult spectrum."

> Paraphrased user feedback: "A top three list with confidence is more useful than one confident-looking result."

> Paraphrased user feedback: "If the software says low confidence, tell me exactly what to try next."

> Paraphrased user feedback: "When operators rotate, interpretation style changes too much between shifts."

> Paraphrased user feedback: "We can defend our decisions when we have a complete audit trail, not just a final label."

> Paraphrased user feedback: "Offline use is non-negotiable for parts of our exploration workflow."

> Paraphrased user feedback: "Students can run the instrument, but they struggle to explain why a match is plausible."

> Paraphrased user feedback: "I need a report format that my quality team can review quickly without extra manual editing."

## Requirements: Product and Commercial
### Functional Requirements (Acceptance Style)
- The system shall accept spectrum input from live capture and file upload workflows.
- The system shall return a ranked top-N candidate list for each analysis.
- The system shall present a confidence score for each candidate in a clear, non-technical format.
- The system shall display key spectral regions that support candidate suggestions.
- The system shall support a low-confidence pathway with recommended operator actions.
- The system shall allow the operator to accept, reject, or escalate recommendations.
- The system shall capture instrument, acquisition, and operator metadata automatically where available.
- The system shall produce an exportable report including candidate set, confidence, metadata, and review actions.
- The system shall maintain an auditable action history including overrides and reason codes.

### Non-Functional Requirements (Acceptance Style)
- The system shall provide routine identification results within defined latency targets for supported hardware profiles.
- The system shall operate in fully offline mode for designated workflows and synchronise records when connectivity returns.
- The system shall use versioned, deterministic software packages suitable for validated deployment environments.
- The system shall preserve traceability between result output and software version used.
- The system shall maintain stable performance across expected instrument operating ranges.

### Data Governance Requirements
- The system shall clearly define what data is stored locally and what may be synchronised.
- The system shall support customer control over retention policies for spectra and metadata.
- The system shall support opt-in telemetry with transparent scope and disablement controls.
- The system shall respect customer IP concerns by allowing local-only operation without mandatory cloud transfer.

### Security and Privacy Expectations
- Role-based access controls shall restrict analysis approval and administrative functions.
- Audit logs shall be tamper-evident and exportable for quality review.
- Enterprise deployments shall support documented backup and recovery policies.
- Customer data handling shall align with internal security review requirements and contractual commitments.

## Success Metrics and KPIs
### KPI Framework by Audience
| KPI type | Metric | Target threshold | Applicable segments |
|---|---|---|---|
| Product | Median time-to-identification | 30 percent reduction within 6 months of launch | Mining, commercial labs, industrial QA |
| Product | Unknown or unresolved outcome rate | 20 percent relative reduction in routine samples | Commercial labs, academic labs |
| Product | Feature adoption | 60 percent of active instrument users engage weekly | All segments except highly restricted deployments |
| Product | 6-month retention of active use | Above 75 percent in paid tier | Mining, commercial labs, industrial QA |
| Commercial | Software attach on new instrument sales | +15 percentage points in targeted regions | Mining, commercial labs, gemmology |
| Commercial | Upsell from basic to advanced tier | 20 percent of eligible installed base in year one | Commercial labs, QA, government |
| Commercial | Churn reduction for software renewals | 10 percent relative reduction | All subscription segments |
| Commercial | Support ticket volume on interpretation issues | 25 percent reduction | All segments |
| Customer | Samples processed per operator shift | 15 to 30 percent improvement | Mining, commercial labs, QA |
| Customer | Cross-operator repeatability on same sample set | Measurable variance reduction against baseline SOP | QA, government, commercial labs |
| Customer | Time to operator independence after training | 30 percent reduction | Academic labs, mining, QA |

### Measurement Approach
Baseline metrics should be captured during pre-launch pilots and compared at 30, 90, and 180 days post-deployment. Segment-specific scorecards should be used to prevent overgeneralisation across very different workflows.

## Rollout Strategy and Packaging
### Beta Programme with Design Partners
- Select 8 to 12 design partner accounts across mining, commercial labs, industrial QA, and one government-style environment.
- Define pilot success criteria before deployment, including turnaround time, confidence handling, and operator feedback.
- Run fortnightly product and customer success reviews to capture workflow friction and update playbooks.

### Sales Enablement Plan
- Build role-specific demo scripts for lab managers, QA leaders, and field operations.
- Prepare battlecards against manual interpretation status quo, generic spectroscopy tools, and outsourced testing.
- Develop pilot-to-production conversion playbook with required evidence checklist.
- Create case-study templates focused on operational and financial outcomes.

### Packaging and Pricing Logic
No list prices are specified here. Packaging should follow value tiers:
- **Tier 1: Core Match** for standard library search and reporting.
- **Tier 2: Guided Identification** for top-N, confidence, and low-confidence recommendations.
- **Tier 3: Enterprise Assurance** for advanced audit, governance controls, and validation documentation.

Licensing logic should support per-instrument and enterprise options, with explicit upgrade path from Tier 1 to Tier 2 based on throughput and staffing pain points.

### Training and Support Playbook
- Operator onboarding modules by skill level.
- Supervisor training on confidence thresholds and escalation policy.
- Quality team module on audit trail review and report defensibility.
- Customer success check-ins at 30 and 90 days with usage and outcome dashboard review.

## Risks and Mitigations
### Key Business Risks
#### Misidentification and Downstream Impact
Incorrect identification can drive expensive and harmful decisions, including wrong process choices, inaccurate quality release decisions, and reputational damage.

#### Domain Shift Across Instruments and Settings
Performance may vary with instrument configuration, operating conditions, sample preparation, and local workflow practices. This can erode trust if not managed.

#### Customer Trust and Explainability Gaps
If users cannot understand why suggestions were produced, adoption may stall even if objective performance is strong.

### Mitigation Strategy
- Use confidence gating to prevent over-assertive outputs in ambiguous conditions.
- Present top-N candidates and explicitly allow unknown outcome when evidence is insufficient.
- Require human review checkpoints for critical workflows.
- Provide structured, transparent rationale views including highlighted spectral regions.
- Maintain validation packs by instrument family and usage context.
- Implement ongoing post-release performance monitoring with clear escalation pathways.

### Regulatory and Quality Considerations
Adopt an ISO-style quality management mindset with controlled documentation, versioned release processes, verification records, and change control discipline. Position the capability as decision support within documented SOP frameworks, not autonomous final authority in high-consequence settings.

## Assumptions and Open Questions
1. Sufficient labelled reference spectra are available across priority mineral classes for launch scope.
2. Instrument metadata quality is adequate for robust traceability in most installed environments.
3. Offline operation is mandatory for at least mining and selected government workflows.
4. Customers will accept top-N plus confidence as a practical improvement over single-answer outputs.
5. Design partner accounts are willing to participate in structured pilot measurement.
6. Customers will permit opt-in anonymised telemetry at a rate high enough to guide roadmap decisions.
7. Existing support organisation can absorb new onboarding and success playbooks with minor resourcing changes.
8. Sales teams can effectively position tiered software value without heavy discounting.
9. Enterprise buyers will prioritise auditability and governance sufficiently to justify higher-tier packaging.
10. Internal release and quality processes can deliver deterministic versioning and validation artefacts at target cadence.
11. Field hardware profiles in target accounts can meet on-device latency expectations.
12. Regulatory and legal review will approve positioning language that emphasises human decision accountability.

## Appendix
### Glossary
- **Raman shift:** Difference in wavenumber between incident and scattered light, used to characterise material-specific vibrational features.
- **Fluorescence:** Background emission that can mask Raman peaks and reduce interpretability.
- **Baseline:** Underlying signal trend that must be handled to interpret peak structure reliably.
- **Library match:** Comparison of measured spectrum against reference spectra to rank likely candidates.
- **Top-N candidates:** Ranked shortlist of plausible identifications rather than one forced output.
- **Confidence score:** Normalised indicator of certainty used for triage and review decisions.
- **Oriented spectra:** Reference spectra measured with crystallographic orientation considered.
- **Unoriented spectra:** Reference spectra measured without orientation constraints.
- **Audit trail:** Chronological record of user actions, system outputs, and metadata used for review.
- **Unknown outcome:** Explicit state used when available evidence does not support a reliable identification.

### Example Before vs After Workflow Narrative
**Before:** A junior operator captures a spectrum, runs a library search, and gets several similar matches. Unsure which is credible, they email a senior analyst and wait several hours for review. The report is delayed, and shift handover notes are incomplete.

**After:** The operator captures the spectrum and receives a top three list with confidence and highlighted key regions. The system flags medium confidence and recommends a recapture with adjusted integration time. After recapture, confidence improves. The operator submits for supervisor review with full metadata and action history already attached, reducing turnaround time and avoiding ad hoc email escalation.

### Example Exported Report Outline
1. Report header
- Sample ID, project or batch reference, operator, date and time.

2. Instrument and acquisition metadata
- Instrument ID, laser wavelength, integration time, calibration status, capture location.

3. Identification results
- Top-N candidate list, confidence per candidate, unknown status if applicable.

4. Interpretability summary
- Highlighted spectral regions supporting the ranked candidates.

5. Operator actions and review
- Recapture attempts, parameter adjustments, escalation actions, override reason codes.

6. Final decision and sign-off
- Reviewer identity, approval status, comments, timestamp.

7. Version and traceability
- Software version, reference library version, workflow template version.

8. Audit attachment index
- Linked raw spectrum file identifiers and change history.
