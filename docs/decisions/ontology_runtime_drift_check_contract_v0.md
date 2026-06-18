# Ontology<->Runtime Drift-Check Contract v0 (W2b leak-surface semantics)

```yaml
retrieval_header_version: 1
artifact_role: Orca decision record
scope: >
  The contract pinning the leak-surface semantics of the ontology<->runtime
  drift-check (.agents/hooks/check_ontology_drift.py): which TOP-LEVEL
  class-local serialized surfaces count as a self-identifying (payload-leaking)
  name, which names the not_payload_identifier guard protects, how composed_with
  classes are handled, and the nested-payload scope boundary plus its tripwire.
  Resolves the three semantics the #268 leak-guard hardening surfaced, as
  revised by a cross-vendor architecture pass. Prepare-only: it specifies a
  conformance delta and changes no code.
use_when:
  - Modifying or reviewing check_ontology_drift.py's not_payload_identifier leak guard.
  - Adding or changing a runtime_binding in ontology.yaml (what the guard checks).
  - Adjudicating whether a drift-check finding is a real leak or a false positive.
authority_boundary: retrieval_only
open_next:
  - .agents/hooks/check_ontology_drift.py
  - orca/product/spines/foundation/ontology/ontology.yaml
  - docs/decisions/adversarial_review_routing_policy_v0.md
stale_if:
  - The conformance delta in this contract is implemented (the PENDING rows become DONE).
  - A runtime binding introduces a nested BaseModel / discriminated-union payload (the tripwire fires; the top-level scope must be revisited).
  - Pydantic's serialization semantics for alias / serialization_alias / computed fields change.
```

## Status

**Prepare-only contract.** It pins the leak-surface semantics of the
ontology<->runtime drift-check and resolves three questions the #268 leak-guard
hardening surfaced. It **specifies a conformance delta** to
`.agents/hooks/check_ontology_drift.py` but **changes no code, edits no
ontology.yaml binding, and authorizes no implementation.** Implementing the
delta is a separate, owner-gated follow-up.

**Revision — architecture pass (2026-06-19).** v0 was reviewed by a
**different-family (cross-vendor) controller**, which returned
`NEEDS_ARCHITECTURE_PASS`: the original "serialized payload" wording implied the
full object graph while the guard is top-level class-local. The home (Claude)
lane adjudicated the findings (independently verified against Pydantic primary
source) and set the guard's scope to **top-level class-local, complete for that
scope, with a nested tripwire** (owner-selected). See *Cross-vendor review
adjudication* below.

**Non-claims.** Not validation, readiness, or proof. All three runtime bindings
pass `check_ontology_drift.py --strict` cleanly today; these are edge /
robustness semantics, not bug fixes. No claim is made that the conformance delta
is implemented — it is PENDING.

## Context

The drift-check (`.agents/hooks/check_ontology_drift.py`, landed #267, hardened
#268) verifies the scoped alignment between the ontology SSOT
(`ontology.yaml` `runtime_bindings`) and three runtime Pydantic classes. One
invariant, `not_payload_identifier`, asserts that the runtime class name must
**not** appear as a self-identifying tag **in the serialized payload** — the
condition under which the ID-doctrine "the runtime name is just a forward-only
storage alias of the ontology name" reconciliation is safe. If the name shows up
in serialized data, the name is load-bearing in the payload, not a mere alias,
and the reconciliation breaks. #268 generalized the guard from name-only to also
inspect `Literal` values and field aliases via `_payload_identifier_surfaces`.

## Scope (the architecture decision)

The guard inspects each runtime class's **own top-level serialized surfaces** —
its fields, its computed fields, their aliases, and the `Literal` values in their
annotations — **not the full nested payload graph.** Rationale: the three
bindings are flat Pydantic models (no computed fields or discriminated unions in
the checked classes, verified); full-graph recursion is over-built for that and
amplifies the false-positive surface. Nested cases are **explicitly out of
scope** and covered by a **tripwire** (below) so the boundary is loud, never a
silent false negative.

## The contract (leak-surface set)

A name `N` is a **payload-leaking self-identifier surface** on a runtime class
`C` iff `N`, compared case-insensitively, equals any of `C`'s **top-level
serialized surfaces**:

1. a **field name** (`model_fields`) or a **computed-field name**
   (`model_computed_fields`);
2. a **`Literal` string value** reachable in any field's or computed-field's
   annotation, recursing through `Optional` / `Union` / `Annotated`; an `Enum`
   member contributes its string **`.value`**;
3. a field's or computed-field's **`alias`** or **`serialization_alias`**
   (including `alias_generator`-derived aliases, which Pydantic lands on
   `FieldInfo`). **Not** `validation_alias` (input-side; see R1).

**Conservative-proxy semantics.** The guard flags any *appearance* of an
interchangeable name in the class's top-level serialized surfaces. It is a
**flag-to-investigate, not a proof of a type discriminator**: it deliberately
over-fires (false-positive-leaning) so that a real self-identifying leak cannot
pass silently. A fire means "reconcile this binding," not "auto-fail." A guard
of this kind must prefer false positives (loud, a human reconciles) over false
negatives (a silent, unsafe reconciliation).

A binding declaring `not_payload_identifier: true` is **clean** iff none of its
**interchangeable names** — `{ ontology concept name, runtime class __name__,
explicit name_alias if present }` — is a leak surface on its runtime class **or**
any of its `composed_with` classes (each composed class scanned against the same
**concept** name set).

## Resolutions

### R1 — `validation_alias` is NOT a leak surface (DROP it)

**Decision: drop it.** `validation_alias` is **input-side** (controls
population, not serialization). Primary-source proof (Pydantic 2.13): a field
with `validation_alias="vIN", serialization_alias="sOUT"` populated `M(vIN=5)`
yields `model_dump() -> {'x': 5}` and `model_dump(by_alias=True) -> {'sOUT': 5}`;
`vIN` appears in neither. The serialization surfaces are the field name, the
`Literal` value, and `alias` / `serialization_alias`. `alias_generator`-derived
aliases are already covered — Pydantic writes them onto `FieldInfo.alias` /
`.serialization_alias` at class build (verified), which the helper reads.
Dropping `validation_alias` also moots the `AliasChoices` / `AliasPath`
sub-question (that shape is only valid on `validation_alias`).

### R2 — check the interchangeable-name SET, not one name

**Decision: check `{concept, cls.__name__, name_alias?}`.** The current guard
checks only `name_alias` if present **else** `cls.__name__`, missing the concept
name. A leak of the *concept* name is as disqualifying as a leak of the runtime
name. Accepted cost (conservative-proxy direction): adding the concept name can
false-positive if the concept name is also a legitimate field/value; a fire is a
reconciliation flag, not an auto-fail.

### R3 — extend the leak check to `composed_with` classes (against the concept set)

**Decision: yes — each `composed_with` class is scanned against the CONCEPT's
interchangeable-name set** (e.g. for `Case`: `{Case, FacilitatorLedger}`), not
against the composed class's own name. (v0 erroneously implied `CaseReport`'s own
name was in scope; it is not — `CaseReport` is a legitimate sub-type that may
self-identify.) `composed_with` classes currently get import-only checks.

## Architecture-pass additions (from the cross-vendor review)

- **A1 — computed fields are a surface (AR-01).** `@computed_field` serializes
  into `model_dump()` but is absent from `model_fields` (verified). The surface
  set must also iterate `model_computed_fields` (name + alias).
- **A2 — Enum `Literal` values (AR-03).** `Literal[SomeEnum.MEMBER]` with a
  non-`str` `Enum` is missed by an `isinstance(arg, str)` test (verified); use
  the member's string `.value`. `str`-subclass enums are caught incidentally.
- **A3 — conservative-proxy framing (AR-05).** "Surface appearance" is a
  deliberate over-approximation of "type discriminator" (see contract section).
- **A4 — nested scope boundary + tripwire (AR-02).** Out of scope (named
  limitations): nested-model field names/aliases, **nested discriminated-union
  member discriminator values**, nested computed fields. A discriminator value
  living in a union member model serializes (`{'pet': {'kind': 'Case'}}`) but is
  unreachable by annotation recursion (verified). **Tripwire:** the conformance
  delta MUST add a report-mode check that flags any binding whose runtime or
  composed class has a field whose annotation contains a nested `BaseModel` or a
  discriminated union — the point where top-level scope stops being complete. A
  tripwire fire means "revisit scope / extend the guard," converting a silent
  false negative into a loud boundary signal.

## Conformance status

| Surface / check | Current code | Contract |
| --- | --- | --- |
| `validation_alias` in surface set | included | excluded (R1) |
| computed fields (`model_computed_fields`) | not inspected | inspected: name + alias (A1) |
| `Enum` `Literal` values | missed (`isinstance str`) | use member `.value` (A2) |
| name(s) checked | `name_alias` else `cls.__name__` | set `{concept, __name__, name_alias?}` (R2) |
| `composed_with` leak check | import-only | leak-checked vs the concept set (R3) |
| nested model / discriminated union | silently uncovered | report-mode **tripwire** flags it (A4) |
| framing | "type discriminator" | conservative name-collision proxy (A3) |

All deltas are additive. R2/R3 and the new surfaces **strengthen** the guard, so
implementation must re-confirm the three live bindings stay `--strict`-clean (a
newly surfaced finding is either a real catch or a false positive to reconcile).
The existing non-vacuity `--selftest` probe should be extended with computed-field,
Enum-`Literal`, concept-name, `composed_with`, and tripwire probes.

## Cross-vendor review adjudication

A different-family controller reviewed v0 and returned `NEEDS_ARCHITECTURE_PASS`.
The home (Claude) lane adjudicated each finding as a claim and **independently
verified the load-bearing ones against Pydantic primary source** (computed
fields serialize yet are absent from `model_fields`; `Union` annotation recursion
does not reach member-model `Literal`s; non-`str` `Enum` fails `isinstance str`;
`alias_generator` aliases land on `FieldInfo`).

- **Accepted:** AR-01 (computed fields -> A1), AR-02 (nested discriminators ->
  scope boundary + tripwire A4), AR-03 (Enum `Literal` values -> A2), AR-04 (R3
  name-set inconsistency -> fixed: concept set, not the composed class's own
  name), AR-05 (overbroad -> reframed as a conservative proxy A3).
- **Confirmed:** AR-06 / R1 (`validation_alias` is input-side); its
  `alias_generator` sub-caveat is **moot** (generated aliases land on
  `FieldInfo`, already read).
- **Architecture decision (owner-selected):** top-level class-local scope,
  complete for that scope (A1/A2), with the nested tripwire (A4) — not full
  payload-graph recursion (over-built for three flat bindings and amplifies the
  A3 false-positive surface).

The revised contract above incorporates all accepted findings. A brief
re-confirmation pass is optional (the architecture is now decided and the
remaining changes are mechanical); it is the owner's call per
`docs/decisions/adversarial_review_routing_policy_v0.md`. The home lane retains
final authority over what is kept.
