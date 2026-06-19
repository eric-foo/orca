```yaml
retrieval_header_version: 1
artifact_role: Orca migration note
scope: >
  Master index for the Phase-2 W3a (read-only PROPOSE) fan-out: per-area
  bloat/deletion candidates + ontology findings across orca/product/ and
  docs/decisions/, assembled for the owner's CENTRAL adjudication. Executes
  nothing.
use_when:
  - Adjudicating Phase-2 W3a deletion candidates and ontology findings.
  - Choosing which areas to take into W3b execute.
authority_boundary: retrieval_only
open_next:
  - docs/migration/orca_second_pass_consolidation_plan_v0.md
  - docs/decisions/deletion_evidence_doctrine_v0.md
stale_if:
  - Any candidate is executed (deleted) or any source file in a scanned area changes.
```

# Phase-2 W3a — Propose Fan-Out Index (read-only; for central adjudication)

**This is W3a (propose) of the Phase-2 plan: read-only.** 14 subagents scanned the
corpus and produced one proposal artifact per area. **Nothing was deleted or
edited** — `git status` shows only additions under `docs/migration/phase2_proposals/`.
The owner adjudicates these candidates; **W3b (execute)** is a separate, later,
owner-gated wave.

## Scope + coverage

- **Scanned:** `orca/product/` (226 `.md`, all spines + shared + case_families +
  satellites + README) **and** `docs/decisions/` (91 `.md`, incl. the
  `consultant_loop/` subdir). Total **317 files**. Coverage verified: every file
  claimed by exactly one subagent (the 2 `docs/decisions/consultant_loop/` files
  were swept by the lead — both kept).
- **Read-only verified:** no source file modified or deleted.
- **No cross-area duplicate targets** (areas were disjoint).
- **`docs/decisions/` is ungated:** the deletion gate governs `orca/product/`
  only, so every `docs/decisions/` candidate is tagged **`ungated:
  human-review-only at execute`** — those deletions are not gate-protected.

## Roll-up

| Area | Files | Deletion candidates (hi/med/lo) | Ontology findings | Artifact |
| --- | --- | --- | --- | --- |
| capture/operating_model | 35 | **2** / 0 / 0 | 4 | `capture_operating_model_w3a_proposal_v0.md` |
| capture/contracts+rest | 19 | **2** / 0 / 0 | 1 | `capture_contracts_rest_w3a_proposal_v0.md` |
| capture/toolbox+families | 50 | 0 / 1 / 0 | 4 | `capture_toolbox_families_w3a_proposal_v0.md` |
| judgment | 25 | 0 / 3 / 1 | 1 | `judgment_w3a_proposal_v0.md` |
| case_families | 24 | 0 / 1 / 2 | 0 | `case_families_w3a_proposal_v0.md` |
| doctrine/decisions-A | 44 | **1** / 0 / 1 | 0 | `doctrine_decisions_A_w3a_proposal_v0.md` |
| doctrine/decisions-B | 45 | **1** / 0 / 0 (+5 withdrawn) | 1 | `doctrine_decisions_B_w3a_proposal_v0.md` |
| scanning | 11 | 0 / 0 / 0 | 5 | `scanning_w3a_proposal_v0.md` |
| foundation | 21 | 0 / 0 / 0 | 2 | `foundation_w3a_proposal_v0.md` |
| cleaning | 3 | 0 / 0 / 0 | 3 | `cleaning_w3a_proposal_v0.md` |
| commission_signal_board | 9 | 0 / 0 / 0 | 0 | `commission_signal_board_w3a_proposal_v0.md` |
| data_lake | 5 | 0 / 0 / 0 | 0 | `data_lake_w3a_proposal_v0.md` |
| shared | 2 | 0 / 0 / 0 | 1 | `shared_w3a_proposal_v0.md` |
| rest (satellites + README) | 6 | 0 / 0 / 0 | 0 | `rest_w3a_proposal_v0.md` |
| consultant_loop (lead-swept) | 2 | 0 / 0 / 0 | 1 (header defect) | (this index) |
| **TOTAL** | **317** | **6 / 5 / 4 = 15** | **~23** | |

## Headline

The corpus is **lean** — 317 files yield only **15 deletion candidates (6 high
confidence)** and **~23 ontology findings** (most "clean, with notes"). The
spine-first migration (#255) consolidated well; the remaining bloat is targeted.

## The 6 high-confidence deletion candidates (adjudicate first)

- **capture/operating_model** — `data_capture_harness_operating_model_architecture_v0.md`
  and `_v1.md`: superseded by `_v2.md` (v2 absorbed their unique content per the
  hybridization decision). Live refs are historical/comparative provenance, not
  active routing. *Successor resolves.*
- **capture/contracts+rest** — 2 already-accepted proposal docs absorbed into their
  parent contracts (see the artifact for the exact paths + the "parent absorbed it"
  evidence).
- **doctrine/decisions-A** — `docs/decisions/turn_07_branch_casing.md`: **0 inbound
  refs** anywhere; records a one-time pre-first-commit branch rename; the fact lives
  permanently in git. `successor: none -- pure bloat`. *Ungated.*
- **doctrine/decisions-B** — 1 high-confidence record (see the artifact). *Ungated.*

Medium/low candidates (judgment ×4, case_families ×3, capture/toolbox ×1,
doctrine-A conditional ×1) and the **5 withdrawn** doctrine-B candidates (withdrawn
because of live inbound refs / pending status) are detailed in each artifact.

## Ontology findings — mostly clean

No SSOT violations. The findings are alignment notes (e.g. scan-core
`brand_decision_event` vs SSOT `DecisionEvent`; the `milwaukee_initial_judgement.md`
non-standard `authority_boundary`), correct-absence confirmations, and two repo-wide
new-term candidates (`FailureEvent`, `RetailPdpProjectionPacket`) flagged for a later
ontology pass. Details per artifact.

## What happens next (NOT in this PR)

This PR is the **central adjudication surface** — review the candidates and decide
which to take forward. **W3b (execute)** is the separate next wave and is **gated**
on the two deferred Phase-1 rails:

- **waiver registry** (the strict deletion gate's emergency override) — needed before
  a strict-gated execute wave;
- **lane-charter template** — bounds each execute lane (W3b is "1 PR per spine").

`orca/product/` deletions execute through the deletion-evidence gate (each carries a
register record); `docs/decisions/` deletions are **human-review-only** (ungated).
