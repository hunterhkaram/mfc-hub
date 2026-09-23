---
mfc_topic: operations-governance
artifact_role: review
canonical_source: 60-projects/measurement-strategy-v1/25-EMAIL-CAPTURE-RULING.md
created: 2026-09-23
status: findings_applied
specialist_id: A-07
execution_mode: bounded_specialist_review
pack_version: '2026-08-13'
pack_state: baseline_equipped
task_packet: 90-meta/full-permanent-specialist-bench-v1/routing-records/packets/2026-09-23-head-of-digital-email-list-storage.yml
artifact_reviewed: 60-projects/measurement-strategy-v1/25-EMAIL-CAPTURE-RULING.md
---

# A-07 - where the email list lives and what keeps it apart

## Bounded question
If MFC holds participant email addresses to send and chase Form 4, where do they live, who can
reach them, and what must be true to satisfy `AG-195`?

## Position
**A separate Google Sheet file in an MFC-owned Workspace account, shared with nobody, two columns,
no code column. Reminders sent by plain BCC, no mail-merge. Deletion driven by a calendar event
created in the same sitting as the cohort tab. $0 above what MFC already pays.**

**Google Workspace with restricted sharing genuinely satisfies `AG-195` as Debra stated it**, and
nothing beyond it is proposed.

## Sources reviewed
`60-projects/measurement-strategy-v1/25-EMAIL-CAPTURE-RULING.md` · `38-DECISIONS` §3 ·
`form-set-v2/config.js`, `form-set-v2/backend/Code.gs`, `form-set-v2/README.md` ·
`50-authority/advisor-guidance-register/REGISTER.md` - `AG-195`, `AG-016`, `AG-194`

## Professional principles applied
A control that depends on someone remembering is not a control. A promise printed to a participant
constrains the architecture, not the other way round.

## Evidence strength and limitations
No cohort has run and no list exists yet. The recommendation is against the platform as configured
today; a change of platform changes the deletion surface.

## A separate file, not another tab
Sharing is per-file, everyone with the responses Sheet gets every tab in it, and a single lookup
inside one file is the easiest join in the world. **Separate files mean separate access lists,
separate deletion, and a deliberate cross-file export that nobody does by accident.**

## What "encryption" means here
⚑ **Access, not cryptanalysis.** `AG-195` reads *"as long as it's encrypted and no one can see it"*
- one requirement, not two - and in the university context Debra is describing it is shorthand for
a locked drawer. **Nobody is attacking Google's storage layer**; the realistic failure is a file
that got link-shared or a copy on a laptop.

So: MFC-owned account rather than a personal one, **two-factor on it**, restricted sharing, link
sharing off, no CSV exports. **That is the whole answer, and all of it is free.**

## Alternatives considered
⛔ Client-side encryption, a password-protected spreadsheet, an encrypted volume, Workspace CSE -
**all rejected as invented gates.** No advisor, law or licence asked for them, `L-088` and §12 both
bite, and **a password-protected file that must be unlocked to send a reminder is a file that gets
copied to the desktop "just this once."**

⛔ **Mail-merge rejected**, not on taste. Mailchimp or YAMM adds a third processor, turns open and
click tracking on by default - the join path, reintroduced by a checkbox - personalises links by
default, and creates a deletion surface outside Google that the calendar event would have to
remember separately.

⛔ **An Apps Script deletion trigger rejected.** Twenty lines, and it would work. But it runs
unattended on an account whose grant expires, deleting data, with nobody watching whether it fired,
and **a silent failure in a deletion job is indistinguishable from success.**

## What enforces never-merged
**The absence of a join key.** Contact file: email and cohort. Response data: code and cohort. The
only common field is the cohort, which is fifteen people rather than a person. **An accidental join
is not sloppy, it is impossible.** A schema, not a habit.

⚠ **Three things would break it and all three are what a well-meaning build proposes:** a per-person
link token in the URL, tracking that is on by default, and a code written beside an address so
non-responders can be chased. **MFC cannot chase a named non-responder.** The day-21 reminder goes
to everyone and says so.

## Recommendation
Build it as above and spend nothing: separate Sheet file, MFC-owned Workspace account with 2FA and
a second admin, restricted sharing, per-cohort tabs with no code column, BCC sends labelled per
cohort, and a calendar event created in the same sitting as the tab. **A cohort tab is not created
until its deletion event exists** - that pairing is the control, not the reminder. About two hours
once, fifteen minutes per cohort, ten minutes per deletion.

## Strongest objection
That Sent mail is a second copy of the addresses, so the architecture leaks by design. **True, and
there is no version of this where it does not.** The answer is to make it *one* copy, in a store the
deletion step already covers: a per-cohort Gmail label, deleted by the same event.

## What would change this view
A platform change. A cohort large enough that BCC stops being practical, somewhere past fifty.

## Two defects found
1. ✅ **Fixed the same morning.** The privacy page said *"nobody else sees it"* while `Code.gs`
   requires a second Workspace admin so MFC does not lose its data if Hunter is unavailable. **Right
   arrangement, wrong sentence**, and the promise was already printed.
2. ⛔ **Open.** The withdrawal route asks participants to email an address, a code and a cohort **in
   one message** - precisely the joined record this architecture prevents - landing in an ordinary
   inbox where by default it stays forever. The join is the accepted price of offering withdrawal;
   **nothing governs the artefact.**

## Adjacent specialist or human boundary
Whether MFC must retain proof a withdrawal was honoured is `head-of-compliance`'s to confirm. Claim
language on the privacy page is not this lens's to write.

## Proposed learning
Candidate: the strongest control in this design is the one that costs nothing to maintain, because
it is a schema rather than a rule. **Where a control can be made structural, a procedural version of
it is strictly worse even when it is easier to write down.**
