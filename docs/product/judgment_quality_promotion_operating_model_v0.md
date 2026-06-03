# Judgment Quality Promotion Operating Model v0

```yaml
retrieval_header_version: 1
artifact_role: Product artifact
scope: Case-agnostic operating model (conductor) that sequences Judgment Spine gates JSG-01 through JSG-10 into a runnable, receipt-verified path, using mechanical gate predicates, a total fail/blocked transition function, an explicit by-hand isolation cap, and named run lifecycle states, without computing judgment quality and without restating gate semantics owned elsewhere.
use_when:
  - Running or planning a case through the Judgment Spine gates end to end.
  - Deciding which run lifecycle state a partial or held run is in.
  - Checking what a partially completed or by-hand run can and cannot claim.
  - Routing an agent from one gate to the next without inventing gate ownership.
authority_boundary: retrieval_only
no_authority_invariant: >
  This conductor sequences gates and verifies receipts. It does not authorize
  model execution, probe execution, scoring, fixture admission, or claim
  promotion, and it does not compute judgment quality, recognition verdicts, or
  scores. Those remain owned by the controlling sources, the deterministic
  scorer, the memorization-probe artifact, and human authorization gates.
open_next:
  - docs/product/judgment_spine_evidence_ladder_architecture_v0.md
  - docs/product/judgment_spine_gate_ownership_map_v0.md
  - docs/product/judgment_spine_reveal_calibration_owner_contract_v0.md
  - docs/research/judgment-spine/harness/v0_14/contestant_no_tools_execution_contract_v0.md
  - docs/research/judgment-spine/harness/v0_14/memorization_probe_protocol.md
  - .agents/workflow-overlay/product-proof.md
  - .agents/workflow-overlay/validation-gates.md
input_hashes:
  AGENTS.md: 5800D6EC863102DC680A6FDB91199337BC8CAC65A4C820FE3F94610B0AFA82A1
  .agents/workflow-overlay/README.md: 40E28238868A423CD43559C1BE5C312E088439E596ECE8AFD25E73835A62A27F
  .agents/workflow-overlay/source-of-truth.md: 7DFBF052A098C0AD77A5598BB6EA4738DA9AD6943D391852DC2E032A173182EF
  .agents/workflow-overlay/source-loading.md: 5CE8772563021F02968C76B9FE34D5E136459EFDF9DC92CF9F74077C59932560
  .agents/workflow-overlay/product-proof.md: AD1724202841D616F74494B22E3659D7987CC875BD36BF0F23B12C210E4B19C4
  .agents/workflow-overlay/validation-gates.md: FD7AE96F481733ED7FA5F1DDE252B7CF6A7C5A9053DAC7317795353F003F520F
  docs/product/judgment_spine_evidence_ladder_architecture_v0.md: 79F6696DD50BE3FDCB574FD6AED4FE0761C6335029BFDBE39B51F104F4AD16CF
  docs/product/judgment_spine_gate_ownership_map_v0.md: 83463329DC42816B5701E7692E5EFD484359AF9504CA3E36E3450C4C6122D5E3
  docs/product/judgment_spine_reveal_calibration_owner_contract_v0.md: ED146BEB5767EFDDA3E979AA798CA5CB044A896421872B02FBDF03615E4E6E07
  docs/research/judgment-spine/harness/v0_14/contestant_no_tools_execution_contract_v0.md: 3301224649991811D91B8B5932F0DFF18D3E356CB51979619BDBE3494BC9193C
  docs/research/judgment-spine/harness/v0_14/memorization_probe_protocol.md: 7862F03D0DA8DB6D845DF47FAA7940D89C2B27C8A27204C41744ECD3AC7B4C61
  docs/research/judgment-spine/harness/v0_14/packing_to_harness_foundation_interface_architecture_v3.md: 7291EF5E7C19A3514AE2B0E91D9FDD8917D7C4BFF039726FCD6075E55F73C1A4
  docs/research/judgment-spine/harness/v0_14/phase_1_infrastructure_architecture.md: 0459C21E7083CD9295290170692BE47A85CBCD24B42B9B0C6E9D7ACF29AC850A
  docs/research/judgment-spine/harness/v0_14/band_input_labeling_rubric.md: 0CE6E9584F4F1C4716559A654870AF43EBED3E5D53D3279AB658993B7DE1C2AE
  docs/workflows/orca_repo_map_v0.md: BF5559164431C98C1C6A1DB614B854A99E70FF2C0E63E33D26DDDA5AD3E6802E
  orca-harness/scoring/band_scorer.py: D54DCD2CB34A8158232E1A428F70A1F3F182052529D7BC8E5293D5F21A67E1E3
  orca-harness/runners/run_case.py: F04BABF1EF4BAFE187E83552E3A3066DEBC47CAD92F5186011BD7B2925CE52AD
branch_or_commit: main @ dd2d06553b4412416b1e37a28b2faaf2b7683d33
input_hash_baseline_note: >
  The worktree was heavily dirty when these hashes were computed. Several
  controlling product docs are untracked and several overlay files are
  modified. These input_hashes pin the current worktree bytes, not a clean
  committed baseline. Recompute before any strict reliance.
downstream_consumers:
  - .agents/workflow-overlay/source-loading.md
  - docs/workflows/orca_repo_map_v0.md
  - docs/research/judgment-spine/manifest_v0.md
  - docs/product/judgment_spine_gate_ownership_map_v0.md
  - future Judgment Spine case runs and case run-state records
stale_if:
  - docs/product/judgment_spine_evidence_ladder_architecture_v0.md changes claim tiers, closeout states, weakest-cleared-gate rule, sub-floor rule, or receipt minima.
  - docs/product/judgment_spine_gate_ownership_map_v0.md changes gate ownership, required receipts, or gate dependencies.
  - docs/product/judgment_spine_reveal_calibration_owner_contract_v0.md changes JSG-08 satisfaction states or claim caps.
  - docs/research/judgment-spine/harness/v0_14/contestant_no_tools_execution_contract_v0.md changes isolation or sealed-output gate semantics.
  - docs/research/judgment-spine/harness/v0_14/memorization_probe_protocol.md changes probe gate interpretation semantics.
  - A later accepted contestant-execution runner, scoring route, or operating-model artifact supersedes this conductor.
```

## Current Task Receipt

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom_judgment_quality_conductor
  edit_permission: docs-write
  target_scope:
    - docs/product/judgment_quality_promotion_operating_model_v0.md
    - .agents/workflow-overlay/source-loading.md
    - docs/workflows/orca_repo_map_v0.md
    - docs/research/judgment-spine/manifest_v0.md
    - docs/product/judgment_spine_gate_ownership_map_v0.md
  dirty_state_checked: yes
  blocked_if_missing: no
  path_collision_checked:
    path: docs/product/judgment_quality_promotion_operating_model_v0.md
    existed_before_write: no
  dirty_or_untracked_notes:
    - The conductor target was absent before this write (owner-deferred until now).
    - Controlling product docs and several overlay files are untracked or modified in this worktree; input_hashes pin current worktree bytes.
```

## Purpose

This artifact is the Judgment Spine **conductor**: the connective tissue that
sequences the owned gates `JSG-01` through `JSG-10` into a path a future agent
can actually walk a case through. The gate semantics, claim vocabulary, and
receipt minima already exist in the evidence ladder, the gate ownership map, the
`JSG-08` owner contract, and the harness contracts. What did not exist was the
operating model that orders those gates, checks each gate's receipt, and routes
between them. This conductor supplies exactly that and nothing more.

It re-opens the owner-deferred operating-model spine. It holds the full Judgment
Spine discipline at minimal footprint by **routing to** the owner sources rather
than restating them. It assembles and verifies receipts; it never computes
judgment quality.

## No-Authority Invariant

The conductor, and any LLM acting as conductor, is supporting cast. It is the
subject or the assistant. It is never the gavel.

```yaml
no_authority_invariant:
  conductor_may_only:
    - evaluate a mechanical predicate over an existing receipt field
    - advance, halt, or hold per the transition function
    - record the resulting run lifecycle state and route to the next gate owner
  conductor_must_never:
    - compute judgment quality
    - decide a memorization recognition verdict
    - compute, revise, or repair a score
    - author a missing gate receipt to escape a halt
    - mint, rename, merge, or split any claim tier or closeout_state
    - authorize a model run, probe run, scoring, fixture admission, or promotion
  authority_owners:
    memorization_recognition_verdict: read from the JSG-05 probe artifact (memorization_probe_protocol)
    score: read from the deterministic scorer output (phase_1_infrastructure / band_scorer)
    gate_semantics_and_ownership: gate ownership map and each gate's owner contract
    claim_caps_and_closeout_vocabulary: evidence ladder
    run_fixture_promotion_authorization: human / owner gate
```

This is **Invariant A**. A run that requires the conductor to exercise judgment
to clear a gate has not cleared that gate.

## Route, Don't Restate

This is **Invariant B**. The conductor owns only routing and lifecycle
constructs: the gate sequence, the predicate-binding rule, the transition
function, the by-hand cap rule, and the run lifecycle states. It owns no gate
semantics and no claim vocabulary. Every predicate checks an owner-produced
receipt field; the conductor cites the owner source and never duplicates or
contradicts it. If this conductor and a controlling source disagree, the
controlling source wins and this conductor is stale for that point.

## Isolation Topology

```yaml
isolation_topology:
  orchestrator_thread:
    role: reads sources, evaluates predicates, sequences gates, records run state
    authority: none
  isolated_child_runs:
    - gate: JSG-05 memorization probe
      isolation_owner: memorization_probe_protocol + contestant_no_tools_execution_contract
    - gate: JSG-06 contestant blind judgment
      isolation_owner: contestant_no_tools_execution_contract
    rule: child runs must be isolated from orchestrator context; the orchestrator must not leak packet, ledger, or outcome material into them
  deterministic_scorer:
    gate: JSG-07
    owner: phase_1_infrastructure_architecture / band_scorer
    rule: code computes the score; the conductor reads it
  human_authorization_gates:
    - run authorization
    - fixture admission
    - claim promotion
    rule: owner decides; the conductor never self-authorizes
```

The conductor coordinates these roles. It never collapses any of them into
itself.

## Gate Sequence And Mechanical Predicate Table

**Seam 1 — predicate-binding rule.** Every gate's clear-condition is expressed
as **either** (a) an exact source-owned receipt field path and an allowed value,
**or** (b) a read of an owner-produced status field. A gate is `cleared` only
when the named field exists and equals an allowed value; this is evaluable
without judgment. A semantically loaded concept (for example "valid source
identity") is **not** clearable by the conductor unless the controlling owner
source defines the exact field that carries it. Where the owner source does not
yet name a checkable field or value, the gate predicate is
`indeterminate_until_authored`: the conductor treats the gate as **not cleared**,
halts, and names the missing owner-schema field as the blocker. The conductor
never clears on a paraphrase and never invents a field.

**Receipt-provenance sub-rule (non-self-certification).** This applies the
Orca-general **Receipt-field provenance gate**
(`.agents/workflow-overlay/validation-gates.md`), which is the single source of
the principle: a receipt field is gate-clearing only when owner-produced and
provenance-bound or independently verifiable, never on a self-asserted value;
absent that, the check is `indeterminate_until_authored`. Conductor-specific
application: for the machine- or run-produced gates (JSG-04, JSG-05, JSG-06,
JSG-07), the predicate must check the provenance the owner contract requires (for
example, `contestant_no_tools_execution_contract_v0.md` Receipt Provenance
Boundary) — an owner-produced authorized status that binds provenance, or the
explicit auditable provenance fields — not the bare `proven`/`pass_valid` field.
Where that provenance is not yet producible (for example, no
contestant-execution runner exists), the predicate is
`indeterminate_until_authored` / not cleared, which caps the run per Seam 3.

This rule is what makes Seam 1 mechanical and what keeps Invariant A and
Invariant B intact.

| Gate | Routed semantics owner | Receipt | Mechanical clear-predicate | If owner field/schema absent |
| --- | --- | --- | --- | --- |
| JSG-01 | data-capture obligation contract + core-spine boundary own the source-identity obligation; packing interface owns `pre_decision_status`; no ECR field-schema owner yet | packing final status + ECR source-identity receipt | `pre_decision_status` present and set to an allowed *cleared* pre-decision value (not `excluded` or an uncertain/placeholder value). The finalization-provenance subpredicate — that the final `pre_decision_status` was finalized by the Judgment authority (AR-01), which the owner names as a block-state when unmet and leaves an open, unstaffed owner decision — is `indeterminate_until_authored`: no owner field yet records Judgment-authority finalization, so bare presence does **not** clear. The source-identity, inspectability, and timing/cutoff subpredicates are likewise `indeterminate_until_authored`: the obligation contract explicitly does not define ECR fields/keys/schema, and no ECR field schema exists yet, so there is no checkable owner field to bind for the source-side obligations | `indeterminate_until_authored` until an ECR field schema names the exact source-identity, inspectability, and timing/cutoff fields and allowed values |
| JSG-02 | evidence ladder + packing interface | frozen participant packet | `participant_packet_hash` present and non-empty **and** the packing admission carries no leakage/spoiler block-class failure for the zero-spoiler participant-visible boundary (no `outcome_leakage_class` in participant-facing content, no source identifiers/provenance in the contestant-visible manifest, leakage/spoiler receipt present — owner hard-marker checks; "structure is not admission"). A bare present hash does **not** clear on its own. A recorded leakage/spoiler block-class failure routes to contaminated/blocked (Leakage) | semantic-leakage subpredicate is `indeterminate_until_authored` (owner leaves it to operator/review) until its admission fields are authored |
| JSG-03 | band-input labeling rubric + packing interface | frozen FacilitatorLedger | `ledger_freeze_hash` and `committed_at` present and valid **and** the owner-required ledger contents present (authors, version pins, enum-valid band inputs, and the `second_label_diffs` disagreement trail). A bare present `ledger_freeze_hash` with any required ledger field missing/invalid does **not** clear; a met rubric-quarantine trigger routes to not-cleared/quarantine | `indeterminate_until_authored` for any required ledger field whose schema is not yet authored |
| JSG-04 | contestant no-tools execution contract | `contestant_execution_isolation` + authorized live-execution provenance | `isolation_result == "proven"` **and** the contract's auditable live-execution provenance is bound (separate owner authorization; production by the live runner; accepted endpoint; out-of-band operator record binding provider, endpoint, UTC timestamp, exit status, console output, `prompt_hash`, `raw_response_hash`). A bare computed `proven` does **not** clear (receipt-provenance sub-rule) | not cleared; with no live runner, by-hand receipts cannot bind provenance, so `indeterminate_until_authored` / capped per Seam 3 |
| JSG-05 | memorization probe protocol + no-tools contract provenance boundary | probe artifact | gate-interpretation `== pass_valid`, **read from the JSG-05 artifact, not the scorer**, **and** bound by the same auditable live-execution provenance as JSG-04. A bare computed `pass_valid` does **not** clear (receipt-provenance sub-rule) | not cleared / `indeterminate_until_authored` until authorized live provenance is bound; a `probe_result == fail` (confirmed recognition) routes to contaminated/blocked via the Seam 2 contamination branch, while `ambiguous` quarantines as not-cleared |
| JSG-06 | no-tools contract blind-judgment section (isolation) + ladder; sealed-output field currently unowned | sealed blind judgment | `isolation_result == "proven"` for the blind-judgment run **and** JSG-04 cleared (so it inherits JSG-04's auditable live-execution provenance). The sealed-output subpredicate is `indeterminate_until_authored`: no JSG-06 owner (the BlindJudgement schema or the no-tools contract) names a checkable `sealed_blind_judgment_hash` field, so there is nothing to bind. `sealed_before_reveal` is a **JSG-08** receipt field, not a JSG-06 clear-condition; the seal-before-reveal property is enforced at JSG-08, where `sealed_before_reveal == no` routes to `blocked_or_contaminated` | not cleared / `indeterminate_until_authored` until a JSG-06 sealed-output field schema names the field and allowed value |
| JSG-07 | phase-1 infrastructure + packing interface | scoring result | version/hash fields present (`scorer_version`, `mapping_table_version`, `labeling_rubric_version`, required frozen-input hashes) **and** authenticity bound to the deterministic scorer's owner-produced provenance. Because scoring is deterministic, that authenticity binding is an owner-authorized **re-derivation match** (owner-authorized verification, not a conductor-computed score): the recorded `scoring_result_hash` equals re-running the scorer over the frozen inputs. A hand-authored result carrying the version fields does **not** clear (receipt-provenance sub-rule). The scoring-integrity-**contamination** subpredicate is `indeterminate_until_authored`: the owner's `score_blocked` is a mixed admission state firing mostly on absences (missing run-metadata/hash/version, `decision_shape` not frozen), with no field that cleanly discriminates an affirmative integrity failure from an absence, so a bare `score_blocked`, a re-derivation mismatch, or an absent result routes to **not-cleared** (Seam 3), not to contamination, until the scorer authors a discriminating integrity-failure signal | authenticity subpredicate is `indeterminate_until_authored` until a scorer-owned provenance/status field or the owner-authorized re-derivation check is authorized; scoring-integrity contamination is likewise `indeterminate_until_authored` |
| JSG-08 | reveal/calibration owner contract | `jsg_08_reveal_calibration_receipt` | `receipt_status == score_linked_outcome_calibration` **and** `sealed_blind_output.sealed_before_reveal == yes` (both JSG-08-owned receipt fields; the seal-ordering read lives here, where the field lives) for judgment-quality strength. `sealed_before_reveal == no` is an affirmative seal-ordering breach — the auditable signal of the owner contract's "relied on unsealed output" condition — and routes to contaminated/blocked; `unknown`, or a weaker `receipt_status`, caps lower / not cleared per the contract | not cleared at judgment-quality strength |
| JSG-09 | evidence ladder `judgment_spine_claim_classification` + validation gate | classification record | record present with `source_quality_state`, `execution_quality_state`, `closeout_state`, `claim_cap`, `weakest_missing_or_failed_gate`, `receipt_artifact_or_gap`, `non_claims` | terminal route (Seam 5) |
| JSG-10 | evidence ladder closeout vocabulary + validation gate | named closeout | `closeout_state` present, drawn from the ladder vocabulary, consistent with the weakest cleared gate | terminal route (Seam 5) |

Note on JSG-05 versus JSG-07: the deterministic scorer emits
`memorization_probe_result="not_run"` as a fixed field; the conductor must read
the recognition verdict from the **JSG-05 probe artifact**, never from the
scorer output. A present scoring result does not imply a cleared probe.

## Transition Function

**Seam 2 — total fail/blocked transitions.** The conductor evaluates gates in
order. The transition function is total over the full outcome alphabet: every
gate, including the closeout gates, has exactly one defined behavior for each
outcome — cleared, contaminated-or-blocked, held (JSG-08 pending-outcome only),
or not-cleared/indeterminate — evaluated in that precedence order.

```yaml
transition_function:
  evaluate_in_order: [JSG-01, JSG-02, JSG-03, JSG-04, JSG-05, JSG-06, JSG-07, JSG-08, JSG-09, JSG-10]
  outcome_precedence: [cleared, contaminated_or_blocked, held, not_cleared_or_indeterminate]
  on_gate_G:  # classify the gate outcome into exactly one branch, in the precedence order above
    if_cleared: advance to the next gate
    elif_contaminated_or_blocked:
      trigger: a gate's owner receipt reports an AFFIRMATIVE invalidity or breach value — JSG-08 `receipt_status == contaminated_or_invalid` (reveal/calibration/scoring entered the wrong lane, relied on unsealed output, used an undeclared biased frame, or cannot identify the revealed material) or `sealed_before_reveal == no` (seal-ordering breach); `isolation_result == violated` (tool-use breach or runtime context leakage); a JSG-02/JSG-03 packing leakage/spoiler block-class failure (an `outcome_leakage_class` in participant-facing content, or source identifiers/provenance in the contestant-visible manifest); or JSG-05 `probe_result == fail` (gate-interpretation `fail_gate_closing` / `fail_gate_closing_with_caveat` — the model affirmatively recognized the case, i.e. post-cutoff contamination, `severity: blocking` per the probe protocol). It fires only on a positive owner-reported invalidity value
      note: this must be an affirmative owner-reported invalidity value, so the routing decision stays a mechanical field read (Invariant A). Absence, not-yet-authored provenance, or unresolved status — `isolation_result == not_proven`, an `indeterminate_until_authored` subpredicate, a by-hand gate with no auditable runner, `sealed_before_reveal == unknown`, or a JSG-05 `probe_result == ambiguous` (quarantine pending operator review or clean rerun, `severity: material`, not a confirmed recognition) — is NOT contamination; it routes to else_not_cleared_or_indeterminate and caps per Seam 3 / the weakest-cleared-gate rule, NOT at "often none". Contamination can poison gates that already mechanically cleared, so it must NOT use the weakest-cleared-gate cap
      action:
        - halt at G; do not advance
        - resolve the closeout to the ladder closeout_state blocked_or_contaminated; cap = weakest UNAFFECTED gate, often none (ladder blocked_or_contaminated rule, not the weakest-cleared-gate rule)
        - name the affected or contaminated gate(s)
        - record via JSG-09 then JSG-10 at that cap, or the terminal route below if G is itself JSG-09 or JSG-10
    elif_held:
      trigger: G is JSG-08 AND the case is a live post-cutoff case whose real-world outcome has not occurred, so JSG-08 cannot yet clear
      action: enter run state sealed_awaiting_outcome (see Run Lifecycle States); this is a hold, not a failure and not a closeout
    else_not_cleared_or_indeterminate:
      - halt at G; do not advance
      - cap the claim at the weakest cleared gate (evidence ladder weakest-cleared-gate rule and sub-floor rule)
      - name the failed, missing, or indeterminate gate G
      - record the closeout via JSG-09 then JSG-10 at that cap
      - EXCEPTION: if G is itself JSG-09 or JSG-10, use the closeout self-dependency terminal route below
```

**Ladder reconciliation (Route, Don't Restate).** The evidence ladder's
`blocked_or_contaminated` use_when names six defects; this conductor maps each to
an affirmative owner value, never to a mere absence: **leakage** → a JSG-02/JSG-03
packing leakage/spoiler block-class failure; **post-cutoff contamination** →
JSG-05 `probe_result == fail`; **tool-use breach** → `isolation_result ==
violated`; **unreconciled scoring failure** → `indeterminate_until_authored` (the owner's
`score_blocked` is a mixed absence/defect admission state with no clean
integrity-vs-absence discriminator, so bare `score_blocked` is treated as absence
→ not-cleared until the scorer authors a discriminating signal); **missing isolation / missing source
identity** → read as an **affirmative defect that breaks an evaluated gate**
(`isolation_result == violated`, or an owner-set `receipt_status ==
contaminated_or_invalid`), consistent with the ladder's own "...breaks the
evaluated gate" framing. Not-yet-authored absence — `not_proven`, a by-hand gate
with no runner, an `indeterminate_until_authored` subpredicate — is an evidence
gap, not a broken gate, so it routes to not-cleared and the by-hand
product-learning cap (Seam 3), not to `blocked_or_contaminated`. This is a
reading the ladder permits, not an override; if the ladder later distinguishes
these explicitly, this conductor tracks it and is stale for that point until
updated.

**Seam 5 — closeout self-dependency terminal route.** When the halting gate is
`JSG-09` or `JSG-10` — the closeout machinery itself is the missing or invalid
receipt — the conductor must not "close out via JSG-09/10," which would be
circular. It enters the terminal run state `halted_no_completed_closeout`:

```yaml
halted_no_completed_closeout:
  trigger: JSG-09 or JSG-10 is the missing or invalid gate
  conductor_must:
    - make no completed-closeout claim
    - name the missing or invalid classification or closeout artifact as the blocker
    - record the weakest cleared gate among JSG-01 through JSG-08 for context
    - resolve the closeout claim itself to the ladder sub-floor: no_durable_evidence
  conductor_must_not:
    - author the missing classification or closeout receipt to escape the halt
    - invent a closeout_state
```

The closeout claim resolves to `no_durable_evidence` because the closeout
receipt has no durable evidence of its own; this is the ladder sub-floor rule
applied to the closeout artifact.

## By-Hand Isolation Cap

**Seam 3 — by-hand cap.** A gate step is "by-hand" when it is performed manually
by a person or an agent thread without an auditable runner receipt that proves
the property. The contrast is a code runner that emits an audit-grade receipt.

```yaml
by_hand_isolation_cap:
  affected_gates: [JSG-04, JSG-05, JSG-06]
  mechanism: >
    By-hand execution cannot bind the authorized, auditable live-execution
    provenance the no-tools contract requires; a hand-typed
    isolation_result == "proven" or gate_interpretation == "pass_valid" field is
    not self-certifying and is not gate-clearing (receipt-provenance sub-rule and
    the no-tools contract Receipt Provenance Boundary). JSG-04 therefore does not
    clear, JSG-05 cannot clear on a by-hand probe receipt, and JSG-06 (which
    depends on JSG-04) does not clear, at judgment-quality strength.
  claim_cap: no stronger than product-learning
  realized_closeout_state_is_one_of:
    - no_durable_evidence
    - unreceipted_product_learning_context
    - completed_product_learning_evidence
  realized_state_rule: >
    Selected per the actual product-learning-receipt completeness under the
    evidence ladder. By-hand does NOT automatically grant
    completed_product_learning_evidence.
  current_harness_reality:
    - There is no contestant-execution runner.
    - band_scorer hardcodes memorization_probe_result="not_run".
    - run_case scores a pre-supplied blind_judgement.yaml; it does not execute a contestant.
    - Therefore the first run loop is by-hand and caps at product-learning by this rule. The runner that would lift the cap is deferred.
```

## Run Lifecycle States

**Seam 4 — named run states.** These are operating-model run-state labels, not
new ladder tiers. Each resolves to an existing ladder closeout_state or claim
cap. The conductor mints no new claim vocabulary.

| Run state | Meaning | Ladder resolution |
| --- | --- | --- |
| `not_started` | no gate evaluated | none |
| `in_progress_at_<gate>` | gates before `<gate>` cleared; evaluating `<gate>` | cap = weakest cleared gate |
| `sealed` | JSG-06 cleared per its full gate-table predicate — note its sealed-output subpredicate is currently `indeterminate_until_authored`, so this state is not yet reachable; a by-hand run also cannot reach it, because by-hand JSG-04 does not clear and the run halts there | cap = weakest cleared gate |
| `scored` | JSG-07 cleared | cap = weakest cleared gate |
| `sealed_awaiting_outcome` | a post-cutoff live case is cleanly sealed and possibly scored, but the real-world outcome has not occurred, so JSG-08 cannot clear; the run is **held, not failed** | JSG-08 `receipt_status = absent`; reveal/calibration claim = `no_durable_evidence`; overall cap = weakest cleared gate; caps **below** `completed_judgment_quality_evidence` |
| `calibrated` | JSG-08 cleared at the required status | cap per the JSG-08 contract status |
| `closed` | JSG-09 classification and JSG-10 closeout recorded | the recorded `closeout_state` |
| `halted_at_<gate>` | a non-closeout gate failed or is indeterminate (ordinary not-cleared, no contamination) | cap = weakest cleared gate; closeout via JSG-09/10 |
| `blocked_or_contaminated` | a gate's owner receipt reports an affirmative invalidity/breach value (JSG-08 `contaminated_or_invalid` or `sealed_before_reveal == no`; `isolation_result == violated`; a JSG-02/JSG-03 packing leakage/spoiler block-class failure; or JSG-05 `probe_result == fail`, a confirmed recognition) — NOT mere absence, a by-hand/indeterminate gate, or a JSG-05 `ambiguous` quarantine, which are `halted_at_<gate>` | closeout_state = `blocked_or_contaminated`; cap = weakest UNAFFECTED gate, often none; name the affected gate |
| `halted_no_completed_closeout` | JSG-09 or JSG-10 itself failed (Seam 5) | closeout claim = `no_durable_evidence` |

`sealed_awaiting_outcome` exit rule: when the real-world outcome arrives, route
to a **JSG-08 attempt**, which resolves to one of the JSG-08 owner-contract
satisfaction states (`absent`, `reveal_readout_only`,
`qualitative_outcome_calibration`, `score_linked_outcome_calibration`, or
`contaminated_or_invalid`). Only `score_linked_outcome_calibration` clears at
judgment-quality strength; weaker statuses cap lower, and `contaminated_or_invalid`
routes through the contaminated/blocked branch. It never mints a new tier.

## Case-Selection Posture

```yaml
case_selection_posture:
  prefer: post-cutoff-first
  post_cutoff_first_means: the decision AND the outcome both fall after the model's training cutoff, giving both non-recognition and a real ground-truth outcome
  probe: JSG-05 memorization probe is mandatory and is the verifier of non-recognition; it is never skipped
  anonymization: probe-verified secondary only; renaming or perturbing a famous case risks hidden re-identification and severs ground-truth anchoring, so it is never assumed
  live_case_note: a post-cutoff live case naturally passes through sealed_awaiting_outcome until its outcome lands
  superseded_first_targets: famous pre-cutoff cases (for example a 2022 event) are poor FIRST judgment-quality targets
```

## How To Run A Case

1. **Authorization (human gate).** The owner authorizes the run. The conductor
   does not self-authorize.
2. **Select the case** per the post-cutoff-first posture; record source identity
   (JSG-01 inputs).
3. **Walk gates JSG-01 through JSG-10 in order.** At each gate, read the named
   receipt and evaluate the mechanical predicate (Seam 1).
4. **On clear, advance. On not-cleared or indeterminate, apply the transition
   function** (Seam 2), or the terminal route (Seam 5) if the halting gate is
   JSG-09 or JSG-10.
5. **Mark the execution mode.** If JSG-04, JSG-05, or JSG-06 ran by-hand, apply
   the by-hand cap (Seam 3).
6. **For a live post-cutoff case with no outcome yet,** record
   `sealed_awaiting_outcome` and hold; revisit JSG-08 when the outcome lands.
7. **Record JSG-09 classification and JSG-10 closeout** at the achieved cap, or
   `halted_no_completed_closeout` per Seam 5.

Existing harness components and their gate roles (plumbing only, not judgment
quality): `orca-harness/runners/run_case.py` scores a supplied blind judgment
(JSG-07 plumbing); `orca-harness/scoring/band_scorer.py` is the deterministic
scorer (JSG-07; note `memorization_probe_result` is hardcoded `not_run`);
`run_memorization_probe` handlers serve JSG-05. No contestant-execution runner
exists, so JSG-04, JSG-05, and JSG-06 are by-hand for now.

## Scaling Rule

Because the conductor routes rather than restates, it absorbs change without
drift:

- **Gate added:** add one predicate row (binding rule applies: exact field/value
  or `indeterminate_until_authored`), one transition entry, and a citation to
  the new owner source. No semantics are duplicated.
- **Gate closed or re-owned:** its predicate becomes a read of the
  owner-produced status field; the conductor changes the citation, not the
  meaning.
- **Owner semantics change:** the predicate auto-tracks because it only checks
  owner-produced fields; update `input_hashes` and `stale_if`.
- **Contestant-execution runner introduced (deferred):** the by-hand cap lifts
  for JSG-04/05/06 once an authorized runner emits the auditable live-execution
  provenance those gates require; the cap rule itself does not change, only which
  execution mode is in force.

This is why the footprint stays minimal: the conductor never holds gate meaning,
only the sequence, the predicates, the transitions, the lifecycle states, and
the by-hand cap.

## Connective-Tissue Wiring

So that every agent is routed here rather than reinventing a path, this
conductor is registered in:

- `.agents/workflow-overlay/source-loading.md` (Judgment Spine read pack);
- `docs/workflows/orca_repo_map_v0.md` (navigation);
- `docs/research/judgment-spine/manifest_v0.md` (Judgment Spine manifest);
- `docs/product/judgment_spine_gate_ownership_map_v0.md` (`downstream_consumers`).

These registrations are applied in the same pass as this artifact; see
`controlling_sources_updated` in the propagation block.

## Non-Claims

- This conductor does not validate Judgment Spine.
- This conductor does not create judgment-quality evidence; existing and
  surviving an adversarial review does not make it a clean run or proof.
- This conductor is the **path** toward judgment-quality evidence, not proof of
  it.
- This conductor does not authorize model execution, probe execution, scoring,
  fixture admission, or claim promotion.
- This conductor does not compute judgment quality, recognition verdicts, or
  scores; it reads them from their owners.
- This conductor does not create, rename, merge, or split any claim tier or
  closeout_state.
- By-hand runs cap at product-learning and cannot reach completed
  judgment-quality evidence.
- This conductor does not authorize implementation, runtime design, tests,
  deployment, commits, pushes, or PRs.

## Direction Change Propagation

```yaml
direction_change_propagation:
  doctrine_changed: >
    The owner-deferred Judgment Spine operating-model spine is re-opened. A
    case-agnostic conductor now sequences JSG-01 through JSG-10 with mechanical
    receipt predicates (including a receipt-provenance non-self-certification
    rule), a total fail/blocked transition function including a
    closeout self-dependency terminal route, an explicit by-hand isolation cap,
    and named run lifecycle states including sealed_awaiting_outcome. All of
    these are routing and lifecycle constructs that resolve to existing ladder
    vocabulary; no new claim tier or closeout_state is minted. Round-3 review
    patch (2026-06-03): the transition function is made total over a four-value
    outcome alphabet — cleared, contaminated_or_blocked, held, and
    not_cleared/indeterminate — with explicit precedence; a contaminated/blocked
    outcome now routes to the existing ladder closeout_state blocked_or_contaminated
    (cap = weakest unaffected gate, often none) instead of being mis-routed to the
    weakest-cleared-gate cap; the JSG-08 pending-outcome hold is folded in as a
    precedence-ordered branch so it is no longer doubly-defined against the
    not-cleared branch; JSG-06's predicate is re-bound to its own owner field
    (isolation_result proven) with the sealed-output subpredicate marked
    indeterminate_until_authored and the JSG-08-owned sealed_before_reveal field
    removed from it; and JSG-06's inherited-provenance dependency on JSG-04 is
    stated explicitly. blocked_or_contaminated already exists in the evidence
    ladder, so still no new claim tier or closeout_state is minted. The same
    pass also made the sealed lifecycle row's predicate explicit (with a
    by-hand-cannot-reach note), enumerated the five JSG-08 satisfaction states in
    the sealed_awaiting_outcome exit rule, and added a JSG-06->JSG-04 dependency
    line to the gate ownership map to make explicit a dependency the conductor
    already encoded — a co-pass alignment, not a superseding gate-dependency
    change, so it does not by itself make this conductor stale. Round-5 review
    patch (2026-06-03): the contaminated/blocked branch is narrowed to fire only
    on an affirmative owner-reported invalidity value (JSG-08
    contaminated_or_invalid, isolation_result == violated, or sealed_before_reveal
    == no), never on absence or a by-hand/indeterminate gate — those route to
    not-cleared and cap per Seam 3, which preserves the by-hand product-learning
    cap and keeps the branch a mechanical field read (Invariant A); and the
    seal-before-reveal ordering check is relocated into the JSG-08 predicate as a
    read of its own sealed_before_reveal field (it had been removed from JSG-06
    but not yet landed at JSG-08). Round-7 review patch (2026-06-03): the
    contaminated/blocked enumeration is completed against the owner sources — a
    confirmed JSG-05 memorization recognition (`probe_result == fail`,
    gate-interpretation fail_gate_closing / fail_gate_closing_with_caveat,
    severity blocking) now routes to blocked_or_contaminated, while a JSG-05
    ambiguous quarantine and all not-yet-authored absences route to not-cleared;
    a Route-Don't-Restate reconciliation note records that the ladder's
    blocked_or_contaminated use_when phrase "missing isolation, missing source
    identity" is read as an affirmative gate-breaking defect (not a
    not-yet-authored absence, which is an evidence gap capped per Seam 3), a
    reading the ladder's "breaks the evaluated gate" framing permits; and the
    JSG-06 forward-reference and the JSG-08 sealed_before_reveal == no mapping are
    reworded to name the field-level mechanism and its owner grounding. A robust
    later option is to add sealed_before_reveal == no to the JSG-08 owner
    contract's contaminated_or_invalid use_when so the conductor reads a literal
    owner mapping. Still no new claim tier or closeout_state minted. Round-9
    review patch (2026-06-03): a systematic predicate-completeness pass binds each
    gate predicate to its owner's full required-receipt rather than a bare
    structural field — JSG-02 now also requires the zero-spoiler participant-visible
    boundary (no packing leakage/spoiler block-class failure; semantic-leakage
    portion indeterminate_until_authored), JSG-03 now also requires the
    owner-required ledger contents (authors, version pins, enum-valid band inputs,
    second_label_diffs disagreement trail), and JSG-01's indeterminate subpredicate
    is broadened to source-identity, inspectability, and timing/cutoff; and the
    contamination enumeration is completed against all six ladder
    blocked_or_contaminated use_when items by adding the JSG-02/JSG-03 packing
    leakage/spoiler block-class failure and the JSG-07 unreconciled scoring
    failure-event as affirmative owner-reported invalidity values (the JSG-07
    value is withdrawn in the Round-11 entry below). Absence still routes to
    not-cleared (Seam 3); still no new claim tier or closeout_state minted. Round-11 review patch (2026-06-03): two predicate-binding corrections
    from the final review — (1) JSG-01's bound pre_decision_status subpredicate no
    longer clears on bare presence; Judgment-authority finalization is marked
    indeterminate_until_authored (the finalizing authority is an unstaffed open
    owner decision and an operator-set status is an owner block-state) and the
    clearing value is constrained to a cleared pre-decision value (not excluded);
    (2) the JSG-07 score_blocked value added in round 9 is WITHDRAWN from the
    contamination set — score_blocked is a mixed admission state firing mostly on
    absences, so the scoring-integrity-contamination subpredicate is now
    indeterminate_until_authored and a bare score_blocked / re-derivation mismatch
    / absent result routes to not-cleared (Seam 3), pending an owner field that
    discriminates an affirmative integrity failure from an absence. Two low nits
    also tidied (the sealed lifecycle row now points to the full JSG-06 predicate;
    JSG-07 re-derivation is framed as owner-authorized verification, not a
    conductor-computed score). The contamination set is therefore five affirmative
    owner values plus the two reconciled missing-isolation/source-identity
    readings; still no new claim tier or closeout_state minted.
  trigger: architecture_doctrine
  related_triggers:
    - lifecycle_boundary
  controlling_sources_updated:
    - docs/product/judgment_quality_promotion_operating_model_v0.md
    - .agents/workflow-overlay/source-loading.md
    - docs/workflows/orca_repo_map_v0.md
    - docs/research/judgment-spine/manifest_v0.md
    - docs/product/judgment_spine_gate_ownership_map_v0.md
  downstream_surfaces_checked:
    - AGENTS.md
    - .agents/workflow-overlay/README.md
    - .agents/workflow-overlay/source-of-truth.md
    - .agents/workflow-overlay/product-proof.md
    - .agents/workflow-overlay/validation-gates.md
    - docs/product/judgment_spine_evidence_ladder_architecture_v0.md
    - docs/product/judgment_spine_gate_ownership_map_v0.md
    - docs/product/judgment_spine_reveal_calibration_owner_contract_v0.md
    - docs/research/judgment-spine/harness/v0_14/contestant_no_tools_execution_contract_v0.md
    - docs/research/judgment-spine/harness/v0_14/memorization_probe_protocol.md
    - docs/research/judgment-spine/harness/v0_14/phase_1_infrastructure_architecture.md
    - docs/research/judgment-spine/harness/v0_14/packing_to_harness_foundation_interface_architecture_v3.md
    - docs/research/judgment-spine/harness/v0_14/band_input_labeling_rubric.md
    - docs/research/judgment-spine/manifest_v0.md
    - orca-harness/scoring/band_scorer.py
    - orca-harness/runners/run_case.py
  intentionally_not_updated:
    - path: .agents/workflow-overlay/validation-gates.md
      reason: >
        The existing Judgment Spine claim-tier gate already requires claim tier
        and closeout state before stronger claims. The conductor routes through
        that gate; it does not add a new overlay validation rule.
    - path: docs/product/judgment_spine_evidence_ladder_architecture_v0.md
      reason: >
        The ladder owns claim tiers, closeout states, weakest-cleared-gate, the
        sub-floor rule, and receipt minima. The conductor consumes that
        vocabulary and adds none.
    - path: docs/product/judgment_spine_reveal_calibration_owner_contract_v0.md
      reason: >
        The JSG-08 contract owns the reveal/calibration receipt shape and
        satisfaction states. The conductor reads its status field and changes
        nothing.
    - path: orca-harness (band_scorer.py, run_case.py, runners, schemas)
      reason: >
        No code changed. The conductor describes how existing plumbing maps to
        gates and records that the contestant-execution runner remains deferred.
    - path: Daimler-specific and Canoo/Walmart case, run, and decision artifacts
      reason: >
        This is a case-agnostic operating model. Applying it to a specific case
        requires a separate case-specific run-state and classification record.
  stale_language_search: >
    rg -n "conductor|operating model|sealed_awaiting_outcome|halted_no_completed_closeout|indeterminate_until_authored|judgment_quality_promotion_operating_model|by-hand"
    docs/product/judgment_quality_promotion_operating_model_v0.md
    .agents/workflow-overlay/source-loading.md
    docs/workflows/orca_repo_map_v0.md
    docs/research/judgment-spine/manifest_v0.md
    docs/product/judgment_spine_gate_ownership_map_v0.md
  stale_language_search_result: >
    Executed on 2026-06-03 after wiring. The new lifecycle vocabulary
    (sealed_awaiting_outcome, halted_no_completed_closeout,
    indeterminate_until_authored) appears only in this conductor, with no
    colliding or contradicting use elsewhere. The operating-model path appears
    in this conductor and the four wired surfaces (source-loading read pack,
    repo map, manifest, gate ownership map), plus historical deferred notes in
    the evidence ladder, product-proof, and the gate map's own prior DCP, one
    prior review output, and disposable hygiene-queue checkpoints. Those prior
    references are historical DCP or checkpoint records left intact by design;
    none contradicts the re-opening recorded here. No hit converted a routing or
    navigation surface into validation, readiness, scoring authorization, model
    execution, or judgment-quality evidence.
  non_claims:
    - not validation
    - not readiness
    - not buyer proof
    - not fixture admission
    - not scoring authorization
    - not model execution
    - not judgment-quality evidence
    - not implementation authorization
```
