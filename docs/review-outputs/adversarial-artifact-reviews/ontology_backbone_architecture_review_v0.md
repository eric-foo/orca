# Ontology Backbone Architecture - Delegated Adversarial Review v0

```yaml
retrieval_header_version: 1
artifact_role: Review output (delegated adversarial artifact review-and-patch)
scope: >
  Repo-mode cross-vendor delegated adversarial artifact review and bounded patch
  of docs/product/core_spine/orca_ontology_backbone_architecture_v0.md.
use_when:
  - Adjudicating the delegated hardening patch before keeping or rejecting it.
  - Checking which ontology-backbone architecture review findings were patched.
authority_boundary: decision_input_only
reviewed_by: openai-gpt-5-codex
authored_by: Anthropic Claude Opus 4.x
de_correlation_bar: cross_vendor_discovery
operating_contract: .agents/workflow-overlay/delegated-review-patch.md
source_prompt: docs/prompts/reviews/ontology_backbone_architecture_delegated_review_prompt_v0.md
target: docs/product/core_spine/orca_ontology_backbone_architecture_v0.md
target_original_sha256: 8e80e65441c316b466ab027c651fae0b5470de719a1d50186c7998ee001d0187
recommendation: patch_before_acceptance
```

## Review Summary

Status: `completed_repo_mode_patch_applied_uncommitted`.

Verdict: no `NEEDS_ARCHITECTURE_PASS`. The artifact has patch-level defects in
boundary encoding, not a design-level failure requiring a new architecture pass.
The patch should be CA-adjudicated before keep.

Patch scope respected: only
`docs/product/core_spine/orca_ontology_backbone_architecture_v0.md` was patched.
This report was written to the commissioned review-output path.

Non-claims: not validation, not readiness, not adoption, not owner acceptance,
not folder/router enactment, not a kept patch until CA adjudication.

## Source Context

SOURCE_CONTEXT_READY with targeted reads.

Source-read ledger:

| Source | Use | Status |
| --- | --- | --- |
| `AGENTS.md` supplied in current context | Orca kernel and smallest complete intervention | supplied |
| `.agents/workflow-overlay/README.md` | Overlay binding | read |
| `.agents/workflow-overlay/delegated-review-patch.md` | Repo-mode delegated review-and-patch authority | read |
| `.agents/workflow-overlay/review-lanes.md` | Review lane and severity/output boundaries | read |
| `.agents/workflow-overlay/prompt-orchestration.md` | Review-report output mode | read |
| `.agents/workflow-overlay/source-of-truth.md` | Source hierarchy and DCP boundary | read |
| `.agents/workflow-overlay/safety-rules.md` | Protected/off-scope edit boundary | read |
| `docs/prompts/reviews/ontology_backbone_architecture_delegated_review_prompt_v0.md` | Commission | read |
| `docs/product/core_spine/orca_ontology_backbone_architecture_v0.md` | Target | read and patched |
| `docs/product/product_lead/orca_demand_gate_definition_closures_proposal_v0.md` | G1/G2/G4, `derived_from`, `diverges_from` | targeted read |
| `docs/product/product_lead/orca_buyer_proof_packet_v0.md` | Hard Gate, buyer/org-motion proof constraints | targeted read |
| `docs/decisions/judgment_spine_backtest_batch1_ledger_declaration_v0.md` | Batch-local dev/holdout and non-claims | targeted read |
| `docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md` | Claim tiers and receipt-gated promotion | targeted read |
| `docs/product/core_spine/beauty_venue_card_set_v0.md` | Venue-card cap/kernel source | targeted read |
| `repo-structure.yaml`, `.agents/workflow-overlay/artifact-folders.md`, `docs/decisions/orca_repo_structure_binding_v0.md` | Layer-2 folder/router boundary | targeted read |

Preflight facts:

- Branch: `ontology-backbone-arch-pass-v0`.
- Start dirty-state command returned only the branch line, with no dirty entries.
- Target original SHA matched the prompt pin exactly.
- User explicitly authorized continuing through SHA/path blockers; the waiver was
  not needed for the target SHA, but one cited ledger path in the prompt/source
  context was corrected by lookup: the batch-1 ledger is under `docs/decisions/`,
  not `docs/product/judgment_spine/`.

## Findings

### AR-01 - Case row imports batch-local and receipt-gated concepts as intrinsic ontology dimensions

Severity: major.

Target anchor: §2.2 `Case` row.

Evidence in target: `Case` listed `claim_tier, split: dev|holdout, entry_basis`
as key states/dimensions.

Source evidence:

- `docs/decisions/judgment_spine_backtest_batch1_ledger_declaration_v0.md:33-35`
  says `BATCH1_ACTIVE_OWNER_SIGNED` is a batch-local label, not an
  evidence-ladder closeout state or claim tier.
- `docs/decisions/judgment_spine_backtest_batch1_ledger_declaration_v0.md:69-73`
  defines dev/holdout as batch-local vocabulary.
- `docs/decisions/judgment_spine_backtest_batch1_ledger_declaration_v0.md:213-217`
  says batch-1 is not validation/readiness/buyer proof/judgment-quality evidence
  and mints no ladder vocabulary.
- `docs/product/judgment_spine/judgment_spine_evidence_ladder_architecture_v0.md:236-249`
  makes claim tier a receipt/promotion outcome, not a type-intrinsic property.

Defense considered: a `Case` needs enough metadata to support backtest routing.
That defense holds only if the ontology maps to the ledger/evidence owners; it
fails when the row promotes batch-local fields into standing dimensions.

Patch applied: changed the `Case` row to `known_outcome; receipt-backed
claim-cap pointers only`, and explicitly kept `split` and `entry_basis` as
batch-ledger metadata.

Minimum closure condition: `Case` remains a domain object, while dev/holdout,
entry basis, and evidence strength are mapped to the batch ledger and evidence
ladder rather than minted as ontology state.

Next authorized action: CA adjudicates the patch.

### AR-02 - Load-bearing provenance links were underspecified at the exact failure edge

Severity: major.

Target anchor: §2.3 `derived_from` and `diverges_from`.

Evidence in target: `derived_from` stated transitive collapse, but not
cycle/multi-parent handling. `diverges_from` stated floor defeat, but not the
layer/coordination basis required to distinguish floor defeat from ceiling cap.

Source evidence:

- `docs/product/product_lead/orca_demand_gate_definition_closures_proposal_v0.md:65-73`
  requires no shared origination ancestry and says pairwise non-derivation is
  insufficient.
- `docs/product/product_lead/orca_buyer_proof_packet_v0.md:114-124` carries the
  same no-shared-origination rule into the Hard Gate.
- `docs/product/product_lead/orca_demand_gate_definition_closures_proposal_v0.md:91-100`
  and `docs/product/product_lead/orca_buyer_proof_packet_v0.md:142-150` say
  divergence defeats the floor only when the costly-behavior instance is likely
  manufactured/coordinated, e.g. in the same coordinated layer.

Defense considered: v0 is naming-normative/schema-light, so implementation
semantics can be deferred. That defense fails here because the commission itself
makes these two links load-bearing for independence and divergence; underspecifying
the failure edge would let future cards count laundered siblings or overapply a
floor defeater.

Patch applied: added cycle collapse, multi-parent union semantics, and a
required layer/coordination basis for G2 floor defeat.

Minimum closure condition: future card/schema work can apply the same
independence and divergence rules without inventing missing edge semantics.

Next authorized action: CA adjudicates the patch.

### AR-03 - Brand-as-WindCaller created a self-origin laundering path

Severity: major.

Target anchor: §2.2 `Brand`, §2.3 structural links.

Evidence in target: `Brand —can_act_as→ WindCaller` was allowed with no guard
against counting the brand's own move as independent demand for its own product
or decision.

Source evidence:

- `docs/product/product_lead/orca_buyer_proof_packet_v0.md:114-124` requires
  independence by origination so no single origin's bias or manipulation carries
  the answer.
- `docs/product/product_lead/orca_buyer_proof_packet_v0.md:126-134` requires
  enough independent origins for material commitment.
- `docs/product/product_lead/orca_buyer_proof_packet_v0.md:182-183` keeps
  org-motion as corroboration inside the artifact, not a G1 origin.

Defense considered: brand moves can legitimately be leading indicators. That is
true for calibration and early-warning reads, but it does not justify treating a
brand's own signal as independent demand for the same brand's product/decision.

Patch applied: added a self-origin guard: brand-originated observations/calls are
`self_originated` for that brand's own Product/DecisionEvent and excluded from G1
independent-origin counting.

Minimum closure condition: the ontology supports brand-as-WindCaller without
allowing self-laundered G1 independence.

Next authorized action: CA adjudicates the patch.

### AR-04 - Final cap/adoption language contradicted the updated roster state

Severity: minor.

Target anchor: §1 success signal, §2.2 roster intro, §7 invariants.

Evidence in target: the artifact now had 17 of 18 types, but the success signal
still said `<=~15` and the invariant still said "hard cap (15) holds." The roster
also did not clearly separate v0 naming authority from first-build readiness.

Source evidence:

- `docs/product/core_spine/beauty_venue_card_set_v0.md:27-29` is a 12-card
  instance cap with review dates and fail-soft cards, not direct authority for a
  15-type domain ontology cap.
- Target §6.1 already recorded the owner decision raising the cap from 15 to 18.
- Target §9 already stages the first build to the ID-canonicalization rule plus
  a few cards, not all 17 roster entries.

Defense considered: historical amendment text can retain the 15-cap narrative.
That holds for §6.1 history, but not for current success/invariant language.

Patch applied: changed the live success/invariant cap to 18 and added that the
roster is v0 naming authority, with build-readiness staged in §9.

Minimum closure condition: current cap language is internally consistent and
does not imply all named types are immediately build-ready.

Next authorized action: CA adjudicates the patch.

## Unified Diff

```diff
diff --git a/docs/product/core_spine/orca_ontology_backbone_architecture_v0.md b/docs/product/core_spine/orca_ontology_backbone_architecture_v0.md
index 4c96b1fb..43be5196 100644
--- a/docs/product/core_spine/orca_ontology_backbone_architecture_v0.md
+++ b/docs/product/core_spine/orca_ontology_backbone_architecture_v0.md
@@ -83,7 +83,7 @@ grammar, and (b) MAPS workflow concepts to their existing overlay owners (Layer
 **Success signal.**
 - *Core success.*
   - *Owner-observable:* owner reads this one doc and sees the full object roster
-    (<=~15), each with definition + stable-ID scheme + key states + governed
+    (<=18), each with definition + stable-ID scheme + key states + governed
     actions/gates + links + backing artifact, plus a Layer-2 pointer table - enough
     to adopt / amend / reject in one pass.
@@ -141,6 +141,10 @@ only via the backing map.
 
 ### 2.2 Object-type roster (17 of 18 types - cap raised to 18 on 2026-06-15; "19th in = one out")
 
+This roster is **v0 naming authority**, not a command to build all cards at once.
+Build-readiness is staged in §9: weak-backing and forward-consumer types may be
+reserved as names while their owning artifacts mature.
+
 Folds applied to stay under the cap (noted): **SubNiche -> Vertical** (self-parent
 link). **`Read` is an ACTION on the `TrendVector` object, not an object type**
@@ -152,7 +156,7 @@ verb (§2.5). Demand-state, action-ceiling, read-type, and claim-tier are
 | # | Type | One-line definition | Key states / dimensions | Backing artifact(s) |
 | --- | --- | --- | --- | --- |
 | 1 | **Vertical** | A demand domain at a level (vertical or sub-niche); sub-niches nest via self-parent. | level: vertical \| sub_niche | thesis, wedge |
-| 2 | **Brand** | A consumer brand (consumer-facing label); company/parent resolution via `Org`. A Brand can itself act as a `WindCaller` (its own moves precede the shift). | - | candidate-pool handoff |
+| 2 | **Brand** | A consumer brand (consumer-facing label); company/parent resolution via `Org`. A Brand can itself act as a `WindCaller` (its own moves precede the shift), but never as an independent demand-origin for its own product/decision. | - | candidate-pool handoff |
@@ -162,7 +166,7 @@ verb (§2.5). Demand-state, action-ceiling, read-type, and claim-tier are
 | 9 | **DecisionEvent** | The live brand-decision event the `Read` action serves (the monetization unit a Memo is produced for); a discovery scan evaluates *candidate* DecisionEvents (absorbs the former Slot). | trigger status, discovery_status: slot_open\|filled\|qualified | candidate pool, discovery brief |
 | 10 | **Reading** | The dated calibrated output of the `Read` action - Orca's call on a `TrendVector` for a `DecisionEvent`: an action ceiling (act/phase/narrow/hold/defend) + read_type, capped by integrity, bound by never-a-feed. The lightweight decision record; a `Memo` elaborates it for a qualified buyer decision. | read_type, action_ceiling, claim_tier | read outputs (gap - scan-spec forward consumer + memos) |
 | 11 | **Memo** | The Public-Signal Demand-Allocation Decision-Risk Memo for one qualified DecisionEvent (reasoning substrate + proof gate). | claim_tier; gate pass/cap/fail | buyer-proof packet |
-| 12 | **Case** | A backtest/proof case: a historical decision with known outcome. | claim_tier, split: dev\|holdout, entry_basis | batch-1 ledger declaration |
+| 12 | **Case** | A backtest/proof case: a historical decision with known outcome. | known_outcome; receipt-backed claim-cap pointers only. `split` and `entry_basis` are batch-ledger metadata, not standing ontology dimensions. | batch-1 ledger declaration |
@@ -191,13 +195,26 @@ read-machinery forward consumer depends on them - design them precisely):
   (independence by de-correlated origination) and the Demand-Substrate Hard Gate's
   independent-origin count. Directed, transitive for the collapse test (any shared
   upstream origination event = one family); pairwise "neither derives from the
-  other" is explicitly insufficient.
+  other" is explicitly insufficient. Cycles are invalid producer data; until
+  repaired, every node in the cycle collapses to one origination family. Multi-parent
+  derivation unions all upstream families, so any shared upstream family blocks
+  independent-origin counting.
 - **`Observation -diverges_from-> Observation`** - the cross-layer disagreement edge.
   The integrity / astroturf tell. Preserved as signal, never averaged away.
   Constrains the action ceiling; and where divergence indicates the costly-behavior
   instance is itself likely manufactured/coordinated, it can **defeat the floor**
   (G2), not merely cap the ceiling. Directed, non-collapsing (divergence is kept,
-  not resolved).
+  not resolved). It must carry the layer or coordination basis that makes the
+  disagreement meaningful: a G2 floor-defeater requires the costly-behavior instance
+  to sit inside the same coordinated layer that the divergence flags; otherwise
+  divergence constrains the ceiling only.
+
+Self-origin guard:
+- A `Brand -can_act_as-> WindCaller` link may support calibration or early-warning
+  reads, but observations/calls self-originated by that Brand are labeled
+  `self_originated` for that Brand's own Product/DecisionEvent and are excluded
+  from the G1 independent-origin count. They may corroborate or explain a move;
+  they cannot launder the brand's own signal into independent demand.
@@ -410,7 +427,7 @@ adversarial / grounding perspectives run locally; extraction delegated read-only
 3. `derived_from` = independence/laundering (collapse); `diverges_from` =
    divergence/integrity (preserve-as-signal, never average) - both load-bearing.
 4. `never_a_feed` is an action constraint, not a new gate.
-5. The hard cap (15) holds; growth is one-in-one-out by dated amendment.
+5. The hard cap (18) holds; growth is one-in-one-out by dated amendment.
```

## Residual Risk

- This review did not re-run the original full architecture source extraction or
  validate the ontology design. It targeted the commissioned review failures and
  patchable seams.
- `Product`, `WindCaller`, `Observation`, `Call`, and `Reading` still depend on
  forward consumers or weak backing. The patch clarifies naming-vs-build readiness;
  it does not create those backing artifacts.
- The first-build ID-canonicalization rule remains owner-decision work after
  adoption.

## DELEGATED_ARTIFACT_REVIEW_RETURN_FOR_HOME_MODEL

Here is the delegated artifact review result. Adjudicate it under the
delegated-review-patch return contract.

- Original commission: `docs/prompts/reviews/ontology_backbone_architecture_delegated_review_prompt_v0.md`.
- Reviewed artifact and bounded patch scope:
  `docs/product/core_spine/orca_ontology_backbone_architecture_v0.md` only.
- Findings and source evidence: AR-01 through AR-04 above.
- Proposed artifact patch: applied in the working tree; unified diff included above.
- Reviewer verdict: `patch_before_acceptance`; no `NEEDS_ARCHITECTURE_PASS`.
- Residual risk: source-targeted review only; no validation/readiness/adoption.
- Blockers/off-scope/not-proven:
  - no owner acceptance;
  - no validation;
  - no ontology adoption;
  - no folder/router enactment;
  - no patch kept until CA adjudication.

Review-use boundary: these findings and the diff are decision input only. They
are not approval, validation, mandatory remediation, or executor-ready authority
beyond the already-applied bounded patch awaiting CA adjudication.

## CA Adjudication (home model — Anthropic Claude Opus 4.x, 2026-06-15)

Adjudicated under the delegated-review-patch return contract: the diff, citations,
and verdicts are treated as **claims verified against source and the artifact's
intent**, not premises inherited. Because the author and CA share a vendor, each
finding was checked against the reviewer's cited ranges rather than CA priors.

Verification performed (cited ranges re-read in the worktree):

- **AR-01** — batch-1 ledger `:33-35`, `:69-73`, `:217` confirm `dev/holdout` and the
  status label are batch-local vocabulary that "mints no ladder vocabulary"; evidence
  ladder `:236-243` confirms `claim_tier` is a receipt-gated closeout outcome, not a
  type-intrinsic field. Citations hold.
- **AR-02** — closures `:65-73` confirm "no shared origination ancestry; pairwise
  non-derivation insufficient" (→ cycle-collapse + multi-parent-union is a faithful
  formalization); closures `:91-100` and buyer-proof `:142-150` confirm a G2 floor-defeater
  requires the costly instance inside the same coordinated layer. Citations hold.
- **AR-03** — buyer-proof `:114-124` (no single origin carries the answer) and `:182-188`
  (own-move / org-motion is corroboration, never a standalone G1 origin) confirm a brand's
  own move cannot be an independent origin for its own product. Citations hold.
- **AR-04** — deliverable §2.2 / §6.1:391 / §9 (cap already 18; build staged) and venue
  card set `:27` (12-card *instance* cap, not type authority) confirm the stale `≤15` / `(15)`
  live language was an internal inconsistency; the fix to 18 is correct.

Per-finding verdict: **AR-01 ACCEPT · AR-02 ACCEPT · AR-03 ACCEPT · AR-04 ACCEPT** (no
modification). Kept: the full bounded patch to the target (all six hunks). Reverted: none.
Modified: none. CA veto not exercised — every change is source-faithful, schema-light, and
restates existing closure-doc policy into ontology row/link semantics rather than minting
new policy. Recorded into the target's §6.1 dated-amendment log (2026-06-15); target status
updated to `PROPOSED_2026-06-15_XVENDOR_REVIEW_APPLIED_AWAITING_OWNER_ADJUDICATION`.

Residual (CA-noted, not patched — outside this commission's scope):

- `Memo` (`claim_tier; gate pass/cap/fail`) and `EvidenceUnit` (`claim_tier`) still carry
  `claim_tier` as a row state. Unlike Case's batch-local fields, these are defensible as a
  per-instance closeout/cap state, so left as-is; flag for the owner's adoption pass if a
  uniform "claim_tier is mapped, never type-intrinsic" rule is wanted.
- Weak-backing / forward-consumer types (`Product`, `WindCaller`, `Observation`, `Call`,
  `Reading`) remain naming-only until their owning artifacts land (esp. the in-flight scan-spec).
- The order-0 ID-canonicalization rule remains an owner decision, gating any card build.

Next authorized step: owner adjudication/adoption of the PROPOSED backbone and the order-0
ID-canonicalization decision. Nothing here adopts or enacts the ontology.
