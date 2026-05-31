# Data Capture Spine Pressure-Test Slot 3 Combined Handoff v0

```yaml
retrieval_header_version: 1
artifact_role: Data Capture pressure-test combined handoff artifact
scope: Combined Slot 3 Reddit + WSO Data Capture posture and final capture-owned handoff-state decision.
use_when:
  - Checking the source inputs, per-venue capture posture, and final Slot 3 combined handoff-state decision.
  - Preserving Reddit and WSO venue-specific limitations before ECR, Cleaning, Judgment, or pressure-test evidence synthesis.
  - Avoiding drift from Data Capture into source completion, ECR schema, Cleaning, Judgment, or runtime/source-system work.
authority_boundary: retrieval_only
open_next:
  - docs/product/data_capture_spine_pressure_test_slot_3_reddit_batch_1of2_reddit_financialcareers_threads_batch_1of2_capture_session_v0.md
  - docs/product/data_capture_spine_pressure_test_slot_3_reddit_batch_2of2_reddit_financialcareers_threads_batch_2of2_capture_session_v0.md
  - docs/product/data_capture_spine_pressure_test_slot3_reddit_subbatch_control_note_v0.md
  - docs/product/data_capture_spine_pressure_test_slot3_wso_capture_session_v0.md
  - docs/product/data_capture_spine_pressure_test_execution_authorization_v0.md
  - docs/product/data_capture_spine_pressure_test_commissioning_plan_v0.md
  - docs/product/core_spine_v0_data_capture_spine_obligation_contract_v0.md
stale_if:
  - A later owner decision rejects or supersedes the Slot 3 combined handoff scope.
  - Either Reddit sub-batch capture artifact is materially amended or superseded.
  - The WSO bounded source-language anchor artifact is materially amended or superseded.
  - The accepted intake-surface target, commissioning plan, or obligation contract is materially amended before this handoff is completed.
```

## Status

Status: `COMBINED_HANDOFF_STATE_DECIDED_RECAPTURE_POSTURE_V0`.

This artifact has been rewritten against the current Reddit and WSO Slot 3
capture surfaces and now sets the combined Slot 3 capture-owned handoff state.
It records an artifact-hygiene validation pass. It does not claim Slot 3
pressure-test completion, Data Capture validation, or downstream readiness.

`SOURCE_CONTEXT_READY`

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom Slot 3 combined Reddit+WSO handoff pack
  edit_permission: docs-write for combined handoff artifact through final handoff-state decision
  target_scope: docs/product/data_capture_spine_pressure_test_slot3_combined_handoff_v0.md
  dirty_state_checked: yes
  blocked_if_missing:
    - AGENTS.md
    - .agents/workflow-overlay/README.md
    - docs/product/data_capture_spine_pressure_test_slot_3_reddit_batch_1of2_reddit_financialcareers_threads_batch_1of2_capture_session_v0.md
    - docs/product/data_capture_spine_pressure_test_slot_3_reddit_batch_2of2_reddit_financialcareers_threads_batch_2of2_capture_session_v0.md
    - docs/product/data_capture_spine_pressure_test_slot3_reddit_subbatch_control_note_v0.md
    - docs/product/data_capture_spine_pressure_test_slot3_wso_capture_session_v0.md
```

## Source Surface

Primary current inputs:

| Input | Path | SHA256 | Current posture |
| --- | --- | --- | --- |
| Reddit batch 1of2 | `docs/product/data_capture_spine_pressure_test_slot_3_reddit_batch_1of2_reddit_financialcareers_threads_batch_1of2_capture_session_v0.md` | `7833038440C81B6BEE30AC4AAEE7F8CBF4AFF383E0AD5269ED671F141293E770` | `re-capture_posture`; checker output `visible_capture_limitation`. |
| Reddit batch 2of2 | `docs/product/data_capture_spine_pressure_test_slot_3_reddit_batch_2of2_reddit_financialcareers_threads_batch_2of2_capture_session_v0.md` | `BA950FCF72AC7EB1B3C85BBEA3BEE8F398CB08D35D292EF82182102C04A2E8F5` | `categorical_handoff_to_ECR`; checker output `visible_capture_limitation`. |
| Reddit control note | `docs/product/data_capture_spine_pressure_test_slot3_reddit_subbatch_control_note_v0.md` | `1BBC784DF6A8DE049DF2F2EA66766AFBB0AB07E5AE741B8F7EF2B2102A1FED1C` | Reddit captured with visible limitations; WSO now no longer deferred. |
| WSO bounded anchor pass | `docs/product/data_capture_spine_pressure_test_slot3_wso_capture_session_v0.md` | `778F92F1F1EAE7E06F75B120D2178687E9131FAE8FDBF95E89AAB7D45A271132` | `categorical_handoff_to_ECR`; checker output `visible_capture_limitation`. |

Controlling execution and obligation sources:

- `docs/product/data_capture_spine_pressure_test_execution_authorization_v0.md`
- `docs/product/data_capture_spine_pressure_test_commissioning_plan_v0.md`
- `docs/product/core_spine_v0_data_capture_spine_obligation_contract_v0.md`

The previous untracked combined handoff draft referenced a stale single Reddit
capture artifact and old obligation vocabulary. It is superseded by this
rewrite.

## Decision Frame

- Decision question: Can Data Capture preserve Slot 3 non-target US-domestic
  resume-driven interview-getting pain across Reddit and WSO as a combined
  source posture, with venue limitations visible, before any ECR receipt,
  Cleaning, Judgment, or synthesis?
- Owner or owner-context: Orca owner / Chief Architect pressure-testing the
  Data Capture Spine and Mechanical Source Projection intake boundary.
- Consequence: The final handoff-state decision will determine whether Slot 3
  can proceed as a captured mixed-forum venue surface, or whether limitations
  require recapture or owner review first.
- Allowed decision verbs: `categorical_handoff_to_ECR`, `visible_stop`,
  `visible_blocker`, `rerun`, `re-capture_posture`, or later owner-authorized
  pressure-test patch planning.
- Cutoff posture: Authorized Slot 3 cutoff is Q2 2026. Reddit uses the local
  JSON file state supplied on 2026-05-29. WSO uses the public-page posture
  visible during the bounded source-language anchor pass.
- Downstream-use intent: Data Capture handoff only. This artifact does not rank
  pains, classify credibility, decide downstream use, define ECR fields, perform
  Cleaning, or synthesize customer meaning.

## Source Boundary

- Reddit in scope:
  - Ten operator-supplied local `r/FinancialCareers` thread JSON slices.
  - Existing Reddit Mechanical Source Projection working views.
  - Reddit readable thread views used for bounded source-language anchors in
    batch 1.
- WSO in scope:
  - Seven public WSO URL slices with bounded source-language anchors.
  - Prior WSO discovery inventory as source-candidate context.
- Boundary compliance:
  - Reddit inspection stayed inside owner-supplied local public-thread files.
  - WSO inspection used public browser/web inspection only.
  - No login, email unlock, social unlock, paid access, private access,
    anti-detect method, proxy, source-system build, scraper, API, ECR schema,
    Cleaning transformation, or Judgment conclusion was used.
- Observed but not used:
  - Reddit live continuation, media binary retrieval, user-profile traversal,
    and archive/cache lookup.
  - WSO hidden/comment-unlocked material, full comment graph retrieval, raw HTML
    preservation, screenshots, archive lookup, and account-created access.

## Capture Mode

- Reddit batch 1 mode: agent-assisted local file inspection over
  owner-supplied raw JSON plus bounded source-language anchors from local
  readable thread views.
- Reddit batch 2 mode: mixed human-led local file inspection plus
  agent-assisted local-file inspection, using owner-supplied raw JSON and
  existing Mechanical Source Projection working views.
- WSO mode: mixed human-led plus agent-assisted public browser/web inspection,
  with bounded source-language anchors embedded directly in the artifact.
- Combined handoff mode: consolidation of current capture artifacts only. This
  artifact does not perform live recapture, archive lookup, source completion,
  ECR design, Cleaning, Judgment, runtime, or tooling.

## Per-Venue Posture

| Venue unit | Captured surface | Capture posture | Principal visible limitations | Current handoff implication |
| --- | --- | --- | --- | --- |
| Reddit batch 1of2, rows R01-R05 | Five local `r/FinancialCareers` JSON slices with bounded source-language anchors added after checker remediation. | `re-capture_posture` at sub-batch level. | `R01` is materially gallery/image-dependent with only media metadata and preview URLs; `R03` includes preview-image rows without local image binaries; no live/archive continuation; one visible `more` placeholder; deleted rows remain pointer-only. | Cannot be treated as fully inspectable for layout/image-dependent meaning without carrying recapture posture visibly. |
| Reddit batch 2of2, rows R06-R10 | Five local `r/FinancialCareers` JSON slices plus existing projection working views. | `categorical_handoff_to_ECR` with visible limitations. | Missing separately logged per-thread acquisition receipts; `R08` and `R10` preserve `i.redd.it` image pointers without local image binaries; supplied set mixes direct-frame, adjacent, older, and UK/DACH context. | Can travel categorically as a bounded Reddit sub-batch only if mixed-slice and media-pointer limitations remain visible. |
| Reddit control note | Control summary for both Reddit sub-batches. | Reddit captured with visible limitations; neither sub-batch has active `capture_closure_blocker`. | Reddit-only state was incomplete Slot 3 coverage before WSO; media binaries and live/archive continuation remain unperformed. | Now serves as routing/control source for combined handoff; not a synthesis or validation artifact. |
| WSO bounded source-language anchor pass | Seven public WSO URL slices with source-language anchors and visible venue envelope limitations. | `categorical_handoff_to_ECR` for bounded anchor pass only. | No raw WSO HTML, screenshots, archive lookup, projection rows, or full comment graph; hidden/comment-unlocked material not captured; checker was artifact-internal Codex pass, not separate manual GPT-5.5 UI invocation. | Can travel as second-venue capture if treated as bounded source-language anchor pass, not as a complete WSO corpus. |

## Cross-Venue Limitation Posture

- Reddit is stronger on raw/projection preservation because it has local raw JSON
  and, for batch 2, existing projection working views. It is weaker where
  image/gallery assets were not locally preserved.
- WSO is stronger as a non-Reddit venue check with source-language anchors. It
  is weaker on raw preservation because there is no local raw HTML, screenshot
  set, archive packet, full comment graph, or projection packet.
- Both venues carry `visible_capture_limitation` checker results rather than
  clean checker closure.
- The combined Slot 3 surface is mixed by design: direct non-target pain,
  resume/no-response pain, networking/interview access pain, advice/context,
  adjacent role/geography slices, and counter-signal context are all visible.
- No combined-source Cleaning, semantic clustering, relevance ranking,
  credibility classification, or downstream-use decision is made here.

## Final Combined Handoff-State Decision

Handoff state: `re-capture_posture`.

Reason:

The combined Slot 3 surface is captured enough to inspect the current venue
posture, but it should not be treated as a clean categorical handoff yet because
one current source input, Reddit batch 1of2, is itself in `re-capture_posture`.
That posture is driven by image/gallery-dependent slices where source meaning
may depend on media binaries that were not locally preserved. WSO is also a
bounded source-language anchor pass rather than a raw corpus or projection
packet. Upgrading the combined Slot 3 surface to `categorical_handoff_to_ECR`
would hide the fact that at least one component still asks downstream to
consider recapture before treating the venue set as fully inspectable.

This is not a `visible_blocker` or `visible_stop`: Reddit batch 2of2 and WSO can
travel categorically as bounded inputs with visible limitations, and Reddit
batch 1of2 remains inspectable as a first-pass snapshot. The combined result is
therefore best classified as `re-capture_posture`: usable for capture learning
and pressure-test evidence, but not cleanly closed for categorical ECR handoff
unless the owner accepts the media and WSO-boundedness limitations as sufficient
or authorizes a targeted recapture.

Recapture candidates, if later authorized:

- Reddit batch 1of2: preserve `R01` gallery/image binaries and `R03`
  preview-image rows as local media artifacts or screenshots.
- WSO: preserve raw HTML, screenshots, archive posture, or account-created
  access output if WSO becomes load-bearing enough to need stronger capture.

No recapture is performed in this artifact.

## Artifact Hygiene Validation Record

Validation scope:

- stale obligation vocabulary and stale artifact reference search;
- current source-input hash confirmation;
- checker-token hygiene;
- downstream leakage search for Judgment, Cleaning, ECR schema, source-quality,
  runtime, approval, or readiness overclaims;
- Markdown diff hygiene.

Validation result:

- Current source-input hashes match the Source Surface table.
- No stale pre-amendment raw-observable or handoff-sufficiency obligation
  vocabulary was found in operative text.
- No stale single-Reddit-capture artifact reference was found in operative text.
- No stale checker scaffolding token was found.
- Downstream-vocabulary hits appear only in boundary, forbidden-output, or
  non-claim contexts, not as operative capture decisions.
- Pre-commit whitespace validation should be run after staging because this
  artifact is currently untracked; an unstaged `git diff --check` does not
  inspect untracked file contents.

This validation record is artifact-hygiene evidence only. It is not Data Capture
validation, source-fidelity certification, pressure-test discharge, ECR receipt,
Cleaning readiness, Judgment readiness, or approval.

## Non-Claims

This artifact does not:

- complete a full Slot 3 corpus;
- claim full Reddit or WSO source completeness;
- claim source quality, credibility, integrity, relevance,
  representativeness, or downstream admissibility;
- validate, certify, approve, accept, or harden the Data Capture Spine;
- discharge the full pressure-test batch;
- define ECR fields, IDs, schemas, storage, file formats, or runtime receipt
  mechanisms;
- perform Cleaning, normalization certification, semantic dedupe, clustering,
  summarization, or translation;
- perform Judgment, Signal Use Classification, Decision Strength, Action
  Ceiling, discounting, exclusion, buyer proof, customer synthesis, or
  commercial-readiness assessment;
- authorize source-system planning, scrapers, APIs, dashboards, storage,
  packages, tests, deployment, commits, pushes, or PRs.
