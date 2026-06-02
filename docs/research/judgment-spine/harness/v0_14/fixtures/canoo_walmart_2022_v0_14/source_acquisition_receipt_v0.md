# Canoo/Walmart v0.14 Source Acquisition Receipt v0

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Source-byte capture receipt for the Canoo/Walmart v0.14 CW-P1 through CW-P6 provenance gate.
use_when:
  - Checking which Canoo/Walmart source bytes have been captured for EvidenceUnit hash fields.
  - Verifying retrieval timestamps and source-byte hashes before evidence-registry updates.
  - Identifying remaining source-acquisition blockers before fixture freeze or scoring gates.
authority_boundary: retrieval_only
open_next:
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/evidence_registry_draft_v0.md
  - docs/research/judgment-spine/cases/canoo-walmart/source_packet_v0.md
input_hashes:
  source_packet_v0.md: 6E2BC0894A36C08B0712C8FE045DF812D3A8857E525CA4412832866FF405E473
branch_or_commit: main @ a2aebdd
stale_if:
  - Any captured source file changes.
  - Any source URL in source_packet_v0.md changes.
  - CW-P6 SEC source bytes are replaced by a different owner-supplied or retrieved capture.
  - Owner requires historical/archive bytes instead of current live web bytes.
```

## Acquisition Boundary

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S0 plus Canoo/Walmart source packet, evidence registry, participant packet, source-manifest adapter, and receipt
  edit_permission: docs-write for provenance artifacts and source captures only
  target_scope: Capture public source bytes and retrieval timestamps for the docs-only CW-P1 through CW-P6 provenance gate.
  dirty_state_checked: yes
  blocked_if_missing: no
source_acquisition_status: COMPLETE_SOURCE_CAPTURE_CW_P1_THROUGH_CW_P6_CURRENT_OR_OWNER_SUPPLIED
```

This receipt records current live public web bytes captured on 2026-05-30 UTC
for CW-P1 through CW-P5 and an owner-supplied local SEC filing capture for
CW-P6. It does not prove that the pages are unchanged from their original
publication dates. If the fixture later requires historical source bytes as of
the original publication date or cutoff window, an archive-specific acquisition
pass remains required.

No runtime code, model run, blind use, probe execution, scoring, schema
implementation, ledger freeze, validation, product proof, or judgment-quality
claim is authorized or performed by this receipt.

## Captured Sources

All hashes are SHA-256 over the captured local file bytes.

| Source ID | Source URL | Retrieval timestamp | Local capture path | Bytes | SHA-256 |
| --- | --- | --- | --- | ---: | --- |
| CW-P1 | `https://corporate.walmart.com/news/2022/01/05/walmart-to-expand-inhome-delivery-reaching-30-million-u-s-homes-in-2022` | `2026-05-30T12:37:36Z` | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_captures/cw_p1_walmart_inhome_expansion_2022_01_05.html` | 189716 | `87522D5B4F31CF3346047DAC39D8AE07B035FB5D3F9E99F48C37FA450FA7FC76` |
| CW-P2 | `https://news.gm.com/home.detail.html/Pages/news/us/en/2022/jan/ces/0105-brightdrop.html` | `2026-05-30T12:37:37Z` | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_captures/cw_p2_brightdrop_walmart_reservation_2022_01_05.html` | 83358 | `320B98A5BB96416E893A5BD7D6E2EEB438CBE28DFAD7A7F4655FA1397416F91F` |
| CW-P3 | `https://corporate.walmart.com/news/2022/06/08/zero-sum-how-walmart-transportation-is-working-to-reduce-emissions-now-and-in-the-future` | `2026-05-30T12:37:38Z` | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_captures/cw_p3_walmart_transportation_emissions_2022_06_08.html` | 187938 | `49E5DDEF58E3EF75843930ED6384E5ACD931D239C8FA17F4CB89269987994F24` |
| CW-P4 | `https://www.prnewswire.com/news-releases/canoo-inc-announces-fourth-quarter-and-fiscal-year-2021-results-301492051.html` | `2026-05-30T12:37:39Z` | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_captures/cw_p4_canoo_fy2021_results_2022_02_28.html` | 349936 | `EB35FFEA45F260DCE52827DC02DD0CAF7434D197E69BE92DD0E9EBA037F89A64` |
| CW-P5 | `https://www.prnewswire.com/news-releases/canoo-inc-announces-first-quarter-2022-results-301544386.html` | `2026-05-30T12:37:41Z` | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_captures/cw_p5_canoo_q1_2022_results_2022_05_10.html` | 270864 | `F354E284E9EDE1DAF9E1E9B580CFC6C56E9668465FF249CC4AEABB7A49BB4202` |
| CW-P6 | `https://www.sec.gov/Archives/edgar/data/1750153/000162828022013637/goev-20220331.htm` | `2026-05-30T12:55:01Z` | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_captures/cw_p6_sec_10q_goev_2022_03_31.html` | 1013579 | `4E8198C49129B07CF808BB47CD560BB6BCC7545EB5EA988F5877C2FB3E329E4D` |

## CW-P6 Source Boundary

```yaml
source_boundary:
  source_id: CW-P6
  source_packet_url: https://www.sec.gov/Archives/edgar/data/1750153/000162828022013637/0001628280-22-013637-index.html
  captured_primary_filing_document: https://www.sec.gov/Archives/edgar/data/1750153/000162828022013637/goev-20220331.htm
  capture_source: owner_supplied_local_file
  original_local_path: C:/Users/vmon7/Documents/goev-20220331.html
  workspace_capture_path: docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/source_captures/cw_p6_sec_10q_goev_2022_03_31.html
  retrieval_timestamp_basis: owner_supplied_file_last_write_time_utc
  source_byte_hash: 4E8198C49129B07CF808BB47CD560BB6BCC7545EB5EA988F5877C2FB3E329E4D
```

CW-P6 is not treated as complete from SEC index metadata alone. The source
packet points to the filing index, while the captured source boundary is the
primary Form 10-Q HTML document supplied by the owner as an inspectable local
file. This receipt does not claim SEC-compliant automated retrieval; it records
the owner-supplied source bytes now available for fixture provenance.

## Evidence Registry Impact

CW-P1 through CW-P6 can now populate source-byte `hash` and
`retrieval_timestamp` fields in the draft EvidenceUnits that cite those source
IDs. CW-P7 remains excluded from the participant-facing material unless a later
source-authoring decision changes that boundary.

Participant-facing source-manifest fields must remain withheld placeholders.
The full source IDs, retrieval timestamps, and source-byte hashes are
facilitator/internal provenance only.

## Non-Claims

- Not an historical archive capture.
- Not a frozen EvidenceUnit registry.
- Not participant-packet readiness.
- Not blind-use readiness.
- Not memorization-probe pass.
- Not model-run authorization.
- Not scoring readiness.
- Not ledger freeze.
- Not schema implementation.
- Not validation.
- Not product proof.
- Not judgment-quality proof.

Required boundary: plumbing works only; not judgment quality.
