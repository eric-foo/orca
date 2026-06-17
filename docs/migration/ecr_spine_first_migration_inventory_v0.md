# ECR Spine-First Migration Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: Migration inventory (ECR spine-first, docs-only)
scope: >
  Classifies current ECR-owned and ECR-adjacent artifacts for a future
  spine-first migration. Proposes future homes, ownership, move risk, and
  post-move validation without moving files in this pass.
use_when:
  - Preparing a future ECR migration into a spine-first workspace.
  - Deciding which ECR-adjacent artifacts belong to ECR, Signal Content/Signal Statement, Judgment, Capture, shared harness, review/provenance, or history.
  - Checking why ECR should wait for spine-first binding and adjacent rename PRs before any source moves.
authority_boundary: retrieval_only
open_next:
  - docs/workflows/ecr_spine_submap_v0.md
  - .agents/workflow-overlay/artifact-folders.md
  - repo-structure.yaml
  - docs/workflows/orca_repo_map_v0.md
stale_if:
  - PR #239 is merged, closed, or materially amended.
  - PR #242 is merged, closed, or materially amended.
  - PR #237 is merged, closed, or materially amended.
  - repo-structure.yaml adds or rejects `orca/product/spines/`.
  - ECR, Signal Content/Signal Statement, JSG-01, Evidence Binding, or source-capture packet paths move.
```

- Status: `MIGRATION_INVENTORY_ONLY`.
- Output path: `docs/migration/ecr_spine_first_migration_inventory_v0.md`.
- No files moved. No code touched. No ECR tests run.
- Current binding on this branch remains `docs/` plus `orca-harness/`; `orca/product/spines/ecr/` is a future target only.

## Start Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S1 + ECR source-side read pack + targeted pending-structure branches
  edit_permission: docs-write
  target_scope: docs-only ECR spine-first migration inventory
  dirty_state_checked: yes
  blocked_if_missing: none
```

Observed repository state:

| Item | Observation |
| --- | --- |
| Work branch | `codex/ecr-spine-first-migration-inventory` |
| Worktree | `C:/Users/vmon7/Desktop/projects/orca/orca-worktrees/ecr-spine-first-migration-inventory` |
| Base HEAD | `b139fa9f` (`docs: add bound search/ product lane + migrate 4 search-primary docs (#236)`) |
| Root worktree before isolation | `main...origin/main`; untracked `.codex/hooks/run_orca_guard.py`, `_scratch/`, and `orca-worktrees/`; warning reading `orca-harness/.pytest_tmp/` |
| Lane isolation | Separate worktree off `main` because the root base was dirty |
| Lane dirty state before edit | clean |

Open/pending structure surfaces observed:

| Surface | Observation | Path impact for ECR |
| --- | --- | --- |
| PR #239, `docs: propose spine-first workspace structure` | Open. Proposes target `orca/product/spines/<spine>/` plus future `orca/docs/`. Names Commission Signal Board as the pilot and explicitly says not to begin with Judgment, Capture, ECR, or Source Capture. | ECR target path is proposed but not live. Use `move_later` / `pointer_only`, not live moves. |
| PR #242, `docs: rename Core Spine to Foundation Layer` | Open. Moves `docs/product/core_spine/**` to `docs/product/foundation/**`, including boundary and data-lake mechanics files ECR points at. | Any ECR pointer to Core Spine/Foundation must tolerate both current `core_spine/` and future `foundation/` until PR status settles. |
| PR #237, `Rename Signal Statement Record` | Open. Renames Signal Content/SCR to Signal Statement Record; moves docs to `docs/product/signal_statement/` and code to `orca-harness/signal_statement/`. | Do not put Signal Content under ECR. Treat it as sibling; future inventory should rebase to Signal Statement if PR #237 lands. |
| Local branch `codex/ecr-sp3-successor` | Present locally; no matching open PR found by connector search. | Treat as branch context only, not a pending GitHub PR claim. |

## Required Searches

Commands run from the isolated worktree:

```powershell
rg --files | rg "(^docs/product/ecr/|ecr|ECR)"
rg -n "ECR|Evidence Candidate Record|SP-1|SP-2|SP-3|SP-6|source visibility|source-side" docs .agents orca-harness --glob "!_scratch/**" --glob "!orca-worktrees/**"
```

The second search was also re-run with copied review-input source-bundle exclusions for inventory triage:

```powershell
rg -l -n "ECR|Evidence Candidate Record|SP-1|SP-2|SP-3|SP-6|source visibility|source-side" docs .agents orca-harness --glob "!_scratch/**" --glob "!orca-worktrees/**" --glob "!docs/review-inputs/**/sources/**" --glob "!docs/review-inputs/**/source_files/**" --glob "!docs/review-inputs/**/source_bundle/**" --glob "!docs/review-inputs/**/source_snapshot/**"
```

Search triage:

- Included: ECR docs, ECR submap, ECR/SCR/JSG-01 prompts, review/provenance outputs, ECR code/tests, Signal Content sibling surfaces, Evidence Binding, FinalizationReceipt, Capture handoff/source-packet boundary docs.
- Excluded from individual rows: `_scratch/`, old worktrees, generated caches, copied review-input source bundles, and case/source-capture receipts whose only ECR relationship is a non-claim such as "not ECR design." Those are captured below as provenance families where relevant.

## Migration Marks

| Mark | Meaning in this inventory |
| --- | --- |
| `move_now` | Safe to move in the future migration batch once binding is accepted. No row uses this today because the target root is not live. |
| `move_later` | Spine-owned or spine-local artifact, but wait for accepted structure binding and path-settling PRs. |
| `pointer_only` | Create a future ECR spine pointer/index only; leave canonical artifact in its owner lane or leave executable code under `orca-harness/`. |
| `do_not_move` | Not an ECR-owned artifact. It may migrate with another spine, not ECR. |
| `historical_only` | Review, provenance, or historical state. Preserve/index/archive; never treat as live authority. |

## Inventory Table

| Current path | Artifact role | Owner lane | Future target path | Migration mark | Reason | Dependencies | Validation needed after move |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `docs/migration/ecr_spine_first_migration_inventory_v0.md` | This inventory | ECR migration/provenance | `orca/product/spines/ecr/migrations/ecr_spine_first_migration_inventory_v0.md` | `move_later` | New migration record should travel with the future ECR spine after binding. | PR #239 or successor; repo-structure binding. | Retrieval header; moved-path index; stale-reference search. |
| `docs/workflows/ecr_spine_submap_v0.md` | ECR/SCR front-door submap | ECR-owned navigation with sibling SCR routing | `orca/product/spines/ecr/workflows/ecr_spine_submap_v0.md` | `move_later` | ECR spine entry point; currently routes integrity, sibling content, Capture, and JSG-01 boundaries. | PR #237 signal rename; PR #239 binding. | Update repo map/global route; stale old-path search; check that owner docs still open. |
| `docs/product/ecr/ecr_consolidation_v0_frame_source_visibility_slice_architecture_plan_v0.md` | ECR frame + SP-6 architecture plan | ECR-owned integrity plan | `orca/product/spines/ecr/plans/ecr_consolidation_v0_frame_source_visibility_slice_architecture_plan_v0.md` | `move_later` | Core ECR integrity architecture; should live in ECR spine plans/authority. | Foundation path rename; JSG-01 SP-6 docs. | Reference rewrite; source pins rechecked; no authority upgrade. |
| `docs/product/ecr/ecr_consolidation_v0_sp1_sp2_sp3_source_side_slice_plan_v0.md` | SP-1/SP-2/SP-3 source-side reconcile plan | ECR-owned integrity plan | `orca/product/spines/ecr/plans/ecr_consolidation_v0_sp1_sp2_sp3_source_side_slice_plan_v0.md` | `move_later` | Completes source-side ECR posture schema candidate. | ECR frame plan; source-capture producer fields. | Deriver/test pointer checks; stale references; no JSG-01 ownership claim. |
| `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md` | JSG-01-scoped EvidenceUnit binding slice plan | Boundary-adjacent ECR/Judgment composition | `orca/product/spines/ecr/plans/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md` with Judgment pointer | `move_later` | Current file lives under ECR, but it is explicitly JSG-01-scoped composition, not general ECR ownership. | Judgment conductor; Evidence Binding code; Foundation boundary. | Recheck owner lane; add Judgment cross-pointer; verify no full Evidence Unit architecture claim. |
| `docs/product/judgment_spine/jsg01_sp6_source_visibility_derivation_architecture_plan_v0.md` | SP-6 derivation ownership/rule plan | Judgment-owned boundary source for ECR SP-6 | `orca/product/spines/judgment/authority/jsg01_sp6_source_visibility_derivation_architecture_plan_v0.md` plus ECR pointer | `pointer_only` | Source evidence places it in Judgment; ECR should point to it, not absorb it. | ECR frame plan; conductor/JSG-01 state. | ECR submap pointer; Judgment migration inventory if moved. |
| `docs/product/judgment_spine/jsg01_sp6_source_visibility_derivation_architecture_routing_v0.md` | SP-6 routing plan | Judgment-owned boundary source | `orca/product/spines/judgment/workflows/jsg01_sp6_source_visibility_derivation_architecture_routing_v0.md` plus ECR pointer | `pointer_only` | Routing belongs with JSG-01/Judgment authority. | Same as SP-6 plan. | Pointer freshness; no duplicate ECR route. |
| `docs/product/judgment_spine/jsg01_source_side_receipt_translator_v0.md` | Interim source-side receipt translator | Judgment-owned / historical bridge | `orca/product/spines/judgment/archive/jsg01_source_side_receipt_translator_v0.md` plus ECR pointer | `historical_only` | Origin/provenance for closed values; not current ECR authority after ratified ECR field schema. | ECR frame; review output. | Mark supersession/pointer; never use as live authority without owner source. |
| `docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md` | Signal Content Record direction | Signal Content sibling | If PR #237 does not land: `orca/product/spines/signal_content/authority/core_spine_v0_signal_content_record_architecture_v0.md`; if PR #237 lands: `orca/product/spines/signal_statement/authority/core_spine_v0_signal_statement_record_architecture_v0.md` | `move_later` | Sibling content layer, not ECR-owned. It references ECR by key. | PR #237; Foundation rename. | Rename-path rebase; no ECR ownership claim; update ECR submap. |
| `docs/product/signal_content/signal_content_record_deriver_architecture_plan_v0.md` | SCR deriver plan | Signal Content sibling | If PR #237 does not land: `orca/product/spines/signal_content/plans/signal_content_record_deriver_architecture_plan_v0.md`; if PR #237 lands: `orca/product/spines/signal_statement/plans/signal_statement_record_deriver_architecture_plan_v0.md` | `move_later` | Sibling deriver contract; ECR is dependency only. | PR #237; ECR posture refs. | Rename-path rebase; model/code pointer checks. |
| `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md` | Data/Cleaning/Judgment boundary and ECR ratification records | Foundation/Core boundary | Future Foundation home, not ECR; ECR pointer at `orca/product/spines/ecr/authority/pointers/foundation_boundary.md` | `pointer_only` | Load-bearing boundary source, but not ECR-owned. PR #242 likely moves it to Foundation Layer. | PR #242; JSG-01 decisions. | Pointer update after foundation rename; strict source citation recheck. |
| `docs/product/core_spine/core_spine_v0_data_lake_mechanics_map_v0.md` | Cross-layer data-lake mechanics map | Foundation/shared mechanics | Future Foundation/shared home; ECR pointer only | `pointer_only` | Shared flow across Capture, projection, ECR/SCR, Cleaning, Judgment. | PR #242; data-lake migration branches. | Pointer update; no storage/schema authority claim. |
| `docs/product/core_spine/core_spine_v0_information_production_foundation_v0.md` | IPF Evidence Unit standard | Foundation/IPF | Future Foundation home; ECR pointer only | `pointer_only` | ECR/SCR cite it, but it is the semantic standard, not ECR local authority. | PR #242. | Pointer rewrite; strict evidence-standard recheck. |
| `docs/product/data_capture_spine/source_capture_packet_schema_evolution_architecture_v0.md` | SourceCapturePacket schema evolution doctrine | Capture-owned | `orca/product/spines/capture/authority/source_capture_packet_schema_evolution_architecture_v0.md` plus ECR pointer | `pointer_only` | ECR inherits re-derive/read-checked doctrine; Capture owns packet evolution. | Capture migration; ECR derivers. | Pointer freshness; ensure ECR does not fork packet doctrine. |
| `docs/workflows/data_capture_spine_consolidation_map_v0.md` | Capture front-door submap | Capture-owned | `orca/product/spines/capture/workflows/data_capture_spine_consolidation_map_v0.md` plus ECR pointer | `pointer_only` | Provenance layer route into SourceCapturePacket; not ECR-owned. | Capture migration; source-loading pack. | Cross-map pointer check. |
| `docs/product/data_capture_spine/source_capture_core_payload_split_explainer_v0.md` | Capture payload split explainer | Capture-owned | `orca/product/spines/capture/authority/source_capture_core_payload_split_explainer_v0.md` plus ECR pointer | `pointer_only` | Explains raw-keyed flow into ECR/SCR/Cleaning/Judgment. | Data-lake mechanics map. | Pointer check; no ECR schema claim. |
| `docs/product/data_capture_spine/source_capture_tenant_payload_attachment_boundary_v0.md` | Tenant payload boundary | Capture-owned | `orca/product/spines/capture/authority/source_capture_tenant_payload_attachment_boundary_v0.md` plus ECR pointer | `pointer_only` | ECR/SCR read raw-keyed inputs but do not own capture payload attachment. | Capture payload split; tenant payload build state. | Pointer check; no Evidence Binding schema claim. |
| `docs/workflows/reddit_capture_to_ecr_consumption_probe_finding_v0.md` | Real-data capture-to-ECR finding | Capture/ECR boundary finding | `orca/product/spines/ecr/reports/reddit_capture_to_ecr_consumption_probe_finding_v0.md` or Capture reports with ECR pointer | `move_later` | It directly probes ECR ingestion but resolves the posture gap as Capture/Decision-Frame by design. | Reddit capture runner; ECR deriver; Capture obligation Ob.9. | Recheck runner paths; decide whether final owner is ECR reports or Capture reports. |
| `docs/research/judgment-spine/ecr_jsg01_test_run_report_v0.md` | ECR/JSG-01 end-to-end test run report | Judgment research / ECR provenance | `orca/product/spines/judgment/reports/ecr_jsg01_test_run_report_v0.md` with ECR pointer | `historical_only` | Test walk only; clears no case. Useful provenance, not live authority. | JSG-01 unfreeze decision; case packet; ECR derivers. | Preserve non-claims; never promote as validation/readiness. |
| `docs/research/judgment-spine/sp5_finalization_receipt_spec_v0.md` | SP-5 FinalizationReceipt behavior spec | Judgment-owned SP-5 | `orca/product/spines/judgment/authority/sp5_finalization_receipt_spec_v0.md` plus ECR pointer | `pointer_only` | Finalization is a JSG-01/Judgment subpredicate, not ECR-owned. | AR-01 decision; finalization code. | Pointer check; no SP-5 ownership transfer. |
| `docs/decisions/ar_01_pre_decision_status_finalizer_staffing_v0.md` | Finalizer staffing decision | Judgment decision | Future global/Judgment decisions home; ECR pointer only | `pointer_only` | Governs SP-5 finalizer family/identity boundary. | SP-5 spec; conductor. | Decision path pointer; no duplicate decision. |
| `docs/decisions/jsg01_unfreeze_decision_v0.md` | JSG-01 unfreeze decision | Judgment decision | Future global/Judgment decisions home; ECR pointer only | `pointer_only` | JSG-01 is downstream consumer; ECR does not own unfreeze. | Conductor; Evidence Binding. | Pointer check; no "ECR unfreezes JSG-01" language. |
| `docs/decisions/jsg01_unfreeze_decision_memo_v0.md` | JSG-01 unfreeze memo | Judgment decision/provenance | Future global/Judgment decisions home; ECR pointer only | `pointer_only` | Boundary-adjacent but Judgment-owned. | Unfreeze decision. | Pointer check. |
| `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md` | Judgment conductor | Judgment-owned | `orca/product/spines/judgment/authority/judgment_quality_promotion_operating_model_v0.md` plus ECR pointer | `pointer_only` | Consumer of ECR postures; not ECR-owned. | JSG-01 unfreeze; Evidence Binding code. | Recheck JSG-01 row; no conductor move with ECR. |
| `docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md` | Gate ownership map | Judgment-owned | `orca/product/spines/judgment/authority/judgment_spine_gate_ownership_map_v0.md` plus ECR pointer | `pointer_only` | Gate ownership stays Judgment. | Conductor and evidence ladder. | Pointer check. |
| `docs/prompts/architecture/ecr_consolidation_v0_frame_source_visibility_slice_architecture_prompt_v0.md` | ECR architecture prompt | ECR prompt/provenance | `orca/product/spines/ecr/prompts/ecr_consolidation_v0_frame_source_visibility_slice_architecture_prompt_v0.md` | `move_later` | ECR-specific prompt artifact. | Prompt-orchestration rules; ECR frame plan. | Prompt metadata; stale source paths; no re-execution claim. |
| `docs/prompts/architecture/jsg01_sp6_source_visibility_derivation_architecture_prompt_v0.md` | SP-6 architecture prompt | Judgment/ECR boundary prompt | `orca/product/spines/ecr/prompts/jsg01_sp6_source_visibility_derivation_architecture_prompt_v0.md` with Judgment pointer | `move_later` | Prompt is ECR-adjacent and source-visibility-specific; ownership must remain boundary-marked. | JSG-01 SP-6 plan/routing. | Prompt source pins; boundary label. |
| `docs/prompts/architecture/source_capture_packet_schema_evolution_architecture_prompt_v0.md` | Packet evolution architecture prompt | Capture prompt | `orca/product/spines/capture/prompts/source_capture_packet_schema_evolution_architecture_prompt_v0.md` plus ECR pointer | `pointer_only` | Capture owns packet schema; ECR consumes. | Capture schema-evolution doc. | Pointer check. |
| `docs/prompts/handoffs/ecr_jsg01_source_side_receipt_lane_setup_v0.md` | ECR/JSG-01 lane setup handoff prompt | ECR/Judgment prompt provenance | `orca/product/spines/ecr/prompts/ecr_jsg01_source_side_receipt_lane_setup_v0.md` | `historical_only` | Handoff prompt for a prior lane; keep as provenance, not active authority. | Prompt-orchestration; translator. | Archive/pointer check. |
| `docs/prompts/handoffs/ecr_jsg01_bounded_unfreeze_build_handoff_prompt_v0.md` | ECR/JSG-01 bounded unfreeze build handoff | Boundary prompt | `orca/product/spines/ecr/prompts/ecr_jsg01_bounded_unfreeze_build_handoff_prompt_v0.md` with Judgment pointer | `move_later` | ECR-adjacent build handoff; must retain explicit JSG-01/Judgment boundary. | Evidence Binding; finalization; conductor. | Prompt source pins; no code-authorization replay. |
| `docs/prompts/handoffs/signal_content_record_deriver_architecture_ecr_lane_handoff_prompt_v0.md` | SCR deriver handoff | Signal Content sibling prompt | Signal Content/Signal Statement spine prompt home, not ECR | `pointer_only` | Signal Content is sibling/adjacent. PR #237 may rename it. | PR #237. | Rename path rebase. |
| `docs/prompts/reviews/ecr_jsg01_bind_vs_fork_cross_family_review_prompt_v0.md` | ECR/JSG-01 review prompt | Review/provenance | `orca/product/spines/ecr/prompts/reviews/ecr_jsg01_bind_vs_fork_cross_family_review_prompt_v0.md` | `historical_only` | Review prompt, not live authority. | Review outputs. | Archive with output pair if moved. |
| `docs/prompts/reviews/ecr_consolidation_v0_plan_cross_family_review_patch_prompt_v0.md` | ECR plan review/patch prompt | Review/provenance | `orca/product/spines/ecr/prompts/reviews/ecr_consolidation_v0_plan_cross_family_review_patch_prompt_v0.md` | `historical_only` | Review prompt; preserve for provenance only. | ECR review outputs. | Pairing check. |
| `docs/prompts/reviews/jsg01_source_side_receipt_translator_adversarial_review_prompt_v0.md` | Translator review prompt | Judgment/ECR provenance | Judgment review prompt home with ECR pointer | `historical_only` | Translator is historical/proposed source. | Translator review output. | Pairing check. |
| `docs/prompts/product-planning/core_spine_v0_method_validation_cutoff_source_visibility_verification_prompt_v0.md` | Cutoff/source-visibility method-validation prompt | Historical method validation | Future Foundation/Judgment archive; ECR pointer only if cited | `historical_only` | Source-visibility wording is adjacent, but this is method-validation history. | Foundation rename. | Preserve as history; do not treat as ECR plan. |
| `docs/prompts/wrappers/core_spine_v0_method_validation_cutoff_source_visibility_verification_wrapper_v0.md` | Wrapper prompt | Historical method validation | Future Foundation/Judgment archive | `historical_only` | Wrapper only; not ECR authority. | Paired prompt/report. | Pairing check. |
| `docs/review-outputs/ecr_sp6_no_repo_review_bundle.zip` | Review bundle archive | Review/provenance | `orca/product/spines/ecr/archive/ecr_sp6_no_repo_review_bundle.zip` | `historical_only` | Binary review bundle; not live authority. | SP-6 plan. | Hash/preserve only; no source promotion. |
| `docs/review-outputs/adversarial-artifact-reviews/ecr_consolidation_v0_frame_source_visibility_slice_architecture_prompt_adversarial_review_v0.md` | Prompt adversarial review | Review/provenance | `orca/product/spines/ecr/reviews/ecr_consolidation_v0_frame_source_visibility_slice_architecture_prompt_adversarial_review_v0.md` | `historical_only` | Review output, not authority. | Prompt and plan. | Preserve verdict/non-claims; do not treat as current route. |
| `docs/review-outputs/adversarial-artifact-reviews/ecr_consolidation_v0_plan_cross_family_review_v0.md` | ECR plan cross-family review | Review/provenance | `orca/product/spines/ecr/reviews/ecr_consolidation_v0_plan_cross_family_review_v0.md` | `historical_only` | Advisory review output only. | ECR frame plan. | Pairing and stale-source labels. |
| `docs/review-outputs/adversarial-artifact-reviews/ecr_consolidation_v0_sp1_sp2_sp3_source_side_reconcile_cross_family_review_v0.md` | SP-1/2/3 review | Review/provenance | `orca/product/spines/ecr/reviews/ecr_consolidation_v0_sp1_sp2_sp3_source_side_reconcile_cross_family_review_v0.md` | `historical_only` | Advisory review output only. | SP-1/2/3 plan. | Pairing and stale-source labels. |
| `docs/review-outputs/adversarial-artifact-reviews/ecr_jsg01_evidence_unit_binding_plan_delegated_adversarial_artifact_review_patch_v0.md` | Evidence Binding plan review/patch | Boundary review/provenance | `orca/product/spines/ecr/reviews/ecr_jsg01_evidence_unit_binding_plan_delegated_adversarial_artifact_review_patch_v0.md` with Judgment pointer | `historical_only` | Review output over boundary plan; no authority. | Binding plan. | Preserve boundary non-claims. |
| `docs/review-outputs/adversarial-artifact-reviews/evidence_binding_slice_delegated_adversarial_code_review_patch_v0.md` | Evidence Binding code review | Shared harness/Judgment provenance | Judgment or shared harness reviews; ECR pointer only | `historical_only` | Review of code that should not move in this pass. | `orca-harness/evidence_binding/`. | Pairing check; no code movement. |
| `docs/review-outputs/adversarial-artifact-reviews/jsg01_source_side_receipt_translator_adversarial_review_v0.md` | Translator adversarial review | Judgment/ECR provenance | Judgment reviews/archive with ECR pointer | `historical_only` | Review output for historical translator. | Translator doc. | Preserve as provenance only. |
| `docs/review-outputs/adversarial-artifact-reviews/sp5_finalization_producer_delegated_adversarial_code_review_patch_v0.md` | Finalization producer code review | Judgment/SP-5 provenance | Judgment/shared harness reviews; ECR pointer only | `historical_only` | SP-5 belongs to Judgment finalization boundary. | Finalization runner. | Pairing check; no ECR ownership claim. |
| `docs/review-outputs/signal_content_v0_no_repo_review_bundle.zip` | Signal Content review bundle | Signal Content review/provenance | Signal Content/Signal Statement archive, not ECR | `historical_only` | Sibling review bundle. | PR #237. | Rename-path rebase. |
| `docs/review-outputs/method-validation/core_spine_v0_method_validation_cutoff_source_visibility_verification_report_v0.md` | Method-validation report | Historical method validation | Foundation/Judgment archive; ECR pointer only if cited | `historical_only` | Adjacent source-visibility term, not ECR owner artifact. | Paired prompt/wrapper. | Preserve as history. |
| `orca-harness/ecr/__init__.py` | ECR package public surface | Shared harness / ECR implementation | `orca/product/spines/ecr/harness/ecr_package_pointer.md` | `pointer_only` | Executable code stays under `orca-harness/`; future ECR spine should point to it. | Code-root migration decision; tests. | ECR unit tests if code moves later; import-path checks. |
| `orca-harness/ecr/models.py` | ECR models | Shared harness / ECR implementation | `orca/product/spines/ecr/harness/ecr_models_pointer.md` | `pointer_only` | Do not move executable code now. | ECR docs; source-capture models. | Unit tests and import compatibility if later moved. |
| `orca-harness/ecr/deriver.py` | ECR derivers | Shared harness / ECR implementation | `orca/product/spines/ecr/harness/ecr_deriver_pointer.md` | `pointer_only` | Do not move executable code now. | ECR models; source-capture packet model. | Unit tests, no-LLM/import tests, pure-deriver checks if later moved. |
| `orca-harness/tests/unit/_ecr_builders.py` | Shared ECR test builders | Shared harness tests | `orca/product/spines/ecr/tests/ecr_builders_pointer.md` | `pointer_only` | Shared test helper; no code move in this pass. | ECR tests. | Test suite if later moved. |
| `orca-harness/tests/unit/test_ecr_*.py` | ECR unit tests | Shared harness tests | `orca/product/spines/ecr/tests/ecr_unit_tests_pointer.md` | `pointer_only` | Executable tests stay in harness until code-root migration. | ECR code. | Full ECR unit subset if later moved. |
| `orca-harness/signal_content/__init__.py`, `models.py`, `deriver.py` | Signal Content implementation | Signal Content sibling / shared harness | Signal Content/Signal Statement spine harness pointer | `pointer_only` | Sibling code, not ECR. PR #237 may rename to `signal_statement/`. | PR #237; SCR docs/tests. | Signal tests if later moved; import-path checks. |
| `orca-harness/tests/unit/test_signal_content_*.py` | Signal Content tests | Signal Content sibling / shared harness tests | Signal Content/Signal Statement spine test pointer | `pointer_only` | Sibling tests, not ECR. | PR #237. | Signal tests if later moved. |
| `orca-harness/evidence_binding/__init__.py`, `models.py`, `composer.py`, `verifier.py` | JSG-01 Evidence Binding implementation | Shared harness / Judgment boundary | `orca/product/spines/ecr/harness/evidence_binding_pointer.md` and Judgment pointer | `pointer_only` | Boundary code composes ECR reads onto JSG-01 evidence; do not move executable code. | Conductor; ECR derivers; finalization models. | Evidence binding tests; no aggregate verdict check if later moved. |
| `orca-harness/tests/unit/test_evidence_binding.py` | Evidence Binding tests | Shared harness / Judgment boundary tests | ECR/Judgment test pointer | `pointer_only` | Do not move executable tests. | Evidence Binding code. | Unit tests if later moved. |
| `orca-harness/tests/unit/test_claim_support_verifier.py` | Claim-support verifier tests | Shared harness / Judgment boundary tests | Judgment/shared harness test pointer | `pointer_only` | Adjacent to Evidence Binding verifier, not ECR-owned. | Evidence Binding verifier. | Unit tests if later moved. |
| `orca-harness/schemas/finalization_models.py` | SP-5 FinalizationReceipt model and consumer | Shared harness / Judgment SP-5 | Judgment/shared harness pointer; ECR pointer only | `pointer_only` | Finalization belongs to JSG-01/Judgment boundary; executable code stays under harness. | SP-5 spec; runner. | Finalization tests and contract tests if later moved. |
| `orca-harness/runners/run_finalization_receipt.py` | SP-5 producer runner | Shared harness / Judgment SP-5 | Judgment/shared harness pointer; ECR pointer only | `pointer_only` | Do not move executable runner in ECR migration. | Finalization models; runner tests. | Runner tests; CLI path checks if later moved. |
| `orca-harness/tests/unit/test_finalization_models.py`, `test_run_finalization_receipt.py`; `orca-harness/tests/contract/test_finalization_models_contract.py` | Finalization tests | Shared harness / Judgment SP-5 tests | Judgment/shared harness test pointer | `pointer_only` | Executable tests stay put. | Finalization code. | Unit and contract tests if later moved. |
| `orca-harness/cases/product_learning/jsg01_binding_assembly_proof_v0/` | JSG-01 binding assembly proof case | Judgment/ECR provenance | `orca/product/spines/judgment/cases/jsg01_binding_assembly_proof_v0/` with ECR pointer | `historical_only` | Product-learning proof/provenance; not ECR authority and not code move. | JSG-01 test run report; case schemas. | Preserve non-claims; case path reference rewrite if moved. |
| `orca-harness/cases/product_learning/**/source_captures/**/{receipt.md,manifest.json}` | Source-capture provenance receipts/manifests | Capture-owned provenance | Capture cases/provenance home; ECR pointer only when a case binds ECR | `do_not_move` | Incidental "not ECR design" hits are not ECR artifacts. | Capture case migration. | Capture inventory owns move; ECR should not absorb. |
| `orca-harness/source_capture/**` and `orca-harness/runners/run_source_capture_*` | Source Capture packet producers/runners | Capture-owned shared harness | Capture harness pointer; ECR pointer only to packet contract | `pointer_only` | ECR consumes SourceCapturePacket; it does not own capture code. | Capture spine migration; source-capture packet contract. | Capture tests, runner contracts, no ECR code move. |
| `.agents/workflow-overlay/source-loading.md` | ECR read-pack pointer | Global overlay authority | Remains global; future ECR spine README points to it | `do_not_move` | Overlay stays global governance. | Overlay binding. | No ECR move; only pointer update if source-loading path changes. |
| `.agents/workflow-overlay/safety-rules.md` | Gate/safety boundaries | Global overlay authority | Remains global; future ECR spine README points to it | `do_not_move` | Global safety rules; not product-spine local. | Overlay binding. | No ECR move. |
| `docs/workflows/orca_repo_map_v0.md` | Global repo map | Global workflow navigation | Future `orca/docs/workflows/orca_repo_map_v0.md` if global docs root accepted | `do_not_move` | Repo-wide map should not become ECR-local. | PR #239. | Map update after actual moves. |
| `repo-structure.yaml` | Machine structure map | Global router | Root/global map, not ECR | `do_not_move` | Placement router stays global. | PR #239 acceptance. | Placement checker after binding changes. |

## Search Families Not Individually Migrated

The broad `rg -n` search found many files that mention ECR only as a non-goal,
non-claim, or downstream boundary. These are not ECR artifacts:

| Family | Treatment | Why |
| --- | --- | --- |
| `docs/product/data_capture_spine/data_capture_spine_pressure_test_*.md` | Capture-owned; do not move with ECR | They use `categorical_handoff_to_ECR` or "no ECR schema" language to preserve Capture boundaries. |
| `docs/product/source_capture_toolbox/**` | Capture/Source Capture owned; pointer only when a specific packet contract is needed | The toolbox does source access and packet production, not ECR schema/receipt ownership. |
| `orca-harness/cases/product_learning/**/source_captures/**` | Capture/case provenance; do not move with ECR | Receipts/manifests commonly state "not ECR design." |
| `docs/review-inputs/**/sources/**` and copied source bundles | Excluded unless a future review provenance move needs an example | Canonical artifacts remain elsewhere; copied review inputs are not live authority. |
| `_scratch/**`, old worktrees, generated caches | Excluded | Not durable migration targets. |

## Proposed Future ECR Spine Shape

Pending accepted binding, use this target shape:

```text
orca/product/spines/ecr/
  README.md
  spine.yaml
  authority/
    pointers/
  plans/
  prompts/
    reviews/
  workflows/
  reviews/
  harness/
  tests/
  migrations/
  archive/
```

Notes:

- Add pointer docs before moving executable code. `orca-harness/ecr/`, `orca-harness/evidence_binding/`, `orca-harness/schemas/finalization_models.py`, and related tests remain executable harness surfaces until a separate code-root migration is accepted.
- Do not place Signal Content or Signal Statement under ECR. It is a sibling spine, even when it shares the derived-record discipline and references ECR posture keys.
- Do not place the JSG-01 conductor, unfreeze decisions, SP-5 finalization authority, or Judgment gate ownership under ECR. ECR may point to them.
- Review outputs can move only as provenance/archive. They do not become live authority by location.

## Move Ordering Recommendation

Do not move ECR before the global structure binding and the Commission Signal Board pilot. The open structure proposal explicitly rejects starting with ECR because ECR has cross-references, review bundles, runtime surfaces, and active adjacent renames. Moving it early would create avoidable path churn and a high chance of accidentally claiming ownership over Signal Content/Signal Statement, JSG-01, Capture, or shared harness surfaces.

Recommended order:

1. Settle PR #239 or its successor and bind `orca/product/spines/` if accepted.
2. Let the Commission Signal Board pilot prove the spine grammar and moved-path-index mechanics.
3. Settle Foundation rename PR #242 and Signal Statement rename PR #237, or rebase this inventory against their final states.
4. Create ECR pointer docs (`README.md`, `spine.yaml`, `authority/pointers/`, `harness/`, `tests/`) before moving source artifacts.
5. Move ECR-owned docs/prompts/reviews in one bounded migration package with a moved-path index.
6. Leave code under `orca-harness/` unless a separate accepted code-root migration authorizes executable moves.

## Non-Claims

- Not a source move.
- Not implementation.
- Not validation or readiness.
- Not proof that the proposed spine-first structure will be accepted.
- Not ECR ownership of Signal Content/Signal Statement.
- Not ECR ownership of JSG-01, SP-5 finalization, the conductor, or the final Evidence Unit architecture.
- Not Capture ownership change.
- Not review-output authority promotion.
