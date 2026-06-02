# Canoo/Walmart Facilitator Ledger Draft v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Draft v0.14 facilitator-ledger surface for the Canoo/Walmart fixture candidate.
use_when:
  - Reviewing draft ledger fields and missing labels before any v0.14 scoring.
  - Separating direct Pydantic FacilitatorLedger fields from protocol fixture metadata.
  - Checking leakage, second-label, underreach, and freeze blockers.
authority_boundary: retrieval_only
input_hashes:
  source_packet_v0.md: 6E2BC0894A36C08B0712C8FE045DF812D3A8857E525CA4412832866FF405E473
  participant_packet_v0.md: E0191512B1A5AD292C023304321B6FD870B4C1CF591DDFF8708ACC69D5B3324F
  blind_judgments_v0.md: 2DF41433DCFACB31832CD51E65EC424888B7EB8955115D6949A35E8C7F2E8225
  facilitator_ledger_v0.md: 6356C45D8E9B75732DB3D146EABFFCE4AD2775BCDD23D0205E26A46222FCE739
  outcome_calibration_v0.md: 8E5766B11F80D716ACFB376E8227A9C610BBB906949AF65C9C1791A070C0A2F0
  fixture_admission_review_v0.md: D81BA050852B6844D3F76D6F840C51A9538E1E4A3628B504C0820821E850D933
  pydantic_schema_reference.md: CFFC7BCAC179B752B9A77204ECA6A6399D30DD7CB6B2C52533E3EC0FDC031D8D
  band_input_labeling_rubric.md: 0CE6E9584F4F1C4716559A654870AF43EBED3E5D53D3279AB658993B7DE1C2AE
  judgement_case_construction_protocol.md: FDEA14A1767D135A8DD56AF073AF0E5E3206B945FB9E603F597491D795889C71
open_next:
  - docs/research/judgment-spine/harness/v0_14/pydantic_schema_reference.md
  - docs/research/judgment-spine/harness/v0_14/band_input_labeling_rubric.md
  - docs/research/judgment-spine/harness/v0_14/judgement_case_construction_protocol.md
```

- Status: FACILITATOR_LEDGER_DRAFT_NOT_FROZEN
- Case ID: `canoo_walmart_2022_v0_14`
- Fixture status: blocked before scoring
- Ledger freeze hash: `NOT_COMPUTED`
- Second-label audit: not performed
- Action band derivation: not performed
- Scoring status: not score-ready

## Direct Pydantic FacilitatorLedger Draft Fields

These fields follow `pydantic_schema_reference.md` and are separate from protocol fixture metadata.

```yaml
case_id: canoo_walmart_2022_v0_14
batch_id: canoo_walmart_2022_v0_14_draft_pack
labeling_rubric_version: v0_14
mapping_table_version_pin: v0_14_mvp
ledger_authors:
  - TBD_PRIMARY_LABELER
  - TBD_SECOND_LABELER
second_label_diffs: []
frozen_band_inputs: NOT_FROZEN
must_address_items: CANDIDATE_ONLY
underreach_observability:
  present: false
  basis: null
  notes: >
    FA-05 requires declaring underreach_observability.present false before this case is frozen.
    Opportunity cost and option value are visible in CW-E01, CW-E02A, CW-E02B, CW-E04A, and CW-E04B.
    The no-primary-underreach determination rests on CW-E03 alternatives plus CW-E05A, CW-E05B,
    CW-E05C, CW-E06A, and CW-E06B counterparty and launch-burden risk. Later outcome evidence also
    lacks Walmart-specific deployment, acceptance, termination-right, financial-exposure, and
    protective-term-effectiveness facts.
leakage_audit_notes: DRAFT_ONLY_SEE_LEAKAGE_SECTION
spoiler_inventory: DRAFT_ONLY_SEE_SPOILER_INVENTORY
ledger_freeze_hash: NOT_COMPUTED
```

This is not a schema-valid frozen ledger because `frozen_band_inputs`, `must_address_items`, leakage notes, spoiler inventory, author identities, commitment timestamp, second-label workflow, and freeze hash remain unresolved.

Fields intentionally not instantiated inside the draft schema block:

```yaml
freeze_required_fields_not_instantiated:
  committed_at: required_at_ledger_freeze_as_iso_8601_utc_z_suffix
```

## Protocol Fixture Metadata

These values are required or useful for the v0.14 case-construction and run protocol, but they are not direct current Pydantic `FacilitatorLedger` fields unless a later adapter or schema revision binds them.

```yaml
case_family: strategic_supplier_selection_fleet_electrification_startup_counterparty_risk
case_family_status: CANDIDATE_PROTOCOL_METADATA
decision_shape: action_band
decision_shape_status: CANDIDATE_PROTOCOL_OR_BLIND_JUDGEMENT_METADATA_NOT_FROZEN
secondary_decision_shape_candidate: option_creation
memorization_probe_required: true
memorization_probe_required_status: PROTOCOL_LEAKAGE_INPUT_NOT_DIRECT_PYDANTIC_FIELD
known_fame_risk: unresolved_moderate_to_elevated
known_fame_risk_status: PROTOCOL_LEAKAGE_INPUT_NOT_DIRECT_PYDANTIC_FIELD
```

`decision_shape` must be frozen before any `BlindJudgement` adaptation or run. `action_band` is the leading candidate because the case tests right-sized commercial commitment under supplier-risk uncertainty. `option_creation` is a secondary lens because the blind LLM answer preserves upside through a staged option-heavy structure.

## Protocol/Pydantic Reconciliation Blocker

The imported v0.14 protocol and Pydantic reference disagree on several field placements. This fixture draft preserves the discrepancy instead of hiding it.

```yaml
protocol_pydantic_reconciliation:
  status: unresolved_implementation_blocker
  protocol_fields_not_in_current_pydantic_facilitator_ledger:
    - case_family
    - decision_shape
  protocol_must_address_fields_not_in_current_pydantic_must_address_item:
    - evidence_unit_ids
  allowed_fixture_status: draft_only
  blocks_before:
    - schema implementation
    - ledger freeze
    - scoring readiness
```

## Frozen Band Inputs - Candidate Review Table

These values are candidate review aids only. They are not frozen labels, not scoring truth, and not participant-facing material.

| Field | Candidate value | Status | Rationale to review |
| --- | --- | --- | --- |
| `evidence_strength` | `moderate` | CANDIDATE_UNFROZEN | Pre-cutoff evidence supports demand pressure, supplier promise, liquidity risk, launch burden, and an alternative supplier, but does not establish volume production or optimal commitment scale. |
| `evidence_independence` | `partially_independent` | CANDIDATE_UNFROZEN | Evidence includes retailer official sources, supplier official/SEC material, and an alternative supplier announcement, but several key claims come from interested parties. |
| `reversibility_feasibility` | `medium` | CANDIDATE_UNFROZEN | A narrow pilot or purchase-option structure may be reversible; a public multi-thousand-vehicle commitment would be materially harder to unwind. |
| `reversibility_cost` | `high` | CANDIDATE_UNFROZEN | Broad commitment could create operational dependency, public credibility transfer, route-planning risk, and reputational exposure if the supplier fails. |
| `authority` | `partial` | CANDIDATE_UNFROZEN | The role frame supports advice to leadership, but legal, procurement, finance, operations, and board authority are not fully established. |
| `authority_acquisition_cost` | `medium` | CANDIDATE_UNFROZEN | Significant supplier commitment would require cross-functional approval and diligence, but not necessarily impossible authority. |
| `capability` | `partial` | CANDIDATE_UNFROZEN | The retailer has logistics scale and some EV-fit infrastructure; the target supplier lacks proven volume production and service capacity. |
| `capability_build_cost` | `high` | CANDIDATE_UNFROZEN | Production, charging fit, route validation, service readiness, compliance, uptime, and delivery remedies are material capability gaps. |
| `loss_shape` | `asymmetric_down` | CANDIDATE_UNFROZEN | Supplier liquidity and going-concern risk create downside that can exceed early allocation or design-influence upside. |
| `opportunity_cost` | `moderate` | CANDIDATE_UNFROZEN | Waiting may lose some early allocation or design influence, but alternatives and milestone learning reduce the severity. |
| `information_decay` | `slow` | CANDIDATE_UNFROZEN | Waiting is likely to improve information through production, financing, delivery, and service evidence; no expiring window is established. |
| `option_value` | `moderate` | CANDIDATE_UNFROZEN | A pilot or staged option-heavy structure could preserve upside while limiting dependence, but protective effectiveness is not established. |
| `upside_shape` | `asymmetric_up` | CANDIDATE_UNFROZEN | Product differentiation and early influence may create upside, but the case does not establish convex upside large enough to justify broad dependence. |
| `urgency` | `low` | CANDIDATE_UNFROZEN | EV last-mile need is real, but the packet does not establish a critical timing deadline for a broad commitment to this supplier. |

Quarantine or review is required if second-labeling creates more than three disagreements, disagreement on evidence strength exceeds one level, loss-shape disagreement includes `ruinous_tail`, information-decay disagreement includes `expiring`, or disagreement cannot be resolved without importing facilitator-only material.

## Second-Label Audit Status

```yaml
second_label_audit:
  status: NOT_PERFORMED
  second_label_diffs: []
  reason: Draft fixture-authoring lane is not authorized to freeze labels or run scoring.
  required_before_scoring: true
```

## Candidate Must-Address Items

These items are candidate scorer/operator material only. They must not appear in the participant packet.

| ID | Candidate item | Evidence unit references |
| --- | --- | --- |
| MA-CW-01 | EV delivery demand is credible, but supplier selection is separable from the EV strategy. | CW-E01, CW-E02A, CW-E02B, CW-E03 |
| MA-CW-02 | The target supplier has product and option value, but not proven volume production. | CW-E04A, CW-E04B |
| MA-CW-03 | Liquidity, going-concern, burn-rate, and launch-burden risk are central to the supplier decision. | CW-E05A, CW-E05B, CW-E05C, CW-E06A, CW-E06B |
| MA-CW-04 | Alternative supplier paths reduce the case for immediate broad dependence on the target supplier. | CW-E03 |
| MA-CW-05 | Any engagement path requires milestone, funding, production, delivery, uptime, service, compliance, and remedy safeguards. | CW-E04A, CW-E04B, CW-E05A, CW-E05B, CW-E05C, CW-E06A, CW-E06B |

Evidence-unit references in this table are protocol-level traceability aids. The current Pydantic `MustAddressItem` shape does not define an `evidence_unit_ids` field; the reconciliation blocker above must be resolved before schema implementation or ledger freeze.

## Underreach Observability

Direct Pydantic draft:

```yaml
underreach_observability:
  present: false
  basis: null
  notes: >
    FA-05 requires false before ledger freeze because a no-proceed judgment would otherwise fall under-band
    under the candidate floor mechanics. Option-value and opportunity-cost pressure is visible in CW-E01,
    CW-E02A, CW-E02B, CW-E04A, and CW-E04B. The no-primary-underreach determination is supported by
    CW-E03 alternative-path evidence and CW-E05A, CW-E05B, CW-E05C, CW-E06A, and CW-E06B counterparty
    and launch-burden risk. Later Walmart-specific evidence about deployment volume, unit acceptance,
    route performance, termination rights, financial exposure, and protective term effectiveness is not established.
```

## Leakage Audit Notes

Draft `leakage_audit_notes` should carry:

- Source packet and participant packet are pre-cutoff and anonymized.
- Raw source locators, titles, file paths, and source IDs must not be shown to blind participants unless a participant-safe source-manifest adapter is accepted.
- The optional independent financial-risk media source CW-P7 remains excluded from participant-facing content.
- Facilitator-only materials include actual Walmart/Canoo identities, definitive agreement, agreement terms, Chapter 7 outcome, reveal readout, and outcome calibration.
- Candidate band inputs and must-address items are facilitator-only.
- Protocol leakage input: `memorization_probe_required: true`.
- Protocol leakage input: `known_fame_risk: unresolved_moderate_to_elevated`.

## Spoiler Inventory

Draft advisory `spoiler_inventory`:

- Walmart and Canoo names;
- the July 2022 public announcement;
- the 4,500-vehicle agreement;
- the option for up to 10,000 vehicles;
- warrant and securities terms;
- Amazon-related restrictions;
- acceptance and termination rights;
- later Canoo Chapter 7 liquidation;
- Walmart-specific evidence gaps;
- reveal readout and outcome calibration;
- owner-assisted judgment;
- candidate band inputs, action floor, action band, and scoring material;
- probe result or model-family quarantine state once any later probe exists.

## Ledger Freeze Blocker

```yaml
ledger_freeze_hash: NOT_COMPUTED
ledger_status: NOT_FROZEN
can_support_scoring: false
blocked_until:
  - participant packet source-manifest handling is resolved
  - participant packet is cleaned and hashed
  - evidence registry fields are resolved and hashed
  - band inputs are primary-labeled, second-labeled, diffed, resolved, and frozen
  - must-address items are finalized
  - underreach observability is finalized
  - protocol/Pydantic field placement for case_family, decision_shape, and must-address evidence IDs is resolved
  - committed_at is set at freeze time as a valid ISO-8601 UTC timestamp with Z suffix
  - leakage audit and spoiler inventory are finalized
  - decision_shape is frozen for the run protocol
  - blind judgement schema input is produced by a clean run or explicitly accepted as legacy adapter input
  - memorization probe passes for the target model family
```

No action band was derived from this draft ledger.

Required boundary: plumbing works only; not judgment quality.
