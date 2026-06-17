# Orca Commission Gate Prompt Adjudication Packet v0

```yaml
retrieval_header_version: 1
artifact_role: Product artifact (decision-prep / adjudication packet)
scope: >
  Maps the temporary backtesting-first Orca commission-gate prompt against
  current Orca consumer-demand, buyer-proof, demand-gate, backtest, and Core
  Spine boundaries before any durable prompt or implementation work.
use_when:
  - Deciding whether to turn the temporary commission-gate prompt into an Orca durable prompt.
  - Checking which prompt sections are adopted, modified, deferred, or rejected.
  - Preparing owner sign-off on the commission-gate packaging and source-routing direction.
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/prompt-orchestration.md
  - docs/product/product_lead/orca_demand_scan_gate_adjudication_packet_v0.md
  - docs/product/product_lead/orca_demand_gate_run_commission_criteria_v0.md
  - docs/product/product_lead/orca_buyer_proof_packet_v0.md
stale_if:
  - The owner ratifies, rejects, or supersedes the demand scan/gate-run adjudication packet.
  - A durable commission-gate prompt is authored through prompt-orchestration.
  - A commission-gate runtime schema or runner is added under orca-harness.
```

## Start Preflight

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S2 product anchor plus target prompt/gate artifacts
  edit_permission: docs-write
  target_scope: product-lead decision-prep artifact; no prompt artifact, no implementation, no runtime authorization
  dirty_state_checked: yes
  blocked_if_missing: AGENTS.md, overlay README, source-loading, prompt-orchestration, buyer-proof packet, demand-gate criteria, demand-gate adjudication packet, temporary prompt
```

## Decision Question

Should the temporary file
`C:/Users/vmon7/AppData/Local/Temp/orca_commission_gate_prompt (1).md`
become the durable Level 1 commission gate, be rewritten through Orca prompt
orchestration, or be deferred?

## Adjudication

Do **not** install the temporary prompt as-is.

Use it as a strong decision-prep draft for a future prompt, but only after the
owner decides the unresolved demand-gate packaging and sourcing questions.
Current Orca doctrine already has a proposed single-candidate gate-run
commission shape, but that shape is not governing authority yet: the demand-gate
criteria are still PROPOSED, the gate packaging/location is owner-owned, and
the first scan remains unauthorized until the decision chain is resolved.

The high-value direction is a hybrid:

- Keep the current Demand-Substrate Hard Gate as the inference layer.
- Fuse the ritual into one commission unit when authorized: evidence plan /
  scan with origination provenance -> in-session gate-run -> verdict.
- Borrow the temporary prompt's mode/cutoff discipline, fragrance source map,
  creator-slice routes, outcome-target vocabulary, graph-family retrieval
  ask, and stop/redirect rules as prompt ingredients.
- Do not let the temporary prompt bypass prompt-orchestration, owner ratification,
  or the current buyer-proof gate.

The prompt is too high-lock-in to adopt wholesale because it mixes five different
objects in one artifact: commission intake, venue playbook, source registry,
forecast-target schema, and graph retrieval schema. Installing that bundle as
authority would silently decide product, Judgment, Data Capture, and prompt
packaging questions that are not all settled.

## Current Source State

The controlling product thesis says Orca is outside-in consumer-demand decision
intelligence for distinguishing durable demand from transient or manufactured
demand; beauty/personal-care is the first vertical and the engine remains
vertical-portable (`docs/decisions/orca_product_thesis_consumer_demand_v0.md`).

The offer hypothesis narrows the first proof offer to US-market indie/DTC beauty
or personal-care operators facing live 30-90 day consumer-demand allocation
decisions, while preserving Orca's broader offer boundary
(`docs/product/product_lead/orca_offer_hypothesis_v0.md`).

The buyer-proof packet binds the Demand-Substrate Hard Gate: independence is
de-correlation by origination, not raw venue count; today's sourced G1 demand
card is forums/community, while review-surface and search-interest are
owner-owned sourcing gaps; retail presence is G4 corroboration, not a G1 origin;
and G2 requires at least one gradeable costly-behavior instance
(`docs/product/product_lead/orca_buyer_proof_packet_v0.md`).

The current gate-run criteria define a single-candidate gate-run, but they are
PROPOSED and owe owner ratification before governing an actual commission
(`docs/product/product_lead/orca_demand_gate_run_commission_criteria_v0.md`).

The current adjudication packet says the first forward-mode scan is blocked on
four owner decisions: scan-core adoption, gate-run criteria ratification,
gate packaging/location, and demand-venue sourcing posture
(`docs/product/product_lead/orca_demand_scan_gate_adjudication_packet_v0.md`).

Prompt policy requires any durable Orca prompt to be authored through
prompt-orchestration or to apply that contract in full. The temporary prompt is
not yet a durable prompt artifact.

Fresh exact-term search in this worktree found no durable hits for the temporary
prompt's schema names: `commission_gate_brief`, `future_information_policy`,
`graph_family_plan`, `forecast_targets_for_downstream`, `backtesting-first`, or
`evidence_cutoff_at`. Existing code provides lower-level capture/provenance,
cutoff posture, projections, graph-frontier patterns, and action-band Judgment
scoring, but not a commission-gate schema, runner, or output contract.

## Section Adjudication Matrix

| Prompt section | Decision | Rationale | Owner / next handling |
| --- | --- | --- | --- |
| 3. Required mode contract | Adopt with modification | The `backtest` cutoff and future-information exclusion are directionally right and align with zero-spoiler backtest doctrine. `live_internal` and `client_facing` need stricter Orca boundaries before use. | Carry into future prompt as required preflight; client-facing mode stays deferred. |
| 4. Intake schema | Modify | The schema is useful, but it must include the current buyer-proof requirements: named decision owner, live allocation consequence, public-first evidence boundary, and unknowns. It must not imply private data is required for first proof. | Rewrite through prompt-orchestration if owner accepts the direction. |
| 5. Gate decision / allocation | Modify | The 70/20/10 allocation is useful search hygiene, not a gate rule. It must not replace the Demand-Substrate Hard Gate or revive a raw collection-count threshold. | Treat as collection guidance only. |
| 6. Decision-type playbooks | Modify | The playbooks are useful venue-routing cards for fragrance/beauty cases, but they are not current Orca gate authority and must be mapped to G1/G2/G4 and origin de-correlation. | Keep as prompt-level route cards, not proof doctrine. |
| 7. Source registry | Adopt with guardrails | The public/repeatable/provenance admission rule fits Orca's public-first proof posture and Data Capture source-family discipline. | Bind each source family to capture/provenance fields before any implementation. |
| 8. Creator routing | Adopt with guardrails | Manual creator routing is acceptable for v1 and the non-creator confirmation guardrail is important. Creator evidence must not clear a demand gate without non-creator confirmation and costly-behavior analysis. | Use as search routing; no algorithmic routing now. |
| 9. Outcome labels | Defer as downstream vocabulary | The labels are valuable for forecast/evaluation design, but the commission gate should route evidence toward them, not score them. Judgment/outcome calibration owns scoring and reveal. | Owner decides whether these labels become a downstream forecast-target registry. |
| 10. Graph-family retrieval plan | Defer as implementation/schema | The graph vocabulary is useful for retrieval output shape, but it is not backed by a commission-domain graph schema or runner. Current graph-frontier code is adjacent, not this object. | Keep as prompt output ask; runtime schema requires separate authorization. |
| 11. Redirect and stop rules | Adopt with modification | The rules correctly prevent tunnel vision, weak provenance, campaign-cluster false positives, and unavailable private-data chases. | Carry into future prompt as search-control policy. |
| 12. Required gate output | Modify | The JSON-like shape is useful, but it must add Orca non-claims and avoid implying readiness, validation, buyer proof, or client-facing authority. | Future prompt output contract after owner approval. |
| 13. Standalone sufficiency | Accept only as commission-gate sufficiency | The prompt may be standalone enough for evidence-plan generation, but it is not enough for the full Orca loop and not enough for runtime implementation. | Keep the boundary explicit. |

## Owner Decisions Needed

1. Decide whether the demand gate remains the inference layer and is fused into
   a single scan->gate-run commission, as the current adjudication packet
   recommends.
2. Decide whether the temporary prompt's fragrance-specific playbooks are the
   first commission-gate satellite or only an example deck for a broader beauty
   commission gate.
3. Decide whether the outcome labels become an accepted downstream forecast
   target vocabulary, or remain prompt-local candidate labels.
4. Authorize a durable prompt artifact through prompt-orchestration after those
   decisions, or explicitly defer prompt authoring.

## Recommended Owner Sign-Off Option

Recommended: **adopt-as-modified direction, do not adopt-as-is**.

This preserves the valuable parts of the prompt while avoiding three failure
modes:

- bypassing the still-PROPOSED gate-run criteria;
- turning search quotas or playbooks into proof rules;
- creating a graph/forecast/runtime contract before the owning lanes accept it.

If the owner accepts this option, the next authorized step is a
prompt-orchestrated durable prompt that references this packet and the current
gate artifacts. If the owner does not accept it, no prompt artifact or
implementation should be created from the temp file.

## Non-Claims

- Not owner ratification.
- Not a prompt artifact.
- Not buyer proof.
- Not validation or readiness.
- Not a scoring engine.
- Not implementation authorization.
- Not authorization to run a scan, capture sources, contact buyers, or produce a client-facing artifact.
