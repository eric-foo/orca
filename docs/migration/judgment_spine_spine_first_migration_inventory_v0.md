# Judgment Spine Spine-First Migration Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: Migration inventory (spine-first marking; docs-only)
scope: >
  Marks visible Judgment Spine and Judgment-adjacent documents for a future
  spine-first migration under `orca/product/spines/judgment/`, without moving
  files or changing current repo-structure binding.
use_when:
  - Planning the Judgment Spine phase of a spine-first Orca workspace migration.
  - Deciding which Judgment documents belong in the future Judgment spine versus global/shared homes.
  - Preparing a later migration manifest or moved-path index for Judgment-related documents.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/orca_spine_first_workspace_structure_proposal_v0.md
  - docs/decisions/orca_repo_structure_binding_v0.md
  - docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md
  - docs/workflows/orca_repo_map_v0.md
stale_if:
  - The spine-first workspace proposal is accepted, rejected, or materially amended.
  - Judgment Spine files move or new Judgment submaps are added.
  - A later migration manifest supersedes this class-level inventory.
```

- Status: MIGRATION_MARKING_ONLY.
- Branch basis: `codex/commission-spine-structure` at
  `14ba32adfd3082f069971d2f7a34a7a943c09804` when this inventory was drafted.
- Current binding remains `docs/` plus `orca-harness/`; this file does not make
  `orca/product/spines/judgment/` live.
- No file moves, rewrites, archive decisions, runtime changes, test moves, or
  reference rewrites are authorized by this inventory.

## Target Spine

Proposed future root, only after a later accepted repo-structure migration:

```text
orca/product/spines/judgment/
  README.md
  spine.yaml
  authority/
  decisions/
  prompts/
  workflows/
  research/
  cases/
  reviews/
  reports/
  harness/
  tests/
  migrations/
  archive/
```

## Inventory Method

Searches run from the worktree root:

```powershell
rg --files docs\product\judgment_spine
rg --files docs\research\judgment-spine
rg --files docs\prompts | rg -i "judg|judgement|jsg|conductor|blind|memorization|fixture"
rg --files docs\decisions | rg -i "judg|judgement|jsg|distillation_binding_judgment|wind_caller|moat_judgment"
rg --files docs\review-inputs docs\review-outputs | rg -i "judg|judgement|jsg|conductor|blind|contestant|canoo_walmart|daimler|unity_v0_14|fixture"
rg --files orca-harness\cases orca-harness\reports | rg -i "\.md$|\.yaml$|\.yml$"
```

Observed candidate counts from those searches:

| Surface | Count | Marking strength |
| --- | ---: | --- |
| `docs/product/judgment_spine/*.md` | 24 | Direct Judgment authority candidates. |
| `docs/research/judgment-spine/**` | 100 | Direct Judgment research/case/harness candidates. |
| Judgment/JSG prompt hits under `docs/prompts/**` | 27 | Prompt candidates; some ECR/JSG prompts need shared-boundary review. |
| Judgment/JSG decision hits under `docs/decisions/**` | 12 | Decision candidates; some are global/shared rather than spine-local. |
| Judgment/fixture/review hits under `docs/review-inputs/**` and `docs/review-outputs/**` | 120 | Mostly spine-local review history, but case and ECR/shared reviews need classification. |
| Human-readable `orca-harness/cases/**` and `orca-harness/reports/**` docs | 279 | Harness/runtime case artifacts; mark for pointer/case-plan treatment, not immediate move. |

These counts are search-observed, not validation or migration completeness. The
large review and harness surfaces are intentionally class-marked below rather
than converted into a hand-maintained 300-row move manifest.

## 5.3 Explorer Reconciliation

Three read-only 5.3 explorers inspected separate Judgment-related surfaces. The
explorers agreed on the major candidate pools but disagreed on some boundary
calls. This inventory uses the conservative current-binding rule: mark likely
future homes, but do not move shared, runtime, consulting, or cross-spine
artifacts without a later accepted migration manifest.

| Explorer surface | Finding | Reconciled mark |
| --- | --- | --- |
| Product/research Judgment tree | Confirmed `docs/product/judgment_spine/` and `docs/research/judgment-spine/` as first-order Judgment trees. | Preserved direct/path-class marks into proposed `orca/product/spines/judgment/` slots. |
| Prompts, decisions, reviews, and workflows outside the Judgment tree | Found 13 decision, 2 hygiene, 29 prompt, 52 review-input, 24 review-output, and 22 workflow hits, including false-positive/global hits. | Added class marks and separated global/shared false positives from spine-local candidates. |
| Harness/case/report docs | Found 15 `blind_judgement.yaml` artifacts under `orca-harness/cases/**` plus 57 harness-facing docs under `docs/research/judgment-spine/harness/**`. | Marks `docs/research/judgment-spine/harness/**` for future migration, but keeps `orca-harness/` runtime and case artifacts in place for now. |

## Direct Authority Candidates

All files under `docs/product/judgment_spine/` are marked as future Judgment
spine authority candidates:

```text
docs/product/judgment_spine/*.md
  -> orca/product/spines/judgment/authority/
```

Current files observed:

| Current path | Proposed target slot | Migration mark |
| --- | --- | --- |
| `docs/product/judgment_spine/conductor_construction_integrity_probe_addendum_proposal_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/conductor_construction_integrity_probe_addendum_v1.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/demand_read_core_adoption_and_ledger_first_direction_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/jsg01_source_side_receipt_translator_v0.md` | `authority/` or `harness/` boundary | migrate_later_with_ECR_check |
| `docs/product/judgment_spine/jsg01_sp6_source_visibility_derivation_architecture_plan_v0.md` | `authority/` or `harness/` boundary | migrate_later_with_ECR_check |
| `docs/product/judgment_spine/jsg01_sp6_source_visibility_derivation_architecture_routing_v0.md` | `workflows/` or `authority/` | migrate_later_with_ECR_check |
| `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/judgment_spine_c2_ledger_read_contract_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/judgment_spine_c2_qualitative_read_feasibility_probe_v0.md` | `research/` or `authority/` | migrate_later_classify |
| `docs/product/judgment_spine/judgment_spine_c2_qualitative_read_feasibility_probe_v1.md` | `research/` or `authority/` | migrate_later_classify |
| `docs/product/judgment_spine/judgment_spine_c2_qualitative_read_feasibility_probe_v2.md` | `research/` or `authority/` | migrate_later_classify |
| `docs/product/judgment_spine/judgment_spine_c2_rule3_reground_phase_a_classification_finding_v0.md` | `research/` or `authority/` | migrate_later_classify |
| `docs/product/judgment_spine/judgment_spine_c3_verdict_action_ceiling_contract_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/judgment_spine_demand_read_grading_rubric_v0.md` | `authority/` or `harness/` | migrate_later_classify |
| `docs/product/judgment_spine/judgment_spine_demand_read_machinery_architecture_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/judgment_spine_first_demand_read_scope_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/judgment_spine_reveal_calibration_owner_contract_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/judgment_spine_toolkit_blocker_specs_from_daimler_source_fanout_v0.md` | `harness/` or `cases/daimler-carve-out/` | migrate_later_classify |
| `docs/product/judgment_spine/near_half_backtest_learning_architecture_v0.md` | `research/` or `authority/` | migrate_later_classify |
| `docs/product/judgment_spine/near_half_signal_reliability_ledger_v0.md` | `research/` or `reports/` | migrate_later_classify |
| `docs/product/judgment_spine/prospective_decision_loop_phase0_semantics_spec_v0.md` | `authority/` | migrate_later |
| `docs/product/judgment_spine/prospective_decision_loop_target_architecture_v0.md` | `authority/` | migrate_later |

## Research, Case, And Harness Candidates

Direct Judgment research tree:

```text
docs/research/judgment-spine/
  -> orca/product/spines/judgment/research/
```

Class-level marks:

| Current path class | Proposed target slot | Migration mark |
| --- | --- | --- |
| `docs/research/judgment-spine/README.md` | `README.md` or `research/README.md` | migrate_later_as_spine_front_door_candidate |
| `docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md` | `workflows/` | migrate_later_front_door |
| `docs/research/judgment-spine/manifest_v0.md` | `research/` or `cases/` | migrate_later |
| `docs/research/judgment-spine/judgment_spine_thesis*` | `authority/` or `research/` | migrate_later_classify |
| `docs/research/judgment-spine/*spec*` | `harness/` | migrate_later_classify |
| `docs/research/judgment-spine/*test_run_report*` | `reports/` | migrate_later |
| `docs/research/judgment-spine/cases/**` | `cases/` | migrate_later |
| `docs/research/judgment-spine/harness/**` | `harness/` | migrate_later |
| `docs/research/judgment-spine/harness/v0_14/fixtures/**` | `harness/fixtures/` or `cases/fixtures/` | migrate_later_classify |
| `docs/research/judgment-spine/harness/v0_14/smoke_tests/**` | `harness/smoke_tests/` or `reports/smoke_tests/` | migrate_later_classify |
| `docs/research/judgment-spine/harness/v0_14/review_prompts/**` | `prompts/reviews/` or `harness/review_prompts/` | migrate_later_classify |

Do not collapse case artifacts, harness specs, smoke receipts, and research
synthesis into one folder. The future spine should preserve the internal role
grammar.

## Prompt Candidates

Judgment-related prompt artifacts are marked for a future
`orca/product/spines/judgment/prompts/` home, but not all should move blindly.
ECR/JSG prompts need boundary review because some belong to ECR/source-side
work rather than Judgment.

| Current path class | Proposed target slot | Migration mark |
| --- | --- | --- |
| `docs/prompts/deep-thinking/judgment_spine_*` | `prompts/deep-thinking/` | migrate_later |
| `docs/prompts/deep-thinking/orca_judgment_spine_*` | `prompts/deep-thinking/` | migrate_later |
| `docs/prompts/handoffs/judgment_spine_*` | `prompts/handoffs/` | migrate_later |
| `docs/prompts/handoffs/orca_judgment_spine_*` | `prompts/handoffs/` | migrate_later |
| `docs/prompts/handoffs/captured_candidate_cases_to_judgment_spine_*` | `prompts/handoffs/` | migrate_later_classify |
| `docs/prompts/handoffs/batch2_*blind*` | `prompts/handoffs/` | migrate_later_classify |
| `docs/prompts/reviews/judgment_spine_*` | `prompts/reviews/` | migrate_later |
| `docs/prompts/reviews/*v0_14*fixture*` | `prompts/reviews/` or `cases/<case>/reviews/` | migrate_later_classify |
| `docs/prompts/reviews/jsg01_*` | `prompts/reviews/` or shared ECR/JSG boundary | migrate_later_with_ECR_check |
| `docs/prompts/architecture/jsg01_*` | `prompts/architecture/` or shared ECR/JSG boundary | migrate_later_with_ECR_check |
| `docs/prompts/wrappers/canoo_walmart_fixture_handoff_source_loading_wrapper_v0.md` | `prompts/wrappers/` or `cases/canoo-walmart/prompts/` | migrate_later_classify |

Observed prompt hit count: 27.

Explorer note: one 5.3 pass marked
`docs/prompts/handoffs/captured_candidate_cases_to_judgment_spine_backtest_batch_handoff_v0.md`
as global/cross-spine. Treat that path family as `migrate_later_classify`, not
a blind move, because it bridges captured candidates into Judgment rather than
originating wholly inside Judgment.

## Decision Candidates

Decision records should not move until the global `orca/docs/decisions/` versus
spine-local `orca/product/spines/judgment/decisions/` split is accepted. These
are marked now for later classification:

| Current path | Proposed target slot | Migration mark |
| --- | --- | --- |
| `docs/decisions/distillation_binding_judgment_spine_v0.md` | `decisions/` | migrate_later |
| `docs/decisions/judgment_spine_backtest_batch1_ledger_declaration_v0.md` | `decisions/` | migrate_later |
| `docs/decisions/judgment_spine_backtest_batch2_band_ratification_v0.md` | `decisions/` | migrate_later |
| `docs/decisions/judgment_spine_backtest_batch2_candidate_routing_v0.md` | `decisions/` | migrate_later |
| `docs/decisions/judgment_spine_backtest_batch2_ledger_declaration_v0.md` | `decisions/` | migrate_later |
| `docs/decisions/judgment_spine_pre_sale_execution_evidence_tier_policy_v0.md` | `decisions/` | migrate_later |
| `docs/decisions/jsg01_unfreeze_decision_memo_v0.md` | `decisions/` or shared ECR/JSG boundary | migrate_later_with_ECR_check |
| `docs/decisions/jsg01_unfreeze_decision_v0.md` | `decisions/` or shared ECR/JSG boundary | migrate_later_with_ECR_check |
| `docs/decisions/orca_moat_judgment_quality_proof_path_decision_chain_v0.md` | `decisions/` or global product strategy | migrate_later_classify |
| `docs/decisions/wind_caller_calibration_carveout_v0.md` | `decisions/` or product/shared calibration | migrate_later_classify |
| `docs/decisions/consultant_loop/milwaukee_initial_judgement.md` | `decisions/` or `orca/docs/decisions/consultant_loop/` | classify_consulting_judgment_before_move |
| `docs/decisions/consultant_loop/milwaukee_owner_judgement.md` | `decisions/` or `orca/docs/decisions/consultant_loop/` | classify_consulting_judgment_before_move |

## Review Candidate Classes

Review artifacts are largely spine-local historical evidence, but the global
review-lane doctrine stays global. Mark review outputs by ownership:

| Current path class | Proposed target slot | Migration mark |
| --- | --- | --- |
| `docs/review-inputs/judgment_conductor_*` | `reviews/inputs/` | migrate_later |
| `docs/review-inputs/blind_judgement_execution_receipt_*` | `reviews/inputs/` or `harness/reviews/` | migrate_later_classify |
| `docs/review-outputs/adversarial-artifact-reviews/judgment_*` | `reviews/outputs/` | migrate_later |
| `docs/review-outputs/adversarial-artifact-reviews/judgment_conductor_*` | `reviews/outputs/` | migrate_later |
| `docs/review-outputs/adversarial-artifact-reviews/conductor_*` | `reviews/outputs/` | migrate_later |
| `docs/review-outputs/adversarial-artifact-reviews/contestant_*` | `harness/reviews/` | migrate_later_classify |
| `docs/review-outputs/adversarial-artifact-reviews/*jsg*` | `reviews/outputs/` or shared ECR/JSG boundary | migrate_later_with_ECR_check |
| `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_*` | `cases/canoo-walmart/reviews/` | migrate_later_classify |
| `docs/review-outputs/adversarial-artifact-reviews/daimler_*` | `cases/daimler-carve-out/reviews/` | migrate_later_classify |
| `docs/review-outputs/adversarial-artifact-reviews/unity_v0_14_*` | `harness/fixtures/unity_runtime_fee_2023_v0_14/reviews/` | migrate_later_classify |

Observed review input/output hit count: 120. Do not hand-move these without a
review-specific moved-path index and a rule for historical review bundles.

## Harness-Facing Documents

Human-readable `orca-harness/cases/**` and `orca-harness/reports/**` documents
are Judgment-relevant, but `orca-harness/` remains the executable/runtime tree
until a separate code-root migration is accepted.

Migration mark:

```text
orca-harness/cases/**/{participant_packet*.md,facilitator_ledger.yaml,source_provenance_notes*.md,packet_construction_receipt*.md,cross_vendor_blind_run_findings*.md,blind_judgement.yaml}
orca-harness/reports/product_learning/**/case_report.yaml
  -> stay in orca-harness for now
  -> future Judgment spine may add pointers or case indexes under cases/
```

If a later migration moves human-readable case artifacts out of
`orca-harness/`, it must separately decide whether code/runners/tests still read
the old paths. This inventory does not authorize that move.

## Shared Or Adjacent - Do Not Auto-Migrate

These surfaced in Judgment searches but should not be treated as Judgment Spine
move targets without owner/source-boundary review:

| Path class | Reason |
| --- | --- |
| `docs/product/ecr/*jsg01*` | ECR/source-side ownership boundary. |
| `docs/product/data_capture_spine/*fixture*` | Data Capture ownership boundary. |
| `docs/product/source_capture_toolbox/*fixture*` | Source Capture / fixture-admission boundary. |
| `docs/product/core_spine/*memorization*`, `docs/product/core_spine/*backtest_specimen*` | Core Spine ownership boundary. |
| `docs/research/consulting-judgment-corpus/**` | Consulting judgment corpus, not necessarily Judgment Spine. |
| `docs/decisions/consultant_loop/**` | Consultant-loop decision records; likely future global docs or separate consulting corpus. |
| Python code under `orca-harness/` | Runtime/code, not document migration. |

## Proposed Migration Sequence

1. Do not move Judgment first. Pilot Commission Signal Board before moving a
   high-reference spine.
2. After the root `orca/product` and `orca/docs` binding is accepted, create a
   Judgment migration manifest from this inventory.
3. Start with `docs/product/judgment_spine/*.md` and the Judgment consolidation
   map; these are the cleanest first-order authority/routing artifacts.
4. Migrate `docs/research/judgment-spine/**` in one case/harness-aware pass with
   a moved-path index.
5. Migrate prompts and review artifacts only after prompt/review path rules for
   spine-local versus global prompt homes are accepted.
6. Leave `orca-harness/` case/runtime files in place until a separate
   harness/code-root migration decision exists.

## Non-Claims

This inventory is not a move manifest, validation, readiness, acceptance,
source-of-truth promotion, proof of completeness, or implementation
authorization. It marks Judgment-related documents and classes for later
migration planning only.
