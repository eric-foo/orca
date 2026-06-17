# Judgment Level 1 Todo Harness Reconciliation v0

```yaml
retrieval_header_version: 1
artifact_role: Judgment Spine product artifact (Level 1 todo and harness reconciliation map)
scope: >
  Inventory-backed map of what is landed in the active Judgment lane, what
  exists only on sibling branches, and what Level 1 product-learning harness
  pieces still need to be authored before a fragrance case can run cleanly.
use_when:
  - Choosing the next docs-only Level 1 Judgment slice after the fragrance skeleton and casebook work.
  - Distinguishing active-lane authority from sibling-only prompt, commission, or validator work.
  - Preventing existing product-learning cases from being mistaken for admitted fragrance Level 1 cases.
authority_boundary: retrieval_only
open_next:
  - docs/product/judgment_spine/judgment_current_state_and_decomposition_v0.md
  - docs/product/judgment_spine/fragrance_level1_product_learning_satellite_skeleton_v0.md
  - docs/product/judgment_spine/fragrance_level1_casebook_admission_frame_v0.md
  - docs/product/judgment_spine/fragrance_level1_named_case_candidate_screen_v0.md
  - docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md
stale_if:
  - The current-state/decomposition map changes the Level 1 default route, SCV loop, core/satellite boundary, or retired-core-artifact status.
  - A sibling branch named here merges, is retired, or is retargeted to the active Level 1 route.
  - A named fragrance Level 1 case is admitted.
  - Source registry, outcome-label, forecast, action, decision-log, evaluation, or receipt artifacts land.
```

## Status

This is a docs-only reconciliation and work queue. It does not change the
Level 1 route, adopt sibling branches, authorize prompts, authorize source
capture, admit a named case, run a case, score anything, or create proof.

The active route remains: use
`judgment_current_state_and_decomposition_v0.md` plus the fragrance Level 1
organizers. The separate
`judgment_level1_product_learning_core_minimum_v0.md` artifact is retired in
the active lane.

## Orca Start Preflight

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S3 judgment Level 1 state audit plus sibling-branch inventory
  edit_permission: docs-write
  target_scope: docs-only reconciliation map for Level 1 todo/harness state; no prompt execution, implementation, run, source capture, scoring, proof, or readiness claim
  dirty_state_checked: yes
  blocked_if_missing: AGENTS.md, overlay README, source-of-truth, decision-routing, source-loading, current-state/decomposition map, fragrance organizers, active lane git status, sibling branch inventories
```

Cynefin routing classified this as mixed/complicated docs reconciliation. The
allowed move was source audit plus a narrow retrieval/to-do artifact. The
disallowed move was to resurrect the removed standalone core-minimum doc or
merge sibling-only prompt work as if it were current lane authority.

## Verified Snapshot

Observed on 2026-06-18 from local git state:

| Surface | Observed state | Reconciliation meaning |
| --- | --- | --- |
| Active Judgment lane | `codex/judgement-lane` at `fa829130`, clean, tracking origin | This is the source state this map reconciles against. |
| Core-minimum artifact | Removed from active lane by `b5921361` | Do not route new work through the standalone core-minimum artifact unless an owner later reverses the deletion. |
| Commission signal-board branch | `codex/commission-gate` at `53fec8ac`, clean, tracking origin | Signal-board prompt, playbook, validator, fixtures, and tests exist only on this sibling branch. |
| Level 1 prompt-artifacts branch | `codex/judgment-level1-prompt-artifacts` at `c65bb20`, tracking origin, with one untracked handoff file | Commission-gate and judgment prompts exist only on this sibling branch and still point at the retired core-minimum doc. |
| PR metadata | `gh pr view` was blocked by local proxy (`127.0.0.1:9`) during this audit | This artifact claims local branch/file state only, not GitHub PR state. |

## Landed In Active Lane

| Area | Active owner or artifact | What exists now | What not to claim |
| --- | --- | --- | --- |
| Current Level 1 route | `docs/product/judgment_spine/judgment_current_state_and_decomposition_v0.md` | Core/satellite split, backtesting-first default, commission/source/forecast/action/log/eval slots, and retired-core-artifact note | Not run authority, prompt approval, source authority, proof, readiness, or judgment-quality evidence |
| Fragrance reconciliation | `docs/product/judgment_spine/fragrance_level1_product_learning_reconciliation_v0.md` | Maps the uploaded fragrance working pack into current Judgment product-learning boundaries | Not adoption of the temp pack as a runnable system |
| Fragrance skeleton | `docs/product/judgment_spine/fragrance_level1_product_learning_satellite_skeleton_v0.md` | Slot organizer for casebook, source, evidence, weighting, forecast, action, decision log, reveal/eval, lesson, and receipt fields | Not a completed schema or admitted case |
| Casebook frame | `docs/product/judgment_spine/fragrance_level1_casebook_admission_frame_v0.md` | 25-slot casebook shape, admission minimums, slot buckets, and outcome-label families | Not named-case admission |
| Named-case screen | `docs/product/judgment_spine/fragrance_level1_named_case_candidate_screen_v0.md` | Candidate ranking; first suggested admission attempt is Boy Smells 2.0 / Sephora rebrand | Not admission, source capture, or signal interpretation |
| Existing product-learning cases | `orca-harness/cases/product_learning/` and `orca-harness/reports/product_learning/` | Real product-learning case assets and reports exist for several beauty/software/product decisions | Not Level 1 fragrance casebook admission, not current Level 1 route completion |

## Existing Case Inventory Boundary

The active lane has product-learning harness material, but it is a parallel
asset class, not the new fragrance Level 1 casebook.

Observed active case-folder inventory:

```text
14 product_learning case folders under orca-harness/cases/product_learning/
11 case reports under orca-harness/reports/product_learning/
1 fragrance-specific case folder observed: nueco_fragrance_pivot_v0
```

Representative complete or near-complete case folders include:

- `cocokind_holdprice_2025_v0`
- `imaginaryauthors_sku_kills_2024_v0`
- `joahbeauty_cvs_kill_2024_v0`
- `kinderbeauty_box_pivot_2023_v0`
- `nueco_fragrance_pivot_v0`
- `privatepacks_retail_retreat_v0`
- `saie_price_increase_2025_v0`
- `selflessbyhyram_target_entry_2023_v0`
- `sundaily_gummy_pivot_v0`

Use these as learning references for packet shape, source-capture residue,
blind-run findings, and report structure. Do not count them as admitted
fragrance Level 1 casebook rows unless a later admission artifact explicitly
records the casebook minimum fields.

## Sibling-Only Work

| Sibling branch | What exists there | Reconciliation status | Before integration |
| --- | --- | --- | --- |
| `codex/commission-gate` | `docs/prompts/product-planning/orca_commission_signal_board_prompt_v0.md`, `docs/workflows/commission_signal_board_playbook_v0.md`, `.agents/hooks/check_commission_signal_board_output.py`, validator fixtures/tests, adjudication packet | Useful upstream evidence/signal-board work, but absent from active `codex/judgement-lane` | Decide whether Level 1 uses the signal board as an upstream evidence-routing object, then merge or cherry-pick through the active route without turning it into a Judgment gate |
| `codex/judgment-level1-prompt-artifacts` | `docs/prompts/product-planning/judgment_level1_commission_gate_prompt_v0.md` and `docs/prompts/product-planning/judgment_level1_judgment_prompt_v0.md` | Prompt artifacts exist, but they still name `judgment_level1_product_learning_core_minimum_v0.md` as an accepted source | Retarget the prompts to `judgment_current_state_and_decomposition_v0.md` plus the fragrance organizers, then rerun prompt-artifact validation |
| `codex/judgment-level1-prompt-artifacts` | Untracked `docs/hygiene/judgment_level1_prompt_artifacts_pr234_handoff_v0.md` | Local untracked hygiene artifact only | Do not rely on it unless the owning branch explicitly tracks or retires it |

## Remaining Harness Pieces

This table is the actionable queue. It names the object to author or reconcile,
not a permission to execute it.

| Slice | Current state | Needed output | Main blocker or dependency |
| --- | --- | --- | --- |
| Active-route prompt reconciliation | Prompt artifacts exist only on stale sibling branch | Retargeted Level 1 commission/judgment prompts or wrappers that point to current-state/decomposition, not the retired core-minimum doc | Prompt-orchestration must own durable prompt edits |
| Commission/signal-board relationship | Signal board exists only on `codex/commission-gate` | Decision: upstream signal-board object, Level 1 commission-gate object, or both with clear boundary | Avoid renaming the signal board into a Judgment gate or demand classifier |
| Named-case admission | Casebook shape and candidate screen exist | One named fragrance admission artifact or row with cutoff, source governance, outcome labels, forecast targets, benchmark policy, and non-claims | No source registry/governance artifact yet |
| Source registry and source-family governance | Candidate venues and beauty venue hints exist | Level 1 source registry or source-governance artifact with provenance and capture-authority pointers | Source-capture authority is external; venue hints are not capture permission |
| Outcome-label sheet | Outcome-label families exist in the casebook frame | Canonical Level 1 outcome-label sheet or per-case outcome-label section | Must stay evaluation-only, not scoring or proof |
| Evidence and graph-family plan | Slot exists in current-state map and skeleton | Case-specific evidence plan, graph-family retrieval shape, cutoff boundary, and source exclusion notes | Requires named case and source-governance boundary |
| C1/C2 qualitative weighting | Demand-read/C2 owners exist as proposed product-learning surfaces | Qualitative weighting trace template with caveats, no-row handling, and signal IDs | No numeric weights, formula, deterministic score, or scorer route |
| Forecast records | Slot exists; forecast boundary is defined | Sealed forecast-record template with target, horizon, probability bucket, due date, outcome label, and Brier hook | Must be sealed before reveal; not calibration by itself |
| Utility/action object | C3 action ceiling exists as proposed boundary | Utility/action template using only accepted action-family vocabulary | No passive-monitor or new action vocabulary drift |
| Decision log | Slot exists; product-learning receipt boundary exists | Per-case decision-log template binding evidence version, forecasts, utility assumptions, action, limits, and due dates | Needs evidence plan, weighting trace, and forecast/action fields |
| Reveal/evaluation and benchmark | JSG-08 and near-half learning surfaces exist by pointer | Evaluation sheet or record with outcome labels, benchmark comparison, regret/error labels, and forecast note | Cannot reveal before sealed pre-reveal call |
| Product-learning receipt | Evidence ladder names receipt minima | Per-case Level 1 product-learning receipt template | Completed receipt requires real case artifacts, not organizer fields |
| Data-science/calibration layer | Forecast hooks can be recorded | Later calibration/Brier aggregation design after enough sealed cases exist | Do not build a calibration claim from zero or one completed case |

## Recommended Next Order

1. Reconcile the sibling prompt artifacts to the active route. Retire or replace
   references to `judgment_level1_product_learning_core_minimum_v0.md`.
2. Decide how the commission signal board relates to Level 1 Judgment:
   upstream evidence-routing board, Level 1 commission surface, or separate
   sibling object.
3. Author the source-registry/source-governance and outcome-label artifacts
   needed before a named fragrance case can be admitted.
4. Admit one named case through the casebook minimum. The candidate screen says
   Boy Smells 2.0 / Sephora rebrand is the first attempt to try, not an
   admitted case.
5. Author the forecast/action/decision-log/evaluation/receipt templates against
   that admitted case.
6. Run only a docs-bound, pre-reveal product-learning pass after the required
   case, source, evidence, and prompt inputs exist.

## Product-Learning Non-Claims

This artifact is not validation, readiness, buyer proof, product proof,
judgment-quality evidence, source-capture authority, prompt approval, run
authorization, scoring authorization, fixture admission, casebook admission, CI
status, PR status, or owner adoption of any sibling branch.

It is a map of open work under the existing active route. If a later artifact
turns any row here into a durable rule, gate, authority boundary, or lifecycle
boundary, that later artifact must run the Doctrine Change Propagation Contract.

## Source-Read Ledger

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/decision-routing.md`
- `.agents/workflow-overlay/source-loading.md`
- `.agents/workflow-overlay/artifact-folders.md`
- `.agents/workflow-overlay/retrieval-metadata.md`
- `.agents/workflow-overlay/validation-gates.md`
- `docs/product/judgment_spine/judgment_current_state_and_decomposition_v0.md`
- `docs/product/judgment_spine/fragrance_level1_product_learning_reconciliation_v0.md`
- `docs/product/judgment_spine/fragrance_level1_product_learning_satellite_skeleton_v0.md`
- `docs/product/judgment_spine/fragrance_level1_casebook_admission_frame_v0.md`
- `docs/product/judgment_spine/fragrance_level1_named_case_candidate_screen_v0.md`
- `docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md`
- `docs/workflows/orca_repo_map_v0.md`
- `orca-harness/cases/product_learning/`
- `orca-harness/reports/product_learning/`
- sibling worktree inventory: `codex/commission-gate`
- sibling worktree inventory: `codex/judgment-level1-prompt-artifacts`
