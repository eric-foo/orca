# Cross-Vendor Blind-Run Findings — cocokind_holdprice_2025_v0 (dev case)

**Status: product-learning observation record. NOT distilled.**
Observed facts from one by-hand exam run. Derives no harness/method/judgment-quality
claims. Every result is a product-learning observation, not a validated conclusion.

- Case: `cocokind_holdprice_2025_v0` (Batch 2 **dev** case)
- Harness: `v0_14`
- Recorded: 2026-06-16 (slice 2 dev arm)
- Frozen scoring key freeze hash: `71093da84ee9c15a86878e8d698704f8056d99d3dc38b6d9fbb10a1d5900a814`

## 1. Scope and cap

By-hand exercise that uses the harness; not judgment-quality. Dev case → may inform
method; run **once** per arm. Packet was built outcome-blind in slice 1 (#172); this
record now includes Claude and GPT-5.5 blind runs. Isolation instructed/attested
(sub-agent, `tool_uses=0`, web-off by instruction; Codex CLI `gpt-5.5` external run
recorded with no tool-like events observed in the JSONL transcript). `memorization_probe_result`
hardcoded `not_run`; recognition collected. Band inputs facilitator-set (slice 1), owner
ratification pending.

## 2. Exam setup

- **Decision question:** at the 2025-06-01 cutoff, should cocokind hold prices, raise to
  offset tariff cost pressure, or selectively adjust SKUs — and with what confidence?
- **Calibrated band from the frozen key: [1, 4], band_status: normal.** Moderate evidence,
  correlated (ceiling 4); low pressure floors → floor 1.
- **Held outcome (hindsight only; roster-stated, not independently verified):** cocokind
  **held** prices (founder publicly stated a hold-price position under tariff pressure;
  absent from a later tariff-raiser list).

## 3. Clean blind runs (scored)

| contestant | family | call | vs band [1,4] | recognition | isolation | score id |
|---|---|---|---|---|---|---|
| `claude_sonnet_isolated_subagent_v0` | Anthropic (claude-sonnet-4-6) | **3** | **in-band** | recognized brand = yes; attested no post-2025 info used | sub-agent, `tool_uses=0` | `01KV7TCSPYRR3D2VSRX66Z914Q` |
| `gpt55_isolated_v0` | OpenAI (gpt-5.5) | **2** | **in-band** | recognized brand = yes; no specific post-cutoff information recalled | Codex CLI fresh `gpt-5.5` session, `--search` not enabled, read-only sandbox, no tool-like events observed in JSONL transcript | `01KV7YKVMVQMNFYWAXN4HY3WEC` |

- **One blocking failure event (`evidence_id_missing`):** the contestant marked its
  cost-data-gap claim (C4: "no cost/margin data appears") as `load_bearing` with **empty**
  `evidence_unit_ids`. The scorer flags any load-bearing claim with no cited evidence.
  Reported as-is (dev cases run once; not re-run to dodge the flag). Substantively the call
  is in-band; the flag is a citation-discipline miss, not a band error.
- Evidence-id presence, pre-decision status, and must-address coverage (MA-01…MA-04) passed.
- The GPT-5.5 run passed evidence-id presence, pre-decision status, load-bearing citation,
  and must-address coverage. No failure events were logged.

### JSG-08 tell-audit
Recognition = yes; attested no outcome use. The contestant recommended a **selective price
increase** (level 3); the actual held outcome was a **hold**. The recommendation diverges
from the outcome → no evidence of outcome-USE. Recorded as data; not quarantined.

GPT-5.5 also recognized the brand and recommended **holding list prices** (level 2), which
directionally aligns with the held outcome. No demonstrated outcome-use appears in the
reasoning trace, so this is recorded as data with an alignment caveat, not quarantined.

## 4. Observations
1. **In-band (3 in [1,4]).** Decision-quality pass on the ladder for this arm.
   GPT-5.5 also landed in-band (2 in [1,4]).
2. **Load-bearing absence-claim left uncited** → blocking citation flag. Contrast: the
   holdout (nueco) contestant cited all units for its analogous absence-claim. Contestant
   handling of "the decisive data is absent" claims is inconsistent across runs — a genuine
   N=1 dev observation (not a derived lesson).
3. **Dev case_id cue (limitation):** the committed packet's `case_id`
   (`cocokind_holdprice_2025_v0`, containing "holdprice") is visible to the contestant and
   mildly cues the action direction. Inherited from the slice-1-built packet (not rebuilt
   for this run); noted, not corrected.

## 5. Open / not concluded
GPT-5.5 is now recorded; Grok 4 and Gemini are not run. No harness/key/method change
made or proposed. No judgment-quality/readiness claim.

## 6. Provenance
- Score: `scores/01KV7TCSPYRR3D2VSRX66Z914Q.yaml` (gitignored).
- Blind judgement: `runs/claude_sonnet_isolated_subagent_v0/run_001/blind_judgement.yaml`.
- GPT-5.5 score: `scores/01KV7YKVMVQMNFYWAXN4HY3WEC.yaml` (gitignored).
- GPT-5.5 blind judgement: `runs/gpt55_isolated_v0/run_001/blind_judgement.yaml`.
- Case report: `reports/product_learning/cocokind_holdprice_2025_v0/case_report.yaml`.
- Packet construction receipt: `packet_construction_receipt_v0.md` (slice-1 outcome-blind build).
