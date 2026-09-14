# Archive and supersession policy

Status: controlled operational policy  
Owner: Hunter  
Automation boundary: enforced for registered current artifacts and canonical-source declarations

## Purpose

Keep useful MFC history available in Obsidian without allowing an old name, draft, export or abandoned direction to be mistaken for current organisational truth.

## Default treatment

1. Decisions, foundations, evidence records and change history stay in their existing paths. When their authority changes, record the supersession in the controlling decision/register; do not hide the historical chain by moving it.
2. A current source with stale terminology is reconciled or renamed in place. Archive is not a substitute for correcting an active source.
3. Move a file into a project-local `archive/` folder only when it is wholly superseded or retired, has no live operational responsibility, and retaining it beside current candidates creates retrieval risk.
4. Never archive generated Hub pages. Change their source/register and regenerate them.

## Required archive metadata

Every newly archived Markdown artifact must identify:

```yaml
lifecycle_status: superseded # or retired
do_not_use_as_current: true
superseded_by: path/to/current-source.md
archived_at: YYYY-MM-DD
archive_reason: concise reason
```

If there is no successor, use `superseded_by: none` and explain why the work was retired.

## Retrieval and authority rule

Archived material is historical evidence only. It may be inspected for provenance, lessons or explicit historical comparison. It must not be selected as the authority for current recommendations, builds, exports or Hub projections. The active source must come from the canonical topic register or a controlling decision.

The artifact guard denies new current candidates that declare an `/archive/` canonical source. The topic-register validator also rejects an archived source whose role/status claims that it is current or generated.

## Moving an artifact

Before moving a file:

1. Resolve its current topic and successor.
2. Add the required metadata and update the topic register/source links.
3. Search inbound links and update any current operational reference.
4. Move it only into that project's local `archive/` folder.
5. Record a `corrected` or `reconciled` topic receipt. The receipt regenerates and verifies the Hub.

No bulk archival is authorised by this policy. Archive candidates are assessed individually so history, live links and source authority are preserved.
