---
mfc_topic: measurement
artifact_role: review
canonical_source: 60-projects/measurement-strategy-v1/39-THE-FINAL-QUESTION-SET-2026-09-21.md
created: 2026-09-22
status: findings_applied
task_id: "de497b776405d278-2026-09-22T11:20:31.476642+10:00"
specialist_id: A-07
execution_mode: bounded_specialist_review
pack_version: '2026-08-13'
pack_state: baseline_equipped
task_packet: 90-meta/full-permanent-specialist-bench-v1/routing-records/packets/2026-09-22-head-of-digital-forms-hosting.yml
artifact_reviewed: 30-decisions/D-0133-measurement-forms-are-delivered-online.md
---

# A-07 — where the forms are hosted, and whether residency was ever a requirement

## Bounded question
Is Australian data residency an actual requirement or an assumption; what is the cheapest
option that works and what does it cost; what receives the POST now the forms are hand-built
static HTML; and what would make Hunter regret the choice in six months?

## Position
**Australian data residency is an internally-generated gate with no external basis, and the
hosting cost is AU$0 per year, not the AU$220 previously recommended.**

Three independent reasons the Privacy Act does not reach this data, any one sufficient:
the **small business exemption (s 6D) is still in force** — the compilation current to
4 June 2026 retains it, the 2024 Amendment Act deferred removal to a second tranche, and the
31 August 2026 Exposure Draft does not remove it either; **APP 8 only bites on personal
information** (OAIC APP Guidelines Ch.8 ¶8.4, and Ch.B ¶B.62: *"De-identified information is
not 'personal information'"*); and **no Australian data-localisation law** applies to a
charity's survey data.

`D-0133` uses residency to exclude Wix Forms and Google Forms. **Two exclusions, two different
reasons, and only one is real.** Wix Forms carries undisableable telemetry including visitor
IP — a genuine defect. Google's US storage is not.

## Sources reviewed
`30-decisions/D-0133-measurement-forms-are-delivered-online.md` ·
`30-decisions/D-0135-participant-forms-are-completed-in-session-digitally.md` ·
`50-authority/advisor-guidance-register/REGISTER.md` (`AG-016`, `AG-194`, `AG-195`, full sweep) ·
`60-projects/measurement-strategy-v1/39-THE-FINAL-QUESTION-SET-2026-09-21.md` ·
Privacy Act 1988 compilation to 4 June 2026 · OAIC APP Guidelines Ch.8 and Ch.B ·
Privacy Amendment (Personal Data Protection) Bill 2026 Exposure Draft ·
current Cloudflare Pages, Netlify, Formspree, Basin and Supabase pricing pages

## Professional principles applied
A privacy guarantee that depends on remembering to configure something is weaker than one the
platform cannot violate. The real requirement is a property of the payload, not of the
disk's jurisdiction. Bus factor is a design constraint at a charity with one technical person.

## Evidence strength and limitations
Statutory position and vendor prices checked against live pages on 2026-09-22, not asserted
from memory. **The "10 December 2026 small-business deadline" circulating on Australian IT-MSP
blogs is unsourced lead-generation content** and is contradicted by the OAIC, LK, Norton Rose
Fulbright and Pinsent Masons. **The Apps Script CORS path was not verified in this
environment** and is flagged below as the first deployment test.

## Recommendation
**Cloudflare Pages + Google Apps Script → Google Sheet. AU$0/year.**

LimeSurvey on a Sydney VPS was the right call only while the forms were being *authored inside
a survey tool*. Per-option stored values, the `-99/-98/-97` sentinels and the Form 5 work-gate
branching now live in MFC's own JavaScript. What remains is a POST target, and paying AU$220/yr
plus OS patching, PHP updates and TLS renewal to receive a JSON blob buys nothing.

**The privacy argument is the stronger one.** Apps Script's `doPost(e)` is never given the
client IP. It cannot record what it cannot see. Compare a Cloudflare Worker, where
`CF-Connecting-IP` sits on every request and staying clean depends on remembering not to write
it down. **`D-0133`'s raw-export inspection still has to happen** — but against a spreadsheet
whose columns MFC wrote by hand.

Cloudflare Pages accepts direct folder upload through the dashboard: no CLI, no git, no
wrangler. **Nothing here becomes unmaintainable if the one technical person is unavailable.**

## Alternatives considered
Formspree and Basin — free tiers of 50 submissions/month, and a cohort of 20 across six forms
is 120, so MFC pays immediately and the store is theirs. Netlify Forms — genuinely free and
unlimited since 14 April 2026, a fair second choice, but submissions live in Netlify's own UI
and the export path is worse than a Sheet. Supabase — **pauses free projects after one week of
inactivity**, fatal for a form that fires monthly. Cloudflare D1 — would work, but the data
then lives somewhere only a developer can read.

## Strongest objection
That a spreadsheet is not a database and this will not scale. **It does not need to.** At ten
cohorts it is still fine; at a hundred, move it. Building for the hundred now is the error.

## What would change this view
The small business exemption actually commencing its repeal. A funder or insurer imposing
residency as a condition. MFC beginning to collect anything that names a participant.

## Risks that survive the recommendation
- **Test Apps Script CORS on day one, before building all six links.** POST the JSON body as
  `text/plain` so the browser issues a simple request; Apps Script does not return CORS headers
  on its redirect. If it misbehaves, a Pages Function proxy is the fallback — and the forms do
  not change either way, which is the point of keeping hosting separable.
- **Silent data loss.** A fire-and-forget POST loses responses when a phone drops off wifi, and
  nobody finds out. On paper a lost form was at least visible.
- **Ownership.** The Cloudflare account, the Apps Script project and the Sheet must sit under
  an MFC-owned Google account with a second admin **at setup, not later.** Under Hunter's
  personal account, MFC loses its data the day he is unavailable.

## Adjacent specialist or human boundary
**A participant-chosen six-character code is pseudonymisation, not de-identification.** In a
single-employer cohort of fifteen, with role or team fields, re-identification can be trivial.
That is `head-of-compliance`'s call against the actual instrument — and it argues for
collecting less, not for hosting in Sydney. **There is still no recorded MFC privacy position
and no cyber cover**, and the 90-day withdrawal promise requires a named human and a monitored
inbox before the first cohort. `D-0133` should be **amended, not deleted**, and Rachel Willis
should see this finding first.

## Proposed learning
Candidate, not a lesson: `D-0133`'s residency clause is the third internally-generated gate
found in this session, after the reporting floor and the clinical-response pathway. The tell is
the same each time — a requirement stated without the external source that would have imposed
it. `L-088` already names the rule; what is missing is the habit of asking *who asked for this*
at the moment a constraint is written down, not years later when it blocks something.
