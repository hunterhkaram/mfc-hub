---
mfc_topic: measurement
artifact_role: review
canonical_source: 60-projects/measurement-strategy-v1/39-THE-FINAL-QUESTION-SET-2026-09-21.md
created: 2026-09-23
status: findings_applied
specialist_id: A-11
execution_mode: bounded_specialist_review
pack_version: '2026-08-13'
pack_state: baseline_equipped
task_packet: 90-meta/full-permanent-specialist-bench-v1/routing-records/packets/2026-09-23-head-of-research-wording-reverification.yml
artifact_reviewed: 60-projects/measurement-strategy-v1/form-set-v2/index.html
---

# A-11 - are all the advisor wording positions implemented, right now

## Bounded question
Hunter will not start his full review until he has a straight answer: are every Eimear Quigley and
Debra Fidler position specifically about **question wording** implemented in the forms as they
stand?

## Position at the time of review
**No. Sixteen of seventeen implemented, one question stem broken, and it broke in the em-dash
rewrite.**

**Form 3 item 8** rendered as:

> *"Earlier today you chose a real moment from your own life to work on. Thinking about that moment
> How realistic does it feel to actually do something different in it?"*

The dash after *moment* was removed and **nothing replaced it**, so two clauses ran together with no
connector. **The only one** - every rendered string on all six forms was scanned for a lowercase
word followed by a capitalised word with no punctuation between, and this was the single hit.

## Why this was re-checked rather than taken from the earlier pass
These positions were verified against the built forms on 22 September and reported implemented.
**Then the wording changed**: forty-five phrase-level rewrites to remove em dashes, several landing
inside question stems; the consent panel rewritten; the code removed from both Introduction forms; a
stem-detection fix that changed how seventeen questions render. **A verification that predates those
edits is not evidence about the current files.** `L-045`.

## Evidence strength and limitations
Every claim is a literal string matched in a named rendered file, not a reading judgement. **No
participant has read these questions cold**, and per Hunter's ruling of 2026-09-22 no comprehension
test will be run, so nothing here speaks to whether a stem is understood as intended - only to
whether the advisors' positions are present.

## Strongest objection
That this duplicates the verification of 22 September. **It does not, because the thing verified
then no longer exists**: forty-five phrase-level rewrites landed after it, several inside question
stems. The re-run found a broken stem, which settles whether it was worth doing.

## Sources reviewed
The six rendered `form-*.html` files in `60-projects/measurement-strategy-v1/form-set-v2/`, built
22 Sep 23:22 · `50-authority/advisor-guidance-register/REGISTER.md`, each entry read in full rather
than from summary · `38-DECISIONS-AFTER-ADVISOR-MEETING-2026-09-21.md` ·
`39-THE-FINAL-QUESTION-SET-2026-09-21.md`

## Professional principles applied
A wording verification has to read the rendered artefact, because the participant reads the
artefact. A position settled the other way by a ruling is not an unimplemented position and must
not be reported as one.

## Verified implemented, with the literal string
`AG-545` other-specify · `AG-546` one product one name · `AG-549` moment anchored before the first
item on Form 2 · `AG-552` *Prefer not to say* on every MFC closed item, last, below the escape rule,
correctly absent from WHO-5 and IMTTAQ · `AG-553` every list least to most · `AG-557` the repeat
orienting line · `AG-559` *practise* not *try to practise* · `AG-560` the near-duplicates unified ·
`AG-561` verbatim repeats, confirmed **independently of the build check** · `AG-562` moment and
mental-rep reminders before the Radar items on Form 4 · `AG-563` Radar referent named, *"came out of
nowhere"* zero hits · **`AG-564` survived the rewrite**, all three conditionals read *if* ·
**`AG-565` survived**, *happen* gone as the referent · `AG-566` the rep named at items 8 to 10 ·
language drift, one construct one wording, with the forward-looking pair byte-identical on Forms 3
and 4.

## Settled the other way by ruling, not unimplemented
`AG-547` Form 1 items 4 and 6 stay categorical, and `AG-551` the recall item stays open-ended.
Both recorded at `38-DECISIONS` §4, *"Two items that are format, not wording"*.

## Partial, and the document says so
`AG-550`. §0.1 to §0.3 fix the scales; **the Kirkpatrick-level granularity she asked for is not
claimed as closed**, and §5 records it as open rather than ticking it.

## Two further findings, not question wording
1. **Form 1 contradicted itself about the code.** The panel said *"There is no code on this form"*
   while the detail page still described building a six-character code from three questions, and the
   thank-you screen still asked for *"your six characters"*. **On a form with no code field, a
   participant could not reconcile that.**
2. *"This hour"* survives on Form 1's consent panel, where Form 3 says *"the session"*. Form 1 **is**
   the one-hour Introduction, so it is accurate rather than drifted, but it is the one place the old
   word is still on screen.

## Alternatives considered
Reporting the sixteen as a pass and listing the broken stem as a note - **rejected.** The question
asked was whether all of them are implemented, and one stem a participant cannot parse is not a
footnote to that answer.

## Recommendation
Repair the stem, split the detail page so the Introduction variant describes no code, and make the
thank-you screen truthful per form. **Then the answer is yes.**

## What would change this view
A further edit to the source that is not followed by a rebuild and a re-read. That is the failure
mode this check exists to catch, and it has now caught it twice.

## Adjacent specialist or human boundary
Advisor sign-off on the final set is Debra Fidler's and Eimear Quigley's. Nothing here is that.

## Proposed learning
Candidate: a global find-and-replace across participant-facing prose needs a clause-level read
afterwards, not only a count of what was replaced. The em-dash sweep reported 45 of 45 applied and
was correct about that, while leaving one stem ungrammatical. **Counting the edits is not reading
the result.**
