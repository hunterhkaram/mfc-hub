---
id: D-0120
title: "D-0120 — Kirkpatrick applies where a return session exists; Introduction is pre/post comprehension only, no WHO-5"
type: decision-record
mfc_topic: measurement
artifact_role: supersession
canonical_source: 30-decisions/D-0109-who5-moves-to-routine-measurement-core.md
status: decided
decided_by: Hunter Karam
decided_date: 2026-09-01
independent_check: >
  fresh-context agent, 2026-09-01. Checked five load-bearing claims against their actual sources.
  Three passed (the D-0109 point-3 quote, the propagation to MEASUREMENT-FORMS-v4.html, the core
  Level-4-is-organisational logic). Two real overstatements found and corrected the same pass:
  point 4 had offered D-0115's organisation check-in as an equivalent Level 4 source alongside
  A-11's actual named sources, but D-0115 contains no mention of Kirkpatrick or Level 4 at all —
  removed. And the K-08 attribution-error sentence implied K-08 itself states this reasoning about
  Kirkpatrick levels, when the specific chain is A-11's application of K-08's general prohibitions,
  not K-08's own text — reworded to attribute it correctly. Both findings verified directly (grep
  against D-0115 and A-11's evidence file) before being accepted, not taken on the checker's word.
advisor_guidance: AG-206, AG-183, AG-182
amends:
  - 30-decisions/D-0109-who5-moves-to-routine-measurement-core.md
supersedes_reading_in:
  - 60-projects/measurement-strategy-v1/MEASUREMENT-FORMS-v4.html
confidentiality: internal
legal_status: >
  No legal, privacy, licensing or research-ethics conclusion is drawn. This record scopes an
  architecture decision only.
---

# D-0120 — Kirkpatrick's scope, and Introduction's form settled

## Decision

**1. Kirkpatrick's four-level structure applies to any service with a return
session.** Currently Essentials and Foundations. If MFC later builds a return
touchpoint for another service or an organisation-level re-engagement, the same
structure extends to it by default — this is a rule about *return sessions*,
not a fixed list of two products.

**2. Introduction is pre/post only — comprehension, not the full ladder.**
Before and immediately after, nothing else. No return-session Form C, no
Level 3, no Level 4. Hunter, 2026-09-01: *"the introduction can just be pre
and post... so we get people's understanding of what they've learned."*

**3. This closes D-0109 point 3 as a live founder decision, not an inference.**
`D-0109` had provisionally placed WHO-5 at Introduction baseline, flagging
itself explicitly as *"Claude's reading… applied to a format that has no
day-21 return, not a separate founder decision."* That reading is now
superseded directly: **Introduction carries no WHO-5.** A pre/post
comprehension pair only.

**4. Level 4 stays where it already was: an organisation-level form, not a
participant form, and only where a return exists.** For Essentials and
Foundations, when the environmental/implementation work (manager sessions,
Radar) happens, MFC asks the *organisation* — via the delivery/fidelity
record and the Radar/manager implementation record, A-11's actual named
sources — whether anything changed at the organisational level.
**Correction, made on independent check 2026-09-01:** an earlier draft of
this point also offered `D-0115`'s recurring organisation check-in as an
equivalent Level 4 source. Checked directly: D-0115 contains no mention of
Kirkpatrick or Level 4 at all — it is a relationship/data-generation
touchpoint, explicitly "not costed, not priced," and conflating it with
A-11's specific architecture overstated what A-11 actually built. Removed;
D-0115's check-in may turn out to be a useful Level 4 input later, but that
is a future design question, not something this record can claim A-11
already settled.

This is what A-11 already built, and this record adopts it — with the
disclosed limit that A-11's own pack is `baseline_only_not_substantively_
evaluated`, a same-day specialist reasoning pass, not independently
field-tested assurance. "Confirms it was the right call" should be read as
"adopts A-11's reasoning," not as external validation of it. Level 4 was
never available to build from a participant's WHO-5 score, because doing so
would risk the causal-attribution error K-08's general prohibitions on
outcome claims are designed to prevent — a reasoning chain A-11 draws
explicitly (K-08 §Commercial Model prohibitions → A-11's application to
Kirkpatrick), not a sentence K-08 itself states about Kirkpatrick levels.

## Why

Hunter's reasoning, recorded: the Introduction is a single, non-personal
touchpoint with no disclosure and no return — there is nothing for Levels 3–4
to measure, and asking WHO-5 with no second timepoint produces a number with
no comparison to test it against. Pre/post comprehension answers the only
question Introduction can actually answer: did people understand what was
taught.

## A conflict this record surfaces rather than silently resolves

`D-0111` characterises Introduction as categorically different from
Essentials/Foundations partly *because* it has "no institutional
infrastructure behind it (no return session, **no data capture**, no
environment work)." Point 2 above puts a pre/post comprehension pair on
Introduction, which reverses that specific clause. Hunter's words in the
Decision section read as a deliberate call, not an oversight — but per
`CLAUDE.md` §4/§2a a conflict like this must be surfaced explicitly rather
than reconciled quietly. **Flagging it here: if Introduction keeps
"no data capture" as part of its identity, this point needs to be revisited;
if pre/post comprehension is the intended exception, that's a conscious
narrowing of D-0111's language, not an accidental one.**

## What this does not do

Does not change Essentials/Foundations' architecture, already specified in
`60-projects/measurement-strategy-v1/MEASUREMENT-FORMS-v4.html`. Does not
authorise fielding — `D-0100`'s and `D-0109`'s remaining gates are unchanged.
Does not add a form to Introduction that does not already exist; if
Introduction gains a pre/post pair, it is built and reviewed under the same
gates as every other MFC-designed item.

## Propagation

- `MEASUREMENT-FORMS-v4.html` — §1 Introduction row, and remove the flagged
  D-0109/D-0115 Introduction-WHO-5 conflict (resolved by this record)
- `D-0109` — point 3 marked superseded, pointing here
- `KN-0006` — WHO-5 cadence table
