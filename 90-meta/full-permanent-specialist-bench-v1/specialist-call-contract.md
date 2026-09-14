---
title: "Specialist call contract"
type: operating-standard
status: controlled-pilot
created: 2026-08-13
owner: hunter
maintained_by: A-04 with A-05 and SYS-04
---

# Specialist call contract

This contract distinguishes consulting a role lens from completing a bounded specialist review.
It applies every time material MFC work claims that a registered specialist executed.

The universal live control is
`verify_specialist_call_records.py`. It validates the task-packet contents, source and artifact
paths, review frontmatter, every required review section, source trace, unique output and learning
disposition for all future material work types—not only design-intelligence projects.

Invocation is enforced by `.claude/hooks/enforce_material_specialist_closure.py`. Every new
`MFC_MATERIAL` prompt receives a unique task ID from the intake hook. The task is blocked from stopping
unless a schema-v2 routing record matches that task and the universal validator passes. The record
must contain or point to a reasoned disposition for every registered bench member. Routing nobody
is permitted only when the record preserves why; silent non-use is not.

This is a mechanical process guarantee inside Claude Code sessions using this vault and its live
hooks. It does not guarantee that AI professional judgement is correct, replace qualified-human or
Hunter approval, control work performed in another application, or survive deliberate hook removal.

## Permitted execution modes

- `bounded_specialist_review` — the specialist received the complete five-layer context, answered
  one bounded question and produced its own contract-complete output. This may support internal AI
  specialist assurance, subject to pack state and evidence limits.
- `independent_specialist_review` — the same contract, completed in a genuinely separate context
  without exposure to other reviewers' findings. This is required wherever independence is claimed.
- `same_context_role_lens` — one producing context applied a named perspective during synthesis.
  Useful consultation, but **not a separately executed specialist and not independent assurance**.
- `reuse_current_evidence` — a current, inspectable prior review answers the exact bounded question;
  cite it and explain why it remains applicable.
- `restricted_screen` — an AI preparation or risk screen whose conclusion remains with a qualified
  human. It never clears the human boundary.
- `reconciliation` — Relay or the accountable lead reconciled completed inputs. This is not a new
  domain review.

## Call-time preflight

Before `bounded_specialist_review` or `independent_specialist_review`, save a task packet containing:

1. specialist ID, pack path, pack state and pack version/review date;
2. shared orientation manifest and the authoritative current-state interface used;
3. objective, audience, lifecycle stage and exact artifact/version;
4. one bounded question and the decision or interface it informs;
5. source hierarchy, approved decisions, known conflicts, evidence limits and unknowns;
6. acceptance criteria and adjacent/human boundaries; and
7. prior accepted, narrowed and rejected MFC learning relevant to this call.

If any required context is absent, stale or contradictory, the review stops as `not_equipped` or
`blocked_context_conflict`. It must not improvise through the gap and retain the specialist label.

Before execution, screen the whole registered bench and preserve one reasoned disposition for each
role: route now, reuse current evidence, same-context role lens, defer conditionally, not relevant,
human boundary, not equipped, or reconciliation. This is a relevance screen, not a direction to
manufacture 25 reviews.

For every material task, preserve a separate `coverage_challenge` completed by a reviewer other
than the original selector. It must challenge omissions and unnecessary inclusions against the
actual decision surfaces, record upgrades/downgrades and unresolved uncertainty, and be reconciled
before specialist execution. Efficiency may narrow a routed question; it may not be the sole reason
for omitting a perspective that could materially alter the result.

For a restricted AI screen, the same task packet and output requirements apply; its boundary section
must still name the qualified-human authority. Same-context role lenses and reconciliation are
truthfully limited modes and do not claim separate specialist execution.

## Required output

Each completed review is saved as its own substantive file and states:

- specialist ID, execution mode, pack version/state, task-packet path and artifact reviewed;
- bounded question;
- exact sources reviewed;
- professional principles applied;
- position and strongest objection;
- evidence strength and limitations;
- alternatives considered;
- recommendation and what would change the view;
- adjacent-specialist or qualified-human boundary; and
- proposed learning, or the explicit statement `No new learning proposed`.

One combined synthesis may summarise many outputs, but it cannot be cited as each specialist's own
output. Reusing one file path across several specialists is valid only for `same_context_role_lens`
or `reconciliation`, and must be labelled that way.

## Reconciliation and learning return

Every material finding receives `accepted`, `narrowed`, `rejected`, `unresolved` or `escalated`, with
a reason and any artifact change. Every review also receives a learning disposition:
`no_new_learning`, `candidate_update`, or `writeback_completed`.

A candidate does not become pack knowledge merely because a specialist said it. Follow
`specialist-knowledge-standard.md`: verify the claim and source, check authority/conflicts,
reconcile it, update the canonical source first where meaning changed, append the learning record,
and test reusable corrections. Preserve rejected advice.

## Assurance language

Recent activity and assurance are separate facts. A fresh `same_context_role_lens` may be useful and
recent while remaining limited assurance. Pack existence, a role name, a shared synthesis, a recent
timestamp or a passing structural check cannot be translated into professional approval.
