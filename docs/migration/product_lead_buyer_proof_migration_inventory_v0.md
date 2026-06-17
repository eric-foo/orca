# Product Lead / Buyer Proof Migration Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: Migration inventory for Product Lead / buyer-proof authority
scope: Inventory-only map of Product Lead, offer, buyer-proof, ICP/wedge, pull/kill/graduation, and product-proof authority surfaces that should remain upstream of the spine-first migration.
use_when:
  - Planning spine-first repo migration around Product Lead, buyer proof, offer, ICP/wedge, or pull/kill/graduation authority.
  - Checking what downstream spines may consume but must not absorb.
  - Orienting a fresh agent before moving or renaming Product Lead / product-proof artifacts.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/product-proof.md
  - docs/workflows/orca_repo_map_v0.md
  - docs/decisions/orca_product_thesis_consumer_demand_v0.md
  - docs/product/product_lead/orca_buyer_proof_packet_v0.md
downstream_consumers:
  - Commission Signal Board
  - Capture
  - Search
  - ECR/SCR
  - Cleaning
  - Judgment
stale_if:
  - Product Lead, buyer-proof, offer, ICP/wedge, search lane, or spine folder structure is reorganized.
  - A later accepted Orca decision changes Product Lead ownership or product-proof claim tiers.
  - docs/workflows/orca_repo_map_v0.md is superseded.
```

## Preflight Receipt

```yaml
orca_start_preflight:
  agents_read: true
  overlay_files_read:
    - .agents/workflow-overlay/README.md
    - .agents/workflow-overlay/source-loading.md
    - .agents/workflow-overlay/product-proof.md
    - .agents/workflow-overlay/prompt-orchestration.md
    - .agents/workflow-overlay/decision-routing.md
  repo_status_checked: true
  repo_map_loaded_as: retrieval_only
  source_pack: custom Product Lead / buyer-proof migration inventory scan
  isolation: isolated worktree on codex/product-lead-buyer-proof-inventory because the root checkout had unrelated untracked paths
  pending_pr_assumption: none
```

This artifact is inventory only. It does not move, rename, supersede, ratify,
validate, or promote any artifact. It records the surfaces found during the
spine-first migration inventory and proposes allocation questions for the owner.

## Inventory Rule

For this inventory, "product-authority" means an artifact that governs Product
Lead direction, offer shape, buyer-proof gates, ICP/wedge selection, trust
objection handling, pull-vs-praise, kill/graduation criteria, product thesis, or
first-proof discovery boundaries.

Prompt artifacts, review outputs, migration inventories, repo maps, and
workflows can point at product authority. They are not product authority by
placement alone.

## Migration Posture

Product Lead / Buyer Proof should not be forced under Judgment, Commission,
Capture, Search, ECR/SCR, or Cleaning.

Recommended future allocation:

| Allocation option | Mark | Rationale |
| --- | --- | --- |
| Top-level product authority area | Recommended | Product Lead owns buyer, offer, proof-loop, ICP/wedge, and pull/kill/graduation authority that downstream spines consume. |
| Spine-adjacent governance lane | Acceptable label | It governs spine use from upstream, but should stay adjacent to the spines rather than becoming one. |
| Shared substrate | Partial only | Product-proof semantics and claim-tier controls are shared substrate; the Product Lead lane itself is not. |
| Normal product spine | Do not use | Product Lead is not a data, cleaning, evidence-record, or judgment-processing spine. |

Smallest complete future move, if the owner later authorizes one: keep
`docs/product/product_lead/` as the current Product Lead home unless an accepted
migration decision promotes it to a clearly named product-authority namespace.

## Current Repo Surfaces Found

| Surface | Current inventory finding | Migration implication |
| --- | --- | --- |
| `docs/product/product_lead/` | Fourteen Product Lead lane files found, including live authority docs, adopted discovery instrument, prepared revision packages, advisory/readiness report, runbook, and superseded discovery/wedge history. | Keep upstream of spines. Split live, historical, and prepared-package roles before any future move. |
| `docs/decisions/` | Current thesis/wedge/ratification decisions, superseded wedge chain, product-proof bindings, search-lane binding, advisory proof slice, and pre-capture discovery recommendation. | Keep decision records in `docs/decisions/`; downstream spines may cite but should not absorb them. |
| `docs/prompts/product-planning/` | Product Lead, consumer-demand, ICP, gate, discovery, and commercial-frame commissioning prompts found. Some are historical or retired. | Prompt surfaces stay prompt surfaces. Do not use them as current product authority without rereading their status. |
| `docs/prompts/feature-planning/` | `source_access_method_plan_prompt_v0.md` found as a Data Capture source-access plan prompt. | Feature-planning prompt surface only; not Product Lead authority. |
| `docs/review-outputs/` | Product, proof, claim-defense, pricing-first, data-capture, search, and Judgment reviews found. | Review outputs are advisory/review surfaces unless accepted by an owner decision. |
| `docs/workflows/orca_repo_map_v0.md` | Retrieval map loaded. It lists Product Lead anchor files and downstream spine maps, but is not proof of readiness or current state by itself. | Use as a route map only. Do not use as acceptance, validation, or build-state proof. |
| `repo-structure.yaml` and `docs/product/README.md` | `product_lead` is listed as a current product lane. `search` is also listed as a current topic lane. | Current folder allocation already treats Product Lead as a product lane, not as a child of a processing spine. |
| Commission Signal Board | No exact current repo surface named "Commission Signal Board" was found by exact/near phrase search during this inventory. | Treat as a downstream/future consumer named by the owner, not as an existing authority home. |

## Product Lead Owned Docs

These are the files found under `docs/product/product_lead/`. They should remain
upstream of the spines unless a later owner decision explicitly moves Product
Lead authority.

| File | Inventory classification | Migration note |
| --- | --- | --- |
| `docs/product/product_lead/orca_offer_hypothesis_v0.md` | Current offer authority surface. | Keep upstream. Governs offer language, first-proof framing, pull signals, and non-claims consumed by downstream work. |
| `docs/product/product_lead/orca_buyer_proof_packet_v0.md` | Current buyer-proof packet and proof-gate surface. | Keep upstream. Governs buyer qualification, Demand-Substrate Hard Gate, pull/kill/graduation logic, and proof non-claims. |
| `docs/product/product_lead/orca_product_proof_lead_charter_v0.md` | Current Product Proof Lead role boundary. | Keep upstream. Owns proof-loop duties and exclusions; does not own roadmap, feature planning, implementation, or readiness. |
| `docs/product/product_lead/orca_claim_defense_doctrine_v0.md` | Product claim-defense doctrine. | Keep upstream/global-facing. It is subordinate to evidence ladder/tier policy and should not be buried in Judgment. |
| `docs/product/product_lead/orca_discovery_consumer_demand_target_selection_brief_v0.md` | Live consumer-demand discovery target-selection instrument. | Keep upstream. It governs target slots and discovery qualification but authorizes no outreach by itself. |
| `docs/product/product_lead/orca_icp_ratification_readiness_report_v0.md` | Advisory consistency sweep/report. | Keep in Product Lead history/support. Its title includes "readiness," but the body says it is not ratification, acceptance, validation, review-lane output, patch queue, or readiness. |
| `docs/product/product_lead/orca_ratification_day_runbook_v0.md` | Prepared ratification-day checklist/runbook. | Keep as historical process context. Do not treat as owner consent or live migration authority. |
| `docs/product/product_lead/orca_offer_hypothesis_consumer_demand_revision_v0.md` | Prepared revision package. | Treat as historical/prepared package; the live `orca_offer_hypothesis_v0.md` is the reread target. |
| `docs/product/product_lead/orca_buyer_proof_packet_consumer_demand_revision_v0.md` | Prepared revision package. | Treat as historical/prepared package; the live buyer-proof packet is the reread target. |
| `docs/product/product_lead/orca_product_proof_lead_charter_consumer_demand_revision_v0.md` | Prepared revision package. | Treat as historical/prepared package; the live charter is the reread target. |
| `docs/product/product_lead/orca_product_lead_first_icp_wedge_decision_v0.md` | Superseded historical Product Lead wedge decision. | Keep as Product Lead history; current wedge authority is in `docs/decisions/orca_icp_wedge_consumer_demand_first_v0.md`. |
| `docs/product/product_lead/orca_discovery_batch_0_target_selection_brief_v0.md` | Superseded/off-target discovery instrument. | Keep as historical. Do not use for current consumer-demand discovery. |
| `docs/product/product_lead/orca_discovery_batch_0_qualification_prep_sentry_clerk_v0.md` | Superseded/off-target prep surface. | Keep as historical. It points at older pricing-first discovery context. |
| `docs/product/product_lead/orca_discovery_batch_0_candidate_context_scan_v0.md` | Superseded/off-target context scan. | Keep as historical. It should not seed live target slots. |

## Global Product Doctrine Product Lead Depends On

These docs govern Product Lead or buyer-proof work but should not be moved into
Product Lead as owned lane docs unless the owner explicitly changes authority.

| File | Governs | Allocation |
| --- | --- | --- |
| `.agents/workflow-overlay/product-proof.md` | Product-proof trust states, pull-vs-praise, kill discipline, product-proof non-claims. | Overlay authority. Shared substrate. |
| `docs/decisions/orca_product_thesis_consumer_demand_v0.md` | Current consumer-demand product thesis and vertical-portable engine/spine/method boundary. | Decision record. Upstream product direction. |
| `docs/decisions/orca_icp_wedge_consumer_demand_first_v0.md` | Current first-proof ICP/wedge direction lock. | Decision record. Upstream product direction. |
| `docs/decisions/orca_consumer_demand_ratification_decision_memo_v0.md` | Owner outcomes for thesis, wedge, probe feasibility, and outreach gate. | Decision record. Do not convert to Product Lead folder state. |
| `docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md` | Claim tiers and closeout states, including product-learning and buyer-proof caps. | Judgment/Core proof doctrine. Product Lead consumes it but does not own it. |
| `docs/decisions/judgment_spine_pre_sale_execution_evidence_tier_policy_v0.md` | Evidence-tier policy for pre-sale/manual/subscription execution. | Decision record. Product Lead consumes claim boundaries. |
| `docs/product/core_spine/core_spine_v0_product_contract.md` | Core vs satellite boundary, decision artifacts, buyer/satellite requirements. | Core shared substrate. |
| `docs/product/core_spine/core_spine_v0_information_production_foundation_v0.md` | Manual information-production and Evidence Unit discipline. | Core shared substrate. |
| `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md` | Capture/ECR/Cleaning/Judgment/Decision Artifact/Outcome Memory boundaries. | Core boundary authority. |
| `docs/decisions/orca_search_product_lane_binding_v0.md` | Search topic-lane binding for demand-signal discovery method. | Decision record. Product Lead consumes Search outputs; Search is not Product Lead. |
| `docs/decisions/pre_capture_discovery_spine_charter_recommendation_v0.md` | Recommendation not to build a new pre-capture discovery spine/lane at that point. | Decision/recommendation surface; useful migration boundary. |
| `docs/decisions/advisory_proof_slice_definition_v0.md` | Advisory proof slice and no-buyer-contact boundary context. | Decision record. Product Lead consumes no-outreach boundary. |
| `docs/decisions/distillation_binding_product_proof_v0.md` | Prepare-only distillation binding for product-proof lessons. | Decision/distillation surface; not a Product Lead-owned proof claim. |
| `docs/decisions/orca_moat_judgment_quality_proof_path_decision_chain_v0.md` | Moat/Judgment-quality proof-path decision-chain context. | Pending/contextual decision-chain surface; do not bury inside Product Lead or Judgment as current proof. |

Superseded global product-history docs that should remain available as history,
not spine-owned current authority:

- `docs/decisions/turn_08_product_thesis_v0.md`
- `docs/decisions/orca_icp_wedge_pricing_first_v0.md`
- `docs/decisions/orca_icp_wedge_convergence_break_in_first_v0.md`

## Proposed Future Allocation

| Future area | Belongs there | Does not belong there |
| --- | --- | --- |
| Product Lead authority | Offer hypothesis, buyer-proof packet, Product Proof Lead charter, current discovery target-selection brief, claim-defense doctrine, current/historical Product Lead lane records. | ECR/SCR schemas, source capture mechanics, cleaning transforms, Judgment conductor logic, search topic method ownership, implementation plans. |
| Global product-proof substrate | Product-proof overlay, evidence ladder, evidence-tier policy, claim-defense constraints where cross-lane. | Product Lead target slots, offer copy, ICP/wedge choices, outreach operations. |
| Core shared substrate | Core Spine product contract, IPF, data/cleaning boundary, logical data-lake mechanics. | Product Lead buyer qualification, pull/kill/graduation decisions, market-specific offer authority. |
| Search topic lane | Search/answer-engine surfaces and demand-signal discovery method now under `docs/product/search/`. | Product Lead offer/wedge/proof-loop authority. |
| Capture / Data Capture | Commissioned capture obligations, source access, preservation, raw observable capture, source visibility, capture-to-ECR handoff. | ICP selection, offer definition, buyer proof, pull grading, kill/graduation, claim-tier promotion. |
| ECR/SCR | Source-side integrity records and Signal Content Record content layer. | Buyer proof, final Evidence Unit field architecture, Cleaning design, Judgment design, Product Lead authority. |
| Cleaning | Non-destructive transformation, normalization, dedupe, and cleaning ledger work when separately owned. | Credibility, decision strength, action ceiling, Product Lead gates, offer language. |
| Judgment | Signal integrity, signal-use classification, uncertainty, counterevidence, decision strength, action ceiling, conductor/gate ownership. | Product Lead ownership, offer/ICP/wedge selection, buyer pull/graduation authority, capture/storage/deck ownership. |
| Commission Signal Board | If created, route commissions against Product Lead proof objectives, target buyers, decision families, and success/kill gates. | Product Lead authority itself. It should not become the home for the buyer-proof packet, offer hypothesis, or ICP/wedge decisions. |

## Downstream Spine Consumers

| Consumer | What it consumes from Product Lead / buyer proof | What it must not absorb |
| --- | --- | --- |
| Commission Signal Board | Proof objective, target buyer, decision family, commissioned signal need, success/kill gates, and pull-vs-praise criteria. | Offer authority, ICP/wedge authority, buyer-proof packet ownership, Product Lead charter ownership. |
| Capture | Decision frame, source families, capture obligations implied by the proof question, Demand-Substrate Hard Gate inputs, and visible capture limits. | Buyer qualification, pull grading, proof graduation, claim-tier promotion, final decision strength. |
| Search | Demand-signal question framing, search/gate needs, public-signal families, and demand-read context. | Offer hypothesis, buyer-proof gates, Product Lead role boundary. |
| ECR/SCR | Captured signal packets, provenance keys, source-side integrity posture, and signal-content fields where separately authored. | Product Lead proof claims, final Evidence Unit architecture, Judgment evaluation, buyer proof. |
| Cleaning | Raw/ECR/SCR inputs and any separately owned cleaning obligations. | Signal credibility, uncertainty discounting, action ceiling, buyer pull, Product Lead gates. |
| Judgment | Cleaned/source-side evidence, Product Lead claim caps, buyer-proof tier boundary, and decision-artifact constraints. | ICP/wedge selection, offer wording, buyer/outreach ownership, capture/storage/deck production. |

## Stale Placement Or Stale Naming Risks

- The three `*_consumer_demand_revision_v0.md` Product Lead files are prepared
  revision packages. The live reread targets are the non-revision `v0` docs.
- `docs/product/product_lead/orca_discovery_consumer_demand_target_selection_brief_v0.md`
  has a title that still says proposed, while its metadata/status records it as
  the adopted live discovery instrument.
- `docs/product/product_lead/orca_product_lead_first_icp_wedge_decision_v0.md`
  is superseded by later decisions. It should not be used as current wedge
  authority.
- `docs/product/product_lead/orca_discovery_batch_0_*` files are superseded or
  off-target for the consumer-demand lane.
- `docs/prompts/product-planning/orca_product_proof_lead_customer_discovery_prompt_v0.md`
  is explicitly retired/off-target and still hard-gated to the superseded
  pricing wedge. No live consumer-demand discovery operating prompt exists yet.
- `docs/prompts/product-planning/orca_product_lead_ca_first_icp_wedge_prompt_v0.md`
  is a historical prompt surface. Its embedded `input_hashes` include older
  pre-lane-move paths; use live `open_next` paths and controlling decisions.
- Some prompt, review, and historical migration references still mention old
  product paths or old wedge framing. Treat these as historical references
  unless a live owner artifact says otherwise.
- `docs/workflows/orca_repo_map_v0.md` is active as a retrieval map, not proof
  that a surface is accepted, fresh, validated, built, or ready.
- Search-lane demand-signal method docs have moved to `docs/product/search/`.
  Do not re-bury them inside Product Lead, Capture, Judgment, or Core during a
  Product Lead migration.
- "Commission Signal Board" is not currently an exact repo surface found by this
  inventory search. If the owner wants it, create or identify it in a separate
  decision/workflow lane before wiring references to it.

## Documents That Should Not Move Into A Spine

- `docs/product/product_lead/orca_offer_hypothesis_v0.md`
- `docs/product/product_lead/orca_buyer_proof_packet_v0.md`
- `docs/product/product_lead/orca_product_proof_lead_charter_v0.md`
- `docs/product/product_lead/orca_claim_defense_doctrine_v0.md`
- `docs/product/product_lead/orca_discovery_consumer_demand_target_selection_brief_v0.md`
- Historical and prepared Product Lead support docs under `docs/product/product_lead/`
- `docs/decisions/orca_product_thesis_consumer_demand_v0.md`
- `docs/decisions/orca_icp_wedge_consumer_demand_first_v0.md`
- `docs/decisions/orca_consumer_demand_ratification_decision_memo_v0.md`
- Superseded thesis/wedge decisions under `docs/decisions/`, which should remain
  decision history rather than spine-owned current authority
- `.agents/workflow-overlay/product-proof.md`
- `docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md`
- `docs/decisions/judgment_spine_pre_sale_execution_evidence_tier_policy_v0.md`
- Core shared-substrate docs under `docs/product/core_spine/`
- Search topic-lane docs under `docs/product/search/`
- Product-planning and feature-planning prompt artifacts
- Product/proof/search/data-capture/Judgment review outputs

## Open Questions For The Owner

1. Should Product Lead remain at `docs/product/product_lead/`, be promoted to a
   top-level product-authority namespace, or be explicitly named a
   spine-adjacent governance lane?
2. Should "Product Proof Lead" remain a sub-role inside Product Lead, or should
   buyer-proof loop ownership get a separate lane label?
3. Should prepared revision packages be marked consumed/archived in a later
   hygiene pass, or kept beside live Product Lead docs?
4. Should the retired pricing-first discovery prompt be replaced only when the
   owner opens the outreach/discovery-prep gate?
5. What exact artifact should own the user-named "Commission Signal Board" role,
   since no current exact repo surface was found?
6. Should stale prompt/path references be fixed in a separate prompt/hygiene
   lane, or intentionally left as historical references?
7. Should Product Lead own pricing/commercial-frame authority, or only consume
   pricing/commercial-frame commissions as downstream inputs to proof strategy?

## Suggested Migration Order

1. Treat this file as the inventory freeze for Product Lead / buyer-proof
   migration planning.
2. Ask the owner to decide Product Lead allocation: keep current folder,
   promote to top-level product authority, or label it spine-adjacent governance.
3. Preserve live Product Lead authority docs together before moving any
   historical/prepared packages.
4. Separate historical, prepared revision, prompt, and review surfaces from live
   Product Lead authority in the migration manifest.
5. Wire downstream consumers by references and `open_next` routes before moving
   documents into spine folders.
6. If a Commission Signal Board is created, make it a consumer/router of Product
   Lead authority rather than the owner of that authority.
7. After owner allocation, update repo map and folder README surfaces as a
   follow-on migration step.
8. Commission any live consumer-demand discovery operating prompt through the
   prompt-orchestration lane only when the owner opens that work.

## Explicit Non-Claims

This artifact does not claim:

- buyer validation;
- buyer pull;
- willingness to pay;
- product proof;
- buyer-proof completion;
- proof graduation;
- commercial readiness;
- product readiness;
- feature readiness;
- implementation readiness;
- outreach authorization;
- source-access authorization;
- ECR/SCR design approval;
- Cleaning design approval;
- Judgment design approval;
- repo-map freshness beyond retrieval use;
- pending PR merge state;
- owner acceptance of the proposed future allocation.
