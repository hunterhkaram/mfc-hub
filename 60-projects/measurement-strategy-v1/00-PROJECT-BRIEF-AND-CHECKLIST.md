---
title: "Measurement Strategy v1 — project brief and completion checklist"
mfc_topic: measurement
artifact_role: candidate
canonical_source: 30-decisions/D-0109-who5-moves-to-routine-measurement-core.md
created: 2026-08-31
revised: 2026-08-31
revision_note: >
  v2 after an independent fresh-context check returned NOT READY on v1. Eight findings
  applied: the v3-vs-D-0109 contradiction surfaced as the primary conflict, the item budget
  rebuilt by timepoint, R3's actual TYDQ position corrected, advisor count corrected 48->51,
  a manufactured AG-187/AG-193 conflict removed, the 10/5 vs 20/10 threshold conflict added,
  an overclaimed ceiling prediction softened, and four missing checks (M1-M4) added.
owner: Hunter Karam
maintained_by: ai
confidentiality: internal
claims_boundary: >
  K-08 governs. Nothing here claims MFC causes behaviour change, wellbeing improvement or
  habit formation. No instrument is described as validated unless it is. No advisor position
  is recorded as approved — all 51 are `pending-approval` in the register.
status: superseded
superseded_by: 60-projects/measurement-strategy-v1/2026-09-04-MEASUREMENT-v5.md
superseded_on: 2026-09-04
supersession_note: "Superseded 2026-09-04 by MEASUREMENT-v5. Retained as the record of how the measurement work was originally scoped."
---

# Measurement Strategy v1 — brief and checklist

## Why this is a project, not a decision

MFC does not have a measurement gap. It has **at least six live measurement artefacts**,
each authored or endorsed by someone with real authority, none reconciled against the
others — and one direct, unresolved contradiction between a founder decision record and the
build candidate that came after it.

| # | Design | Authority | Status |
|---|---|---|---|
| 1 | **v0.14 live forms** — three timepoints, lean MFC core, WHO-5 *removed* | `D-0100`, founder-approved | Live in Google Docs at revision **1226 / 20**. Registered as **STALE** — predates D-0105, D-0109, the pre-read and IMTTAQ |
| 2 | **R3 research recommendation** — 17 named changes: opportunity-conditional rep count, SGIC token linkage, then-test, critical-incident free text, TYDQ-15 as a labelled *secondary* | Commissioned research, committee pack | Roughly **2–3 of 17 applied** to v3 (#1, #2, and #8 at different thresholds). #3, #5, #6, #9, #10, #12, #13, #14 not present |
| 3 | **`D-0109` + `KN-0006`** — WHO-5 routine for **every** participant at baseline and return; intact IMTTAQ six items at day-21 | Founder decision (`D-0109`, 2026-08-25) + Eimear/Debra, 2026-08-24 | **CONTROLLING** per the topic register |
| 4 | **Measurement System v3** — day-21 Form C is **C1–C6: six items, no WHO-5, no IMTTAQ** | Build candidate, independently reviewed 2026-08-30 | *"WHO-5 is **not in the v3 base route**"* (`20-MEASUREMENT-SYSTEM-v3.md:82`). **Awaiting founder review — that review has not happened** |
| 5 | **2026-08-23 pre-read position** — TYDQ-15 anchored, WHO-5 removed entirely | Advisor pre-read | Superseded by 3, but still on the record |
| 6 | **`workshop-package.html`** meas1/meas3/meas90 tabs — built around IMTTAQ + WHO-5 | Vault artefact, 2026-08-25 | Registered `historical_not_current_v3` while still describing a different design from v3 |

Plus, from tonight: **Kirkpatrick four levels + a 10–15 question pulse** (Onno, `AG-206`,
`AG-207`, `AG-208`) — in none of the six.

### The conflict that has to be resolved first

**A founder decision record mandates an instrument the later build candidate silently
dropped.** `D-0109` puts WHO-5 in the routine core for every participant, at baseline and
at the return. `KN-0006` puts intact IMTTAQ at day-21. Measurement System v3, built
afterwards and independently reviewed, has neither — its day-21 form is six MFC-designed
items. The topic register carries both positions in adjacent paragraphs: v3 as *"the
current controlled build candidate"*, and `D-0109`/`KN-0006` as *"CONTROLLING RECORDS as at
2026-08-25."*

Under `CLAUDE.md` §4, a newer timestamp does not override higher authority — the decision
record wins until amended. **Either v3 adds both instruments, or `D-0109` is amended by a
new decision record.** It cannot stay as it is. This is surfaced, not reconciled, and it is
the project's first substantive item.

**Second reason it is a project:** **51** advisor positions bearing on measurement sit in
the Advisor Guidance Register (section E: `AG-168`–`AG-216`, 49 consecutive IDs, plus
`AG-319`/`AG-320`), and **every one is `pending-approval`** — 0 of 51 carry any other
status. Note the register's own live-conflict table flags four tensions (caveat placement,
ambassador programme, insurance, price floor) and **none is a measurement conflict**. So the
advisor guidance is unratified rather than self-contradicting. Ratifying it is a founder
action nothing currently forces.

**Third reason:** the person whose contribution the measurement layer *is* — Debra, per
`AG-198` — supplied a Measures Table on 2026-06-22 whose **contents have never been
extracted into the vault** (register gap 2). The design is being built without reading it.

---

## The binding constraint nobody has costed: item budget

Rebuilt by timepoint, because R3's additions are not all at day-21 and treating them as
one pool overstates the day-21 load.

### Day-21 return form

| Block | Items | Source |
|---|---|---|
| **v3 as actually built** (C1–C6) | **6** | `20-MEASUREMENT-SYSTEM-v3.md:104–110` — the only design with a countable item list |
| IMTTAQ (Transfer ×3 + Opportunities ×3) | +6 | `KN-0006:99` — must stay intact or it is not IMTTAQ |
| WHO-5 | +5 | `D-0109` (routine, every participant, repeated at return) |
| Opportunity-conditional rep count | +3 (partly *replaces* C5) | `R3` §5.3(a) |
| Critical-incident free text | +1 item, ~90 sec | `R3` §6.3 |
| TYDQ-15, if R3 #11 is honoured | +15 | `R3:353` |
| **Day-21 total, controlling design (v3 + D-0109 + KN-0006)** | **~17** | |
| **With R3's day-21 additions** | **~20–21** | |
| **With TYDQ-15 as well** | **~35–36** | |

### Baseline and immediate-post

Not budgeted anywhere in the current work, and they carry their own load: WHO-5 at baseline
(+5, `D-0109`), R3's then-test block at post only (+4–6, `R3:375`), and R3's situational
judgement items at pre and post (+2, `R3:485`). **No artefact currently assigns every
measure to a timepoint.** That assignment is a required output of this project.

### Why the number matters

Onno's position (`AG-207`) is a **recommendation**, not a hard ceiling: *"Prefer short
pulse surveys of 10–15 questions"* — participation rates are far higher. Set against
`AG-176` (Eimear, HARD) — post-workshop survey completion is *"dismally low (~15%)"* and
response mechanics must be engineered in — and `AG-183` (Eimear + Gina, tonight) — added
measures must *"test genuinely different things and not overlap or overload"* — burden is a
live design constraint, not a preference.

**The arithmetic that matters is not item count but expected N.** A cohort of 20 at a 15%
response rate returns 3 responses. `v3:151` already refuses to report a participant section
below 10 respondents. **On current assumptions the design suppresses its own output** — and
that is the finding this project exists to act on, independent of how the item count lands.

So the strategic decision is **what comes out, and how response rate is engineered up.**
Not what goes in.

---

## The best steer — provisional recommendation, not a decision

Stated so the project has something to argue against rather than starting blank.

**1. Adopt Kirkpatrick as the internal reporting spine, not as an additional instrument.**
It is a filing structure for measures MFC already has. Levels 1–2 are already what `D-0100`
measures; F9's own construct matrix already labels them that way. Zero item cost, and it
answers Onno.

**2. Resolve the WHO-5/IMTTAQ contradiction in favour of the decision record — then
re-decide it deliberately.** `D-0109` controls, so v3 is currently non-compliant. But
`D-0109` was made before v3's burden analysis existed. The right move is not to bolt 11
items onto v3; it is to put the amendment question to Hunter explicitly, with the burden
and expected-N numbers attached. Eimear's rationale for WHO-5 (`AG-171`, `AG-172`) is
specifically that a validated measure lets a stats package cross-compare against
enactment — which only pays off if N supports an analysis at all.

**3. On TYDQ-15 — correcting a v1 error in this brief.** R3 does *not* reject TYDQ
outright. `R3:333` rejects it *as MFC's primary outcome*; `R3:339` and `R3:353`
**recommend adopting TYDQ-15 as a single, clearly-labelled secondary context measure**,
pre-labelled as not expected to move in three weeks. `KN-0006` separately declines it on
burden grounds. Those are compatible only if burden is the deciding factor — so the
exclusion must be argued on burden and expected N, not by claiming research support that
does not exist. Licensing is also unconfirmed (`R3` §5.3 note).

**4. Replace, do not add, on the enactment measure.** R3's opportunity-conditional rep
count (3 items) should *displace* v3's C5 rather than sit beside it — it is the only
measure aligned to MFC's own "count the attempt, not the outcome" definition. R3's reasoning
that a Likert version would ceiling is a **reasoned projection from adjacent evidence, not a
verified prediction** (`R3:493` rates its own projections moderate); the ANU scale's p = .68
is evidence that the ceiling problem is real in a comparable instrument, not a forecast of
MFC's result.

**5. Keep the critical-incident free text.** One prompt, ~90 seconds. `AG-208` (Onno,
HARD) requires genuinely open questions; R3 calls it *"the single most persuasive material
MFC will have for a committee or a funder."* It is the only item producing checkable
behavioural detail. Its screening cost is real and must be budgeted (`R3` §4.2).

**6. Do the founder review that is already sitting there.** `27-MEASUREMENT-FOUNDER-REVIEW-v3.md`
asks four specific questions, is marked `ready-for-founder-review`, and takes 8 minutes.
Nothing downstream can be frozen until those four are answered — including decision 3,
"choose a build owner," which no other artefact assigns.

---

## Completion checklist

The project is complete when every line is `PASS` with named evidence. A line is not passed
by an argument that it does not apply.

### A. Reconstruction — is the current truth actually known?

| # | Check | Pass condition |
|---|---|---|
| A1 | All six live artefacts identified and their conflicts stated, not silently reconciled | Named conflict list; each says which source wins and under what authority |
| A2 | The v3 vs `D-0109`/`KN-0006` contradiction resolved by decision record | Either v3 amended, or `D-0109` amended. Not left open |
| A3 | Debra's Measures Table contents extracted into the vault | Document read and instruments registered, or its absence stated with the retrieval attempted and failed |
| A4 | All 51 measurement-bearing advisor positions mapped to accept / reject / not-yet | No position unaddressed; rejections carry a reason. Include `AG-167`, which sits in section D but bears on cadence |
| A5 | `UNCERTAIN`-attributed positions (e.g. `AG-193`, `AG-175`) never quoted to a named advisor | Attribution flag preserved wherever cited |
| A6 | Live Google Docs revision state verified, not assumed | Checked against the register's recorded 1226 / 20 |
| A7 | The integration review's four named open conditions carried into this project | Each appears against a check below |

### B. The strategic decision — is the right thing being measured?

| # | Check | Pass condition |
|---|---|---|
| B1 | Every retained item traced to a named decision it informs | An item informing no decision is cut |
| B2 | Item budget counted **per timepoint**, stated, and inside a defended ceiling | Baseline, post and day-21 each budgeted separately |
| B3 | Overlap between blocks tested item by item | `AG-183` satisfied with evidence, not assertion |
| B4 | Response-rate mechanics designed, not assumed | `AG-176`'s ~15% addressed with a named mechanism. Note `v3:70` permits only whole-cohort neutral reminders, which forecloses most rate-lifting tactics — that trade must be made explicitly |
| B5 | Expected N modelled against v3's own 10-respondent reporting floor | If the design suppresses its own output at realistic cohort sizes, that is stated before fielding |
| B6 | Each of the three intervention parts (`KN-0006`) separately measurable | Already satisfied by v3's three-record model (`v3:36–39`) — verify it survives any change |
| B7 | Kirkpatrick's role decided explicitly — spine, instrument, or vocabulary | Written decision, with Level 4's boundary paragraph drafted |
| B8 | A pre-registered "what would disconfirm this" line | Written before fielding, per `AG-188` and `D-0051` |
| B9 | **M1** — every measure assigned to a specific timepoint | No measure floats; `D-0100`'s three timepoints and `D-0105`'s case-study cadence both covered |
| B10 | **M4** — analysis plan written, with a named person competent to run it | Statistical approach, software, and a power or precision estimate. `AG-171`/`AG-172`/`AG-182` are unachievable without this |

### C. Claims and honesty

| # | Check | Pass condition |
|---|---|---|
| C1 | Every reportable sentence checked against `K-08` | No causal, competence, habit, wellbeing-improvement or prevention claim survives |
| C2 | MFC-designed questions labelled as such everywhere | Never described as validated (`KN-0006` boundary; `AG-193`) |
| C3 | IMTTAQ used intact or explicitly relabelled MFC-adapted | A rewritten subscale is not IMTTAQ |
| C4 | One reporting-threshold rule, not two | **Live conflict:** `v3:151` uses 10 respondents / suppress below 5; `R3` #8 and `AG-209` use N≥20 report / N≥10 breakdown. Pick one and write it into the organisation agreement |
| C5 | Null results pre-committed as publishable | `AG-188`; a predictable null must not read as failure |
| C6 | **M3** — instrument wording actually held before any burden or field claim | IMTTAQ's six items are **not in the vault** (register note). A reconstructed instrument is not the instrument (`R3:357`) |

### D. Privacy, ethics and safeguarding — the hard gates

| # | Check | Pass condition |
|---|---|---|
| D1 | **M2** — linkage mechanism *chosen*, not merely classified | Three incompatible options are live: `D-0100` pt 7 (system ID + separate key), `R3` #2/#3 (token card + Rep Code SGIC, no key exists), `v3:66` (unassigned code register). Choose one |
| D2 | R3 #5 and #6 implemented with the chosen mechanism | 3-pass matcher written before first pilot; matched-vs-unmatched baseline reported every time |
| D3 | Free-text screening rule written **before** first field use | `R3` §4.2 — non-negotiable; identifiability lives here |
| D4 | `D-0100`'s five open gates each resolved or explicitly still open | Privacy/legal, clinical/safeguarding, Eimear+Debra wording review, two comprehension rounds, frozen version |
| D5 | `D-0109`'s WHO-5 gates addressed | Clinical-response owner, licence, privacy, analysis plan, ethics — all five, for *every* participant now |
| D6 | Manager/employer visibility impossible by construction | Largely satisfied by v3 (`:56, 62, 70, 139`) — verify it survives any change |
| D7 | Research-vs-service-evaluation path decided before collection | HREC cannot be obtained retrospectively (`AG-168`, `KN-0006`) |

### E. Governance and closure

| # | Check | Pass condition |
|---|---|---|
| E1 | Founder review `27-MEASUREMENT-FOUNDER-REVIEW-v3.md` completed — all four questions | Hunter's actual answers recorded. **First action, not last** |
| E2 | **M5** — build owner named, date set, cost stated against runway | Founder review decision 3; no artefact currently assigns it |
| E3 | Eimear and Debra review the exact wording | Their review, not a proxy — `D-0100` gate 3 names them |
| E4 | Onno sent the reconciled Kirkpatrick position | He offered materials (`AG-206`); the loop closes either way |
| E5 | One exact version frozen for one defined cohort | Version label, date, cohort |
| E6 | Superseded designs marked superseded, not left live | v0.14 Google Docs and `workshop-package.html` cannot stay live and stale |
| E7 | Topic register and Hub updated; reconciliation receipt run | `record_topic_reconciliation.py` |
| E8 | Independent check by a fresh context against this checklist | Findings applied, not filed |

### F. Anti-checks — the ways this project fails

| # | Failure mode | Guard |
|---|---|---|
| F1 | Adding Kirkpatrick as a seventh design instead of reconciling six | B7 must produce a *reduction* |
| F2 | Advisor positions averaged into mush, or an `UNCERTAIN` attribution quoted to a named person | A4, A5 |
| F3 | Instrument frozen before Debra's table is read | A3 blocks E5 |
| F4 | Item count grows because every advisor gets one item | B2, B3 |
| F5 | The 8-minute founder review stays unread another month | E1 first, E2 sets the date |
| F6 | A perfect instrument that is never fielded | `AG-187`, Debra, HARD: *"I wouldn't put any hold on anything"* |
| F7 | The v3-vs-`D-0109` conflict quietly resolved by whichever file is edited next | A2 requires a decision record either way |
| F8 | A form that is fielded but never analysed | B10 |

---

## What this brief does not do

It makes no decision and approves nothing. All 51 advisor positions cited remain
`pending-approval`. `D-0100`, `D-0105` and `D-0109` remain controlling until amended by a
decision record. The "best steer" section is a provisional recommendation written so the
project has a position to attack.

**Provenance:** v1 of this brief was checked by an independent fresh context against its own
sections A–C and returned **NOT READY** with eight findings, all applied here. Three were
substantive: the v3-vs-`D-0109` contradiction was collapsed into a single table row and is
now the brief's lead finding; the item budget mixed timepoints and inflated the day-21
figure by 6–8 items; and the brief cited R3 as rejecting TYDQ-15 when R3 recommends it as a
labelled secondary. This v2 has **not** itself been independently checked.
