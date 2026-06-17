# Commission Signal Board Migration Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: Migration inventory (Commission Signal Board marking; docs-only)
scope: >
  Marks Commission Signal Board-owned, legacy-named, consumed, and adjacent
  surfaces before any further spine-first allocation, without moving files or
  changing the existing CSB migration plan.
use_when:
  - Deciding what currently belongs to Commission Signal Board.
  - Separating legacy `commission gate` wording from current Commission Signal Board semantics.
  - Planning whether CSB stays in the pilot spine or becomes an above-spine intake authority.
authority_boundary: retrieval_only
open_next:
  - orca/product/spines/commission_signal_board/README.md
  - orca/product/spines/commission_signal_board/spine.yaml
  - docs/migration/commission_signal_board_spine_pilot_migration_plan_v0.md
  - orca/product/spines/commission_signal_board/migrations/moved_paths_index.md
  - docs/decisions/orca_repo_structure_binding_v0.md
  - docs/decisions/orca_spine_first_workspace_structure_proposal_v0.md
  - docs/workflows/orca_repo_map_v0.md
stale_if:
  - The CSB pilot spine is renamed, rejected, or materially amended.
  - CSB is reallocated from a pilot spine to a shared/above-spine product-intake home.
  - The CSB validator, tests, fixtures, prompt, playbook, or authority packet move.
  - Search/AEO, Capture, Judgment, ECR/SCR, Cleaning, or Product Lead source boundaries change in a way that alters CSB handoff ownership.
```

- Status: MIGRATION_MARKING_ONLY.
- Worktree basis: `codex/commission-spine-structure` at
  `a2705cb25d9eb408837c443a13365d0807e5bd89` before this inventory was
  drafted.
- Preflight note: the root `main` checkout did not contain
  `docs/migration/commission_signal_board_spine_pilot_migration_plan_v0.md`;
  the clean commission worktree did, and this inventory was written there.
- Current branch reality: the docs-only CSB pilot spine is already live on this
  branch. This inventory marks ownership and future allocation; it does not
  reverse, extend, or reauthorize that move.
- Conceptual stance for future allocation: CSB is likely above individual
  product spines as intake/commission signal authority. The current physical
  home is the docs-only pilot spine until the owner decides whether that pilot
  remains permanent or is promoted/reallocated.
- No file moves, code changes, runtime changes, hook wiring, CI wiring,
  reference rewrites, doctrine-change claims, validation claims, readiness
  claims, or buyer-proof claims are authorized by this inventory.

## 1. Current Surfaces Found

### CSB-Owned Current Surfaces

| Surface | Current role | Inventory mark |
| --- | --- | --- |
| `orca/product/spines/commission_signal_board/README.md` | Live CSB pilot spine entry point. | csb_owned_current |
| `orca/product/spines/commission_signal_board/spine.yaml` | Machine-readable CSB manifest for canonical docs, stubs, shared validator/test surfaces, and non-goals. | csb_owned_current |
| `orca/product/spines/commission_signal_board/authority/orca_commission_signal_board_prompt_adjudication_packet_v0.md` | Authority-adjacent packet that records why the temporary gate-shaped prompt became an evidence/signals-only signal board. | csb_owned_current |
| `orca/product/spines/commission_signal_board/prompts/orca_commission_signal_board_prompt_v0.md` | Full CSB prompt. | csb_owned_current |
| `orca/product/spines/commission_signal_board/workflows/commission_signal_board_playbook_v0.md` | Operating playbook: intake first, full board only when inputs are complete, manual validator only against full board output. | csb_owned_current |
| `orca/product/spines/commission_signal_board/harness/validator.md` | Spine-local pointer to the manual validator. | csb_owned_pointer |
| `orca/product/spines/commission_signal_board/tests/validator_tests.md` | Spine-local pointer to executable validator tests/fixtures. | csb_owned_pointer |
| `orca/product/spines/commission_signal_board/migrations/moved_paths_index.md` | Moved-path index for CSB old paths and intentionally unmoved executable surfaces. | csb_owned_current |

### Legacy CSB Paths Retained As Resolver Stubs

| Surface | Current role | Inventory mark |
| --- | --- | --- |
| `docs/product/product_lead/orca_commission_signal_board_prompt_adjudication_packet_v0.md` | Resolver stub to the spine-local authority packet. | legacy_stub_do_not_edit_as_source |
| `docs/prompts/product-planning/orca_commission_signal_board_prompt_v0.md` | Resolver stub to the spine-local prompt. | legacy_stub_do_not_edit_as_source |
| `docs/workflows/commission_signal_board_playbook_v0.md` | Resolver stub to the spine-local playbook. | legacy_stub_do_not_edit_as_source |

### Shared Executable Or Test Surfaces

| Surface | Current role | Inventory mark |
| --- | --- | --- |
| `.agents/hooks/check_commission_signal_board_output.py` | Manual/local mechanical checker for CSB classifier-handoff row safety. | shared_global_keep_in_place |
| `orca-harness/tests/unit/test_commission_signal_board_output_validator.py` | Executable validator unit tests. | shared_harness_keep_in_place |
| `orca-harness/tests/fixtures/commission_signal_board_outputs/` | Validator fixtures. | shared_harness_keep_in_place |

### Migration, Decision, Workflow, And Prompt Surfaces

| Surface | Current role | Inventory mark |
| --- | --- | --- |
| `docs/migration/commission_signal_board_spine_pilot_migration_plan_v0.md` | Applied CSB spine-pilot migration plan. | dependency_do_not_update_from_this_inventory |
| `docs/prompts/handoffs/commission_signal_board_spine_pilot_reconciliation_handoff_prompt_v0.md` | Historical handoff that commissioned reconciliation of stale gate wording and spine pilot planning. | historical_handoff_keep_global |
| `docs/decisions/orca_spine_first_workspace_structure_proposal_v0.md` | Proposed spine-first target; CSB pilot partially accepted/live on this branch. | structure_dependency_keep_global |
| `docs/decisions/orca_repo_structure_binding_v0.md` | Binding decision that makes `orca/product/spines/commission_signal_board/` live only for the CSB docs-only pilot. | structure_dependency_keep_global |
| `.agents/workflow-overlay/artifact-folders.md` | Artifact folder authority that binds accepted homes. | overlay_dependency_keep_global |
| `repo-structure.yaml` | Machine map that knows the live CSB pilot root. | machine_map_dependency_keep_global |
| `docs/STRUCTURE.md` | Human structure guide updated for the CSB pilot root. | structure_guide_keep_global |
| `docs/workflows/orca_repo_map_v0.md` | Retrieval map that routes agents to the live CSB spine, playbook, validator, and migration plan. | route_map_keep_global |

### Review Surfaces

No direct CSB-specific review input or review output was found in the targeted
review search:

```powershell
rg --files docs\review-inputs docs\review-outputs | rg -i "commission_signal_board|commission signal board|commission_gate|commission-gate|\bcsb\b|signal_board"
rg -n -i "commission signal board|commission_signal_board|commission gate|commission-gate|commission_gate|\bCSB\b|signal board" docs\review-inputs docs\review-outputs
```

One unrelated review-output hit used `commission-gated` in a Data Capture
context. It is not marked as CSB-owned.

## 2. Legacy Wording Risks

| Wording/surface | Risk | Current treatment |
| --- | --- | --- |
| `commission gate`, `commission-gate`, `commission_gate` | Future agents may import pass/fail or approval semantics into CSB. | Preserve only where factual or historical; current product object is Commission Signal Board. |
| `codex/commission-gate` branch/base references | Branch provenance can look like product semantics. | Keep as factual legacy lane name with "legacy-named" context where edited. |
| Temp prompt path `orca_commission_gate_prompt (1).md` | Historical prompt name suggests a gate. | Preserve in adjudication packet as provenance, not current authority. |
| `commission_gate_brief` schema name | Can imply current schema still owns CSB. | Treat as historical prompt residue. Current prompt uses signal-board rows and classifier handoff packet. |
| `Gate decision / allocation` in the source prompt history | Can turn evidence allocation into a demand gate. | Current CSB keeps allocation as search hygiene only, not pass/fail. |
| Product Lead demand-gate artifacts | Separate demand/proof historical surfaces may be mistaken for CSB. | Mark as Product Lead/Product Strategy context, not CSB-owned. |
| `intake gate` phrasing | Makes missing-input checks sound like approval checks. | Current playbook uses intake check semantics; intake-only outputs are not boards and should not be validator targets. |

Do not perform a global rename. Some `gate` language is valid in Judgment,
Data Capture, proof, validation, and historical records. The migration rule is
local: CSB is not a gate, not a demand verdict, and not an approval surface.

## 3. CSB-Owned Surfaces

CSB owns these concepts:

| Concept | Owning surface |
| --- | --- |
| Required commission intake fields and missing-input scaffold | `orca/product/spines/commission_signal_board/prompts/orca_commission_signal_board_prompt_v0.md` |
| Source family/subfamily board rows | `orca/product/spines/commission_signal_board/prompts/orca_commission_signal_board_prompt_v0.md` |
| Evidence/signals-only boundary | Prompt plus `authority/orca_commission_signal_board_prompt_adjudication_packet_v0.md` |
| Graph-light retrieval brief shape | Prompt plus adjudication packet |
| Signal role / row purpose / graph role labels | Prompt plus adjudication packet |
| Classifier handoff packet packaging | Prompt plus playbook |
| Validator applicability sequence | `orca/product/spines/commission_signal_board/workflows/commission_signal_board_playbook_v0.md` |
| CSB moved-path resolution | `orca/product/spines/commission_signal_board/migrations/moved_paths_index.md` |

CSB does not own evidence truth, retrieval, scraping, capture, demand
classification, graph construction, graph scoring, forecast probability,
Judgment, buyer proof, validation, readiness, CI, or runtime.

## 4. Surfaces CSB Consumes

These are source surfaces CSB may point to, read, or package for handoff. They
should not be moved into CSB just because CSB consumes their concepts.

| Owning lane/family | Consumed surfaces | CSB use | Migration rule |
| --- | --- | --- | --- |
| Product Lead / product proof | `docs/decisions/orca_product_thesis_consumer_demand_v0.md`, `docs/product/product_lead/orca_offer_hypothesis_v0.md`, `docs/product/product_lead/orca_offer_hypothesis_consumer_demand_revision_v0.md`, `docs/product/product_lead/orca_buyer_proof_packet_v0.md`, `docs/product/product_lead/orca_buyer_proof_packet_consumer_demand_revision_v0.md` | Decision context, demand-allocation frame, proof non-claims. | Keep Product Lead/shared. CSB only packages signal routes. |
| Product Lead demand-gate history | `docs/product/product_lead/orca_demand_scan_gate_adjudication_packet_v0.md`, `docs/product/product_lead/orca_demand_gate_run_commission_criteria_v0.md`, `docs/product/product_lead/orca_demand_gate_definition_closures_proposal_v0.md` | Historical gate-shaped demand language to avoid importing into CSB. | Do not move into CSB without owner decision; likely product-strategy history. |
| Search / AEO | `docs/product/data_capture_spine/demand_search_interest_sourcing_and_gate_delta_spec_v0.md` | Search-interest and AEO posture: AEO visibility annotation only, search methodology/pins owned elsewhere. | Keep with Search/AEO/Data Capture until its lane allocates a future home. |
| Capture / Source Capture | `docs/workflows/data_capture_spine_consolidation_map_v0.md`, `docs/product/source_capture_toolbox/source_capture_playbook_v0.md`, `docs/product/source_capture_toolbox/capture_recon_index_v0.md`, `docs/product/source_capture_toolbox/source_quality_state_assembler_v0.md` | Source access posture, capture/recon method, source-quality support. | Keep Capture/Source Capture owned. CSB can require route briefs, not capture. |
| Creator capture | `docs/product/data_capture_spine/orca_creator_monitoring_policy_architecture_v0.md`, `docs/product/data_capture_spine/orca_creator_momentum_pipeline_architecture_v0.md`, `docs/research/creator_momentum_data_landscape_v0.md`, `docs/migration/capture_spine_ig_creator_migration_inventory_v0.md` | Creator/social-video family context and future IG/TikTok/YouTube/Reddit creator slices. | Keep Capture/IG creator migration-owned. CSB only marks creator slices. |
| Retail / PDP capture | `docs/product/source_capture_toolbox/retail_pdp_projection_contract_v0.md`, `docs/product/source_capture_toolbox/retail_pdp_projection_playbook_v0.md`, `docs/product/source_capture_toolbox/retail_pdp_sidecar_operator_playbook_v0.md`, `docs/product/data_capture_spine/retail_pdp_typed_envelope_probe_v0.md` | Retail/PDP corroboration and operational signal posture. | Keep Capture/retail owned; CSB does not own retailer capture or projection. |
| LinkedIn / org motion | `docs/product/data_capture_spine/data_capture_spine_linkedin_lane_index_v0.md`, `docs/workflows/linkedin_lane_operator_pilot_plan_v0.md` | Org-motion route posture; prefer ATS/careers pages; LinkedIn no-live/planning-only unless explicitly routed. | Keep LinkedIn/Capture lane owned. |
| Judgment | `docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md`, `docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md`, `docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md`, `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md` | Downstream claim-tier, gate, and case-run boundaries. | Keep Judgment owned. CSB cannot claim Judgment quality. |
| ECR / SCR / Signal Content | `docs/workflows/ecr_spine_submap_v0.md`, `docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md`, `docs/product/signal_content/signal_content_record_deriver_architecture_plan_v0.md` | Future derived-record and signal-content handoff context. | Keep ECR/SCR owned. CSB outputs are not Evidence Content Records or Signal Content Records. |
| Cleaning / Core data boundary | `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md`, `docs/product/core_spine/core_spine_v0_information_production_foundation_v0.md`, `docs/product/core_spine/core_spine_v0_data_lake_mechanics_map_v0.md` | Boundary between raw/projection/derived records, Cleaning, Evidence Units, and Judgment consumption. | Keep Core/Cleaning/Data Lake owned. CSB does not clean or normalize evidence. |

## 5. Proposed Future Allocation

Current physical allocation on this branch:

```text
orca/product/spines/commission_signal_board/
```

This is the live docs-only pilot home. It is a valid current route, but it does
not settle the conceptual product role forever.

Proposed conceptual allocation:

```text
Commission Signal Board = above-spine intake / commission signal authority.
Capture, Search/AEO, ECR/SCR, Cleaning, Judgment, Product Lead = owners of
their own methods, records, proof standards, and downstream decisions.
```

Future allocation options:

| Option | What it means | Inventory recommendation |
| --- | --- | --- |
| Keep CSB as its own pilot spine | The current physical home becomes the permanent CSB workspace. | Viable if Orca treats CSB as a product subsystem with prompts/playbook/validator pointers. |
| Promote CSB to a shared above-spine intake home | CSB becomes an intake/commission authority used by multiple spines. | Conceptually strongest, but needs owner decision and a bounded migration plan from the pilot spine. |
| Put CSB under Capture | CSB becomes a capture intake module. | Reject by default; CSB defines signal routes before retrieval/capture and consumes Capture rather than belonging to it. |
| Put CSB under Judgment | CSB becomes a judgment gate or demand verdict precursor. | Reject by default; CSB is evidence/signals-only and hands off to classifier/Judgment boundaries. |

Default: keep the current pilot spine stable while asking the owner whether the
long-term home is "own spine" or "above-spine shared intake." Do not move it
again until that decision exists.

## 6. Pilot Migration Dependency

This inventory depends on, but does not update:

```text
docs/migration/commission_signal_board_spine_pilot_migration_plan_v0.md
orca/product/spines/commission_signal_board/migrations/moved_paths_index.md
docs/decisions/orca_repo_structure_binding_v0.md
docs/decisions/orca_spine_first_workspace_structure_proposal_v0.md
```

The pilot migration plan says the CSB pilot spine is applied on this branch.
This inventory adds a marking layer for what CSB owns, what it consumes, which
legacy gate wording should be treated as residue, and what should not be moved
yet.

The other current migration inventories are adjacent precedent, not CSB
authority:

```text
docs/migration/judgment_spine_spine_first_migration_inventory_v0.md
docs/migration/data_capture_projection_spine_first_migration_inventory_v0.md
docs/migration/capture_spine_ig_creator_migration_inventory_v0.md
docs/migration/data_lake_spine_first_migration_inventory_v0.md
```

Use them to avoid swallowing Capture, Judgment, projection, creator, or
data-lake surfaces into CSB.

## 7. Open Owner Questions

1. Should CSB remain a permanent `commission_signal_board` spine, or should it
   become an above-spine/shared intake authority after the pilot?
2. If CSB becomes above-spine/shared, what exact future root should own it?
3. Should future CSB durable board outputs get a bound artifact folder, or stay
   chat/local until a board-output storage rule exists?
4. Should the validator remain manual/local, or later become CI/pre-commit once
   board-output paths are standardized?
5. Should Product Lead demand-gate history be renamed, archived, or simply
   marked as non-CSB historical context?
6. Which source-family lanes must expose hard contracts before CSB can require
   them in board rows: Search/AEO, creator platforms, Retail/PDP, forums,
   ATS/org-motion, or news/editorial?
7. Should graph retrieval briefs become a separate graph-family artifact
   contract later, or stay inside the CSB prompt until a graph lane exists?

## 8. Suggested Migration Order

1. Freeze this inventory as the CSB marking artifact.
2. Do not move any additional CSB or adjacent files until the owner answers the
   long-term allocation question: own spine versus above-spine shared intake.
3. Keep old CSB resolver stubs in place while the pilot is live.
4. If the current pilot home remains, create future CSB docs under
   `orca/product/spines/commission_signal_board/` and update the moved-path
   index only for CSB-owned docs.
5. If CSB is promoted above-spine, write a separate bounded migration plan from
   the pilot spine to the selected shared/intake home, then update structure
   binding, repo map, stubs, and moved-path indexes together.
6. Keep validator code, executable tests, and fixtures in `.agents/hooks` and
   `orca-harness` until separate implementation/code-root migration authority
   exists.
7. Move consumed surfaces only through their owning lane inventories: Product
   Lead, Search/AEO, Capture/Source Capture, Judgment, ECR/SCR, Cleaning, or
   Data Lake. Do not bulk-move a consumed source into CSB.

## 9. Explicit Non-Claims

This inventory is not:

- a move manifest;
- an authorization to move files;
- an authorization to update the existing CSB spine pilot migration plan;
- a doctrine-change claim;
- source-of-truth promotion;
- validation;
- readiness;
- buyer proof;
- demand classification;
- graph construction;
- graph scoring;
- forecast probability;
- retrieval or scraping authorization;
- CI, hook, runtime, or implementation authorization;
- proof that every possible textual reference to `commission` was found;
- proof that the current CSB pilot home is the permanent long-term home.
