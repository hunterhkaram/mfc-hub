---
mfc_topic: operations-governance
artifact_role: review
canonical_source: 60-projects/measurement-strategy-v1/39-THE-FINAL-QUESTION-SET-2026-09-21.md
created: 2026-09-28
status: findings_applied
specialist_id: A-07
execution_mode: bounded_specialist_review
pack_version: '2026-08-13'
pack_state: baseline_equipped
task_packet: 90-meta/full-permanent-specialist-bench-v1/routing-records/packets/2026-09-28-head-of-digital-0928-flow-and-capture.yml
artifact_reviewed: 60-projects/measurement-strategy-v1/form-set-v2/index.html
---

# A-07 - measurement forms review, 2026-09-28

## Bounded question
Under Hunter's rules for this pass: create nothing new, bring approach changes as cases, find
unimplemented advisor positions, and make every question clear and fit for its purpose.

## Position
Eleven findings, four losing or corrupting data. The 'Somewhere else, please say where' text was rendered, typed into and silently discarded on every submission because it was not in the value map. The backend never wrote the consent flag or form version, so there was no record of which consent wording anyone saw. Text answers beginning with = became spreadsheet formulas. And the error message promised nothing is lost while nothing reads the saved draft back.

## Sources reviewed
`60-projects/measurement-strategy-v1/form-set-v2/index.html` and the six rendered forms beside it ·
`60-projects/measurement-strategy-v1/39-THE-FINAL-QUESTION-SET-2026-09-21.md` ·
`50-authority/advisor-guidance-register/REGISTER.md`

## Professional principles applied
Read what the participant sees, not what the document intends. A finding that changes approved
wording is a proposal, not an edit.

## Evidence strength and limitations
Every finding reproduced against the rendered forms or verified in the register. No participant has
used these forms, and none will before cohort one.

## Alternatives considered
Applying every finding directly - rejected under Hunter's rule that approach changes come as cases.

## Recommendation
All four data losses fixed and verified end to end; the time corrected; the coding and sheet-layout questions sent as proposals.

## Strongest objection
Form 4's stated three minutes is really six to eight on a phone. Don't-know and won't-say are both stored as -99.

## What would change this view
An advisor ruling on the open disagreements, or cohort one's data showing a different pattern.

## Adjacent specialist or human boundary
Advisor disagreements are the advisors' to settle. Changes to approved wording are Hunter's.

## Proposed learning
Candidate: every data loss found today was invisible in the downloaded JSON and only visible by
comparing what the page renders against what the page sends. Reading the output is not testing it.
