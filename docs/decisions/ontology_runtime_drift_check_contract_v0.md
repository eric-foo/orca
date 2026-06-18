# Ontology<->Runtime Drift-Check Contract v0 (W2b leak-surface semantics)

```yaml
retrieval_header_version: 1
artifact_role: Orca decision record
scope: >
  The contract pinning the leak-surface semantics of the ontology<->runtime
  drift-check (.agents/hooks/check_ontology_drift.py): what counts as a
  payload-leaking type discriminator, which names the not_payload_identifier
  guard protects, and whether composed_with classes are in scope. Resolves the
  three semantics the #268 leak-guard hardening surfaced but did not adjudicate.
  Prepare-only: it specifies a conformance delta and changes no code.
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
  - A new runtime_binding shape is added that the leak-surface set does not cover.
  - Pydantic's serialization semantics for alias / serialization_alias change.
```

## Status

**Prepare-only contract.** It pins the leak-surface semantics of the
ontology<->runtime drift-check and resolves three questions the #268 leak-guard
hardening surfaced. It **specifies a conformance delta** to
`.agents/hooks/check_ontology_drift.py` but **changes no code, edits no
ontology.yaml binding, and authorizes no implementation**. Implementing the
delta is a separate, owner-gated follow-up that should land **after** the
cross-vendor review recommended in the last section.

**Non-claims.** Not validation, readiness, or proof. All three runtime bindings
pass `check_ontology_drift.py --strict` cleanly today (verified 2026-06-19);
these are edge / robustness semantics, not bug fixes. No claim is made that the
conformance delta is implemented — it is PENDING.

## Context

The drift-check (`.agents/hooks/check_ontology_drift.py`, landed #267, hardened
#268) verifies the scoped alignment between the ontology SSOT
(`ontology.yaml` `runtime_bindings`) and three runtime Pydantic classes. One of
its per-binding invariants is `not_payload_identifier`: the runtime class name
must **not** be a serialized type discriminator — the condition under which the
ID-doctrine "the runtime name is just a forward-only storage alias of the
ontology name" reconciliation is safe. If the name instead shows up **in the
serialized payload** as a type tag, the name is load-bearing in data, not a mere
alias, and the reconciliation breaks.

#268 hardened the guard from name-only (the runtime name appearing as a literal
field *name*) to also inspect `Literal` discriminator values and field aliases,
via `_payload_identifier_surfaces(cls)`. That hardening exposed three
semantic questions about *what the surface set should contain* and *which names
it should be checked against* — contract-level questions, deferred here.

## The contract

A name `N` is a **payload-leaking type-discriminator surface** on a runtime
class `C` iff `N`, compared case-insensitively, equals any of:

1. a **field name** of `C` (serializes by default), or
2. a **`Literal[...]` string value** reachable in any field's annotation,
   recursing through `Optional` / `Union` / `Annotated` (serializes as that
   field's value), or
3. a field's **`alias`** or **`serialization_alias`** (the serialized key under
   `by_alias=True`).

A binding declaring `not_payload_identifier: true` is **clean** iff none of the
binding's **interchangeable names** is a leak surface on its runtime class **or**
any of its `composed_with` classes. The interchangeable-name set is:

> `{ ontology concept name (the binding key), runtime class __name__, explicit name_alias if present }`

These are exactly the names the reconciliation treats as the-same-thing; the
guard protects all of them, because a leak of *any* one of them defeats the
"just an alias" claim.

## Resolutions

### R1 — `validation_alias` is NOT a leak surface (DROP it)

**Question.** The hardened surface set includes `validation_alias`. Is it a
serialization-leak surface?

**Decision: No. Drop it.** `validation_alias` is **input-side** — it controls
how a field is *populated*, not how it *serializes*. Primary-source proof
(Pydantic 2.13, 2026-06-19): a field with `validation_alias="vIN",
serialization_alias="sOUT"` populated as `M(vIN=5)` yields `model_dump() ->
{'x': 5}` and `model_dump(by_alias=True) -> {'sOUT': 5}` — the string `vIN`
appears in **neither** serialized form. A name reachable only via
`validation_alias` can therefore never be a payload discriminator, so including
it can only produce false positives. The true serialization surfaces are the
field name, the `Literal` value, and `alias` / `serialization_alias` (note: in
Pydantic v2 a bare `alias` sets the serialization name too unless
`serialization_alias` overrides it, so `alias` stays in scope).

**Side effect.** Dropping `validation_alias` moots the open sub-question about
extracting members from a non-string `AliasChoices` / `AliasPath`
`validation_alias` — that shape is only valid on `validation_alias`, which is no
longer inspected. `alias` and `serialization_alias` are always plain strings.

**Conformance delta (PENDING).** In `_payload_identifier_surfaces`, change the
inspected attribute tuple from `("alias", "serialization_alias",
"validation_alias")` to `("alias", "serialization_alias")`; update the helper
docstring and the `not_payload_identifier` comment in `ontology.yaml`.

### R2 — check the interchangeable-name SET, not one name

**Question.** For bindings without `name_alias` (`EvidenceUnit`; `Case ->
FacilitatorLedger`) the guard defaults the checked name to `cls.__name__`. Is a
single name right?

**Decision: No — check the full interchangeable-name set.** The guard currently
checks only `name_alias` if present **else** `cls.__name__`. So for
`CapturePacket` it checks `SourceCapturePacket` (the alias) but not the concept
name `CapturePacket`; for `Case` it checks `FacilitatorLedger` but not `Case`.
A leak of the *concept* name is just as disqualifying as a leak of the runtime
name (the payload would commit to the ontology name). The guard should check the
set `{concept, cls.__name__, name_alias?}`.

**Conformance delta (PENDING).** In the guard, replace the single lowercased
`alias` with the lowercased interchangeable-name set and test set-intersection
against `_payload_identifier_surfaces(cls)`. Expected to stay `--strict`-clean
on the live bindings (e.g. `FacilitatorLedger`'s surface is `case_id`, not
`case`); **re-verify** — a newly surfaced finding is either a real catch or a
signal this resolution is mis-scoped.

### R3 — extend the leak check to `composed_with` classes

**Question.** `composed_with` classes (e.g. `Case`'s
`scoring_models.py:CaseReport`) are currently only checked for **importability**,
not for payload-identifier leakage. Should they get the leak check?

**Decision: Yes.** `composed_with` declares that the concept's runtime
representation is *composed from* those classes, so their serialized payloads are
part of the concept's payload surface. A leak of an interchangeable name into a
composed class's payload is the same hazard. Apply the `not_payload_identifier`
check to each `composed_with` class against the same interchangeable-name set.

**Conformance delta (PENDING).** In the `composed_with` loop, after a successful
import, also test the interchangeable-name set against
`_payload_identifier_surfaces(c2)`. Expected `--strict`-clean (`CaseReport` must
not surface `case` / `facilitatorledger` / `casereport`); **re-verify**.

## Conformance status

| Surface / check | Current code | Contract | Status |
| --- | --- | --- | --- |
| `validation_alias` in surface set | included | excluded (R1) | PENDING |
| name(s) checked | `name_alias` else `cls.__name__` | set `{concept, __name__, name_alias?}` (R2) | PENDING |
| `composed_with` leak check | import-only | leak-checked (R3) | PENDING |

All three deltas are small and additive. R2 and R3 **strengthen** the guard, so
implementing them must re-confirm the three live bindings stay `--strict`-clean;
the existing non-vacuity `--selftest` probe (self-naming `Literal` +
`serialization_alias`) should be extended with a concept-name and a
`composed_with` probe.

## Adversarial review

This contract pins the semantics of a **live CI gate**, so it is a candidate for
a **cross-vendor (Codex/GPT) delegated-review-patch** per
`docs/decisions/adversarial_review_routing_policy_v0.md`, to be commissioned by
the owner (not self-reviewed) **before** the conformance delta is implemented.
The review target is the three decisions above (especially R2/R3 scope and the
R1 serialization-semantics claim), not the prose. The home (Claude) lane
adjudicates any returned findings as claims.
