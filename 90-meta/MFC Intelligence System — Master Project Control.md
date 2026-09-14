---
type: master-project-control
current_stage: "Stage 9 COMPLETE. Stage 10 COMPLETE. Stage 11 AUTHORISED TO BEGIN (D-0044, 2026-07-31), NOT STARTED -- D-0016 blocks final pilot-ready approval and all participant-facing delivery only, not Stage 11 entry. Full detail: SS3/SS10 below; historical current_stage text archived in state-history.md 2026-08-02 under D-0053."
active_decision: "none"
as_of_commit: "cf28d3af60caa5d377414e3c03cced9b2a45a735"
---

# MFC Intelligence System — Master Project Control

**Canonical roadmap and controlling source**

**Owner:** Hunter Karam  
**Status:** Active  
**Compacted 2026-08-02 (`D-0053`):** the explicitly self-labelled "(Retained... superseded)" historical
paragraphs below and in §10 were moved verbatim to [[90-meta/state-history|state-history.md]] —
nothing judged current was touched, and §11's dated change-control ledger is untouched by design
(it is meant to accumulate). **The "Current stage" paragraph immediately below this notice is
itself stale** — it predates `D-0044`'s Stage 11 correction and everything merged since
`D-0049` (2026-08-01). Verify current position directly (`git log main`, recent `D-`/`M-`/`L-`
records, [[90-meta/Current State and Next Action|Current State and Next Action.md]]) rather than
trusting this paragraph's content; rewriting it correctly needs a dedicated reconciliation task
that actually checks every workstream, which this housekeeping pass deliberately did not attempt.  
**Parallel system workstream:** `CONTROLLED AUTOMATION V1 — PHASE 0 COMPLETE (BATCH A AND BATCH B MERGED); PHASE 1 (READ-ONLY DETERMINISTIC VERIFICATION) IMPLEMENTED, REVIEWED, CORRECTED — MERGED`, per `D-0006`/`D-0007` (architecture), `D-0009` (Phase 0 specification approval), `D-0011`/[[30-decisions/D-0012-phase0-batch-a-merge-and-batch-b-task-preparation-authorisation|D-0012]] (Batch A/Batch B authorisations), and Hunter's chat-recorded approvals of Batch B and Phase 1 implementation. Not a roadmap stage; does not alter the workshop's Stage 9 status below. See §11, 2026-07-29 entries, for full detail.  
**Current stage:** Stage 9 COMPLETE. Stage 10 COMPLETE. Stage 11 AUTHORISED TO BEGIN (`D-0044`, 2026-07-31), NOT STARTED — `D-0016` blocks final pilot-ready approval and all participant-facing delivery only, not Stage 11 entry (matches this record's own `current_stage` frontmatter field, compacted under `D-0053`). Full detail follows: Stage 9 — Produce design requirements and product strategy — **COMPLETE WITH EXPLICIT DOWNSTREAM GATES**. Decisions 1–7 approved as previously recorded (`D-0003`, `D-0004`, `D-0005`, `D-0008`, `D-0010`, `D-0013`, `D-0014`). **Hunter delegated product-design authority to Claude for Decisions 8–11, 29 July 2026** (see §11, delegation entry): Decision 8 (`D-0015`, universal minimum choice/opt-out/disclosure controls); Decision 9 (`D-0016`, safeguarding — design-level/facilitator-scope components decided; the mandatory pre-pilot gate remains **unresolved**, pending qualified legal/clinical validation); Decision 10 (`D-0017`, minimum low-burden measurement architecture, extended for the three-moment Radar); Decision 11 (`D-0018`, minimum quality-assurance/consistency system extending Decision 7's own taxonomy). The consolidated Stage 9 product-strategy deliverable is [[60-projects/workshop-evidence-informed-adult/04-design-requirements/16-stage9-consolidated-product-strategy|60-projects/workshop-evidence-informed-adult/04-design-requirements/16-stage9-consolidated-product-strategy.md]]. Stage 9's original authorisation (not-started) is recorded in `D-0002`. **Stage 10 — Build the pilot workshop package — is now COMPLETE.** Hunter explicitly authorised Stage Autonomy V1 to execute Stage 10 (`D-0020`, `M-014`, 2026-07-29), extending the control loop built and synthetically proven under `D-0019`/`M-013` to this one live workshop objective. The complete thirteen-component package (`60-projects/workshop-evidence-informed-adult/05-stage10-workshop-package/`) was built, independently reviewed (one Sonnet reviewer, verdict **PASS**, zero critical/major/minor findings, no correction pass required), and merged to `main`. Every essential function from Decisions 1–11 is preserved unaltered; Decision 9's safeguarding gate remains **unresolved and unsatisfied**, exactly as before — no distress-response, referral, escalation, or mandatory-reporting content was drafted; no live Google document was edited; no pilot readiness is declared; **Stage 11 has not begun; no participant-facing delivery is authorised.** See §11 change log, 2026-07-29 entries, for full detail.

**Inter-stage change control, 2026-07-27 (after Stage 7, not a new stage):** Hunter approved a roadmap amendment adding four controls identified through the Stage 7 source-retrieval failure (Stage 8 entry gate; Hunter decision-explanation standard; Stages 10–11 pilot-readiness controls; just-in-time timing for the Project Learning and Memory Steward). **Approved and operational** — see §11 change log. **Correction on approval:** the bounded Stage 8 source-readiness check is the next required procedural action once merged — it does not require a separate Hunter authorisation decision. Hunter's next genuine decision occurs after that check, deciding whether the verified state supports authorising Stage 8 broad evidence discovery. **Stage 8 remains not authorised** until that decision is made.

**Pre-Stage 8 research-agenda quality gate, 2026-07-28 (procedural, not a new stage):** the Stage 8 source-readiness check passed. A subsequent research-agenda quality gate found the handoff's original 10 questions could not be authorised unchanged; Hunter approved a final 9-question agenda (F1–F9) and execution order, superseding the handoff's 10 questions for Stage 8 execution — see §11 change log. **This approval is agenda-only; it does not authorise Stage 8 broad evidence discovery.** Stage 8 remains not authorised.  
**Parallel system workstream, merged 2026-07-31:** `PROJECT LEARNING AND MEMORY V1 — HUMAN INTENT, DECISION LINEAGE AND REASONING CONTROL — MERGED TO MAIN`, per `D-0032`/`M-032`/`PO-011`. Not a roadmap stage. Available for **controlled operational use**; **not yet operationally mature and not yet proven reusable**, having never governed an independent live objective. No new permanent agent was created; A-04, A-05 and A-06 carry the integrated responsibilities. **Website product work remains paused** until a separately authorised website pre-synthesis reconciliation objective begins, which will be this control layer's first independent live application.

**First production project:** Evidence-informed MFC adult workshop

## 1. Overarching objective

Build a reusable MFC intelligence system that can:

1. receive an organisational objective;
2. retrieve the correct authoritative MFC context;
3. determine the evidence, expertise and work required;
4. coordinate the minimum reusable specialist capabilities;
5. complete an approved stage with limited supervision;
6. review important outputs proportionately;
7. involve Hunter only at genuine decision points;
8. maintain a live dashboard and exact resume state;
9. retain evidence, decisions, corrections and learning;
10. improve future projects through better context and proven workflows.

The workshop is the first real project used to build and prove this system.

## 2. Target operating model

Hunter approves an objective and project charter. The system then runs one approved stage until:

- the stage is complete;
- a genuine Hunter decision is required;
- a stop condition is triggered;
- usage or permissions prevent continuation.

This is stage autonomy, not unrestricted autonomy.

## 3. Current position

### Substantially established

- Structured Obsidian vault.
- Sources, knowledge, conflicts, decisions and authority records.
- Capability and learning structure.
- Git history.
- Management-controlled internal advisory AI authority.

### Partially established

- A-02 Integrity Reviewer.
- Evaluation and remediation work.
- Context-bounded review model.

### Not yet operational

- MFC Objective Orchestrator v0.
- Knowledge and Authority Steward.
- Reusable Evidence Discovery and Synthesis capability.
- Persistent project dashboard.
- Proven resume workflow.
- Autonomous looping.

### A-02 facts

- It has not passed.
- It is not active.
- It has not reviewed real MFC material.
- It detected serious planted issues but over-flagged clean material.
- Its immediate target is supervised, context-bounded review.
- It is a quality checkpoint, not the research engine or orchestrator.

## 4. Fixed roadmap

### Stage 0 — Recover exact repository state

**Deliverable:** branch, HEAD, main HEAD, working tree, partial files, interrupted tasks, relevant branches, exact A-02 state and safest next action.  
**Rules:** Sonnet Medium; no editing, testing, subagents or Opus.

### Stage 1 — Create operating pack and dashboard

Create one permanent source of operating truth, templates, model policy, anti-drift rules, live dashboard and workshop project folder.  
**Rules:** no workshop research and no A-02 evaluation.

### Stage 2 — Close A-02 narrowly

Target supervised, context-bounded evidence and draft review.

**Permitted:**

- one correction pass;
- one concise regression;
- one small unseen test;
- one human decision.

**Stop if Claude proposes:**

- another harness;
- another canary;
- a security-engineering programme;
- governance redesign;
- reviewer-of-reviewer chains.

### Stage 3 — Build MFC Objective Orchestrator v0

**Minimum functions:**

- accept one objective;
- define deliverables and completion criteria;
- identify required context and specialist roles;
- sequence work;
- enforce usage and review limits;
- update dashboard and resume state;
- stop at Hunter decision gates.

### Stage 4 — Build Knowledge and Authority Steward v0

**Minimum functions:**

- distinguish authoritative, provisional, historical and rejected records;
- identify unresolved conflicts;
- prepare bounded context packets;
- identify missing context;
- prevent drafts being treated as approved MFC positions.

### Stage 5 — Build and test Evidence Discovery and Synthesis v0

**Minimum functions:**

- convert objectives into research questions;
- discover adjacent lenses beyond Hunter’s prompts;
- search broadly and reproducibly;
- prioritise strong current evidence;
- record contradictory evidence and limitations;
- maintain a Missing Lenses Register;
- produce traceable syntheses and MFC implications.

**Bounded test question:**

> What most influences whether adults transfer a skill learned in a workshop into everyday behaviour?

### Stage 6 — Approve Workshop Intelligence Programme charter

Lock audience, outcomes, research standards, product questions, specialist assignments, decision gates, output requirements and usage budget.

### Stage 7 — Establish MFC teaching and outcomes spine

Define:

- audience;
- problem;
- knowledge outcomes;
- skill outcomes;
- transfer outcomes;
- essential content;
- intended behaviour;
- exclusions;
- unresolved choices.

### Stage 8 — Run broad evidence discovery

**[APPROVED, 2026-07-27 by Hunter — operational] Entry gate.** Broad evidence discovery may not begin until:

- load-bearing internal MFC sources are registered or explicitly linked;
- current Drive-controlled sources have been checked rather than assuming the local vault is complete;
- authority, approval, version and supersession status are clear;
- unresolved conflicts and missing sources are listed;
- full-text access exists for load-bearing evidence, or limitations are recorded and escalated;
- abstract-only, summary-derived or inaccessible evidence cannot silently become decision-grade support;
- research questions trace to the approved Stage 7 spine;
- dashboard and exact resume state are current.

*Approved following the Stage 7 source-retrieval failure (see change log, 2026-07-27). This gate does not itself perform the check. Per Hunter's approval, the bounded Stage 8 source-readiness check is now the next required procedural action — it does not require a separate Hunter authorisation decision to begin. Hunter's next genuine decision occurs after that check, when deciding whether the verified state supports authorising Stage 8 broad evidence discovery.*

Research:

- adult learning;
- learning science;
- behaviour change;
- transfer;
- implementation;
- motivation;
- active learning;
- cognitive load;
- psychological safety;
- facilitation;
- accessibility;
- dosage;
- evaluation;
- product adoption;
- newly discovered material lenses.

### Stage 9 — Produce design requirements and product strategy

Translate evidence into workshop requirements.

Compare no more than three credible product formats against:

- learning;
- transfer;
- access;
- adoption;
- delivery;
- scale;
- evaluation;
- MFC fit.

### Stage 10 — Build the pilot workshop package

Build:

1. participant journey;
2. learning sequence;
3. session architecture;
4. explanations;
5. experiences;
6. practice;
7. transfer;
8. facilitator guide;
9. participant resources;
10. slides;
11. evaluation;
12. follow-up and pilot plan.

### Stage 11 — Integrated review and pilot readiness

One independent integrated review and one correction pass.

**[APPROVED, 2026-07-27 by Hunter — operational] Pilot-readiness controls (Stages 10–11).** Without changing either stage's existing purpose, pilot readiness requires verification of:

- privacy and consent;
- data access, retention and reporting rules;
- minimum reporting thresholds;
- safeguarding and escalation;
- non-clinical boundaries;
- accessibility and inclusion;
- facilitator competence and delivery fidelity;
- host responsibilities;
- workshop and measurement version control;
- permitted claims;
- handling of adverse or unexpected participant responses;
- pre-specified pilot learning questions;
- minimum acceptable data quality;
- proceed, revise and stop criteria;
- limits on what the pilot can establish.

*These materials are not built now — this records what Stage 10–11 must verify before pilot readiness is declared. Approved and operational; resolved during Stages 10–11, not before.*

**Final status:**

> **Pilot-ready, not yet proven.**

### Stage 12 — Pilot, learn and improve

Record:

- participant outcomes;
- facilitator learning;
- product barriers;
- false assumptions;
- capability failures;
- corrections;
- reusable workflows.

## 5. Reusable capabilities

### Core

1. MFC Objective Orchestrator
2. A-02 Integrity Reviewer
3. Knowledge and Authority Steward
4. Evidence Discovery and Synthesis Lead
5. Project Learning and Memory Steward — **[APPROVED, 2026-07-27 by Hunter — operational] timing:** not required for Stage 8 entry; to be created or formally assigned just in time during Stage 11, before pilot readiness is approved; must preserve versioned assumptions, decisions, corrections, delivery deviations, evidence, results and lessons for Stage 12; must not be built earlier without a demonstrated dependency.

### Developed through the workshop

6. Learning and Behaviour Design Lead
7. Product and Adoption Lead
8. Workshop Experience and Facilitation profile
9. Evaluation and Measurement profile

These are reusable roles given project-specific assignments, not workshop-only or website-only agents.

## 6. Hunter’s role

Hunter decides:

- organisational objectives;
- strategic direction;
- authoritative MFC positions;
- consequential product choices;
- approval at decision gates;
- pilot and public claims.

Hunter should not need to:

- launch every task;
- prompt each agent;
- reconstruct interrupted sessions;
- supervise routine drafting;
- approve low-consequence operational work.

**[APPROVED, 2026-07-27 by Hunter — operational] Hunter decision-explanation standard.** Every genuine Hunter decision must explain:

- what is being decided;
- why it is required now;
- supporting authoritative records and evidence;
- uncertainty or conflict;
- realistic alternatives;
- recommended position;
- consequences of approval, deferral and rejection;
- reversibility;
- what follows after approval.

Also:

- settled rules must not be manufactured into Hunter decisions;
- consequential decisions must be explained before an approval prompt is presented;
- provisional assumptions must be distinguished from final MFC positions.

## 7. Non-negotiable anti-drift rules

Every Claude task must state:

- current roadmap stage;
- objective;
- exact deliverable;
- inputs;
- permitted work;
- excluded work;
- definition of done;
- decision gates;
- model and effort;
- maximum subagents;
- maximum review cycles;
- usage/time budget;
- stop conditions;
- dashboard and resume requirements;
- response-length cap.

New issues are classified:

1. Must resolve now
2. Record and continue
3. Future improvement

Only category 1 may interrupt the stage.

Additional rules:

- Sonnet Medium by default.
- Sonnet High only for bounded complex synthesis or final review.
- Opus requires Hunter’s explicit approval.
- One independent review and one correction pass per major deliverable.
- No reviewer-of-reviewer chains.
- No silent scope expansion.
- No automatic promotion of research into authoritative MFC knowledge.
- No agent approval, publication or implementation authority.
- Checkpoints normally under 500 words.
- Dashboard and resume state updated before stopping.
- Usage and time are formal constraints.

## 8. Tool split

### ChatGPT Project

- maintains strategy and roadmap;
- drafts bounded Claude prompts;
- reviews Claude checkpoint reports;
- detects drift;
- prepares Hunter decisions;
- updates this control document after approved changes.

### Claude Code

- reads and changes the Obsidian vault;
- performs Git operations;
- executes approved stages;
- launches bounded roles;
- updates dashboard and resume state.

### Obsidian

The operational source of truth for authoritative MFC context, capabilities, project status, evidence, decisions and learning.

Chat history is not the operational source of truth.

## 9. Mandatory workflow

1. ChatGPT identifies the current stage.
2. ChatGPT drafts one bounded Claude prompt.
3. Hunter confirms the objective.
4. Claude verifies repository state.
5. Claude performs only the approved task.
6. Claude updates dashboard and resume state.
7. Claude returns a short checkpoint.
8. Hunter pastes the checkpoint into the ChatGPT Project.
9. ChatGPT checks scope, safety and the next stage.
10. This roadmap changes only through an approved recorded decision.

## 10. Current next action

**Stage 0 is complete**, approved by Hunter 27 July 2026, on the basis of a read-only repository verification checkpoint (branch, HEAD, main HEAD, working tree, partial files, relevant branches, exact A-02 state and safest next action all confirmed).

**Stage 1 is complete and merged into `main`**, approved by Hunter and ChatGPT: operating-pack index, standard task-brief template, checkpoint/exact-resume template, model/usage/review policy, anti-drift and issue-classification protocol, live system dashboard, and the evidence-informed adult workshop project shell (scaffolding only) all exist on `main`.

**Stage 2 — Close A-02 narrowly — is COMPLETE.** Hunter approved the blocked decision 27 July 2026: A-02 remains unpassed, inactive, and prohibited from real-material review.

**Stage 3 — Build MFC Objective Orchestrator v0 — is COMPLETE.** A-04 approved for bounded controlled use under M-010, merged into `main`.

**Stage 4 — Build Knowledge and Authority Steward v0 — is COMPLETE.** A-05 approved for bounded controlled use under M-011, merged into `main`.

**Stage 5 — Build and test Evidence Discovery and Synthesis v0 — is COMPLETE.** A-06 approved for bounded controlled use under M-012, merged into `main`.

**Stage 6 — Approve Workshop Intelligence Programme charter — is COMPLETE.** Charter approved under Hunter's three decisions, merged into `main`.

**Stage 8 — Run broad evidence discovery and assurance — is COMPLETE.** Hunter approved closure 28 July 2026, per `D-0002` ([[30-decisions/D-0002-stage8-closure-stage9-authorisation|30-decisions/D-0002-stage8-closure-stage9-authorisation.md]]), following nine completed F1–F9 evidence runs, one integrated synthesis, one independent review, and one authorised correction pass, all merged into `main`. 0 critical and 0 major issues remain; 2 minor issues carried forward, uncorrected. See §11 change log, 2026-07-28 entry, for full detail.

**Stage 9 is now `COMPLETE WITH EXPLICIT DOWNSTREAM GATES`.** Under Hunter's delegated product-design authority (§11, delegation entry below), Decisions 8, 9, 10, and 11 were decided in one consolidated task: Decision 8 (`D-0015`, universal minimum controls); Decision 9 (`D-0016`, design-level/facilitator-scope safeguarding decided, mandatory pre-pilot gate unresolved); Decision 10 (`D-0017`, minimum low-burden measurement architecture); Decision 11 (`D-0018`, minimum quality-assurance/consistency system). The consolidated Stage 9 product-strategy deliverable, participant-experience review, completed Forms Reconciliation Register, one independent review, and one unexecuted Stage 10 prompt are all complete. *(This paragraph's own closing sentence is superseded below — Hunter's approval to begin Stage 10 was given and exercised on 2026-07-29, per `D-0020`/`M-014`; see the Stage 10 completion entry immediately below and the §11 change log.)*

**Stage 10 — Build the pilot workshop package — is `COMPLETE`.** Hunter's approval to begin Stage 10, sought at the close of the paragraph above, was given 2026-07-29 (`D-0020`, `M-014`); Stage Autonomy V1 executed the production run; the complete thirteen-component package was built, independently reviewed (verdict `PASS`, zero findings), and merged to `main`. Decision 9's mandatory pre-pilot safeguarding gate (`D-0016`) remains unresolved and unsatisfied, exactly as carried forward from Stage 9 — Stage 10 completion does not touch or narrow that gate. See §11, 2026-07-29 entry ("Stage Autonomy V1 authorised for, and executed against, workshop Stage 10"), for full detail.

**Stage 11 — Integrated review and pilot readiness — is `AUTHORISED TO BEGIN`, `NOT YET STARTED`.** **Corrected 2026-07-31, per `D-0044`** (superseding this paragraph's own prior wording, which read Stage 11 itself as `BLOCKED` pending D-0016 resolution — a stricter reading than `D-0016`'s own text or this Master Project Control's own §4 Stage 11 definition support). `D-0016` does not block entry into Stage 11. `D-0016` blocks **final pilot-ready approval and all participant-facing pilot delivery** until its six named safeguarding matters (distress-response content and referral-pathway design; escalation thresholds; emergency-response procedure; mandatory-reporting and jurisdiction-dependent legal requirements; host responsibilities; insurance and clinical-governance sign-off) are resolved by the appropriate qualified authority and Hunter/the appropriate MFC governance authority formally approves the resulting complete safeguarding model, per `D-0016`'s own preserved gate text ("MUST RESOLVE BEFORE PILOT-READY APPROVAL AND BEFORE ANY PARTICIPANT-FACING PILOT DELIVERY") and §4's own design ("resolved during Stages 10–11, not before"). **Stage 11's integrated review is the authorised mechanism for resolving and verifying the six D-0016 matters — not a stage barred from starting until they are pre-resolved elsewhere.** **The exact global next action is a Hunter decision/review gate, not a Claude execution task: Hunter separately authorises the start of substantive Stage 11 work, and — within it — the qualified legal and clinical-governance input `D-0016` items 1–6 require remains reserved to qualified authorities, not MFC's committee.** No Claude task may begin substantive Stage 11 work, resolve or reinterpret D-0016's six items, appoint a reviewer, conduct outreach, or declare pilot readiness without that separate, explicit Hunter decision. `D-0016` remains in force, unresolved, 0 of 6 matters closed.

**Parallel Portfolio Autonomy V1 workstreams — not roadmap stages, do not compete with or substitute for the Stage 11 gate above.** Six further bounded objectives completed and merged after Stage 10, each under its own Hunter chat authorisation, none altering the fixed Stage 0–12 roadmap and none touching Decisions 1–11 or the D-0016 gate: Website Intelligence Stage 3 (`D-0025`/`M-019`/`PO-005`, 2026-07-29, Hunter's own further review of the package itself still outstanding); Framework Integrity and Evidence Observatory V1 (`D-0026`/`M-020`/`PO-006`, 2026-07-30); Workshop Product Experience Assurance V1 (`D-0027`/`M-023`/`PO-007`, 2026-07-30, Hunter's own founder review of its output still outstanding); Core Operations Hardening and Token Efficiency V1 (`D-0028`/`M-024`/`PO-008`, 2026-07-30); Retrieval Reliability and Source Precedence Evaluation V1 (`D-0029`/`M-025`/`PO-009`, 2026-07-30); Evidence Discovery and Synthesis Reliability V1 (`D-0030`/`M-028`/`PO-010`, 2026-07-30). Full detail for each is recorded in the §11 change-control entry dated 2026-07-31 below. These are Portfolio Autonomy workstream reviews for Hunter, not global-roadmap next actions — the single global next action remains the Stage 11/D-0016 decision gate stated above.

**Outcome Delivery Orchestrator operating model + first live proof, canonicalised 2026-08-01 (`D-0049`/`M-047`) — parallel track, does not touch or substitute for the Stage 11/D-0016 gate above.** Hunter authorised a permanent operating-model change: A-04 upgraded from a planning-only capability (v0, `M-010`, historical) to the accountable executive agent for authorised production objectives (v1, `M-047`, `supervised-real-review`), governed by the Complete-Candidate Standard (now including a permanent Candidate Integrity Closure Gate) and its supporting protocols at `90-meta/outcome-delivery-orchestrator-v1/` (17/17 regression cases passing). As this operating model's first live proof, a complete three-page website candidate (Home, Mental Fitness, Building Mental Fitness, plus an optional supporting glossary) was produced, reconciling the live pages against `D-0034`'s fuller approved architecture, addressing `D-0046`'s outstanding Gina-feedback glossary gap as a deliberate, disclosed reversal of that record's own prior decision, and integrating governed input from six specialists (A-07/08/09/12/18/22). A follow-on Candidate Integrity Closure objective found and resolved four further control conflicts before ratification: a genuine authority-identifier collision (`D-0043`/`M-042` renumbered to `D-0049`/`M-047`, the earlier legitimate `D-0043`/`M-042` lineage on `ops/mental-fitness-page-live-proof-v1` left untouched); a capability-discovery failure (A-18/A-22 were wrongly claimed absent from this vault — both are canonical, `PERMANENTLY_REGISTERED` capabilities in the 23-capability specialist bench at `90-meta/full-permanent-specialist-bench-v1/specialist-bench.yml`); a non-compliant review model (an initial independent review run with Opus without Hunter's required task-specific approval, reclassified `NON_COMPLIANT_SUPPORTING_EVIDENCE_ONLY`); and an unclassified scope addition (the glossary, now explicitly `OPTIONAL_SUPPORTING_COMPONENT`, never a mandatory journey step). A compliant Sonnet reviewer independently re-verified all of the above from primary sources and returned `READY_FOR_HUNTER_RATIFICATION`. **Hunter ratified the completed candidate as MFC's current official website direction, 2026-08-01** (`D-0049` addendum) — this approval does not authorise Wix implementation, publication, or claims that real users have validated the predicted experience. Both branches (`ops/outcome-delivery-orchestrator-v1`, then `ops/website-three-page-complete-candidate-v1`) were merged into `main`, system first, at merge commits recorded in the §11 change-control entry dated 2026-08-01 below. Outstanding before any publication: qualified safeguarding confirmation of the footer crisis-line's sufficiency; Alysse's final visual/responsive design review; genuine audience validation of the untested assumptions A-22 identified; and a classification decision on whether the unbuilt "How it all connects" diagram is required before publication. No Wix or publication occurred. This is a Portfolio-Autonomy-style workstream review for Hunter, not a global-roadmap next action — the single global next action remains the Stage 11/D-0016 decision gate stated above.

## 11. Change control

This roadmap can change when real work proves a better route. It cannot change silently.

Every material change records:

- what changed;
- why;
- supporting evidence or experience;
- impact on remaining stages;
- Hunter’s approval;
- date.

### Change log

**2026-08-01 — Self-review of D-0051 (`L-010`, `L-011`, `L-012`).** The Outcome Excellence Standard
applied to itself at Hunter's direction. Four defects found in the corrective objective: a false
positive published as evidence in three control records (A-06 reported missing from the specialist
bench when it is a registered control-layer capability under `M-012`) — retracted everywhere; no
execution path actually ran the new controls, reproducing the nominal-execution failure D-0051 had
just diagnosed; the Lesson Binding Register was itself unverified and three bindings proved
decorative; and — the material one, found by adversarial review — **the excellence gate was never
wired to the closure verdict**, so none of its claims were enforced where the verdict was produced.
Closed by `verify_objective_closure.py`, which derives the verdict from artefacts on disk.
Regression 17 → 25 cases; all controls now run from `run_all_controls.py`, referenced in CLAUDE.md
§9. No roadmap stage, `D-0016` matter, kernel record or website artefact changed.

**2026-08-01 — Outcome Excellence and Learning Binding (`D-0051`, `M-049`).** Hunter identified,
for the third consecutive objective, that delivered work was technically compliant but not
excellent, and that he was the one detecting it. Investigation confirmed six structural causes:
specialist routing was nominal (the bench mandates structured outputs; a repository-wide search
found none ever produced); the Complete-Candidate Standard measured presence, not strength, and
the independent review inherited that blindness by design; assurance was self-graded against
hand-authored fixtures; evidence relevance was self-judged (40+ recordings reachable, one used,
the named messaging authority's seven sessions unread); lessons bound to no control; and no
closure status existed meaning "complete but not excellent". Adds the Outcome Excellence Standard
(checked *before* completeness, with six new failure statuses), Specialist Execution Binding plus
an artefact-level verifier, the Evidence Sufficiency Floor, and the Lesson Binding Register (now
mandatory at session start). Seven lessons `L-003`–`L-009` added, each bound to an executable
control. Regression suite 17 → 24 cases, all passing. **No roadmap stage, `D-0016` matter, kernel
record, or website artefact was changed.** Stage 11's authorised next action is unaffected.
Discloses two open defects: `id_reservation_ctl.rb` now returns identifiers six or more numbers
behind actual usage and cannot be relied on for allocation; and `M-035` is duplicated on `main`
in the reservation ledger, surfaced rather than silently reconciled.

**2026-07-27 — Stage 0 → Stage 1 transition**
- **What changed:** Status header and §10 updated to record Stage 0 as complete and Stage 1 as the current authorised action. No change to §1 (overarching objective) or §4 (fixed roadmap) — stage definitions and sequence are unaltered. **Verification note (added on independent review):** this document had no prior git-tracked version on `main` at the time of this edit, so §1/§4-unchanged is confirmed by direct content review against the version supplied for this task, not by a git diff against an earlier committed revision. From this commit onward, git history can verify future changes directly.
- **Why:** Stage 0's read-only repository verification was completed and its checkpoint reviewed by Hunter.
- **Supporting evidence:** Stage 0 checkpoint confirming branch `fix/a-02-over-escalation-v1` at HEAD `218cb19`, `main` at `6cb99fa`, working-tree state, untracked regression/holdout directories, and A-02/M-009 protected-state facts as recorded at the time.
- **Impact on remaining stages:** None. Stage 1 begins under its existing rules (no workshop research, no A-02 evaluation).
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 1 complete and merged; status correction**
- **What changed:** Status header and §10 updated to record Stage 1 as complete, reviewed, corrected and merged into `main`, and current position as awaiting Hunter's explicit decision on Stage 2. Current `main` HEAD recorded as `a38f9e851360ffa05fa84e6c8da20cdecee4381d`. No change to §1 (overarching objective), §4 (fixed roadmap), or Stage 2 scope.
- **Why:** Stage 1 operating pack and dashboard were completed, independently reviewed, corrected, merged to `main`, and approved by Hunter and ChatGPT.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `a38f9e851360ffa05fa84e6c8da20cdecee4381d`.
- **Impact on remaining stages:** None. Stage 2 remains not authorised pending a separate, explicit Hunter decision.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 2 authorised and started**
- **What changed:** Status header and §10 updated to record Stage 2 — Close A-02 narrowly — as authorised and in progress, on a dedicated branch/worktree from `main` at `271255e926bf4dadcc611c3714783768eb9465b7`. No change to §1, §4, or Stage 2's own scope as fixed in §4.
- **Why:** Hunter authorised Stage 2 to reach one evidence-grounded decision on whether A-02 is suitable for supervised, context-bounded evidence and draft review.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `271255e926bf4dadcc611c3714783768eb9465b7`, clean working tree.
- **Impact on remaining stages:** None. Stage 3 remains not authorised pending Hunter's decision on the Stage 2 outcome.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 2 complete: A-02 kept blocked**
- **What changed:** Status header and §10 updated to record Stage 2 as complete. Hunter approved the decision packet's recommendation to keep A-02 blocked from real-material review (unpassed, inactive), with re-entry condition: (1) complete the M-009-required 16-case seeded evaluation, (2) independently score it against existing criteria, (3) a human records `evaluation_status`. Remaining holdout cases are supplementary, not mandatory. `ops/stage-2-close-a02-narrowly` merged into `main` by fast-forward. No change to §1, §4, or Stage 2's fixed scope.
- **Why:** Hunter's explicit decision on the Stage 2 decision packet.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `044f7a3c76694e55b66e50c9b7378053ccae4960`, clean working tree, fast-forward merge (no new commit).
- **Impact on remaining stages:** None. Stage 3 remains not authorised pending a separate, explicit Hunter decision.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 3 authorised and started**
- **What changed:** Status header and §10 updated to record Stage 3 — Build MFC Objective Orchestrator v0 — as authorised and in progress, on a dedicated branch/worktree from `main` at `36b7ac71b5ec536b14367bcdacae4f2874021bd3`. No change to §1, §4, or Stage 3's own scope as fixed in §4.
- **Why:** Hunter authorised Stage 3 to build the minimum usable Objective Orchestrator v0, per the fixed roadmap's Stage 3 definition.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `36b7ac71b5ec536b14367bcdacae4f2874021bd3` (working tree carried only a cosmetic `.obsidian/graph.json` interface-state change, not vault content — noted, not treated as blocking).
- **Impact on remaining stages:** None. Stage 4 remains not authorised pending Hunter's decision on the Stage 3 outcome.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 3 complete: A-04 approved for bounded controlled use**
- **What changed:** Status header and §10 updated to record Stage 3 as complete. Hunter approved A-04 (MFC Objective Orchestrator v0) for controlled internal use under M-010, `authorization_scope: internal-advisory-review`, bounded exactly to: internal advisory planning for one explicitly Hunter-approved roadmap stage at a time; manually supplied/named authoritative context only; defining deliverables, sequencing, budgets, review limits and decision gates; generating bounded downstream Claude task briefs; updating dashboard and exact resume state. A-04 may not retrieve context autonomously, execute downstream work, launch agents, approve/publish/implement anything, advance roadmap stages, or treat unavailable/unverified capabilities as operational. **Expiry: completion of Stage 5, or 25 October 2026, whichever occurs first.** `ops/stage-3-objective-orchestrator-v0` merged into `main` by fast-forward. No change to §1, §4, or Stage 3's fixed scope.
- **Why:** Hunter's explicit decision on the Stage 3 build, following one independent review and one correction pass.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `5ae781d69f57576a2194e2ac34561e5a5b053c67`, fast-forward merge (no new commit), working tree carrying only the known `.obsidian/graph.json` interface-state change.
- **Impact on remaining stages:** None. Stage 4 remains not authorised pending a separate, explicit Hunter decision.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 4 authorised and started**
- **What changed:** Status header and §10 updated to record Stage 4 — Build Knowledge and Authority Steward v0 — as authorised and in progress, on a dedicated branch/worktree from `main` at `c425f54807ac7fa78e70f38e74dfc51002835221`. No change to §1, §4, or Stage 4's own scope as fixed in §4.
- **Why:** Hunter authorised Stage 4 to build the minimum usable Knowledge and Authority Steward v0, per the fixed roadmap's Stage 4 definition.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `c425f54807ac7fa78e70f38e74dfc51002835221` (working tree carried only the known `.obsidian/graph.json` interface-state change, not vault content).
- **Impact on remaining stages:** None. Stage 5 remains not authorised pending Hunter's decision on the Stage 4 outcome.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 4 complete: A-05 approved for bounded controlled internal advisory use**
- **What changed:** Status header and §10 updated to record Stage 4 as complete. Hunter approved A-05 (MFC Knowledge and Authority Steward v0) for controlled internal advisory use under M-011, `authorization_scope: internal-advisory-review`, bounded exactly to: classifying explicitly supplied/named records by status and authority; identifying unresolved conflicts and missing context; preparing bounded, traceable context packets; stating what may/may not be treated as authoritative; escalating genuine authority decisions to Hunter. A-05 may not resolve conflicts, approve/change MFC positions, alter source/knowledge/decision/conflict records, conduct research, retrieve broadly or autonomously, or publish/implement/advance roadmap stages. **Expiry: completion of Stage 6, or 25 October 2026, whichever occurs first.** `ops/stage-4-knowledge-authority-steward-v0` merged into `main` by fast-forward. No change to §1, §4, or Stage 4's fixed scope.
- **Why:** Hunter's explicit decision on the Stage 4 build, following one independent review and one correction pass.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `5a71f3ef4f5e1ded9ef87e8abe5d4782677de5dd`, fast-forward merge (no new commit), working tree carrying only the known `.obsidian/graph.json` interface-state change.
- **Impact on remaining stages:** None. Stage 5 remains not authorised pending a separate, explicit Hunter decision.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 5 authorised and started**
- **What changed:** Status header and §10 updated to record Stage 5 — Build and test Evidence Discovery and Synthesis v0 — as authorised and in progress, on a dedicated branch/worktree from `main` at `a8e85cc20f944261feb14e50d7539ce92e66de29`. No change to §1, §4, or Stage 5's own scope as fixed in §4.
- **Why:** Hunter authorised Stage 5 to build and test the minimum reusable Evidence Discovery and Synthesis v0 capability, per the fixed roadmap's Stage 5 definition.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `a8e85cc20f944261feb14e50d7539ce92e66de29` (working tree carried only the known `.obsidian/graph.json` interface-state change, not vault content).
- **Impact on remaining stages:** None. Stage 6 remains not authorised pending Hunter's decision on the Stage 5 outcome.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 5 complete: A-06 approved for bounded controlled evidence discovery**
- **What changed:** Status header and §10 updated to record Stage 5 as complete. Hunter approved A-06 (MFC Evidence Discovery and Synthesis v0) for controlled internal evidence discovery and provisional synthesis under M-012, `authorization_scope: internal-advisory-review`, bounded exactly to: framing bounded research questions; discovering adjacent evidence lenses; searching and logging evidence reproducibly; assessing source quality and applicability; identifying contradictions, limitations and missing lenses; producing provisional, traceable synthesis; separating evidence findings from proposed MFC implications. Mandatory: label every material claim full-text verified/summary-derived/unverified; stop and escalate when a load-bearing source is inaccessible; exclude unverified quantitative claims from decision-grade outputs; prevent provisional synthesis from being treated as authoritative MFC knowledge. A-06 may not approve claims, publish findings, modify authoritative records, or treat summaries as sufficient evidence. **Expiry: completion of Stage 8, or 25 October 2026, whichever occurs first.** `ops/stage-5-evidence-discovery-synthesis-v0` merged into `main` by fast-forward. No change to §1, §4, or Stage 5's fixed scope.
- **Why:** Hunter's explicit decision on the Stage 5 build and test, following one independent review, one correction pass, and one Hunter-authorised full-text validation pass.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `d6bbcf9d0411f12c3453d417ed3f0a7bb6078b85`, fast-forward merge (no new commit), working tree carrying only the known `.obsidian/graph.json` interface-state change.
- **Impact on remaining stages:** None. Stage 6 remains not authorised pending a separate, explicit Hunter decision.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 6 authorised and started**
- **What changed:** Status header and §10 updated to record Stage 6 — Approve Workshop Intelligence Programme charter — as authorised and in progress, on a dedicated branch/worktree from `main` at `3f97d7c9fef5acffc8859d790de19bd41871dc8d`. No change to §1, §4, or Stage 6's own scope as fixed in §4.
- **Why:** Hunter authorised Stage 6 to prepare (not approve) a decision-ready Workshop Intelligence Programme charter, per the fixed roadmap's Stage 6 definition.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `3f97d7c9fef5acffc8859d790de19bd41871dc8d` (working tree carried only the known `.obsidian/graph.json` interface-state change, not vault content).
- **Impact on remaining stages:** None. Stage 7 remains not authorised pending Hunter's decision on the Stage 6 outcome.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 6 complete: Workshop Intelligence Programme charter approved**
- **What changed:** Status header and §10 updated to record Stage 6 as complete. Hunter approved the charter under three decisions: (1) primary design audience is general adults — no clinical/specialist/workplace-specific context assumed, delivery setting deferred to product/pilot stages, non-workplace not a permanent exclusion; (2) K-04 Position 1 usable only as a provisional internal Stage 7 design assumption — C-13 remains open and unresolved, no public claim or authoritative knowledge update may rely on it without the required human decision; (3) specialist capabilities built one at a time, immediately before the roadmap stage that demonstrably requires each. `ops/stage-6-workshop-intelligence-charter` merged into `main` by fast-forward. No change to §1, §4, or Stage 6's fixed scope. No authoritative MFC record altered; C-13/C-01/C-14 remain open.
- **Why:** Hunter's explicit decision on the Stage 6 charter, following one independent review and one correction pass.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `ab74afc0afb6d845dd38a6b84c3ed9f015ca3111`, fast-forward merge (no new commit), working tree carrying only the known `.obsidian/graph.json` interface-state change.
- **Impact on remaining stages:** None. Stage 7 remains not authorised pending a separate, explicit Hunter decision.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 7 authorised and started**
- **What changed:** Status header and §10 updated to record Stage 7 — Establish MFC teaching and outcomes spine — as authorised and in progress, on a dedicated branch/worktree from `main` at `5cf9bb4ac922bc94c6dc2d4d8f6716c4bfd79611`. No change to §1, §4, or Stage 7's own scope as fixed in §4.
- **Why:** Hunter authorised Stage 7 to establish the teaching and outcomes spine, per the fixed roadmap's Stage 7 definition and the approved Stage 6 charter.
- **Supporting evidence:** Verified repository state — branch `main`, HEAD `5cf9bb4ac922bc94c6dc2d4d8f6716c4bfd79611` (working tree carried only the known `.obsidian/graph.json` interface-state change, not vault content).
- **Impact on remaining stages:** None. Stage 8 remains not authorised pending Hunter's decision on the Stage 7 outcome.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Stage 7 complete: teaching and outcomes spine approved**
- **What changed:** Status header and §10 updated to record Stage 7 as complete. Hunter approved the spine and Hunter decision packet under two decisions: (1) no prescribed post-workshop reinforcement mechanism — Stage 8 must examine transfer/reinforcement evidence, Stage 9 must determine the product/follow-up/reinforcement approach, and the existing 3–4 week evaluation follow-up is measurement, not automatically a reinforcement intervention; (2) the "one attempted application" transfer threshold is retained, explicitly as a provisional evaluation threshold only — not a Mental Rep pass/fail definition; the outcome of an attempt does not determine whether it counts; a relevant moment may be caught before, during, or after it occurs; one attempt does not establish competence, guaranteed benefit, habit formation, or durable behaviour change; Stage 8 must validate or revise the threshold and timeframe. **C-13 remains open and unresolved** — the current definition (K-04 Position 1) continues only as the previously approved, caveated internal design assumption; C-13 may close only when its own recorded resolution gate (Hunter's confirmation plus correction of the Committee Business Plan, Commercial Model, and Management Business and Operating Plan) is explicitly verified — not by inference from this or any other approval. `ops/stage-7-teaching-outcomes-spine` merged into `main` by fast-forward (HEAD `0c16d98`). No specialist capability was required for Stage 7. No authoritative MFC record altered.
- **Why:** Hunter's explicit decision on the Stage 7 spine and decision packet, following the earlier independent review/correction pass and the bounded source-registration, authority-reconciliation, and authority-correction tasks.
- **Supporting evidence:** Verified repository state before merge — `main` HEAD `c71ff19cd15d92d2865736636fc016b8ebd28b92`, Stage 7 branch HEAD `0c16d9884b574ef32a468e29cf8372b6dca59479`, clean fast-forward confirmed, working tree carrying only the known `.obsidian/graph.json` interface-state change.
- **Impact on remaining stages:** None to Stage 9+ scope. Stage 8 remains not authorised pending a separate, explicit Hunter decision.
- **Hunter's approval:** Approved 27 July 2026.
- **Date:** 2026-07-27.

**2026-07-27 — Inter-stage change control: roadmap amendment PROPOSED (not approved, not merged)**
- **What changed:** §4 (Stage 8 entry gate; Stage 10–11 pilot-readiness controls), §5 (Project Learning and Memory Steward just-in-time timing), and §6 (Hunter decision-explanation standard) each gained one clearly marked `[APPROVED, 2026-07-27 by Hunter — operational]` addition. No stage was added, renumbered, or redesigned; no existing stage purpose changed; no wording elsewhere altered.
- **Why:** Stage 7 initially proceeded without several current Drive-controlled workshop, measurement and framework records because they were absent from the local vault. This exposed a gap in the roadmap's own controls: no explicit Stage 8 entry gate for source readiness, no standard for how Hunter decisions must be explained, no recorded pilot-readiness controls for Stages 10–11, and no explicit just-in-time rule for when the Project Learning and Memory Steward should be built.
- **Issue classifications:** Stage 8 source readiness — must resolve before Stage 8 research begins (a bounded source-readiness check, not performed by this task). Decision-explanation standard — applies from the next Hunter decision onward. Pilot-governance controls — recorded now, resolved during Stages 10–11 (no materials built now). Learning and Memory Steward — a future just-in-time dependency, not required for Stage 8 entry.
- **Supporting evidence:** Verified repository state before this task — `main` HEAD `060b8adbe2cad2419660e40566595100f1ffc320`, Stages 0–7 complete and closed, Stage 8 unauthorised, control records consistent; prepared on branch `ops/pre-stage8-roadmap-control-amendment`, worktree `/Users/hunterkaram/Documents/MFC-pre-stage8-roadmap-control-amendment`, isolated from `main`.
- **Impact on remaining stages:** None yet — this amendment is **proposed only**. It does not authorise Stage 8, does not perform the source-readiness check, does not reopen Stage 6/7, does not resolve C-13, and does not build any capability or pilot-governance material. Blocking sequence once approved: amendment approval → bounded Stage 8 source-readiness check → Hunter's separate decision on Stage 8 research.
- **Hunter's approval:** **Preparation only** authorised 27 July 2026. Final wording, merge, and Stage 8 authorisation remain **not approved** — awaiting explicit Hunter and ChatGPT review.
- **Date:** 2026-07-27.

**2026-07-27 — Inter-stage change control: roadmap amendment APPROVED and merged**
- **What changed:** All four `[PROPOSED …]` tags in §4, §5, and §6 changed to `[APPROVED, 2026-07-27 by Hunter — operational]`. The Stage 8 entry gate's explanatory note and the status header corrected per Hunter's approval condition: the bounded Stage 8 source-readiness check is now the next required **procedural** action once this amendment is merged — it does **not** require a separate Hunter authorisation decision to begin. Hunter's next genuine decision occurs **after** that check, deciding whether the verified state supports authorising Stage 8 broad evidence discovery. No other wording, stage definition, or scope changed. `ops/pre-stage8-roadmap-control-amendment` merged into `main` by fast-forward.
- **Why:** Hunter reviewed and approved the proposed amendment, subject to this one correction to the blocking-sequence description, so the roadmap accurately reflects that the source-readiness check is procedural, not a second authorisation gate.
- **Issue classifications (unchanged from proposal):** Stage 8 source readiness — resolves via the now-next bounded procedural check, before Stage 8 research. Decision-explanation standard — applies from the next Hunter decision onward. Pilot-governance controls — recorded now, resolved during Stages 10–11. Learning and Memory Steward — a future just-in-time dependency, not required for Stage 8 entry.
- **Supporting evidence:** Verified repository state before merge — `main` HEAD `060b8adbe2cad2419660e40566595100f1ffc320`, amendment branch HEAD as committed on `ops/pre-stage8-roadmap-control-amendment`, clean fast-forward confirmed, working tree carrying only the known `.obsidian/graph.json` interface-state change.
- **Impact on remaining stages:** None to stage scope or sequencing. Stage 8 remains not authorised. This task does not perform the source-readiness check and does not begin Stage 8 research.
- **Hunter's approval:** Approved 27 July 2026, subject to the one correction above (source-readiness check is procedural, not a separate authorisation decision).
- **Date:** 2026-07-27.

**2026-07-28 — Stage 8 research agenda APPROVED (agenda-only; Stage 8 itself remains unauthorised)**
- **What changed:** Hunter approved a final nine-question Stage 8 research agenda (F1–F9) and its execution order, superseding the approved Stage 8 handoff's original ten-question list for operational Stage 8 execution. No stage was reopened, redesigned, or renumbered; no completed stage's status changed.
- **Why:** the original ten questions could not be authorised unchanged — a research-agenda quality gate found neutrality defects, an incorrect stage allocation (a Measurement Blueprint alignment check misframed as evidence research), missing measurement-validity coverage, unclear question boundaries, and duplication risk. The revised agenda corrects these while reusing, not duplicating, MFC's existing Learning Science Evidence Library.
- **Impact on remaining stages:** if Stage 8 is subsequently authorised, it will run as a nine-run bounded programme (F1–F9, in the approved execution order) rather than the original ten. No completed stage is reopened. Stage 8 research remains unauthorised.
- **Supporting evidence:** [[60-projects/workshop-evidence-informed-adult/03-evidence-discovery/01-stage-8-research-agenda-quality-gate|60-projects/workshop-evidence-informed-adult/03-evidence-discovery/01-stage-8-research-agenda-quality-gate.md]] (approved), [[60-projects/workshop-evidence-informed-adult/03-evidence-discovery/02-proposed-stage-8-execution-register|02-proposed-stage-8-execution-register.md]] (approved), [[60-projects/workshop-evidence-informed-adult/03-evidence-discovery/03-stage-8-hunter-decision-packet|03-stage-8-hunter-decision-packet.md]] (decided); supersession notice added to [[60-projects/workshop-evidence-informed-adult/02-outcomes-spine/04-stage-8-handoff|02-outcomes-spine/04-stage-8-handoff.md]]. `ops/stage8-research-agenda-quality-gate` merged into `main` by fast-forward.
- **Hunter's approval:** Approved 27–28 July 2026.
- **Date:** 2026-07-28.

**2026-07-28 — Stage 8 authorised, executed, and closed complete; Stage 9 authorised (not started)**
- **What changed:** Following the agenda-only approval recorded immediately above, Hunter separately authorised Stage 8 — Run broad evidence discovery (the bounded nine-question F1–F9 programme, execution order `F3→F2→F9→F4→F1→F5→F8→F6→F7`, under M-012/A-06). All nine question-level runs completed and merged into `main`, six with one bounded evidence-interpretation correction pass each (F1, F4, F5, F6, F7, F8) after independent verification revealed overstatement, none reopening Stage 7. One bounded integrated Stage 8 synthesis (`70-capability/performance/runs/stage8-integrated-synthesis-2026-07-28/`) then consolidated all nine runs' final corrected state, applying a six-category evidence classification scheme, an evidence-sufficiency assessment per question, a consolidated Missing Lenses register, and an eleven-decision Stage 9 agenda (a tenth was later split to eleven by correction, below) — merged, with one bounded terminology correction (qualifying "at least one reported attempt" as provisional, not a validated threshold). One independent review of that merged package (`70-capability/performance/runs/stage8-independent-review-2026-07-28/`) returned verdict `PASS WITH BOUNDED CORRECTIONS — ONE CORRECTION PASS REQUIRED` (22 claims sampled, 0 critical issues, 3 major issues M1–M3, 2 minor issues) — merged. One authorised correction pass (`70-capability/performance/runs/stage8-integrated-review-corrections-2026-07-28/`) then resolved M1 (added Decision 11, "consistency and cultural/contextual fit," owning a previously-unassigned design tension), M2 (added "a validated measurement or evaluation architecture" to the consolidated prohibited-claims lists, per F9's own boundaries), and M3 (corrected the Missing Lenses register's stated count to the transparently reconciled 50 items across 11 categories) — merged, leaving 0 critical and 0 major issues, with the 2 minor issues explicitly carried forward, uncorrected. **Hunter then approved, 28 July 2026: close Stage 8 as complete, and authorise Stage 9 — Design Requirements and Product Strategy — subject to all existing evidence, authority, claims, safeguarding and C-13 boundaries**, recorded in decision record `D-0002` ([[30-decisions/D-0002-stage8-closure-stage9-authorisation|30-decisions/D-0002-stage8-closure-stage9-authorisation.md]]). Stage 9 is recorded `AUTHORISED — NOT STARTED`, not in progress. M-012 (the mandate authorising A-06's Stage 8 work) is now `expired`, per its own recorded expiry condition ("completion of Stage 8, or 25 October 2026, whichever occurs first") — Stage 8's completion is the earlier trigger; see [[50-authority/mandates/M-012-mfc-evidence-discovery-synthesis-v0|50-authority/mandates/M-012-mfc-evidence-discovery-synthesis-v0.md]] and its mandate-register row. A-06's own capability status is unchanged and governed separately by the agent register; it is not deactivated by this expiry.
- **Why:** Hunter's explicit decision, following the complete evidence-discovery-and-assurance chain above: nine bounded evidence runs, one integration, one independent review, and one correction pass, with no critical or major issue remaining and no requirement found anywhere to reopen Stage 7.
- **Closure basis:** 0 critical issues; 0 major issues; 2 minor issues (`RECORD AND CONTINUE`, not corrected: F2/F9's partially shared-source "converging" language; F9's non-load-bearing pre-F5 booster figure); Stage 7 integrity intact (general-adult audience, five knowledge outcomes, three skill outcomes, transfer outcome, six essential-content items all unchanged); no Stage 8 evidence question classified as blocking Stage 9 itself (F7's safeguarding-governance component blocks pilot-ready approval and participant-facing delivery specifically, not Stage 9); the unresolved S18/E4 implementation-intentions contradiction and C-13's existing authority boundary both preserved, neither resolved by this transition.
- **What Stage 8 closure means:** Stage 8 provides a principle-level, boundary-labelled, decision-support evidence base, sufficient to inform bounded Stage 9 design decisions. It does not validate workshop effectiveness, a final session design, real-world transfer, lasting change, habit formation, wellbeing improvement, a follow-up mechanism, Radar, a facilitator standard, a measurement architecture, accessibility/inclusion guarantees, participant safety, or causal impact.
- **Stage 9 authority (per D-0002):** Stage 9 may compare evidence-bounded design options, establish product/implementation requirements, and prepare consequential Hunter/governance decisions, preserving Stage 7 unless an authorised change process is triggered. Stage 9 may not make public evidence claims, declare pilot readiness, bypass C-13, approve safeguarding governance, begin participant-facing delivery, silently alter Stage 7, treat a proposed requirement as a validated finding, or advance automatically to Stage 10.
- **Supporting evidence:** Verified `main` HEAD `3a649ba1952091e51cc2196da745a31c27c37721` before this task; all nine F1–F9 run directories, the integrated-synthesis directory, the independent-review directory, and the correction-pass directory all present and merged under `70-capability/performance/runs/`; [[90-meta/Current State and Next Action|90-meta/Current State and Next Action.md]] and [[90-meta/operating-pack/05-dashboard|90-meta/operating-pack/05-dashboard.md]] in full agreement with this record. Prepared on branch `ops/stage8-close-authorise-stage9`, worktree `/Users/hunterkaram/Documents/MFC-stage8-close-authorise-stage9`, isolated from `main`.
- **Impact on remaining stages:** Stage 9 may now be initiated via a separate, explicit, bounded task selecting one decision from the approved eleven-decision Stage 9 agenda — not executed by this entry. No completed stage is reopened. Stage 7 remains closed and unaltered. C-13, the S18/E4 contradiction, the two minor issues, and the mandatory safeguarding gate all remain exactly as recorded, unresolved, carried forward.
- **Hunter's approval:** Approved 28 July 2026 (Stage 8 authorisation, execution oversight throughout, and this closure/Stage 9 authorisation decision).
- **Date:** 2026-07-28.

**2026-07-28 — Stage 9 begun; Decision 1 (session content structure and sequencing) underway**
- **What changed:** Hunter authorised: "Merge the completed Stage 9 initiation brief, begin Stage 9, and prepare Decision 1 — Session Content Structure and Sequencing — to a reviewed and decision-ready state." The Stage 9 initiation brief ([[60-projects/workshop-evidence-informed-adult/04-design-requirements/00-stage9-initiation-brief|60-projects/workshop-evidence-informed-adult/04-design-requirements/00-stage9-initiation-brief.md]]) was merged into `main`. Stage 9 is now recorded `IN PROGRESS — DECISION 1 UNDERWAY` (not "not started"). Work on Decision 1 proceeds on branch `ops/stage9-d1-session-content-structure-sequencing`, worktree `/Users/hunterkaram/Documents/MFC-stage9-d1-session-content-structure-sequencing`, not merged. No other Stage 9 decision has begun.
- **Why:** the initiation brief (prepared and reviewed under the prior task) identified Decision 1 as the unambiguous first Stage 9 decision, and Hunter authorised proceeding to prepare it to a decision-ready state — a bounded product-strategy task, not a final approval.
- **Scope of this authorisation:** Hunter's authorisation does not approve any Decision 1 option, a final workshop structure, detailed session content, exercises, participant- or facilitator-facing materials, Radar, reinforcement/follow-up, measurement architecture, safeguarding governance, Stage 10 advancement, or pilot readiness. Hunter retains final Decision 1 approval, to be recorded separately once the reviewed and corrected Decision 1 package is presented.
- **Supporting evidence:** Verified `main` HEAD `278cf1f7c94f18cce267a338cca97d09fbdbd4db` before branching (the Stage 9 initiation brief merge commit); Decision 1 package prepared on the branch above, including a decision frame, evidence/design constraints, up to three structural options, a comparison and recommendation, a provisional session architecture (labelled provisional), a downstream dependency map, claims/authority boundaries, a Hunter decision brief, one independent review, and — if required — one bounded correction pass.
- **Impact on remaining stages:** None to Stage 7, Stage 8, or Stage 10+ scope or definitions. Decision 2 through 11 remain unstarted. Stage 10 remains unauthorised. C-13, the safeguarding gate, and Stage 7's approved outcomes and essential content are all unaffected.
- **Hunter's approval:** Authorised 28 July 2026 to prepare Decision 1 to a decision-ready state; **final approval of the recommended Decision 1 option remains a separate, later, explicit Hunter decision, not made by this entry.**
- **Date:** 2026-07-28.

**2026-07-28 — Stage 9 Decision 1 approved (session content structure and sequencing)**
- **What changed:** Hunter approved: "Approve Option 2 — Segmented, simple-to-compound sequencing within the session — as the provisional Stage 9 session content structure and sequencing requirement, subject to the stated evidence, authority, safeguarding and later-decision boundaries." Recorded in decision record `D-0003` ([[30-decisions/D-0003-stage9-decision1-session-structure-sequencing|30-decisions/D-0003-stage9-decision1-session-structure-sequencing.md]]). The Decision 1 branch (`ops/stage9-d1-session-content-structure-sequencing`) was merged into `main` by fast-forward. The approved provisional architecture is the five-phase sequence: Orientation → Skills → Mechanism → Revisiting/Connecting → Application. Stage 9 status changes from `IN PROGRESS — DECISION 1 UNDERWAY` to `IN PROGRESS — DECISION 1 APPROVED; DECISION 2 NOT STARTED`.
- **Rationale:** Option 2 was recommended at Moderate confidence, applying F3's best-supported content-scope principle (segment/sequence simple-to-compound) without Option 3's dependency on undecided Decision 4, and without Option 1's highest cognitive-load-concentration risk. One independent review (`PASS WITH BOUNDED CORRECTIONS`, 0 critical, 2 major, 4 minor) and one authorised correction pass (resolving both major findings) preceded this approval — 0 critical and 0 major issues remain; 4 minor issues carried forward, `RECORD AND CONTINUE`, uncorrected.
- **Effect on downstream decisions:** Decisions 2, 4, 6, 7, 10, and 11 may use the approved provisional architecture as a controlled starting assumption, retaining full authority over their own questions (per `06-downstream-dependency-map.md`). No later decision may treat Option 2 as validated evidence.
- **Evidence and authority boundaries preserved:** Stage 7's audience, five knowledge outcomes, three skill outcomes, one transfer outcome, and six essential-content items are unchanged. C-13, C-20, C-22, and C-23 remain unresolved, at their existing boundaries, untouched. The mandatory pre-pilot safeguarding gate (`MUST RESOLVE BEFORE PILOT-READY APPROVAL AND BEFORE ANY PARTICIPANT-FACING PILOT DELIVERY`) is unchanged — this approval does not satisfy it, and participant-facing delivery remains prohibited until it is resolved by Hunter and the appropriate MFC governance authority. Option 2 is not validated, not proven effective, and not proven to produce transfer, habit, benefit, or durable change.
- **Supporting evidence:** Verified `main` HEAD `278cf1f7c94f18cce267a338cca97d09fbdbd4db` before merge; Decision 1 branch HEAD `70ddd8d3485067de71d799965b53f76f03c4ef07`, clean, fast-forward-eligible, containing all 11 Decision 1 artefacts under `60-projects/workshop-evidence-informed-adult/04-design-requirements/decision-01-session-content-structure-and-sequencing/`.
- **Impact on remaining stages:** Stage 9 remains `IN PROGRESS`, not complete. Decision 2 has not begun. No change to Stage 7, Stage 8, or Stage 10+ definitions.
- **Hunter's approval:** Approved 28 July 2026.
- **Date:** 2026-07-28.

**2026-07-28 — Stage 9 Decision 2 approved (in-session practice, feedback and retrieval design)**
- **What changed:** Hunter approved: "Approve Option 1 — Verified-core minimum — as the provisional Stage 9 Decision 2 in-session practice, feedback and retrieval requirement." Recorded in decision record `D-0004` ([[30-decisions/D-0004-stage9-decision2-practice-feedback-retrieval|30-decisions/D-0004-stage9-decision2-practice-feedback-retrieval.md]]). The Decision 2 branch (`ops/stage9-decision2-practice-feedback-retrieval`) was merged into `main` by fast-forward. Approved requirement: explanatory/elaborated feedback content (E11, full-text verified) + one recall-based retrieval element (E1, summary-derived) — no unverified worked-example mechanism, no productive-failure mechanism, no evidence-prescribed feedback timing. Stage 9 status changes from `IN PROGRESS — DECISION 1 APPROVED; DECISION 2 NOT STARTED` to `IN PROGRESS — DECISION 1 APPROVED; DECISION 2 APPROVED; DECISION 3 NOT STARTED`.
- **Rationale:** Option 1 was recommended and approved at Moderate confidence as the only option built entirely from mechanisms F4 verifies or summary-derives, with zero reliance on an unverified mechanism, operating cleanly within Decision 1's fixed architecture. One independent review (`PASS`, 0 critical, 0 major, 2 minor, 1 future-improvement) preceded this approval; no correction pass was required.
- **Required clarifications recorded in D-0004:** feedback timing is an adaptable Stage 10 material-design choice, not evidence-prescribed (F4's own mixed timing finding — no significant timing×learning-level interaction); immediate feedback must not be presented as evidence-required; Decision 2's mechanisms interact with Decisions 4, 6, 7, 9, and 10 without Option 1's own validity being contingent on any of them; the "no material additional safeguarding interaction" judgment is recorded explicitly as an MFC design inference, not a verified evidence finding.
- **Effect on downstream decisions:** Decisions 4, 6, 7, 9, and 10 may use the approved mechanisms as a controlled starting assumption where relevant, retaining full authority over their own questions (per `06-downstream-dependency-map.md`). No later decision may treat Option 1 as validated evidence.
- **Evidence and authority boundaries preserved:** Decision 1's architecture and D-0003 unchanged. Stage 7's audience, outcomes, and essential content unchanged. C-13, C-20, C-22, C-23 remain unresolved, untouched. The mandatory pre-pilot safeguarding gate is unchanged — this approval does not satisfy it. Option 1 is not validated, not proven effective, and not proven to produce transfer, habit, benefit, or durable change.
- **Supporting evidence:** Verified `main` HEAD `f7f4b325f4d012fc55cf7eb4f9a6f801dffe69be` before merge; Decision 2 branch HEAD `04ad251f1d135c2277584fb75969f4d1707749ae`, clean, fast-forward-eligible, containing all 10 Decision 2 artefacts under `60-projects/workshop-evidence-informed-adult/04-design-requirements/decision-02-in-session-practice-feedback-retrieval/`. The approval record was independently cross-checked against every element of Hunter's stated decision before this entry was written.
- **Impact on remaining stages:** Stage 9 remains `IN PROGRESS`, not complete. Decision 3 has not begun. No change to Stage 7, Stage 8, Decision 1, or Stage 10+ definitions.
- **Hunter's approval:** Approved 28 July 2026.
- **Date:** 2026-07-28.

**2026-07-29 — Stage 9 Decision 3 approved (transfer-support and contextual framing)**
- **What changed:** Hunter approved: "Approve Option 1 — Minimum context-neutral framing — for Stage 9 Decision 3." Recorded in decision record `D-0005` ([[30-decisions/D-0005-stage9-decision3-transfer-support-contextual-framing|30-decisions/D-0005-stage9-decision3-transfer-support-contextual-framing.md]]). The Decision 3 branch (`ops/stage9-decision3-transfer-support-contextual-framing`) was merged into `main` by fast-forward. Approved requirement: the session communicates that it does not assume participants have workplace structures, an ongoing host relationship, organisational support, accountability systems, or continuing contact available to support transfer — communicating simply that circumstances, environments, and available support may differ. Stage 9 status changes from `IN PROGRESS — DECISION 1 APPROVED; DECISION 2 APPROVED; DECISION 3 NOT STARTED` to `IN PROGRESS — DECISIONS 1–3 APPROVED; DECISION 4 NOT STARTED`.
- **Rationale:** Option 1 was recommended and approved at Moderate confidence as the option requiring no undecided classification infrastructure (unlike Option 2) while still actively disclosing MFC's position on context-dependence (unlike Option 3's silence). One independent review (`PASS WITH BOUNDED CORRECTIONS`, 0 critical, 2 major, 2 minor) and one correction pass (resolving both major findings) preceded this approval; one independent line-by-line verification of the decision record against Hunter's exact approval text found no material mismatch.
- **Required clarifications recorded in D-0005:** F1's workplace findings (transfer climate r=.27, supervisor/peer support r=.21) are associative, not causal; their application outside workplace training remains uncertain; MFC's future delivery setting remains unresolved (Stage 7's own unresolved item, untouched); classifying MFC's content as an "open" skill type is an evidence-supported MFC design inference, not a tested finding; Decisions 4, 8, 9, and 11 retain their own authority and are not pre-empted.
- **Effect on downstream decisions:** Decisions 4, 6, 7, 8, 9, and 11 may use the approved framing as a controlled starting assumption where relevant, retaining full authority over their own questions (per `06-downstream-dependency-map.md`). No later decision may treat Option 1 as validated evidence.
- **Evidence and authority boundaries preserved:** Decision 1's architecture, Decision 2's mechanisms, and Stage 7's audience/outcomes/essential content remain unchanged. Stage 7's delivery-setting question remains unresolved. C-13, C-20, C-22, C-23 remain unresolved, untouched. The mandatory pre-pilot safeguarding gate is unchanged — this approval does not satisfy it. Option 1 is not validated, not proven effective, and does not claim transfer cannot occur without workplace or host structures.
- **Supporting evidence:** Verified `main` HEAD `af6d7a9f6fe153314a4011a4d3cb05628e1f4b3a` before merge; Decision 3 branch HEAD `68b3a7448ed6d347cc7e6e75f647247fd146993c`, clean, fast-forward-eligible, containing all 11 Decision 3 artefacts under `60-projects/workshop-evidence-informed-adult/04-design-requirements/decision-03-transfer-support-and-contextual-framing/`. The approval record was independently verified line-by-line against every element of Hunter's stated decision before this entry was written.
- **Impact on remaining stages:** Stage 9 remains `IN PROGRESS`, not complete. Decision 4 has not begun. No change to Stage 7, Stage 8, Decisions 1–2, or Stage 10+ definitions.
- **Hunter's approval:** Approved 29 July 2026.
- **Date:** 2026-07-29.

**2026-07-29 — Controlled Automation V1 architecture APPROVED; Phase 0 task preparation authorised, not started (parallel system workstream, not a roadmap stage)**
- **What changed:** Hunter Karam approved: "Approve the Controlled Automation V1 architecture and minimum phased build sequence, based on a Pattern B file-backed controlled orchestrator built on a Pattern A deterministic-verification foundation, and authorise preparation of the first bounded Phase 0 task only." Recorded in `D-0007` ([[30-decisions/D-0007-controlled-automation-v1-architecture-approval|30-decisions/D-0007-controlled-automation-v1-architecture-approval.md]]). The completed, independently reviewed, twice-reconciled architecture package (`D-0006`, `90-meta/controlled-automation-v1/`, 13 files) was transferred onto branch `ops/controlled-automation-v1-architecture-approval`, based on `main` at `ed394a1`, and **merged into `main` by fast-forward**. **Approved:** the V1 definition; manual objective initiation; Pattern B on a Pattern A foundation; Markdown with structured frontmatter; persistent objective/project/task/capability/mandate/approval/review/event/resume records; project/branch/worktree/context-packet isolation; permanent human gates; capability/mandate validation; one review and one correction maximum; the six-phase build sequence. **Authorised:** preparation of the Phase 0 task specification only — not its implementation, and not any later phase. **Not approved:** any implementation, unattended operation, automatic merges (beyond this one), capability activation, external integrations, sensitive-data access, or roadmap advancement.
- **Why:** the architecture reached decision-ready status through independent review (`PASS WITH BOUNDED CORRECTIONS`, 0 critical, 1 major corrected, 2 minor carried forward, 1 future-improvement carried forward), one reconciliation against `main`'s advance through Decision 3's approval, and one final integration against `main`'s further advance through Decision 4's initiation brief — all passing final integration verification (`PASS — FINAL INTEGRATION READY`, 18/18 checks) with no core-architecture change required at any stage.
- **Impact on remaining stages/workstreams:** None. Workshop Stage 9 status (Decisions 1–3 `APPROVED — COMPLETE`; Decision 4 initiation brief prepared, reviewed, corrected, execution not begun) is unaffected and untouched.
- **Hunter's approval:** Approved 2026-07-29, per `D-0007`. **Phase 0 task specification, its implementation, and every later phase remain separate, later, explicit Hunter decisions, not made by this entry.**
- **Date:** 2026-07-29.

**2026-07-29 — Stage 9 Decision 4 approved (post-session reinforcement/follow-up)**
- **What changed:** Hunter approved: "I approve Option 2 — Minimum low-burden reinforcement — for Stage 9 Decision 4." Recorded in decision record `D-0008` ([[30-decisions/D-0008-stage9-decision4-post-session-reinforcement-follow-up|30-decisions/D-0008-stage9-decision4-post-session-reinforcement-follow-up.md]]). The Decision 4 options package (prepared and reviewed on branch `ops/stage9-decision4-post-session-reinforcement-follow-up`, HEAD `28408db`) was faithfully reapplied by cherry-pick onto a fresh closure branch, `ops/stage9-decision4-closure`, created from current `main` (HEAD `707a3b7`, which had meanwhile advanced through the unrelated Controlled Automation V1/`D-0007` entry above), after verifying the reapplied commit range contained only the authorised Decision 4 package and Stage 9 status updates, with no unrelated collision. Approved requirement: one participant-selected reminder/cue intended to support later recall, and one brief retrieval prompt at or near the existing 3–4 week evaluation contact. Stage 9 status changes from `IN PROGRESS — DECISIONS 1–3 APPROVED; DECISION 4 NOT STARTED` to `IN PROGRESS — DECISIONS 1–4 APPROVED; DECISION 5 NOT STARTED`.
- **Rationale:** Option 2 was recommended and approved as the lowest combination of unsupported-claim risk and undeliverable-commitment risk among the three prepared options, given F5's evidence that no mechanism examined is proven for MFC's own population/format, and that Option 3's optional host-facilitated layer depends on host capacity F5 found unaddressed and likely uncertain for a small charity host. One independent review of the options package (`PASS WITH BOUNDED CORRECTIONS`, 0 critical, 2 major, 3 minor, 1 future-improvement) and one correction pass (resolving both major findings — a fabricated F5-confidence attribution, and a comparison-table/option-set burden mismatch) preceded Hunter's approval; one independent line-by-line verification of `D-0008` against Hunter's exact approval text found no material mismatch, so no further correction was required.
- **Required clarification recorded in D-0008 — protecting the evaluation:** where the retrieval prompt uses the same contact as the 3–4 week evaluation, evaluation data must be collected and submitted first, and the reinforcement/retrieval prompt may only follow after that response is complete; the support prompt must not influence the outcomes being measured. Decision 10 retains authority over the exact measurement architecture, instruments, sequencing, and data handling — this approval establishes only the non-contamination principle.
- **Additional approval boundaries recorded in D-0008:** the 3–4 week point remains an initial-use/early-repetition assessment point, not a habit or maintenance checkpoint; the reminder/cue must not assume a Decision 5 Radar target count, tracking system, or cueing structure; the retrieval prompt is a single low-burden component, not an ongoing cadence; exact wording, format, channel, and delivery platform remain Stage 10 material-design questions; no continuing host relationship is required; no host-facilitated booster or peer-pairing system is approved; no specific mechanism or dose is validated; MFC may not claim this support improves real-world use, habit formation, automaticity, wellbeing, or durable behaviour change; Decisions 5, 9, and 10 retain full authority over their own questions; the safeguarding gate remains unchanged and unsatisfied; this approval does not establish pilot readiness.
- **Effect on downstream decisions:** Decision 5 (Radar/tracking) and Decision 10 (measurement architecture) may treat Option 2's two components as a controlled starting input where relevant, retaining full authority over their own questions (per `06-downstream-dependency-map.md`). Decision 9 must, before any pilot delivery, confirm no host-facilitated or distress-adjacent element requires its own resolution — none is approved here. No later decision may treat Option 2 as validated evidence.
- **Evidence and authority boundaries preserved:** Decision 1's architecture, Decision 2's mechanisms, Decision 3's framing, and Stage 7's audience/outcomes/essential content remain unchanged. Decision 5's Radar/tracking authority, Decision 9's safeguarding authority, and Decision 10's measurement authority are each fully preserved. C-13, C-20, C-22, C-23 remain unresolved, untouched. The mandatory pre-pilot safeguarding gate is unchanged — this approval does not satisfy it.
- **Supporting evidence:** Verified current `main` HEAD `707a3b77f45e0298ee6e44fd60fbc3cfd809e6a8` before reconciliation; confirmed the commit range `ed394a144b1d528ff008c4be759e9a46babc6c29..28408db` contained only the Decision 4 package and status-file updates (13 files, no unrelated change); Decision 4 closure branch `ops/stage9-decision4-closure` clean, fast-forward-eligible from that verified `main` HEAD. The approval record was independently verified line-by-line against every element of Hunter's stated decision before this entry was written.
- **Impact on remaining stages:** Stage 9 remains `IN PROGRESS`, not complete. Decision 5 has not begun. No change to Stage 7, Stage 8, Decisions 1–3, the parallel Controlled Automation V1 workstream, or Stage 10+ definitions.
- **Hunter's approval:** Approved 29 July 2026.
- **Date:** 2026-07-29.

**2026-07-29 — Controlled Automation V1: Phase 0 specification APPROVED; implementation task not yet authorised to begin (parallel system workstream, not a roadmap stage)**
- **What changed:** Hunter approved (1) the bounded Phase 0 implementation task specification exactly as proposed — structured control records, canonical field ownership, deterministic source-of-truth validation, subject to the stated migration/authority/rollback/human-decision boundaries; and (2) the decision register ([[30-decisions/README|30-decisions/README.md]]) becomes a generated derived view, matching Current State/dashboard's own treatment. Recorded in `D-0009` ([[30-decisions/D-0009-phase0-specification-approval-and-decision-register-ownership|30-decisions/D-0009-phase0-specification-approval-and-decision-register-ownership.md]]). The reviewed, corrected Phase 0 specification package (`90-meta/controlled-automation-v1/phase-0-structured-control-records/`, 11 files) was transferred onto branch `ops/controlled-automation-v1-phase0-specification-approval`, based on `main` at `5f1ed8f`, and **merged into `main`**. File `05`'s classification of the decision register updated from `DEFER` to `MIGRATE IN PHASE 0` (regeneration itself deferred to the implementation task's Batch A, not performed here).
- **Why:** the specification passed independent review (`PASS WITH BOUNDED CORRECTIONS`, 0 critical, 1 major corrected, 2 minor, 1 future-improvement) and the one open canonical-ownership question was the sole remaining decision-readiness gap.
- **What this does not authorise:** Phase 0 implementation (Batch A/Batch B execution) does not begin from this decision — a separate, later, explicit task, following this build's own established preparation-then-approval pattern, is still required before any record is created or modified.
- **Impact on remaining stages/workstreams:** None. Workshop Stage 9 status (Decisions 1–4 `APPROVED — COMPLETE`; Decision 5 initiation brief prepared, reviewed; execution not begun) is unaffected and untouched.
- **Hunter's approval:** Approved 2026-07-29, per `D-0009`. **Authorisation to begin Phase 0 implementation remains a separate, later, explicit decision, not made by this entry.**
- **Date:** 2026-07-29.

**2026-07-29 — Workshop Forms and Measurement Blueprint treatment rule adopted; Stage 9 Decision 5 initiation brief amended (procedural, not a decision or stage transition)**
- **What changed:** Hunter instructed that MFC's current `MFC Workshop Forms` and `MFC Measurement Blueprint` be treated, from this point forward, as **provisional operational inputs and testable current assumptions** for the remainder of Stage 9 and for Stage 10 — not final approved authority, and not to be ignored. A bounded amendment added a new §15 to the Stage 9 Decision 5 initiation brief ([[60-projects/workshop-evidence-informed-adult/04-design-requirements/06-stage9-decision5-initiation-brief|60-projects/workshop-evidence-informed-adult/04-design-requirements/06-stage9-decision5-initiation-brief.md]]) recording this treatment for Decision 5 specifically, amended the brief's own embedded execution prompt (now §16) to require every future Decision 5 option to be tested against the current forms/Blueprint assumptions and to record retain/revise/remove/add/defer effects rather than editing the live documents, and created a new **Forms Reconciliation Register** ([[60-projects/workshop-evidence-informed-adult/04-design-requirements/00-forms-reconciliation-register|60-projects/workshop-evidence-informed-adult/04-design-requirements/00-forms-reconciliation-register.md]]) seeded with 15 verified rows relevant to Decisions 1–5. The brief's one outstanding minor citation finding (Radar's Stage 7 essential-content row incorrectly attributed to Skill outcomes S2+S3+T1, when the spine's own table attributes only S2+T1) was corrected in the same pass.
- **Workshop-wide rule recorded (applies to Decisions 5–11 and Stage 10):** Decisions 5–11 and Stage 10 must consider the current `MFC Workshop Forms` and `MFC Measurement Blueprint` as provisional operational inputs, neither final authority nor to be ignored; live forms will not be repeatedly edited after every individual Stage 9 decision; the Forms Reconciliation Register will accumulate required changes across decisions as they are approved; **one controlled forms-and-measurement reconciliation must occur before pilot-readiness approval**, covering the Workshop Forms, the Measurement Blueprint, the follow-up workflow, the measurement dashboard, and relevant participant/host administration. This reconciliation requirement is additive to, and does not replace, the existing Stages 10–11 pilot-readiness controls adopted 2026-07-27.
- **Recognised-measures evidence resources registered:** two further Drive records — `MFC Evidence Bank Source — Debra Rapid Review Measures Table.docx` and `MFC Evidence & Measures Bank` — were confirmed not previously registered under a Drive ID anywhere in the vault (only a passing reference inside the Measurement Blueprint's own record) and were given minimum metadata/reference stubs ([[10-sources/PENDING-mfc-evidence-bank-source-debra-rapid-review-measures-table|10-sources/PENDING-mfc-evidence-bank-source-debra-rapid-review-measures-table.md]]; [[10-sources/PENDING-mfc-evidence-and-measures-bank|10-sources/PENDING-mfc-evidence-and-measures-bank.md]]) pending full ingestion. Both are classified as **evidence and recognised-measures reference sources** — provisional inputs for future measure discovery and comparison, reusable across this workshop and future MFC projects — and explicitly **not** the current operational measurement authority (which remains the Measurement Blueprint), not approved participant-facing forms, not permission to use any listed instrument, not evidence that a listed measure suits the Foundations Session, and not authority to change the Measurement Blueprint. Inclusion of a measure in either resource does not constitute approval or validation for MFC use. **Decision 10 must consult both when assessing constructs, established instruments, MFC-created items, measurement burden, evidence status, and gaps in available measures**; any future adoption, adaptation, rejection, or deferral of a specific measure must separately assess construct fit, population/age fit, intervention/timeframe fit, participant burden, scoring/interpretation, licensing/permissions, and privacy/safeguarding implications, and must record the outcome (adopted/adapted/rejected/deferred) with rationale and authority basis.
- **What this amendment does not do:** it does not execute Decision 5, prepare or compare Decision 5 options, select or recommend an option, edit the live Google Workshop Forms or Measurement Blueprint, perform a full forms audit, reopen Decisions 1–4 or `D-0008`, begin Decision 6, decide Decision 10's measurement architecture, conduct new evidence research, resolve safeguarding, or declare Stage 9 complete or pilot readiness.
- **Review:** one independent Sonnet Medium review of this amendment (scope: the amended brief's new §15/§15A and renumbered §16/§17, the new register, and the two new source stubs) — verdict `PASS`, 0 critical, 0 major, 2 minor (both in the register: inconsistent "retain" vs. "retain (provisionally)" wording across otherwise-equivalent rows; the register's summary scope line reads slightly narrower than two of its own rows, which name Decision 10 and a data-hygiene item respectively). No correction pass required (minor-only); both findings recorded, uncorrected.
- **Impact on remaining stages:** Stage 9 remains `IN PROGRESS — DECISIONS 1–4 APPROVED`; Decision 5 execution has not begun. No change to Stage 7, Stage 8, Decisions 1–4, `D-0008`, or the Controlled Automation V1/`D-0007` workstream.
- **Hunter's instruction:** given 2026-07-29.
- **Date:** 2026-07-29.

**2026-07-29 — Stage 9 Decision 5 approved (Radar / practice-target structure)**
- **What changed:** Hunter approved: "I approve a refined form of Option 2 — Three participant-selected Radar moments with cue-linked practical planning — for Stage 9 Decision 5," explicitly excluding the options package's own prepared Option 1. Recorded in decision record `D-0010` ([[30-decisions/D-0010-stage9-decision5-radar-practice-target-structure|30-decisions/D-0010-stage9-decision5-radar-practice-target-structure.md]]). The Decision 5 options package (prepared and reviewed on branch `ops/stage9-decision5-radar-practice-target-structure`, HEAD `b5435b4`) was closed on the same branch, since `main` had not advanced past the verified starting HEAD (`584db0e`) during preparation — no reconciliation was required. Approved structure: each participant identifies three personally meaningful real-life moments, and one possible practical next move or Mental Rep for each (`three meaningful moments → one possible next move for each`). Stage 9 status changes from `IN PROGRESS — DECISIONS 1–4 APPROVED; DECISION 5 NOT STARTED` to `IN PROGRESS — DECISIONS 1–5 APPROVED; DECISION 6 NOT STARTED`.
- **Rationale (recorded as an MFC product-design decision, not an evidence-established count):** one moment may be too narrow to represent the different areas of life participants want to strengthen; the workshop's prior education and guided reflection support a more informed selection than an unsupported website visitor could make; three moments provide breadth while remaining bounded and understandable; the structure aligns with MFC's current operational thinking; the initial pilot will test whether three feels manageable, relevant, memorable, and useful. One independent review of the options package (`PASS`, 0 critical, 0 major, 1 minor, 1 future-improvement, neither requiring correction) preceded Hunter's approval; one independent line-by-line verification of `D-0010` against Hunter's exact approval text found no material mismatch, so no further correction was required.
- **Practice and measurement boundaries recorded in `D-0010`:** the Radar is a personal map, not a three-part compliance task — participants are not required to practise all three moments equally, experience every moment, complete a formal log for each, meet a frequency target, demonstrate progress in all three, or treat the moments as fixed permanently; exact review/change/replacement instructions remain Stage 10 work. The design must not be reduced to one moment merely for measurement ease; Decision 10 retains full authority over the final measurement architecture; five example measurement possibilities were recorded explicitly as examples only, not approved instruments.
- **`D-0008` boundary:** Decision 4's approved requirement (one participant-selected reminder/cue; one retrieval prompt at the 3–4 week evaluation contact; evaluation-first sequencing; no validated mechanism/cadence claim) is preserved unchanged; Decision 4 approved one reminder/cue, not necessarily one per Radar moment — which of three possible reminder-design routes is used remains undecided, deferred to later design work.
- **Forms Reconciliation Register updated:** rows 16 and 18 (Options 1 and 3) marked not-selected/historical; row 17 (originally-prepared Option 2) marked superseded by the refined selection; rows 19–24 added, recording the refined structure's likely implications for the singular Form 2 Radar question, the singular intended-Mental-Rep question, intention recording, and the three follow-up questions (noticed opportunities, approximate count, Radar helpfulness) — exact wording, branching, scoring, and measurement treatment deferred to Decision 10 and Stage 10. The live Workshop Forms and Measurement Blueprint were not edited or marked as updated.
- **Website relationship recorded, not executed:** the three-moment Radar is intended to support a coherent product concept across the workshop and MFC's website, while explicitly not approving website copy, interaction design, or an assumption that both surfaces must operate identically — recorded as a downstream implication for a later, separate task.
- **Recognised-measures resources:** the existing treatment of the Debra Rapid Review Measures Table and the Evidence & Measures Bank as recognised-measures reference resources for Decision 10 is preserved unchanged; no measure was selected, assessed, or applied.
- **Evidence and authority boundaries preserved:** Decisions 1–4's approved requirements and Stage 7's audience/outcomes/essential content remain unchanged. Decision 6's facilitator-competency authority, Decision 9's safeguarding authority, and Decision 10's measurement authority are each fully preserved. C-13, C-20, C-22, C-23 remain unresolved, untouched. The mandatory pre-pilot safeguarding gate is unchanged — this approval does not satisfy it.
- **Supporting evidence:** verified current `main` HEAD `584db0e9582ee49e7e35b9ce56287a82901e28b7` before closure, confirmed unchanged from the options-package task's own ending state; Decision 5 branch clean, fast-forward-eligible. The approval record was independently verified line-by-line against every element of Hunter's stated decision before this entry was written.
- **Impact on remaining stages:** Stage 9 remains `IN PROGRESS`, not complete. Decision 6 has not begun. No change to Stage 7, Stage 8, Decisions 1–4, `D-0008`, or the Controlled Automation V1/`D-0007`/`D-0009` workstream.
- **Hunter's approval:** Approved 29 July 2026.
- **Date:** 2026-07-29.

**2026-07-29 — Controlled Automation V1: Phase 0 Batch A APPROVED AND MERGED; Batch B task preparation authorised, not started (parallel system workstream, not a roadmap stage)**
- **What changed:** Hunter approved the completed Batch A implementation for merge and authorised preparation and review of one exact bounded Batch B task only. During integration, a second identifier collision was found and mechanically resolved: workshop Decision 5's own approval had independently claimed `D-0010` (merged, canonical), colliding with the unmerged automation's own `D-0010` (Batch A authorisation). Per this build's established precedent (the earlier D-0005/D-0006 case), the canonical workshop record was left untouched and the two unmerged automation decisions were renumbered: Batch A authorisation `D-0010` → **`D-0011`**; the Batch A merge/Batch B task-preparation decision `D-0011` → **`D-0012`**. Every internal cross-reference across both decision files and the Batch A package was updated to match; no stale reference remains; the canonical workshop `D-0010` is confirmed byte-identical to its pre-existing state. The renumbered payload (`90-meta/controlled-automation-v1/phase-0-structured-control-records/batch-a/`, 15 files) was merged into `main`.
- **Why:** the collision was a direct, mechanical consequence of two independent workstreams both using the next sequential decision number; resolving it before merge prevents a permanent, confusing identifier clash in the decision register.
- **What this does not do:** no real operational record was migrated or given frontmatter; no capability or mandate status changed; the live decision register was not regenerated; no validator, `mfcctl`, or Phase 1 component exists; Batch B implementation was not authorised, only preparation and review of its exact task specification (not begun by this entry).
- **Impact on remaining stages/workstreams:** None. Workshop Stage 9 status (Decisions 1–5 `APPROVED — COMPLETE`; Decision 6 not started) is unaffected and untouched.
- **Hunter's approval:** Approved 2026-07-29, per `D-0011`/`D-0012`. **Batch B task preparation, its implementation, and Phase 1 remain separate, later, explicit steps, not begun by this entry.**
- **Date:** 2026-07-29.

**2026-07-29 — Stage 9 Decision 6 approved (facilitator requirements)**
- **What changed:** Hunter approved a refined form of Option 2: "MFC facilitators must meet defined minimum competencies, receive a structured facilitator guide and orientation, rehearse delivery, and complete one light fidelity or competency verification before independently facilitating the workshop." Recorded in decision record `D-0013` ([[30-decisions/D-0013-stage9-decision6-facilitator-requirements|30-decisions/D-0013-stage9-decision6-facilitator-requirements.md]]). The Decision 6 options package (prepared and reviewed on branch `ops/stage9-decision6-facilitator-requirements`, HEAD `f3f7b96`) was closed on the same branch, since `main` had not advanced past the verified starting HEAD (`5acdde5`) during preparation — no reconciliation was required. Ten minimum competency areas were recorded (claims-boundary knowledge; five-phase delivery; explanatory feedback/retrieval; context-neutral framing; guiding the three-moment Radar; non-clinical scope; avoiding unsupported claims; inclusive language; recognising when a situation exceeds facilitator/workshop scope; following approved escalation/safeguarding procedures once established), plus a minimum preparation structure (guide; orientation; rehearsal; one observed/simulated verification; feedback; a light pre/post-delivery checklist). Stage 9 status changes from `IN PROGRESS — DECISIONS 1–5 APPROVED; DECISION 6 NOT STARTED` to `IN PROGRESS — DECISIONS 1–6 APPROVED; DECISION 7 NOT STARTED`.
- **Rationale (recorded explicitly as an MFC product/operating-standard decision, not an evidence-proven finding):** F6 establishes no proven facilitator-training model and recommends none of its three options with confidence; the selected model is based on delivery fidelity, participant clarity, quality assurance, and proportionate risk control, incorporating Option 1's minimum-competency-and-guide content as a floor while adding Option 2's proportionate rehearsal/verification. One independent review of the options package (`PASS`, 0 critical, 0 major, 2 minor, 1 future-improvement, neither requiring correction) preceded Hunter's approval; one independent line-by-line verification of `D-0013` against Hunter's exact approval text found no material mismatch.
- **Safeguarding and Decision 9 boundary recorded in `D-0013`:** no facilitator is required to be a clinician solely because they deliver the workshop; facilitator orientation and rehearsal do not satisfy the mandatory pre-pilot safeguarding gate; Decision 6 does not define the non-clinical distress-response protocol's content; Decision 9 retains full authority over the safeguarding model; no facilitator may be cleared for participant-facing pilot delivery until the safeguarding gate and applicable facilitator instructions are approved.
- **Decision 7/11 boundary recorded:** Decision 6 establishes the minimum initial facilitator standard only — it does not decide the exact participant-experience/facilitation-design question (Decision 7), the full quality-assurance/replication/scaling/governance question (Decision 11), a risk-tiered facilitator model, or setting-classification rules.
- **Forms Reconciliation Register updated:** row 26 marked decided (refined Option 2 selected; Options 1/3 not selected, with rationale); row 25 marked unresolved-unchanged; row 27 added, recording the new administration records the approved standard creates (guide/orientation/rehearsal/verification/checklist completion), all deferred to Stage 10 for format/retention/ownership/integration. The live Workshop Forms and Measurement Blueprint were not edited or marked as updated.
- **Evidence and authority boundaries preserved:** Decisions 1–5's approved requirements (`D-0003`/`D-0004`/`D-0005`/`D-0008`/`D-0010`) and Stage 7's audience/outcomes/essential content remain unchanged. Decision 7's, Decision 9's, and Decision 11's authority are each fully preserved. C-13, C-20, C-22, C-23 remain unresolved, untouched. The mandatory pre-pilot safeguarding gate is unchanged — this approval does not satisfy it.
- **Supporting evidence:** verified current `main` HEAD `5acdde5910b41deb5d4990f3db14600ce5cbe62b` before closure, confirmed unchanged from the options-package task's own ending state; Decision 6 branch clean, fast-forward-eligible. The approval record was independently verified line-by-line against every element of Hunter's stated decision before this entry was written.
- **Impact on remaining stages:** Stage 9 remains `IN PROGRESS`, not complete. Decision 7 has not begun. No change to Stage 7, Stage 8, Decisions 1–5, or the Controlled Automation V1/`D-0007`/`D-0009`/`D-0011`/`D-0012` workstream.
- **Hunter's approval:** Approved 29 July 2026.
- **Date:** 2026-07-29.

**2026-07-29 — Stage 9 Decisions 7–11 controlled fast-track activated (procedural process change, not a substantive workshop design decision)**
- **What changed:** Hunter approved replacing, for Stage 9 Decisions 7–11 only, the process `separate initiation → separate options → Hunter selection → closure` with `combined initiation and options → Hunter selection → closure`. Recorded in [[90-meta/operating-pack/06-stage9-decisions7-11-fast-track-control|90-meta/operating-pack/06-stage9-decisions7-11-fast-track-control.md]] (no D-number assigned, per Hunter's own explicit instruction not to invent one unless the governance records require it — this is a process record, not a decision record). Two new canonical templates created: [[99-templates/stage9-combined-decision-run-template|99-templates/stage9-combined-decision-run-template.md]] (verify state; retrieve the agenda entry; perform a bounded initiation analysis in place of a separate initiation brief; stop before option preparation if an escalation condition exists; otherwise prepare ≤3 options; one independent review; ≤1 correction pass; commit, do not merge; stop before Hunter selection) and [[99-templates/stage9-decision-closure-template|99-templates/stage9-decision-closure-template.md]] (use Hunter's exact selection; create the formal decision record; update only directly affected reconciliation records; one line-by-line verification; ≤1 material-correction pass; safe reconciliation if `main` has advanced; update status records; merge; report the final HEAD; prepare, but do not execute, the next decision's combined-run prompt — or, for Decision 11's own closure, the Stage 9 completion-verification task instead).
- **Controls retained (unchanged):** fidelity to the approved Stage 9 agenda; the named evidence input only; preservation of all prior approved decisions; evidence/claims-boundary discipline; full dependency mapping; capability-sufficiency assessment; Workshop Forms/Measurement Blueprint/register consideration where relevant; safeguarding separation (no fast-tracked decision may satisfy or narrow the mandatory pre-pilot gate); exactly one independent Sonnet Medium review per combined run and one per closure; at most one correction pass per stage, critical/major only; Hunter's own selection before any closure; a separate, later, explicit closure and merge; no automatic continuation.
- **Controls consolidated (removed for Decisions 7–11 only):** a separately merged initiation brief as its own artefact; a separate Hunter/ChatGPT approval step between initiation and options preparation; an initiation-only independent review; duplicated full repository-state verification at both an initiation step and a subsequent options step; repeated full restatement of controls already fixed by the fast-track control record or the canonical templates.
- **Automatic escalation conditions recorded:** unclear/conflicting authority; missing or non-final evidence input; material conflict with an approved decision; genuine need for new research; demonstrable specialist-capability gap; a safeguarding dependency preventing option preparation; inability to separate the decision from another unresolved one; unreliable repository state; time/context/usage limits threatened. Any such condition stops a combined run before option preparation and escalates to Hunter.
- **Git merge-queue rule recorded:** only one bounded Stage 9 workshop task may merge into `main` at a time; unrelated work (e.g., the Controlled Automation V1/system workstream) may continue on separate branches without restriction; unrelated merges should wait, where practicable, while a short Stage 9 combined run or closure is active — a short cooperative queue, not a repository freeze; if `main` advances anyway, the established fresh-closure-branch reconciliation process applies, and unrelated work is never overwritten.
- **Suspension conditions recorded:** recurring critical/major findings suggesting the consolidated process itself causes errors; a safeguarding or authority-boundary violation; Hunter's own instruction to revert; or any automatic escalation condition triggered mid-run.
- **What this does not do:** no substantive Stage 9 design decision was made by activating the fast-track; C-13/C-20/C-22/C-23 remain unresolved; the mandatory pre-pilot safeguarding gate is unchanged and unsatisfied; Decisions 1–6 and Stage 7 are untouched; the Controlled Automation V1/`D-0007`/`D-0009`/`D-0011`/`D-0012` workstream is untouched; Decision 7 has not begun — its combined-run prompt ([[60-projects/workshop-evidence-informed-adult/04-design-requirements/11-stage9-decision7-combined-run-prompt|60-projects/workshop-evidence-informed-adult/04-design-requirements/11-stage9-decision7-combined-run-prompt.md]]) is prepared, not executed.
- **Hunter's approval:** Approved 29 July 2026.
- **Date:** 2026-07-29.

**2026-07-29 — Stage 9 Decision 7 approved (fidelity and adaptation boundaries); Decision 8 combined-run prompt prepared**
- **What changed:** Hunter approved a refined form of Option 3: "MFC will use a structured essential-versus-flexible delivery taxonomy that broadly protects the workshop's approved outcomes, mechanisms, product requirements, facilitator boundaries and safety requirements while permitting appropriate surface-level and accessibility adaptation. Material and safety-driven deviations will be recorded through a light facilitator-side process." Recorded in decision record `D-0014` ([[30-decisions/D-0014-stage9-decision7-fidelity-adaptation-boundaries|30-decisions/D-0014-stage9-decision7-fidelity-adaptation-boundaries.md]]). The Decision 7 combined-run package (prepared and reviewed on branch `ops/stage9-decision7-fidelity-adaptation-boundaries`, HEAD `510b927`) was closed on the same branch, since `main` (`41a9cae`, which had meanwhile advanced through the unrelated Controlled Automation V1 Phase 0 Batch B merge) had not advanced further during closure — no reconciliation was required. Options 1 and 2 were not selected (Option 1: insufficient structured information for later learning/QA; Option 2: too narrow a protected set). A complete six-part taxonomy was recorded (essential functions; flexible forms; ordinary adaptation; accessibility/context adaptation; safety-driven deviation; material deviation), plus a light deviation-recording requirement. Stage 9 status changes from `IN PROGRESS — DECISIONS 1–6 APPROVED; DECISION 7 NOT STARTED` to `IN PROGRESS — DECISIONS 1–7 APPROVED; DECISION 8 NOT STARTED`.
- **Rationale:** this is recorded explicitly as an MFC product/delivery/quality-assurance decision, not an evidence-validated fidelity model — F6's core-vs-peripheral framework remains conceptual and unvalidated for MFC, F3/F4 identify plausibly-relevant elements without establishing a complete fidelity boundary, and no claim is made that the selected taxonomy is optimal or that recording deviations improves outcomes. One independent review of the options package (`PASS WITH BOUNDED CORRECTIONS`, 0 critical, 1 major, 0 minor, 0 future-improvement) and one correction pass (reproducing the mandatory safeguarding gate verbatim, which had only been paraphrased) preceded Hunter's approval; one independent line-by-line verification of `D-0014` against Hunter's exact approval text found no material mismatch.
- **Decision 9/11 boundaries recorded in `D-0014`:** safety-driven deviation always takes priority over planned delivery, but Decision 7 does not define the complete distress-response/safeguarding protocol, does not satisfy or advance the mandatory pre-pilot gate, and does not treat safety-driven deviation as proof of pilot readiness — Decision 9 retains full authority. Decision 7 provides Decision 11 with the approved taxonomy and deviation categories as an input; it does not execute or narrow Decision 11's own quality-assurance/governance question.
- **Forms Reconciliation Register updated:** row 28 marked add-deferred, recording the approved light deviation-recording scope (what triggers a record; minimum information captured); exact fields/workflow/ownership/retention/integration deferred to Stage 10. The live Workshop Forms and Measurement Blueprint were not edited.
- **Decision 8 combined-run prompt prepared, not executed:** [[60-projects/workshop-evidence-informed-adult/04-design-requirements/12-stage9-decision8-combined-run-prompt|60-projects/workshop-evidence-informed-adult/04-design-requirements/12-stage9-decision8-combined-run-prompt.md]], populated from [[99-templates/stage9-combined-decision-run-template|99-templates/stage9-combined-decision-run-template.md]] with Decision 8's exact agenda entry (question: "What choice, opt-out, and disclosure-depth defaults should the session use?"; evidence input F7's Level C proposed requirements; F7's own three-option range reproduced, not reinvented; dependencies Decision 9 — mutual — and Decision 3 — one-directional — confirmed against all eleven agenda entries; Decision 10 and Decision 11 confirmed one-directional in reverse; the agenda's own explicit split between Decision 8's design-principles component, addressable now, and its safeguarding component, blocked pending Decision 9). The prompt explicitly excludes finalising any safeguarding-relevant content.
- **Evidence and authority boundaries preserved:** Decisions 1–6's approved requirements and Stage 7's outcomes remain unchanged. Decision 9's and Decision 11's authority are each fully preserved. C-13, C-20, C-22, C-23 remain unresolved, untouched. The mandatory pre-pilot safeguarding gate is unchanged — this approval does not satisfy it.
- **Supporting evidence:** verified `main` HEAD `41a9cae84c9c5b16fb380a0bdefdb0a749afdceb` before closure (differing from the reported expected HEAD `422c894` by an unrelated Controlled Automation V1 Batch B merge, confirmed via diff to touch no workshop file); Decision 7 branch clean, fast-forward-eligible. The approval record was independently verified line-by-line against every element of Hunter's stated decision before this entry was written.
- **Impact on remaining stages:** Stage 9 remains `IN PROGRESS`, not complete. Decision 8 has not begun. No change to Stage 7, Stage 8, Decisions 1–6, or the Controlled Automation V1 workstream.
- **Hunter's approval:** Approved 29 July 2026.
- **Date:** 2026-07-29.

**2026-07-29 — Controlled Automation V1: Phase 1 (read-only deterministic verification) implemented, reviewed, corrected, and merged (parallel system workstream, not a roadmap stage)**
- **What changed:** Hunter approved the bounded Phase 1 implementation task, subject to first reconciling a reported verification-rule count inconsistency (checkpoint stated "18 rules" against category counts summing to 19). Enumeration confirmed **19 unique rule IDs** (A: 5, B: 4, C: 4, D: 3, E: 3) — a pure arithmetic/documentation error, corrected consistently across the living specification files; no rule was missing, duplicated, or cross-listed. The verifier (`90-meta/controlled-automation-v1/phase-1-read-only-verification/verify_controlled_automation.rb`) was implemented: 19 deterministic rules, structurally read-only (every file read uses explicit read mode; no write call exists anywhere in the script; no AI model is invoked). 13 synthetic, isolated fixtures and a test harness (`tests/test_verify.rb`) were built — all 20 assertions pass. A real-repository read-only smoke test ran twice (before and after one correction): **0 errors, 0 warnings, 7 information findings** each time (3 correctly-reported expired mandates M-010/011/012; 4 informational notes on mandate files' `id` field naming, a known non-blocking difference) — `git hash-object` confirmed byte-identical on all 9 checked real records before and after both runs. One independent review found `RULE-E01` existed only as a code comment, never emitted as a distinct finding — corrected (now emits alongside `RULE-B01` for the one typed cross-record reference in scope), re-verified with an identical clean smoke-test result.
- **Why:** Phase 1 is the first automated (non-manual) component in Controlled Automation V1 — a reporting-only verifier proving the Phase 0 structured data is machine-checkable, without crossing into remediation, unattended operation, or any write capability.
- **What this does not do:** no operational capability, mandate, or decision record was changed; no workshop content was touched; no automatic remediation, `--apply`/`--repair` mode, `mfcctl`, command framework, or Phase 2 component exists; Phase 2 was not authorised or begun.
- **Impact on remaining stages/workstreams:** None. Workshop Stage 9 status (Decisions 1–7 approved; Decision 8 fast-track combined-run prompt prepared, not executed) is unaffected and untouched.
- **Hunter's approval:** Approved 2026-07-29, subject to the rule-count reconciliation completed above. **Phase 2, automated remediation, scheduled/continuous verification, and any agentic action based on findings remain separate, later, explicit Hunter decisions, not made by this entry.**
- **Date:** 2026-07-29.

**2026-07-29 — Material authority change: product-design decision delegation for Stage 9 Decisions 8–11 (process/governance change, not itself a workshop design decision)**
- **What changed:** Hunter determined the decision-by-decision approval workflow used for Decisions 1–7 was creating excessive process burden without adding meaningful human judgement for decisions that are evidence-informed but not evidence-determined. Hunter delegated authority to Claude to select and formally record the recommended product-design approach for Stage 9 Decisions 8–11 without returning to Hunter after each decision, where the decision is: evidence-informed but not evidence-determined; reversible through later pilot learning; consistent with authoritative MFC records; within the approved workshop scope; and not a legal, ethical, or organisational risk-acceptance decision reserved for Hunter. No D-number is assigned to this delegation itself, per Hunter's own explicit instruction, consistent with this build's established practice of not creating a decision record for pure process changes (e.g., the Decisions 7–11 fast-track activation).
- **Hunter's reserved authority, unchanged:** a material legal, ethical, or safeguarding risk; a change to MFC's mission, framework, approved definition, or organisational claims; a consequential budget/staffing/credential commitment; an unresolvable conflict between authoritative MFC records; two or more credible approaches creating materially different workshop products where evidence/experience/reversibility/simplicity do not provide a responsible basis for selection; and participant-facing pilot-readiness approval itself.
- **Effect:** Decisions 8, 9, 10, and 11 were completed under this delegation in one consolidated task (see the Stage 9 completion entry below). One genuine Hunter-reserved matter was identified during that work (Decision 9's outstanding safeguarding validation items) and is carried forward as an explicit, named, unresolved requirement — not fabricated or bypassed.
- **What this does not do:** it does not delegate any of the six reserved-authority categories above; it does not retroactively alter Decisions 1–7's own approval basis (each remains Hunter's own decision, recorded under the original process); it does not weaken any evidence, claims, or safeguarding boundary already established.
- **Hunter's approval:** Approved 29 July 2026.
- **Date:** 2026-07-29.

**2026-07-29 — Stage 9 complete with explicit downstream gates: Decisions 8, 9, 10, and 11 decided under delegated authority; consolidated product strategy, participant-experience review, completed Forms Reconciliation Register, and one independent review produced; Stage 10 prompt prepared, not executed**
- **What changed:** Under the delegation above, Claude completed Decisions 8–11 as one integrated task, each recorded in its own formal decision record: **Decision 8** (`D-0015`) — universal minimum choice/opt-out/low-disclosure controls (F7's own Option 1), moderate confidence, no setting-specific tiering. **Decision 9** (`D-0016`) — design-level and facilitator-scope safeguarding principles decided (non-clinical framing; standard disclosure-statement principle; facilitator scope-recognition/handoff; reuse of Decision 7's safety-driven-deviation authority); distress-response content, referral pathway, escalation thresholds, emergency procedure, mandatory-reporting/jurisdictional requirements, host responsibilities, and insurance/clinical-governance sign-off explicitly **NOT** decided — recorded as named requirements for qualified legal/clinical/organisational validation. **Decision 10** (`D-0017`) — F9's Option A (minimum low-burden) measurement architecture, extended to cover the three-moment Radar (general, not per-moment, per `D-0010`'s own boundary) and to keep facilitator-side administrative records (Decision 6/7's own) as a distinct stream from participant outcome measurement; no second wave, substudy, or Debra-resource instrument adopted for the initial pilot. **Decision 11** (`D-0018`) — minimum quality-assurance/replication system extending Decision 7's own essential/flexible taxonomy, with version-control and correction-authority rules fixed; culturally specific adaptation for any future context explicitly reserved to appropriate MFC governance/specialist input.
- **Supporting work produced:** an integrated participant/facilitator product-experience review ([[60-projects/workshop-evidence-informed-adult/04-design-requirements/15-stage9-participant-experience-and-product-review|60-projects/workshop-evidence-informed-adult/04-design-requirements/15-stage9-participant-experience-and-product-review.md]]) — coherent overall, with one identified, already-disclosed, unresolved gap (Decision 9's distress-response content); a consolidated Stage 9 product-strategy deliverable assembling all eleven decisions for Stage 10 ([[60-projects/workshop-evidence-informed-adult/04-design-requirements/16-stage9-consolidated-product-strategy|16-stage9-consolidated-product-strategy.md]]); a completed Forms Reconciliation Register (34 rows) providing a decision-requirement-level Stage 10 implementation plan, with every row either Stage-10-actionable, explicitly blocked pending Decision 9, or already in effect; one independent review of the complete package; and one bounded, unexecuted Stage 10 workshop-production prompt.
- **Review and correction:** one independent review (verdict and issue counts recorded in the dated Current State entry and in [[60-projects/workshop-evidence-informed-adult/04-design-requirements/14-stage9-decisions8-11-independent-review|14-stage9-decisions8-11-independent-review.md]]); at most one correction pass applied for any critical/major finding, per the fast-track's own established policy.
- **Stage 9 completion determination:** Stage 9 is recorded as **`COMPLETE WITH EXPLICIT DOWNSTREAM GATES`**, not unconditionally complete — the mandatory pre-pilot safeguarding gate (Decision 9) remains genuinely unresolved and is carried forward exactly as the agenda's own text anticipates ("the decision itself must be resolved before Stage 11 pilot-ready approval, at the latest" — Stage 9 may develop options, which it has; full resolution is not a Stage-9-blocking requirement per the agenda's own text, but is a pre-pilot-blocking requirement, honestly disclosed, not bypassed).
- **Evidence and authority boundaries preserved:** Decisions 1–7's approved requirements and Stage 7's outcomes remain unchanged. C-13, C-20, C-22, C-23 remain unresolved, untouched. The mandatory pre-pilot safeguarding gate is unchanged and unsatisfied. The Controlled Automation V1 architecture and all its approved records remain untouched.
- **Impact on remaining stages:** Stage 9 is complete with the gate above carried forward. Stage 10 has not begun — its complete, bounded production prompt is prepared, not executed, per Hunter's own explicit instruction.
- **Hunter's approval:** exercised via the delegation above; Hunter's own review of this consolidated result and the outstanding Decision 9 items remains the next authorised action.
- **Date:** 2026-07-29.

**2026-07-29 — Stage Autonomy V1 authorised for, and executed against, workshop Stage 10 (parallel system workstream extending into a roadmap stage)**
- **What changed:** Hunter explicitly authorised (chat, this session) extending Stage Autonomy V1 — built and synthetically proven under `D-0019`/`M-013` — to one live, bounded Stage 10 production run. Recorded via a new decision and mandate, `D-0020` and `M-014` (neither retrospectively alters `D-0019`/`M-013`, which remain accurate: the original build-and-proof deliberately excluded workshop work). Under `M-014`, Stage Autonomy run `SA-001` executed the prepared, previously-unexecuted Stage 10 production prompt ([[60-projects/workshop-evidence-informed-adult/04-design-requirements/19-stage10-workshop-production-prompt|19-stage10-workshop-production-prompt.md]]), building all thirteen required deliverable components as `60-projects/workshop-evidence-informed-adult/05-stage10-workshop-package/00-...md`–`13-...md`, each recording its own delegated-decision rationale (selected direction, evidence basis/limitations, why minimum sufficient, reversibility, revision trigger) in the run's journal.
- **Safeguarding-timing authority check:** performed before any Stage 10 content was built, per Master Project Control §4's own pilot-readiness controls ("resolved during Stages 10–11, not before"), the Stage 9 completion-verification record, and the Stage 10 prompt's own text — all three agree Stage 10 execution is permitted before Decision 9's six items resolve, provided safeguarding-dependent content stays blocked, not fabricated. No conflict found; recorded in full in `D-0020`.
- **Review and correction:** one independent Sonnet reviewer (fresh context) checked the complete package against the production prompt, the consolidated Stage 9 strategy, `D-0016`, and `K-08`, plus direct spot-checks of several individual decision records. Verdict: **PASS**, zero critical/major/minor findings across all seven checked areas (no fabricated safeguarding content; no claim beyond any decision's permitted boundary; no essential function altered; internal consistency; no live-document edit; no unassessed measure selection; essential/flexible taxonomy applied correctly). No correction pass was required. Recorded at [[60-projects/workshop-evidence-informed-adult/05-stage10-workshop-package/14-stage10-independent-review|14-stage10-independent-review.md]].
- **Merge:** Phase 1 re-verified clean (`errors=0`) before and after merge; `main` had not advanced during the run, so no reconciliation was required; the package was merged to `main` via `--no-ff`.
- **Evidence and authority boundaries preserved:** Decisions 1–11 and Stage 7's outcomes remain unchanged. C-13, C-20, C-22, C-23 remain unresolved, untouched. **The mandatory pre-pilot safeguarding gate (`D-0016`) is unchanged and unsatisfied** — no distress-response, referral, escalation, mandatory-reporting, or host-responsibility content exists anywhere in the package; every such placeholder is left explicitly, visibly empty ([[60-projects/workshop-evidence-informed-adult/05-stage10-workshop-package/10-safeguarding-integration-bounded|10-safeguarding-integration-bounded.md]]). No live Google document (Workshop Forms, Measurement Blueprint) was edited. No measure was selected from the Debra resources.
- **Impact on remaining stages:** **Stage 10 is complete.** Stage 11 has not begun and is not authorised by this work. No participant-facing pilot delivery is authorised. `M-014` does not auto-renew and does not authorise Stage 11 or any further workshop use.
- **Hunter's approval:** exercised via `D-0020`'s explicit authorisation; Hunter's own review of the merged package and its next action (commissioning Decision 9's qualified safeguarding/legal validation) remains the next genuine decision.
- **Date:** 2026-07-29.

**2026-07-29 — Stage Autonomy V1 applied to Stage 10 review pack and Decision 9 safeguarding-validation preparation (second live application; parallel system workstream)**
- **What changed:** Hunter explicitly authorised a second live Stage Autonomy V1 objective, materially different from Stage 10 production: preparing (never sending, never answering) a concise Hunter review pack for the already-merged Stage 10 package, and a qualified-human validation package for Decision 9's six unresolved safeguarding items. Recorded via a new decision and mandate, `D-0021` and `M-015` (neither alters `D-0020`/`M-014`, which remain accurate records of Stage 10 production itself). Stage Autonomy run `SA-002` built: a Hunter review pack (executive overview, participant/facilitator journey review, workshop-content review, review checklist, material-issues classification, recommended review method) and a safeguarding-validation package (a master brief reproducing Decision 9's six items verbatim with all 15 required fields each; a qualified-reviewer role map with no names invented; four reviewer-specific packs — legal, clinical-governance, insurance/organisational-risk, delivery-host; reviewer-response and MFC-decision templates; a validation tracker; unsent communication drafts; a bounded Stage 11 readiness pathway; an implementation map) — `60-projects/workshop-evidence-informed-adult/06-stage10-review-and-safeguarding-validation/`.
- **Review and correction:** one independent Sonnet reviewer (fresh context) returned **PASS WITH MINOR FINDINGS** — two broken cross-references, both corrected in one pass. No critical/major finding; no fabricated legal/clinical content found anywhere; correct legal/clinical/insurance/host authority separation confirmed; no premature safeguarding or pilot-approval signalling found.
- **Evidence and authority boundaries preserved:** no Decision 9 item was answered; no external communication was sent (all drafts have no recipient filled in); no live Google document was edited; no Stage 10 package file was materially changed (only its own already-blank placeholders remain blank; the implementation map lists them, does not fill them); Decisions 1–11 remain unaltered.
- **Impact on remaining stages:** does not advance Stage 10's own status (already complete) or begin Stage 11. The mandatory pre-pilot safeguarding gate (`D-0016`) is unchanged and unsatisfied.
- **Hunter's approval:** exercised via `D-0021`'s explicit authorisation; Hunter's next genuine actions are named in [[60-projects/workshop-evidence-informed-adult/06-stage10-review-and-safeguarding-validation/00-index|60-projects/workshop-evidence-informed-adult/06-stage10-review-and-safeguarding-validation/00-index.md]] (review the pack; choose/confirm qualified reviewers; authorise sending the prepared requests).
- **Date:** 2026-07-29.

**2026-07-29 — Portfolio Autonomy V1 built and proven; pre-launch MFC Website Intelligence Baseline complete (new, parallel system workstream)**
- **What changed:** Hunter authorised (`D-0022`, `M-016`) a new control layer, Portfolio Autonomy V1, above Stage Autonomy V1 — a minimum-sufficient multi-objective register, deterministic validator (`portfolio_ctl.rb`), priority/dependency/idle-state model, and file-scope/concurrency-safety model, proven against a required P1–P5 synthetic fixture (10/10 assertions) and a separate file-scope-conflict fixture. No second orchestrator was created. Its first live objective, executed while the separate, concurrently active workshop chat's own objective was correctly represented and protected (never touched), was a pre-launch Website Intelligence Baseline: `60-projects/mfc-website/`. This triangulates MFC's existing, active, Drive-controlled "Website UX Foundation and Expert Review Brief" (a seven-discipline expert-panel process already through Gates 1–3) against Obsidian authority, 33 Fathom meetings, read-only Wix inspection, and bounded external evidence (WCAG 2.2; nonprofit UX research) — registering and cross-checking that process rather than recreating it. Produces a source/authority map, audience/journey model, sitemap and missing-page analysis, homepage/informational-page architecture, conversion/donation/participation journeys, navigation/accessibility/mobile requirements, a pre-launch measurement framework, a usability/experimentation plan, a capability/agent blueprint (no durable agent created — the gate was not met), a prioritised backlog, and a three-item genuine Hunter decision brief.
- **Review and correction:** one independent Sonnet reviewer covered both Portfolio Autonomy V1 and the baseline together. Verdict **PASS WITH MINOR FINDINGS** — two minor Portfolio Autonomy V1 documentation inaccuracies (both corrected, no functional defect); zero findings against the baseline itself across all eight checked areas.
- **Evidence and authority boundaries preserved:** no Wix edit, publication, or write call of any kind occurred (confirmed via git diff and the reviewer's own independent check); no external communication was sent; no live Google document was edited; no workshop file, decision, or safeguarding material was touched by either branch; no durable/permanent capability was created.
- **Impact on remaining stages:** none on the workshop workstream. Does not begin website implementation, Stage 11, or any participant/visitor-facing action.
- **Hunter's approval:** exercised via `D-0022`'s explicit authorisation; three genuine decisions remain for Hunter (accessibility target level; pricing-tier disclosure; whether to commission real-user usability testing before launch) — see [[60-projects/mfc-website/13-hunter-decision-brief|60-projects/mfc-website/13-hunter-decision-brief.md]].
- **Date:** 2026-07-29.

**2026-07-29 — Website Intelligence Stage 2 built and merged (concurrent session; verified retrospectively by this entry's own author)**
- **What changed:** A concurrent session executed `D-0023`/`M-017` (Website Intelligence Stage 2 — deep-research reconciliation of `PO-002` into a definitive Website Product Strategy and Pre-Build Blueprint), registered `PO-003`, and merged the result to `main` (verified live HEAD `c246119617c90d826c5950e0da59614a26342b21`) before the Living Operating Model task below began. This entry exists so the change log stays in commit order; it was written retrospectively during verification for the entry immediately below, not by the session that did the Stage 2 work.
- **Why recorded here:** The Living Operating Model task's own brief stated an expected `main` HEAD of `fc9cff9`; live verification found `main` had already advanced past that point by exactly this Stage 2 work, which was not yet reflected in this change log.
- **Impact on remaining stages:** None beyond what Stage 2's own commits already record (see [[60-projects/mfc-website/stage-2/00-index-and-executive-summary|60-projects/mfc-website/stage-2/00-index-and-executive-summary.md]]).
- **Date:** 2026-07-29.

**2026-07-29 — MFC Intelligence System Living Operating Model and Capability Directory V1 built and merged**
- **What changed:** Hunter authorised (`D-0024`, `M-018`) one canonical, living control-map documentation package, registered as portfolio objective `PO-004`: a human-readable operating model, a machine-readable system map, a capability directory with role cards for the six currently built capabilities (A-02, A-04, A-05, A-06, and newly-carded `SYS-01`/`SYS-02` for Stage/Portfolio Autonomy V1), an assessment of the 13 approved target capability domains and 6 named future systems (assessed, not built), a gap register, a dependency/build-sequence map, an end-state operating flow with a Mermaid diagram, Portfolio Autonomy integration rules, an update protocol, a core-chat start protocol, a Hunter dashboard, a progress scorecard, and a deterministic validator for the package's own referential integrity — all at `90-meta/living-operating-model/`.
- **Verified findings disclosed by this work:** A-05 and A-06 are both built but currently dormant (`M-011`/`M-012` expired 2026-07-29/2026-07-28, not renewed) — previously true but not visible in one place. Portfolio Autonomy V1's own [[90-meta/controlled-automation-v1/portfolio-autonomy-v1/08-implementation-and-live-proof-evidence|08-implementation-and-live-proof-evidence.md]] claims a live-proof commit for the `PO-002` website baseline that could not be located in `main`'s git history at verification; the underlying mechanism is now separately, genuinely proven via `PO-003`/`PO-004` — recorded as gap `G-03`, not corrected retroactively in the original file (out of this objective's file scope).
- **Review and correction:** one independent Sonnet reviewer (fresh context) returned **PASS WITH MINOR FINDINGS** — three minor findings (a portfolio-register status/schema mismatch; a self-contradictory YAML comment; one role card's maturity wording overstating its own lifecycle status), all corrected in one pass. Deterministic validator (`validate_lom.rb`) ran clean before and after correction (0 errors).
- **Impact on remaining stages:** None. No workshop or website product file was touched (only the shared `portfolio-register.yml` and [[50-authority/mandates/mandate-register|mandate-register.md]] were additively edited). No proposed capability domain or future system was built or activated. No second orchestrator was created. Opus was not used.
- **Hunter's approval:** exercised via `D-0024`'s explicit authorisation; this package raises no new genuine Hunter decision of its own — it surfaces (does not create) the two already-outstanding decisions on `PO-001` and `PO-003`, listed in [[90-meta/living-operating-model/12-hunter-dashboard|90-meta/living-operating-model/12-hunter-dashboard.md]].
- **Date:** 2026-07-29.

**2026-07-31 — Canonical control-state catch-up: this Master Project Control had fallen materially behind six completed, merged Portfolio Autonomy V1 objectives and one Hunter-approved global-roadmap milestone (Stage 10 completion); this entry closes that gap. No product, decision, or mandate content is altered by this entry — it records status only.**

- **Record:** `D-0020`/`M-014` (Stage 10 production) and `D-0021`/`M-015` (Stage 10 review/safeguarding-prep). **What changed:** already recorded above (2026-07-29 entries); this catch-up adds no new fact for these two — flagged here only because §10's own closing sentence had not been updated to reflect that Hunter's approval to begin Stage 10 (sought in the Stage 9 entry) was in fact given and exercised. **Why it matters:** §10 read as though Stage 10 approval was still pending, when Stage 10 had been complete since 2026-07-29. **Effect on roadmap:** global roadmap — Stage 10 is now explicitly stated `COMPLETE` in §10 itself, not only in the frontmatter/status header. **Approval basis:** Hunter, 2026-07-29 (as originally recorded). **Status:** complete. **Date recorded here:** 2026-07-31.
- **Record:** `D-0025` / `M-019` / `PO-005` — Website Intelligence Stage 3 (Experience Strategy, Multidisciplinary Synthesis and Prototype). **What changed:** a corrected, multidisciplinary website experience strategy (three concepts, one recommended, Founder Explanation Architecture, Home/Mental Fitness blueprints, offline prototype, Founder Review Pack) was built, independently reviewed (`PASS WITH MINOR FINDINGS`, corrected), and merged to `main` (merge commit `33db4b7`, per the recovered-branch merge recorded in `Current State and Next Action.md`). **Why it matters:** this Master Project Control previously contained zero mention of `D-0025` or `PO-005`; the objective and its completion were verifiable only from `Current State and Next Action.md` and the decision/portfolio records themselves. **Effect on roadmap:** parallel Portfolio Autonomy V1 workstream — does not touch or advance the fixed Stage 0–12 roadmap. **Approval basis:** Hunter's exact chat authorisation, 2026-07-29, quoted in `D-0025`. **Status:** `COMPLETE` per `60-projects/mfc-website/portfolio-register.yml`; `founder_review_status: PENDING` — Hunter's own review of the package is a separate, still-outstanding action. **Date:** 2026-07-29 (authorised and merged); recorded here 2026-07-31.
- **Record:** `D-0026` / `M-020` / `PO-006` — Framework Integrity and Evidence Observatory V1. **What changed:** one deep framework-integrity examination (source-authority map, canonical framework map, claim-and-evidence register, evidence-strength model, contradiction register) and a designed, built, one-proof-run Evidence Observatory V1 were completed, independently reviewed (`PASS WITH MINOR FINDINGS`, corrected), and merged. This objective also performed the ID-collision reconciliation that resolved a genuine double-claim of `D-0025`/`M-019`/`PO-005` between two unmerged branches, renumbering the workshop objective to `D-0027`/`M-023`/`PO-007`. **Why it matters:** previously unrecorded in this file; the reconciliation is load-bearing for reading `D-0025` through `D-0027` correctly. **Effect on roadmap:** parallel workstream; no framework position was silently changed, no product file touched. **Approval basis:** Hunter's exact chat authorisation, 2026-07-30, quoted in `D-0026`. **Status:** `COMPLETE` per the portfolio register. **Date:** 2026-07-30; recorded here 2026-07-31.
- **Record:** `D-0027` / `M-023` / `PO-007` — Workshop Product Experience Assurance V1 (renumbered from the original, collision-affected `D-0025`/`M-019`/`PO-005` claim per `D-0026`'s reconciliation). **What changed:** a multidisciplinary specialist synthesis, three distinct workshop experience concepts, a recommended concept, complete activity/facilitator/participant materials, a slide storyboard, a Stage 10 comparison, and an HTML delivery prototype were built, independently reviewed (`PASS WITH MINOR FINDINGS`, corrected), and merged to `main` at full HEAD `f16c56c79d2374a322c8e38e334797caf160e8ef`. **Why it matters:** previously unrecorded in this file under its correct, post-reconciliation ID; this is the workshop workstream's most current completed work, and is not itself Stage 11. **Effect on roadmap:** does not begin or substitute for Stage 11; no Decision 9 item resolved; no pilot authorised. **Approval basis:** Hunter's exact chat authorisation, 2026-07-30, quoted in `D-0027`. **Status:** `COMPLETE, INDEPENDENTLY REVIEWED, MERGED` per `Current State and Next Action.md` and the portfolio register; Hunter's own founder review of `10-founder-review.md` and the prototype remains the outstanding next action for this workstream specifically. **Date:** 2026-07-30; recorded here 2026-07-31.
- **Record:** `D-0028` / `M-024` / `PO-008` — Core Operations Hardening and Token Efficiency V1. **What changed:** a worktree-aware deterministic ID-reservation protocol (tested against 5 required cases), Objective Intake V2, Context Manifest V1, Checkpoint and Resume V2, and a bounded Ponytail assessment were built, independently reviewed (`PASS WITH MINOR FINDINGS`, corrected), and merged. **Why it matters:** previously unrecorded in this file; this objective is why later objectives (`D-0029`, `D-0030`) could reserve IDs deterministically across active worktrees rather than merged `main` alone. **Effect on roadmap:** system/tooling workstream; no website, workshop, or framework product content touched. **Approval basis:** Hunter's exact chat authorisation, 2026-07-30, quoted in `D-0028`. **Status:** `COMPLETE` per the portfolio register. **Date:** 2026-07-30; recorded here 2026-07-31.
- **Record:** `D-0029` / `M-025` / `PO-009` — Retrieval Reliability and Source Precedence Evaluation V1. **What changed:** a formal source-precedence model, a sealed 16–20 case evaluation suite with pre-registered thresholds, and one real non-product proof objective were completed against the existing A-04/A-05/A-06 retrieval workflow, independently reviewed (`PASS WITH MINOR FINDINGS`, corrected), and merged. **Why it matters:** previously unrecorded in this file; establishes the first honest, evidence-based maturity assessment of the A-04/A-05/A-06 retrieval pipeline's internal half. **Effect on roadmap:** system/evaluation workstream; no website, workshop, or framework product content touched; no replacement RAG system built. **Approval basis:** Hunter's exact chat authorisation, 2026-07-30, quoted in `D-0029`. **Status:** `COMPLETE` per the portfolio register. **Date:** 2026-07-30; recorded here 2026-07-31.
- **Record:** `D-0030` / `M-028` (plus task mandates `M-029`, `M-030`) / `PO-010` — Evidence Discovery and Synthesis Reliability V1. **What changed:** a formal A-06 evidence-reliability standard, a sealed 16-case evaluation suite, and one bounded live-research proof objective were completed testing A-06's external evidence-discovery function, complementing `D-0029`'s internal-retrieval evaluation, and merged (independent review recorded in the objective's own implementation-and-review evidence file). **Why it matters:** previously unrecorded in this file; completes the retrieval-and-evidence reliability pair (`D-0029` internal, `D-0030` external) referenced in the A-06 maturity assessment. **Effect on roadmap:** system/evaluation workstream; no website, workshop, or framework product content touched; no replacement research agent or paid evidence subscription created. **Approval basis:** Hunter's exact chat authorisation, 2026-07-30, quoted in `D-0030`. **Status:** `COMPLETE` per the portfolio register. **Date:** 2026-07-30; recorded here 2026-07-31.

**What this entry does not do:** it does not resolve, narrow, or reinterpret D-0016's six safeguarding items; it does not authorise Stage 11; it does not adopt, merge, or repair the separately-tracked navigability branch (`ops/vault-navigability-v1`), which remains unmerged and outside this entry's scope; it does not alter any decision, mandate, or product record — only this file's own status text and change log.
**Impact on remaining stages/workstreams:** none. Stage 11 remains not started and blocked exactly as before this entry.
**Hunter's approval:** exercised via Hunter's chat approval of the verified control-state position (Stage 10 complete; Stage 11 blocked by `D-0016`; Portfolio Autonomy workstreams parallel, not roadmap-substituting), 2026-07-31, authorising this reconciliation task itself.
**Branch:** `ops/canonical-control-state-catch-up-v1`, from `main` at `538bd9c35931c5891ee7c7a8e151cd84b1bbbca2`. Not merged by this entry.
**Date:** 2026-07-31.

**2026-07-31 — D-0044: Stage 11 entry vs. pilot-readiness reconciliation (governance correction, not a workshop or safeguarding decision)**
- **What changed:** a bounded, read-only reconciliation found a genuine conflict between `D-0016`'s own preserved gate text plus this Master Project Control's own §4 Stage 11 definition (both treating Stage 11 as the mechanism that resolves safeguarding, "resolved during Stages 10–11, not before") against this file's own §10 status text and `Current State and Next Action.md`'s top section (which had, since shortly after 2026-07-29, read Stage 11 itself as blocked from starting). Hunter reviewed the exact quoted language from both sides and approved the reading consistent with `D-0016`'s own words: `D-0016` blocks final pilot-ready approval and participant-facing delivery, not Stage 11's entry. Recorded formally at `D-0044`.
- **Why it matters:** the prior wording ("before Stage 11 can begin") was stricter than `D-0016` itself or the fixed roadmap's own design required, and had been repeated across multiple objective entries as though settled, without ever being reconciled against the source text.
- **What this does not do:** it does not resolve, narrow, or reinterpret any of `D-0016`'s six matters — items 1–2 (clinical-governance), 4 (legal, cannot be resolved internally), 3/5 (host/MFC operational arrangements), and 6 (insurer/broker plus governance sign-off) all require exactly the qualified treatment `D-0016` already specifies; MFC's committee may coordinate and contribute within its documented competence but may not substitute for reserved professional judgement. It does not begin substantive Stage 11 work, appoint any reviewer, conduct outreach, alter workshop content, or mark any matter resolved. `D-0016` remains in force, unresolved, 0 of 6 matters closed.
- **Impact on remaining stages:** Stage 11 is now correctly stated as authorised to begin, not yet started. No participant-facing delivery is authorised at any point before all six matters resolve and Hunter/the appropriate MFC governance authority formally approves the resulting complete safeguarding model.
- **Hunter's approval:** `D-0044`, exercised via Hunter's own explicit chat decision, 2026-07-31, after reviewing the quoted conflicting language directly and approving Interpretation B.
- **Branch:** `ops/d0016-stage11-entry-reconciliation-v1`. Not merged by this entry.
- **Date:** 2026-07-31.

**2026-08-01 — `D-0049`/`M-047`: Outcome Delivery Orchestrator operating model canonicalised, three-page website candidate ratified and merged (parallel workstream, does not touch the Stage 11/D-0016 gate)**
- **What changed:** A-04 upgraded from planning-only (v0, `M-010`) to accountable executive agent (v1, `M-047`, `supervised-real-review`), governed by the Complete-Candidate Standard plus a new permanent Candidate Integrity Closure Gate and supporting protocols (`90-meta/outcome-delivery-orchestrator-v1/`, 17/17 regression cases). As first live proof, a complete three-page website candidate (Home, Mental Fitness, Building Mental Fitness, optional supporting glossary) was produced, independently reviewed, corrected, and — after a follow-on Candidate Integrity Closure objective resolved a genuine authority-identifier collision (`D-0043`/`M-042` → `D-0049`/`M-047`), a capability-discovery failure (A-18/A-22 wrongly claimed absent; both are canonical), a non-compliant review model (an Opus review reclassified `NON_COMPLIANT_SUPPORTING_EVIDENCE_ONLY`), and an unclassified glossary scope (now `OPTIONAL_SUPPORTING_COMPONENT`) — reassessed by a compliant Sonnet reviewer, which returned `READY_FOR_HUNTER_RATIFICATION`. Hunter ratified the candidate as MFC's current official website direction. System branch (`ops/outcome-delivery-orchestrator-v1`) merged into `main` first (merge commit recorded in that branch's own final HEAD and this repository's `git log`); product branch (`ops/website-three-page-complete-candidate-v1`) retested against the now-canonical system controls and merged second, both by non-fast-forward merge, no squash, no history rewrite.
- **Why it matters:** this is the first live proof that the outcome-delivery operating model (one accountable agent completing a production objective end to end, rather than returning research or recommendations) works in practice, including the model correctly catching and disclosing its own process defects (the identifier collision, the capability-discovery failure, the reviewer-model violation) rather than hiding them.
- **What this does not do:** it does not resolve, narrow, or reinterpret any `D-0016` safeguarding matter; it does not authorise Stage 11; it does not authorise Wix implementation, publication, or any claim that real users have validated the predicted experience; it does not alter MFC's mission, vision, or controlled category meaning; it does not touch the earlier, legitimate `D-0043`/`M-042` decision/mandate lineage on the separate, unmerged `ops/mental-fitness-page-live-proof-v1` branch.
- **Impact on remaining stages:** none. Stage 11 remains not started and blocked exactly as before this entry. Outstanding before any publication of this website work: qualified safeguarding confirmation of the footer crisis-line's sufficiency, Alysse's final visual/responsive design review, genuine audience validation of the untested assumptions A-22 identified, and a classification decision on the unbuilt "How it all connects" diagram.
- **Hunter's approval:** direct chat authorisation for the operating model (`D-0043`/`D-0049` original decision), for the Candidate Integrity Closure objective, and for the final ratification and canonicalisation instruction, all 2026-08-01.
- **Branches:** `ops/outcome-delivery-orchestrator-v1` and `ops/website-three-page-complete-candidate-v1`, both merged into `main` by this entry.
- **Date:** 2026-08-01.

**2026-08-01 — Active-workstream clarification: MFC Agentic Operating System implementation is the active objective; Stage 11 workshop plan remains complete but paused (process clarification, not a new decision — no D-number assigned, per this build's established practice for pure workstream-priority clarifications)**
- **What changed:** following the Stage 11 integrated-review plan's completion and merge, session activity drifted from the parallel MFC Agentic Operating System implementation programme (Nabill's supplied roadmap: `T-01` Session Context Baseline, complete and merged; `T-04` Workflow Packaging, next) back into workshop roadmap planning. Hunter clarified directly: the active objective is continued Agentic OS implementation. The Stage 11 plan may remain complete in the vault; `S11-01` is **not authorised**, and the workshop workstream is **paused**, not cancelled or superseded, until Hunter separately resumes it.
- **Why it matters:** without this clarification, two parallel workstreams (workshop Stage 11 execution vs. the Agentic OS build) could each read as "the" active objective, since both had a completed plan and a stated next action. This entry removes that ambiguity without altering either workstream's own substance.
- **What this does not do:** it does not alter the fixed Stage 0–12 roadmap; it does not authorise, begin, or narrow Stage 11 or any of its six execution tasks (`S11-01`–`S11-06`); it does not resolve, weaken, or touch `D-0016` or `D-0044`; it does not delete, supersede, or invalidate the Stage 11 integrated-review plan, which remains complete and awaiting Hunter's own approval whenever the workshop workstream resumes; it does not alter any capability, mandate, or authority status.
- **Impact on remaining stages/workstreams:** the fixed roadmap's Stage 11 position is unchanged — still authorised to begin, still not started, still gated on `D-0016` for final pilot-ready approval. The Agentic OS implementation programme (a parallel system workstream, not a roadmap stage) becomes the active improvement objective; its next task is `T-04` — Workflow Packaging.
- **Hunter's approval:** exercised via Hunter's own explicit chat clarification, 2026-08-01.
- **Branch:** `ops/bounded-objective-workflow-v1`. Not merged by this entry.
- **Date:** 2026-08-01.

*MFC Intelligence System Build • Project Source Document*
