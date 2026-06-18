# Deletion-Evidence Doctrine v0 (Phase-2 deletion safety)

```yaml
retrieval_header_version: 1
artifact_role: Orca decision record
scope: >
  The deletion-evidence doctrine + register contract for the Phase-2 bloat-cut
  fan-out: deleting a governed artifact is central-adjudicated and two-phase, with
  no standing per-lane delete, and carries a complete evidence record in the
  deletion-evidence register, executed only via a human-merged PR. Enforced
  report-mode now (strict in Phase-3) by check_deletion_evidence.py.
use_when:
  - Proposing or executing a deletion of a governed artifact (under governed_roots).
  - Reviewing or adjudicating a deletion PR.
  - Modifying the register schema or check_deletion_evidence.py.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/deletion_evidence_register_v0.yaml
  - .agents/hooks/check_deletion_evidence.py
  - docs/migration/orca_second_pass_consolidation_plan_v0.md
stale_if:
  - The register schema changes (update this doctrine + the checker together).
  - The frozen deletion doctrine (central-adjudicated, two-phase, no per-lane delete) changes.
  - The report-mode checker is flipped to strict (Phase-3).
```

## Status

Decision record + contract. Establishes the deletion-evidence register and its
report-mode checker, ahead of the Phase-2 bloat-cut fan-out. **Non-claims:** not
validation, readiness, or proof; report-mode is visibility, not a hard gate (the
strict flip is Phase-3).

## The rule

Deleting a **governed artifact** (one under `governed_roots` in the register) is
**central-adjudicated** and **two-phase**, with **no standing per-lane delete**.
Every such deletion carries a complete evidence record in the register and is
executed only via a **human-merged PR**.

## Two-phase + central adjudication (reuses the existing PR / merge flow)

1. **PROPOSE** — a lane opens a PR that (a) removes the target(s) **and** (b)
   appends a register record with `phase: proposed` and complete evidence. The
   lane does **not** self-merge.
2. **ADJUDICATE + EXECUTE** — the **human merger** of that PR is the central
   adjudicator; merging is the approval, and the record is set to `executed`. The
   deletion takes effect only on merge.

No new adjudication machinery is invented: the existing human-merge gate
(`docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md`) **is** the
central adjudication.

## The four evidence elements (all required, non-empty)

- **reverse_ref_check** — who/what still references the target; confirmed safe to remove.
- **successor** — what replaces it (path/doc), or `none -- pure bloat`.
- **semantic_delta** — what meaning is lost vs preserved by the deletion.
- **rollback** — how to restore (the executing PR/commit; `git revert <sha>`).

## The register

`docs/decisions/deletion_evidence_register_v0.yaml` — an **append-only** YAML
audit trail (schema in the file header). Append records; never rewrite or remove
past records — the audit trail is the point. A record's `phase` advances
`proposed -> adjudicated -> executed`.

## Enforcement

`.agents/hooks/check_deletion_evidence.py` — **report-mode (exit 0) now**: reports
any deleted governed file (in the diff against the base) that lacks a complete
`executed` register record. The **strict (exit 1) flip is Phase-3**, per the
frozen-predicate ratchet the other Orca gates use. Fails open on infrastructure
gaps (no git / PyYAML / register).

## Worked example (illustrative)

```yaml
- deletion_id: "del:capture.superseded_blueprint.1"
  phase: executed
  targets: ["orca/product/spines/capture/operating_model/old_blueprint_v0.md"]
  evidence:
    reverse_ref_check: >
      0 inbound references after the v2 blueprint superseded it (grep across docs/,
      .agents/, orca/); the repo map points only at v2.
    successor: "orca/product/spines/capture/operating_model/..._architecture_v2.md"
    semantic_delta: >
      No unique content lost -- v0 is a strict subset of v2 (v2 added the projection
      section; everything in v0 is restated there).
    rollback: "git revert <executing-PR merge sha>"
  adjudicator: "owner (human merge of the executing PR)"
  proposed_by: "claude/<bloat-cut lane>"
  proposed_at: "YYYY-MM-DD"
  adjudicated_at: "YYYY-MM-DD"
  executed_at: "YYYY-MM-DD"
```
