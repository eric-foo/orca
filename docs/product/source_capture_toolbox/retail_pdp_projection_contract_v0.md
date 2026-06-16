# Retail/PDP Projection Contract v0

```yaml
retrieval_header_version: 1
artifact_role: Product contract / playbook for Retail PDP mechanical projection
scope: >
  Retail/PDP raw-packet-to-projection contract for Amazon, Sephora, and Ulta:
  what capture must preserve, what projection may emit, what residuals mean,
  and what remains outside projection until a later owner-authorized lane.
use_when:
  - Stabilizing or reviewing the Retail/PDP projection slice before capture-to-projection wiring.
  - Checking Amazon, Sephora, or Ulta product/offer/review binding limits.
  - Deciding whether the next move is playbook review, implementation patch, or ECR sequencing.
authority_boundary: retrieval_only
open_next:
  - docs/product/core_spine_v0_projection_doctrine_v0.md
  - docs/product/data_capture_spine/demand_durability_multi_retailer_rendered_capture_spec_v0.md
  - orca-harness/source_capture/retail_pdp_projection.py
  - orca-harness/tests/unit/test_retail_pdp_projection.py
stale_if:
  - Retail PDP projection code changes row kinds, residual vocabulary, required bindings, or retailer parsing posture.
  - Multi-retailer rendered capture posture changes for Amazon, Sephora, or Ulta.
  - Projection doctrine changes raw-canonical, carry-or-residualize, or no-salience-decision rules.
```

## Status

Status: `CONTRACT_V0`.

This contract is a docs-first stabilization surface for the current Retail/PDP
projection slice. It is not implementation authorization, not capture execution,
not ECR sequencing, not Cleaning, not Judgment, not validation, and not readiness.

The next implementation patch may wire capture output into projection only after
this contract is accepted or explicitly used as the bounded implementation
surface.

## Purpose

Retail PDPs are useful to Orca only if the source-visible product, offer, and
review facts remain tied to the raw retailer packet that produced them. The goal
is not to make retailer pages look clean. The goal is to preserve a narrow,
mechanical row view over raw capture bytes so downstream layers can inspect:

- which product/SKU/variant was captured;
- which price, currency, availability, and review substrate were source-visible;
- which retailer-specific fallbacks were unsafe and visibly residualized;
- which facts came from rendered DOM, visible text, embedded structured JSON, or
  carried frame-sensitive modules; and
- which gaps remain visible before ECR, Cleaning, or Judgment acts.

Raw remains canonical. Projection is a re-derivable view.

## Source Read Ledger

| Source | Why read | Supported claim |
| --- | --- | --- |
| `AGENTS.md` and `.agents/workflow-overlay/README.md` | Orca project authority and overlay binding | Docs-write work must stay inside Orca authority and visible boundaries. |
| `.agents/workflow-overlay/source-loading.md` | Source-loading and capture/projection read-pack route | Capture-spine activity starts from the source-capture playbook; raw-to-Judgment projection opens projection doctrine. |
| `.agents/workflow-overlay/source-of-truth.md` | Doctrine-change propagation rule | This new product contract carries an inline propagation receipt. |
| `.agents/workflow-overlay/artifact-folders.md` and `retrieval-metadata.md` | Placement and retrieval-header rules | New durable product artifacts belong under `docs/product/` and need retrieval metadata. |
| `docs/product/source_capture_toolbox/source_capture_playbook_v0.md` | Capture method boundary | Retail capture must locate the signal substrate first and preserve source-native bytes, not paraphrase. |
| `docs/product/source_capture_toolbox/capture_recon_index_v0.md` | Existing recon evidence | Sephora progressive-scroll/Bazaarvoice and Ulta Apollo state are reported as worktree-pending recon; Amazon recon remains open in the rendered-capture spec. |
| `docs/product/core_spine_v0_projection_doctrine_v0.md` | Projection doctrine | Raw is canonical; projection is a view; Retail/PDP must preserve SKU/variant/price, availability, review-substrate, per-retailer/locale series, and embedded JSON. |
| `docs/product/data_capture_spine/demand_durability_multi_retailer_rendered_capture_spec_v0.md` | Multi-retailer rendered capture spec | Per-retailer series, substrate-first posture, and Amazon/Sephora/Ulta source-access status. |
| `orca-harness/source_capture/retail_pdp_projection.py` | Current implementation | Row kinds, binding map, residual names, no-Judgment-field guard, and structure-preservation rule. |
| `orca-harness/tests/unit/test_retail_pdp_projection.py` | Current behavioral tests | Amazon, Sephora, Ulta, unsafe fallback, no-Judgment-smuggling, and structure-preserved behavior. |

## Contract

### Capture Input Required

Retail projection consumes an existing `SourceCapturePacket` plus preserved raw
file bytes. It does not fetch, browse, enrich, or choose sources.

For a PDP slice to be projectable, the raw packet should preserve:

- rendered DOM HTML for the PDP slice;
- visible text for fallback and module detection;
- packet and slice identifiers, file hashes, hash basis, source locator,
  `series_id`, locale pin, currency pin, variant pin, capture time, cutoff
  posture, access posture, and archive-history posture;
- embedded structured JSON when the retailer exposes it in the captured HTML;
- enough rendered structure to anchor product, variant, price, availability, and
  review substrate; and
- raw screenshot/media as packet evidence when captured, even when the current
  projection only ledger-collapses hero imagery or cart/notify chrome.

If rendered DOM HTML is missing, projection must emit a residual rather than
fabricating rows.

### Projection Output Allowed

The current projection view may emit only these row families:

| Row kind | Meaning |
| --- | --- |
| `retail_pdp_product` | Packet/slice-level product context: retailer, source locator, series, pins, timing, cutoff, and archive posture. |
| `retail_variant_offer` | Source-visible SKU/product/variant/price/currency/availability facts. |
| `retail_review_substrate` | Source-visible review-count/rating substrate and how it was located. |
| `retail_embedded_structured_json` | Raw JSON-LD or Apollo-state text preserved verbatim with parse status. |
| `retail_carried_module` | Frame-sensitive modules such as shipping, loyalty, and recommendations carried as visible context, not trusted as target product/review facts. |

Projection may emit these bindings:

- `sku_variant_price`;
- `variant_availability`;
- `review_substrate_for_product`;
- `series_locale_currency`;
- `structured_json_for_product`;
- `module_carried`.

Projection must not emit credibility, integrity, demand, discounting,
inclusion/exclusion, Signal Use, Decision Strength, Action Ceiling, or any
Judgment-facing label. Current code rejects source-visible field names that
smuggle those concepts.

### Structure And Residual Semantics

`structure_preserved` is true only when the required retail bindings are present:

- `sku_variant_price`;
- `variant_availability`;
- `review_substrate_for_product`;
- `series_locale_currency`.

Residuals are not failures by themselves. A residual is a visible gap, fallback
warning, mismatch, or absent substrate that travels with the view so downstream
work cannot mistake a brittle carry for a clean fact.

Known residual classes include:

| Residual | Meaning |
| --- | --- |
| `retail_pdp_rendered_dom_absent` | No rendered PDP HTML was available for the slice. |
| `<slice>:<retailer>:variant_offer_absent` | Projection could not locate a variant/offer binding. |
| `<slice>:<retailer>:review_substrate_absent` | Projection could not locate the review substrate. |
| `amazon_price_from_unanchored_visible_text_fallback` | Amazon price came only from a position-dependent visible-text `$N` fallback, not the target DOM price input. |
| `sephora_review_count_from_unanchored_fallback` | Sephora review count came only from an unanchored visible-text review pattern, not the target `Ratings & Reviews (N)` widget. |
| `sephora_ld_json_review_count_differs_from_target_dom` | Sephora structured JSON review count differs from the target DOM review widget. |
| `ulta_ld_json_apollo_<field>_mismatch` | Ulta JSON-LD and Apollo state disagree for a variant field such as SKU, product ID, price, or availability. |
| `ulta_ld_json_apollo_review_count_mismatch` / `ulta_ld_json_apollo_rating_mismatch` | Ulta JSON-LD and Apollo state disagree for review substrate values. |
| `<structured_kind>_<index>_malformed_json` | Embedded structured JSON was preserved but could not be parsed. |

`hierarchy_preserved=True` is vacuous for current PDP projection. PDPs do not
have thread parent/reply hierarchy; their structure is the product/variant/price
/availability/review binding map above.

### Retailer Postures

| Retailer | Capture substrate to preserve | Projection posture | Binding limits |
| --- | --- | --- | --- |
| Amazon | Rendered DOM plus visible text; US storefront/locale/currency pins when the capture series requires comparability. | Current projection reads ASIN, DOM target price input, availability text, average customer review nodes, and best-sellers-rank text; it carries shipping, loyalty, and recommendation modules. | If the DOM price input is absent, the visible-text price fallback is residualized because it can pick up store-card or promo amounts. Amazon capture recon remains the open source-access question in the multi-retailer rendered-capture spec. |
| Sephora | Rendered DOM after the review area has actually loaded; Bazaarvoice configuration and target review widget should be preserved when present. | Current projection preserves JSON-LD verbatim, uses structured product/offer fields, treats `Ratings & Reviews (N)` as the target review count, and carries recommendation review-count examples separately. | Recommendation counts are not the target review substrate. Bare `<token> Reviews` fallback is residualized. JSON-LD disagreement with the target DOM review widget is residualized. |
| Ulta | Rendered DOM carrying JSON-LD and `window.__APOLLO_STATE__`; requested SKU context should remain visible. | Current projection preserves JSON-LD and Apollo state verbatim, prefers/merges Apollo offer fields, carries `apollo_requested_sku`, and compares JSON-LD against Apollo for mismatches. | JSON-LD/Apollo disagreements are residualized. Apollo state is a source-visible embedded-state substrate, not an authority to normalize away SKU or review mismatches. |

### What Must Stay Out

Projection must not:

- fetch retailer pages, run browsers, retry blocked captures, or decide source
  access posture;
- clean, normalize, dedupe, cluster, translate, summarize, or judge facts;
- decide salience, demand relevance, independence, credibility, or strength;
- convert residuals into exclusion or failure labels;
- treat frame-sensitive shipping, loyalty, or recommendation modules as target
  SKU/price/review facts; or
- sequence ECR before the source-visible projection layer has preserved its
  gaps.

## Next Move Gate

The next safest move is **not** automatic ECR. The next move is one of:

1. **Playbook review / owner acceptance** of this Retail/PDP projection contract.
2. **Bounded implementation patch** to wire already-captured Retail PDP packets
   into `build_retail_pdp_projection`, using this contract as the behavior
   surface.
3. **Retailer recon closure**, especially Amazon, if the immediate bottleneck is
   source-access posture rather than projection behavior.

Auto-project-after-capture wiring is acceptable only as a bounded patch against
this contract. It must not hide residuals, silently trust fallbacks, or feed ECR
facts that projection could not anchor.

## Direction Change Propagation

```yaml
direction_change_propagation:
  doctrine_changed: >
    Added a Retail/PDP projection contract/playbook that binds the current
    Amazon, Sephora, and Ulta raw-packet-to-projection slice: raw remains
    canonical, projection is a view, unsafe retailer fallbacks are carried only
    with visible residuals, and ECR/Cleaning/Judgment remain downstream.
  trigger: product_doctrine
  related_triggers:
    - architecture_doctrine
    - output_authority
  controlling_sources_updated:
    - docs/product/source_capture_toolbox/retail_pdp_projection_contract_v0.md
    - docs/product/source_capture_toolbox/README.md
    - docs/workflows/data_capture_spine_consolidation_map_v0.md
  downstream_surfaces_checked:
    - AGENTS.md
    - .agents/workflow-overlay/README.md
    - .agents/workflow-overlay/source-loading.md
    - .agents/workflow-overlay/source-of-truth.md
    - .agents/workflow-overlay/artifact-folders.md
    - .agents/workflow-overlay/retrieval-metadata.md
    - .agents/workflow-overlay/validation-gates.md
    - docs/product/core_spine_v0_projection_doctrine_v0.md
    - docs/product/data_capture_spine/demand_durability_multi_retailer_rendered_capture_spec_v0.md
    - docs/product/source_capture_toolbox/source_capture_playbook_v0.md
    - docs/product/source_capture_toolbox/capture_recon_index_v0.md
    - orca-harness/source_capture/retail_pdp_projection.py
    - orca-harness/tests/unit/test_retail_pdp_projection.py
  intentionally_not_updated:
    - path: .agents/workflow-overlay/source-loading.md
      reason: >
        Existing source-loading already routes capture-spine activity to the
        capture playbook and raw-to-Judgment projection work to projection
        doctrine; this artifact is reachable through the Armory README and Data
        Capture submap without changing the read-pack rule.
    - path: docs/workflows/orca_repo_map_v0.md
      reason: >
        The root map already routes Data Capture / Source Capture Armory detail
        through the Data Capture submap. The submap now names this artifact
        directly, preserving pointer hierarchy.
    - path: orca-harness/source_capture/retail_pdp_projection.py
      reason: >
        This turn stabilizes the contract around current behavior; no code
        behavior was changed or authorized.
    - path: orca-harness/tests/unit/test_retail_pdp_projection.py
      reason: >
        Current tests already cover the behavior summarized here; this docs
        turn did not change code or test expectations.
  stale_language_search: >
    rg -n "retail_pdp_projection_contract|Retail/PDP projection|Retail PDP projection"
    docs/product/source_capture_toolbox/README.md docs/workflows/data_capture_spine_consolidation_map_v0.md
    .agents/workflow-overlay/source-loading.md docs/workflows/orca_repo_map_v0.md
  stale_language_search_result: >
    Executed 2026-06-17 in this worktree. Hits appeared only in the intended
    new routing surfaces: Source Capture Armory README lines indexing this
    artifact and the Data Capture Spine submap fast-route row. No checked
    overlay or root-map surface carried conflicting Retail/PDP projection
    routing language.
  non_claims:
    - not validation
    - not readiness
    - not owner acceptance
    - not implementation authorization
    - not capture execution
    - not ECR, Cleaning, Judgment, buyer proof, or source completeness proof
```
