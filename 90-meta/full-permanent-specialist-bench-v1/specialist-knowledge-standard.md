---
title: "Specialist knowledge, calibration and learning standard"
type: operating-standard
status: controlled-pilot
created: 2026-08-13
owner: hunter
maintained_by: A-05 with A-06 and A-23
confidentiality: internal
---

# Specialist knowledge, calibration and learning standard

## Purpose

A role card explains what a specialist is meant to do. It does not by itself equip that specialist
to do it well. Every routed specialist must arrive with enough current MFC context, professional
knowledge, source traceability and prior organisational learning to provide a genuine expert lens
rather than a plausible generic opinion.

This standard extends the existing permanent bench. It does not create private agent databases or
a parallel organisational knowledge base.

## The five-layer specialist context

Every equipped specialist receives:

1. **Shared MFC orientation** — mission, strategy, audience, products, founder intent, language,
   current state, source precedence and authority boundaries from `onboarding-manifest-v1.yml`.
2. **Professional toolkit** — the theories, principles, evidence traditions, debates and failure
   modes that materially govern the role.
3. **MFC domain position** — what MFC currently believes or has decided in that domain, clearly
   separated from external evidence and provisional analysis.
4. **Accumulated MFC learning** — accepted, narrowed and rejected recommendations; Hunter or human
   corrections; observed results; known failures; and implications for the next use.
5. **Task packet** — the current objective, audience, artifact, decision, relevant sources,
   conflicts, evidence limits, human boundaries and exact bounded question.

The first four layers are maintained between tasks. The fifth is assembled at routing time.

## Knowledge-pack states

- `role_only_not_equipped` — role and method exist; no curated domain pack. May be screened for
  relevance but may not be represented as domain assurance.
- `baseline_pack` — a source-linked starting toolkit and MFC position exist; suitable for a
  controlled live evaluation, not mature professional assurance.
- `evaluated_pack` — the pack and agent have passed representative live/holdout tests with an
  independent reviewer.
- `current_operational_pack` — evaluated and refreshed within its stated review interval, with
  material corrections propagated.
- `restricted_human_boundary` — AI preparation is equipped, but the conclusion or approval remains
  with a qualified human.
- `stale` — a refresh trigger has fired and the pack must be checked before it bears a decision.

Registration, routing frequency and a structurally complete role card do not advance these states.

## Required pack contents

Each entry in `specialist-knowledge-index.yml` must identify:

- specialist ID, display name, domain and pack state;
- last review date, next review date or event trigger, and accountable maintainer;
- core professional principles and named limitations;
- canonical source paths supporting those principles;
- current MFC domain positions and their authority type;
- open questions and known disagreements;
- accepted, narrowed and rejected learning records;
- evaluation evidence and known failure modes; and
- human or adjacent-specialist boundaries.

Packs point to canonical sources; they do not copy whole research libraries or convert analysis into
authority by repetition.

## Routing contract

The mechanically enforced contract and templates are in `specialist-call-contract.md`,
`specialist-task-packet-template.yml` and `specialist-review-template.md`. A same-context role lens
may inform a synthesis, but it is not a separately executed specialist review and may not be
presented as one.

Before a specialist executes, the orchestrator must load:

1. the shared orientation;
2. that specialist's current pack;
3. the task packet; and
4. any sources specifically required by the bounded question.

The specialist output must state:

- sources and pack version used;
- professional principles applied;
- position and strongest objection;
- evidence strength and limitations;
- alternatives considered;
- recommendation and what would change it;
- required adjacent specialist or human boundary; and
- proposed learning, if anything genuinely new was learned.

The task packet and review output must be saved as inspectable files for bounded or independent
reviews. Every routing/receipt entry declares its truthful execution mode and learning disposition.
One combined report cannot be reused as the individual output of several bounded specialists.

If a decision-bearing specialist is `role_only_not_equipped` or `stale`, the objective must first
equip/refresh it or disclose that the lens has not been supplied. Naming the role is not assurance.

## Controlled learning write-back

Agents do not autonomously add every output to their own knowledge. A proposed learning follows this
route:

1. **Capture:** the specialist labels the candidate as external evidence, MFC observation, human
   correction, accepted/rejected recommendation, hypothesis or failure.
2. **Verify:** A-06 checks research claims; A-23 checks source identity and linkage; A-05 checks
   organisational authority and conflicts.
3. **Reconcile:** SYS-04 records whether it is accepted, narrowed, rejected, unresolved or
   escalated and what operational artifact changed.
4. **Write back:** update the canonical source first where meaning changed, then update the pack's
   pointer/summary and append its learning record. Preserve rejected and superseded advice.
5. **Test:** a reusable correction requires a regression or fresh-context evaluation under the
   existing Correction Propagation and Learning Protocol.

Every completed review records one learning disposition even when no write-back is warranted:
`no_new_learning`, `candidate_update`, or `writeback_completed`. This makes an omitted learning
return visible without manufacturing knowledge.

No participant personal data belongs in a pack. Use aggregated or de-identified findings only.

## Weekly maintenance

The Monday evidence cycle reviews, without manufacturing updates:

- the latest evidence-watch digest and any completed full-text evidence-research records;
- new approved decisions and canonical artifact changes;
- routed specialist outputs and their reconciliation dispositions;
- Hunter, committee, qualified-human, participant, facilitator or host corrections/feedback; and
- pack freshness triggers and unresolved conflicts.

For each pack the cycle records `no_change`, `candidate_update`, `updated`, `stale`, or
`human_review_required`. Abstract-only evidence-watch findings remain candidates and cannot update a
core principle. A quiet week produces no artificial learning.

## Evaluation

An agent is not equipped merely because the pack exists. For promotion beyond `baseline_pack`, test:

- a normal live case;
- a premise-challenge case;
- an ambiguity or conflicting-source case;
- a boundary/refusal case;
- an adjacent-domain handoff;
- a stale/missing-source case; and
- whether the advice materially improves an artifact without overclaiming.

Evaluation must identify what the specialist caught, missed, duplicated, got wrong and changed.
Hunter response is useful evidence of value but does not prove scientific or professional truth.

The complete case design, separation, scoring, promotion, critical-failure and refresh rules are in
`specialist-substantive-evaluation-standard.md`. Keyword checks, role-name presence, routing-table
membership and structural completeness may verify plumbing but can never promote a pack.

## Governance decision

No new persistent specialist is needed. The concrete gap is missing knowledge, calibration and
learning infrastructure for the existing roles. Improve those roles first; reconsider capability
creation only if live evaluations expose a distinct recurring responsibility with no owner.
