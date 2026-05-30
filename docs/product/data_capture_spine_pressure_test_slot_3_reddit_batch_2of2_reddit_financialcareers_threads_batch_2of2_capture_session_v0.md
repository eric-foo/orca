# Data Capture Spine Pressure-Test Slot 3 Reddit Batch 2of2 Capture Session v0

```yaml
retrieval_header_version: 1
artifact_role: Data Capture pressure-test capture-session artifact
scope: Records one bounded Slot 3 Reddit sub-batch capture session for five operator-supplied FinancialCareers threads preserved as local raw JSON plus existing Mechanical Source Projection working views.
use_when:
  - Checking capture-obligation discharge for Slot 3 Reddit manifest rows R06-R10.
  - Preserving per-thread source posture before any ECR receipt, Cleaning work, Judgment work, or cross-venue synthesis.
  - Running the separate LLM Capture-Visibility Checker in a fresh conversation.
authority_boundary: retrieval_only
open_next:
  - docs/prompts/data_capture_spine_pressure_test_llm_capture_visibility_checker_prompt_v0.md
  - docs/product/data_capture_spine_pressure_test_execution_authorization_v0.md
  - docs/product/data_capture_spine_pressure_test_commissioning_plan_v0.md
  - docs/product/core_spine_v0_data_capture_spine_obligation_contract_v0.md
  - docs/product/data_capture_source_access_boundary_decision_v0.md
stale_if:
  - A later capture-session artifact supersedes this exact five-thread sub-batch.
  - The current obligation contract, execution authorization, or commissioning plan is materially amended before this artifact is used downstream.
  - The owner rejects the supplied five-thread set as the authorized Slot 3 Reddit sub-batch target.
```

Status: `CAPTURE_SESSION_RECORDED_V0`.

This artifact records exactly one bounded Slot 3 Reddit sub-batch capture unit
for owner-supplied manifest rows R06-R10. The folder path supplied by the owner
uses `slot3_reddit_b1`, but the selected manifest rows are R06-R10 and were
executed here as the owner-authorized `slot_3_reddit_batch_2of2` capture unit.

## Decision Frame

- Decision question: Can Data Capture preserve the owner-supplied Reddit
  sub-batch for `non_target_us_domestic_resume_driven_interview_getting_pain`
  as raw observable plus Mechanical Source Projection working views, with enough
  categorical context for downstream receipt, without drifting into ECR schema,
  Cleaning, Judgment, or runtime/source-system design?
- Owner or owner-context: Orca owner commissioning one bounded Slot 3 Reddit
  pressure-test sub-batch under the current execution authorization.
- Consequence: This artifact determines whether the five supplied threads can be
  handed downstream as captured source slices with visible limitations, and
  whether any limitation must travel without silent normalization.
- Allowed decision verbs (if relevant): `categorical_handoff_to_ECR`,
  `visible_stop`, `visible_blocker`, `rerun`, `re-capture_posture`.
- Cutoff posture: Use the local raw JSON file state captured on 2026-05-29 as
  the per-thread cutoff state. No live Reddit fetch, continuation fetch, archive
  fetch, or external venue fetch was performed in this session.
- Downstream-use intent: Data Capture handoff only. No credibility judgment,
  exclusion, relevance ranking, source-quality scoring, ECR design, Cleaning,
  or buyer-proof synthesis is authorized here.

## Source Boundary

- Source surfaces in scope:
  - `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/raw/thread_json/reddit_t3_1t9dp7z.json`
  - `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/raw/thread_json/reddit_t3_1sbky91.json`
  - `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/raw/thread_json/reddit_t3_1ow472d.json`
  - `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/raw/thread_json/reddit_t3_184odt8.json`
  - `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/raw/thread_json/reddit_t3_1qaxpq4.json`
  - Existing Mechanical Source Projection working views under
    `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/cleansed/threads/reddit_t3_<thread_id>/`
  - Supporting selection manifest:
    `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/thread_selection_manifest.csv`
- Boundary compliance (discoverable-or-entitled / free or account-created /
  disclosable / no obvious spillover once noticed / no hard-stop access path):
  This session inspected only operator-supplied local files already inside the
  workspace. No live login, private surface, exploit path, nonconsensual
  session, no-entitlement bypass, or undisclosable method was used.
- Out-of-bounds material observed and excluded:
  - Wall Street Oasis was not attempted in this session.
  - No external Reddit live page, archive, cache, mirror, API, or search fetch
    was attempted.
  - No runtime/source-system planning, schema design, Cleaning transformation,
    or Judgment work was performed.

## Capture Mode

- Initial mode (human-led / agent-assisted / structured access / archive-history
  / automated extraction / multimodal / mixed): mixed human-led local file
  inspection plus agent-assisted local-file inspection, using existing
  Mechanical Source Projection working views bundled with the owner-supplied
  packet.
- Material mode changes during the session (each with reason):
  - None. The session stayed inside local raw-file inspection plus inspection of
    pre-existing working views.

## Per-Obligation Discharge States

| # | Obligation | State | Reason (required for non-`met`) |
| --- | --- | --- | --- |
| 1 | Commissioning Gate | met | |
| 2 | Boundary Compliance | met | |
| 3 | Capture-Event Provenance | partial | Raw file paths, file hashes, local last-write times, manifest row IDs, and current-session artifact time are visible, but the original operator acquisition event is only inferable from the 2026-05-29 delivery folder and file timestamps rather than a separately logged per-thread capture receipt. |
| 4 | Capture Mode Disclosure | met | |
| 5 | Mode-Change Rule | met | |
| 6 | Raw Observable Fidelity | partial | Thread JSON, comment hierarchy, scores, edit flags, deleted-author rows, and existing readable working views are preserved, but the two image-linked resume-review slices (`1ow472d`, `1qaxpq4`) are pointer-only to `i.redd.it` assets in the supplied packet and no local screenshot or media copy identifiable to those thread IDs was supplied. |
| 7 | Source Identity And Actor Context | met | |
| 8 | Decomposed Timing | partial | Source post creation times, visible edit times, local raw-file last-write times, and current artifact timing are visible, but there is no separately logged original operator acquisition timestamp per thread beyond the 2026-05-29 preserved file state. |
| 9 | Cutoff Posture | met | |
| 10 | Archive / Historical Posture | met | |
| 11 | Source Visibility And Access Limits | met | |
| 12 | Related Context Preservation | partial | The saved thread/reply hierarchies are preserved per slice, but the commented-on resume images for `1ow472d` and `1qaxpq4` are not locally preserved beyond URL pointers, and the five supplied slices visibly mix in-frame, adjacent-role, older, and non-US/non-domestic context that must travel as context rather than be normalized away. |
| 13 | Bundled-Offer Structure Observables | not_applicable | This capture unit is a threaded forum sub-batch, not a bundled offer, package, settlement, or multi-term counterparty proposal. |
| 14 | Capture Failure And Blocker Visibility | met | |
| 15 | Re-Capture Semantics | met | |
| 16 | Categorical Handoff Readiness | partial | The five slices can be handed downstream categorically with visible limits, but two slices lack local preservation of the linked resume image artifact and the owner-supplied set includes adjacent/non-US context that downstream must inspect without treating this sub-batch as a cleaned or normalized frame-fit set. |

## Per-Slice Posture

| Slice | Archive/history per slice | Source visibility/access per slice | Related context per slice | Re-capture relationship per slice |
| --- | --- | --- | --- | --- |
| `R06 / 1t9dp7z` | Local raw JSON snapshot preserved; local raw file last write `2026-05-29T09:09:39Z`; no separate archive/cache lookup attempted. | Self-post under `r/FinancialCareers`; public-source state preserved as local JSON only in this session; one AutoModerator notice row is visible. | Thread title and selftext are preserved; 13 comment nodes are preserved; one top-level reply is visibly edited; no deleted-author or deleted-body rows observed. | Initial preserved raw snapshot for this artifact; any later live re-capture should supplement rather than overwrite the 2026-05-29 raw state. |
| `R07 / 1sbky91` | Local raw JSON snapshot preserved; local raw file last write `2026-05-29T08:39:28Z`; no separate archive/cache lookup attempted. | Self-post under `r/FinancialCareers`; public-source state preserved as local JSON only in this session; one AutoModerator notice row is visible. | Thread title, long selftext, 86 preserved comment nodes, edited-post flag, and two edited comment rows are visible. The raw `num_comments` field shows `90`, so count vs preserved-node differences remain source-visible rather than normalized. | Initial preserved raw snapshot for this artifact; any later live re-capture should be recorded as supplement/conflict against this saved state. |
| `R08 / 1ow472d` | Local raw JSON snapshot preserved; local raw file last write `2026-05-29T09:10:04Z`; no separate archive/cache lookup attempted. | Image-linked post under `r/FinancialCareers` with `i.redd.it` URL pointer preserved in raw JSON; no separately preserved local image file identifiable to this thread ID was supplied. | Selftext plus 45 comment nodes are preserved, including 6 deleted-author rows, 1 deleted-body row, and depth through 7 levels. The commented-on resume image is pointer-only, so full visual context is limited. | Initial preserved raw snapshot for this artifact; any later visual or live re-capture should supplement the current raw-file state and remain tied back to the saved `i.redd.it` pointer. |
| `R09 / 184odt8` | Local raw JSON snapshot preserved; local raw file last write `2026-05-29T09:08:41Z`; older 2023 thread state preserved without separate archive/cache lookup. | Self-post under `r/FinancialCareers`; public-source state preserved as local JSON only in this session. | Selftext plus 67 comment nodes are preserved, including 17 deleted-author rows and 3 deleted-body rows. The slice is visibly adjacent to the frame through educational-background rejection rather than undergraduate resume review. | Initial preserved raw snapshot for this artifact; later re-capture should remain explicitly linked as older-thread supplement/conflict rather than silent replacement. |
| `R10 / 1qaxpq4` | Local raw JSON snapshot preserved; local raw file last write `2026-05-29T09:08:32Z`; no separate archive/cache lookup attempted. | Image-linked post under `r/FinancialCareers` with `i.redd.it` URL pointer preserved in raw JSON; no separately preserved local image file identifiable to this thread ID was supplied. | Selftext plus 22 comment nodes are preserved, including 1 deleted-author row and 1 deleted-body row. The slice is visibly UK/DACH-focused rather than US-domestic, and the commented-on resume image is pointer-only. | Initial preserved raw snapshot for this artifact; any later live or visual re-capture should supplement this saved state and keep the current geographic mismatch visible. |

## Raw Observable Pointers

Capture roots:

```text
raw_thread_root:
  docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/raw/thread_json/
projection_root:
  docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/cleansed/threads/
selection_manifest:
  docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/thread_selection_manifest.csv
```

Per-slice raw and working-view pointers:

| Slice | Raw file | Raw SHA256 | Raw size (bytes) | Projection dir | Projection rows | Projection row types |
| --- | --- | --- | ---: | --- | ---: | --- |
| `R06 / 1t9dp7z` | `reddit_t3_1t9dp7z.json` | `21FD3B56EC2F736E7F459A8614B389276A564CCA72F0F77914D8B303E21055C5` | 48988 | `reddit_t3_1t9dp7z/` | 14 | `post:1`, `comment:12`, `moderator_notice:1` |
| `R07 / 1sbky91` | `reddit_t3_1sbky91.json` | `3FB580861469FC4619C7C745DBE25A913559C9C3F57BF07A272422E8B3491819` | 228559 | `reddit_t3_1sbky91/` | 87 | `post:1`, `comment:85`, `moderator_notice:1` |
| `R08 / 1ow472d` | `reddit_t3_1ow472d.json` | `D418CA68E2893EBFFE3037A2D65DFDADC1D188E4B600CCBC8FC26458C9428108` | 108524 | `reddit_t3_1ow472d/` | 46 | `post:1`, `comment:45` |
| `R09 / 184odt8` | `reddit_t3_184odt8.json` | `0FD437D9F8D0207A46556ECE57BFAB7B354E88334A484EEAE8E0F55D19F3F778` | 175334 | `reddit_t3_184odt8/` | 68 | `post:1`, `comment:67` |
| `R10 / 1qaxpq4` | `reddit_t3_1qaxpq4.json` | `194E69CA5EF7EA8201BBFBC21F163C37831B01E6D36DE43E1EF75035488AFFBE` | 54383 | `reddit_t3_1qaxpq4/` | 23 | `post:1`, `comment:22` |

Raw observable preservation notes:

- The raw JSON files preserve post metadata, body text, author handles, scores,
  timestamps, edit flags, reply nesting, deleted/deleted-author residue, and
  thread URLs/permalinks.
- The existing Mechanical Source Projection working views preserve row reachability
  through `thread.json`, `content.jsonl`, and `readable.md`, including source
  file and source SHA256 linkage back to the raw JSON.
- No `more_placeholder` rows were present in the five supplied thread working
  views.
- The two image-linked resume-review slices preserve the `i.redd.it` pointer in
  raw JSON but not a local copy of the underlying resume image asset.

## Failures, Blockers, and Limitations

- Capture-owned failures observed:
  - No capture-owned blocker prevented local inspection of the five supplied raw
    JSON files or their existing working views.
- Visible limitations to travel downstream:
  - `R08 / 1ow472d` and `R10 / 1qaxpq4` preserve only the linked `i.redd.it`
    image pointer, not a local preserved copy of the commented-on resume image.
  - The owner-supplied five-slice set is not frame-uniform: it includes one
    UK/DACH slice (`R10`), one older 2023 educational-background rejection slice
    (`R09`), and one relationship-management / wealth-management-adjacent resume
    slice (`R08`) alongside the more direct non-target/high-finance threads.
  - Original operator acquisition timing is not separately logged per thread
    beyond the supplied 2026-05-29 file timestamps and the current-session
    artifact timing.
  - No separate archive/cache lookup was attempted for any slice in this
    session.
- Out-of-bounds material treated as out of bounds (not worked around):
  - Wall Street Oasis and any live Reddit surface were not fetched.
  - No private/authenticated/paywalled/deceptive source path was used.
  - No ECR design, Cleaning transformation, Judgment decision, source-quality
    scoring, runtime planning, package install, test run, commit, push, or PR
    activity was attempted.

## Agent-Assistance Context

- Allowed agent verbs used:
  - read local authority docs and current obligation-contract sources;
  - inspect local raw JSON, CSV manifest rows, and existing Mechanical Source
    Projection files;
  - compute local file hashes, sizes, timestamps, and row-count checks;
  - draft this single Markdown capture-session artifact.
- Discarded candidates and discard reason categories:
  - None inside the supplied five-thread target set. The owner-supplied target
    set itself was treated as binding for this capture unit.
- Any cross of the allow/forbid line (must be `blocked` on the relevant
  obligation):
  - None observed. No relevance ranking, exclusion, credibility judgment,
    Cleaning, ECR design, or runtime/source-system work was performed.

## Categorical Handoff Or Visible Stop

- Handoff state: `categorical_handoff_to_ECR`
- Reason if not categorical_handoff_to_ECR: not_applicable.
- Handoff limitations that must remain visible:
  - two image-linked resume-review slices are pointer-only for the underlying
    resume image asset;
  - the owner-supplied sub-batch visibly mixes direct-frame and adjacent/non-US
    slices and must not be treated as a cleaned homogeneous set;
  - this artifact records only the Reddit sub-batch, not Wall Street Oasis or a
    cross-venue Slot 3 synthesis;
  - this artifact does not define ECR fields, IDs, schemas, storage, or receipt
    mechanics.

## LLM Capture-Visibility Checker Output

```text
visible_capture_limitation: Obligations 3 and 8 show that original operator acquisition timing is visible only through the 2026-05-29 delivery folder and local file timestamps, not through separately logged per-thread acquisition receipts. Obligations 6 and 12 show that slices `R08 / 1ow472d` and `R10 / 1qaxpq4` preserve only `i.redd.it` image pointers, not local preserved copies of the commented-on resume images. Obligations 12 and 16 show that the owner-supplied five-slice set visibly mixes direct-frame, adjacent, older, and UK/DACH context. These are artifact-visible capture limitations that can travel downstream without being a blocker because the artifact declares them explicitly at obligation level and per-slice level rather than hiding or normalizing them.
```
