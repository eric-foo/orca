# Reddit / Data-Capture Lane Hygiene Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: Repository hygiene inventory record (classify-only)
scope: >
  Read-only inventory + classification of the broad Reddit / data-capture lane's
  uncommitted (untracked + modified + staged) work, to support an owner-triaged
  cleanup. Classification only; not validation, readiness, acceptance, or a
  commit/delete authorization.
use_when:
  - Deciding what Reddit/data-capture uncommitted work to commit, discard, or defer.
  - Avoiding a re-inventory of the same dirty state.
authority_boundary: retrieval_only
created: 2026-06-08
branch: ecr-sp3-timing-deriver-slice1
method: 6 read-only Explore agents fanned out by concern-cluster; results synthesized.
stale_if:
  - Files are committed, discarded, or moved (re-inventory the changed set).
  - The worktree dirty set changes materially.
```

## Summary

~106 files classified across 6 clusters. Headline: the broad lane holds **~88
durable, keep-worthy artifacts that are uncommitted** (built across many
sessions, never saved to git), plus ~18 disposable / superseded / owner-decision
items.

| Cluster | Files | Keep-worthy | Other | Key flags |
|---|---|---|---|---|
| Harness code + tests | 20 | 20 | -- | 3x LIVE_NETWORK; 5 modified (armory infra) |
| Product / architecture | 18 | 17 | 1 owner-decision | 1 modified |
| Decisions | 11 | 11 | -- | 1 staged, 1 modified |
| Review-outputs | 17 | 17 | -- | 5 awaiting adjudication |
| Prompts + research | 16 | 13 | 1 precompact, 1 owner-decision, 1 superseded | 9 consumed |
| Workflows + scratch | ~24 | 10 | 6 precompact, ~8 scratch | no secrets |
| Total | ~106 | ~88 | ~18 | -- |

## Risk flags

- **LIVE_NETWORK (3):** `orca-harness/runners/run_reddit_candidate_intake_live.py`,
  `orca-harness/runners/run_reddit_old_http_batch.py`,
  `orca-harness/source_capture/adapters/direct_http.py` (modified). The live-fetch
  surface; gated by run-envelopes + AST import-contract tests that forbid network
  imports in the spine. Committing the code is not executing it, but it is the
  live capability.
- **No DANGLING_TESTS:** code/test pairing is sound (incl. AST no-network contract tests).
- **No SECRETS:** operator inputs are public Reddit HTML / thread manifests; no creds/PII.
- **Git state:** 1 staged (`data_capture_spine_reddit_candidate_url_intake_default_policy_decision_v0.md`);
  modified tracked: `data_capture_spine_source_access_tooling_build_authorization_v0.md`,
  `source_capture_toolbox/reddit_precommercial_capture_consolidation_planning_thread_v0.md`,
  plus armory-infra (`source_capture/__init__.py`, `adapters/__init__.py`,
  `adapters/direct_http.py`, and two source-capture tests).

## Bucket A -- keep-worthy (~88)

- **Code + tests (20):** candidate-intake live runner+tests+contract; consolidation
  module (`source_capture/reddit_consolidation/` = `__init__`, `consolidator`,
  `html_dom`, `parser`) + tests; batch-quality runner+test; old-http-batch
  runner+test; 5 modified armory-infra files (different sub-lane).
- **Product / architecture (17):** candidate-url-intake contract; reddit crawler
  architecture; intake-surface consolidation; lane product thesis; post-batch patch
  plan; pressure-test slot1/slot2/slot3 sessions + all-slot + closeout syntheses;
  MV-05 reddit API pricing replay; source-observability requirements scoping; 3
  source_capture_toolbox reddit docs (playbook, consolidation runner spec, success-signal arch).
- **Decisions (11):** reddit default-policy (staged); post-batch patch-plan owner
  decision; post-slot3 recapture-delta acceptance; pressure-test batch classification;
  4 source-observability decisions/authorizations; 2 candidate-intake delegated-review
  adjudications; source-access tooling build authorization (modified).
- **Review-outputs (17):** 12 adversarial-artifact reviews + 5 delegated code/artifact
  review-and-patch records (5 of these have proposed-but-unapplied patches awaiting
  Chief Architect adjudication -- see in-flight caveat).
- **Prompts + research (13):** 9 consumed review prompts; 4 worker/threading prompts
  (slot2 capture, mechanical projection, vocabulary checker, manifest framing); N=3 synthesis.
- **Workflows / closeouts (10):** candidate-intake closeouts (pilot 001 executed,
  blocked-input, b2b_001, seo_002), dry-use receipt, fixture rehearsal, pilot plan/packet,
  old-reddit search-surface handling, intake->projection handoff.

## Bucket B -- owner-decision (2)

- `docs/product/data_capture_spine_posture_vocabulary_enforcement_proposal_v0.md` -- awaiting Data Capture lane ratification.
- `docs/prompts/data_capture_pressure_test_slot3_reddit_manifest_architecture_thread_prompt_v0.md` -- boundary call vs mechanical projection.

## Bucket C -- superseded (1)

- `docs/research/data_capture_spine_pressure_test_batch_synthesis_n2of3_v0.md` -- replaced by the N=3 synthesis. Discard or keep as history (owner call).

## Bucket D -- disposable (~15)

- **Precompact checkpoints (7):** the `docs/hygiene/precompact_*` reddit/capture-spine
  packets + 1 prompt-cluster precompact. Disposable by their own contract.
- **Scratch operator inputs (~8 + bulk):** `docs/_inbox/reddit_candidate_intake_operator_inputs/`
  (2 HTML), `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/`
  (manifests + ~30 mechanically projected thread outputs).

## In-flight caveat (load-bearing for cleanup)

A chunk of Bucket A is **other threads' in-progress work**, not settled lane records:
the 5 delegated review-and-patch outputs carry proposed-but-unapplied patches
**awaiting Chief Architect adjudication**, and the posture-vocabulary proposal awaits
ratification. "Keep-worthy artifact" does not mean "ready to commit now" for these;
committing them blanket could freeze other threads' mid-decision state prematurely.
Their commit timing is each owning thread's call, not this hygiene pass's.

## Open structural questions (gate the commit cleanup)

1. **Branch placement.** `ecr-sp3-timing-deriver-slice1` is the ECR branch; Reddit
   work has been accumulating here (already mixed since 159017d). Commit the rest
   here (low-friction, consistent, local/reversible) or move to a dedicated branch
   (clean lanes, costs history surgery on already-committed Reddit work)?
2. **Live-network code.** Commit the 3 LIVE_NETWORK files with the rest (architecturally
   sanctioned + gated), or hold separately?

## Scope note

Inventory covered Reddit / candidate-intake / consolidation / pressure-test work.
The **source-capture-armory** sub-lane (CloakBrowser, proxy, cadence runners/modules)
has additional untracked code that was **not** inventoried here -- adjacent lane, separate pass.

## Non-Claims

Not validation, readiness, acceptance, review verdict, a commit authorization, a
delete authorization, or proof any listed artifact is correct or complete. Disposition
labels are recommendations for owner triage only.
