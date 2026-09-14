---
title: "Living Operating Model & Capability Directory"
type: living-operating-model-index
status: active
owner: hunter
created: 2026-07-29
authority: D-0024, M-018, PO-004
confidentiality: internal
---

# MFC Intelligence System — Living Operating Model and Capability Directory V1: Index

**Start here.** This is the one file Hunter (or a future Claude session) opens first to understand the whole system without decoding any technical file. Everything below links to a deeper file only if more detail is wanted.

## What this package is

The permanent, living control map for the MFC Intelligence System — authorised by [[30-decisions/D-0024-living-operating-model-and-capability-directory-v1-authorisation|D-0024]]/[[50-authority/mandates/M-018-mfc-living-operating-model-v1|M-018]], registered as portfolio objective `PO-004`. It replaces the need to remember, across sessions: what the system is meant to become, what exists now, what's missing, who does what, what's authorised, what to build next, and what's already happening elsewhere.

## Package contents

| # | File | What it answers |
|---|---|---|
| 1 | [[90-meta/living-operating-model/01-living-operating-model|01-living-operating-model.md]] | What is the MFC Intelligence System? What can it do now? |
| 2 | [`02-system-map.yml`](02-system-map.yml) | Machine-readable capability/status/dependency record |
| 3 | [[90-meta/living-operating-model/03-capability-directory|03-capability-directory.md]] | Index of every current capability's role card |
| 4 | `role-cards/*.md` | One card per current capability — 25-field format |
| 5 | [[90-meta/living-operating-model/04-system-build-register|04-system-build-register.md]] | What's built, active, proposed, deferred, rejected |
| 6 | [[90-meta/living-operating-model/05-target-domains-and-proposed-systems|05-target-domains-and-proposed-systems.md]] | The 13 approved domains + 6 named future systems, assessed not built |
| 7 | [[90-meta/living-operating-model/06-gap-register|06-gap-register.md]] | Every verified capability gap, prioritised |
| 8 | [[90-meta/living-operating-model/07-dependency-and-build-sequence|07-dependency-and-build-sequence.md]] | What depends on what; recommended build order |
| 9 | [[90-meta/living-operating-model/08-end-state-operating-flow|08-end-state-operating-flow.md]] | How the system should eventually work, end to end |
| 10 | [[90-meta/living-operating-model/09-portfolio-autonomy-integration|09-portfolio-autonomy-integration.md]] | How Portfolio Autonomy uses this map |
| 11 | [[90-meta/living-operating-model/10-update-protocol|10-update-protocol.md]] | When and how this package must be updated |
| 12 | [[90-meta/living-operating-model/11-core-chat-start-protocol|11-core-chat-start-protocol.md]] | What a future core-system Claude session reads first |
| 13 | [[90-meta/living-operating-model/12-hunter-dashboard|12-hunter-dashboard.md]] | Current system state, one screen |
| 14 | [[90-meta/living-operating-model/13-progress-scorecard|13-progress-scorecard.md]] | "Are we on track?" — domain by domain |
| 15 | [[90-meta/living-operating-model/14-deterministic-validation|14-deterministic-validation.md]] | What is mechanically checked about this package |
| 16 | [[90-meta/living-operating-model/15-implementation-and-review-evidence|15-implementation-and-review-evidence.md]] | Build evidence, independent review verdict, correction record |
| 17 | [[90-meta/living-operating-model/17-failure-recovery-process-v1|17-failure-recovery-process-v1.md]] | What happens when a role, skill, or control fails — diagnose, repair the smallest part, independently retest, restore only what passes |

## Answers in one paragraph each

**What is the MFC Intelligence System?** A reusable set of bounded AI capabilities (objective orchestration, knowledge/authority stewardship, evidence discovery, integrity review) plus two control layers (Stage Autonomy V1, Portfolio Autonomy V1) that let Claude Code complete authorised work across the workshop and website workstreams with limited supervision, stopping only at genuine Hunter decisions. See [[90-meta/living-operating-model/01-living-operating-model|01-living-operating-model.md]] §1.

**What has already been built?** A-04 (orchestrator), A-05 (knowledge/authority steward), A-06 (evidence discovery), A-02 (integrity checker, unactivated), Stage Autonomy V1, Portfolio Autonomy V1, and the Phase 0/1 Controlled Automation deterministic-verification layer. See [[90-meta/living-operating-model/03-capability-directory|03-capability-directory.md]].

**What can it genuinely do now?** Only A-04, via the Stage Autonomy V1 / Portfolio Autonomy V1 lineage (`M-013`→`M-018`), currently holds an active mandate. A-05 and A-06's own mandates expired 2026-07-28/29 and have not been renewed — both are built and dormant, not currently authorised to run. A-02 has never been activated for real material. See [[90-meta/living-operating-model/04-system-build-register|04-system-build-register.md]] and the gap register's `G-01`.

**What is the next most important capability gap?** See [[90-meta/living-operating-model/06-gap-register|06-gap-register.md]] — currently `G-01` (A-05/A-06 mandate renewal, if their function is needed again) and `G-02` (no capability yet exists for Framework Integrity and Evidence, the next domain the approved build sequence calls for after the workshop/website workstreams close their current gates).

**What should happen after each existing workstream finishes?** Workshop: Stage 11 review/pilot-readiness, gated on Decision 9. Website: Stage 2 implementation/build, gated on Hunter's own build-vs-defer decision. Neither is advanced by this package. See [[90-meta/living-operating-model/07-dependency-and-build-sequence|07-dependency-and-build-sequence.md]].

## Genuine Hunter decisions raised by this package

None required to complete this objective — see [[90-meta/living-operating-model/10-update-protocol|10-update-protocol.md]] and `M-018`'s decision-rights bounds. The only standing, pre-existing Hunter decisions this package surfaces (not creates) are listed in [[90-meta/living-operating-model/12-hunter-dashboard|12-hunter-dashboard.md]] § "Hunter decisions outstanding".

## What this package does not do

Build, activate, or start any proposed capability domain or named future system. Touch any workshop or website product file. Send communications. Change MFC strategy. Create a second orchestrator. Use Opus.

## Standing rules

- [`16-website-dual-assurance-completion-gate.md`](16-website-dual-assurance-completion-gate.md) — **Rule 13A.** Claims assurance and visitor experience assurance are independent required gates for every website objective. Neither compensates for the other. Established by Hunter, 31 July 2026.
