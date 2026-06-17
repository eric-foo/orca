# Orca Search Product Lane Binding v0

```yaml
retrieval_header_version: 1
artifact_role: Orca decision record
scope: >
  Adds `search/` as a bound docs/product/ lane (the search / answer-engine topic
  vertical), with its inclusion test and precedence rule, and references the
  scoped 4-file migration package that physically co-locates the search-primary
  artifacts. Extends the docs/product/ by-lane parameter bound in
  docs/decisions/orca_repo_structure_binding_v0.md.
use_when:
  - Deciding whether a doc belongs in docs/product/search/ versus a spine lane.
  - Authoring or revising repo-structure.yaml product_lanes or artifact-folders.
  - Planning or executing the search-lane migration.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/orca_repo_structure_binding_v0.md
  - .agents/workflow-overlay/artifact-folders.md
  - repo-structure.yaml
  - docs/migration/repo_structure_search_lane_v0/runbook.md
  - docs/product/search/README.md
stale_if:
  - repo-structure.yaml and this record disagree on the search lane or its status.
  - A later accepted Orca decision supersedes the lane, its inclusion test, or its precedence rule.
```

## Status

Owner-authorized adoption, v0. Authorized by explicit current-turn owner
instruction to create a consolidated Search lane and physically co-locate the
search-primary artifacts ("full physical move", option C), reached through a
deep-think -> assumption-gate -> re-scope -> implementation-scoping ->
micro-decision-lock sequence this session. The inclusion test, precedence rule,
lane name (`search`), and the 4-file move-set were owner-confirmed at the
micro-decision lock. This binds the lane as Orca doctrine; it is not validation,
readiness, or product proof, and it does not execute the migration (see
Migration).

## Decision

`docs/product/search/` is a bound second-level lane under `docs/product/`,
extending the by-lane axis bound in
`docs/decisions/orca_repo_structure_binding_v0.md`. It is the home for the
search / answer-engine topic vertical: how Orca captures, reads, and
source-classes search-surface and answer-engine signal (web search / SERP,
Google AI Overviews and other answer engines, zero-click, AEO/GEO, and
search-interest / "trends" as a capture surface).

This lane is a deliberate, bounded **topic** vertical placed beside the
function (spine) lanes. See "Relationship to invariant #1."

## Inclusion test (bound)

A doc belongs in `docs/product/search/` when its reason-to-exist IS the search /
answer-engine surface itself - how Orca captures it, what it exposes, or its
source-class - not a demand-integrity mechanic (scan, gate, read-taxonomy,
durability indicator) that merely consumes search as one venue among many.

## Precedence rule (bound)

When a doc is both search-primary and spine-functional, topic-primacy wins: it
lives in `search/`, not its spine lane. Every artifact keeps exactly one
physical home (invariant #6); there is no dual placement.

## Scope - what this lane holds (v0)

Move-set (search-primary; physically relocated by the migration package):

| New home `docs/product/search/` | Moved from |
| --- | --- |
| `aeo_capture_feasibility_probe_phase0_v0.md` | `source_capture_toolbox/` |
| `aeo_capture_feasibility_probe_phase0_v0_evidence.json` | `source_capture_toolbox/` |
| `demand_search_interest_sourcing_and_gate_delta_spec_v0.md` | `data_capture_spine/` |
| `demand_durability_indicator_search_interest_capture_profile_v0.md` | `data_capture_spine/` |

Stays in its spine lane, cross-linked from the lane index (demand-primary, NOT
search-primary - moving would orphan it from its functional spine and its
downstream consumers): the demand-scan core spec, the demand-scan / gate
adjudication packet, gate-definition and commission-criteria records, and the
demand-read taxonomy + adjudication.

Never in scope (different venue entirely): retail availability/restock,
price-timeseries, and review-velocity durability capture profiles.

The inclusion test governs future membership; this v0 scope is not exhaustive of
what may later qualify.

## Relationship to invariant #1 (one primary axis per subtree)

The `docs/product/` axis is otherwise by spine-function. `search/` is a topic
axis, so adding it beside the spine lanes bends invariant #1. The owner accepted
this trade at the re-scope decision. It is contained, not waived: the inclusion
test draws a narrow membership boundary, and the precedence rule preserves
invariant #6 (single physical home) by making topic-primacy decisive for the
small search-primary set. Any further topic vertical is a deliberate extension
recorded by its own decision, not an open licence.

## Migration (packaged, not executed here)

The physical co-location is packaged under
`docs/migration/repo_structure_search_lane_v0/` (manifest, dedicated
apply/reverse script, runbook, reference inventory). Applying it is gated by the
runbook precondition (clean commit checkpoint) AND an owner-coordinated freeze
of `data_capture_spine` (the move's only contended lane). This record does not
execute the move. `repo-structure.yaml` carries `search` at `status: planned`
until the apply runs, then `current` (per the migration-state discipline in the
structure binding).

## Controlling sources updated by this change

- `repo-structure.yaml` - `product_lanes` += `{ name: search, status: planned }`.
- `.agents/workflow-overlay/artifact-folders.md` - search-lane accepted-folder entry + lane-subfolder list + the direction-change-propagation receipt.
- `docs/decisions/orca_repo_structure_binding_v0.md` - bound-lanes bullet notes `search/`.
- `docs/product/README.md` - lane list includes `search/`.
- `docs/product/search/README.md` - lane front-door index (new).

## Direction change propagation

The `direction_change_propagation` receipt for this change set lives inline in
`.agents/workflow-overlay/artifact-folders.md` (a controlling overlay source
updated), per the Doctrine Change Propagation Contract in
`.agents/workflow-overlay/source-of-truth.md`.

## Non-claims

- Not validation, readiness, approval, or product proof; placement / doctrine only.
- Not execution of the migration; the move is packaged and owner-freeze-gated.
- Not a ToS, legal, or sourcing authorization; the AEO probe's own posture and
  non-claims are unchanged by relocation.
- A green `check_placement.py` run after apply is placement shape, not validation
  or authority (placement is not authority).
