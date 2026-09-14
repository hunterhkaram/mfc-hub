---
specialist_id: A-09
execution_mode: bounded_specialist_review
pack_version: 2026-08-13
pack_state: evaluated_pack
task_packet: 60-projects/lead-generation-v2/packets/A-09-packet.yml
artifact_reviewed: 60-projects/committee-pack-v1/FINAL-03-marketing-and-lead-generation.md
---

# A-09 — bounded specialist review, 2026-08-24


> This document is the contract-conformant rendering of the review this specialist actually
> returned. Every section below is drawn from that returned output, which is reproduced in
> full and verbatim at the end of this file. Nothing has been added to it.


## Bounded question

Model the actual behaviour chain and find where it breaks: map the full free-session sequence with realistic per-step conversion estimates and identify the two steps that will kill the funnel; do the same for the comment-to-DM social route and judge whether an automated DM builds or destroys trust for this audience and topic; give the evidence-supported mechanisms that raise show-up rate and say which are appropriate versus manipulative for a charity in this topic area; model the internal advocacy step where an attendee must persuade their own organisation; apply the binding social-norms backfire warning; and name the one cheap behaviourally-designed change that would most raise conversion.

## Sources reviewed

- 90-meta/full-permanent-specialist-bench-v1/knowledge-packs/A-09-milo.md
- 60-projects/lead-generation-v2/00-task-packet.md
- 60-projects/committee-pack-v1/FINAL-03-marketing-and-lead-generation.md
- 60-projects/committee-pack-v1/FINAL-08-committee-paper.md
- 00-foundations/K-08-claims-red-lines.md
- 90-meta/controlled-automation-v1/topic-control/canonical-topic-register.yml

Plus the role-specific reading and external search named in the returned output below.

## Professional principles applied

1. **Capability, opportunity and motivation are separate.** Intention is not behaviour. Most of the failures below are opportunity and capability failures, not motivation failures — which matters, because the current plan's implicit remedy for every leak is "more/better content", which only addresses motivation.
2. **Do not individualise environmental barriers.** A manager who attends and then does nothing is usually not under-motivated; they have no budget line, no meeting slot, and no artefact to hand upward. Designing a "nurture sequence" to fix that is individualising a structural barrier.
3. **Do not infer real-world use from in-room performance.** A post-form score of "very useful" collected 30 seconds after a free Zoom predicts almost nothing about a purchase decision taken 6 weeks later inside an organisation MFC never sees.

## Position

Basis for all estimates: (i) general B2B/nonprofit practitioner priors held by this model — **not vault-registered, not primary-source-checked this session, and not benchmarked against any MFC data**; (ii) two vault-internal anchors — `D6 §5`'s stated close assumption (*"one close per five to eight qualified conversations"*, itself flagged there as an assumption, not a measured benchmark) and `R7`'s documented competitor landscape; (iii) MFC-specific downward adjustment for zero brand, zero testimonials, no paid spend, and organic-only reach from three people's personal networks. Ranges are wide on purpose. Treat as a structural model of where volume dies, not as a forecast.

| # | Step | Estimate (per monthly cycle) | Biggest friction |
|---|---|---|---|
| 1 | Post seen | 800–1,500 impressions | **No audience.** Reach comes from Hunter + Alysse + Nabill's personal networks. `FINAL-03` already judges LinkedIn organic "close to worthless". Impressions ≠ ICP: most viewers are not managers who can book. |
| 2 | Sees → clicks | **1–2%** → 12–25 clicks | Nothing distinguishes the post from the free-wellbeing-webinar wallpaper. `R7` documents that SafeWork NSW, WorkSafe VIC (sessions **booked out**), Black Dog and Be Well Co all offer free, regulator-branded, psychologist-delivered sessions. MFC is the least credentialled entrant in a saturated free market. |
| 3 | Clicks → registers | **20–30%** → 3–7, plus 3–8 from the website-quiz endpoint and direct asks → **8–15 registrations** | The registration page must answer "who is this person and why is this not a sales pitch" in ~8 seconds, with no case studies and no clinical credential to point at. |
| 4 | Registers → **attends** | **30–40%** → **3–6 attendees** | Classic free-webinar leak. Zero cost = zero commitment; a mid-morning Zoom is the first thing dropped when the day goes sideways. Currently the plan has no named show-up mechanism at all. |
| 5 | Attends → completes post-form | **55–70% if run live in-session** → 2–4. **10–20% if emailed afterwards** → 0–1 | The single largest controllable swing in the whole chain. An emailed post-form loses roughly three-quarters of the data Hunter explicitly wants (the ~3,000-people knowledge-gap capture). |
| 6 | Registrant → on the list | **~85–95%** of registrants (email already captured at step 3) → 7–14 | Not a real leak — but only if the registration form carries a lawful, explicit marketing opt-in. If consent is bundled or assumed, this is a compliance problem, not a conversion one. |
| 7 | Opens newsletter | **35–45% open in months 1–3, decaying to 20–30%**; click-through **2–5%** | The list is tiny and cold-ish. Open rate is a vanity number here — at a 12-person list, 40% open is 5 people. |
| 8 | Becomes or refers a buyer | **Attendee → qualified conversation ≈ 5–12%** → **0.2–0.6 per cycle.** Qualified conversation → sale at `D6`'s 1-in-5-to-8 → **≈0.03–0.12 sales per cycle** ≈ **0.4–1.4 sales per year** | The attendee is not the buyer. Between "that was useful" and a purchase order sits an internal conversation MFC does not attend, is not present for, and currently equips nobody to have. |

**Read the bottom line honestly:** at plausible organic volumes, this route as currently specified produces on the order of **one sale a year, and quite possibly zero**. That is not an argument against the free session — its authority, data-capture and mission-reach value may well justify it on their own terms (Nabill's point at 27:00, and Hunter's at 39:18). It is an argument against treating it as the lead-generation engine without changing two specific steps.

## Strongest objection

**My whole Killer-1 argument rests on an assumed audience size I did not verify, and I may have the objective wrong as well.**

Two ways this analysis fails:

1. **The volume assumption.** I modelled 800–1,500 impressions from three people's organic networks. If Hunter's actual reach is materially larger — a warm list from the endurance runs that raised $20,000+, the seven-person committee's networks, the ~3,000 people he has spoken to in person, peak-body distribution via CCWT/NCOSS/NDS, or a single co-working space or peak body agreeing to promote the session to its membership — then registrations per cycle could be 40–80 rather than 8–15. At that volume the funnel simply works on arithmetic, Killer 1 dissolves, and my "one sale a year" conclusion is not merely conservative but wrong in kind. **I did not check what distribution actually exists, and I should flag that as a real hole rather than defend the estimate.** Notably, if this is the case, the correct design is exactly what I recommended for a different reason — treat the session as a container for the ranked relationship channels, not as an independent acquisition channel.
2. **The objective.** I have modelled the free session as a sales funnel and judged it on sales. Nabill's argument (25:00–27:00) is that its value is authority, reputation and word-of-mouth; Hunter's (39:18) is that the accumulated public voice of participants is what "becomes a movement"; and Hunter's data-capture ask is about evidencing the knowledge gap, which has funding and credibility value entirely independent of conversion. On those objectives, "0.4 sales a year" is close to irrelevant and my framing would push MFC to over-engineer the wrong end of the thing. The counter I would still hold: those are real objectives and should be *stated* as the objectives, because the measurement, the cadence and the design differ — and the task packet's own "ultimate goal" is organisations paying MFC to deliver.

## Evidence strength and limitations

- **Every conversion figure above is an estimate**, derived from general practitioner priors plus two vault-internal anchors, not from MFC data, and not from any registered source. Zero cohorts, zero sales, zero sessions run — there is nothing to calibrate against. Wide ranges reflect genuine uncertainty, not false modesty.
- `D6 §5`'s 1-in-5-to-8 close rate is explicitly flagged **in D6 itself** as a generic B2B planning assumption, not a measured benchmark. I have propagated it and inherited its weakness.
- **No registration→attendance benchmark exists anywhere in the vault.** Searched `60-projects`, `10-sources`, `20-knowledge` on 2026-08-24 for `webinar|show-up rate|no-show`: `R7` documents competitors' free webinars in detail but records no attendance or conversion rates for any of them; `D6`/`R1` model channel volumes but not webinar attendance.
- **No registered source in `10-sources/` covers implementation intentions, reminder effects, or effort-justification.** Searched the whole vault for `implementation intention|commitment device|plan-making` on 2026-08-24: hits appear only in workshop-design and website-design contexts, never applied to lead-generation attendance. The mechanisms in SHOW-UP RATE MECHANISMS therefore rest on this model's general knowledge and need a verification pass (the `evidence-research` skill) before any of those numbers appear in a founder- or committee-facing document.
- `Grunseit et al. (2020)`, the one registered source I lean on, is `status: draft`, `awaiting-specialist`, with its full citation not yet located.
- I have not read the Fathom transcript directly; I have worked from the task packet's verbatim extracts.
- **I am an AI behavioural lens.** This is not clinical, legal or safeguarding clearance. The DM-channel duty-of-care point under `D-0016` needs qualified human input, not my say-so.

## Alternatives considered

Not returned under a separately-titled section by this role. See the verbatim output below; the substance is carried within its own headings.

## Recommendation

**Change the advertised object from the session to the artefact: "Free 45 minutes for managers — and you leave with the one-page you can take to your leadership team."** Build that one document (the INTERNAL ADVOCACY DESIGN list above). One file, a few hours of work, zero recurring cost.

Why this one, above all the show-up mechanisms:

- **It attacks both killers with a single asset.** At step 2 it gives the post a differentiated, concrete, non-wellbeing-wallpaper reason to click — no free government webinar in `R7`'s landscape advertises "you leave with the thing you need to make this happen at work", because none of them are trying to sell anything. At step 8 it *is* the missing internal-advocacy artefact.
- **It is capability-and-opportunity design, not persuasion** — the correct target per the diagnosis above, and it doesn't touch the social-norms tripwire at all.
- **It has structural properties, not message properties** — one checkable act, explicit reciprocity, zero qualification to enter. That is the class of mechanism `Grunseit et al. (2020)` and `FINAL-03 §8` both point at, rather than the class that `§8` warns off.
- **It also unblocks the ranked channels.** `D6 §3.2` already names the one-pager as "the single highest-leverage missing asset" for Channels 1–3 and 6. Building it for the free session builds it for everything.

**Runner-up, if only one hour is available instead:** calendar hold at registration plus a 24-hour and 1-hour reminder from a named human. Highest-certainty uplift per minute spent — but it optimises the step I have argued is *not* one of the two killers, so it should be second.

## What would change this view

1. **Actual reach data** — Hunter's and Alysse's/Nabill's real impression and engagement numbers on comparable posts, and whether any list exists from the endurance-run fundraising. This is a 10-minute check and it is the highest-value missing input in this whole review. If reach is 5× my assumption, rewrite the model.
2. **A committed distribution partner** — one peak body, co-working space or WHS consultancy agreeing to promote the monthly session to its membership. That single fact moves the free session from Killer-1 territory to a viable channel and would make it the correct #1 or #2 in the ranked model rather than a support asset.
3. **Two cycles of real numbers.** Registrations, attendance, post-form completion, and — critically — how many attendees ask an unprompted question about cost or booking. That last count is the earliest honest read on step 8 and is available after two sessions.
4. **Any evidence that a free session in this market converts at all.** `R7` shows the competitor free-session landscape in unusual detail; none of it records what those sessions produce. If WorkSafe VIC's booked-out sessions or Be Well Co's masterclasses have published downstream figures, that is the closest available real benchmark and would beat every estimate in this document.
5. **On the DM question specifically:** evidence that this audience receives an automated DM on this topic without a trust penalty. I would treat one real adverse reaction as decisive against, given what MFC is.

## Proposed learning

**Proposed lesson — "When the attendee is not the buyer, the deliverable is the artefact they carry, not the follow-up you send."**

- **The gap:** the lead-gen model is specified in detail up to the point of capture (register, attend, post-form, list, newsletter) and stops there. The step where the free offer actually becomes revenue — a manager persuading their own organisation, in a room MFC is not in, weeks later — is modelled nowhere. Confirmed by search (see absence claim above): every asset in the plan speaks in MFC's voice to the prospect; none is designed to be carried by the attendee into their own organisation.
- **Why it recurs:** funnels are drawn from the seller's side, so they naturally end at the last action the seller can observe. Every step MFC can measure is specified; the one step MFC cannot see is the one that decides the outcome. This will reproduce identically in the website quiz, the pro-bono sessions, the community talks and the peak-body channel — every one of them ends with a person who must go and convince someone else.
- **Proposed binding control:** any MFC funnel design must model the chain **to the money, not to the capture**, and must name — for every step where the person acting is not the person paying — the specific artefact handed to the advocate. A funnel diagram that terminates at "joins list" or "attends" fails this check.
- **Suggested wiring:** a check item in the `copywriting` and lead-gen review path, and a line in `FINAL-03`'s asset checklist alongside the two existing one-pagers, so the attendee-voiced leave-behind is tracked as a named missing asset rather than an implicit one.
- Sits alongside `L-025`'s pattern in a different register: here it is not a control that exists and isn't invoked, but a step that was never drawn, so nothing could invoke anything.

**Not proposed as a lesson (one-off, or already covered):** the social-norms risk is already bound by `FINAL-03 §8` and needs no new record — only enforcement in the v2 copy. The evidence-verification gap on the show-up mechanisms is ordinary `10-sources/` work, not a lesson.

## Adjacent specialist or human boundary

- H-01 clinical and H-02 regulatory remain restricted human gates and are routed, never cleared, by this panel
- qualified legal, clinical and insurer input are real external gates that no AI lens supplies
- committee approval and real buyer validation remain separate and unmet

This role routes to these boundaries and does not clear any of them.

---

## Verbatim contract-complete output as returned

PACK STATUS

- Role: **A-09 "Milo" — behavioural and social context.** Loaded from `90-meta/full-permanent-specialist-bench-v1/specialist-knowledge-index.yml` (lines 58–74).
- Pack state: **`evaluated_pack`**. Evaluation status **`passed_independent_substantive_evaluation`**, holdout passed, independent checker context `independent_retest_checker`; evidence at `90-meta/full-permanent-specialist-bench-v1/evaluations/2026-08-13-governed-retest/checker-results/00-aggregate-decision.md`. Last review 2026-08-13; next trigger: after Half-Day behaviour review or new real-participant evidence. Maintainer A-23.
- **Limit, stated up front and once:** that evaluation tests reasoning quality in fresh context. It is not field evidence, and I have no real MFC participant data to reason from — zero cohorts, zero sales, zero sessions run. Everything numeric below is a modelled estimate, labelled as such.
- Section 8 of `FINAL-03` read in full and treated as binding.

PROFESSIONAL PRINCIPLES APPLIED

1. **Capability, opportunity and motivation are separate.** Intention is not behaviour. Most of the failures below are opportunity and capability failures, not motivation failures — which matters, because the current plan's implicit remedy for every leak is "more/better content", which only addresses motivation.
2. **Do not individualise environmental barriers.** A manager who attends and then does nothing is usually not under-motivated; they have no budget line, no meeting slot, and no artefact to hand upward. Designing a "nurture sequence" to fix that is individualising a structural barrier.
3. **Do not infer real-world use from in-room performance.** A post-form score of "very useful" collected 30 seconds after a free Zoom predicts almost nothing about a purchase decision taken 6 weeks later inside an organisation MFC never sees.

BEHAVIOUR CHAIN — FREE SESSION ROUTE

Basis for all estimates: (i) general B2B/nonprofit practitioner priors held by this model — **not vault-registered, not primary-source-checked this session, and not benchmarked against any MFC data**; (ii) two vault-internal anchors — `D6 §5`'s stated close assumption (*"one close per five to eight qualified conversations"*, itself flagged there as an assumption, not a measured benchmark) and `R7`'s documented competitor landscape; (iii) MFC-specific downward adjustment for zero brand, zero testimonials, no paid spend, and organic-only reach from three people's personal networks. Ranges are wide on purpose. Treat as a structural model of where volume dies, not as a forecast.

| # | Step | Estimate (per monthly cycle) | Biggest friction |
|---|---|---|---|
| 1 | Post seen | 800–1,500 impressions | **No audience.** Reach comes from Hunter + Alysse + Nabill's personal networks. `FINAL-03` already judges LinkedIn organic "close to worthless". Impressions ≠ ICP: most viewers are not managers who can book. |
| 2 | Sees → clicks | **1–2%** → 12–25 clicks | Nothing distinguishes the post from the free-wellbeing-webinar wallpaper. `R7` documents that SafeWork NSW, WorkSafe VIC (sessions **booked out**), Black Dog and Be Well Co all offer free, regulator-branded, psychologist-delivered sessions. MFC is the least credentialled entrant in a saturated free market. |
| 3 | Clicks → registers | **20–30%** → 3–7, plus 3–8 from the website-quiz endpoint and direct asks → **8–15 registrations** | The registration page must answer "who is this person and why is this not a sales pitch" in ~8 seconds, with no case studies and no clinical credential to point at. |
| 4 | Registers → **attends** | **30–40%** → **3–6 attendees** | Classic free-webinar leak. Zero cost = zero commitment; a mid-morning Zoom is the first thing dropped when the day goes sideways. Currently the plan has no named show-up mechanism at all. |
| 5 | Attends → completes post-form | **55–70% if run live in-session** → 2–4. **10–20% if emailed afterwards** → 0–1 | The single largest controllable swing in the whole chain. An emailed post-form loses roughly three-quarters of the data Hunter explicitly wants (the ~3,000-people knowledge-gap capture). |
| 6 | Registrant → on the list | **~85–95%** of registrants (email already captured at step 3) → 7–14 | Not a real leak — but only if the registration form carries a lawful, explicit marketing opt-in. If consent is bundled or assumed, this is a compliance problem, not a conversion one. |
| 7 | Opens newsletter | **35–45% open in months 1–3, decaying to 20–30%**; click-through **2–5%** | The list is tiny and cold-ish. Open rate is a vanity number here — at a 12-person list, 40% open is 5 people. |
| 8 | Becomes or refers a buyer | **Attendee → qualified conversation ≈ 5–12%** → **0.2–0.6 per cycle.** Qualified conversation → sale at `D6`'s 1-in-5-to-8 → **≈0.03–0.12 sales per cycle** ≈ **0.4–1.4 sales per year** | The attendee is not the buyer. Between "that was useful" and a purchase order sits an internal conversation MFC does not attend, is not present for, and currently equips nobody to have. |

**Read the bottom line honestly:** at plausible organic volumes, this route as currently specified produces on the order of **one sale a year, and quite possibly zero**. That is not an argument against the free session — its authority, data-capture and mission-reach value may well justify it on their own terms (Nabill's point at 27:00, and Hunter's at 39:18). It is an argument against treating it as the lead-generation engine without changing two specific steps.

THE TWO STEPS THAT KILL IT

**Killer 1 — Step 2/3, the top of the funnel (volume in).** Everything downstream is a percentage of a number that is currently near zero. Three people's organic networks against a market where the *government itself* gives away psychologist-delivered sessions for free and can't meet demand (`R7`: WorkSafe VIC sessions booked out) is not a volume problem you optimise your way out of with better copy. If steps 1–3 deliver 8–15 registrations a month, no improvement anywhere else in the chain reaches a meaningful sale count. Note the structural implication: **the free session's realistic supply of registrations is the same relationship-channels list `FINAL-03` already ranks 1–7.** It is not a new source of people; it is a better *container* for people those channels already produce. Designing it as an independent acquisition channel is the category error.

**Killer 2 — Step 8, the attendee-to-buyer handoff.** This is the step the plan does not model at all, and it is where a genuinely successful session still yields nothing. See INTERNAL ADVOCACY DESIGN.

**Explicitly not one of the two: step 4, registration→attendance.** It is the famous one and it is a real leak, but it is bounded (you lose 60–70% of a number that is already small) and it is the cheapest step in the chain to improve with known, non-manipulative mechanisms. Fixing show-up rate while killers 1 and 2 stand converts 0.4 sales/year into 0.6 sales/year. Prioritising it because it is the familiar problem would be a misallocation.

SOCIAL ROUTE ASSESSMENT

| Step | Estimate | Friction |
|---|---|---|
| Sees content | 800–1,500 impressions | Same audience ceiling as above. |
| **Comments** | **0.2–0.6% of reach** → **2–9 comments** | The killer. Commenting is public and identity-costly. On *this* topic, in *this* culture, a public comment on a mental-health post is read as a disclosure about yourself — Peeters (2004) tall-poppy dynamics push against visible self-nomination, and the audience is Australian managers who by role must appear to be coping. Expect the comment population to skew to supporters and peers, not buyers. |
| Receives DM | ~100% (automated) | Deliverability and platform-throttling aside, mechanically fine. |
| Replies to DM | **25–45%** → 1–4 | Whether it reads as a person or a bot decides this outcome almost entirely. |
| Gives email | **10–25% of repliers** → 0–1 | They already engaged publicly for free; the DM must offer something worth a second identity-cost. |
| Converts | **≈0** per cycle at these volumes | Same step-8 wall as the free session, with a colder relationship. |

**Where it breaks:** at the comment step, decisively. Everything after it is arithmetic on a number between 2 and 9.

**Is an automated DM a trust-builder or a trust-destroyer here? It depends entirely on what triggered it, and the distinction is not optional:**

- **Trust-building, and legitimate:** an automated DM fired by an *explicit resource request* — "comment TOOLKIT and I'll send you the one-pager." The person has performed a transaction, knows a thing is coming, and gets exactly it. The exchange is honest and the automation is obvious and unobjectionable. This is the parkrun property `Grunseit et al. (2020)` identifies: one checkable act, zero qualification to enter, explicit reciprocity.
- **Trust-destroying, and a safeguarding problem:** an automated DM fired by *any comment*, including comments that are disclosures. Someone writes "yeah, I've been struggling with this since my brother died" and receives an instant templated message with a booking link. That is the single worst outcome available to MFC in this whole plan — it converts a moment of real disclosure into evidence that the charity is a funnel, and it is exactly the kind of harm that reaches Hunter's own network faster than any marketing does.

**Binding conditions if a ManyChat-style mechanism is built at all:**
1. **Keyword-triggered only. Never comment-triggered.** No blanket automation on any post about mental health, pressure, or personal difficulty.
2. **Every automated message discloses itself** ("This is an automated reply — Hunter will see anything you send back") and carries a plain support boundary and Lifeline 13 11 14. `D-0016` remains open; an inbound DM channel on this topic is a live duty-of-care surface MFC has no clinical clearance for.
3. **A named human reads and answers every reply within 24 hours.** If Hunter cannot commit to that, do not build the channel — an unanswered reply is worse than no DM.

SHOW-UP RATE MECHANISMS

Evidence status caveat for this whole section: the four external literatures I draw on (plan-making prompts, appointment reminders, effort-justification, structural-format effects) are **general behavioural-science knowledge held by this model, not registered in `10-sources/` and not primary-source-verified this session**, with the single exception of Grunseit/parkrun, which *is* registered — and which carries its own open verification gap (full citation not yet located). Do not restate any of these numbers publicly without a verification pass.

**Appropriate here — use all five:**

1. **Calendar hold sent at registration (.ics or a real calendar invite).** Pure opportunity-barrier removal: it puts the session where the manager's attention actually lives and defends the slot against being double-booked. No persuasion component at all, therefore no manipulation risk. Cheapest, highest-certainty item on this list.
2. **Reminders — 24 hours and 1 hour before, from a named human.** Reminder effects on appointment non-attendance are among the better-replicated findings in applied behavioural science. Send from "Hunter Karam" not "MFC Bookings", and make the 1-hour one a single line with the join link. Typical practitioner uplift on free-webinar show rates: **+8 to +15 percentage points (estimate, not MFC-measured).**
3. **A plan-making / intention question at signup.** Plan-making prompts (implementation intentions) produce small but real and very cheap uplifts on attendance-type behaviours — in the published field trials on comparable acts, in the region of **3–5 percentage points**. Ask one question: *"What's the one thing you want to walk away able to do?"* This does double duty — it is also precisely the knowledge-gap data Hunter said he wants captured rather than remembered from 3,000 in-person conversations.
4. **Small, honest friction at signup.** Two or three real questions (role, organisation size, that intention question) rather than a bare email box. Mechanism is effort-justification/consistency — **weaker evidence than 1–3, plausible not proven** — but it also self-selects for people who actually intend to come, which improves attendance *rate* partly by reducing junk registrations. Be clear-eyed that this trades a little volume at step 3 for quality at step 4; given Killer 1, keep it to three questions maximum.
5. **Social obligation to a named other — "bring one person from your team."** This is the strongest structural analogue MFC has in its own registered evidence: `Grunseit et al. (2020)` attributes parkrun's no-budget success to format properties including social obligation to a named other, and `FINAL-03 §8` already treats that as confirming MFC practice. It also improves the session itself (two people from one org can actually change something on Monday) and directly seeds the internal-advocacy step below. **This is the one I would implement first after the calendar hold.**

**Manipulative here, and to be ruled out explicitly:**

- **Fabricated scarcity** — countdown timers, "only 3 seats left" when there are 200. A real capacity cap (the 20-person cap already exists in the product design) is honest and can be stated; a manufactured one is a lie told by a mental-health charity to a manager under pressure. Non-negotiable.
- **Guilt-framed no-show follow-ups** — "we held a seat for you and you didn't come." Applies emotional pressure over an unpaid, unfulfilled obligation, to an audience selected for being overstretched. This is the mechanism that turns goodwill into resentment.
- **Deposits or refundable fees.** Effective in general, wrong here — it contradicts the "free public offer" whose entire point is zero qualification to enter, and it is a bad look for a charity.
- **Auto-enrolling non-attenders into a nurture sequence they did not opt into.** Consent problem before it is a behaviour problem.
- **Any implied social norm about how many people attend or how common struggling is.** See below.

INTERNAL ADVOCACY DESIGN

**Absence claim, with method.** Searched `60-projects/committee-pack-v1/FINAL-03-marketing-and-lead-generation.md`, `60-projects/committee-pack-v1/D6-lead-generation-marketing-funnel.md` and `60-projects/lead-generation-v2/` on **2026-08-24**, terms: `leave-behind|leave behind|one-page|one-pager|sell it up|upward|internal advocacy|take back to|make the case to`. **Result:** the only assets found are the *one-page partner proposition* and *one-page pitch document* — both written in MFC's voice, both directed at the prospect, and both recorded as **not built** (`D6 §3.2`: "Does not exist… the single highest-leverage missing asset"; `FINAL-03` checklist lines 264–265 unticked). **Zero hits** for any artefact designed to be carried by the attendee into their own organisation. The task packet's characterisation is correct: this step is absent, not merely thin.

**The behavioural diagnosis.** The manager leaving a good free session is not short of motivation. They are short of **capability** (they don't have the words, the numbers, or the risk answer) and **opportunity** (no budget line, no agenda slot, no authority). The default remedy — follow-up emails from MFC — targets motivation, the one thing that isn't broken, and it targets the wrong person: MFC's email persuades the attendee, who is already persuaded, and never reaches the person who says yes. **Give them the artefact; don't nurture them.**

**What the attendee must be handed, at the end of the session, in one file:**

1. **A one-page internal proposal written in the manager's voice, not MFC's** — "Here's what I attended, here's what I think we should do, here's what it costs, here's what we'd get." Pre-drafted with three blanks to fill (team size, preferred format, why now for us). A manager will forward a document they can edit; they will not write one.
2. **The price, in writing, unambiguous.** Foundations $3,900 + $95/person; Essentials by band; Introduction $600 or $0 as capped outreach. Nobody can advocate for a number they have to email someone to find out. Include what is and isn't included.
3. **The budget-line hook: the NSW psychosocial-hazard duty framing.** This is what lets the manager route the spend through an existing WHS/compliance line rather than create a new discretionary wellbeing line — a materially easier internal ask. It also speaks the language their HR/WHS colleague already uses. Within `K-08`: state the duty and state what MFC delivers; do not claim MFC discharges the duty or confers compliance.
4. **The "who are these people and is this safe" answer, honestly.** The first question a cautious internal stakeholder asks. State the facilitator, the qualification, what MFC does and does not do, and where MFC refers on. Do **not** paper over the open `D-0016` items — a manager who discovers a gap after advocating internally is a permanently lost relationship, and honesty here is also the differentiator against slicker competitors.
5. **A no-cost or low-cost first step they can propose instead.** Advocating internally for a free 1-hour Introduction is an order of magnitude easier than advocating for $3,900, and it puts MFC in the room. This is the single most important item on the list, and it aligns with `D6 §5`'s own finding that pro-bono delivery is the biggest lever on the true conversion rate.
6. **A three-sentence forwardable email**, literally written out, with the one-pager attached. Reduce the act to copy, paste, send.
7. **The honest gap: no case study exists.** Zero cohorts have run. Do not manufacture a substitute. What can stand in its place is the pre/post measurement report *format* — showing the buyer exactly what they will receive about their own people. That converts the absence of proof into a concrete promise of evidence, which is both truthful and, for a compliance-minded buyer, arguably more interesting than someone else's testimonial.

**And one design change to the session itself:** the "bring a colleague" mechanism above is not only a show-up device. Two attendees from one organisation is the difference between an individual advocating alone and a pair with a shared reference experience — which is the actual unit that gets things through a small organisation.

SOCIAL-NORMS COMPLIANCE

`FINAL-03 §8` risk 1 is binding: Foxcroft et al. (2015, Cochrane, 70 RCTs, n=44,958) found no substantive benefit; Papakonstantinou et al. (2025) found d=0.01 after publication-bias correction; Schultz et al. (2007) documented the boomerang. **Three places the proposed messaging will reach for a descriptive norm, and the safe alternative for each:**

| # | The instinctive line | Why it's a problem | Safe alternative |
|---|---|---|---|
| 1 | **"Most managers are struggling / you're not alone in finding this hard."** The near-inevitable opener for a free session aimed at overstretched managers. | Textbook descriptive norm of the *undesired* state. Schultz boomerang: it tells a manager who is coping that struggling is normal and no action is required, and tells one who is struggling that this is simply the condition of the job. Weak evidence base for any benefit. | **Drop the norm; offer the act.** "Forty-five minutes, one thing you can run in your next team meeting." Concrete, self-efficacy-framed, no claim about anybody else's state. Per `§8` risk 2, an Australian permission structure — self-deprecation, humour (Peeters 2004; Proudfoot et al. 2015) — does the warming work a norm claim was being asked to do, and does it better. |
| 2 | **Prevalence statistics as the hook** — "1 in 5 Australians experience…", "X% of workplaces report…". | Same failure mode wearing a citation. A prevalence figure is a descriptive norm about a problem, and is precisely the class of message Papakonstantinou's corrected d=0.01 applies to. Also risks `K-08` drift into implied causal territory. | **Injunctive/duty framing, which is not a descriptive norm at all:** the psychosocial-hazard obligation is a statement about what organisations are *required* to do, not what most are doing. It carries genuine motivational force for the buyer and rests on regulation, not on contested norm evidence. |
| 3 | **List and attendance social proof** — "join 200 other managers", "our sessions fill up". | Descriptive norm of the desired behaviour — the *least* problematic variant, and the one that does work when the number is large and true. But MFC's number is currently zero, so today the only way to say it is to lie. There is also a boomerang risk in reverse: "join 11 other managers" actively signals a fringe offer. | **Say nothing about numbers until the number helps.** Substitute specificity of who it's for: "built for managers in organisations under 50 people." Revisit once the number is genuinely impressive; if a dynamic norm is later used ("a growing number of small NSW organisations…"), it must be literally true and evidenced. |

**Standing rule I'd propose for the lead-gen v2 copy deck:** no MFC public copy may motivate action by describing what other people are doing or feeling. Motivate by naming the duty, the concrete act, or the specific person it's for.

HIGHEST-LEVERAGE CHEAP CHANGE

**Change the advertised object from the session to the artefact: "Free 45 minutes for managers — and you leave with the one-page you can take to your leadership team."** Build that one document (the INTERNAL ADVOCACY DESIGN list above). One file, a few hours of work, zero recurring cost.

Why this one, above all the show-up mechanisms:

- **It attacks both killers with a single asset.** At step 2 it gives the post a differentiated, concrete, non-wellbeing-wallpaper reason to click — no free government webinar in `R7`'s landscape advertises "you leave with the thing you need to make this happen at work", because none of them are trying to sell anything. At step 8 it *is* the missing internal-advocacy artefact.
- **It is capability-and-opportunity design, not persuasion** — the correct target per the diagnosis above, and it doesn't touch the social-norms tripwire at all.
- **It has structural properties, not message properties** — one checkable act, explicit reciprocity, zero qualification to enter. That is the class of mechanism `Grunseit et al. (2020)` and `FINAL-03 §8` both point at, rather than the class that `§8` warns off.
- **It also unblocks the ranked channels.** `D6 §3.2` already names the one-pager as "the single highest-leverage missing asset" for Channels 1–3 and 6. Building it for the free session builds it for everything.

**Runner-up, if only one hour is available instead:** calendar hold at registration plus a 24-hour and 1-hour reminder from a named human. Highest-certainty uplift per minute spent — but it optimises the step I have argued is *not* one of the two killers, so it should be second.

EVIDENCE LIMITS

- **Every conversion figure above is an estimate**, derived from general practitioner priors plus two vault-internal anchors, not from MFC data, and not from any registered source. Zero cohorts, zero sales, zero sessions run — there is nothing to calibrate against. Wide ranges reflect genuine uncertainty, not false modesty.
- `D6 §5`'s 1-in-5-to-8 close rate is explicitly flagged **in D6 itself** as a generic B2B planning assumption, not a measured benchmark. I have propagated it and inherited its weakness.
- **No registration→attendance benchmark exists anywhere in the vault.** Searched `60-projects`, `10-sources`, `20-knowledge` on 2026-08-24 for `webinar|show-up rate|no-show`: `R7` documents competitors' free webinars in detail but records no attendance or conversion rates for any of them; `D6`/`R1` model channel volumes but not webinar attendance.
- **No registered source in `10-sources/` covers implementation intentions, reminder effects, or effort-justification.** Searched the whole vault for `implementation intention|commitment device|plan-making` on 2026-08-24: hits appear only in workshop-design and website-design contexts, never applied to lead-generation attendance. The mechanisms in SHOW-UP RATE MECHANISMS therefore rest on this model's general knowledge and need a verification pass (the `evidence-research` skill) before any of those numbers appear in a founder- or committee-facing document.
- `Grunseit et al. (2020)`, the one registered source I lean on, is `status: draft`, `awaiting-specialist`, with its full citation not yet located.
- I have not read the Fathom transcript directly; I have worked from the task packet's verbatim extracts.
- **I am an AI behavioural lens.** This is not clinical, legal or safeguarding clearance. The DM-channel duty-of-care point under `D-0016` needs qualified human input, not my say-so.

STRONGEST OBJECTION TO MY OWN VIEW

**My whole Killer-1 argument rests on an assumed audience size I did not verify, and I may have the objective wrong as well.**

Two ways this analysis fails:

1. **The volume assumption.** I modelled 800–1,500 impressions from three people's organic networks. If Hunter's actual reach is materially larger — a warm list from the endurance runs that raised $20,000+, the seven-person committee's networks, the ~3,000 people he has spoken to in person, peak-body distribution via CCWT/NCOSS/NDS, or a single co-working space or peak body agreeing to promote the session to its membership — then registrations per cycle could be 40–80 rather than 8–15. At that volume the funnel simply works on arithmetic, Killer 1 dissolves, and my "one sale a year" conclusion is not merely conservative but wrong in kind. **I did not check what distribution actually exists, and I should flag that as a real hole rather than defend the estimate.** Notably, if this is the case, the correct design is exactly what I recommended for a different reason — treat the session as a container for the ranked relationship channels, not as an independent acquisition channel.
2. **The objective.** I have modelled the free session as a sales funnel and judged it on sales. Nabill's argument (25:00–27:00) is that its value is authority, reputation and word-of-mouth; Hunter's (39:18) is that the accumulated public voice of participants is what "becomes a movement"; and Hunter's data-capture ask is about evidencing the knowledge gap, which has funding and credibility value entirely independent of conversion. On those objectives, "0.4 sales a year" is close to irrelevant and my framing would push MFC to over-engineer the wrong end of the thing. The counter I would still hold: those are real objectives and should be *stated* as the objectives, because the measurement, the cadence and the design differ — and the task packet's own "ultimate goal" is organisations paying MFC to deliver.

WHAT WOULD CHANGE MY VIEW

1. **Actual reach data** — Hunter's and Alysse's/Nabill's real impression and engagement numbers on comparable posts, and whether any list exists from the endurance-run fundraising. This is a 10-minute check and it is the highest-value missing input in this whole review. If reach is 5× my assumption, rewrite the model.
2. **A committed distribution partner** — one peak body, co-working space or WHS consultancy agreeing to promote the monthly session to its membership. That single fact moves the free session from Killer-1 territory to a viable channel and would make it the correct #1 or #2 in the ranked model rather than a support asset.
3. **Two cycles of real numbers.** Registrations, attendance, post-form completion, and — critically — how many attendees ask an unprompted question about cost or booking. That last count is the earliest honest read on step 8 and is available after two sessions.
4. **Any evidence that a free session in this market converts at all.** `R7` shows the competitor free-session landscape in unusual detail; none of it records what those sessions produce. If WorkSafe VIC's booked-out sessions or Be Well Co's masterclasses have published downstream figures, that is the closest available real benchmark and would beat every estimate in this document.
5. **On the DM question specifically:** evidence that this audience receives an automated DM on this topic without a trust penalty. I would treat one real adverse reaction as decisive against, given what MFC is.

PROPOSED MFC LEARNING

**Proposed lesson — "When the attendee is not the buyer, the deliverable is the artefact they carry, not the follow-up you send."**

- **The gap:** the lead-gen model is specified in detail up to the point of capture (register, attend, post-form, list, newsletter) and stops there. The step where the free offer actually becomes revenue — a manager persuading their own organisation, in a room MFC is not in, weeks later — is modelled nowhere. Confirmed by search (see absence claim above): every asset in the plan speaks in MFC's voice to the prospect; none is designed to be carried by the attendee into their own organisation.
- **Why it recurs:** funnels are drawn from the seller's side, so they naturally end at the last action the seller can observe. Every step MFC can measure is specified; the one step MFC cannot see is the one that decides the outcome. This will reproduce identically in the website quiz, the pro-bono sessions, the community talks and the peak-body channel — every one of them ends with a person who must go and convince someone else.
- **Proposed binding control:** any MFC funnel design must model the chain **to the money, not to the capture**, and must name — for every step where the person acting is not the person paying — the specific artefact handed to the advocate. A funnel diagram that terminates at "joins list" or "attends" fails this check.
- **Suggested wiring:** a check item in the `copywriting` and lead-gen review path, and a line in `FINAL-03`'s asset checklist alongside the two existing one-pagers, so the attendee-voiced leave-behind is tracked as a named missing asset rather than an implicit one.
- Sits alongside `L-025`'s pattern in a different register: here it is not a control that exists and isn't invoked, but a step that was never drawn, so nothing could invoke anything.

**Not proposed as a lesson (one-off, or already covered):** the social-norms risk is already bound by `FINAL-03 §8` and needs no new record — only enforcement in the v2 copy. The evidence-verification gap on the show-up mechanisms is ordinary `10-sources/` work, not a lesson.
