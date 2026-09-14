---
type: approach-review
reviewer: Flint (FL-02), approach contrarian
date: 2026-08-12
subject: HREC research integration into MFC Roadmap board
context: Hunter requested integration of HREC/data-strategy research document (224-line strategy, 31-university pathways analysis, five action items) into trackable workflow on Monday.com MFC Risk & Roadmap board.
---

# Approach Review: HREC Strategy Integration into MFC Roadmap

## The work being reviewed

**Chosen approach:** Parent item "HREC approval & data strategy — 2026 research pathway" (Roadmap This Year group) with strategy document linked in Detail column and 5 subitems for five identified actions (Adelaide email, UTAS/SWSLHD confirmation, academic collaborator identification, data policy/consent form draft, privacy-law question to legal).

**Objective:** Integrate complex research (evidence, reasoning, confidence notes, ranked options) into a trackable action workflow, keeping research retrievable and execution actionable.

---

## Independent alternative approach: Decision-Indexed Strategy Structure

**Name:** Decision-Indexed Strategy Structure (DISS)

**Architecture:**

1. **Parent item:** "HREC pathway — three-track strategy awaiting confirmation"
   - Status: "Strategy complete; awaiting Hunter decision on recommended approach"
   - Detail column: Abbreviated three-point recommendation
     - Track 1: University of Adelaide (free collaboration pathway)
     - Track 2: UTAS + South Western Sydney LHD (fee-for-service, $1,000–unknown cost range)
     - Track 3: Direct academic collaborator search (bypasses external-org fee wherever it applies)
     - One sentence per track: rationale and target outcome
   - Document link: Full 224-line working-strategy as evidence base
   - Timeline: Research complete, decision pending (no projected date until confirmed)

2. **First subitem (strategic decision, not action):**
   - Title: "Hunter decision: Confirm three-track parallel approach?"
   - Type: Decision checkpoint (not action)
   - Assignee: Hunter
   - Dependencies: None (unblocking item)
   - Must complete: Before operational actions (1–5) escalate beyond draft

3. **Remaining 5 subitems (operational actions):**
   - Same five actions as chosen approach
   - Status/timeline: Blocked until decision confirmed
   - Assignees and acceptance criteria as already defined

**What changes in typical workflow:**
- A reader scanning the board sees immediately: "This is awaiting a strategic decision"
- The decision is explicit and trackable (Hunter can check off "Confirm approach" once read)
- The three tracks are visible as chosen recommendation, not inferred from action titles
- Actions follow visibly from decision, creating a decision→action chain on the board itself

---

## Comparison: Chosen vs. Alternative

| Dimension | Chosen (Parent + 5 Actions) | Decision-Indexed Alternative |
|---|---|---|
| **Strategy visibility on board** | Document link in Detail field (one click minimum) | Recommendation summary in parent detail (inline, zero clicks) |
| **Decision recording** | Implicit (no recorded Hunter confirmation on board; research speaks for itself) | Explicit (Hunter decision item: "Confirm approach?") |
| **Actionability** | Immediate; five actions ready to execute or assign | Gated; five actions visible but logically downstream of decision |
| **Dependency modeling** | None; actions appear independent | Clear; decision is explicit prerequisite for action escalation |
| **Research-to-action tracing** | Weak; doc link is the only bridge | Strong; three tracks are the bridge between research and actions |
| **Reasoning accessibility** | Requires reading 224-line document to understand why these five actions | Readable from board: "Oh, we're pursuing three tracks, and these actions support each" |
| **Change adaptability** | Document edit + separate action revision (two places to update if approach changes) | One place: revise decision item and parent recommendation if approach shifts |
| **Onboarding friction** | New team member must read doc to understand context | New team member sees context inline; doc is supporting evidence, not essential preread |
| **Board narrative clarity** | "Do these 5 things" | "We decided to do this; here are the 5 things that follow" |
| **Structural complexity** | Minimal (six items: parent + 5 actions) | One extra item (seven items: parent + decision + 5 actions) |
| **Monday.com UX dependency** | Works in any Monday.com board | Depends on conditional visibility/gating (if Monday lacks this, decision item just floats alongside actions) |

---

## Adversarial argument: Why the chosen approach is suboptimal

**Frame:** The chosen approach prioritizes *execution readiness* at the cost of *decision transparency*.

**The problem:**

1. **Strategy is documentation, not decision.** The 224-line working-strategy document holds the reasoning—ranked options, universities checked, confidence ratings, three recommended tracks—but it is *not a decision record*. The research recommends three parallel tracks, but there is no board-level artifact showing Hunter has confirmed that approach. If Hunter reads the research and decides differently (e.g., "actually, pursue only Adelaide, not SWSLHD as fallback"), that decision lives nowhere except in a new edit to the doc or an offboard conversation. The board shows five actions, but not the strategic choice that unlocked them.

2. **Hierarchy is inverted.** The board structure is action-primary: five subitems are the visible content; the strategy is a detail-field link. But research should drive actions, not the reverse. A reader of the board learns "do these five things" first and only later discovers *why* if they click through. The architectural primacy should flow from strategy→decision→action, not float as action+detail-link.

3. **Reasoning is segregated from execution.** Someone executing action 1 (Adelaide email) or action 2 (UTAS/SWSLHD confirmation) might not know they're part of a *three-track strategy*. They see five independent action items. If Adelaide responds slowly, there's no visible board state indicating "that's why we're also pursuing UTAS/SWSLHD in parallel." The connection exists in the doc, not in the board's working view.

4. **No decision checkpoint.** The working-strategy is marked "awaiting-committee" and clearly states "No D- or M- identifier reserved." The decision to proceed on three tracks is not yet formally recorded. The Monday.com board doesn't surface this gap. A structure that includes an explicit "Confirm approach?" decision item forces that clarity: is the recommendation confirmed, or still under Hunter review? The current approach assumes offline confirmation.

5. **Onboarding cost.** If a second team member comes on board to execute actions 2–4 (UTAS confirmation, academic search, data policy draft), they see five action items and a document link. They must read the 224-line strategy to understand *why* they're emailing UTAS specifically and what makes academic collaborator search a parallel rather than fallback option. The board tells them *what to do*, not *why*. Alternative puts the why inline.

**Strength of argument:** Medium-to-strong. The argument holds if the decision needs to be visible and if new team members will be executing. It weakens if Hunter is the executor and offline confirmation is acceptable.

---

## Specific findings and classifications

### Finding 1: No explicit board-level decision gate on three-track approach
**Classification:** `GENUINE_FOUNDER_DECISION`

**Detail:** The strategy document recommends three parallel tracks. The current approach treats this as implicit instruction; the Decision-Indexed Alternative makes it an explicit, checkable decision item. This is a real trade-off:
- **Current:** Strategy is documented; confirm offline; execute when ready. Simpler, less board noise.
- **Alternative:** Strategy is documented; confirm on board as a visible item; execute when decision is recorded. More transparent, more formal.

Neither is wrong. The choice depends on Hunter's preference: Does the board need to show strategic decisions, or is research-complete-then-execute sufficient? This is genuinely his call.

---

### Finding 2: Research document is detail-field context, not primary board content
**Classification:** `NOTED_NOT_BLOCKING`

**Detail:** The 224-line document is linked in the parent item's Detail column. It is retrievable and accessible. However, it is architecturally subordinate to the action list. For execution, this is fine. For explaining strategy to someone unfamiliar with the research, it creates friction. Not a blocker; the document is there. Just suboptimal for clarity.

---

### Finding 3: Three parallel tracks are implicit, not explicit on the board
**Classification:** `NOTED_NOT_BLOCKING`

**Detail:** The five action items include two separate universe pathways (Adelaide email + UTAS/SWSLHD confirmation) and academic partner search, but the *three-tracks-in-parallel* strategic frame is not explicit. The board shows five separate actions; it does not say "these five actions support three coordinated strategic tracks." A reader scanning only the board might think they are five sequential or independent items. If you read the research, the frame is clear. If you don't, it's unclear. No blocker for Hunter-as-executor; friction for team expansion.

---

### Finding 4: Data governance work is embedded in action list, not separated as system work
**Classification:** `GENUINE_FOUNDER_DECISION`

**Detail:** The HREC research document ends with "The bigger picture — data handling beyond this one pilot" and recommends six steps (data policy, consent form, technical controls, breach response, data-sharing agreement, governance framework). These appear as line items 4 and 5 in the "This month" actions. Current approach treats them as part of HREC work.

A structurally stronger alternative might separate these:
- **Workstream A:** HREC pathway (resolve university/fee-for-service pathway, actions 1–3)
- **Workstream B:** Org-wide data governance (policy, consent, technical controls, actions 4–6, plus future 5–6)

This clarification is a genuine founder choice: Are HREC approval and org-wide data governance one coordinated workstream, or two distinct but interdependent ones? The current approach assumes one. The alternative suggests two, with shared timing but separate leadership/accountability.

---

### Finding 5: No formal decision record if approach changes
**Classification:** `NOTED_NOT_BLOCKING`

**Detail:** If Hunter reads the research and decides to revise the three-track approach (e.g., "pursue only Adelaide for now, not UTAS as parallel"), the current structure has no formal place to record that change. It would be a doc edit. A Decision-Indexed structure with an explicit decision item would force that decision to be either confirmed or revised and re-recorded. Not a blocker for current work; relevant if approach shifts.

---

## One-line verdict

**Functional and actionable as-is; Decision-Indexed Alternative would surface strategic choice and decision transparency, but the trade-off between simple-flat and strategy-indexed is a genuine founder preference, not a structural defect.**

---

## Confidence and reasoning

- **High confidence on comparison:** Both approaches are architecturally sound and will execute. The difference is visibility and governance, not capability.
- **Medium confidence on adversarial framing:** The strongest argument against the chosen approach assumes a team expansion or formal decision-tracking need. If Hunter is the executor and informal confirmation is acceptable, the argument weakens.
- **Genuine uncertainty:** Whether Monday.com supports conditional visibility/gating for the Decision-Indexed approach. If it doesn't, the decision item becomes just another action item, and the structural gain is lost.

---

## Recommendation for Hunter

Neither approach is broken. If clarity on strategic choice and decision-gating matters (especially if this work will distribute across the team), the Decision-Indexed Alternative is worth the one-item overhead. If simplicity and implicit-but-documented approach is preferred, the current structure is correct. The call is genuinely his.
