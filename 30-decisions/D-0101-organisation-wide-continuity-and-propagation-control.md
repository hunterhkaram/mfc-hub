---
id: D-0101
type: decision-record
title: "Organisation-wide continuity and propagation control"
decision_authority: hunter
decided_by: "Hunter Karam — explicit instruction to implement the transcript outcome now"
decided_date: 2026-08-13
status: decided
committee_approval: "not sought — internal intelligence-system operating control"
committee_notification: "not required"
independent_check: "not run — deterministic register, Hub, routing, anti-duplication and closure tests passed in the same accountable AI context; this is technical assurance, not independent review or proof that every source claim or external system is current"
canonical: true
storage_mode: obsidian-primary
authoritative_location: obsidian
confidentiality: internal
owner: hunter
maintained_by: ai
affects:
  - "CLAUDE.md"
  - ".claude/skills/mfc-executive-intake/SKILL.md"
  - ".claude/hooks/route_mfc_intake.py"
  - ".claude/hooks/check_routing_completion.py"
  - ".claude/hooks/enforce_canonical_artifact.py"
  - ".claude/hooks/require_topic_start_receipt.py"
  - "90-meta/controlled-automation-v1/topic-control/canonical-topic-register.yml"
  - "90-meta/hub/generate_hub.py"
  - "90-meta/hub/check_hub_integrity.py"
  - "90-meta/MFC-HUB.html"
---

# D-0101 — Organisation-wide continuity and propagation control

## Decision

Extend the existing deterministic topic-control path from the measurement pilot to every existing MFC Hub pillar. A fresh Claude Code session working in the MFC vault must, for a registered topic:

1. resolve the topic before broad discovery;
2. receive the registered purpose, current truth, readiness, canonical sources, operational destinations, open gates and strongest next action;
3. inspect the linked authoritative sources and current destinations before recommending or changing material work;
4. recommend the strongest evidence-grounded next action before asking Hunter a resolvable technical question;
5. update existing destinations after an approved change, record external revisions and readback where applicable, update the register and regenerate the existing Hub;
6. block a completion claim when the register is invalid or any registered Hub projection is stale;
7. prevent an unlabelled new Markdown or HTML artifact from quietly becoming a competing final for a registered topic; and
8. keep AI review visibly separate from founder, clinical, legal, privacy, insurer, ethics or other qualified-human approval.

The Hub remains a generated readable projection. It is not a replacement system of record and no parallel Hub or persistent agent is authorised.

## Why this is the smallest sufficient intervention

The system already had executive intake, prompt routing, canonical decisions, operational artifacts, a Hub generator and closure controls. The recurring failure was that those parts did not share one enforceable organisation-wide map: only measurement had deterministic reconciliation and propagation. The appropriate intervention is therefore to generalise and bind the existing path, not build another architecture.

The Agent Steward need test did not justify a new persistent agent. The need is recurring, but its responsibilities duplicate existing intake, knowledge stewardship, quality governance and Hub generation. Clarified instructions, an expanded register and executable checkpoints cover the gap with less authority and less duplication.

## Implemented scope

The register now covers 13 existing pillars: grand strategy, workshop delivery, measurement, pricing, marketing and leads, grants and funding, WIIFM, committee send, website, safeguarding, market intelligence, social media and community events.

Each pillar's Hub page is generated from the registered state and includes a source-state fingerprint. The home page carries the same fingerprint. Registered local source changes therefore make the Hub integrity check fail until it is regenerated.

## Retained limits

- Topic resolution is deterministic phrase matching. It is a reliable floor for registered language, not general semantic understanding; the agent must still interpret the request and inspect sources.
- Local controls cannot authenticate to Drive, Wix, Monday or another external service. External freshness is proven only when the working agent uses an available connector, records the returned revision or receipt and reads the destination back.
- A matching fingerprint proves propagation from the registered local state; it does not prove the underlying claim, professional judgement or approval is true.
- Known missing future work is recorded honestly as an open gate. It is not fabricated merely to make the system appear complete.
- The protocol applies when Claude Code is operating in this vault. Work completed in another chat or tool can still be absent until it is deliberately reconciled into the vault and registered destinations.

## Activation evidence

- canonical register validation: pass;
- Hub structure and all 13 topic projections: pass;
- continuity regression suite: 12/12 pass;
- generated Hub retains one home page and the existing 13 pillar pages.

## Cold-start correction — 13 August 2026

The first real cold-start test used the ordinary portfolio question, “What should MFC be working on right now, and what is the strongest next action?” The topic-specific register did not fire because no pillar was named. Claude therefore relied on the mandatory `Current State and Next Action.md` pointer, which was dated 10 August and still described workshop build as the single authorised next action. It also repeated D-0016 framing superseded by D-0099, stale branch state and a founder-signal maintenance choice.

The active control was corrected in place:

- the same canonical register now contains a dated, ranked organisation-wide portfolio view;
- organisation-wide state and priority language has its own deterministic cold-start route;
- the current-state pointer is again a short derived view and explicitly defers to the register and later decisions;
- the register distinguishes the immediate Committee and grant priorities from workshop delivery as the strongest authorised build workstream;
- the Hub home-page priority view and fingerprint now derive from the portfolio record; and
- regression coverage now includes the exact cold-start prompt that exposed the defect.

This remains an instruction/register/evaluation gap, not a need for a new persistent agent. The first activation verdict was therefore revised from technically activated to **revised after failed live cold-start evidence**. Current technical re-test: register pass, all 13 Hub projections pass, continuity suite 14/14 pass, exact portfolio-prompt injection pass. A second genuinely fresh Claude Code session remains the operational acceptance gate.

## External-work reconciliation correction — 13 August 2026

The second cold-start test correctly followed the portfolio register, but Hunter then identified that its leading Committee state was false: the system-drafted email had already been sent to Jake and Onno for review. The existing local email artifact still said `DRAFTED — NOT SENT`, so the register and every downstream projection inherited that stale local status. This is the exact external-to-vault propagation limitation the protocol discloses.

Hunter's direct correction now controls the operational state. The existing email draft was updated in place as a source draft and sent-status record; it does not pretend to be a verbatim sent-message readback. The Committee topic now records `SENT_FOR_REVIEW_AWAITING_JAKE_ONNO_FEEDBACK`, with the exact sent wording/date and external receipt explicitly unverified. The portfolio was re-ranked: live grant verification is the strongest immediate action, workshop delivery is the strongest authorised build workstream, and Committee work waits for Jake/Onno feedback. The two internal Committee quality defects remain recorded for correction before any later final committee issue; they are not misrepresented as preventing an external review send that already occurred.

### Verified external readback and transcript-aligned expansion

Gmail readback subsequently verified the exact external event: Hunter sent “MFC ready for review” to Jake Pepper and Onno van-Es on 11 August 2026 at 3:20 pm with `Strategy & Commerical.pdf` attached. The sent body was read and differs from the longer local source draft. The Committee destination and reconciliation receipt were upgraded from `user_reported` to `verified_readback`; feedback remains pending.

Hunter then supplied the full originating transcript as the authoritative outcome specification. That evidence confirmed continuity alone is insufficient. The same existing control path was expanded to cover evidence-bearing start/progress/completion/waiting/correction receipts; source and complete topic-record comparison at closure; objective-specific specialist assurance with evidence paths and explicit AI/human separation; and Hub visibility of freshness, external confidence, transitions, known failures, learning and the intelligence system's own capability status. No new persistent agent or parallel organisational source of truth was created.

The two pre-existing Committee quality failures were then corrected in the existing founder result and decision trail: the distinct premise audit is explicitly recorded, and the five previously generated approaches are visibly ranked in a real comparison table. Both L-051 and L-057 pass. These corrections do not rewrite the already-sent review email or PDF; they improve the controlled reasoning and assurance record that future work must preserve.

## Live-project acceptance test — grants and funding, 13 August 2026

The current highest-ranked task was executed as real work, not as a synthetic routing prompt. The system first recovered the registered grants topic and its canonical source, then found that the source itself simultaneously said FRRR was the immediate priority, “apply now,” and deferred under Hunter's recorded refusal to commit to regional/rural delivery. Later reconciliation material said the deferral was settled, while the portfolio had nevertheless promoted a fresh FRRR check to organisation-wide priority one.

The workflow then:

1. recorded the project start before changing organisational state;
2. inspected the broader controlled grants corpus rather than trusting the Hub summary;
3. checked official FRRR, Camden Council and City of Parramatta sources live;
4. challenged the premise that an open grant is necessarily an MFC opportunity;
5. established that FRRR is open but deferred under the recorded geography decision, Parramatta's general 2026 round is closed, and Camden is open but lacks a recorded qualifying project/cohort and $20 million public-liability evidence;
6. updated the existing `FINAL-05-grants-and-funding.md` in place, including its recommendation and current source links, rather than creating another grants plan;
7. corrected the grants register, assurance evidence, portfolio ranking and current-state pointer;
8. recorded progress and completion receipts, regenerated the existing Hub and verified the projection; and
9. ran the complete executable control suite: 30 pass, 0 fail, with two controls still honestly labelled self-test-only because they inspect no live artifact.

This test materially improves confidence in the local end-to-end path and also exposes the remaining boundary. The system can reconcile live external evidence when a working session has an authenticated connector or browser and then writes the result back. It cannot know that another chat, Drive, Wix, Monday or a human action changed unless that environment is inspected or the change is explicitly reconciled. The Hub is now an evidence-bearing projection of that reconciled state, not a universal event listener.

## Default-workflow correction — workshop deck live test, 13 August 2026

A real fresh-session test then exposed three coupled failures. The portfolio prompt contained a
minor typo and routed light with no topic scope; the system built a new deck from a legacy
`3-hour` storyboard without first reconciling D-0094's later Half-Day Foundations decision; and a
Stop hook forced Hunter to choose “full intake” versus “direct pass,” even though standing autonomy
assigns specialist routing and reversible production decisions to the system. The resulting deck is
a useful unreviewed candidate, but it does not count as a reviewed current flagship artefact.

The existing continuity path was corrected in place:

1. portfolio routing tolerates the observed missing initial “w” and treats “continue/proceed/build”
   portfolio prompts as material;
2. material registered-topic work cannot delegate or write/edit before a current-session start
   receipt records the actual topic reconstruction, source conflicts, selected action and required
   checks;
3. the workshop record now puts D-0094 ahead of legacy production files, names the preferred and
   retired product labels, preserves the legacy files as evidence rather than silently rewriting
   history, and requires deck-specific instructional-design, accessibility, safeguarding,
   canonical-fidelity and rendering checks;
4. new/current deck candidates using the retired `3-hour`/`3hr`/`MFC-3H-v1` framing are denied;
5. generated Hub pages can no longer be directly edited through Edit or Write—the source record or
   generator must change, followed by regeneration; and
6. the old material-choice Stop hook is no longer registered. Claude chooses the smallest sufficient
   workflow by default and asks Hunter only for a genuinely protected founder or human-authority
   decision.

The Agent Steward need test again rejects a new persistent agent: this was an invocation,
precedence and evaluation defect in capabilities already assigned to executive intake, knowledge
stewardship and quality governance. The binding regression uses the exact typo-bearing prompt and
passes the new route, start, Hub and terminology controls.

## Minimum-complete Hub and lifecycle pass — 13 August 2026

The transcript outcome required more than correct routing. A minimum useful organisational Hub must make the state that guides action visible, including uncertainty and responsibility. The existing control was therefore extended in place rather than replaced:

1. the register now controls 15 topics, adding Framework integrity and operations/governance;
2. nine organisational-domain groups show what is controlled, embedded or only partial, without duplicating Radar/digital/product architecture;
3. external observability is explicit for Obsidian, Drive, Gmail, Monday and Wix, including the last verified boundary and known limitation;
4. every topic page now renders accountability/review trigger, canonical and operational lifecycle, recent receipts, conflicts/supersessions, assurance evidence links and open gates with owner and due/trigger where registered;
5. the home page now renders domain coverage, external-system observability and one human/founder decision queue;
6. a controlled archive/supersession policy preserves history while preventing archived sources from authorising current candidates or projections;
7. accepted reconciliation receipts now regenerate the existing Hub and run its integrity check automatically; and
8. regression coverage tests the two added topics, all minimum Hub sections, archive rejection and receipt-to-Hub propagation.

The workshop continuation was rerun as the live failure-case test. The ordinary continuation prompt routed to `workshop-delivery`, recovered D-0094 and the Half-Day Foundations terminology, exposed the five required artifact-specific checks and blocked an edit before a source-reconstruction receipt. After the evidence-bearing start receipt, controlled continuation unlocked, the Hub regenerated and all 15 topic projections passed. A candidate declaring an archived source remained blocked. No slide edit or specialist review was falsely claimed by this test.

This is now a reliable automatic local lifecycle inside the declared vault/Claude scope. It is not a universal event listener: work in another chat or external system remains invisible until that environment supplies a connector event/readback or a deliberate reconciliation. Qualified-human approval also remains human. These limits are shown in the Hub rather than hidden behind a general readiness label.
