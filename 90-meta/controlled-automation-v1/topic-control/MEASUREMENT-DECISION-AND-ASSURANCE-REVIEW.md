---
mfc_topic: measurement
artifact_role: review
canonical_source: 90-meta/controlled-automation-v1/topic-control/canonical-topic-register.yml
status: founder-direction-implemented
review_date: 2026-08-12
approval_status: founder-approved-candidate-not-field-approved
---

# Measurement decision and assurance review

## Decision in one sentence

For MFC's first routine Foundations pilot, retain three participant timepoints but use a lean instrument focused on comprehension, real-moment retrieval and early self-reported application; remove WHO-5 from the core forms and reserve it for a later, separately governed research module.

Hunter approved this direction on 12 August 2026 and it is recorded in D-0100. The existing live Workshop Forms and Measurement Blueprint were revised in place as candidate v0.14. This is still not clinical, legal/privacy, advisor, participant-testing or research-ethics approval.

## What was inspected

- Live Google Sheet: [MFC Measurement Blueprint](https://docs.google.com/spreadsheets/d/1CC4o982pnJNu0xqt-BAHiKQGhL_bYIyATGOAfLGKhaQ/edit), current revision `18`; all seven tabs read.
- Live Google Doc: [MFC Workshop Forms](https://docs.google.com/document/d/1xZff9ZPoaUCOIFCyB0Y-tRsiqOKd2VwmE3sWUkov1TI/edit), current connector revision `AIroW35…`; all form tabs and open Drive comments read.
- Vault decisions and reconciliation: `D-0017`, `D-0056`, `B5e`, `B5-forms-build-ready`, and the two 12 August candidate results.
- Current external sources: WHO's 2024 WHO-5 publication and licence; the WHO-5 systematic review; CDC questionnaire-evaluation guidance; OAIC privacy, pseudonymity and data-minimisation guidance; and NHMRC's 2025 National Statement.

## Why this is the strongest design

The first pilot's decision is not “did a 90-minute workshop improve psychological wellbeing?” It is whether the session lands, whether people can retrieve the core process in a real moment, whether they attempt a Mental Rep, and what supports or blocks use. The current Blueprint itself places these questions in stages 1 and 2 and says external outcomes belong later, once earlier stages are stable.

WHO-5 is a short, credible wellbeing instrument with a two-week recall period. That supports using it when wellbeing is a pre-specified outcome. It does not make wellbeing the right first-pilot outcome. In a small, uncontrolled, self-reported implementation pilot, baseline-to-follow-up movement would be highly confounded and easy to overinterpret. Baseline-only collection has no strong decision use. Collecting it also introduces sensitive wellbeing data, response-pathway questions and a current WHO licence whose non-commercial condition needs a qualified determination for MFC's paid corporate delivery model.

Therefore:

1. **Keep three timepoints:** baseline, immediate post-session, and day-21 follow-up closing day 28.
2. **Make the follow-up application cascade the primary evidence:** opportunity occurred → moment noticed → Mental Rep attempted → repetition/helpfulness/barriers.
3. **Use one concise matched access item as secondary evidence**, rather than ten responses across a five-situation matrix in both baseline and follow-up.
4. **Keep unaided Stop–Shift–Do recall and plan specificity as learning/retention evidence.**
5. **Remove WHO-5 from the routine first-pilot core.** Preserve it as an optional future research module after a named research question, exact licence position, clinical response pathway, privacy assessment, analysis plan and appropriate ethics determination.
6. **Move mission, discovery and optional demographic questions out of the core forms.** Add them only when each has a named decision use and small-cell privacy risk is controlled.

## Proposed lean core

### Form 1 — baseline, approximately 3–4 minutes

- Voluntary participation, purpose, access, reporting, retention and support explanation.
- Random evaluation ID; no email inside the response dataset.
- Prior practical education source, as a multi-select rather than one collapsed category.
- One matched past-14-day access item with “no relevant moment,” “did not know what might help,” and “not sure” kept separate from the ordinal responses.
- No WHO-5 and no default demographic module.

### Form 2 — immediate, approximately 4 minutes

- Mental-fitness recognition item.
- Unaided Stop–Shift–Do recall.
- One recognisable Radar moment and one intended Mental Rep.
- Feasibility/intention item.
- Individual participation-comfort and audience-fit items; these do not replace safeguarding.
- One optional improvement item.

### Form 3 — day 21, approximately 5–6 minutes

- Unaided Stop–Shift–Do recall.
- The exact matched access item.
- Opportunity, noticing, attempt, repetition and conditional helpfulness sequence.
- Radar use.
- Barriers and supports without arbitrary “top two” limits unless the question explicitly asks for the two most important.
- Optional real-life example with clear de-identification warning.

## Data-linkage recommendation

The current live Doc collects email and converts it to an ID; that is pseudonymous, not anonymous. The Blueprint simultaneously says anonymous unlinked data is the earliest-pilot default. Participant-generated codes based on personal facts are not the preferred fix: they can be forgotten, mistyped, collide, and embed personal information.

Preferred approach: generate a random evaluation ID; keep the email-to-ID contact key in a separate restricted store used only for sending and matching; give employers aggregate findings only; set an approved deletion date for the key. If MFC cannot implement and govern that separation safely before the first cohort, use unlinked anonymous responses and explicitly give up within-person change analysis for that cohort.

## Item-level defects requiring correction

### Critical

- The forms are not approved for fielding but use “required” language for WHO-5 and appear operationally complete.
- “Anonymous” and email-linked longitudinal analysis conflict. Linked records remain potentially identifiable.
- Consent does not yet state the complete purpose, voluntariness, access, retention, withdrawal limits, reporting, privacy contact and support pathway.
- WHO-5 licence and clinical-response implications have not been settled for paid corporate delivery.

### Major

- The Doc heading says v0.10 while resolved comments say changes were actioned in v0.12/v0.13.
- Eimear's unresolved comments include data linkage, item purpose, wording, response limits, qualitative handling, participant expectations and approval ownership.
- The five-situation knowledge/access matrix is burdensome and produces ten matched responses without a clear first-pilot decision for each.
- The proactive-style and “actions towards what matters” items are broad, normative and unlikely to yield interpretable change over three weeks.
- The positive-difference contribution question invites attribution in an uncontrolled design.
- Free-text handling says “paraphrase or suppress”; advisor feedback correctly notes that redaction and thematic reporting preserve meaning better than untracked paraphrase.

### Mechanical but field-blocking

- Malformed text remains: `A few times a monthOccasionally`, `a an appropriate`, `IfNow`, `useful answers`, `Other, please list (free text?)`, and several corrupted Host Debrief headings.
- “Cognitive testing” was misunderstood as IQ testing by an advisor. Use “question-comprehension and form-usability interviews” in participant/advisor-facing material, while recording cognitive interviewing as the survey-method term.

## Evidence basis and limits

- [WHO's 2024 WHO-5 publication](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01) confirms five items, a past-two-week timeframe, six response options and a CC BY-NC-SA 3.0 IGO licence.
- [Topp et al. systematic review](https://pubmed.ncbi.nlm.nih.gov/25831962/) supports WHO-5's general validity and responsiveness; it does not establish that a small uncontrolled MFC workshop pilot can attribute change to the workshop.
- [CDC CCQDER](https://www.cdc.gov/nchs/CCQDER/index.html) supports cognitive interviewing to examine comprehension, recall, judgement and response error. This is survey testing, not an IQ assessment.
- [OAIC de-identification guidance](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/handling-personal-information/de-identification-and-the-privacy-act) says de-identification cannot eliminate all re-identification risk.
- [OAIC APP 2 guidance](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-2-app-2-anonymity-and-pseudonymity) distinguishes anonymity from pseudonymity and cautions against linking identity unless necessary or consented.
- [NHMRC's 2025 National Statement](https://www.nhmrc.gov.au/research-policy/ethics/national-statement-ethical-conduct-human-research) is current from 23 June 2026. Whether MFC's activity is internal evaluation, research, or later publication requires a qualified institutional ethics determination; the AI system cannot decide that status conclusively.

## Approval sequence

1. Hunter decides the proposed pilot purpose, lean core and WHO-5 position.
2. The exact wording is revised once in the live Workshop Forms and the architecture once in the Blueprint; a single new pilot version is assigned.
3. A privacy/legal reviewer approves consent, linkage, access, retention, deletion and partner-reporting rules.
4. A clinical/safeguarding reviewer approves the support and response pathway.
5. Eimear and Debra review the exact core wording, burden and interpretations; all comments are resolved with rationale.
6. Conduct two small rounds of question-comprehension and form-usability interviews with varied intended participants, revising between rounds.
7. Freeze one version for the first cohort, record deviations, then make a continue/adapt/stop decision from the pilot evidence.

## Founder decision and implementation

Approved and implemented: **three timepoints; lean comprehension-and-application core; WHO-5 removed from the routine first pilot and retained only as a separately governed future research module.**

- Canonical vault decision: 30-decisions/D-0100-first-pilot-measurement-core.md.
- Live Workshop Forms: candidate v0.14, Drive revision 1226.
- Live Measurement Blueprint: candidate v0.14, Drive revision 20.
- Founder gate: closed.
- Fielding gate: open pending privacy/legal, clinical/safeguarding, Eimear/Debra exact-wording review, two participant-testing rounds and one frozen cohort version.
