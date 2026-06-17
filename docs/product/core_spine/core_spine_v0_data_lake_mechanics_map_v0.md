# Core Spine v0 Data Lake Mechanics Map v0

```yaml
retrieval_header_version: 1
artifact_role: Product architecture map
scope: >
  Planning-only logical mechanics map for how captured source data flows from
  Source Capture through typed payload envelopes, projection, ECR, Signal
  Content, Cleaning, and Judgment without replacing raw source truth.
use_when:
  - Planning capture-to-projection-to-ECR/SCR-to-Cleaning/Judgment data flow.
  - Checking whether a downstream layer may copy, mutate, persist, or merge source truth.
  - Deciding whether a proposed storage, schema, projection-cache, or Cleaning lane is still blocked by deferred gates.
authority_boundary: retrieval_only
open_next:
  - docs/product/data_capture_spine/source_capture_tenant_payload_attachment_boundary_v0.md
  - docs/product/data_capture_spine/source_capture_core_payload_split_explainer_v0.md
  - docs/workflows/ecr_spine_submap_v0.md
  - docs/product/core_spine_v0_projection_doctrine_v0.md
  - docs/product/core_spine/core_spine_v0_cleaning_spine_foundation_v0.md
branch_or_commit:
  - Based on codex/source-capture-tenant-payload-boundary at d5dcf1a4; verify landing status before treating the payload boundary as present on another base.
stale_if:
  - The payload-boundary lane is rejected or materially changed before landing.
  - A later accepted physical envelope storage, manifest, sidecar, projection-cache, or storage-engine decision supersedes this logical map.
  - A non-IG source-family envelope probe proves the packet/slice-keyed boundary wrong or materially incomplete.
  - ECR, Signal Content, Cleaning, or Judgment ownership changes in a later accepted source.
```

## Status

`TARGET_RECOMMENDED_LOGICAL_MECHANICS_MAP_V0`.

This is a docs-only architecture map. It records the recommended logical
mechanics after the accepted Source Capture payload-boundary lane and the
delegated data-lake architecture review. It does not select physical storage,
authorize manifest migration, add code, add `SourceCaptureSlice` fields, persist
projection, design the final ECR/SCR/Cleaning/Judgment schemas, or claim
validation/readiness.

## Start Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom (data-lake mechanics over payload boundary, ECR/SCR, projection, and Cleaning)
  edit_permission: docs-write
  target_scope:
    - docs/product/core_spine/core_spine_v0_data_lake_mechanics_map_v0.md
    - docs/workflows/data_capture_spine_consolidation_map_v0.md
    - docs/workflows/ecr_spine_submap_v0.md
  dirty_state_checked: yes
  isolation: clean worktree branch codex/data-lake-mechanics-map based on codex/source-capture-tenant-payload-boundary @ d5dcf1a4
  blocked_if_missing: no (target sources present in this lane)
external_source_boundary: workflow skills and delegated passes are task-local mechanics only; Orca authority remains AGENTS.md, the overlay, and accepted Orca docs.
doctrine_propagation_expected: architecture_doctrine
```

## Source Readiness

`SOURCE_CONTEXT_READY` for a logical mechanics map.

Loaded source basis:

- `docs/product/data_capture_spine/source_capture_tenant_payload_attachment_boundary_v0.md`:
  accepted logical boundary for packet/slice-keyed typed extension envelopes.
- `docs/product/data_capture_spine/source_capture_core_payload_split_explainer_v0.md`:
  plain-language next-lane scope and non-decisions.
- `orca-harness/source_capture/models.py`: current packet, slice, file, and
  incumbent slice-field reality.
- `docs/workflows/ecr_spine_submap_v0.md`, `orca-harness/ecr/`, and
  `orca-harness/signal_content/`: ECR/SCR by-key sibling records and
  carry-or-residualize discipline.
- `docs/product/core_spine_v0_projection_doctrine_v0.md`: projection as a
  re-derived view over raw, with Cleaning consuming one raw-keyed input handle.
- `docs/product/core_spine/core_spine_v0_cleaning_spine_foundation_v0.md` and
  `docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md`:
  Cleaning/Judgment ownership boundary and raw-pull triggers.
- Three delegated architecture passes from the current thread, treated as
  advisory input only and adjudicated against the repo sources above.

One load-bearing state fact must travel with this map: the payload-boundary docs
were created on `codex/source-capture-tenant-payload-boundary` at `d5dcf1a4`.
This branch is based on that lane, so the files are present here; another base
must still verify that dependency before treating the boundary as landed.

## Decision

Adopt the logical by-key mechanics map:

```text
Source Capture writes immutable raw packet truth.
Downstream layers read by packet/slice/file keys.
Downstream layers write derived views, receipts, records, or ledgers.
No downstream layer becomes a replacement source of truth.
Physical storage and runtime mechanics remain deferred.
```

The universal handle family is the existing source-capture vocabulary:

- `packet_id` for packet-scoped identity;
- `slice_id` when a fact is slice-scoped;
- preserved file references plus `sha256` and `hash_basis` for file integrity;
- posture or derived-record IDs only as references to sibling derived records,
  never as replacements for the raw packet handle.

## Core Invariants

1. Raw `SourceCapturePacket` is canonical and immutable for this architecture
   layer.
2. Reference, never merge: projection, ECR, SCR, Cleaning, and Judgment point
   back to raw by key instead of copying source truth into a competing truth
   object.
3. Re-derive, never migrate: derived records and views can be rebuilt from
   frozen inputs; taxonomy changes are re-derivations, not stored-column
   migrations.
4. Carry supplied facts or emit named residuals; do not author missing facts
   from prose.
5. Absence, blocked access, out-of-window, not-attempted, and not-applicable
   states are postures, not observed zeroes.
6. One derived record per epistemic kind: provenance, integrity, content,
   projection, Cleaning mechanics, and Judgment effects remain separate.
7. Projection and Cleaning own mechanics only. Credibility, independence,
   salience, exclusion, Signal Integrity, Signal Use, Decision Strength, and
   Action Ceiling stay Judgment-owned.
8. New source-family payloads default to typed packet/slice-keyed attachment
   envelopes, not new direct `SourceCaptureSlice` fields.
9. Physical envelope storage, serialization, manifest changes, projection
   cache, and storage engine are not selected here.
10. Judgment raw pull-in remains first-class: when a trigger fires, the derived
   view is advisory and raw is authority.

## Layer Read/Write Map

| Layer | Reads | Writes | Authority boundary | Deferred or blocked |
| --- | --- | --- | --- | --- |
| Source Capture | Source surface, method context, capture obligations. | Immutable `SourceCapturePacket` bundle with source slices, preserved file refs, postures, hashes, and raw provenance. | Source truth and raw handle origin. | Physical lake storage/runtime beyond current packet bundle conventions. |
| Core slice frame | Packet-level capture state and per-slice capture facts. | `SourceCaptureSlice` stable facts plus current incumbent fields. | Shared capture frame. | New direct source-family fields require separate owner decision proving true cross-family core status. |
| Typed attachment envelope | Source-family payload material tied to a packet or slice. | Logical packet/slice-keyed typed payload envelope: family, payload kind, schema version, pins, body, and absence/residual posture. | Source-family payload home. | Physical representation, serialization, sidecar/manifest choice, envelope registry, and migration. |
| Projection / Projected Unit | Raw packet, stable slice facts, incumbent fields, and typed envelopes when present. | Re-derived row view, loss ledger, and projection receipt. | Mechanical convenience view over raw. | Standing projection object, projection cache, storage engine, and any salience/Judgment effect. |
| ECR integrity | Raw packet, source slices, preserved file refs, producer postures. | SP-1 identity, SP-2 inspectability, SP-3 timing, and SP-6 source-visibility postures. | Integrity sibling records keyed to raw. | Full ECR/Evidence Unit field architecture, canonical ECR object name, D2/corroborated tier, and final runtime schema. |
| Signal Content Record | Raw packet keys, source-slice body material supplied to the deriver, and ECR posture refs when supplied. | Per-slice `SignalContentRecord` referencing provenance and integrity by key. | Content sibling record, "what the signal says." | Authored-interpretation lane and any use of `FamilyDetailBase` as a competing payload home. |
| Cleaning | One input handle keyed to raw, optionally carrying projection/ECR/SCR refs. | Non-destructive transform ledger, cleaned working view, warnings, residuals, and raw-pull triggers. | Mechanics and traceability only. | Runtime Cleaning schema, tag/write location, near-match dedupe, copied-language grouping, clustering, and all Judgment effects. |
| Judgment | Traceable chain: raw, projection, ECR, SCR, Cleaning ledger, and raw pull-in on triggers. | Verdicts and decision-use outputs such as Signal Integrity, Signal Use, Decision Strength, and Action Ceiling. | Interpretation and decision-use effects. | This map does not design Judgment internals or authorize a run. |

## Logical Flow

```text
Decision Frame or approved capture need
  -> Source Capture
       writes SourceCapturePacket [canonical raw truth]
       key family: packet_id / slice_id / preserved_file sha256 + hash_basis
       |- stable core facts on the packet/slice frame
       |- incumbent SourceCaptureSlice payload fields remain readable
       |- new source-family payloads attach as logical typed envelopes
  -> Projection
       reads raw + core facts + envelopes
       writes re-derived view + loss ledger + receipt
  -> ECR
       reads raw-keyed packet/slice/file facts
       writes integrity postures
  -> SCR
       reads raw-keyed body material and posture refs
       writes content record
  -> Cleaning
       reads one raw-keyed input handle with optional sibling refs
       writes ledger + cleaned working view + warnings/raw-pull triggers
  -> Judgment
       composes by reference, reopens raw on triggers, writes effects
```

## Option Disposition

| Option | Disposition | Reason |
| --- | --- | --- |
| Logical raw-canonical, key-anchored derived siblings | Selected for this map | Matches the accepted payload boundary and existing ECR/SCR/projection/Cleaning doctrine with the least irreversible lock-in. |
| Keep adding direct `SourceCaptureSlice` fields | Rejected as default | Incumbent fields may remain readable, but more direct fields make every new source family a lake-core schema change. |
| Physicalize envelopes now | Deferred | The envelope boundary is logical and has not been exercised by a second non-IG family; storage choices are one-way doors. |
| Give each source family its own pipeline/world | Rejected | Locally simple, but breaks shared traceability, replay, Cleaning, Judgment, and cross-family evidence questions. |
| Blend raw, projection, ECR, SCR, and Cleaning into one materialized store | Rejected | Violates reference-never-merge and makes a derived object compete with raw source truth. |

## Adjudicated Delegated Findings

The delegated passes agree on the logical architecture and diverge only on how
much to commit next. The adjudication is:

- Accept DIRECTIONAL/GROUNDING for the logical target: raw is canonical;
  packet/slice/file keys are the shared handle family; projection, ECR, SCR,
  Cleaning, and Judgment are by-key readers/writers.
- Accept ADVERSARIAL as the blocker against physicalization: no manifest bump,
  no storage engine, no persisted projection, no sixth direct
  `SourceCaptureSlice` source-family field, and no schema migration from this
  map.
- Preserve the branch-status fact: payload-boundary acceptance exists on the
  payload-boundary lane at `d5dcf1a4`; this lane is based on it, but other
  integration bases must verify it.
- Carry the two live risks forward: `SourceCaptureSlice` is already a fat
  coupling point, and SCR `FamilyDetailBase` plus capture-side envelopes could
  become two parallel payload homes if not governed before use.
- Record SP-6 archive-slice keying as implemented convention, not a generalized
  packet-field contract.

## Gates Before The Next Physical Lane

Before any storage, schema, manifest, projection-cache, or envelope
serialization lane opens, the owner or lane must clear these gates:

1. Verify whether the payload-boundary lane is landed or explicitly accepted as
   the base for the new lane.
2. Run a read-only one-non-IG-family envelope probe, such as Retail/PDP or
   Reddit, to prove that packet/slice-keyed envelopes survive a real second
   family without adding new `SourceCaptureSlice` fields.
3. Decide the physical envelope representation: embedded manifest, immutable
   packet-bundle sidecar, or another hash-pinned representation.
4. Decide whether incumbent fields stay frozen, dual-read, replayed into
   envelopes, or left as legacy-only.
5. Prove that projection remains a re-derived view and that any materialized
   cache cannot become source truth.
6. Prove that `FamilyDetailBase` in SCR is not being used as a competing
   capture-payload home.

Before any Cleaning implementation lane opens, the owner or lane must decide:

- Cleaning input-handle shape and representation;
- transformation ledger schema and tag/write location;
- allowed warning/blocker vocabulary;
- raw-pull trigger propagation;
- the line between exact-identity mechanics and Judgment-owned similarity,
  copied-language, independence, credibility, or salience effects.

## Non-Goals

This artifact does not:

- authorize code changes;
- authorize packet, manifest, fixture, or migration changes;
- add or remove any `SourceCaptureSlice` field;
- choose envelope storage, serialization, registry, or physical scope;
- choose a projection cache, query plane, runtime, scheduler, or storage engine;
- define final ECR, Evidence Unit, Signal Content, Cleaning, or Judgment schema;
- authorize ECR/Cleaning/Judgment runs;
- validate any packet, source family, projection, receipt, ledger, or judgment;
- claim readiness, buyer proof, implementation completion, or product proof.

## Known Risks And Not-Proven Items

- The accepted payload-boundary docs are branch-dependent relative to main until
  landed or explicitly accepted as the base for another lane.
- The extension-envelope boundary is not yet built and not yet exercised by a
  non-IG source family.
- `SourceCaptureSlice` already carries incumbent source-family fields; the
  "transitional/incumbent" label is a docs boundary, not a code-enforced block.
- SCR `FamilyDetailBase` is an empty future extension slot and must not become a
  second source-family payload home without an owner decision.
- SP-6 archive-slice keying currently depends on a naming convention, not a
  generalized contracted packet field.
- The exact physical place where capture lands in a future lake is still open.

## Direction Change Propagation

```yaml
direction_change_propagation:
  doctrine_changed: >
    Orca now has a planning-only logical data-lake mechanics map: raw
    SourceCapturePacket is canonical; stable packet/slice/file keys and
    packet/slice-keyed typed payload envelopes feed projection, ECR/SCR,
    Cleaning, and Judgment through by-key references; derived layers write
    views, receipts, records, or ledgers only, and physical storage/schema/
    migration remain deferred.
  trigger: architecture_doctrine
  related_triggers:
    - workflow_authority
  controlling_sources_updated:
    - docs/product/core_spine/core_spine_v0_data_lake_mechanics_map_v0.md
    - docs/workflows/data_capture_spine_consolidation_map_v0.md
    - docs/workflows/ecr_spine_submap_v0.md
  downstream_surfaces_checked:
    - AGENTS.md
    - .agents/workflow-overlay/README.md
    - .agents/workflow-overlay/source-of-truth.md
    - .agents/workflow-overlay/source-loading.md
    - .agents/workflow-overlay/artifact-folders.md
    - .agents/workflow-overlay/artifact-roles.md
    - .agents/workflow-overlay/retrieval-metadata.md
    - .agents/workflow-overlay/validation-gates.md
    - docs/product/data_capture_spine/source_capture_tenant_payload_attachment_boundary_v0.md
    - docs/product/data_capture_spine/source_capture_core_payload_split_explainer_v0.md
    - docs/workflows/ecr_spine_submap_v0.md
    - docs/product/core_spine_v0_projection_doctrine_v0.md
    - docs/product/core_spine/core_spine_v0_cleaning_spine_foundation_v0.md
    - docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md
    - orca-harness/source_capture/models.py
    - orca-harness/ecr/
    - orca-harness/signal_content/
  intentionally_not_updated:
    - path: orca-harness/source_capture/models.py
      reason: Docs-only logical map; no code/schema migration or new slice field is authorized.
    - path: orca-harness/ecr/
      reason: Built ECR derivers already follow the by-key pure derivation discipline; this map adds no code work.
    - path: orca-harness/signal_content/
      reason: SCR remains a by-key content sibling; FamilyDetailBase risk is recorded here without changing code.
    - path: docs/workflows/orca_repo_map_v0.md
      reason: The Data Capture and ECR submaps route to this artifact; the top-level map already routes through those submaps.
    - path: docs/product/core_spine_v0_projection_doctrine_v0.md
      reason: Existing projection doctrine already constrains projection as a re-derived view over raw.
    - path: docs/product/core_spine/core_spine_v0_cleaning_spine_foundation_v0.md
      reason: Existing Cleaning foundation already records the non-destructive, raw-keyed handle boundary; runtime schema remains deferred.
  stale_language_search: >
    rg -n "data-lake mechanics|data lake mechanics|SourceCaptureSlice|extension envelope|projection cache|ECR|Signal Content|Cleaning|Judgment|FamilyDetailBase|archive-body slice"
    docs/product docs/workflows orca-harness/source_capture orca-harness/ecr orca-harness/signal_content
  stale_language_search_result: >
    Executed 2026-06-17 on branch codex/data-lake-mechanics-map. Hits were
    expected across this artifact, the accepted payload-boundary and explainer
    docs, existing projection/ECR/SCR/Cleaning boundary docs, and current
    source_capture/ecr/signal_content code. No checked live surface converted
    this map into storage selection, manifest migration, projection-cache
    authorization, a new SourceCaptureSlice-field authorization, or
    implementation readiness.
  non_claims:
    - not validation
    - not readiness
    - not implementation authorization
    - not storage selection
    - not migration authorization
```
