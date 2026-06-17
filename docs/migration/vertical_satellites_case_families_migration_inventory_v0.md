# Vertical Satellites And Case Families Migration Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: migration_inventory
artifact_scope: vertical satellites, domain context, product-learning cases, specimens, run corpora, reusable case-family artifacts, and source-family exclusions
status: inventory_only
created_for: spine-first migration marking
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/source-loading.md
  - .agents/workflow-overlay/artifact-folders.md
  - docs/workflows/orca_repo_map_v0.md
stale_if:
  - any listed artifact is moved, renamed, deleted, promoted, or superseded
  - a satellite owning doc or case-family owning doc is created
  - pending migration PRs land on main after this inventory
non_authorizing: true
```

## 1. Current surfaces found

Preflight read:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/decision-routing.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/retrieval-metadata.md`
- `.agents/workflow-overlay/artifact-folders.md`
- `docs/workflows/orca_repo_map_v0.md` as a retrieval map only

Initial repo status on the original checkout showed `main...origin/main [behind 1]` plus untracked `_scratch/`, `.codex/hooks/run_orca_guard.py`, and `orca-worktrees/`. This inventory was therefore written on isolated branch `codex/vertical-satellites-case-inventory` in worktree `C:\tmp\orca-vertical-satellites-case-inventory`.

Inventory granularity: directory rows classify the directory as a migration artifact group. Child files inherit the row classification unless separately named. This is an inventory and marking artifact only; it does not move, rename, admit, validate, run, or promote anything.

| artifact | current_path | current_owner_if_known | recommended_future_home | classification | consuming_spines | why_not_owned_by_first_consumer | open_question_if_unclear |
|---|---|---|---|---|---|---|---|
| Beauty venue card-set | `docs/product/core_spine/beauty_venue_card_set_v0.md` | Beauty/personal-care card-set owner recorded as Eric in the promotion decision | `orca/product/satellites/beauty/venue_card_set/` | `vertical_satellite` | Core, Judgment, Product Lead, Capture | It is reusable beauty and fragrance-adjacent domain context. Core currently hosts the guide that imports it, but Core does not own the vertical facts. | None. |
| Beauty venue card-set promotion decision | `docs/decisions/beauty_venue_card_set_promotion_decision_v0.md` | Eric | Keep as decision provenance until a migration rule says whether decision records are moved or only referenced from `orca/product/satellites/beauty/` | `vertical_satellite` | Core, Product Lead, Judgment | It records why the beauty card-set became reusable vertical context; it should not be treated as Core-owned method just because the card-set currently sits under Core. | Whether historical decision records stay in `docs/decisions/` after satellite front doors exist. |
| Beauty and fragrance ontology instance cards | `docs/product/core_spine/ontology_cards/vertical_beauty_v0.md`; `docs/product/core_spine/ontology_cards/venue_basenotes_v0.md` | Core ontology area by current path | `orca/product/satellites/beauty/ontology_cards/` or a shared ontology registry with satellite ownership pointers | `vertical_satellite` | Core, Judgment, Product Lead | The ontology grammar is Core or shared substrate, but these cards name domain instances such as beauty, fragrance, and Basenotes. | Whether instance cards physically move to satellites or remain in an ontology registry with satellite owner metadata. |
| Beauty Pie ontology case-object cards | `docs/product/core_spine/ontology_cards/brand_beautypie_v0.md`; `docs/product/core_spine/ontology_cards/case_beautypie_repricing_2023_v0.md`; `docs/product/core_spine/ontology_cards/decision_beautypie_repricing_2023_v0.md`; `docs/product/core_spine/ontology_cards/outcome_beautypie_repricing_2023_v0.md` | Core ontology area by current path | `orca/product/case_families/consumer_demand_backtests/beautypie_repricing_2023/ontology_cards/` or shared ontology registry with case-family pointers | `case_family` | Core, Judgment, Product Lead | The first consumer is Core ontology, but the cards describe a reusable case object and should travel with the Beauty Pie case family or with a case-aware ontology registry. | Same ontology-placement question as above. |
| Fragrance Level 1 product-learning reconciliation | `docs/product/judgment_spine/fragrance_level1_product_learning_reconciliation_v0.md` | Judgment by current path; content says owner confirmed lane should stay product-learning | `orca/product/satellites/fragrance/level1_product_learning/reconciliation_v0.md` | `vertical_satellite` | Judgment, Product Lead, Core | It is currently Judgment-facing because the first skeleton is a demand-read/Judgment fit check, but the reusable content is fragrance domain and product-learning context. | None. |
| Fragrance Level 1 product-learning satellite skeleton | `docs/product/judgment_spine/fragrance_level1_product_learning_satellite_skeleton_v0.md` | Judgment by current path; content says Core owns judgment machinery and Fragrance owns domain instances | `orca/product/satellites/fragrance/level1_product_learning/satellite_skeleton_v0.md` | `vertical_satellite` | Judgment, Product Lead, Core, Capture | The file itself states the split: Core owns machinery; Fragrance owns domain instances, source families, casebook slots, and evidence slots. | None. |
| Fragrance Level 1 casebook admission frame | `docs/product/judgment_spine/fragrance_level1_casebook_admission_frame_v0.md` | Judgment by current path | `orca/product/case_families/fragrance_level1_casebook/admission_frame_v0.md` | `case_family` | Judgment, Fragrance satellite, Product Lead | It is vertical-specific, but allocation says case families own reusable evidence and run corpora. The first Judgment consumer should import it by pointer. | Whether the future parent is a case family with a fragrance satellite pointer, or a subfolder under the fragrance satellite that is explicitly case-family-owned. |
| Fragrance Level 1 named-case candidate screen | `docs/product/judgment_spine/fragrance_level1_named_case_candidate_screen_v0.md` | Judgment by current path | `orca/product/case_families/fragrance_level1_casebook/named_case_candidate_screen_v0.md` | `case_family` | Judgment, Fragrance satellite, Product Lead | It screens candidate named cases; it is not Judgment machinery and should not be owned by the first Judgment skeleton. | Same parent-choice question as the casebook admission frame. |
| Beauty advisory intake scans | `docs/research/orca_discovery_candidate_scan_beauty_neutral_chatgptpro_v0.md`; `docs/research/orca_discovery_candidate_scan_beauty_subniche_chatgptpro_v0.md` | Research by current path | Hold in research until accepted into `orca/product/satellites/beauty/advisory_intake/` or retired | `unclear` | Product Lead, Core, Beauty satellite | They contain vertical niche advice, but they are advisory research inputs. They should not become satellite authority merely because they are useful context. | Whether a no-contact verification scan promoted any part of these advisory intakes. |
| Consumer-demand candidate pool handoff | `docs/product/core_spine/consumer_demand_candidate_pool_handoff_v0.md` | Core by current path; content says one-shot dated discovery-lane consolidation | `orca/product/case_families/consumer_demand_backtests/candidate_pool_handoff_v0.md` | `case_family` | Core, Judgment, Product Lead | It is a reusable candidate corpus, not Core method. Core used it to consolidate candidates, but the case family should own it. | None. |
| Beauty screen 2 ledger | `docs/decisions/venue_procedure_proving_screen_beauty_ledger_v0.md` | Decisions by current path | `orca/product/case_families/consumer_demand_backtests/screen_ledgers/beauty_screen2/` | `case_family` | Core, Product Lead, Judgment | It is a historical candidate and provenance ledger. Reusable beauty venue context extracted from it may feed the beauty satellite, but the ledger itself is a case-corpus artifact. | Whether historical decision ledgers stay in `docs/decisions/` and are indexed from case families instead of moved. |
| Beauty subtle-decision screen 3 ledger | `docs/decisions/beauty_subtle_decision_screen3_ledger_v0.md` | Decisions by current path | `orca/product/case_families/consumer_demand_backtests/screen_ledgers/beauty_screen3/` | `case_family` | Core, Product Lead, Judgment, Beauty satellite | It produced case candidates and also triggered the card-set promotion. The ledger remains corpus/provenance; the card-set is the reusable satellite extraction. | Same decision-ledger placement question. |
| Ingestible beauty screen 1 ledger | `docs/decisions/ingestible_beauty_screen1_ledger_v0.md` | Decisions by current path | `orca/product/case_families/consumer_demand_backtests/screen_ledgers/ingestible_beauty_screen1/` | `case_family` | Core, Product Lead, Judgment | It is part of the consumer-demand candidate corpus and should not become a satellite just because it names a beauty subdomain. | Same decision-ledger placement question. |
| Judgment backtest batch 1 ledger | `docs/decisions/judgment_spine_backtest_batch1_ledger_declaration_v0.md` | Judgment by name and content | `orca/product/case_families/consumer_demand_backtests/batch1/ledger_declaration_v0.md` | `case_family` | Judgment, Product Lead, Core | It declares a product-learning backtest batch. Judgment consumes the batch, but the reusable batch corpus is not Judgment-owned machinery. | Whether the future case-family index points to ledgers in place or moves them. |
| Judgment backtest batch 2 ledger and controls | `docs/decisions/judgment_spine_backtest_batch2_ledger_declaration_v0.md`; `docs/decisions/judgment_spine_backtest_batch2_candidate_routing_v0.md`; `docs/decisions/judgment_spine_backtest_batch2_band_ratification_v0.md` | Judgment by name and content | `orca/product/case_families/consumer_demand_backtests/batch2/` | `case_family` | Judgment, Product Lead, Core | These are batch/corpus control artifacts. Judgment is the first consumer, not the owner of the reusable case family. | Whether all batch 2 control files are co-located or indexed from a case-family front door. |
| Product-learning case directories | `orca-harness/cases/product_learning/beautypie_repricing_2023_v0/`; `cocokind_holdprice_2025_v0/`; `feedhaven_repricing_2019_anon_v0/`; `imaginaryauthors_sku_kills_2024_v0/`; `inoreader_repricing_2019_v0/`; `joahbeauty_cvs_kill_2024_v0/`; `jsg01_binding_assembly_proof_v0/`; `kinderbeauty_box_pivot_2023_v0/`; `nueco_fragrance_pivot_v0/`; `privatepacks_retail_retreat_v0/`; `saie_price_increase_2025_v0/`; `selflessbyhyram_target_entry_2023_v0/`; `sundaily_gummy_pivot_v0/`; `topicals_retail_expansion_2021_v0/` | Harness/runtime path by current placement | `orca/product/case_families/product_learning_cases/` for corpus ownership; runtime path remains subject to harness/runtime mapping | `case_family` | Judgment, Product Lead, Core, Capture | The harness path is a storage/runtime location, not durable ownership. These are reusable case corpora and should not be owned by the first runner or Judgment batch. | Which files inside each directory are pure case artifacts versus runtime fixtures is deferred to a harness/runtime mapping inventory. |
| Product-learning case reports | `orca-harness/reports/product_learning/b2_holdout_h7_v0/`; `cocokind_holdprice_2025_v0/`; `feedhaven_repricing_2019_anon_v0/`; `imaginaryauthors_sku_kills_2024_v0/`; `inoreader_repricing_2019_v0/`; `joahbeauty_cvs_kill_2024_v0/`; `kinderbeauty_box_pivot_2023_v0/`; `privatepacks_retail_retreat_v0/`; `saie_price_increase_2025_v0/`; `selflessbyhyram_target_entry_2023_v0/`; `sundaily_gummy_pivot_v0/` | Harness reports path by current placement | `orca/product/case_families/product_learning_reports/` for corpus ownership; runtime path remains subject to harness/runtime mapping | `case_family` | Judgment, Product Lead, Core | Reports are reusable run/result artifacts. They should not be owned by the reporting path or by Judgment merely because Judgment consumed the runs. | Same runtime mapping question. |
| Product-learning research adjuncts | `docs/research/topicals_sephora_expansion_sealed_outcome_facilitator_only_v0.md`; `docs/research/orgmotion_topicals_capture_feasibility_v0.md`; `docs/research/orgmotion_beautypie_sealed_outcome_facilitator_only_v0.md`; `docs/research/orgmotion_beautypie_capture_feasibility_v0.md`; `docs/research/orgmotion_blind_run_pilot_findings_v0.md` | Research by current path | Index from relevant product-learning or org-motion case-family front doors before any move | `case_family` | Judgment, Product Lead, Core | These are case-adjacent sealed outcome, capture-feasibility, or blind-run artifacts. They should not be owned by research path, Product Lead, or Judgment merely because they were produced for those workflows. | Whether org-motion research adjuncts become their own case family or remain adjuncts to Product Lead/Judgment case families. |
| Org-motion demand-signal research substrate | `docs/research/orgmotion_signal_interpretation_intent_vs_realization_v0.md`; `docs/research/orgmotion_demand_signal_wedge_discovery_v0.md` | Research by current path | Shared Product Lead / Judgment substrate unless a specific case-family owner is later declared | `shared_global` | Product Lead, Judgment, Core | These are interpretation and wedge-discovery references, not one case corpus or one vertical satellite. | Whether org-motion becomes a shared substrate or a case-family parent. |
| Judgment research case corpus | `docs/research/judgment-spine/cases/` including `canoo-walmart/`, `daimler-carve-out/`, `unity-runtime-fee/`, `milwaukee-fiscal-crossroads/`, `craft-expressionengine/`, `inoreader-repricing/`, and `case_usage_ledger_v0.md` | Research/Judgment by current path | `orca/product/case_families/judgment_research_cases/` or indexed from there while research path remains | `case_family` | Judgment, Core | These are reusable case tracks and ledgers. Judgment may consume them, but the case corpus should not be folded into Judgment machinery. | Whether research cases graduate to product case families or remain research-only with an index. |
| Judgment v0.14 harness fixture and run corpus | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/`; `docs/research/judgment-spine/harness/v0_14/fixtures/unity_runtime_fee_2023_v0_14/`; `docs/research/judgment-spine/harness/v0_14/fixtures/daimler_corporate_structure_vote_2019_v0_14/`; `docs/research/judgment-spine/harness/v0_14/smoke_tests/` | Judgment research harness by current path | `orca/product/case_families/judgment_v0_14_fixture_corpus/` for case corpus; no-case smoke artifacts stay with Judgment/harness mapping | `case_family` | Judgment, Core | Fixture and run corpora are reusable evidence/run surfaces. They should not be treated as Judgment method just because they live under the Judgment harness tree. | No-case smoke artifacts may be harness infrastructure rather than case family; split before movement. |
| Unity runtime fee specimen trio | `docs/product/core_spine/orca_backtest_specimen_memo_unity_runtime_fee_at_cutoff_v0.md`; `docs/product/core_spine/orca_backtest_specimen_unity_runtime_fee_source_packet_v0.md`; `docs/product/core_spine/orca_backtest_specimen_unity_runtime_fee_outcome_calibration_v0.md` | Core by current path | `orca/product/case_families/unity_runtime_fee_backtest_specimen/` | `case_family` | Core, Judgment | The specimen is a reusable case artifact. Core hosts the current specimen docs, but Core should own specimen procedure, not the specimen family itself. | Whether fixture drafts stay in research harness folders until runtime mapping. |
| Vertical exploration guide | `docs/product/core_spine/orca_vertical_exploration_guide_v0.md` | Core by current path | `orca/product/spines/core/vertical_exploration_guide_v0.md` or shared method substrate | `shared_global` | Core, Product Lead, Capture, Judgment | It is a method/procedure for vertical exploration and promotion triggers, not a vertical satellite or case family. | None. |
| Memorization-resistant case finder frame | `docs/product/core_spine/orca_memorization_resistant_case_finder_frame_v0.md` | Core by current path | `orca/product/spines/core/` or shared method substrate | `shared_global` | Core, Judgment, Product Lead | It is case-finding method, not a case corpus. | Not read in full for this inventory; confirm before any future move. |
| Ontology backbone architecture | `docs/product/core_spine/orca_ontology_backbone_architecture_v0.md` | Core by current path | `orca/product/shared/ontology_backbone/` or `orca/product/spines/core/ontology/` | `shared_global` | Core, Judgment, Product Lead, satellites | The backbone owns grammar and relationship mechanics. Domain and case instance cards may be satellite or case-family owned, but the grammar should not move under any first vertical. | Future ontology registry boundary remains unresolved. |
| Judgment consolidation and decomposition maps | `docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md`; `docs/product/judgment_spine/judgment_current_state_and_decomposition_v0.md` | Judgment by current path | `orca/product/spines/judgment/` | `spine_specific_adapter` | Judgment, Core, Fragrance satellite | These maps consume satellite and case-family groups but should not own them. | None. |
| Judgment demand-read and near-half machinery | `docs/product/judgment_spine/judgment_spine_demand_read_machinery_architecture_v0.md`; `docs/product/judgment_spine/near_half_backtest_learning_architecture_v0.md`; `docs/product/judgment_spine/near_half_signal_reliability_ledger_v0.md`; `docs/product/judgment_spine/prospective_decision_loop_*`; `docs/product/judgment_spine/judgment_spine_c2_ledger_read_contract_v0.md`; `docs/product/judgment_spine/judgment_spine_c3_verdict_action_ceiling_contract_v0.md` | Judgment by current path | `orca/product/spines/judgment/` | `spine_specific_adapter` | Judgment, Product Lead, case families, satellites | These files are Judgment method, loop, ledger, and action-ceiling mechanics. They can import domain or corpus material but should not own it. | Confirm exact membership before any later migration. |
| Product Lead consumer-demand surfaces | `docs/product/product_lead/orca_offer_hypothesis_consumer_demand_revision_v0.md`; `docs/product/product_lead/orca_buyer_proof_packet_consumer_demand_revision_v0.md`; `docs/product/product_lead/orca_discovery_consumer_demand_target_selection_brief_v0.md` | Product Lead by current path | `orca/product/product_lead/` or shared offer/proof substrate | `shared_global` | Product Lead, Core, Judgment, Beauty satellite | These are offer, proof, and discovery instruments. They mention beauty and consumer-demand cases but are not vertical domain context or case corpora. | None. |
| Creator-momentum data landscape | `docs/research/creator_momentum_data_landscape_v0.md` | Research by current path | Shared creator-momentum/source-data substrate, not a vertical satellite by default | `shared_global` | Product Lead, Capture, Data Capture, future creator-momentum work | It is a data landscape and proof-plan reference. It may inform source capture, but it is not reusable domain context for a specific vertical. | Whether creator-momentum becomes a shared substrate or spine-specific adapter. |
| Retail/PDP capture and projection docs | `docs/product/data_capture_spine/retail_pdp_typed_envelope_probe_v0.md`; `docs/product/source_capture_toolbox/retail_pdp_projection_contract_v0.md`; `docs/product/source_capture_toolbox/retail_pdp_projection_playbook_v0.md`; `docs/product/source_capture_toolbox/retail_pdp_sidecar_operator_playbook_v0.md` | Data Capture / Source Capture Toolbox by current path | Capture / Source Capture Toolbox allocation, not satellites | `source_family_capture_projection` | Capture, Data Capture, ECR, Cleaning, Judgment by reference | Retail/PDP is a source-family/projection-family surface. It is not a vertical satellite by default, and product-page mechanics should not be placed under a vertical. | None. |
| Retail/PDP runtime and tests | `orca-harness/source_capture/retail_pdp_projection.py`; `orca-harness/runners/run_retail_pdp_projection.py`; `orca-harness/tests/unit/test_retail_pdp_projection.py` | Harness/runtime by current path | Leave to harness/runtime mapping inventory unless a file is only a case artifact | `source_family_capture_projection` | Capture, Data Capture, ECR, Cleaning, Judgment by reference | Runtime code belongs to runtime mapping and source capture ownership, not a vertical or case family. | Runtime mapping inventory needed before any path change. |
| Reddit candidate intake, consolidation, projection, graph-frontier, and operator docs | `docs/product/data_capture_spine/data_capture_spine_candidate_url_intake_contract_v0.md`; `docs/product/data_capture_spine/data_capture_spine_reddit_candidate_url_intake_crawler_architecture_v0.md`; `docs/product/data_capture_spine/data_capture_spine_reddit_graph_frontier_lane_architecture_v0.md`; `docs/product/source_capture_toolbox/reddit_precommercial_capture_consolidation_success_signal_architecture_v0.md`; `docs/product/source_capture_toolbox/reddit_precommercial_capture_consolidation_planning_thread_v0.md`; `docs/product/source_capture_toolbox/reddit_packet_consolidation_runner_structural_spec_v0.md`; `docs/product/source_capture_toolbox/reddit_capture_operator_playbook_v0.md`; Reddit pressure-test docs under `docs/product/data_capture_spine/` | Data Capture / Source Capture Toolbox by current path | Capture / Source Capture Toolbox allocation, not a Reddit satellite | `source_family_capture_projection` | Capture, Data Capture, Product Lead, Judgment by later reference | Reddit is a source family in these files. Reddit evidence inside a case belongs to the case family; Reddit venue guidance in beauty card-sets belongs to the beauty satellite. The capture/projection mechanics do not. | None. |
| Reddit runtime and tests | `orca-harness/capture_spine/reddit_candidate_intake/`; `orca-harness/capture_spine/reddit_graph_frontier/`; `orca-harness/source_capture/reddit_*`; `orca-harness/source_capture/adapters/reddit_api.py`; `orca-harness/runners/run_reddit_*`; Reddit unit, contract, and integration tests | Harness/runtime by current path | Leave to harness/runtime mapping inventory | `source_family_capture_projection` | Capture, Data Capture, Source Capture Toolbox | These files implement source-family capture/projection/runtime behavior. They are not a Reddit vertical or case family. | Runtime mapping inventory needed before any path change. |
| IG creator discovery, roster/frontier, feasibility, probe, and creator-momentum capture docs | `docs/product/source_capture_toolbox/ig_creator_discovery_spec_v0.md`; `docs/product/source_capture_toolbox/ig_creator_roster_frontier_ledger_spec_v0.md`; `docs/product/source_capture_toolbox/ig_creator_discovery_suggested_accounts_recon_v0.md`; `docs/product/source_capture_toolbox/ig_sustained_cadence_r_probe_design_v0.md`; `docs/product/source_capture_toolbox/ig_r_probe_results_v0.md`; `docs/product/source_capture_toolbox/ig_wind_caller_capture_feasibility_recon_v0.md`; `docs/product/source_capture_toolbox/ig_wind_caller_calls_capture_build_architecture_v0.md`; `docs/product/source_capture_toolbox/ig_reel_viewcount_capture_feasibility_recon_v0.md`; `docs/product/source_capture_toolbox/ig_logged_out_sustainability_probe_plan_v0.md`; `docs/product/source_capture_toolbox/ig_capture_findings_consolidated_v0.md`; `docs/product/data_capture_spine/orca_creator_momentum_pipeline_architecture_v0.md`; `docs/product/data_capture_spine/orca_creator_monitoring_policy_architecture_v0.md` | Source Capture Toolbox / Data Capture by current path | Capture / Source Capture Toolbox and creator-momentum substrate, not satellites by default | `source_family_capture_projection` | Capture, Data Capture, Product Lead, future creator-momentum work | These documents contain beauty use-case examples, but their durable surface is IG creator/source capture and monitoring mechanics. Any reusable beauty sub-niche guidance should be split before satellite placement. | Whether any sub-niche taxonomy belongs in a future beauty satellite after extraction. |
| IG creator runtime and tests | `orca-harness/source_capture/ig_*`; `orca-harness/runners/run_source_capture_ig_calls_packet.py`; `orca-harness/runners/run_ig_creator_momentum_projection.py`; IG source-capture tests | Harness/runtime by current path | Leave to harness/runtime mapping inventory | `source_family_capture_projection` | Capture, Data Capture, creator-momentum work | Runtime and parser/projection code are not vertical context or case corpus. | Runtime mapping inventory needed before any path change. |
| Prompt and review artifacts that point at cases | `docs/prompts/deep-thinking/orca_judgment_spine_case_learning_preservation_prompt_v0.md`; `docs/prompts/handoffs/captured_candidate_cases_to_judgment_spine_backtest_batch_handoff_v0.md`; relevant `docs/prompts/reviews/`; relevant `docs/review-outputs/` | Prompt/review lanes by current path | Leave in prompt/review lanes unless a separate prompt/review migration inventory says otherwise | `spine_specific_adapter` | Judgment, Core, Product Lead, reviewers | Prompt and review artifacts can point at case corpora, but they are not themselves source case evidence or vertical context by default. | Exact prompt/review membership was not exhaustively classified in this inventory. |

## 2. Proposed satellite groups

Beauty satellite:

- Proposed future home: `orca/product/satellites/beauty/`.
- Primary preserved artifacts: beauty venue card-set, beauty venue card-set promotion decision as provenance, beauty/fragrance ontology instance cards, and any future split-out beauty sub-niche/domain guidance.
- Consuming spines or surfaces: Core vertical exploration, Product Lead consumer-demand target selection, Judgment demand-read work, Capture only as a consumer of venue/source hints.
- Not owned by first consumer because: Core and Judgment currently host or consume the files, but the reusable material is beauty/personal-care domain context.
- Must not move yet: decision records, ontology cards, advisory research intakes, and any card-set file until a satellite owning doc and reference rewrite plan exist.

Fragrance satellite:

- Proposed future home: `orca/product/satellites/fragrance/`.
- Primary preserved artifacts: fragrance Level 1 product-learning reconciliation and satellite skeleton.
- Consuming spines or surfaces: Judgment, Product Lead, Core, Capture by reference.
- Not owned by first consumer because: the first skeleton is Judgment-facing, but the file itself says Core owns machinery and Fragrance owns domain instances.
- Must not move yet: fragrance casebook and named candidate screens should be resolved as case-family-owned or explicitly subowned before path movement.

No PDP satellite proposed:

- Retail/PDP remains a source-family/projection-family surface by default.
- PDP reusable domain context may later become satellite material only if it is domain guidance, not capture/projection mechanics.

## 3. Proposed case-family groups

Consumer-demand backtests:

- Proposed future home: `orca/product/case_families/consumer_demand_backtests/`.
- Includes discovery/screen ledgers, candidate pool handoff, batch 1 and batch 2 ledgers/controls, and Beauty Pie case-object cards.
- Consuming spines or surfaces: Judgment, Product Lead, Core, future beauty/fragrance satellites by pointer.
- Must not move yet: historical decision ledgers and ontology cards until the future policy for decisions and ontology instance placement is settled.

Product-learning harness cases:

- Proposed future home: `orca/product/case_families/product_learning_cases/`.
- Includes the 14 directories under `orca-harness/cases/product_learning/`.
- Consuming spines or surfaces: Judgment batch work, Product Lead proof work, Core case-finding work, Capture by source references.
- Must not move yet: any harness directory until runtime mapping separates pure case artifacts from executable fixtures, runners, reports, or expected-output surfaces.

Product-learning reports:

- Proposed future home: `orca/product/case_families/product_learning_reports/`.
- Includes `orca-harness/reports/product_learning/` report directories.
- Consuming spines or surfaces: Judgment, Product Lead, Core.
- Must not move yet: reports in harness output paths until runtime/report provenance policy is defined.

Product-learning research adjuncts:

- Proposed future home: index from the relevant product-learning or org-motion case-family front doors before any path movement.
- Includes Topicals and Beauty Pie sealed-outcome, capture-feasibility, and blind-run research adjuncts.
- Consuming spines or surfaces: Judgment, Product Lead, Core.
- Must not move yet: org-motion adjunct ownership is unresolved, and no adjunct is promoted or validated by this inventory.

Fragrance Level 1 casebook:

- Proposed future home: `orca/product/case_families/fragrance_level1_casebook/`.
- Includes the casebook admission frame and named-case candidate screen.
- Consuming spines or surfaces: Fragrance satellite, Judgment, Product Lead.
- Must not move yet: no named cases are admitted by this inventory, and no source-family or evidence slots are promoted.

Judgment research cases and specimens:

- Proposed future homes: `orca/product/case_families/judgment_research_cases/`, `orca/product/case_families/judgment_v0_14_fixture_corpus/`, and `orca/product/case_families/unity_runtime_fee_backtest_specimen/`.
- Includes `docs/research/judgment-spine/cases/`, Judgment v0.14 fixture folders, the Unity runtime fee specimen trio, and associated fixture drafts.
- Consuming spines or surfaces: Judgment and Core.
- Must not move yet: research case corpora may remain research-only; fixture drafts need runtime mapping before any relocation.

## 4. Source-family capture/projection surfaces excluded from satellite ownership

The following are excluded from satellite ownership unless a later artifact extracts pure domain guidance from them:

- Retail/PDP typed-envelope, projection contract, projection playbook, sidecar operator playbook, projection runtime, runner, and tests.
- Reddit candidate URL intake, Reddit candidate intake crawler, Reddit graph frontier lane, Reddit precommercial consolidation architecture, Reddit projection/consolidation/adapters/runners/tests.
- IG creator discovery, IG roster/frontier ledger, creator-momentum pipeline architecture, creator monitoring policy architecture, IG parser/projection/harvest runners and tests.

Allocation:

- Capture and Source Capture Toolbox own source-family mechanics, capture envelopes, projection contracts, sidecar procedures, raw/projection boundaries, and source-specific runtime.
- Satellites may own reusable vertical domain context, venue interpretation, or sub-niche guidance only after it is separated from capture/projection mechanics.
- Case families own evidence, participant packets, run reports, and reusable case corpora, including PDP or Reddit evidence when embedded inside a case.

## 5. PDP-specific classification notes

Retail/PDP is already a source-family and projection-family surface in Orca. Default classification is `source_family_capture_projection`, not `vertical_satellite`.

Known non-satellite PDP control surfaces:

- `docs/product/data_capture_spine/retail_pdp_typed_envelope_probe_v0.md`
- `docs/product/source_capture_toolbox/retail_pdp_projection_contract_v0.md`
- `docs/product/source_capture_toolbox/retail_pdp_projection_playbook_v0.md`
- `docs/product/source_capture_toolbox/retail_pdp_sidecar_operator_playbook_v0.md`
- `orca-harness/source_capture/retail_pdp_projection.py`
- `orca-harness/runners/run_retail_pdp_projection.py`
- `orca-harness/tests/unit/test_retail_pdp_projection.py`

Boundary notes:

- Retail/PDP capture and projection docs belong with Capture / Source Capture Toolbox allocation.
- Retail/PDP runtime belongs in harness/runtime mapping.
- PDP evidence inside product-learning cases belongs with the relevant case family.
- PDP reusable domain context belongs in a satellite only if it is domain guidance and not capture/projection mechanics.

## 6. Owning spine or parent surface per group

| group | owner or parent surface | consuming spines |
|---|---|---|
| Beauty satellite | `orca/product/satellites/beauty/` once created | Core, Product Lead, Judgment, Capture by pointer |
| Fragrance satellite | `orca/product/satellites/fragrance/` once created | Judgment, Product Lead, Core, Capture by pointer |
| Consumer-demand backtest case family | `orca/product/case_families/consumer_demand_backtests/` once created | Judgment, Product Lead, Core |
| Product-learning harness cases | `orca/product/case_families/product_learning_cases/` once created, with runtime paths still governed by harness mapping | Judgment, Product Lead, Core, Capture |
| Fragrance Level 1 casebook | `orca/product/case_families/fragrance_level1_casebook/` once created | Fragrance satellite, Judgment, Product Lead |
| Judgment research cases | `orca/product/case_families/judgment_research_cases/` or research index, pending owner choice | Judgment, Core |
| Retail/PDP source family | Capture / Source Capture Toolbox allocation | Capture, Data Capture, ECR, Cleaning, Judgment by reference |
| Reddit source family | Capture / Source Capture Toolbox allocation | Capture, Data Capture, Product Lead, Judgment by reference |
| IG creator/source family | Capture / Source Capture Toolbox plus creator-momentum substrate | Capture, Data Capture, Product Lead |
| Core methods and ontology grammar | Core or shared product substrate | Core, Product Lead, Judgment, satellites |
| Product Lead offer/proof surfaces | Product Lead or shared offer/proof substrate | Product Lead, Core, Judgment, satellites |

## 7. Shared artifacts used by multiple spines

Shared or shared-like artifacts that should not be captured by a first consumer:

- `docs/product/core_spine/orca_vertical_exploration_guide_v0.md`: shared/Core method for vertical exploration and promotion triggers.
- `docs/product/core_spine/orca_memorization_resistant_case_finder_frame_v0.md`: shared/Core case-finding method.
- `docs/product/core_spine/orca_ontology_backbone_architecture_v0.md`: ontology grammar and relationship architecture.
- `docs/product/product_lead/orca_offer_hypothesis_consumer_demand_revision_v0.md`: Product Lead offer substrate for consumer-demand work.
- `docs/product/product_lead/orca_buyer_proof_packet_consumer_demand_revision_v0.md`: Product Lead buyer-proof substrate, not a validation claim here.
- `docs/product/product_lead/orca_discovery_consumer_demand_target_selection_brief_v0.md`: discovery instrument, not a case-family source slot.
- `docs/research/creator_momentum_data_landscape_v0.md`: research/data-landscape substrate, not a vertical satellite by default.
- `docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md`: Judgment retrieval map that points at case and method surfaces but should not own them.

## 8. Stale placement risks

- Fragrance Level 1 files can be misread as Judgment-owned because they currently sit under `docs/product/judgment_spine/`.
- Beauty venue cards can be misread as Core-owned because the current path is `docs/product/core_spine/`.
- Beauty screen ledgers can be misread as vertical satellite material; only extracted reusable domain context should become satellite material, while ledgers remain case corpus/provenance.
- Retail/PDP can be misread as a retail vertical satellite. The known control surfaces are capture/projection infrastructure unless evidence says they are pure domain guidance.
- Reddit can be misread as Capture-owned in all forms. Reddit capture/projection mechanics are Capture-owned, but Reddit venue hints in beauty card-sets are satellite context, and Reddit evidence inside cases is case-family material.
- Product-learning harness directories can be misread as runtime-only because they live under `orca-harness/`; they also carry reusable case corpora.
- Ontology instance cards can be misread as Core-owned because they live under Core ontology; grammar ownership and instance ownership need separation.
- Prompt and review artifacts can be misread as case evidence. They should remain prompt/review lane artifacts unless a separate migration inventory says otherwise.

## 9. Missing owning-doc risks

- No durable beauty satellite front door was found in the requested surfaces.
- No durable fragrance satellite front door outside Judgment was found.
- No case-family front door was found for `orca-harness/cases/product_learning/`.
- No case-family front door was found for `orca-harness/reports/product_learning/`.
- No case-family front door was found for product-learning research adjuncts under `docs/research/`.
- No case-family front door was found for Judgment v0.14 fixture corpus under `docs/research/judgment-spine/harness/v0_14/fixtures/`.
- No final ontology instance registry boundary was found for splitting grammar ownership from vertical/case instance ownership.
- No runtime mapping inventory was found that separates product-learning case artifacts from harness fixtures, runners, tests, and reports.
- No decision-record migration policy was found for whether historical `docs/decisions/` artifacts move, stay, or are indexed by future homes.
- No source-family extraction rule was found for splitting beauty sub-niche context out of IG creator/source-capture docs.

## 10. Open owner questions

1. Should the beauty satellite owning doc be created at `orca/product/satellites/beauty/README.md`, `orca/product/satellites/beauty/beauty_satellite_v0.md`, or another Orca front-door pattern?
2. Should fragrance Level 1 casebook artifacts live under `orca/product/case_families/fragrance_level1_casebook/` with a pointer from the fragrance satellite, or under the fragrance satellite with explicit case-family subownership?
3. Do historical decision ledgers stay in `docs/decisions/` with future-home indexes, or are they intended to move during the migration?
4. Where should ontology instance cards live after the grammar/instance split: satellite folders, case-family folders, or a shared ontology registry with owner metadata?
5. Which files inside `orca-harness/cases/product_learning/` are pure case-family artifacts versus runtime fixture surfaces?
6. Which files inside `orca-harness/reports/product_learning/` should be preserved as case-family report corpus versus regenerated runtime output?
7. Should product-learning research adjuncts under `docs/research/` become their own case-family group or remain adjuncts to named case families?
8. Should advisory research intake such as the beauty ChatGPT Pro scans be preserved as satellite context, indexed as research provenance, or retired after verified scans?
9. Is creator-momentum a shared substrate, a source-family surface, or a Product Lead adapter for future ownership purposes?

## 11. Suggested migration order

1. Create non-moving front-door indexes for beauty satellite, fragrance satellite, and the main case families.
2. Mark source-family exclusions first for Retail/PDP, Reddit, and IG creator/source capture so they are not accidentally pulled under satellites.
3. Add beauty and fragrance satellite owner docs that import current artifacts by pointer without moving files.
4. Add case-family owner docs for consumer-demand backtests, product-learning harness cases, product-learning reports, product-learning research adjuncts, fragrance Level 1 casebook, Judgment research cases, and Judgment v0.14 fixture corpus.
5. Resolve ontology instance placement before moving ontology cards.
6. Resolve decision-record placement before moving historical screen ledgers or batch ledgers.
7. Run a separate harness/runtime mapping inventory before moving anything under `orca-harness/`.
8. Only after those owner docs exist, propose path moves and reference rewrites as a separate migration patch.

## 12. Explicit non-claims

This inventory does not authorize moving files, renaming folders, promoting fixtures, running cases, validating claims, or declaring any spine/satellite ready.

Additional non-claims:

- No validation, buyer-proof, judgment-quality, fixture-admission, source-quality, or readiness claim is made here.
- No case was executed.
- No source was captured.
- No fixture was admitted.
- No PDP, Reddit, IG, beauty, fragrance, or creator-momentum surface was promoted.
- No pending PR is assumed merged into `main`.
- No future home listed here is created by this inventory; future homes are proposed allocation markers only.
