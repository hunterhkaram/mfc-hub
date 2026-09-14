---
mfc_topic: system-continuity
artifact_role: review
canonical_source: 90-meta/controlled-automation-v1/topic-control/canonical-topic-register.yml
status: active
---

# Organisation-wide continuity and propagation control

This is a bounded control layer inside the existing MFC intelligence system. It is not a new source of organisational truth: decisions and operational documents retain their authority. The register maps 15 controlled topics and nine organisational-domain groups to controlling sources, operational destinations, present readiness, accountability, conflicts, assurance evidence, open gates and strongest next action. The prompt router uses that map to reconstruct active state before broad discovery.

The register also contains one ranked `portfolio` view for cold-start questions such as “what should MFC be working on?” This distinction matters: a well-developed or authorised workstream is not automatically the most urgent organisation-wide priority. Portfolio ranking must compare deadlines, reversibility, safety gates, readiness and strategic leverage, and must be refreshed at its recorded trigger.

For every registered topic, completion requires the existing operational destinations to be updated and any external revision/readback to be recorded. An accepted reconciliation receipt automatically regenerates the existing Hub and runs its integrity check; `--no-regenerate` exists only as a batch escape hatch before a final receipt performs the check. A new Markdown or HTML artifact for a registered topic must either be an allowed projection/review or declare its relationship to the existing canonical source. Archived sources remain historical evidence and cannot authorize a current candidate or projection; see `ARCHIVE-AND-SUPERSESSION-POLICY.md`. These controls reduce parallel drafts and stale retrieval; they cannot observe unconnected work outside Claude Code.

Routing records entry into a topic. Material progress, completion, waiting, blockage, external action and later Hunter correction require an evidence-bearing reconciliation receipt in the existing loop log. The closure gate compares both the registered local-source fingerprint and the complete topic-record fingerprint with the latest receipt. Regenerating the Hub alone cannot make a stale semantic state current.

Assurance requirements are objective-specific. Claude determines the relevant professional lenses, executes them and records their evidence; Hunter does not select the agent checklist. AI specialist assurance is always distinct from qualified-human approval and real-user evidence. A named role without an executed artifact cannot produce a pass.

The Hub is a generated projection. Its topic fingerprints prove it was generated from the current register and registered local-source state; they do not prove that the underlying claims or human approvals are true. Its home page exposes domain coverage, external observability and the human/founder decision queue. Topic pages expose current state, responsibility, lifecycle, history, conflicts, assurance evidence and gates. Drive, Wix, Monday and other authenticated systems remain receipt-based: the agent doing the work must inspect them through an available connector, update the existing destination, then record the returned revision and read it back. A local hook cannot independently authenticate to those systems.
