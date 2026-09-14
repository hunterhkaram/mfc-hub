---
title: "MFC Measurement System v3 — mission evidence backbone"
type: controlled-measurement-architecture
status: superseded
owner: Hunter
maintained_by: Codex
mfc_topic: measurement
supersedes: MFC-MEASUREMENT-FORMS-CANDIDATE-v2 (as the current architecture)
superseded_by: 60-projects/measurement-strategy-v1/2026-09-04-MEASUREMENT-ARCHITECTURE-AND-COMPLETION-ENGINE.md
superseded_on: 2026-09-04
supersession_note: "Superseded 2026-09-04 by the measurement architecture build (node 2), which rebuilds the instrument set, the reporting tiers and the completion design. Retained as history; do not build from it."
---

# MFC Measurement System v3 — mission evidence backbone

## Purpose

MFC exists to help people notice meaningful everyday moments and choose what to do next when it is useful. This system makes that mission **testable**. It is not merely a satisfaction survey or internal improvement loop.

It has two evidence lanes:

1. **Standard organisation evaluation** — captured with selected Essentials and Foundations deliveries. It produces a truthful aggregate report about delivery, participant-reported learning, later opportunity, reported intentional next-step use, barriers and component implementation.
2. **Enhanced effectiveness study** — a separately approved comparative design which can test whether a defined MFC version outperforms a credible alternative on a pre-specified outcome.

Routine data are evidence of what participating respondents reported. They do not, by themselves, prove that MFC caused a change. The enhanced lane exists specifically to test that mission-level effectiveness question rather than exaggerating routine report data.

## Scope and service rule

| Service | Measurement status |
|---|---|
| Introduction | No routine participant data, form, QR, contact or follow-up in the standard service. Separately recruited research remains possible. |
| Essentials-EVAL-v1 | Standard private organisation evaluation is included when the organisation contracts this measured service version. Forms are offered before, immediately after and at day 21–28; they are outside teaching time. |
| Foundations-EVAL-v1 | Same standard evaluation architecture, with service/version-specific delivery record. |
| Radar / manager session | Separate implementation/context tracks. They are never silently joined to anonymous participant responses. |

## The three records — never one score

| Record | Unit and owner | Captures | May support | Must not support |
|---|---|---|---|---|
| 1. Participant pathway record | random-code-linked participant responses; MFC custodian | immediate process understanding, rehearsal access, later opportunity, participant-reported intentional next-step event, barriers | respondent-reported learning/use pathway | individual assessment, objective behaviour, culture change, causal effect |
| 2. Delivery/fidelity record | delivery lead; aggregate only | version, duration, material deviations, eligible/attendee/offered counts, form availability, component delivery | what MFC actually delivered and evaluation coverage | participant outcome or component impact |
| 3. Radar/manager implementation record | designated implementation lead; held separately | whether components occurred, version/dose, stated support actions and implementation barriers | component reach and organisational context | employee experience, individual trajectory, combined MFC effect percentage |

## Claim ladder

Every report labels the highest level it has earned.

| Level | Evidence required | Permitted language |
|---|---|---|
| A — delivery and response | delivery record and response flow | “MFC delivered [version] and received [n] responses at each point.” |
| B — participant-reported learning/use | valid participant pathway denominators | “Among responding participants, [n/%] reported…” |
| C — descriptive paired change | same measure/assay repeated at defined times, linked respondents, pre-specified analysis | “Among linked respondents, a descriptive difference was observed…” |
| D — comparative effectiveness | prospectively specified comparator, allocation/analysis, fidelity and missing-data plan | “In this defined comparison, [version] showed a difference on [outcome] relative to [comparator]…” |

Standard organisation reports stop at A–B. Level C is an enhanced evaluation option. Level D is the route for a credible intervention-effect claim. Never call an A/B finding “proof that MFC caused change.”

## Standard participant form journey

The organisation contracts a **standard private evaluation process**. MFC asks every attendee to complete it; no manager, facilitator or host learns who did, did not, skipped or exited. A person can leave an item blank or exit without consequence. This is necessary for truthful privacy representation and valid data; it is not a marketing choice about whether evaluation matters.

### Standard information screen and facilitator script

> This short MFC evaluation is a standard part of today’s service. We ask everyone to complete it so we can improve the service and give the organisation a combined report. Please do not enter your name, workplace or anyone else’s name. Your manager and facilitator will not see individual answers or know whether you complete it. You can skip a question or exit at any time; this will not affect your participation in the session or your employment. This form is not monitored for urgent support.

The facilitator reads this verbatim, provides protected completion time and then creates physical/privacy space. A manager/host does not collect devices/cards, stand over participants, request screenshots, ask who completed, or receive response status.

### Linkage and code rules

- Each participant privately takes a shuffled, unassigned random-code card. The code register contains codes and technical status only—never name, attendance, seat, device, time or contact key.
- Each wave validates against the issued-code register without disclosing valid codes. One accepted response per code per wave; later duplicates are `duplicate_pending`, retained in audit and resolved using the pre-recorded earliest-complete rule.
- A lost code cannot be recovered in the no-contact route. A later response without that code is not joined by inference.
- The selected platform must be checked for email/login/IP/device/URL-token/analytics metadata before MFC uses the word “anonymous.” Until then: “MFC does not ask for your name or contact details; the organisation receives combined results only.”
- The generic return link contains no participant-specific code, prefill, token or identifying URL parameter. Only whole-cohort neutral reminders are permitted. MFC, host and manager do not send, record or receive individual reminders, opens, completion or non-response status.

### Form A — before session (2 minutes)

No consent checkbox or opt-in record. An exit submits nothing.

| ID | Exact field | Response / rule | Construct |
|---|---|---|---|
| A0 | Enter your random study code. | required valid issued code | linkage |
| A1 | In the past 14 days, how often have you noticed an everyday moment where you may have wanted to pause, create some space or perspective, or choose what to do next? | Never / Once / 2–3 times / 4 or more times / Not sure / Prefer not to say | pre-service context only |
| A2 | System-captured service, service version, form version and session date. | no participant entry | delivery linkage |

WHO-5 is **not in the v3 base route**. It may be added only as an intact, separately governed context annex after its purpose, permissions, scoring, missing-data handling, aggregate interpretation and response pathway are recorded.

### Form B — immediate after session (3 minutes)

| ID | Exact field | Response / rule | Construct |
|---|---|---|---|
| B0 | Enter your random study code. | required valid issued code; system captures version/date | linkage |
| B1 | Which best describes what a guided rehearsal was for in this session? | Trying the process with a fictional or low-risk example / Proving I can use it in real life / Sharing a personal problem with the group / Not sure / Prefer not to say | process discrimination |
| B2 | Which best describes a Mental Rep? | Intentionally using the process in a real moment / Completing a guided rehearsal during the session / Getting every feeling under control / Not sure / Prefer not to say | process discrimination |
| B3 | Were you offered a guided rehearsal today? | Yes / No / Not sure / Prefer not to say | offer/access |
| B4 | Which best describes your participation? | show only if B3=Yes: Joined in / Worked privately / Observed / Passed / Prefer not to say; otherwise store not applicable | participation route |
| B5 | How was the amount of choice about participation? | Too little / About right / Too much / Not sure / Prefer not to say | agency/burden |
| B6 | Was any part of the wording, example or activity difficult to take part in? | No / Wording unclear / Example did not fit / Felt uncomfortable / Activity hard to access / Another reason / Prefer not to say | access/friction |

These are MFC-authored product diagnostics. Do not sum them into a capability score or call them an unaided-retrieval or validated measure.

### Form C — day 21–28 return (3 minutes)

The organisation distributes the same generic link to the whole eligible cohort. MFC records `return link distributed`, not individual receipt/opening. Submission date determines actual days since session.

| ID | Exact field | Response / rule | Construct |
|---|---|---|---|
| C0 | Enter your random study code. | required valid issued code | linkage |
| C1 | Since the session on [date], has a moment come up where you might have wanted to pause, create some space or perspective, or choose what to do next? | Yes / No / Not sure / Prefer not to say | opportunity |
| C2 | Thinking of one such moment, did you notice the moment and intentionally choose what to do next? | show only C1=Yes: Yes / No / Not sure / Prefer not to say | participant-reported intentional next-step event |
| C3 | Which, if any, made this difficult? Select all that apply. | show only C1=Yes: Did not notice / No workable Shift / Next move unclear / Safety or relationship concern / Capacity or time / Needed support or change beyond me / Another reason / None / Prefer not to say. `None` and `Prefer not` exclusive. | breakpoint/context |
| C4 | Did a situation arise where using this process did not feel appropriate or safe? | show only C1=Yes: Yes / No / Not sure / Prefer not to say | appropriateness/safety context |
| C5 | Over this period, how many times did you notice a relevant moment and intentionally choose what to do next? | show only C1=Yes: 0 / 1 / 2–3 / 4 or more / Not sure / Prefer not to say | reported repetition |
| C6 | What would make this learning more useful in everyday moments? Select any that apply. | show only C1=Yes: Clearer language / Different example / More guided practice / More time / More private participation / More support or environmental change / Nothing in particular / Not sure / Prefer not to say. Last three exclusive. | product improvement |

If C2=Yes/C5=0, or C2=No/C5>0, retain both, flag `C2_C5_inconsistent`, retain C2 in its denominator and exclude that record from C5-pattern numerator. Do not silently recode.

## Delivery and fidelity record (one per delivery)

The delivery lead records these fields separately from participant data:

| Field | Allowed value |
|---|---|
| Organisation/cohort ID | MFC internal organisation code, not participant dataset |
| Service/version/form version/facilitator/date | exact controlled IDs |
| Contracted eligible count; actual attendee count; forms offered count | counts only—no attendance list supplied to MFC for matching |
| Planned/actual duration and material deviations | structured delivery record |
| Protected form time offered | before / immediate post / return link distribution |
| Radar component | not purchased / offered / delivered; version and duration |
| Manager component | not purchased / offered / delivered; version and duration |
| Access adjustments made | structured category only; no disability/person detail |

## Radar and manager implementation records

### Radar record (one per organisation component)

Record: component version; offered/delivered; eligible aggregate count; aggregate participation/reach where genuinely known; delivery date/duration; access route supplied; whether a visibility support was offered; implementation barriers selected from `time/capacity`, `technology/access`, `context/safety`, `unclear ownership`, `not attempted`, `other operational barrier`; and actions completed/next action. A completed Radar is not a Mental Rep or behaviour-change outcome.

### Manager/context record (one per manager component)

Record: session version; invited/attended aggregate count; objective topics delivered; private/collective participation routes offered; structured manager self-report immediately after: `I can distinguish an individual learning practice from an organisational condition` (agree / not sure / disagree / prefer not); `One support condition we will examine is…` (select: workload/time, role clarity, safety/relationship, access to support, other; no employee examples); and a 21–28-day implementation check: `Was an agreed support action put in place?` (yes/no/in progress/not sure) plus action category. This is implementation-lead perspective only, not an employee/culture measure.

No individual participant code, response, attendance status or free text joins any implementation record.

## Organisation agreement — minimum clauses

1. The organisation approves MFC’s standard private evaluation process and provides protected completion time.
2. It does not require a particular person to submit, identify non-responders, provide an employee/attendance list for matching, seek answers/screenshots or use participation/results for employment or performance decisions.
3. It nominates one authorised recipient for the aggregate report and does not attempt re-identification or combine the report with personnel data.
4. MFC provides aggregate findings only, applies pre-defined small-cell suppression, and may report insufficient data rather than a result.
5. Radar/manager component information is a separately held implementation/context record, not a key for participant data.

## Reporting release and accessibility rules

- Do not issue an organisation-facing participant-result section where fewer than **10 respondents** contribute. Suppress every subgroup/cross-tab cell below **5**. Apply a stricter rule or withhold the section where date, role, service configuration or other context could still make a person reasonably identifiable. A delivery-only note may still be issued.
- If suppression, missingness or complementary-cell deduction means a section cannot be interpreted without meaningful re-identification risk, display: **“Insufficient data to report responsibly.”** Never replace it with an inferred residual or a report-wide effectiveness statement.
- Before every delivery, MFC records an equivalent private accessible completion route. Participant-controlled assistance may help with access but cannot view, enter, retain or report answers or codes. No person is asked to disclose health/disability information to use it.
- The form end screen and code card include the final non-monitored support wording and code-based record-location/deletion route. Do not promise deletion unless the selected platform and no-contact code process can perform it.

## Standard organisation report template (A–B only)

1. **What MFC delivered** — exact service/form versions, duration, facilitator, deviations, Radar/manager components delivered.
2. **Who is represented** — eligible, attended, offered, started/completed per wave, valid linked pairs, link distributed, return count; never disguise non-response as non-use.
3. **Immediate participant-reported learning/experience** — B1–B6, each denominator shown; guided rehearsal never reported as real-world use.
4. **Later participant-reported pathway** — C1 opportunity → C2 intentional next-step event among C1=Yes → barriers/context/repetition, each denominator shown.
5. **Component implementation/context** — Radar/manager delivery and implementation record displayed separately.
6. **MFC product response** — what MFC will keep, investigate, adapt or stop, labelled as a product decision.
7. **Limits** — anonymous/de-identified self-report as configured; respondent coverage; no individual assessment; no objective behaviour observation; no causal, wellbeing, performance or culture claim.

Example headline:

> “This report describes what MFC delivered and combined participant-reported learning and later-use signals among respondents. It does not assess individuals or establish that the service caused change.”

## Enhanced effectiveness-study lane

To test whether MFC is effective, rather than merely describe reported signals, create a separately versioned protocol with:

- one pre-specified primary outcome, either a cognitive-tested MFC target assay or an intact externally sourced measure with a clear product decision;
- a credible comparison, such as staggered/team-level allocation or a time-matched alternative;
- pre-specified eligible population, allocation/analysis unit, timing, fidelity, clustering, missing-data and sensitivity rules;
- a distinct Radar/manager component allocation or comparison if their incremental value is being tested;
- independent review and, where appropriate, a research partner.

No routine client dashboard may borrow Level-D language before this protocol is run.

## Required build checks before collection

1. Founder records scope: selected Essentials/Foundations, routine standard evaluation, report recipient and relevant component configuration.
2. Platform test confirms actual metadata, access, exports, deletion, analytics controls and accessibility route.
3. Named MFC data custodian and backup complete least-privilege test; organisation has no raw or response-status access.
4. Synthetic end-to-end run covers exit/skip, invalid/lost/duplicate code, every branch, C2/C5 inconsistency, low response/small cells, report suppression, export, deletion request, offboarding, manager-present and no-personal-device scenarios.
5. A mock organisation report is generated from the synthetic data and independently red-teamed against the claim ladder.
6. Qualified human review is obtained for final privacy/data handling, support/safeguarding position and any external measure conditions. This document makes no such approval claim.

The exact participant information, retention/deletion position and non-monitored support wording are controlled in `MFC-MEASUREMENT-PARTICIPANT-AND-DATA-NOTICE-v3.md`; it must be finalised against the selected platform before collection.
