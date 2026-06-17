# Orca Search Lane

```yaml
retrieval_header_version: 1
artifact_role: Orca product lane index
scope: >
  Front-door index for docs/product/search/ - the search / answer-engine topic
  vertical. Lists the co-located search-primary artifacts and cross-links the
  demand-spine docs that consume search but live in their function lanes.
use_when:
  - Looking for Orca's search / answer-engine work (capture, source-class, AEO).
  - Deciding whether a new doc belongs in this lane.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/orca_search_product_lane_binding_v0.md
```

The search lane composes Orca's search / answer-engine work: web search / SERP,
Google AI Overviews and other answer engines, zero-click, AEO/GEO, and
search-interest ("trends") as capture surfaces. The lane is **bound by**
`docs/decisions/orca_search_product_lane_binding_v0.md`; that record holds the
inclusion test and precedence rule that decide membership.

> Migration status: the four in-lane docs below are relocated here by the
> freeze-gated `docs/migration/repo_structure_search_lane_v0/` move. Until that
> apply runs, the in-lane (relative) links resolve only after the move; the
> cross-links to other lanes below are live now.

## In this lane (search-primary)

- [`aeo_capture_feasibility_probe_phase0_v0.md`](aeo_capture_feasibility_probe_phase0_v0.md)
  - Phase-0 feasibility probe: can AI answer engines' output (surfaced brands +
    cited sources + issued queries) be reliably and automatably captured?
    ChatGPT + Google AI Overviews. GO verdict, extraction patterns, failure
    taxonomy.
- [`aeo_capture_feasibility_probe_phase0_v0_evidence.json`](aeo_capture_feasibility_probe_phase0_v0_evidence.json)
  - Machine-readable per-run evidence for the probe.
- [`demand_search_interest_sourcing_and_gate_delta_spec_v0.md`](demand_search_interest_sourcing_and_gate_delta_spec_v0.md)
  - Source classes + gate-read placement for search-interest and AEO (which
    surface feeds which demand gate).
- [`demand_durability_indicator_search_interest_capture_profile_v0.md`](demand_durability_indicator_search_interest_capture_profile_v0.md)
  - Capture obligations for search-interest signals: temporal regime,
    cold-start, comparability.

## Related, but living in their function lanes (cross-links)

These consume search as one venue but are demand-integrity mechanics, not
search-primary; they stay in their spine lanes (moving them would orphan them
from their downstream consumers):

- Demand-scan method - `docs/product/core_spine/orca_demand_scan_core_spec_v0.md`
- Demand-scan / gate adjudication - `docs/product/product_lead/orca_demand_scan_gate_adjudication_packet_v0.md`
- Demand gate definition / commission criteria - `docs/product/product_lead/orca_demand_gate_definition_closures_proposal_v0.md`, `docs/product/product_lead/orca_demand_gate_run_commission_criteria_v0.md`
- Demand-read taxonomy (search-interest = one signal layer) - `docs/product/product_lead/orca_demand_read_taxonomy_v0.md`, `docs/product/product_lead/orca_demand_read_taxonomy_adjudication_v0.md`

## Not in this lane

Retail availability/restock, price-timeseries, and review-velocity durability
capture profiles are different venues (not search) and stay in
`data_capture_spine/`.
