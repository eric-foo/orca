# Handoff — Batch 2 External Arms Run Commission (GPT-5.5 / Grok 4 / Gemini)

```yaml
retrieval_header_version: 1
artifact_role: Implementation handoff prompt (docs/prompts/handoffs/)
scope: >
  Cross-runtime commission to run the three external panel contestants — GPT-5.5,
  Grok 4, and Gemini — as blind contestants on ALL 9 Batch 2 product-learning
  cases, completing the Batch-1 panel. The Claude-Sonnet arm is done and merged
  (slice 1 #172 + slice 2 #177). These external arms cannot be run from the Claude
  lane (no GPT/Grok/Gemini contestant runtime there); each must be run in its own
  runtime by the owner/operator. Same frozen key, same owner-ratified bands, same
  outcome-blind + anti-cherry-pick discipline as the Claude arm.
use_when:
  - Running the GPT-5.5, Grok 4, or Gemini contestant arm for Batch 2.
  - Completing the multi-model panel so Batch 2 has cross-vendor results.
authority_boundary: retrieval_only
authored_by: judgment-spine batch-2 coordination lane (Opus 4.8), 2026-06-16
supersedes: none
```

## Load Contract

- packet_version: handoff_v0
- mode: max
- created_at: 2026-06-16
- created_by_lane: judgment-spine batch-2 coordination thread (provenance only; NOT authority)
- workspace: C:\Users\vmon7\Desktop\projects\orca
- handoff_path: docs/prompts/handoffs/batch2_external_arms_run_commission_handoff_v0.md
- expected_branch: a receiving lane/operator spins up its OWN worktree/branch off `origin/main`.
- expected_head: `origin/main` at/after `31829fcb` (slice-2 PR #177); re-fetch (main moves fast).
- load_rule: confirm-don't-trust; re-verify every load-bearing fact against its compare target before acting; sender claims are hypotheses, not authority.

## Authoring Route (prompt-orchestration compliance)

```yaml
authoring_route:
  authored_via: workflow-prompt-orchestrator
  template_kind: handoff
  output_mode: saved-artifact (file-write)
  contract_applied: .agents/workflow-overlay/prompt-orchestration.md (Implementation handoff family; docs/prompts/handoffs/; header_index.py --strict + check_map_links.py --strict gates; confirm-don't-trust load contract)
  workflow_sequence_source: explicit_user_instruction + accepted_project_artifacts (signed Batch 2 ledger; band ratification record)
  not_a_claim: not validation, not readiness, not a new execution authorization beyond the signed Batch 2 ledger + band ratification, not source promotion
```

## Goal Handoff

Carried verbatim (orientation only, not authority):

- long_term_goal: Orca demand calls become trustworthy enough that an owner allocates/pays against them — trust earned by method.
- anchor_goal: Admit + run the 9 captured pre-cutoff cases as backtests under batch-ledger anti-cherry-pick discipline, results feeding L3.
- success_signal: a findings/score record per case PER ARM with ALL results reported; output fit = run-on-all + report-all with no selective construction/reporting.

```yaml
thread_operating_target_continuity:
  carried_forward: yes
  reason: same_workstream
  changed_from_input: no
  lifecycle_status: active_thread_local
  if_changed_reason: "Same anchor goal; sub-step = run the three external contestant arms so all 9 cases have the full panel."
```

## Active Objective

Run GPT-5.5, Grok 4, and Gemini as blind contestants on all 9 Batch 2 cases, in
their own runtimes; score each against the unchanged pinned key and the
owner-ratified bands; write a per-arm findings record per case; report ALL
results. This completes the Batch-1 panel for Batch 2.

## Why this is a separate runtime (not the Claude lane)

The Claude lane runs Claude-class contestants only. GPT-5.5 / Grok 4 / Gemini must
each be run where that model is the contestant (e.g. a Codex/GPT runtime for the
GPT arm, the respective model's runtime/API for Grok and Gemini). The orchestrator
of each arm may be any capable operator; the *contestant* must be the named model,
isolated.

## Exact Next Authorized Action (per arm, per case)

For each external model M in {GPT-5.5, Grok 4, Gemini}, and each of the 9 cases:

1. **Re-verify load** (confirm-don't-trust): pinned key SHA-256 `d54dcd2c…` /
   `8bfd4830…` unchanged; the case's `participant_packet.md` + `facilitator_ledger.yaml`
   present on `origin/main`; bands match the ratification record. Return a load outcome.
2. **Assemble the blind exam (operator side, outcome-aware is OK; contestant must be blind):**
   take the case's committed `participant_packet.md` (frontmatter + body) **verbatim**
   + the `facilitator_ledger.yaml` `must_address_items` (ids + descriptions) + the
   fixed action ladder (below) + the output schema (below). Do **NOT** show the
   contestant the `frozen_band_inputs`, the derived band, the `spoiler_inventory`, or
   any post-cutoff fact.
3. **Run the contestant isolated:** fresh session, web-off, no outside/training/post-cutoff
   knowledge (whitelist-only), target `tool_uses=0`. Collect a one-line **recognition
   self-report** (recognized brand? recalled any post-cutoff info? yes/no) for the
   JSG-08 tell-audit. The contestant returns the judgement YAML only.
4. **Write the judgement:** `cases/product_learning/<case_dir>/runs/<contestant_id>/run_001/blind_judgement.yaml`
   with operator-set metadata (`case_id` = the case's ledger case_id — for nueco use
   the neutralized `b2_holdout_h7_v0`; `contestant_id`; `run_id: run_001`; `model_id`;
   `model_family`; `prompt_hash` = SHA-256 of the exact contestant prompt; `temperature`;
   `harness_version: v0_14`) + the contestant's content fields.
5. **Score:** `python orca-harness/runners/run_case.py orca-harness/cases/product_learning/<case_dir>`
   (project root = `orca-harness/`). A distinct `contestant_id` per model avoids the
   duplicate-score guard. The scorer writes a gitignored score + regenerates the
   case_report (now multi-contestant).
6. **Findings:** add the arm's row to (or a per-arm section of) the case's
   `cross_vendor_blind_run_findings_v0.md`, including the call vs band, recognition,
   isolation basis, and any failure events. Report whatever it scores.

### contestant_id convention
`gpt55_isolated_v0` (GPT-5.5), `grok4_isolated_v0` (Grok 4), `gemini_isolated_v0`
(Gemini). One `run_001` per (case, contestant). Use the runs dir naming the Claude
arm used as the shape model: `runs/claude_sonnet_isolated_subagent_v0/run_001/`.

### Fixed action ladder (give to the contestant verbatim)
0 abstain · 1 wait · 2–5 graduated recommend (2 minimal … 5 strong short of escalation)
· 6 escalate · 7–8 aggressive recommend. `recommend` must use {2,3,4,5,7,8};
abstain→0, wait→1, escalate→6.

### Output schema (contestant returns one fenced yaml block)
`judgement_class`, `decision_shape`, `recommended_action{ladder_level, action_label,
rationale}`, `contestant_band_claim{claimed_floor, claimed_ceiling, reasoning,
advisory_only:true}`, `evidence_used[]{claim_id, claim_text, claim_role
(load_bearing|supporting|contextual), evidence_unit_ids}` (every load_bearing claim
MUST cite ≥1 evidence id — see Drift Guard), `must_address_items_covered[]`,
`load_bearing_assumption{statement, evidence_unit_ids, would_flip_if_false}`.
The exact pydantic models are `orca-harness/schemas/judgement_models.py:BlindJudgement`.

## The 9 cases (owner-ratified bands; operator-only — never shown to the contestant)

Bands per `docs/decisions/judgment_spine_backtest_batch2_band_ratification_v0.md`.
7 holdout (run once, report only, no method iteration) + 2 dev (cocokind, saie; may
inform method; run once). nueco's contestant-facing case_id is **neutralized**
(`b2_holdout_h7_v0`) — assemble its exam from the committed nueco packet, which already
carries the neutral id; do not reintroduce the dir name to the contestant.

## Authority And Source Ledger

- Repository instructions: `AGENTS.md` + `.agents/workflow-overlay/` (read overlay `README.md` first). Reread-required.
- Governing authority: the **signed Batch 2 ledger** (`docs/decisions/judgment_spine_backtest_batch2_ledger_declaration_v0.md`, blob to re-verify on origin/main) owns set/split/key/panel/discipline; **band ratification** (`docs/decisions/judgment_spine_backtest_batch2_band_ratification_v0.md`) owns the accepted answer key; per-lane PR + human-gated merge.
- Pinned key: `orca-harness/scoring/band_scorer.py` + `mapping_table.py`, SHA-256 `d54dcd2c…` / `8bfd4830…` — unchanged; a key change stops the batch.
- Runner: `orca-harness/runners/run_case.py` (env-agnostic Python; project root `orca-harness/`).
- Claude-arm exemplars to MIRROR (artifact shape): any slice-1 case (e.g. `joahbeauty_cvs_kill_2024_v0`) for the full run footprint; the slice-2 cases (`nueco_fragrance_pivot_v0`, `cocokind_holdprice_2025_v0`, `saie_price_increase_2025_v0`) for the blind-run + findings shape and the recognition/tell-audit treatment.
- Source gaps: external-model runtimes are operator-provided; this lane does not bind which environment runs which model.
- Not-proven boundaries: results are product-learning learning signal — NOT validation/readiness/buyer-proof.

## Drift Guard

- **Contestant must be the named external model, isolated.** The operator may be
  outcome-aware; the contestant must be blind (packet + must-address items only; no
  band, no spoiler, no post-cutoff knowledge).
- **Pinned key unchanged; bands owner-ratified.** Score only via `run_case.py`. Do not
  edit `frozen_band_inputs` or any ledger. A key/band change stops/rolls the batch.
- **Anti-cherry-pick / report-all.** Run all 9 per arm; report every result (in-band /
  over / under / escalate / failure / quarantine). Holdouts run once, report only, no
  method iteration conditioned on them; dev cases (cocokind, saie) run once.
- **JSG-08 tell-audit.** Collect recognition self-report. Contamination = demonstrated
  outcome-USE → quarantine (recorded-as-data), not silent drop. Recognition alone is not
  contamination. (Watch the saie recognition/outcome-alignment pattern noted in the
  Claude arm.)
- **Load-bearing citation.** Every `load_bearing` claim must cite ≥1 evidence id, or the
  scorer logs a blocking `evidence_id_missing` event (this happened on both Claude dev
  runs). Brief the contestant to cite the relevant evidence ids even for "the decisive
  data is absent" claims (cite the units that collectively show the absence).
- **nueco neutralization.** Keep the neutralized contestant-facing case_id
  (`b2_holdout_h7_v0`); never surface the `fragrance_pivot` dir name or the capture
  `manifest.json`/`receipt.md` (which state the outcome) to the contestant.
- **INV-1 captures** (never edit to add scores/verdicts); **do NOT route raw captures to
  L3/L4**; **product-learning cap**.

## Stop conditions

External model not the named contestant; scoring-key or band change; live-API claims
beyond a contestant run; new case admission; L3/L4 routing of raw captures. Land each
arm via per-lane PR (human-gated). Do not claim validation/readiness.

## Confirm-Don't-Trust Load Checklist

- Re-verify before acting: pinned key SHA-256 (`d54dcd2c…` / `8bfd4830…`); the signed
  Batch 2 ledger + the band ratification record; each case's `participant_packet.md` +
  `facilitator_ledger.yaml` present on `origin/main`; `run_case.py` present.
- Load outcomes: `REUSE` (proceed); `STALE_REREAD_REQUIRED` (main moved / blob changed —
  re-read); `BLOCKED_DRIFT` (key/band changed — stop); `BLOCKED_UNVERIFIABLE` (a
  load-bearing source missing — stop).

## Do Not Forget

- The contestant is the external model, isolated; the operator holds the bands.
- Pinned key + owner-ratified bands are frozen; score only via `run_case.py`.
- Report all 9 per arm; holdouts once + report-only; dev cases once.
- nueco stays neutralized (`b2_holdout_h7_v0`); never leak its dir name / capture manifest.
- Results are product-learning signal — not validation/readiness/buyer-proof.
