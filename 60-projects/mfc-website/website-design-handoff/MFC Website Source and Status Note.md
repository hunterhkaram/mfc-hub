---
title: "MFC Website Source and Status Note"
type: source-and-status-note
subtype: website-design-handoff
version: "1.0"
status: prepared-not-approved
authority_ref: D-0031
mandate_ref: M-031
owner: hunter
maintained_by: ai
created: 2026-07-31
last_retrieval: 2026-07-31
confidentiality: internal
scope: "Records what was read, at what depth, what was inspected read-only, what is confirmed, what remains assumed, and what depends on a future technical inspection. Establishes no authority and approves nothing."
---

# MFC Website Source and Status Note

This note exists so that every statement in the Website handoff package can be traced to something that was actually read, and so that anything not read is visible rather than implied. It approves nothing and changes nothing.

## 1. Repository state at the start of this objective

| Item | Value |
|---|---|
| Worktree | `/Users/hunterkaram/Documents/MFC-founder-decision-rationale-system-v1` |
| Branch | `ops/founder-decision-rationale-system-v1` |
| Branch HEAD at start | `eac3253dfc48d22db1e5e07820c0980d33afbe2d` |
| `main` HEAD | `538bd9c35931c5891ee7c7a8e151cd84b1bbbca2` |
| Working tree at start | Clean |
| Commits after `eac3253` on the branch | None |
| Branch merged into `main` | No |
| Hunter decisions recorded | None |
| Stage 11 | Not started |
| Superseding objective | None found |

All ten pre-edit verification checks required by the objective were performed and all ten matched the expected state. No later Website work was found that would supersede this objective, and no recorded Hunter decision conflicts with this brief.

## 2. Controlling sources read directly this session

| Source | Location | Depth |
|---|---|---|
| MFC Public Messaging Source Library, tab 00I "Home Page Locked Copy - 23 July 2026" | Drive `1MyOBjAGKl6dfWduJd7obGnstexjUDF5iI2JYhqHTK-w` | 100 per cent, verbatim, retrieved and extracted in full |
| Same file, tab 00E "Hunter Decision List, Current" | Same | 100 per cent |
| Same file, tab 00F "Controlled Glossary v1" | Same | 100 per cent |
| Same file, tab 00G "Website Messaging Decision Gate v1" | Same | 100 per cent |
| Same file, tab map and structure for all 21 tabs | Same | Header scan; tabs 00A, 00B, 00C, 00D, 00H and 01 to 09 located but not read in full this pass |
| MFC Audience Intelligence System, Master sheet, tab START - Website Audiences | Drive `1-j01MZC1eZHW2wnWQ0rshPNMrKmTskaC9bStbm3NEGc` | WA01 to WA07 rows read in full, all 21 columns; plus Default Panel, Selection Rules, Review Workflow and Master Prompt |
| MFC kernel K-00 to K-11 | Repository `00-foundations/` | 100 per cent, all twelve notes |
| Website verified baseline | Repository `60-projects/founder-decision-rationale/32-website-verified-baseline.md` | 100 per cent |
| Website Founder Decision Report V3 | Repository `.../42-website-founder-decision-report-v3.md` | 100 per cent |
| Website technical appendix V3 | Repository `.../42b-website-technical-appendix-v3.md` | 100 per cent |
| Founder Decision Agenda V1.1, Website and cross-project sections | Repository `.../MFC Founder Decision Agenda V1.1.md` | Part 1 (FD-01 to FD-04), FD-07, Part 4 (FD-15 to FD-17) and Part 5 (CB-01 to CB-07) read in full |
| 27 July 2026 Hunter and Alysse discussion | Repository `.../08a-27-july-transcript-source-record.md` and `.../08b-transcript-reconciliation-matrix.md` | 100 per cent of both; the underlying Fathom transcript was read in full by the prior objective and is relied on through those two controlled records |
| Current sitemap and page-purpose record | Repository `60-projects/mfc-website/03-sitemap-and-page-purpose-matrix.md` | 100 per cent |
| Wix inspection findings, prior pass | Repository `60-projects/mfc-website/14-wix-inspection-findings.md` | 100 per cent |
| Brand and visual experience principles | Repository `60-projects/mfc-website/stage-3/09-brand-visual-experience-principles.md` | 100 per cent |
| Dashboard and exact resume state | Repository `90-meta/Current State and Next Action.md` | Current-stage block and resume statement read; the full 215 KB history was not re-read |

## 3. Read-only Website and platform inspection

**Method.** Wix connector `GetSiteContext` for platform metadata, and browser inspection of the published site for content, routes, navigation and mobile rendering. **No write call of any kind was made at any point.** Nothing was edited, published, created, submitted, configured or contacted. No form was submitted. No setting was changed.

**Environment: WIX STUDIO PREVIEW / EDITOR-SIDE CURRENT SITE, not LIVE PRODUCTION.** All inspection was of a `wixstudio.com` test address on a free plan. **MFC's production domain was never inspected**, so nothing in this package describes MFC's live public website. Hunter has confirmed Share Your Rep is not live.

**Confirmed platform facts.** One site, ID `8639395c-8d07-45de-8ea8-4a3c7fdac647`, name "(CURRENT) Site", reachable at `https://contact435546.wixstudio.com/mfc-test`. Free plan. Wix Studio editor. Velo enabled. Created 14 June 2026, updated 25 July 2026. Locale en, country AU, timezone Australia/Sydney, currency AUD. Apps installed: Promote SEO, Wix Blog, Wix Forms, Wix Invoices, Wix Members Area.

**Confirmed page inventory.** Twenty-two routes resolve, including Home, Radar, Quick Check In, Skill Assessment, Learn the Basics, Start Here, Try a Moment, Our Mission, Start Building, Human Operating System, Methods tools supports and foundations, Foundational Human Skills, Share Your Rep and Stop. Shift. Do., plus `/blog` and a members-area route.

**Findings recorded in full in the handoff.** The seven findings H1 to H7 are stated in the primary handoff and in the Build Readiness Register. In summary: every page slug is an auto-generated duplicate chain with no human-readable URL; the current Wix site homepage does not implement the locked copy; Start Building exists in draft, correcting four prior passes that recorded it absent; the draft Start Building page carries visible copy defects; the Human Operating System is publicly reachable; Share Your Rep is built to an operational state while formally deferred, in a non-live environment; and mobile rendering shows no horizontal overflow, a correct viewport meta tag, a single H1 and alt attributes on all images, but no meta description.

**Not inspected, and therefore untested rather than adequate.** The Wix editor's own page tree; hidden or unpublished pages; CMS and content-collection configuration; form field configuration and submission destinations; Members Area configuration and whether visitor accounts are enabled; Velo code; analytics configuration; colour-contrast and keyboard-navigation conformance; the Drive-side website audit spreadsheet's page-by-page inventory.

**Conclusions that depend on a future technical inspection.** Whether the free plan and Velo support private per-visitor storage for saved Radar moments. Whether Wix Forms can deliver the Workshops enquiry with the required privacy handling. Whether the auto-generated slugs can be changed without breaking existing links. Whether the Members Area is a viable route to an optional account without forcing one.

## 4. Sources deliberately not re-read

The objective directed use of the minimum relevant authoritative corpus and prohibited broad rereading of unrelated Framework or Workshop files. The following were consulted through controlled repository records rather than re-retrieved from Drive, because a current, verified record already existed and re-retrieval would have added cost without adding accuracy:

- The MFC Mental Fitness Framework, relied on through kernel notes K-04 to K-08, which record it as read in full by text extraction on 26 July 2026.
- The Claims and Evidence Register, relied on through K-08, which carries the standing warning that all eight board decisions remain pending.
- "Why Mental Fitness, Why Now", relied on through the Website verified baseline, which read approximately 56 per cent directly.
- The Year 1 Diffusion and Participation Strategy, relied on through the Website verified baseline, which read it in full.
- "Building Mental Fitness, The Practical Pathway". **Update, 31 July 2026: this gap is closed.** The controlling copy, Drive ID `1NPnwqQ04REMAmkYxGG0q88pnReE7stlF`, last modified 23 July 2026, was read in full in the final assurance pass. It was previously the weakest link in the chain. The direct read **confirmed and strengthened** the assumption that Start Building is an assembly job, and surfaced three matters not previously visible: the Pathway carries pre-lock definitional wording; it teaches the Human Operating System as Part 1 starter content, which is material to FD-07; and it names Return, Reflection and Repair but not Reward. See `Practical Pathway Website Reconciliation.md`.
- The full MFC Website UX Foundation and Expert Review Brief, approximately 202,000 characters, relied on through the Stage 2 records that already summarise its Gate 2 output.
- Fathom transcripts other than 27 July, relied on through the Stage 2 Fathom source log.

## 5. Known conflicts carried, not resolved here

| Conflict | Status |
|---|---|
| C-01, vision wording with or without "for everyone" | Open. The locked homepage uses the "for everyone" form, so the Website inherits a resolved-in-practice position while the underlying conflict remains |
| C-14, superseded mission in both Strategic Direction files | Open. The Website uses the current mission as locked in HOME-01-BODY-01 |
| C-13, three live definition formulations | Open. Correction bundle item CB-01 addresses it. The Website uses the locked 20 July definition throughout |
| C-22, five-skill ordering discrepancy | Open. The Website uses the locked homepage order: Notice, Shift, Choose, Focus, Connect |
| Five foundational skills versus five public skills | Open, and flagged by the locked homepage's own record as an open controlled issue. FD-04 |
| Claims Register adoption | All eight board decisions BD-01 to BD-08 remain pending. No red-line claim is board-approved |
| Movement versus programmes weighting | Open. Not an architecture question, and the four parallel routes serve both readings |

## 6. What this package changes

Nothing. No MFC authority, product, page, copy, setting or record outside this handoff directory has been changed. The locked homepage wording is reproduced exactly and is unchanged. No Hunter decision has been recorded. No implementation has occurred. The branch remains unmerged.

## 6a. Final assurance pass, 31 July 2026

After the package was released at commit `f04c17a`, a bounded assurance pass closed four gaps. The controlling Practical Pathway was read directly. The final released copy deck received its own isolated independent review against a confirmed hash. The published homepage was compared section by section against the locked authority. The live Share Your Rep feature was assessed read-only. **No live change of any kind was made in that pass**, no form was submitted and no personal submission was accessed. Records: `Practical Pathway Website Reconciliation.md`, `Final Released Copy Deck Review Record.md`, `Published Homepage Authority Comparison.md`, `Share Your Rep Governance and Risk Brief.md`, `Targeted Correction Record.md`.

## 7. Retrieval date

31 July 2026. Any statement about what MFC's records currently say is bounded to that date.
