# Orca Harness Runtime Mapping Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: Migration inventory
scope: Inventory-only ownership map for orca-harness runtime, tests, fixtures, and adjacent docs before spine-first repo migration.
use_when:
  - Mapping orca-harness surfaces to product spines before moving or renaming code.
  - Checking stale placement or ownership risks for harness/runtime migration planning.
  - Onboarding a fresh agent to Capture, ECR/SCR, Cleaning, Judgment, Search, Foundation, CSB, and shared-infrastructure surfaces under orca-harness.
open_next:
  - docs/workflows/orca_repo_map_v0.md
  - docs/workflows/data_capture_spine_consolidation_map_v0.md
  - docs/workflows/ecr_spine_submap_v0.md
  - docs/product/source_capture_toolbox/README.md
  - docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md
stale_if:
  - orca-harness packages, runners, adapters, fixtures, or tests are added or reorganized.
  - docs/workflows/orca_repo_map_v0.md or docs/workflows/data_capture_spine_consolidation_map_v0.md changes harness routing.
  - ECR/SCR, Cleaning, Judgment, Search, Source Capture Armory, or company-signal ownership docs change.
authority_boundary: retrieval_only
```

## Purpose

This artifact marks the current `orca-harness/` runtime inventory before a spine-first repository migration. It maps code, tests, fixtures, reports, and runtime-adjacent docs to the likely owning product spines or shared substrates without moving code.

Use this as an orientation map, not as a migration execution plan, validation record, readiness claim, packaging claim, or authorization to rename packages.

## Start Preflight Receipt

```yaml
orca_start_preflight:
  agents_read: AGENTS.md
  overlay_read:
    - .agents/workflow-overlay/README.md
    - .agents/workflow-overlay/source-loading.md
    - .agents/workflow-overlay/prompt-orchestration.md
  status_checked: git status --short --branch
  retrieval_map_loaded: docs/workflows/orca_repo_map_v0.md
  route: complicated inventory-only docs-write
  isolation: isolated worktree on codex/harness-runtime-mapping-inventory because the main checkout was dirty
  tests_run: none
  test_reason: owner instruction said not to run tests unless separately authorized
  runtime_changes: none
```

Additional owning-rule context loaded for this inventory:

- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/decision-routing.md`
- `.agents/workflow-overlay/retrieval-metadata.md`
- `.agents/workflow-overlay/artifact-folders.md`
- `docs/workflows/artifact_retrievability_guide.md`

Source searches covered `orca-harness/`, `docs/workflows/orca_repo_map_v0.md`, `docs/product/`, `docs/decisions/`, `docs/migration/`, and references to `harness`, `fixture`, `runner`, `ecr`, `signal_content`, `source_capture`, `evidence_binding`, `cleaning`, `judgment`, and `scoring`.

`workflow-deep-thinking` was used after source context was ready to keep ownership mapping separate from implementation or migration execution.

## 1. Runtime / Code Surfaces Found

| Surface | Runtime/code found | Proposed owner | Docs that point at it | Inventory notes |
| --- | --- | --- | --- | --- |
| `orca-harness/source_capture/` | Packet models, writer, packet assembly and inspection, cadence, source quality, historical capture, block shell, local secret/auth/proxy helpers, Reddit/IG/Retail projection helpers. | Capture / Source Capture Armory under Data Capture Spine. | `docs/workflows/orca_repo_map_v0.md`; `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `docs/product/source_capture_toolbox/README.md`; `docs/product/data_capture_spine/core_spine_v0_data_capture_spine_obligation_contract_v0.md`; `docs/product/data_capture_spine/source_capture_packet_schema_evolution_architecture_v0.md`; `docs/product/data_capture_spine/source_capture_tenant_payload_attachment_boundary_v0.md`; `docs/decisions/source_capture_packet_fixture_retention_sensitivity_decision_v0.md`; `docs/decisions/source_capture_archive_snapshot_typed_timing_decision_v0.md`. | This is capture-side provenance and packet substrate. It does not own ECR, Cleaning, Judgment, scoring, or fixture admission. |
| `orca-harness/source_capture/adapters/` | Direct HTTP, media/asset, Archive.org, archive.today, browser snapshot, authenticated browser, Reddit API, anti-blocking HTTP, CloakBrowser, publisher history, Amazon delivery-location adapter surfaces. | Capture / Source Capture Armory adapter substrate. | `docs/product/source_capture_toolbox/README.md`; `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `orca-harness/docs/source_capture_agent_runbook.md`; `orca-harness/docs/adapter_author_contract.md`; `docs/product/source_capture_toolbox/reddit_capture_operator_playbook_v0.md`; `docs/product/source_capture_toolbox/source_access_auth_state_operator_contract_v0.md`. | Adapter presence is runtime inventory only. This does not claim broad crawling, storage, scheduling, dashboarding, deployment, or production operation. |
| Reddit capture/projection surfaces | `source_capture/reddit_consolidation/`, `source_capture/reddit_projection.py`, `source_capture/screening_reddit_read.py`, `source_capture/reddit_agent_view*.py`, `capture_spine/reddit_candidate_intake/`, `capture_spine/reddit_graph_frontier/`, Reddit runners. | Capture primary; Search is a product consumer for search-led and old-Reddit demand-signal surfaces. | `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `docs/product/source_capture_toolbox/reddit_capture_operator_playbook_v0.md`; `docs/product/data_capture_spine/*reddit*` records; `docs/decisions/orca_search_product_lane_binding_v0.md`; `docs/product/core_spine/beauty_venue_card_set_v0.md`. | Do not move the whole Reddit set as one unit without preserving the Capture owner and Search consumer distinction. |
| IG projection surfaces | `source_capture/ig_calls_parse.py`, `source_capture/ig_momentum_harvest.py`, `source_capture/ig_projection.py`, `runners/run_ig_creator_momentum_projection.py`. | Capture / Data Capture projection substrate. | `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `docs/product/source_capture_toolbox/README.md`; IG operating-envelope docs under `docs/product/source_capture_toolbox/`. | Inventory only; no claim of live IG acquisition, scheduler, or momentum-quality scoring. |
| Retail/PDP projection surfaces | `source_capture/retail_pdp_projection.py`, `source_capture/price_payload_extraction.py`, `runners/run_retail_pdp_projection.py`, `runners/run_source_capture_cloakbrowser_packet.py` sidecar path. | Capture / Source Capture Armory Retail/PDP projection substrate. | `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `docs/product/data_capture_spine/retail_pdp_typed_envelope_probe_v0.md`; Retail/PDP projection contract and playbook docs under `docs/product/data_capture_spine/`; `docs/product/source_capture_toolbox/README.md`. | Sidecar projection remains capture-side and separate from ECR, Cleaning, and Judgment. |
| `orca-harness/source_observability/` | Operator record parsing, posture checking, limitation reporting; related source-quality runners. | Capture support / Source Capture Armory source-observability substrate. | `docs/workflows/orca_repo_map_v0.md`; `docs/product/source_capture_toolbox/README.md`; `orca-harness/docs/source_observability_operator_records.md`; `orca-harness/docs/source_observability_scalability_note.md`; `orca-harness/docs/source_observability_operator_records_template.yaml`. | This is support/limitation reporting, not source acquisition, scoring, validation, or readiness proof. |
| `orca-harness/capture_spine/reddit_candidate_intake/` | Reddit candidate URL intake models, projection, and live runner support. | Capture Spine / Candidate URL Intake. | `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `docs/workflows/orca_repo_map_v0.md`; Candidate URL Intake docs under `docs/product/data_capture_spine/`. | Capture planning/runtime support; not packet output by itself unless routed through Source Capture Packet surfaces. |
| `orca-harness/capture_spine/reddit_graph_frontier/` | Graph frontier register, receipt, model helpers and runners. | Capture Spine / Reddit Graph Frontier. | `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `docs/workflows/orca_repo_map_v0.md`; Reddit Graph Frontier docs under `docs/product/data_capture_spine/`. | Non-claims in code/docstrings exclude ECR, Cleaning, Judgment, fixture admission, and commercial permission. |
| LinkedIn capture surfaces | `capture_spine/linkedin_lane/`, `capture_spine/linkedin_graph_frontier/`, `capture_spine/linkedin_live_adapter/`. | Data Capture / LinkedIn lane capture planning and adapter substrate. | `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `docs/product/data_capture_spine/data_capture_spine_linkedin_discovery_planning_lane_architecture_v0.md`; LinkedIn/Reddit concurrent structure docs under `docs/product/data_capture_spine/`. | Ownership should not be inferred from folder prefix alone; these are not the same surface as Reddit Candidate Intake. |
| `orca-harness/capture_spine/linkedin_live_runtime/` | No-live legal-gated runtime skeleton, live fetcher/extractor structure, company signal extraction model support. | CSB / company-aggregate forward-signal LinkedIn extraction adapter, consumed by Capture; LinkedIn lane remains a likely satellite owner. | `docs/decisions/company_aggregate_forward_signal_architecture_decision_v0.md`; `docs/decisions/company_aggregate_forward_signal_capture_lane_scope_decision_v0.md`; `docs/workflows/data_capture_spine_consolidation_map_v0.md`. | Exact CSB versus Capture versus LinkedIn-lane home is an owner question before moves. |
| `orca-harness/ecr/` | Source-side ECR models, builders, deriver, posture evaluation for SP-1/SP-2/SP-3/SP-6. | ECR/SCR integrity spine; Judgment consumes through JSG-01 boundary. | `docs/workflows/ecr_spine_submap_v0.md`; `docs/product/ecr/ecr_consolidation_v0_frame_source_visibility_slice_architecture_plan_v0.md`; `docs/product/ecr/ecr_consolidation_v0_sp1_sp2_sp3_source_side_slice_plan_v0.md`; `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md`. | ECR is a derived receipt/integrity layer over Source Capture Packet. It does not own capture, Cleaning, Evidence Unit final architecture, or Judgment readiness. |
| `orca-harness/signal_content/` | Signal Content Record models, validators, builders, deriver. | ECR/SCR content spine, parallel to ECR integrity records. | `docs/workflows/ecr_spine_submap_v0.md`; `docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md`; `docs/product/signal_content/signal_content_record_deriver_architecture_plan_v0.md`; `docs/workflows/orca_repo_map_v0.md`. | Stale-risk surface: the repo map describes no SCR deriver, while code currently contains `signal_content/deriver.py`. |
| `orca-harness/evidence_binding/` | Minimal composition and claim-support verification layer above source-side ECR/SCR surfaces. | Foundation / ECR-to-Judgment binding substrate; shared boundary between ECR/SCR and Judgment. | `docs/workflows/ecr_spine_submap_v0.md`; `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md`; ECR/JSG-01 binding docs under `docs/product/ecr/` and `docs/product/judgment_spine/`. | Owner is unclear enough that it should not be absorbed into pure ECR or pure Judgment without owner decision. |
| `orca-harness/cleaning/` | Cleaning models, exact-identity deriver, validators, package boundary. | Cleaning Spine bounded substrate. | `docs/product/core_spine/core_spine_v0_cleaning_spine_foundation_v0.md`; Cleaning projection/contract docs under `docs/product/core_spine/`; `docs/workflows/orca_repo_map_v0.md`. | Cleaning is non-destructive transformation over raw/projection/ECR handles. It does not replace raw, finalize ECR, or make Judgment claims. |
| `orca-harness/schemas/` | Case, finalization, judgement, probe, scoring, and fixture schema models. | Judgment Harness Foundation, with boundary-specific shared models for ECR/JSG finalization and scoring. | `docs/workflows/orca_repo_map_v0.md`; `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md`; `docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md`; no-case smoke and judgment-gate decisions under `docs/decisions/`. | `finalization_models.py` is bridge-shaped; `scoring_models.py` is Judgment scoring; package should not be treated as one single product owner without file-level review. |
| `orca-harness/scoring/` | Deterministic band scorer and mapping table. | Judgment Spine / deterministic scoring substrate, especially JSG-07. | `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md`; `docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md`; judgment backtest decisions under `docs/decisions/`; `docs/workflows/orca_repo_map_v0.md`. | Deterministic scoring is not a judgment-quality proof and does not authorize label repair or missing-input repair. |
| Judgment runners | `runners/run_case.py`, `runners/score_external_run.py`, `runners/run_memorization_probe.py`, `runners/run_memorization_probe_raw_api.py`, `runners/run_finalization_receipt.py`. | Judgment runtime/plumbing, with finalization bridging ECR/SCR into JSG-01. | `orca-harness/README.md`; `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md`; `docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md`; no-case smoke authorization docs under `docs/decisions/`; pre-sale evidence policy docs under `docs/product/judgment_spine/`. | Runner presence is not authorization to execute probes or claim readiness. |
| Capture runners | `runners/run_source_capture_*.py`, `runners/run_reddit_*.py`, `runners/run_retail_pdp_projection.py`, `runners/run_ig_creator_momentum_projection.py`, `runners/run_source_observability_report.py`, source-quality runners. | Capture / Source Capture Armory and related capture-spine slices. | `docs/product/source_capture_toolbox/README.md`; `docs/workflows/data_capture_spine_consolidation_map_v0.md`; harness runbook docs; adapter author contract; Reddit operator playbook. | Some runners are packet-producing, some projection-producing, and some report-only; preserve those distinctions during migration. |
| `orca-harness/reports/` | `case_report.py` plus product-learning report artifacts. | Judgment/Product Learning reporting substrate; shared report artifact area. | `docs/workflows/orca_repo_map_v0.md`; judgment backtest decisions under `docs/decisions/`; product-learning case docs. | Separate report-rendering code from generated or historical report artifacts before moving. |
| `orca-harness/config/` | Static YAML consumed by harness runners. | Shared harness infrastructure, currently Judgment-leaning by runner usage. | `docs/workflows/orca_repo_map_v0.md`; `orca-harness/README.md`; runner references. | Config ownership should follow consuming runner ownership, not current folder placement. |
| Shared package/runtime metadata | `harness_utils.py`, `Makefile`, `pyproject.toml`, `uv.lock`. | Shared harness infrastructure / Foundation. | `docs/workflows/orca_repo_map_v0.md`; `orca-harness/README.md`; packaging metadata itself. | `pyproject.toml` still describes the package as a deterministic Step A judgment harness despite broader runtime surfaces. |
| `orca-harness/docs/` | Source Capture packet/runbook/adapter docs, source-observability docs, source-capture review rendering findings, `v0_14/README.md`. | Mixed: Capture docs, Source Observability docs, Judgment Harness v0.14 docs. | Referenced by `docs/product/source_capture_toolbox/README.md`, `docs/workflows/data_capture_spine_consolidation_map_v0.md`, `docs/workflows/orca_repo_map_v0.md`, and source-capture fixture decisions. | This directory should be split by owning spine or marked as runtime-adjacent docs during migration. |

## 2. Test And Fixture Surfaces Found

| Surface | Tests/fixtures found | Proposed owner | Docs that point at it | Inventory notes |
| --- | --- | --- | --- | --- |
| `orca-harness/tests/unit/test_source_capture_*` and related source tests | Source packet models, writer, adapters, source quality, observability, block shell, auth/local secret, durability, Retail/PDP, IG, Reddit surfaces. | Capture / Source Capture Armory. | `docs/product/source_capture_toolbox/README.md`; `docs/workflows/data_capture_spine_consolidation_map_v0.md`; Source Capture Packet and adapter docs. | Test names should be preserved until owners decide package moves; this inventory did not run them. |
| Reddit tests and fixture | Reddit candidate intake, graph frontier, old Reddit screening, consolidation, quality summary, `tests/fixtures/reddit_candidate_intake/old_reddit_listing_noisy.html`. | Capture primary; Search consumer for old-Reddit/search-led demand-signal surfaces. | Reddit capture/operator docs; data capture map; Search lane binding docs; beauty venue card docs. | Fixture is capture/search support, not Judgment evidence by default. |
| LinkedIn tests | LinkedIn lane, graph frontier, live adapter/runtime tests. | Data Capture / LinkedIn lane; CSB for company-signal extraction tests if tied to `linkedin_live_runtime`. | LinkedIn discovery planning docs; company aggregate signal decisions. | File-level owner split is needed before migration. |
| ECR/SCR tests | ECR builders/deriver/tests, Signal Content Record tests, finalization receipt/model tests, claim support verifier, evidence binding tests. | ECR/SCR plus Foundation/Judgment boundary. | `docs/workflows/ecr_spine_submap_v0.md`; ECR and SCR architecture docs; Judgment conductor docs. | Keep ECR, SCR, finalization, and evidence-binding tests distinct during migration. |
| Cleaning tests | `test_cleaning_*` surfaces. | Cleaning Spine. | `docs/product/core_spine/core_spine_v0_cleaning_spine_foundation_v0.md`. | Bounded substrate tests only; no broader cleaning readiness claim. |
| Judgment/scoring tests | Band scorer, mapping table, schema validation, run-case, memorization-probe, external scoring, runner artifact tests. | Judgment Spine / Judgment Harness Foundation. | Judgment quality promotion operating model; gate ownership map; no-case smoke decisions. | Test existence does not authorize probe execution or scoring readiness claims. |
| Contract tests | No-LLM-import guard, no-tools memorization contract, finalization model contract, runner artifact contracts, capture contracts. | Shared infrastructure plus owning gate-specific spines. | Harness README; Judgment and Capture docs; repo map. | Contract tests are migration-critical because they encode boundary restrictions. They were not run here. |
| Integration tests | `tests/integration/test_run_case_tr_casetext.py`, `tests/integration/test_reddit_screening_read_live.py`. | Judgment plumbing fixture for TR/Casetext; Capture/Search for Reddit screening live surface. | Harness README; Reddit capture docs; Judgment plumbing/backtest docs. | Live or integration naming is not a license to execute. Owner instruction blocked test execution. |
| `orca-harness/cases/plumbing/tr_casetext_2023_v0_14/` | Fixed TR/Casetext plumbing fixture with evidence and run material. | Judgment Harness / deterministic plumbing fixture. | `orca-harness/README.md`; `docs/workflows/orca_repo_map_v0.md`; Judgment backtest and harness docs. | Historical fixture should stay traceable as Judgment plumbing, not Capture runtime. |
| `orca-harness/cases/product_learning/*` | Product-learning case corpus with evidence, runs, raw/source-capture material, and case metadata. | Judgment/Product Learning case corpus, with embedded Capture source-capture fixtures and evidence substrate. | Judgment backtest decisions under `docs/decisions/`; `docs/workflows/orca_repo_map_v0.md`; product-learning report references. | Do not split case directories mechanically without owner policy for source-captures, evidence, runs, and raw material. |
| `orca-harness/cases/product_learning/jsg01_binding_assembly_proof_v0/` | JSG-01 binding assembly proof fixture. | ECR/SCR to Judgment boundary; likely Foundation-owned proof fixture. | ECR submap; Judgment conductor docs; ECR/JSG-01 binding docs. | Ownership is unclear enough to require owner decision before migration. |
| `orca-harness/reports/product_learning/*` | Product-learning report artifacts. | Judgment/Product Learning reporting artifacts. | Judgment backtest decisions; repo map. | Separate generated or historical reports from report code during migration. |

## 3. Proposed Owning Spine Or Shared Substrate By Surface

| Owning spine / substrate | Surfaces currently under `orca-harness/` |
| --- | --- |
| Capture / Source Capture Armory | `source_capture/`, `source_capture/adapters/`, `source_capture/reddit_consolidation/`, packet/projection/source-quality runners, `source_observability/`, capture-facing harness docs. |
| Capture Spine / Reddit Candidate and Graph Frontier | `capture_spine/reddit_candidate_intake/`, `capture_spine/reddit_graph_frontier/`, related runners and tests. |
| Capture / LinkedIn lane | `capture_spine/linkedin_lane/`, `capture_spine/linkedin_graph_frontier/`, `capture_spine/linkedin_live_adapter/`, part of `capture_spine/linkedin_live_runtime/`. |
| CSB / company-aggregate signal | Company-signal extraction parts of `capture_spine/linkedin_live_runtime/`, especially minimized company signal extraction and fetcher/runtime hooks. |
| Search consumer surface | Old-Reddit screening, Reddit candidate intake fixtures, search-led demand-signal capture docs; likely consumer, not primary runtime owner. |
| ECR/SCR | `ecr/`, `signal_content/`, ECR/SCR builders, derivers, validators, and related tests. |
| Foundation / ECR-Judgment boundary | `evidence_binding/`, `schemas/finalization_models.py`, `runners/run_finalization_receipt.py`, JSG-01 proof fixtures. |
| Cleaning | `cleaning/` and `test_cleaning_*`. |
| Judgment / Judgment Harness Foundation | `schemas/` files for case/judgement/probe/scoring, `scoring/`, Judgment runners, TR/Casetext fixture, product-learning cases and reports. |
| Shared harness infrastructure | `harness_utils.py`, `Makefile`, `pyproject.toml`, `uv.lock`, `config/`, cross-spine contract tests. |

## 4. Docs That Point At Runtime Surfaces

| Runtime surface group | Primary pointing docs found |
| --- | --- |
| Whole `orca-harness/` tree | `docs/workflows/orca_repo_map_v0.md`; `orca-harness/README.md`. |
| Source Capture Packet and adapters | `docs/product/source_capture_toolbox/README.md`; `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `orca-harness/docs/source_capture_packet.md`; `orca-harness/docs/source_capture_agent_runbook.md`; `orca-harness/docs/adapter_author_contract.md`; `docs/decisions/source_capture_packet_fixture_retention_sensitivity_decision_v0.md`; `docs/decisions/source_capture_archive_snapshot_typed_timing_decision_v0.md`. |
| Source quality and observability | `docs/product/source_capture_toolbox/README.md`; `orca-harness/docs/source_observability_operator_records.md`; `orca-harness/docs/source_observability_scalability_note.md`; source-quality state assembler docs under `docs/product/source_capture_toolbox/`. |
| Data Capture projections and storage | `docs/workflows/data_capture_spine_consolidation_map_v0.md`; `docs/product/data_capture_spine/orca_capture_projection_storage_spine_architecture_v0.md`; `docs/product/data_capture_spine/capture_envelope_durability_delta_spec_v0.md`; `docs/product/data_capture_spine/source_capture_tenant_payload_attachment_boundary_v0.md`; `docs/product/data_capture_spine/source_capture_packet_schema_evolution_architecture_v0.md`. |
| Retail/PDP | `docs/product/data_capture_spine/retail_pdp_typed_envelope_probe_v0.md`; Retail/PDP projection contract, sidecar, and playbook docs under `docs/product/data_capture_spine/`; `docs/workflows/data_capture_spine_consolidation_map_v0.md`. |
| Reddit capture and candidate surfaces | `docs/product/source_capture_toolbox/reddit_capture_operator_playbook_v0.md`; `docs/workflows/data_capture_spine_consolidation_map_v0.md`; Reddit Candidate URL Intake and Reddit Graph Frontier docs under `docs/product/data_capture_spine/`; `docs/decisions/orca_search_product_lane_binding_v0.md`; `docs/product/core_spine/beauty_venue_card_set_v0.md`. |
| LinkedIn and company-signal surfaces | `docs/product/data_capture_spine/data_capture_spine_linkedin_discovery_planning_lane_architecture_v0.md`; `docs/decisions/company_aggregate_forward_signal_architecture_decision_v0.md`; `docs/decisions/company_aggregate_forward_signal_capture_lane_scope_decision_v0.md`. |
| ECR | `docs/workflows/ecr_spine_submap_v0.md`; `docs/product/ecr/ecr_consolidation_v0_frame_source_visibility_slice_architecture_plan_v0.md`; `docs/product/ecr/ecr_consolidation_v0_sp1_sp2_sp3_source_side_slice_plan_v0.md`; Judgment conductor docs. |
| SCR | `docs/workflows/ecr_spine_submap_v0.md`; `docs/product/signal_content/core_spine_v0_signal_content_record_architecture_v0.md`; `docs/product/signal_content/signal_content_record_deriver_architecture_plan_v0.md`. |
| Evidence binding and finalization | `docs/workflows/ecr_spine_submap_v0.md`; `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md`; ECR/JSG-01 boundary docs under `docs/product/ecr/` and `docs/product/judgment_spine/`. |
| Cleaning | `docs/product/core_spine/core_spine_v0_cleaning_spine_foundation_v0.md`; Cleaning projection and boundary docs under `docs/product/core_spine/`. |
| Judgment scoring and runners | `docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md`; `docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md`; judgment backtest decisions under `docs/decisions/`; no-case smoke authorization docs under `docs/decisions/`. |
| Product-learning cases and reports | Judgment backtest batch decisions under `docs/decisions/`; `docs/workflows/orca_repo_map_v0.md`; `orca-harness/README.md`. |

## 5. Runtime Surfaces With Unclear Ownership

- `orca-harness/evidence_binding/`: bridges ECR/SCR and Judgment. Proposed migration owner is Foundation / ECR-Judgment boundary, but source docs also point through ECR and Judgment. It should not be moved under only one side without owner decision.
- `orca-harness/schemas/`: mixes case, judgement, scoring, probe, finalization, and fixture models. It may need file-level ownership instead of a single package-level move.
- `orca-harness/capture_spine/linkedin_live_runtime/`: company-signal extraction ties to CSB/company-aggregate signal decisions, while runtime placement and surrounding files sit in Capture/LinkedIn lane. Owner decision needed.
- `orca-harness/capture_spine/` as a whole: includes Reddit Candidate Intake, Reddit Graph Frontier, LinkedIn lane, LinkedIn graph frontier, LinkedIn live adapter, and company-signal runtime hooks. The directory is not one product spine.
- `orca-harness/cases/product_learning/*`: product-learning case folders mix Judgment case material, embedded Capture source captures, raw materials, evidence, and runs. Migration should not split or retain them blindly.
- `orca-harness/reports/product_learning/*`: may be generated or historical reporting artifacts rather than runtime code. Retention and destination need owner policy.
- `orca-harness/config/`: shared runner config should follow the consuming runner owners, but current files are grouped as harness infrastructure.
- `orca-harness/docs/source_capture_review_rendering_findings_v0.md`: runtime-adjacent review/rendering findings may belong with Capture docs, migration notes, or review artifacts depending on retention policy.

## 6. Stale Naming Or Stale Placement Risks

- `orca-harness/README.md` and `orca-harness/pyproject.toml` still describe the package primarily as a deterministic Step A judgment harness, while the tree now contains Capture, Source Capture Armory, ECR/SCR, Cleaning, source-observability, LinkedIn/CSB-adjacent runtime slices, and shared infrastructure.
- `orca-harness/pyproject.toml` package discovery includes `cleaning`, `ecr`, `capture_spine*`, `runners`, `schemas`, `scoring`, `source_capture*`, and `source_observability`, but does not list `signal_content` or `evidence_binding` even though both code directories exist. This inventory does not claim packaging failure; it marks a packaging-risk surface.
- `docs/workflows/orca_repo_map_v0.md` describes `orca-harness/signal_content/` as having no deriver, while the tree contains `signal_content/deriver.py`.
- Judgment/ECR docs contain mixed state language around JSG-01 and ECR/SCR finalization boundaries. Some docs route current built surfaces through finalization and evidence binding, while other notes preserve frozen or deferred wording. This inventory does not resolve that doctrine conflict.
- The module `schemas/judgement_models.py` uses the spelling `judgement`, while product docs generally use `Judgment`. Rename risk should be handled only through owner-approved compatibility planning.
- `source_capture_toolbox` is the current doc path for Source Capture Armory. Migration should preserve links or add redirects/markers if display naming changes.
- Search-linked Reddit surfaces are capture-owned runtime surfaces with Search as a product consumer. Treating them as pure Search runtime would blur source acquisition and demand-signal interpretation.
- `reports/product_learning/*` and `cases/product_learning/*/runs` can look like runtime outputs even when they are historical report or fixture artifacts.

## 7. Open Owner Questions

1. Should `evidence_binding/` move with ECR/SCR, Judgment, or a Foundation boundary package?
2. Should `schemas/` remain a shared runtime-model package, or be split by case, finalization, probe, scoring, and fixture ownership?
3. What is the canonical destination label for CSB/company-aggregate signal code: CSB, company-signal, Capture satellite, or LinkedIn lane?
4. Should Search receive any runtime-owned code, or only docs/fixtures that consume Capture outputs for demand-signal workflows?
5. Should `cases/product_learning/*` remain intact as case bundles during the first migration, with internal ownership markers added later?
6. Which `reports/product_learning/*` artifacts are durable migration inputs versus generated outputs that should be excluded or archived?
7. Should `pyproject.toml` continue to define one `orca-harness` installable package during migration, or should runtime owners get separate package metadata later?
8. What compatibility promise, if any, is required for imports from `schemas/judgement_models.py`, `source_capture/*`, `ecr/*`, `signal_content/*`, and `evidence_binding/*`?
9. Should source-observability and source-quality support remain under Source Capture Armory or move to a shared infrastructure/foundation support substrate?

## 8. Suggested Migration Order

1. Mark shared harness infrastructure first: `pyproject.toml`, `Makefile`, `uv.lock`, `harness_utils.py`, `config/`, and cross-spine contract tests. Decide whether one package remains during migration.
2. Migrate or mark Capture / Source Capture Armory surfaces next: `source_capture/`, `source_capture/adapters/`, `source_observability/`, source-quality runners, source-capture docs, and packet/projection tests.
3. Split `capture_spine/` by actual sub-spine: Reddit Candidate Intake, Reddit Graph Frontier, LinkedIn lane, LinkedIn Graph Frontier, LinkedIn live adapter, and company-signal runtime. Do not move it as one folder.
4. Move ECR/SCR derived-record surfaces after Source Capture references are stable: `ecr/`, `signal_content/`, related tests, and docs. Resolve the `signal_content/deriver.py` versus repo-map wording before publishing new route docs.
5. Resolve the Foundation / ECR-Judgment boundary before moving `evidence_binding/`, `schemas/finalization_models.py`, `runners/run_finalization_receipt.py`, and JSG-01 proof fixtures.
6. Migrate Cleaning after Capture and ECR reference locations are clear, because Cleaning handles point to raw/projection/ECR material.
7. Migrate Judgment harness runtime and fixtures: `schemas/` Judgment-owned files, `scoring/`, Judgment runners, TR/Casetext fixture, product-learning cases, and reports. Keep fixture bundles traceable.
8. Reconcile Search-linked Reddit artifacts after Capture ownership is stable. Preserve Search as consumer unless the owner explicitly assigns runtime ownership.
9. Only after the above, rename packages or paths. Rename work should be owner-approved and compatibility-planned, not inferred from this inventory.

## 9. Explicit Non-Claims

- This artifact moves no code, fixtures, reports, package names, tests, or docs outside this file.
- This artifact does not run tests and does not claim any test, package, runner, fixture, or adapter passes.
- This artifact does not claim runtime readiness, production readiness, migration readiness, validation status, scoring quality, model quality, source quality, commercial permission, live-capture permission, or JSG gate status.
- This artifact does not authorize ECR, SCR, Cleaning, Judgment, Search, Capture, CSB, or Foundation implementation work.
- This artifact does not resolve conflicts between docs that describe frozen, unfrozen, built, deferred, or authorized states.
- This artifact does not decide final package names, import compatibility, retention policy, or fixture relocation policy.
- This artifact does not treat `orca-harness/` as one owner-owned runtime. The current tree is a mixed historical harness substrate.
