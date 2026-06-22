<!-- fixture_expected: pass -->
<!-- fixture_purpose: minimum CSB-first scanning artifact receipt shape passes -->

# Fixture CSB-First Scan

```yaml
retrieval_header_version: 1
artifact_role: Research artifact (fixture)
scope: Fixture for the CSB-first scanning artifact checker.
use_when:
  - Testing the checker.
authority_boundary: retrieval_only
```

## Scan Intake Receipt

```yaml
commission_id: fixture_csb_first_scan
scan_date: 2026-06-23
mode: forward
subject: Fixture Brand
market_or_geography: US
source_context_status: SOURCE_CONTEXT_READY
run_caps:
  max_screening_moves_total: 8
  max_exact_queries_total: 3
screening_moves_used: 4
exact_queries_used: 2
hidden_venue_pointers: 1
capture_requests: 1
closeout_state: no_candidate_after_discovery
```

## Broad Scout Return

The bounded `broad_scout_return` checked public buyer-language venues, exact
query risk, hidden venue value, negatives, and current-state route priority.
It did not decide candidates.

## CSB Board Intake

Board source: `docs/research/fixture_csb.md`.

Rows consumed as route map: SBR-001 through SBR-003.

## Exact Query Discovery Ledger

| Query ID | Query text | Intent | Result class | Next-route decision |
| --- | --- | --- | --- | --- |
| EQ-001 | `"Fixture Brand" "Fixture Product" review` | Test buyer-language venue. | negative | Record gap. |
| EQ-002 | `"Fixture Product" stockout` | Test current-state venue. | hidden_venue_pointer | Record HVP-001. |

## Venue Evaluation Move Log

| Move | CSB row(s) | Frontier | Value class | What happened | Stop check |
| --- | --- | --- | --- | --- | --- |
| M01 | SBR-001 | Official PDP | venue_value | Current state observed. | a:no b:no c:no |
| M02 | SBR-002 | Forum query | negative | No readable buyer-origin venue surfaced. | a:no b:branch-close c:no |

## Hidden Venue Pointers

```yaml
hidden_venue_pointer_id: HVP-001
source_move_id: M02
url: https://example.test/fixture-hidden-venue
reason: >
  Public venue worth later inspection, not demand proof.
```

## Observations

```yaml
observation_id: OBS-001
source_move_id: M01
url: https://example.test/fixture-product
retrieval_date: 2026-06-23
short_quote_or_summary: >
  Fixture official PDP had current-state availability.
signal_stage: access_note
gate_role: none
```

## Negatives And Access Notes

- `NEG-001`: No public buyer-language venue surfaced inside the exact-query cap.
- `ACCESS-001`: One community surface needed an authorized screening read.

## Capture Triage

```yaml
capture_request_id: CR-001
triage_result: preservation_only
urls:
  - https://example.test/fixture-product
route_binding_state: unknown
not_proven:
  - demand proof
  - gate clearance
```

## Candidate Decision

```yaml
candidate_decision:
  closeout_state: no_candidate_after_discovery
  independent_origins_seen: []
  reason: >
    Fixture scan has venue value but no gradeable independent buyer-origin
    support.
```

## Closeout

`no_candidate_after_discovery`.
