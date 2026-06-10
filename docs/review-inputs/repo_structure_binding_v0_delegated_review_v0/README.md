# Delegated Review Bundle - Orca Repo Structure Binding v0 (no_repo)

```yaml
retrieval_header_version: 1
artifact_role: Review input bundle
scope: >
  Self-contained no_repo delegated-review bundle for the repo-structure
  binding v0 change set: commission contract, verbatim target attachments,
  and reviewer instructions for a cross-vendor de-correlated review.
use_when:
  - Couriering this bundle to a non-Anthropic reviewer for the delegated pass.
  - Adjudicating the returned findings (home model / CA).
authority_boundary: retrieval_only
open_next:
  - docs/review-inputs/repo_structure_binding_v0_delegated_review_v0/MANIFEST.md
```

## Commission (read first)

- **Lane**: provisional opt-in Delegated Review-and-Patch convention
  (`.agents/workflow-overlay/delegated-review-patch.md`), `no_repo` access
  mode: you have NO repo access; you review the verbatim attachments in this
  bundle and return FINDINGS, not a diff. The commissioning home model (CA)
  applies and adjudicates everything afterward; your findings are decision
  input, not kept truth.
- **Who-constraint (de-correlation)**: the author/home model family is
  Anthropic (Claude). This review is valid for the cross-vendor discovery bar
  only if you are a non-Anthropic model. State your vendor/lineage in your
  output header. Unknown lineage cannot satisfy the bar.
- **Primary target (patchable scope for proposed fixes)**:
  `orca_repo_structure_binding_v0.md` - an Orca decision record that restates
  an eight-point repo-structure invariant core and binds Orca parameters.
- **Supporting read-only context (flag issues, do not propose direct edits)**:
  `check_placement.py` (the EP-04 placement checker the binding authorizes),
  `runbook.md` (the applied Phase-2 migration procedure),
  `repo-structure.yaml` (the machine map the checker consumes).
- **Why read-only review is insufficient**: the binding is doctrine-bearing; a
  wrong invariant restatement, a checker false-WARN pattern, or unsafe
  migration semantics erode compliance silently. Bounded proposed patches
  (as findings with exact suggested text) are in scope for the primary target.
- **Escalation valve**: if you find a design-level problem (not patchable in
  the target), return `NEEDS_ARCHITECTURE_PASS` with findings only.

## Review method

Run an adversarial artifact review over the primary target with the
supporting files as cross-checks. For each finding return: id, severity
(blocker/major/minor), the exact quoted text or code at issue, why it fails
(cite the in-bundle evidence - file + section/line), a bounded proposed fix
for the primary target (exact replacement text) or a flag for off-scope
surfaces, and what would prove the fix sufficient. Findings must be
self-contained: assume the adjudicator will check them against the cited
attachment text only. Close with: a verdict (sound / sound-with-patches /
NEEDS_ARCHITECTURE_PASS), a residual-risk note, and your model vendor/lineage
statement.

Attack surfaces to prioritize: (1) internal contradictions between the eight
restated invariants and the bound parameters; (2) authority leaks - any
reading under which the jb-origin doctrine, the machine map, or a passing
checker run becomes authority/validation; (3) checker semantics - fake-pass
paths, false-WARN patterns that erode compliance, map<->checker drift; (4)
migration safety - reference-rewrite scope (live vs historical vs moved-set),
hash-pin survival, reversibility claims; (5) claim inflation anywhere
(validated / ready / enforced / complete).

## Non-claims

This bundle is review input. It is not validation, readiness, acceptance, or
proof. Your findings create no strict claims; CA adjudication decides what is
kept. Attachment integrity: byte-exact copies of the in-repo files at bundle
time; hashes in `MANIFEST.md`.
