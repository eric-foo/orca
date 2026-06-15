```yaml
retrieval_header_version: 1
artifact_role: implementation-facing behavior/contract spec (non-authorizing) — IG capture-shape contract
scope: >
  The behavior contract for the IG capture-shape: what each IG capture packet must preserve, per metric,
  so that momentum series are rebuildable and absence is never stored as an observed value. The smallest
  next build OBJECT of the capture→projection storage lane (the one deliberate, irreversible lock-in).
  Stabilizes required behavior, non-goals, the typed-observation contract, acceptance criteria, and the
  scoping handoff. PROPOSED; authorizes NO build.
use_when:
  - Scoping or building the IG typed-metric capture field on the source-capture packet.
  - Checking what an IG capture must record per metric (value + typed posture + coverage) and why.
authority_boundary: retrieval_only
open_next:
  - docs/product/data_capture_spine/orca_capture_projection_storage_spine_architecture_v0.md   # the backbone this instantiates (capture-shape options, rebuild input set)
  - docs/product/data_capture_spine/orca_creator_monitoring_policy_architecture_v0.md           # the IG monitoring profile values
  - orca-harness/source_capture/models.py                                                       # the packet model (gated build target; NOT edited by this spec)
  - docs/product/data_capture_spine/source_capture_packet_schema_evolution_architecture_v0.md   # governs the v1→v2 manifest bump
stale_if:
  - The owner overturns the capture-shape (b) decision, the posture enum, or the identity/conflict policy.
  - The backbone's Reframe 1 / rebuild-input-set is amended.
  - The models.py field-add is built (moves this from contract to implemented).
status: PROPOSED — IG capture-shape contract; instantiates the cross-vendor-reviewed backbone; authorizes no build
```

# IG Capture-Shape Contract — Spec (PROPOSED, v0)

**Confirm-don't-trust:** load-bearing sources — the backbone + monitoring policy (this lane, committed
`49b5d0b`); `orca-harness/source_capture/models.py` + the IG capture findings (ig-cadence-rails worktree
`@ c365dca2`); `source_capture_packet_schema_evolution_architecture_v0.md` (origin/main,
`ADOPTED_WITH_AMENDMENT_V0`). Re-verify before strict/actionable use.

**Spec status: `SPEC_COMPLETE_READY_FOR_SCOPING`**

## Required behavior

1. Each IG capture packet must record, **per metric in the IG metric set**, a **typed value**, a **typed
   availability posture**, and the capture's **coverage/window boundary** — such that absence, a null, a
   not-applicable metric, or an un-attempted read can **never** be stored as if it were an observed value
   (in particular, never as an observed `0`).
2. The capture shape is a **typed shared observation, discriminated on metric identity** (decision (b)) —
   not a bespoke field per metric (a), and not a single untyped `metric_value` column (c, rejected). Each
   observation carries its own typed value and its own posture.
3. **Value and posture are coupled at write time:** a value is present **iff** posture = `observed`; a
   reason is present **iff** posture ≠ `observed`. A non-observed observation carries no value.
4. **Typing is packet-recoverable.** Each packet pins the schema version that defines the
   metric→typed-value mapping and the identity/conflict-policy version, so the typed series rebuilds from
   the packet alone — **without** consulting any external runtime registry.
5. **Identity is the stable numeric id**, never the mutable username; a re-capture of the same entity
   records a typed re-capture relationship.
6. Each capture declares **which posts / period it claims to cover**, so a post missing from the claimed
   window is distinguishable from one that was never attempted.

## Non-goals

- **Authorizes no build.** Editing `orca-harness/source_capture/models.py` is runtime work and is
  **double-gated**: (1) separate explicit owner authorization, and (2) the v1→v2 breaking `manifest_version`
  bump must handle persisted-v1-packet read-back per the schema-evolution doctrine (whose read-back
  mechanism is build-deferred) **or** confirm no v1 packets need to survive. Out of scope here.
- The derived projection EAV row, the projection store, cross-platform unification, the velocity/momentum
  derivation, and the monitoring **scheduler mechanics** are not defined here (other artifacts; rebuildable
  / deferred).
- `R` (safe reads/day), the at-scale repeated-harvesting behavior, and empirical confirmation that IG's
  logged-out surface distinguishes every posture-reason (private vs blocked vs rate-limited vs hidden) are
  **probe-confirmed at build**, not by this spec.

## Interfaces / contracts

- **Typed observation (per metric, on the capture packet):**
  `{ metric: <closed metric identity>, posture: MetricPosture, value: <typed, present iff observed>,
  reason: <present iff posture ≠ observed>, coverage_window: {start, end} }`.
- **`MetricPosture` (new closed enum):** `observed` / `unavailable_with_reason` / `out_of_capture_window`
  / `not_attempted` / `not_applicable`. (The AR-01 four **plus** `not_applicable`, required because an
  image post genuinely has no `view_count` — a distinct state from blocked/hidden/0.) `reason` is a
  closed-vocabulary token for the non-observed states (e.g. `private`, `blocked`, `rate_limited`,
  `metric_hidden`, `content_type_inapplicable`).
- **IG metric set + value types:** account-level — `follower_count` (int ≥ 0); identity/time —
  `numeric_id` (stable key), `capture_time`; per-post, keyed by `shortcode` + `timestamp` —
  `view_count` (int ≥ 0), `like_count` (int ≥ 0), `comment_count` (int ≥ 0). Each metric value carries its
  posture.
- **Identity / conflict policy (versioned):** stable key = `numeric_id`; `username` = mutable attribute;
  re-capture relationship ∈ `{supersede, supplement, conflict, mixed}` (the existing
  `re_capture_relationship` vocabulary). The policy version is pinned per packet.
- **Version pinning:** each packet carries the `manifest_version` defining its metric→type mapping and the
  identity/conflict-policy version — the "registry" is the manifest-pinned model definition, not an
  external lookup.
- **IG monitoring profile (the contract's monitoring parameters; all R-tunable):** content-unit =
  reel/post; momentum metric = `view_count`; curve window ≈ 30d; age-bucket cadences 0–5d daily / 6–15d
  every 3d / 16–30d weekly; per-creator concurrently-tracked cap K ≈ 30; Tier-C heartbeat ≈ weekly.

## Acceptance criteria

- A **video-post** capture records `view_count` with posture `observed` and a typed integer value —
  including a genuine `0` recorded as observed `0`.
- An **image-post** capture records `view_count` with posture `not_applicable` + reason, and **no value**.
- A **blocked / private / rate-limited / hidden** metric records posture `unavailable_with_reason` + the
  matching reason token, and no value.
- A metric **outside the declared coverage window** records posture `out_of_capture_window`; an
  un-attempted metric records `not_attempted`; neither carries a value.
- No capture can store a **non-observed** metric **with** a value (the coupling invariant rejects it).
- Two captures of the same creator under **different usernames but the same `numeric_id`** resolve to one
  entity; a conflicting re-capture records a typed re-capture relationship.
- A metric's **typed series is reconstructable from packets alone** (each packet pins the version defining
  its metric→type mapping); no external registry read is required.
- A post **missing** from a capture's claimed coverage window is distinguishable from one **not attempted**.

## Open questions

- **Deferred to scoping:** whether the typed observation attaches to `SourceCaptureSlice` or a new
  sub-model, and the exact discriminated-union encoding — implementation shape; the contract is
  shape-agnostic. *Safe to defer:* it does not change what must be true.
- **Deferred to build/probe:** empirical confirmation that IG's logged-out surface lets capture fill each
  posture-reason in practice. *Safe to defer:* the contract defines the reasons; the probe confirms fill.
- **Deferred to build (gated):** the v1→v2 manifest bump + persisted-v1 read-back handling + the owner
  authorization for the runtime field-add. *Safe to defer:* these gate the build, not the contract's intent.
- **Resolved here:** capture shape = (b); `MetricPosture` = AR-01 four + `not_applicable`; value↔posture
  coupling; identity = `numeric_id`; version-pinning makes typing packet-recoverable.

## Downstream handoff

```yaml
spec_handoff:
  status: SPEC_COMPLETE_READY_FOR_SCOPING
  required_behavior: "Per-metric typed value + typed posture + coverage window on each IG capture packet; typed-shared-observation shape (b); value↔posture coupled; identity = numeric_id; typing packet-recoverable via version pinning."
  non_goals: "No models.py edit / no build (double-gated); no projection store, EAV row, cross-platform unification, velocity layer, or scheduler mechanics; R + at-scale posture fill are probe-confirmed."
  interfaces_contracts: "Typed observation {metric, posture, value, reason, coverage_window}; MetricPosture closed enum (AR-01 four + not_applicable); IG metric set + int types; versioned numeric-id identity/conflict policy; manifest version-pinning."
  acceptance_criteria: "observed-0 vs not_applicable vs unavailable_with_reason vs out_of_capture_window vs not_attempted all distinguishable; no value on non-observed; same numeric_id across usernames = one entity; series rebuildable from packets alone; missing-in-window ≠ not-attempted."
  deferred_open_questions:
    - "exact sub-model placement + discriminated-union encoding -> scoping"
    - "empirical IG posture-reason fill -> build/probe"
    - "v1->v2 bump + persisted-v1 read-back + owner authorization -> gated build"
  review_timing_advisory:
    adversarial_review: recommended
    highest_value_checkpoint: after_artifact_pre_implementation
    review_target: "this IG capture-shape contract spec"
    why_this_checkpoint: "it binds the one irreversible, un-re-capturable lock-in; reviewing before the build implements it prevents baking a wrong typed shape into manifest v2."
  scoping_may_rely_on: "the (b) decision, the MetricPosture enum + coupling, the IG metric set + types, the versioned numeric-id identity/conflict policy, the coverage-window contract, and per-packet version pinning."
```
