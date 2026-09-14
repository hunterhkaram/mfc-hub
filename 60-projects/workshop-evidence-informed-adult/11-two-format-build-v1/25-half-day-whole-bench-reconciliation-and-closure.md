---
title: "Half-Day Foundations — whole-bench reconciliation and specialist-loop closure"
type: reconciliation
role: SYS-04
status: reconciled-with-disclosed-gaps
created: 2026-08-17
mfc_topic: workshop-delivery
artifact_role: review
canonical_source: 60-projects/workshop-evidence-informed-adult/11-two-format-build-v1/workshop-package.html
artifact_reviewed: workshop-package.html, slide-deck-half-day-foundations.html, 20-half-day-foundations-facilitator-guide-current.md, 21-half-day-foundations-participant-materials-current.md
frozen_hashes:
  arc: e430a6f960149aac8255b751b726223c716576514e9e55705de2515efebb8be0
  deck: 723c6ec782a02d4101d7daacea50cfa271113307a4f2d9bdbf9950ece5ec8f50
  guide: 4ac38422913252ac119374e3026cd6afb33b3264c82537f59f25e8579594ca9b
  materials: 6fdfa5d2f465234e5c73c0ac658ef386da8e364e480411781844c2703789be92
---

# Whole-bench reconciliation and closure

## Why this document exists

Two bounded evaluation-pilot panels ran on 2026-08-13:

1. `assurance-2026-08-13/` — 18 unique task packets/reviews, an independent A-24 coverage challenge,
   and a `SYS-04-integrated-recommendation-final.md` reconciliation. **Contract-complete** for its
   scope.
2. `assurance-2026-08-13-evaluated-panel/` — 24 further reviews plus a genuinely independent checker
   pass (`independent-check.md`) that returned **REVISE**, found six Major defects (source-lifecycle
   drift, an active D-0100/measurement conflict, an active participation-route conflict, overstated
   transfer/impact language, a missing D-0099 record, and a broken manifest evidence path), and set a
   six-step `correction-spec.yml` before the build could be called reconciled.

Neither panel was ever closed by a schema-v2 routing record, so under this vault's own contract
(`specialist-call-contract.md`) **neither counted as registered specialist assurance** — this is the
literal gap Hunter named: real bounded work existed, but it was never mechanically recorded, so it
could not be checked, trusted, or built on by a later session.

This document is that closure: it verifies what was actually applied to the live artifact, closes
what can be honestly closed, and names — rather than hides — what remains open.

## Verification against the live artifact (checked directly, this session, not inherited)

| `correction-spec.yml` item | Claimed disposition | Verified in `workshop-package.html` | Result |
|---|---|---|---|
| ARC-01 (WHO-5/measurement vs D-0100) | applied | Current-summary/historical-split present at both `meas1` and `meas3`; "not part of the routine first-pilot core" language present; no active claim that WHO-5 is routine. | **Confirmed applied.** |
| ARC-02 (visible/majority participation route) | applied | Zero occurrences of the show-of-hands/room-reading instruction; Route B explicitly "disabled by default... a visible show-of-hands or read-of-the-room check does not meet that bar and is not used." | **Confirmed applied.** |
| SOURCE-01 (D-0099 missing from corpus) | applied | Four live references to `D-0099`, correctly distinguishing the superseded formal gate from the six still-open delivery protections. | **Confirmed applied.** |
| ARC-03 (overstated transfer/impact language) | applied | "habit-stacking mechanism" and "you've done thousands" no longer present. One phrase remains at both format views: *"quietly surviving their moments instead of navigating them."* | **Reviewed, not a violation.** This is pre-teaching motivational framing ("many," not "everyone" or "all"), not a causal, transfer, habit or population claim — it does not match the pattern the correction targeted. Retained rather than edited to avoid touching reviewed copy without real cause. |
| MANIFEST-01 (broken evidence path, verifier depth) | partially applied | `package-manifest.yml`'s evidence path now resolves. `verify_half_day_workshop_package.py` still reports a generic PASS and does not yet encode the specific semantic fixtures (WHO-5-as-core, show-of-hands, stale D-0016 framing, habit/no-time/scaled-impact claims) the spec required it to fail on. | **Open** — the verifier is not yet a semantic regression guard; it currently proves structural agreement, not that these specific defects can't silently return. |
| PANEL-01 (25-role disposition + SYS-04 reconciliation) | required | This document. | **Closed by this document** (see table below). |
| PANEL-02 (14 non-contract-complete packets) | required | Not rerun. | **Open, disclosed** — see below. |
| TEST-01 (pair-route/density field questions) | field-only | N/A | **Correctly deferred to rehearsal/participant testing**, not a specialist-loop item. |

## Whole-bench disposition (all 25 registered roles)

| ID | Disposition | Basis |
|---|---|---|
| A-07 | reuse_current_evidence | `assurance-2026-08-13/reviews/A-07.md` + `assurance-2026-08-13-evaluated-panel/fresh-independent/` rerun; journey/navigation finding (rendered check) remains open, not a specialist-coverage gap. |
| A-08 | reuse_current_evidence | `assurance-2026-08-13/reviews/A-08.md` + evaluated-panel `A-08-nova.md`; narrative/language findings applied (ARC-03 table above). |
| A-09 | reuse_current_evidence | `assurance-2026-08-13/reviews/A-09.md` + evaluated-panel `A-09-milo.md`; behaviour/opportunity findings applied. |
| A-10 | reuse_current_evidence | `assurance-2026-08-13/reviews/A-10.md` + evaluated-panel `A-10-reed.md`; architecture retained as candidate, not optimum — correctly unresolved pending rehearsal/participant evidence. |
| A-11 | not_equipped_for_rerun_reuse_prior | `assurance-2026-08-13-evaluated-panel/task-packets/A-11-piper.md` is one of the 14 not contract-complete; its substantive finding (measurement conflict) was independently reproduced and applied (ARC-01), so the finding is trusted even though the packet itself is not. |
| A-12 | reuse_current_evidence | Restricted screen completed in both panels; human boundary correctly preserved. |
| A-13 | not_equipped_for_rerun_reuse_prior | Non-contract-complete packet; finding (private/anonymous route) independently reproduced and applied (ARC-02). |
| A-14 | defer_conditionally | Rendered/print/room evidence requires an actual render pass; no text-only review can close this. |
| A-15 | reuse_current_evidence | `assurance-2026-08-13/reviews/A-15.md` + evaluated-panel `A-15-cole.md`; facilitator-load/rehearsal gate correctly left open, not a text-review gate. |
| A-16 | reuse_current_evidence | `assurance-2026-08-13/reviews/A-16.md`; cue/return findings applied. |
| A-17 | not_equipped_for_rerun_reuse_prior | Non-contract-complete packet; refused (no live comparator claim needed) — a disciplined non-finding, not a gap. |
| A-18 | not_equipped_for_rerun_reuse_prior | Non-contract-complete packet; finding (scaled-cost/outcome promise) independently reproduced and applied. |
| A-19 | not_equipped_for_rerun_reuse_prior | Non-contract-complete packet; finding (movement/ripple relabelled as hypothesis) independently reproduced and applied. |
| A-20 | not_equipped_for_rerun_reuse_prior | Non-contract-complete packet; finding (proximal causal chain, no downstream leaps) independently reproduced and applied. |
| A-21 | defer_conditionally | No named host/employer/cohort exists yet for this candidate; correctly triggered only once one does. |
| A-22 | reuse_current_evidence | `assurance-2026-08-13/reviews/A-22.md`; comprehension gate correctly left open pending intended-participant testing. |
| A-23 | reuse_current_evidence | Ran before and after correction in both panels; current hash set in this document's frontmatter is the reconciled state. |
| A-24 | reuse_current_evidence | Coverage challenge (`assurance-2026-08-13/coverage-challenge.md`) plus non-contract-complete evaluated-panel packet; test-sequencing recommendation stands, staged testing remains a field task. |
| A-25 | not_equipped_for_rerun_reuse_prior | Non-contract-complete packet; finding (reconcile/freeze/test, do not expand) is the disposition this document follows. |
| A-26 | not_relevant | No public-sector/policy/government trigger present in this candidate. |
| H-01 | human_boundary | Preparation-only in both panels; qualified clinical/safeguarding review remains a named, unfilled human gate. |
| H-02 | human_boundary | Preparation-only in both panels; qualified privacy/legal review remains a named, unfilled human gate. |
| FL-01 | independent_specialist_review | `assurance-2026-08-13-evaluated-panel/reviews/FL-01.md` — genuinely independent, fresh-context, dated 2026-08-13. Its finding (build was not yet founder-decision-ready because the arc contradicted deck/guide/materials) is exactly what ARC-01/ARC-02/ARC-03/SOURCE-01 have since corrected. Its **remaining, unmet recommendation** — a beat-by-beat "why this exists / what evidence class / what objection / what test" interface, not just a corrected canonical page — is the one live open item this reconciliation carries forward, not a closed one. |
| SYS-03 | not_relevant | Need-test for a new persistent role fails in both panels; existing role coverage is adequate. |
| SYS-04 | reconciliation | This document. |

## Genuinely open, named rather than hidden

1. **Fourteen non-contract-complete packets** (A-11, A-13, A-17, A-18, A-19, A-20, A-21, A-23, A-24,
   A-25, A-26, H-01, H-02, SYS-03 from the evaluated panel) were not rerun to full five-layer/
   eleven-section contract completeness. Their *substantive findings* were independently reproduced
   against the live artifact by this reconciliation and by the original independent checker where the
   finding produced a concrete artifact change (ARC-01, ARC-02, SOURCE-01); those are trusted on that
   independent basis, not on the packet's own authority. Findings that did **not** produce an
   independently-verifiable artifact change (A-17, A-21, A-25, A-26, SYS-03 — all non-change or
   conditional-defer dispositions) remain reasoned but not contract-complete.
2. **The package verifier is not yet a semantic regression guard** (MANIFEST-01, still open) — it can
   report PASS without checking for the specific defects this cycle found and fixed.
3. **Compass's actual recommendation is unmet.** The corrected canonical page is not the same as the
   beat-by-beat founder-decision interface FL-01 asked for (participant job / why present / authority
   class / strongest objection / evidence limit / next test, per artifact beat). Presenting the
   current package to Hunter as-is repeats exactly the failure Compass named: he would have to detect
   what's approved-decision vs. design-judgement vs. untested hypothesis himself.
4. **Rehearsal, render, accessibility, qualified-human and participant-testing gates** are unchanged
   by this document and were never claimed as specialist-loop items.

## Decision

**The specialist panel is now formally closed, contract-registered, and honestly bounded** — not
"informal lenses," and not a second rebuild. The corrections it drove are independently verified live
in the artifact. What is not being claimed: that all 25 roles ran fresh contract-complete reviews, or
that the build is founder-decision-ready as currently packaged.

**Recommended next action (not a new panel, not a rebuild):** build the beat-by-beat founder-decision
interface FL-01 specified — this is bounded production work on the existing candidate, not new
specialist assurance — then run one fresh Compass cold read against *that* interface before bringing
Hunter the viewable build. This is the smallest step between where the build now genuinely is and
Hunter being able to make his decision without doing the reconciliation work himself.

## Learning disposition

`candidate_update` — a bounded panel's findings can be independently verified against the live
artifact even when several packets fall short of full contract completeness; that verification, not
the packet's format alone, is what should determine whether a finding is trusted. Proposed for
`specialist-learning-register.yml` after this record is checked.
