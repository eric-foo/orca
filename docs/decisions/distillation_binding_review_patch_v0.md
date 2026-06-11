# Distillation Binding — Review / Patch Lanes Harness (prepare-only draft)

```yaml
retrieval_header_version: 1
artifact_role: Orca decision record
scope: per-spine distillation binding for the Orca review/patch harness (read-only review lanes + delegated review-and-patch)
use_when:
  - Distilling a review-or-patch-lane lesson into a carried rule.
  - Reasoning about de-correlated hardening, review-commission binding, or intent-bearing fitness references.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/distillation_doctrine_orca_spine_bindings_v0.md
  - .agents/workflow-overlay/review-lanes.md
  - .agents/workflow-overlay/delegated-review-patch.md
```

**Status: PREPARE-ONLY DRAFT** (see the index). Distills recorded review/patch lane outcomes. Reads
recorded outcomes; edits no overlay file; creates no review verdict, patch queue, or validation claim.

## Harness bound

The agent operating an Orca review lane (artifact / adversarial-artifact / prompt / patch-queue
review) or the Delegated Review-and-Patch convention. Governed actor: the reviewer / commissioning
CA / delegate. Decision nodes are the commission binding, the de-correlation choice, and the
fitness-reference check.

## Pole / key finding

**Actor-carried, lane-tag PARTIAL.** The lessons are judgment (don't retarget, commission a
de-correlated pass, name a missing fitness reference); a hard block is **over-edge** today because
review lanes are not machine-tagged (EP-21). One code-enforceable corner exists: `no_repo` package
freshness is a hash-compare.

## A1 — outcome → cell pairs (real, cited)

### GUARD de-correlated-hardening  (actor-carried)
- decision_node: `node:hardening-commission`
- `GUARD de-correlated-hardening: WHEN hardening a high-stakes authored artifact → commission a de-correlated (different-family) review-and-patch and record author_family ≠ delegate_family → UNLESS the artifact is low-stakes.`
- outcome_class: an author silently reintroduces the exact failure mode its own guardrails exist to prevent (self-review blind spot)
- causal_miss: missing trigger — a same-family/self pass shares the author's priors
- verification: under-case (Opus-authored high-stakes artifact) → non-Opus delegate commissioned; over-edge (low-stakes) → single pass acceptable
- substrate: actor-carried; PARTIAL — `author_family ≠ delegate_family` is a recordable field inequality, but its *truth* is self-cert (EP-29), so the field is shape-checkable only
- PROV: `delegated-review-patch.md:45` "the author encodes guardrails and can reintroduce the exact failure mode those [guardrails exist to prevent]"; recorded instance ~`:167` "a de-correlated pass caught failure modes the author had reintroduced against its own guardrails". tier: probed.

### GUARD reviewer-no-silent-retarget  (actor-carried; OVER-EDGE)
- decision_node: `node:review-commission-binding`
- `GUARD reviewer-no-silent-retarget: WHEN reviewing → do NOT silently retarget, widen the target, or treat an adjacent artifact as the review object → UNLESS the prompt or current user instruction binds that change.`
- outcome_class: a reviewer silently shifts the review object/scope, so the commissioned target is not the one actually reviewed
- causal_miss: missing distinction — commission-bound scope vs adjacent-artifact drift
- verification: under-case (reviewer drifts to an adjacent doc unbidden) → flagged out-of-commission; over-edge (prompt binds the wider target) → allowed
- substrate: actor-carried; **OVER-EDGE** — cannot hard-block without machine-tagged lanes (EP-21); a hard block on an untagged lane manufactures false confidence
- PROV: `review-lanes.md:40-42` "A reviewer must not silently retarget a review, widen the target, or treat an adjacent artifact as the actual review object unless the prompt or current user instruction binds that change." tier: accepted-orca-gate.

### GUARD intent-bearing-needs-fitness-ref  (actor-carried)
- decision_node: `node:fitness-reference-binding`
- `GUARD intent-bearing-needs-fitness-ref: WHEN reviewing an intent-bearing target with no bound fitness_reference (goal + observable success signal) → name the gap as a finding (no checkable success bar bound); do NOT silently invent the goal → UNLESS a fitness reference is bound.`
- outcome_class: a reviewer silently invents the upstream goal for a proof/fixture/plan/runbook, hiding a missing success bar
- causal_miss: missing trigger — intent-bearing correctness needs an anchored, attackable fitness reference
- verification: under-case (proof artifact, no bound fitness ref) → "no checkable success bar bound" finding; over-edge (a bound fitness reference) → review proceeds and also attacks the goal
- substrate: actor-carried (judgment)
- PROV: `review-lanes.md:59-62` "If an intent-bearing target arrives with no bound fitness reference, the review names the gap ... rather than silently inventing the goal."; owning decision `docs/decisions/work_unit_fitness_reference_v0.md`. tier: accepted-orca-gate.

## A2 — core size / budget

Actor-carried; cells compete for budget. `de-correlated-hardening` and `intent-bearing-needs-fitness-ref`
are `silent-wrong-output`-class (an unhardened artifact / a silently-invented goal are silent
defensibility losses) → prune-exempt from frequency-only retirement. Budget model-dependent; not
fixed here.

## A3 — spine / decision nodes

`node:review-commission-binding` · `node:fitness-reference-binding` · `node:reviewer-write-boundary`
(read-only unless assigned patch execution) · `node:hardening-commission` ·
`node:no-repo-freshness-gate` (hash-compare; code-enforceable) · `node:review-output-provenance`
(`reviewed_by` / `authored_by`). Cells index by `decision_node`.

## A4 — slots filled

- **intervention-type set** (closed; owner-extensible): `GUARD`, `ESCALATION` (commission back-pressure), `SCHEMA` (no_repo hash compare; provenance fields).
- **verification substrate**: the `no_repo` portable-method freshness hash-compare (deterministic); the `reviewed_by`/`authored_by` provenance fields (presence-checkable); otherwise findings-first human review.
- **fire-log capability**: MIXED — STRONG for the hash-compare corner; NONE for silent-retarget (lanes not machine-tagged); MODERATE for de-correlation (commission metadata, truth self-cert).
- **tier enum**: {accepted-orca-gate, probed, asserted}.
- **review window**: owner sets (per commission).
- **owner map**: the review-lanes owner + the delegated-review-patch convention owner.

## Secondary finding

This spine is where Orca already dogfoods the doctrine's HARDEN plug-in (de-correlated, different-
family review-and-patch) — the same move the doctrines used on themselves. The `reviewed_by`/
`authored_by` fields make same-family-vs-cross-family coverage measurable (a real recent lesson:
attribution was not previously measurable), but only when both fields carry real values.

## Scaffold / over-edge (no cell invented)

A hard reviewer-lane write block (EP-21) is over-edge until lanes are machine-tagged — named as a
slot, not distilled. The `no_repo` freshness hash-compare is code-enforceable but proposed-not-built
(owner-gated).

## Non-claims

Prepare-only; edits no overlay file; creates no verdict, severity authority, patch queue,
mandatory remediation, validation, or readiness; placement is not authority.
```
