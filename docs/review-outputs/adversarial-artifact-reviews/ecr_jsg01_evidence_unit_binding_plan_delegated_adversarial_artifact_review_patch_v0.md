# Delegated Adversarial Artifact Review And Patch — JSG-01 EvidenceUnit Binding Slice Plan v0

```yaml
retrieval_header_version: 1
artifact_role: Delegated adversarial artifact review-and-patch report
scope: >
  Cross-vendor controller review and bounded patch of the JSG-01-scoped
  EvidenceUnit binding slice plan before owner ratification.
use_when:
  - Adjudicating the patched JSG-01 EvidenceUnit binding slice plan.
  - Checking the review findings, source evidence, and proposed diff before owner ratification.
authority_boundary: retrieval_only
reviewed_by: GPT-5 / OpenAI
authored_by: anthropic / claude-fable-5
de_correlation_bar: cross_vendor_discovery
```

## review_summary

```yaml
review_summary:
  target: docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md
  target_pre_sha256: DB7236B53DF19A8CF582678F9377DA3FB74B2D408E2A60C591FFADA57DE1CFDC
  target_post_sha256: 90B05867E86A00BFD43B68EF66ACEBCF744E176D6D00A2C5801BC8D53C0655CE
  controller: GPT-5 / OpenAI
  author: anthropic / claude-fable-5
  source_context: SOURCE_CONTEXT_READY
  verdict: PATCHED_WITH_MAJOR_BOUNDARY_RESIDUAL
  findings:
    critical: 0
    major: 2
    minor: 1
  validation:
    target_hash_pin: matched
    original_backup: _scratch/delegated_review_jsg01_binding_plan/originals/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md
    retrieval_header_check: passed_for_required_core_fields
    citation_check: passed_for_patched_target_explicit_line_citations
    pytest: not_applicable_docs_only
  non_claims:
    - not approval
    - not validation
    - not owner ratification
    - not JSG-01 unfreeze
    - not home-model adjudication
```

## Source Context

Loaded sources: `AGENTS.md`, `.agents/workflow-overlay/README.md`,
`.agents/workflow-overlay/delegated-review-patch.md`,
`.agents/workflow-overlay/review-lanes.md`,
`.agents/workflow-overlay/retrieval-metadata.md`,
`.agents/workflow-overlay/decision-routing.md`, `workflow-deep-thinking`,
`workflow-adversarial-artifact-review`, and the full commissioned source pack.

The requested controller who-constraint is satisfied: this review was performed
by GPT-5 / OpenAI, non-Anthropic. No reviewer subagents were spawned.

## Findings

### DRP-01 — major — D2/unfreeze boundary was over-compressed

Location: target lines 40-50, 72-76, 240-250 after patch.

Issue: The original plan described the binding as the single remaining
structural reason JSG-01 was indeterminate. That was too strong against the
frozen conductor row, which still names D2 alongside the EvidenceUnit binding
and a case-carried receipt as deferred.

Evidence: The target originally said "one remaining structural reason" in the
why-this-slice paragraph. The conductor row at
`docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md:209`
names the EvidenceUnit binding, a case packet carrying a `FinalizationReceipt`,
and D2 as still deferred. The boundary doc also says D2 remains reserved while
SP-6 may determinately residualize:
`docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md:306-308`.

Impact: Without an explicit D2 reconciliation stop, a later ratification memo
could treat this binding slice as if it had silently consumed the conductor's
D2 blocker. That would turn a reserved surface into an implied unfreeze premise.

Minimum closure condition: The plan must distinguish the composer contract from
the unfreeze ledger and require the owner ratification / unfreeze routing to
state how the conductor's D2 wording is consumed.

Next authorized action: Patched in this pass; home model should adjudicate
whether to keep, revise, or reject the D2 reconciliation language.

### DRP-02 — major — slice selection needed an anti-laundering guard

Location: target lines 93-98, 113-125, 204-210 after patch.

Issue: The original plan required full-vector carry but did not explicitly
forbid the composer or assembly from selecting a better-clearing sibling slice
once `evidence_slice_id` was available. Visibility alone is not sufficient if
the bound-row selector can be chosen for posture quality rather than content
membership.

Evidence: The target uses `evidence_slice_id` to select the JSG-01-relevant
SP-2/SP-3 row. `SourceCaptureSlice.slice_id` is a free string field at
`orca-harness/source_capture/models.py:118`, while the source-side composition
test proves mixed-grain co-reading but no aggregate verdict at
`orca-harness/tests/unit/test_ecr_source_side_composition.py:1-9` and
`186-206`. The frame invariant requires reference-never-merge and re-derive,
not re-author: `docs/workflows/ecr_spine_submap_v0.md:44-48`.

Impact: An implementer could satisfy "full vector carried" but still choose a
favorable bound row at assembly time, making a failing evidence slice look
determinately clear while the failure survives only as a sibling observation.

Minimum closure condition: The plan must state that assembly binds the slice
whose bytes carry the evidence unit content, and that the composer never searches
for or promotes a better-clearing sibling. Tests must cover failing-bound /
clearing-sibling and clearing-bound / failing-sibling cases.

Next authorized action: Patched in this pass; home model should adjudicate test
scope wording before implementation.

### DRP-03 — minor — state/citation metadata was stale after this pass

Location: target lines 12-29 and 172-174 after patch.

Issue: The original retrieval header still said PRE cross-family review and the
SP-5 producer review was pending at authoring time. After this commissioned
patch, the target needed to say the delegated review-and-patch is completed but
unadjudicated, and to avoid making a stale lane-state claim about the SP-5
producer. INV-4 also compressed producer integrity anchors and SP-5 receipt
binding hash into one ownership phrase.

Evidence: Retrieval metadata applies to materially touched durable artifacts:
`.agents/workflow-overlay/retrieval-metadata.md` core header rules require the
header to aid future retrieval without creating authority. The SP-5 consumer
owns `binding_hash` on the receipt model at
`orca-harness/schemas/finalization_models.py:66-82` and re-checks it at
`249-257`, while producer integrity anchors live in `PreservedFile` at
`orca-harness/source_capture/models.py:97-114`.

Impact: Stale review-state text can misroute future agents; compressed ownership
language can make the binding look like it owns receipt or producer integrity
state.

Minimum closure condition: Header state and built-input language must record
this pass as unadjudicated decision input, and INV-4 must separate producer-owned
integrity anchors from receipt-owned `binding_hash`.

Next authorized action: Patched in this pass; home model should decide whether
the status wording is the desired house style.

## Per-Change Citation Map

```yaml
change_citation_map:
  status_and_use_when_update:
    target_lines_after_patch: [12, 14, 27, 28]
    supports:
      - .agents/workflow-overlay/delegated-review-patch.md
      - .agents/workflow-overlay/retrieval-metadata.md
  d2_unfreeze_boundary:
    target_lines_after_patch: [40, 50, 72, 76, 240, 250]
    supports:
      - docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md:209
      - docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md:306-308
      - docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md:473-500
  slice_selection_guard:
    target_lines_after_patch: [93, 98, 113, 125, 204, 210]
    supports:
      - orca-harness/source_capture/models.py:117-127
      - orca-harness/ecr/deriver.py:29-57
      - orca-harness/ecr/deriver.py:74-141
      - orca-harness/tests/unit/test_ecr_source_side_composition.py:1-9
      - docs/workflows/ecr_spine_submap_v0.md:44-48
  inv4_ownership_split:
    target_lines_after_patch: [172, 174]
    supports:
      - orca-harness/source_capture/models.py:97-114
      - orca-harness/schemas/finalization_models.py:66-82
      - orca-harness/schemas/finalization_models.py:249-257
```

## Unified Diff

```diff
diff --git "a/_scratch\\delegated_review_jsg01_binding_plan\\originals\\ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md" "b/docs\\product\\ecr\\ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md"
index c71ee15..6a203f6 100644
--- "a/_scratch\\delegated_review_jsg01_binding_plan\\originals\\ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md"
+++ "b/docs\\product\\ecr\\ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md"
@@ -9,14 +9,14 @@ scope: >
   derived source-side postures (SP-1/2/3/6) and the current FinalizationReceipt
   read — onto one case-packet evidence unit. Advisory design; recommends but
   ratifies nothing; build gated behind owner ratification.
-status: PROPOSED_ARCHITECTURE_ROUTING_OBJECT — advisory, non-executing, PRE cross-family review, PRE ratification.
+status: PROPOSED_ARCHITECTURE_ROUTING_OBJECT — advisory, non-executing, POST delegated cross-vendor review-and-patch (unadjudicated), PRE owner ratification.
 use_when:
-  - Preparing the cross-family review of the JSG-01-scoped EvidenceUnit binding slice.
+  - Adjudicating the delegated cross-vendor review-and-patch of the JSG-01-scoped EvidenceUnit binding slice.
   - Checking what the binding composition decides vs what stays reserved (full EU architecture, canonical name).
 authority_boundary: retrieval_only
 gate_posture: JSG-01 stays FROZEN. This plan does not bind, ratify, build, or unfreeze anything.
 relates_to:
-  conductor_predicate: docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md  # JSG-01 row (~:209) — read, never edit
+  conductor_predicate: docs/product/judgment_spine/judgment_quality_promotion_operating_model_v0.md  # JSG-01 row (:209) — read, never edit
   ratified_field_schema: docs/product/core_spine/core_spine_v0_data_and_cleaning_spine_boundary_v0.md  # SP-1/2/3/6 ratification + decisions B/C; reserved decisions
   ecr_frame: docs/product/ecr/ecr_consolidation_v0_frame_source_visibility_slice_architecture_plan_v0.md  # INV-1..5, three-mode binding rule (inherited verbatim)
   sp5_contract: docs/research/judgment-spine/sp5_finalization_receipt_spec_v0.md  # the receipt + validate-only consumer contract
@@ -25,7 +25,7 @@ built_inputs: >
   ECR derivers: orca-harness/ecr/deriver.py (SP-1/2/3/6, pure, bind no EvidenceUnit).
   SP-5 model + validate-only consumer: orca-harness/schemas/finalization_models.py (committed a37f896).
   SP-5 producer (acting half): orca-harness/runners/run_finalization_receipt.py (built under the same
-  commission; cross-family review pending at this plan's authoring).
+  commission; review/adjudication state must be checked in that lane, not inferred here).
   EvidenceUnit: orca-harness/schemas/case_models.py:53-73 (UNCHANGED by this slice).
 branch_or_commit: ecr-sp3-timing-deriver-slice1 (re-verify citations at ratification time).
 stale_if:
@@ -37,12 +37,17 @@ stale_if:
 - **Status:** advisory design; **non-executing**. Recommends the binding composition
   for owner ratification. Designs the contract; the implementation (models +
   composer + tests) is post-ratification under the same bounded commission.
-- **Why this slice:** the conductor's JSG-01 row is `indeterminate_until_authored`
-  *in practice* for one remaining structural reason — the derivers, the SP-5 model +
-  consumer, and (now) the SP-5 producer exist, but **no composition object binds
-  their outputs onto a case packet's evidence unit**, so no case packet can carry
-  the derived fields + a valid `FinalizationReceipt`. This slice is that missing
-  composition object — and nothing else.
+- **Why this slice:** for the binding surface, the conductor's JSG-01 row is
+  `indeterminate_until_authored` *in practice* because the derivers, the SP-5
+  model + consumer, and (now) the SP-5 producer exist, but **no composition object
+  binds their outputs onto a case packet's evidence unit**, so no case packet can
+  carry the derived fields + a valid `FinalizationReceipt`. This slice is that
+  missing composition object — and nothing else. It is **not** the complete
+  unfreeze ledger: the frozen conductor row still names **D2** as deferred, while
+  the ratified boundary note says SP-6 can evaluate determinately and may
+  residualize without D2. Owner ratification / unfreeze routing must reconcile
+  that wording explicitly before anyone claims "only the owner's unfreeze word
+  remains."
 - **Frame inheritance:** uses the ratified ECR frame verbatim (INV-1..5; M1/M2/M3
   binding modes; D3 upstream-owned/carried; D4 bind-real-fields-coin-nothing) and
   the submap's cross-kind invariants (reference-never-merge; one-record-per-kind;
@@ -65,6 +70,10 @@ ratified schema):
 | 5 | finalization provenance + final value | `FinalizationReceipt` stream via the validate-only consumer | single current cross-family receipt ⇒ surfaces `final_pre_decision_status` (the conductor separately polices the *value*; SP-4 is not this slice) |
 
 Anything beyond these five reads routes to the owner memo, never into this build.
+This table is the **composer contract**, not a JSG-01 unfreeze ledger. In
+particular, D2 remains a reserved surface: the composer may carry an SP-6
+residual caused by absent D2, but it must not decide whether that residual is
+acceptable for unfreeze or silently rewrite the frozen conductor's D2 blocker.
 
 ## The binding contract (working names; canonical name reserved)
 
@@ -81,6 +90,13 @@ is a pure reference object. `Jsg01` in the working names marks the scope honestl
 the **canonical object name stays owner-reserved** — a later rename is cheap
 because everything downstream of the keys is re-derived, not migrated.
 
+The binding declaration is an **assembly-authored key assertion**, not a selector
+over the strongest posture. Assembly must bind the `evidence_slice_id` whose
+preserved bytes actually carry the evidence unit content; the composer only
+checks key coherence and carries the resulting reads. It must never search for a
+slice that clears SP-2/SP-3, infer content membership from posture quality, or
+repair a bad binding by choosing a sibling slice.
+
 **`compose_jsg01_evidence_record(...)` — the pure composer (M2 at composition grain):**
 
 ```text
@@ -97,7 +113,8 @@ compose_jsg01_evidence_record(
 - **Key guards (block, don't repair):** `packet.packet_id != binding.packet_id`,
   or `evidence_slice_id` naming no slice in the packet, raises a named
   `Jsg01BindingError`. A malformed binding is a visible block — never a residual,
-  never silently re-keyed.
+  never silently re-keyed. A low-quality or non-clearing bound slice is still
+  carried as the bound read; the composer does not promote a better sibling.
 - **Posture reads (carry verbatim):** calls the four built derivers fresh
   (`ecr/deriver.py`) — *re-derive, never migrate*. Carries the per-packet SP-1 and
   SP-6 postures, and the **full per-slice SP-2/SP-3 vectors** with
@@ -152,8 +169,9 @@ move without re-ratification as long as the binding keys and composer contract h
 - **INV-3 (no persisted derived field; no migration):** postures and the composed
   record are derived/re-derivable; only the binding keys and the receipts (records
   of acts) are durable. ✓
-- **INV-4 (recomputation basis upstream-owned, carried):** integrity anchors and
-  the binding hash stay owned by producer/SP-5 model; carried by reference. ✓
+- **INV-4 (recomputation basis upstream-owned, carried):** producer integrity
+  anchors stay producer-owned, and the SP-5 `binding_hash` stays receipt-owned;
+  the binding record only carries keys/reference, never re-authors either. ✓
 - **INV-5 (categorical handoff, not schema import):** binds real committed fields;
   defines no producer field; `EvidenceUnit` schema untouched. ✓
 - **Submap invariants:** reference-never-merge (keys, one-directional composition →
@@ -184,10 +202,12 @@ move without re-ratification as long as the binding keys and composer contract h
    stored field mirrors a derived condition; YAML round-trip under `extra="forbid"`).
 2. `evidence_binding/composer.py`: `compose_jsg01_evidence_record` + `Jsg01BindingError`.
 3. Tests (harness pattern): key-guard blocks; grain alignment (bound-slice selection
-   over full vectors); verbatim carry (postures equal the derivers' direct output;
-   finalization read equals the consumer's verdict); blocked-carry (no receipt ⇒
-   BLOCKED carried, nothing authored); purity/determinism; round-trip; **no
-   aggregate verdict field exists**.
+   over full vectors); no selector laundering (a failing bound slice remains the
+   bound read even when a sibling slice clears, and a clearing bound slice does
+   not hide failing siblings in the carried vector); verbatim carry (postures
+   equal the derivers' direct output; finalization read equals the consumer's
+   verdict); blocked-carry (no receipt ⇒ BLOCKED carried, nothing authored);
+   purity/determinism; round-trip; **no aggregate verdict field exists**.
 4. Cross-family code review per the established slice convention before landing.
 
 Validation gates: full pytest suite green; `test_no_llm_imports` untouched;
@@ -223,7 +243,11 @@ ratification: a dated amendment to
 (same shape as the SP-1/2/3+SP-6 ratification records — design basis with SHA256
 pins, owner decisions, reserved-list restated) carrying its own inline
 `direction_change_propagation` receipt (trigger: `architecture_doctrine`, related:
-`lifecycle_boundary`). Build starts only after the owner's word.
+`lifecycle_boundary`). That owner act must also state how the D2 wording in the
+frozen conductor row is consumed: either D2 remains a named blocker, or the owner
+explicitly records that the existing SP-6 residual/does-not-clear behavior is
+determinately evaluable for this unfreeze boundary. Build starts only after the
+owner's word.
 
 ## Non-claims
```

## Residual Risk

The patch keeps the plan at patch-level hardening. It does not resolve the
actual D2 policy question; it forces that question into the owner ratification /
unfreeze routing instead of letting this plan decide it implicitly.

## Off-Scope Flags

- No conductor edit was made; the conductor remains frozen.
- No boundary-doc amendment was made.
- No code, tests, runtime files, commits, staging, or pushes were performed.
- No sealed outcome facilitator-only artifact was opened.

## Review-Use Boundary

This report, verdict, citations, and diff are decision input only. They are not
approval, validation, mandatory remediation, owner ratification, lifecycle
completion, or a JSG-01 unfreeze. The home model adjudicates the diff before
anything is kept; the owner alone ratifies.

## Home-Model Adjudication (anthropic/claude-fable-5, 2026-06-12)

- **DRP-01 (D2/unfreeze boundary): ACCEPTED verbatim.** The composer-contract /
  unfreeze-ledger distinction and the requirement that the owner ratification or
  unfreeze act state how the frozen conductor row's D2 wording is consumed are
  correct hardening: they route a reserved question to the owner act (exactly
  where the slice-D memo must land it) and decide nothing reserved.
- **DRP-02 (anti-laundering guard): ACCEPTED verbatim.** The binding declaration
  as assembly-authored key assertion (never a strongest-posture selector), the
  no-sibling-promotion composer rule, and the two added test cases
  (failing-bound/clearing-sibling; clearing-bound/failing-sibling) close the
  laundering surface the commission asked the review to attack.
- **DRP-03 (state/citation metadata): ACCEPTED with one CA refresh.** The
  reviewer's `(unadjudicated)` status and adjudication-facing `use_when` bullet
  became stale at this adjudication; refreshed by the home model to
  `(adjudicated 2026-06-12: all reviewer changes kept)` and
  `Preparing the owner ratification ...`. The INV-4 ownership split is kept
  verbatim.
- **Kept state (post-adjudication SHA256):**
  `docs/product/ecr/ecr_consolidation_v0_jsg01_evidence_unit_binding_slice_plan_v0.md`:
  `FECCA1DFA0AFD8583A9B3B6FD138FED3937C70DD7D2584D5B34D0F5CABCB62E9`
- **Next authorized step:** OWNER RATIFICATION STOP — dated boundary-doc
  amendment + DCP receipt; the plan and this record land with that ratification
  per the established ECR pattern. Build starts only after the owner's word.
  JSG-01 stays FROZEN.
