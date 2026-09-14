---
id: D-0119
title: "D-0119 — No-counts applies to the room only; WHO-5 is governed by disclaimer, not clinical apparatus"
type: decision-record
mfc_topic: measurement
status: decided
decided_by: Hunter Karam
decided_date: 2026-09-01
advisor_guidance: AG-004, AG-006, AG-007, AG-012, AG-171, AG-172, AG-193, AG-209
independent_check: "fresh-context agent, 2026-09-01, verdict SOUND WITH CHANGES; nine findings applied in this record. Primary source transcript re-read as part of that check, which strengthened rather than weakened the advisor basis."
committee_notification: "not yet performed — Eimear Quigley offered to help draft the disclaimer wording (M11, 35:46); that is the named route to the qualified-human wording review this record retains."
amends:
  - 30-decisions/D-0100-first-pilot-measurement-core.md
  - 30-decisions/D-0109-who5-moves-to-routine-measurement-core.md
clarifies:
  - 30-decisions/D-0114-return-session-is-a-checkin-branching-design-retired.md
  - 30-decisions/D-0115-group-cap-twenty-price-review-clause-and-organisation-checkin.md
precedent:
  - 30-decisions/D-0118-close-d0016-as-claude-enforced-delivery-gate.md
confidentiality: internal
legal_status: >
  No legal, privacy, licensing or research-ethics conclusion is drawn. This record removes an
  internally-generated clinical gate on the advice of MFC's own clinical committee member and
  replaces it with the control she specified. It does not clear the licence, privacy, analysis-plan
  or ethics gates, which remain open.
---

# D-0119 — No-counts scope, and WHO-5 by disclaimer

## Advisor guidance consulted

| Entry | Advisor | Position | Effect on this record |
|---|---|---|---|
| `AG-004` (HARD) | Eimear Quigley, 2026-08-31 | Separate MFC from clinical risk **by disclaimer, not by clinical apparatus** — GP, Lifeline, 000 | **This record follows it.** Basis for decision 2. The register summary reads as workshop-scoped; the primary transcript shows it is not — see "Primary source" below |
| `AG-006` (REC) | Eimear Quigley, 2026-08-31 | If a participant becomes distressed, have a colleague step them out of the room; a solo facilitator is not expected to plan beyond that | **Followed, and preserved.** This is the in-room response that remains in place — see decision 2 |
| `AG-007` (REC) | Eimear Quigley, 2026-08-31 | WHO-5 scoring needs a disclaimer: certain scores indicate a need for further depression screening | **Addressed in draft, not yet followed.** A candidate disclaimer exists in `MEASUREMENT-FORMS-v4.html` §7, deliberately softened from Eimear's own wording ("sometimes a sign it is worth having a proper conversation" vs. her "indicates a need for further depression screening") and explicitly marked as pending her review. A head-of-compliance check flagged that this record originally overstated that as "Followed" — corrected here, per `L-045`: a drafted response and an accepted one are different claims. |
| `AG-012` (HARD) | Onno van-Es, 2026-08-16 | An explicit negative-scope disclaimer is needed, written without pretending to be legal advice | **Consistent** — the disclaimers below are scope statements, not legal advice |
| `AG-171`, `AG-172` (REC) | Eimear Quigley, 2026-08-24 | Run WHO-5 alongside enactment; a validated instrument is what lets a stats package cross-compare | **Preserved** — this record keeps WHO-5 in the core rather than removing it |
| `AG-193` (HARD, `UNCERTAIN` attribution — Debra Fidler or Eimear Quigley) | 2026-08-24 | MFC's bespoke questions have unknown reliability and construct validity; they cannot stand alone | **Preserved** — unblocking WHO-5 serves this position |
| `AG-209` (HARD) | Onno van-Es, 2026-08-16 | Measurement is the value proposition and the biggest exposure; state what can honestly be concluded | **Preserved** — no claim boundary is loosened here |

### Primary source — why AG-004 is not merely workshop-scoped

The register summary of `AG-004` could be read as being about the workshop's clinical framing
rather than about WHO-5. The transcript shows one continuous WHO-5 thread
(`10-sources/fathom-transcripts/2026-08-31-committee-commercial-strategy-review.md`, 32:54–33:31):

- **32:54, Eimear:** *"I forgot to mention it the other day **on the Who 5**, that certain scores are indicative of… potential further screen for depression need."*
- **33:04, Hunter:** *"What we do in research is we just have a disclaimer."*
- **33:09 / 33:16, Eimear:** *"So if you're feeling like you need to talk to somebody, ring Lifeline… Or if it's an emergency, ring 000. **So you kind of separate yourself from the clinical risk because you're not providing a clinical service.**"*

AG-004's clinical-risk sentence is Eimear's own answer to her own WHO-5 point. Earlier in the
same exchange (31:31) she names the miscalibration directly: *"I think it's gone a little bit
skew-wiffed there, because you're not a psychologist, you're not working with people who have
mental health conditions, you're not doing risk assessments… it seems to be picking up on
things that I would never even consider to be an issue."*

**No advisor position is contradicted by this record.** The gate being closed was
internally generated by MFC's own decision records, not requested by any advisor. All
entries above remain `pending-approval` in the register; this record is the founder decision
acting on them.

## Decision 1 — `D-0115`'s no-counts rule applies to the room, not to the written report

**Founder direction, 2026-09-01:** *"no counts is for the room only, reports keep
denominators."*

`D-0114` established that data shown back to participants in the return session carries no
counts at any group size, because in a small room the arithmetic identifies people whatever
words surround it. `D-0115` §4 retired the headcount reporting floor and said what remains
is that no-counts rule.

**That rule governs in-room display.** The written organisation report retains denominators
and continues to operate on Measurement System v3's claim ladder — *"Among responding
participants, [n/%] reported…"* — with small-cell suppression as already specified.

**The written report is not left unprotected by this.** Retiring the ≥20 headcount floor did
not remove the report's own thresholds: `20-MEASUREMENT-SYSTEM-v3.md:151` already forbids
issuing a participant-result section below **10 respondents** and suppresses every
subgroup cell below **5**, mirrored in the report template. Those stand.

This resolves a conflict that would otherwise have required rebuilding v3's claim ladder
from the ground up. No further interpretation of `D-0114`/`D-0115` on this point is needed.

## Decision 2 — WHO-5's clinical-response-pathway gate is closed and replaced

**`D-0100` point 5 and `D-0109` both require a "clinical-response pathway" before WHO-5 may
be fielded. That gate is closed.** It is replaced by the control MFC's own clinical
committee member specified.

### Why

**The gate was internally generated, not externally required.** No regulator, advisor, or
licence condition **known to MFC** asked for it — stated that way deliberately, because the
WHO-5 licence position is itself still unconfirmed (an open gate, below). `D-0100` reasoned that WHO-5 is
"depression-screening-adjacent" and imposed a response pathway on that basis. `D-0109`
widened it to every participant, describing it as *"a materially larger exposure… most
acutely the clinical-response pathway."*

**MFC's clinical committee member specified a different control, on 31 August 2026.**
`AG-004` (HARD): separate MFC from clinical risk **by disclaimer, not by clinical
apparatus**. Her position on WHO-5 specifically, `AG-007`: it needs a **scoring
disclaimer** — that certain scores indicate a need for further depression screening — not an
individual response pathway.

**The gate was also impossible as written — precisely.** Form C is **no-contact and unlinked
to identity by design**; a lost code cannot be recovered; participants are told the form is
not monitored for urgent support. (The word *anonymous* is deliberately avoided: the
participant notice itself refuses to promise it before the platform check, and that check is
still open.) **A score-triggered individual response pathway cannot exist in that
architecture.** A gate that cannot be satisfied is not a safeguard — it is a permanent block
dressed as one.

**What is not affected: in-room distress response.** Baseline WHO-5 is completed with a
facilitator present. `AG-006` specifies exactly what happens if someone becomes distressed —
a colleague steps them out of the room, and a solo facilitator is not expected to plan beyond
that. That response is unchanged by this record and sits with delivery safeguarding under
`D-0118`.

**`K-08` rule 10 is satisfied, not bypassed.** Rule 10 requires referral, safeguarding and
crisis pathways where distress or clinical need falls outside education's scope. Foundations
records outrank decision records, so this matters: unconditional GP/Lifeline/000 signposting
**is** that referral pathway. The rule asks for a route out, not for MFC to operate one.

**`D-0118` is precedent for the diagnosis, not for the disposal.** `D-0118` closed `D-0016`
as a Claude-enforced delivery gate while explicitly refusing to resolve the underlying
matters. This record goes further: it closes a gate **and asserts a replacement control**.
What the two share is the finding — the same advisor, in the same meeting, identifying the
same miscalibration of clinical apparatus to a non-clinical educational service. That
diagnosis recurring is the reason to act; it is not authority to reuse D-0118's mechanism.

### What replaces it

1. **A standing non-clinical disclaimer**, per `AG-004`, wherever WHO-5 is asked: this is
   not a clinical service; if you have clinical needs, see your GP; Lifeline 13 11 14;
   emergency 000.
2. **A WHO-5 scoring disclaimer**, per `AG-007`: stating plainly that certain scores may
   indicate a need for further depression screening, and directing the participant to their
   GP.
3. **Unconditional signposting.** Both are served to **everyone**, not triggered by any
   score — the only form of support information compatible with anonymous collection, and
   stronger than triggered signposting because it also reaches people who skip the items.

### What this does not do

- It does not make WHO-5 field-ready. `D-0100`'s remaining gates — named wellbeing question,
  confirmed licence position, analysis plan, privacy review, ethics determination — are
  untouched and open.
- It does not authorise any wellbeing, improvement, causal or clinical claim from WHO-5
  data. `K-08` continues to govern.
- It does not remove qualified human review of final participant-facing wording. It changes
  what that review reviews: disclaimer wording, not a response pathway. Eimear offered to
  help draft it (M11, 35:46) — that is the cheapest route to closing it.

### Gates this record closes, named rather than left to implication

- **`D-0100` open-gate bullet 2** — *"clinical/safeguarding approval of support wording **and
  response pathway**"* — is **narrowed to support wording only.** The response-pathway half
  is closed.
- **`20-MEASUREMENT-SYSTEM-v3.md:82`** carries a third, independent instance of the same
  requirement (WHO-5 admissible only after its *"response pathway"* is recorded). **Also
  closed.** That same line still says WHO-5 is "not in the v3 base route," which contradicts
  `D-0109` — pre-existing, not caused here, and to be fixed in the same edit.
- It does not touch safeguarding in delivery, which `D-0118` already places with MFC's real
  committee and advisors.

## Founder reasoning, recorded

Hunter, 2026-09-01: *"I don't understand why WHO-5 has a clinical response requirement. Even
Eimear disagreed with that… your AI is very, very overly cautious. Nothing that you're
presenting or doing is clinical. This isn't clinical. And you can just have a disclaimer…
I should be able to come in and talk about a whiteboard marker, and I would never have to
say this is clinical."*

## Propagation required

| Destination | Change | Status |
|---|---|---|
| `60-projects/measurement-strategy-v1/01-MEASUREMENT-SYSTEM-v3.1-ADVISOR-ASKS-INCORPORATED.md` | §6 conflict resolved; blocker 3 closed | **done** |
| `60-projects/workshop-evidence-informed-adult/15-current-service-definition-v1/20-MEASUREMENT-SYSTEM-v3.md` line 82 | Close the response-pathway condition; also fix the stale "not in the v3 base route" clause against `D-0109` | pending |
| `60-projects/workshop-evidence-informed-adult/15-current-service-definition-v1/25-MEASUREMENT-PARTICIPANT-AND-DATA-NOTICE-v3.md` | Draft the two disclaimers | pending |
| `60-projects/measurement-strategy-v1/00-PROJECT-BRIEF-AND-CHECKLIST.md` check D5 | "Clinical-response owner" no longer an open gate | pending |
| `30-decisions/D-0100-...md` gate bullet 2 | Narrow to support wording only | pending |
| `20-knowledge/KN-0006-...md` | WHO-5 gate list | pending |
| Canonical topic register, `measurement` topic | State and open gates | pending |
