---
title: "MFC Measurement System v3 — final independent integration review"
type: independent-integration-review
status: pass-with-conditions
reviewer_role: independent measurement scientist / psychometric challenger
date: 2026-08-30
scope: v3 architecture, organisation agreement, report template, build/test protocol and change ledger
---

# Decision: PASS WITH CONDITIONS for internal candidate progression

The v3 pack is internally coherent enough to progress as MFC’s **controlled build candidate**. It resolves the central validity problem: routine organisation reports are explicitly limited to delivery and participant-reported signals among respondents, while causal intervention-effect claims require the separately designed comparative lane.

It must not yet be fielded. The named conditions below are required before a functioning form is approved for real data collection. They are operational completion conditions, not a reason to reopen the measurement architecture.

## Scope and evidence reviewed

- `outputs/MFC-MEASUREMENT-SYSTEM-v3.md`
- `outputs/MFC-ORGANISATION-MEASUREMENT-REPORT-TEMPLATE-v3.md`
- `outputs/MFC-ORGANISATION-MEASUREMENT-AGREEMENT-v3.md`
- `outputs/MFC-MEASUREMENT-BUILD-AND-TEST-PROTOCOL-v3.md`
- `outputs/MFC-MEASUREMENT-SYSTEM-v3-CHANGE-LEDGER.md`

Latest founder direction was applied as the controlling source: selected Essentials and Foundations use an organisation-approved standard private evaluation; individual participant answers remain non-identifying and unavailable to managers; MFC returns organisation-level reporting; Radar and manager work are included but not conflated with participant outcomes.

## What now passes

### 1. Purpose and claim integrity

The two-lane design is correct. Standard evaluation has a defined job—delivery, learning, opportunity, participant-reported intentional next-step events and barriers—without falsely upgrading these signals into objective behaviour or causal effectiveness. The Level A–D ladder, system wording, agreement and report template all agree that the standard organisation report stops at A–B.

The enhanced lane correctly requires a pre-specified outcome, credible comparator, allocation/analysis/fidelity rules and a distinct component comparison if Radar or manager work is tested. It does not borrow causal language from routine feedback forms.

### 2. Measures and denominators

The form architecture has a coherent construct chain:

`delivery/exposure → immediate discrimination and access → later opportunity → participant-reported intentional next-step event → barrier/context`.

B1/B2 are consistently labelled MFC-authored process diagnostics, not a validated scale or unaided retrieval test. C1 is the correct gate for C2–C6. `No opportunity`, `No`, `Not sure`, `Prefer not to say`, missing, non-return and branch-not-shown remain separate. The C2/C5 inconsistency rule is explicit and carried into the report template.

The agreement, delivery record and report template together correctly prevent the most common aggregate-reporting error: treating respondents as all workers. Eligible, attended, offered, submitted, link-distributed and linked-response counts are all named. B4’s denominator and branch state are correct.

### 3. Organisation, Radar and manager boundary

The three-record model is a major improvement. Participant pathway data, delivery/fidelity data and Radar/manager implementation data have distinct units, owners, permitted inferences and prohibited inferences. The system does not turn a delivered manager/Radar component into proof of employee or organisational change, and it does not join a participant code to a manager/implementation record.

### 4. Privacy and operational coherence in the candidate

The standard-information script, agreement and code rules align: MFC asks all attendees to complete the standard evaluation; a person may skip/exit without employment or service consequences; managers cannot access answers or response status; generic return links and shuffled unassigned codes avoid person-to-code linkage. The documents appropriately make any assertion of anonymity conditional on an actual platform metadata check.

Small-cell suppression, contextual re-identification review, synthetic test fixtures, least-privilege testing and no-manager-present test scenarios are concrete and proportionate safeguards.

### 5. Change control

The change ledger accurately traces why v3 differs from v2 and provides acceptance tests for the material decisions. Versioning is carried across service, form, delivery and component records.

## Conditions required before fielding

### Condition 1 — freeze the exact participant-facing support and data-retention wording

**Finding:** v3 requires a non-monitored support end screen and a code-based record-location/deletion route, but it references rather than reproduces the final text. It also says data are separately held with restricted access but does not state the final retention/deletion schedule in the v3 pack.

**Required completion:** add or formally reference one controlled participant-information/end-screen artifact that contains: final non-monitored support wording; exact deletion request process and limitation; final retention/destruction schedule; storage/role boundary; and the privacy description verified for the selected platform. Do not promise record location/deletion until the platform and no-key code route demonstrably support the stated process.

**Acceptance test:** the built form, code card, organisation agreement and privacy/data record use identical approved wording; an end-to-end synthetic deletion request is demonstrably handled as described.

### Condition 2 — reconcile the selected contracted service versions

**Finding:** v3 makes standard evaluation part of selected Essentials/Foundations **service versions**, while the prior core service packs state that routine data/return are outside their core boundary. This is reconcilable, but must be explicit in the service catalogue/contract version so delivery staff do not improvise.

**Required completion:** designate the exact sellable service versions that include standard private evaluation, and cross-reference v3. Keep the learning-service minutes and form time boundary explicit.

**Acceptance test:** a delivery lead can identify from the service ID whether forms are required to be offered, which form version applies, who distributes the generic link, and that no form consumes core teaching time.

### Condition 3 — technical, accessibility and role-access evidence bundle

**Finding:** the protocol is strong but remains a plan.

**Required completion:** run every build-and-synthetic-test protocol scenario, retain the listed evidence bundle, and independently inspect the actual form, raw export, generated report and access roles.

**Acceptance test:** all protocol checks pass, including no hidden email/login/IP/token/analytics collection incompatible with participant wording; no status leakage in the manager-present simulation; correct branch/denominator/report suppression behaviour; and private keyboard/mobile/screen-reader routes.

### Condition 4 — qualified human review before collection

**Finding:** the candidate correctly withholds legal/privacy/support/measure approval, but fielding needs those decisions.

**Required completion:** obtain proportionate qualified review of actual platform/data handling, participant notice, support/safeguarding position, and any WHO-5/IMTTAQ inclusion. WHO-5 and IMTTAQ remain outside the base route unless separately controlled.

**Acceptance test:** the approvals/decisions are dated, recorded against the exact platform/form version, and any conditions are implemented and re-tested.

## Minor corrections for the build copy

1. Standardise `Prefer not` to `Prefer not to say` in every multiselect implementation and export label.
2. In the report template, define whether a form is “submitted” only when its required code is valid; use that same definition in the delivery record and dashboard.
3. Add a machine-readable `report_level=A-B` field to the mock report so causal wording cannot appear through manual template reuse.
4. Record whether aggregate eligible/attendee counts were host-supplied or directly observed by MFC, so the report can state the source rather than overstate certainty.

## Gate decision

| Gate | Result | Basis |
|---|---|---|
| Mission and decision alignment | pass | Evaluation serves product learning and a credible future effectiveness route. |
| Evidence and claim integrity | pass | Routine reports and causal inference are cleanly separated. |
| Audience and accessibility | pass with conditions | Strong design rules; real build/accessibility checks remain. |
| Safety, privacy and reputation | pass with conditions | Strong boundaries; platform-specific wording and qualified review remain. |
| Conceptual integrity | pass | Participant, delivery and implementation constructs are distinct. |
| Technical/operational verification | revise before fielding | No configured platform or test evidence yet. |
| Change control/reuse | pass | v3 ledger and version fields are adequate. |

## Explicit inference boundary for the first organisation report

The first standard report may say, for example: **“Among return respondents who reported a relevant moment and answered the event item, X% reported intentionally choosing what to do next.”** It may also report exactly what MFC, Radar and manager components were delivered. It may not say MFC improved workers, wellbeing, performance, culture, or organisational outcomes, and it may not attribute participant reports to the intervention.

## What this review did not test

This review did not test real participant comprehension, actual response rates, disability access, platform metadata, privacy/legal authority, the reliability of an enhanced target assay, WHO-5/IMTTAQ permissions, manager usability or the functioning build. It is an independent internal review of the integrated candidate—not expert, legal, privacy, clinical, accessibility or participant validation.

## Next decision gate

Proceed to controlled build and synthetic verification after Conditions 1–2 are reflected in the controlled materials. Fielding requires Conditions 3–4 and a fresh independent re-review of the actual configured system.
