---
mfc_topic: measurement
artifact_role: review
canonical_source: 60-projects/measurement-strategy-v1/39-THE-FINAL-QUESTION-SET-2026-09-21.md
created: 2026-09-22
status: findings_applied
task_id: "513463574c581548-2026-09-22T13:44:58.307812+10:00"
specialist_id: A-11
execution_mode: bounded_specialist_review
pack_version: '2026-08-13'
pack_state: baseline_equipped
task_packet: 90-meta/full-permanent-specialist-bench-v1/routing-records/packets/2026-09-22-head-of-research-advisor-position-verification.yml
artifact_reviewed: 60-projects/measurement-strategy-v1/form-set-v2/index.html
---

# A-11 — is every advisor position actually in the built forms

## Bounded question
Are `AG-541` to `AG-566`, plus the five decisions taken in the 21 September meeting, present in the
**rendered HTML** rather than only in the design document?

## Position
**Nineteen of the twenty-six are implemented and verified in the HTML. Seven are not form changes
at all** — they are written answers owed to Debra Fidler or an action owed to a rights-holder, and
forcing them into a pass/fail on the markup would misreport them. **Three genuine gaps**, all now
fixed.

## Sources reviewed
All six files in `60-projects/measurement-strategy-v1/form-set-v2/` ·
`50-authority/advisor-guidance-register/REGISTER.md` (`AG-541`–`AG-566`, read for exact wording) ·
`60-projects/measurement-strategy-v1/38-DECISIONS-AFTER-ADVISOR-MEETING-2026-09-21.md` ·
`60-projects/measurement-strategy-v1/39-THE-FINAL-QUESTION-SET-2026-09-21.md`

## Professional principles applied
A position implemented in the source and absent from the rendered output is not implemented. That
distinction is the whole reason this check reads HTML. A suggestion considered and declined by a
ruling is not a gap, and must not be reported as one.

## Evidence strength and limitations
Every "implemented" verdict is backed by the literal string from the file, with its filename.
**No participant has used these forms**, so nothing here speaks to comprehension. Scope was the
closed list of 26 positions plus 5 meeting decisions; nothing outside it was examined.

## Verified implemented
`AG-546` one product one name — zero hits for *this hour* across all six ·
`AG-548`/`AG-558` the Introduction pre-measure exists, three baseline items ·
`AG-549` Form 2 carries no unanchored moment item ·
`AG-552` *Prefer not to say* on every scored MFC item, correctly absent from WHO-5 and IMTTAQ ·
`AG-553` every list runs least→most, escapes below a visible rule ·
`AG-556` *Privacy officer* on all six, zero hits for *privacy contact* ·
`AG-557` the repeat-orientation line on forms 1, 3, 4, 5 ·
`AG-559` *practise*, zero hits for *try to practise* ·
`AG-560` the near-duplicates unified, byte-identical across forms 1 and 3 ·
`AG-561` both carried stems appear exactly once per form, identically, across all six ·
`AG-562` Form 4 carries the moment definition ·
`AG-563` zero hits for *out of nowhere*, Radar referent named ·
`AG-564` *if*, not *when*, on all three conditionals · `AG-565` the rep named in each stem ·
plus all five meeting decisions: language drift, crisis lines off (zero hits for Lifeline, 13 11 14
or crisis anywhere), the pre-measure, privacy officer, and the publication clause on the first
screen of all six.

## Gaps found, and fixed
1. **`AG-545` — the "other, please specify" route had a label and no input.** The field printed as
   the literal string `[short text]`. **A participant could tick the option and had nowhere to say
   where.** The same generator gap left `[long text, optional]` unrendered on four further items,
   so five free-text answers could not be given at all.
2. **`AG-566` — Form 3's gloss printed after the item that uses the term.** The source described
   the gloss as sitting *above item 6* while physically placing it below, and the build follows
   position, not prose. A participant met *mental rep* in a stem and met its definition on the next
   screen.
3. **Outside the AG list but fatal to two items MFC would otherwise report:** Form 1's comprehension
   items rendered the **scoring key to the participant** — the correct option carried a ✔ and the
   word *keyed*. Both items were void as built.

## Alternatives considered
Checking the design document instead of the HTML — **rejected, and it is the whole point.** Two of
the three gaps below exist only in the rendered output; the markdown specifies both correctly.

## Recommendation
Fix the three gaps, which are generator defects rather than design defects, and send Debra the
seven written answers. **Nothing here requires reopening a question the advisors approved.**

## Strongest objection
That reporting seven positions as *not applicable to a form* lets MFC mark them closed without
answering them. **It does not, and they are listed by number below so they cannot quietly lapse** —
`AG-543` in particular is the question from the person whose research standard MFC is borrowing.

## Not a form change, and still owed
`AG-541` storage and access · `AG-542` a written risk position · `AG-543` what de-identification
actually is, in prose — **the one she flagged as her own comprehension failure, and she is the
person whose approved research required total de-identification** · `AG-544` email security, tied
to the retention decision · `AG-554` the subscale-validity answer, which exists in the record and
has not been sent · `AG-555` nobody has taken Eimear up on approaching the WHO-5 rights-holder,
while the measure sits in two live forms.

## Considered and declined by ruling, not missed
`AG-547` items 4 and 6 stay categorical · `AG-551` the recall item stays open-ended, because
recognition is a different task from recall and the item is the control that keeps the
self-reported clarity item honest.

## Partial
`AG-550` — Form 3's realism item is now five-point, matching its neighbour, and §0.1–0.3 apply
globally. **The set still mixes four-, five- and six-point structures across forms**, which is not
her question answered at the granularity she asked.

## What would change this view
A rebuild from a changed source. Any hand-edit to the HTML, which would bypass the drift check.

## Adjacent specialist or human boundary
The seven written answers are Hunter's to send. The WHO-5 approach is Eimear's. Nothing here is
ethics approval, clinical assurance, or evidence that a participant understands any question.

## Proposed learning
Candidate: a position can be correctly implemented in a source document and absent from the
artefact a person actually touches. **Verification has to read the thing the participant sees.**
