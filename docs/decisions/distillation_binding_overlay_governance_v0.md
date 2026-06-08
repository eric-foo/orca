# Distillation Binding — Overlay-Governance Harness (prepare-only draft)

```yaml
retrieval_header_version: 1
artifact_role: Orca decision record
scope: per-spine distillation binding for the Orca overlay-governance harness (the always-on agent layer)
use_when:
  - Distilling an overlay-governance lesson into a carried rule or a substrate.
  - Sizing/pruning the overlay's resident instruction budget; deciding code-enforced vs actor-carried.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/distillation_doctrine_orca_spine_bindings_v0.md
  - docs/decisions/overlay_enforcement_placement_classification_v0.md
  - .agents/workflow-overlay/validation-gates.md
```

**Status: PREPARE-ONLY DRAFT** (see the index `distillation_doctrine_orca_spine_bindings_v0.md`).
Distills the overlay's *own* governance lessons. Reads recorded outcomes; **edits no
overlay-authority file and wires no new substrate.** The overlay's authority lives in
`.agents/workflow-overlay/`; this binding does not own or edit it. The per-rule placement
classification (EP-01…EP-31) is the sibling `overlay_enforcement_placement_classification_v0.md`;
this binding adds the distillation *cell* shape on top of it.

## Harness bound

The agent operating under the Orca overlay (`.agents/workflow-overlay/`, the always-on governance
layer). Governed actor: any agent doing Orca project work. Spine: read overlay → route (Cynefin) →
act (write / edit / git / spawn) → claim. Decision nodes are the tool boundaries plus the claim
boundary.

## Pole / key finding

**Mixed, trending code-enforced.** Two substrates already fire by construction (a `PreToolUse`
protected-action guard; a `PostToolUse` retrieval-header check). The EP classification recorded that
"Orca has zero governance substrate today" *before* these were built; building them is the recorded
migration from actor-carried → code-enforced. The remainder (is-this-doctrine-changing, scope,
source precedence) is genuine judgment and stays resident, owing VERIFY FIRING.

## A1 — outcome → cell pairs (real, cited)

### GUARD interactive-gate-inert-in-auto  (code-enforced)
- decision_node: `node:protected-action-enforcement-placement`
- `GUARD interactive-gate-inert-in-auto: WHEN a load-bearing protected-action rule is enforced only by an interactive ask permission → ALSO enforce it with a PreToolUse hook that fires in every permission mode → UNLESS interactive-only coverage is explicitly acceptable.`
- outcome_class: a protected-action rule silently does not fire in auto/bypass mode (no human to prompt)
- causal_miss: treating an interactive-approval gate as mode-independent enforcement
- verification: under-case (protected `git push` in auto mode) → blocked (exit 2); over-edge (`git status`) → allowed (exit 0)
- enforced_in: `.agents/hooks/guard_protected_actions.py` (PreToolUse, all modes)
- PROV: `overlay_enforcement_placement_classification_v0.md` (Update 2026-06-09): "the `ask` rules are **inert in auto / bypass mode** (no human to prompt — the agent's own `git remote -v` ran with no gate)". tier: probed (selftest 15/15; live git-push payload → exit 2). date 2026-06-09.

### GUARD header-rule-at-write-boundary  (code-enforced)
- decision_node: `node:durable-doc-write`
- `GUARD header-rule-at-write-boundary: WHEN a durable in-scope .md is written/edited → check the retrieval header at the write boundary via hook, not by resident instruction → UNLESS the artifact class is excluded by retrieval-metadata.md.`
- outcome_class: the header rule fires only when the model attends to it (unreliable) and spends resident budget
- causal_miss: carrying a mechanically-checkable boundary rule as an instruction instead of a substrate (CLASSIFY SUBSTRATE-FIRST)
- verification: under-case (write an in-scope `.md` with no header) → advisory warning; over-edge (`docs/_inbox/` scratch) → no warning
- enforced_in: `.agents/hooks/check_retrieval_header.py` (PostToolUse; `--strict` CI mode), references `retrieval-metadata.md`
- PROV: `validation-gates.md` → "Enforcement Placement" (EP-06); repo map "Active Hooks". tier: probed. date 2026-06-09.

### GUARD no-self-cert-clearing  (actor-carried; PARTIAL shell)
- decision_node: `node:gate-clearing`
- `GUARD no-self-cert-clearing: WHEN a gate/predicate/claim would clear on a self-asserted field value → do NOT clear; require an owner-produced or independently-verifiable value, else indeterminate_until_authored → UNLESS the field is computed / re-derivable / audited.`
- outcome_class: a gate clears on a value a by-hand / dry-runner / operator could simply assert reading `proven` / `pass_valid` / `complete`
- causal_miss: missing distinction — a substrate checks a field's SHAPE, never its TRUTH
- verification: under-case (hand-typed `isolation_result: proven`, no provenance) → does not clear; over-edge (recomputed sha256 match) → clears
- substrate: actor-carried core; a schema can check presence/shape only (this cell IS the EP-29 formalization of PLACEMENT IS NOT AUTHORITY)
- PROV: `validation-gates.md` → receipt-field provenance gate: "a check ... must not clear on a self-asserted field value ... A value a by-hand, unauthorized, dry-runner ... record could simply assert is not self-certifying". tier: accepted-orca-gate.

## A2 — core size / budget

Only the actor-carried remainder counts against the always-on budget; the two code-enforced cells
live in hooks at zero resident cost. The actor-carried remainder is the EP classification's JUDGMENT
set (EP-23 source precedence, EP-24 Cynefin, EP-25 smallest-complete, EP-26 source-gated method,
EP-29 core, EP-30 chat topology). Budget is model-dependent (doctrine §3 A2); set against the
deploying model — not fixed here (prepare-only). When full: one-in / one-out.

## A3 — spine / decision nodes

`node:protected-action-enforcement-placement` · `node:durable-doc-write` · `node:gate-clearing` ·
`node:doctrine-change-closeout` (DCP receipt) · `node:cynefin-route` · `node:spawn-payload` (EP-18).
Cells index by `decision_node` (doctrine §3 A3).

## A4 — slots filled

- **intervention-type set** (closed; owner-extensible): `GUARD`, `HOOK-SUBSTRATE`, `SCHEMA-GATE`, `SOURCE-RULE`.
- **verification substrate**: `guard_protected_actions.py` + `check_retrieval_header.py` (+ `--strict` CLI/CI backstop); else human review of outputs against intent.
- **fire-log capability**: MODERATE and growing — hook exit codes + selftests are a deterministic log for the two code-enforced cells; the judgment remainder has no checkable surface signal (audit = human review), so its prune triggers are limited to the structural ones (Impossible/Subsumed/Superseded).
- **tier enum**: {accepted-orca-gate, probed, asserted}.
- **review window**: owner sets (e.g. per overlay change or when the EP classification `stale_if` trips).
- **owner map**: the overlay owner.

## Secondary finding

This spine is the live demonstration that placement *migrates*: EP-01/EP-03/EP-06 moved from
actor-carried (the EP classification's "zero substrate today") to code-enforced (two hooks). The
judgment remainder (Cynefin, scope, DCP-ness) is exactly the budget EP §0 says to reserve.

## Scaffold (no cell invented)

EP-04 and EP-08…EP-13 are PARTIAL in the EP classification (checkable shell → schema; truth →
resident); their schemas are proposed-not-built and owner-gated. They are slots here, not cells.

## Non-claims

Prepare-only; references existing substrates and builds none; not validation, readiness, approval,
or source-of-truth promotion; placement is not authority.
```
