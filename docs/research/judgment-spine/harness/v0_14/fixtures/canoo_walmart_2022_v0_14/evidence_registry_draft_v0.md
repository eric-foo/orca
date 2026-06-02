# Canoo/Walmart Evidence Registry Draft v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Draft EvidenceUnit registry for the Canoo/Walmart v0.14 fixture candidate.
use_when:
  - Reviewing candidate EvidenceUnit fields before any fixture freeze.
  - Mapping pre-cutoff source-packet evidence into v0.14 registry shape.
  - Checking which source fields remain unresolved before scoring.
authority_boundary: retrieval_only
input_hashes:
  source_packet_v0.md: 6E2BC0894A36C08B0712C8FE045DF812D3A8857E525CA4412832866FF405E473
  participant_packet_v0.md: E0191512B1A5AD292C023304321B6FD870B4C1CF591DDFF8708ACC69D5B3324F
  fixture_admission_review_v0.md: D81BA050852B6844D3F76D6F840C51A9538E1E4A3628B504C0820821E850D933
  pydantic_schema_reference.md: CFFC7BCAC179B752B9A77204ECA6A6399D30DD7CB6B2C52533E3EC0FDC031D8D
  judgement_case_construction_protocol.md: FDEA14A1767D135A8DD56AF073AF0E5E3206B945FB9E603F597491D795889C71
  source_acquisition_receipt_v0.md: 621EA29B85C3D98936326E47012149582BF28F7B891EE3A810844D0B1CC5264C
open_next:
  - docs/research/judgment-spine/harness/v0_14/pydantic_schema_reference.md
  - docs/research/judgment-spine/cases/canoo-walmart/source_packet_v0.md
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_acquisition_receipt_v0.md
```

- Status: EVIDENCE_REGISTRY_DRAFT_NOT_FROZEN
- Case ID: `canoo_walmart_2022_v0_14`
- Fixture status: blocked before scoring
- Registry freeze hash: `NOT_COMPUTED`
- Source-byte hashes: captured for CW-P1 through CW-P5 from current live public web bytes and CW-P6 from owner-supplied local SEC filing bytes
- Retrieval timestamps: normalized for CW-P1 through CW-P5 current capture and CW-P6 owner-supplied local file timestamp
- EvidenceUnit source shape: single-source draft units only after DFP-02 patch

## Registry Boundary

This registry maps the existing pre-cutoff source packet into draft v0.14 EvidenceUnit fields. It is not a frozen EvidenceUnit registry, not a participant packet, not a facilitator ledger, not a scoring input, and not proof of judgment quality.

CW-P7 remains excluded from participant-facing material because the source-packet safety review identified priming and identifier risk. It is not used in the participant-facing evidence registry below.

## Source Manifest Draft

| Source ID | Source role | Source date | Participant-facing status | Hash status |
| --- | --- | --- | --- | --- |
| CW-P1 | Retailer home-delivery expansion announcement | 2022-01-05 | Participant-safe only as anonymized facts; raw locator leaks identity | `87522D5B4F31CF3346047DAC39D8AE07B035FB5D3F9E99F48C37FA450FA7FC76` |
| CW-P2 | Alternative commercial EV supplier reservation announcement | 2022-01-05 | Participant-safe only as anonymized facts; raw locator leaks identity | `320B98A5BB96416E893A5BD7D6E2EEB438CBE28DFAD7A7F4655FA1397416F91F` |
| CW-P3 | Retailer transportation-emissions strategy note | 2022-06-08 | Participant-safe only as anonymized facts; raw locator leaks identity | `49E5DDEF58E3EF75843930ED6384E5ACD931D239C8FA17F4CB89269987994F24` |
| CW-P4 | Target supplier FY2021 results release | 2022-02-28 | Participant-safe only as anonymized facts; raw locator leaks identity | `EB35FFEA45F260DCE52827DC02DD0CAF7434D197E69BE92DD0E9EBA037F89A64` |
| CW-P5 | Target supplier Q1 2022 results release | 2022-05-10 | Participant-safe only as anonymized facts; raw locator leaks identity | `F354E284E9EDE1DAF9E1E9B580CFC6C56E9668465FF249CC4AEABB7A49BB4202` |
| CW-P6 | Target supplier Form 10-Q filing index | 2022-05-10 | Participant-safe only as anonymized facts; raw locator leaks identity | `4E8198C49129B07CF808BB47CD560BB6BCC7545EB5EA988F5877C2FB3E329E4D` |
| CW-P7 | Optional independent media financial-risk coverage | 2022-05 | Excluded from participant-facing material pending separate source-authoring decision | `TBD_SOURCE_BYTE_HASH` |

## Source Acquisition Status

```yaml
source_acquisition_receipt: docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_acquisition_receipt_v0.md
source_acquisition_receipt_hash: 621EA29B85C3D98936326E47012149582BF28F7B891EE3A810844D0B1CC5264C
capture_scope: current_live_public_web_bytes_for_cw_p1_through_cw_p5_and_owner_supplied_sec_file_for_cw_p6_not_historical_archive
captured_source_ids:
  - CW-P1
  - CW-P2
  - CW-P3
  - CW-P4
  - CW-P5
  - CW-P6
blocked_source_ids: []
participant_visibility: facilitator_internal_only
non_claim: Source acquisition does not freeze the registry, prove participant readiness, authorize blind use, or prove judgment quality.
```

## Draft Evidence Units

```yaml
evidence_units:
  - evidence_id: CW-E01
    source_id: CW-P1
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P1_RAW_LOCATOR_WITHHELD
    timestamp: 2022-01-05
    retrieval_timestamp: 2026-05-30T12:37:36Z
    hash: 87522D5B4F31CF3346047DAC39D8AE07B035FB5D3F9E99F48C37FA450FA7FC76
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The retailer had a real last-mile expansion pressure: a several-fold home-delivery expansion,
      thousands of additional drivers, store-footprint leverage, and a public ambition to build an
      electric delivery-van fleet. This supports demand-side pressure but not a specific supplier,
      volume, or risk threshold.

  - evidence_id: CW-E02A
    source_id: CW-P1
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P1_RAW_LOCATOR_WITHHELD
    timestamp: 2022-01-05
    retrieval_timestamp: 2026-05-30T12:37:36Z
    hash: 87522D5B4F31CF3346047DAC39D8AE07B035FB5D3F9E99F48C37FA450FA7FC76
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The retailer's expansion plan included an electric delivery-van ambition tied to controlled
      last-mile operations. This supports EV strategic fit for the retailer, not a commitment to
      any specific supplier or broad vehicle volume.

  - evidence_id: CW-E02B
    source_id: CW-P3
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P3_RAW_LOCATOR_WITHHELD
    timestamp: 2022-06-08
    retrieval_timestamp: 2026-05-30T12:37:38Z
    hash: 49E5DDEF58E3EF75843930ED6384E5ACD931D239C8FA17F4CB89269987994F24
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The retailer's own transportation framing treated EVs as attractive for some lighter, shorter,
      controlled-route use cases while preserving use-case fit and pilot learning. This supports
      operational testing discipline, not broad commitment.

  - evidence_id: CW-E03
    source_id: CW-P2
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P2_RAW_LOCATOR_WITHHELD
    timestamp: 2022-01-05
    retrieval_timestamp: 2026-05-30T12:37:37Z
    hash: 320B98A5BB96416E893A5BD7D6E2EEB438CBE28DFAD7A7F4655FA1397416F91F
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      A different commercial EV delivery-vehicle supplier with incumbent backing had already announced
      a substantial reservation with the same retailer and early activity with a major logistics customer.
      The case was not simply target supplier versus no EV delivery fleet.

  - evidence_id: CW-E04A
    source_id: CW-P4
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P4_RAW_LOCATOR_WITHHELD
    timestamp: 2022-02-28
    retrieval_timestamp: 2026-05-30T12:37:39Z
    hash: EB35FFEA45F260DCE52827DC02DD0CAF7434D197E69BE92DD0E9EBA037F89A64
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The target supplier reported differentiated EV platform development, battery work, preorders,
      U.S. operations, and facility progress. It was more than a concept deck, but volume production
      had not been proven.

  - evidence_id: CW-E04B
    source_id: CW-P5
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P5_RAW_LOCATOR_WITHHELD
    timestamp: 2022-05-10
    retrieval_timestamp: 2026-05-30T12:37:41Z
    hash: F354E284E9EDE1DAF9E1E9B580CFC6C56E9668465FF249CC4AEABB7A49BB4202
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The target supplier reported progress on gamma vehicles, testing, production preparation,
      and launch-related activity. This supports product and option value, but still does not prove
      production execution or service capacity.

  - evidence_id: CW-E05A
    source_id: CW-P4
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P4_RAW_LOCATOR_WITHHELD
    timestamp: 2022-02-28
    retrieval_timestamp: 2026-05-30T12:37:39Z
    hash: EB35FFEA45F260DCE52827DC02DD0CAF7434D197E69BE92DD0E9EBA037F89A64
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The target supplier's year-end cash and ongoing loss profile made funding capacity relevant
      to any customer commitment. This supports counterparty-risk attention, not a volume-delivery
      guarantee.

  - evidence_id: CW-E05B
    source_id: CW-P5
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P5_RAW_LOCATOR_WITHHELD
    timestamp: 2022-05-10
    retrieval_timestamp: 2026-05-30T12:37:41Z
    hash: F354E284E9EDE1DAF9E1E9B580CFC6C56E9668465FF249CC4AEABB7A49BB4202
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The target supplier's cash balance fell materially over the most recent reporting period, while
      quarterly loss and operating cash use each exceeded 100 million dollars. This makes runway and
      financing risk central to commitment design.

  - evidence_id: CW-E05C
    source_id: CW-P6
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P6_RAW_LOCATOR_WITHHELD
    timestamp: 2022-05-10
    retrieval_timestamp: 2026-05-30T12:55:01Z
    hash: 4E8198C49129B07CF808BB47CD560BB6BCC7545EB5EA988F5877C2FB3E329E4D
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The target supplier disclosed funding and runway uncertainty under accounting rules. This is a
      direct counterparty-risk input for any commitment, purchase option, deposit, publicity, or
      dependence decision.

  - evidence_id: CW-E06A
    source_id: CW-P4
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P4_RAW_LOCATOR_WITHHELD
    timestamp: 2022-02-28
    retrieval_timestamp: 2026-05-30T12:37:39Z
    hash: EB35FFEA45F260DCE52827DC02DD0CAF7434D197E69BE92DD0E9EBA037F89A64
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      Launch and production plans implied material operating and capital needs. Delivery credibility
      depended on manufacturing execution, capital access, and burn-rate control.

  - evidence_id: CW-E06B
    source_id: CW-P5
    source: PARTICIPANT_SAFE_SOURCE_ALIAS_CW_P5_RAW_LOCATOR_WITHHELD
    timestamp: 2022-05-10
    retrieval_timestamp: 2026-05-30T12:37:41Z
    hash: F354E284E9EDE1DAF9E1E9B580CFC6C56E9668465FF249CC4AEABB7A49BB4202
    pre_decision_status: verified_pre_decision
    pre_decision_basis: Source date precedes the July 2022 public action announcement.
    summary: >
      The supplier expected heavy near-term operating expense and capital expenditure tied to launch
      and production work. Any retailer engagement would need production, delivery, uptime, service,
      compliance, and remedy safeguards.
```

## Excluded Or Unresolved Source Material

```yaml
excluded_sources:
  - source_id: CW-P7
    status: excluded_from_participant_facing_registry
    reason: Optional independent media coverage carries source-title and identifier priming risk from the source-packet safety review. Core financial-risk facts are retained only when traceable to CW-P4, CW-P5, or CW-P6.
unresolved_fields:
  - registry freeze hash
  - evidence ID remapping into facilitator ledger, blind judgement adapter, and any future scoring result
```

## Non-Claims

- No frozen EvidenceUnit registry.
- No participant-packet readiness.
- No historical archive source-byte proof.
- No scoring readiness.
- No model run.
- No fixture validation.
- No judgment-quality proof.

Required boundary: plumbing works only; not judgment quality.
