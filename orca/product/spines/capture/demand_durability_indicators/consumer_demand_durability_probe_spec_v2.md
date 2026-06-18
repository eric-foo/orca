# Orca Consumer-Demand Durability Probe — Spec v2 (discovery-hardened)

```yaml
retrieval_header_version: 1
artifact_role: Product artifact - Direction-B method-validation probe spec
scope: >
  v2 (discovery-hardened) validation design for the consumer-demand PERSISTENCE
  discrimination probe (US beauty/skincare): downstream persistence-vs-collapse
  backtest, delta-graded independence-weighted durable-label with a naive-momentum
  baseline, denominator-integrity rules, latent-knowledge blindness states, and
  reuse bindings into existing Core Spine v0 method-validation apparatus.
  Decision-prep for owner sign-off; bounded same-vendor closure recheck completed (CA-adjudicated keep); does not authorize execution.
use_when:
  - Preparing the consumer-demand probe case-identity / case-frame locks or a probe run.
  - Checking the locked durable-label, the persistence read, the momentum baseline, or the staged design.
  - Deciding whether consumer-demand (Direction B) probe material is being overclaimed.
authority_boundary: retrieval_only
supersedes:
  - docs/product/consumer_demand_probe/consumer_demand_durability_probe_spec_v1.md
open_next:
  - docs/product/core_spine_v0_method_validation_rubric_v0.md
  - docs/product/core_spine_v0_method_validation_case_frame_lock_contract_v0.md
  - docs/product/orca_backtest_specimen_unity_runtime_fee_source_packet_v0.md
  - docs/product/judgment_spine_reveal_calibration_owner_contract_v0.md
  - docs/product/core_spine_v0_corroboration_vs_amplification_discipline_v0.md
  - .agents/workflow-overlay/product-proof.md
stale_if:
  - Owner changes the locked durable-label, the staged design, the persistence-discrimination claim, or the momentum baseline.
  - A later accepted Direction decision retires, supersedes, or relocates the Direction-B consumer-demand probe.
  - The reused method-validation rubric, case-frame-lock contract, or JSG-08 receipt shape changes materially.
```

- Status: `PROPOSED_PROBE_SPEC_V2 — KEEP-CLEARED` (delegated-review loop complete, 2026-06-10). Discovery-hardened: incorporates the adjudicated **cross-vendor discovery review** (4 findings) + the v1 sanity-hardening + the owner's "narrow the claim (lean)" decision; the **bounded same-vendor closure recheck confirmed all 4 closed with no new blocker/major**, and the CA adjudicated **keep**. Honest scope: known seams closed and verified — **not** proven seam-free (the recheck is same-vendor verification, not a fresh cross-vendor discovery pass). Still decision-prep / PROPOSED — **not validation, buyer proof, or authorization to execute; pending owner sign-off and case-frame lock before any run.** **UPDATE 2026-06-10: a Round-3 cross-vendor (GPT-5.5 Thinking) re-review of the Stage-2 validity logic returned 4 accepted findings; patches applied (§4/§6/§8/§9/§12/§15 + the Stage-2 lock); keep-clearance was SUPERSEDED by Round-3; the patches landed and the bounded same-vendor post-patch recheck completed (Sonnet — all 4 findings closed, no new blocker, CA-adjudicated keep), so v2 is RE-KEPT at the Round-3 cross-vendor bar (§17).**
- Artifact type: Direction-B method-validation probe specification (consumer-demand persistence discrimination).
- Date context: 2026-06-10, Asia/Singapore.
- Implementation authorized: no. Case execution / evidence collection authorized by this artifact: no. Cleaning/ECR spine, code, harness, automation, scrapers, dashboards, scoring engines authorized: no.
- Source basis: owner direction across the 2026-06-10 Direction-A-vs-B adjudication thread; the adjudicated v0 same-vendor sanity review and the v1 cross-vendor discovery review; reuse bindings to the Core Spine v0 method-validation rubric, the case-frame-lock contract, the Unity backtest specimen template, the JSG-08 reveal/calibration owner contract, the corroboration-vs-amplification discipline, and `.agents/workflow-overlay/product-proof.md`.

## 1. Purpose and the question under test

Direction B (consumer-demand intelligence) rests on one claim: that Orca's judgment layer can read **durable** consumer demand from public signal before it shows up in financials. Before any cleaning/ECR spine build, label corpus, advisor network, or buyer contact, this probe tests that uncertainty at the lowest possible lock-in.

Question under test (**narrowed in v2 — owner decision**):

> On retrievable consumer public substrate (US beauty/skincare), can Orca's judgment layer **discriminate demand that *persists* (durable) from demand that *collapses* (hollow)** — a *decide-grade* call that **beats the pre-registered naive baselines (momentum-extrapolation and the category/structural prior) and is grounded in the brand's own signal**, not a confirmatory restatement of pre-cutoff momentum or a category prior — and is the pollution **separable enough by hand** to specify a cleaning spine?

**What this is scoped to (v2 claim narrowing).** The historical backtest is **scoped to persistence discrimination** (whether pre-cutoff signal lets the judgment layer separate brands that will persist from those that will collapse); being unrun and `product_learning`, it can at most yield **bounded evidence** for that discrimination, never proof of it. It does **not** directly prove **manufactured-vs-organic** separation — a brand can persist on sustained paid spend rather than organic pull, and the paid-proxy stream is not reconstructable historically (see §3). Manufactured-vs-organic separation is a **forward/live** capability; in the backtest, cross-signal consistency provides only a **best-effort, partial** manufactured flag (§3, §8). The probe's byproduct — the hand-derived cleaning protocol — is the first-draft spec for the later cleaning/ECR spine.

This is a method-validation probe in the same family as the Core Spine v0 five-case validation, on a new decision family (consumer-demand persistence) and a new substrate.

## 2. Where this plugs in — reuse vs new

**Reuse (do not reinvent):** the Unity backtest specimen's **phased structure** (Phase 0 frame → Phase 1 pre-cutoff packet → Phase 2 sealed memo → calibration, with anti-leakage ledger, source caps, source-family boundaries); the **method-validation rubric** skeleton (judgment > cleaning > data-farming; pre-selected cases; post-window leakage = fail; preserve misses); the **case-frame-lock 3-layer sequence**; the **zero-spoiler lanes + JSG-08 receipt**; the **corroboration-vs-amplification discipline** (non-destructive cleaning; the organic-vs-artificial call lives in Judgment).

**New (this probe introduces):** the persistence-discrimination decision family; the downstream persistence read (§3); the delta-graded, independence-weighted, pre-registered durable-label **with a naive-momentum baseline** (§4); rubric dimensions funnel-propagation, post-collapse persistence, and the momentum baseline + separability-tractability logging (§8); recent-resolved + retrievability-screened case selection with **structurally enforced momentum-matched hardness and latent-knowledge blindness** (§7, §9, §16); the **N-floor with denominator integrity** (§12).

## 3. The persistence read — downstream model (core mechanic)

The conceptual model is two **time-series** streams: a **paid-proxy stream** (the public shadow of promotional spend — disclosed `#ad`/sponsored, gifting/PR-unboxing, affiliate-code posts, coordinated multi-creator bursts, brand-owned accounts) and an **organic stream** (unprompted, dispersed, user-initiated). Ideal durable = organic rises during the push *and persists after the paid-proxy stream decays*, propagating down-funnel; hollow = a top-of-funnel spike that collapses when paid-proxy decays.

**Backtest reframe (v1) + claim narrowing (v2).** In historical backtests the paid-proxy stream is largely **unrecoverable** (§7), so the backtest does **not** reconstruct it or date spend-stop. The backtest's discriminator is **downstream persistence vs collapse** on the retrievable substrate:

- **Funnel propagation:** did demand propagate *downstream* — search → review velocity → retail presence — rather than stay top-only?
- **Persistence:** did the downstream signal *persist* across the outcome window rather than collapse?
- **Cross-signal consistency — best-effort manufactured flag (v2, partial only):** does the downstream signal move *together* across independent substrates (more likely real) or concentrate/echo in one channel (more likely manufactured)? This is a **weak, partial** proxy for manufactured-vs-organic — it does **not** establish it. A brand persisting via sustained paid spend can still propagate; the backtest cannot rule that out (it is forward/live work). Record cross-signal consistency as supporting context, never as a manufactured-vs-organic verdict.

Where a paid-proxy trace *is* recoverable for a case, it is recorded as best-effort context, not a gate. Capture must be **time-series, not snapshot**; the judged axis is a **relationship over time**, not a single-number threshold.

## 4. The durable-label — LOCKED (tiered, independence-weighted, delta-graded, momentum-baselined, pre-registered)

The ground-truth outcome the blind call is graded against. Structure is load-bearing; thresholds/horizon are tunable.

- **Tier 1 — hard commercial markers (highest authority, when retrievable):** acquisition, an up-round / follow-on raise, or a major retail expansion within the outcome window.
- **Tier 2 — retrievable composite floor, at ~18 months post-cutoff (tunable), graded on DELTAS not levels:** retail presence graded on **post-cutoff delta expansion beyond the pre-cutoff observable** (highest weight); review accumulation graded on the **change in rate** (accel/decel) vs pre-cutoff baseline (mid weight); search-interest persistence (lowest weight, down-weighted for circularity).
- **Retail/review growth counts as demand — no retailer-entry normalization (post-Stage-1 owner decision, 2026-06-10):** Stage-1 proposed *normalizing out* retailer-launch review/retail spikes (e.g., an Ulta-entry surge) as distribution-not-demand. **Declined** — getting into retail and selling through is itself demand evidence (accessibility + social proof drive real buying). Durability is read from **persistence** — does the elevated retail/review rate *hold or keep expanding* after the entry bump vs collapse back (distribution gained then lost = the hollow pattern) — not from subtracting the entry effect. Tier-2 retail/review stay graded on post-cutoff deltas (above); a retailer-entry event is a *test* of persistence, not a confound to remove. Supersedes the Stage-1 report's retailer-entry-normalization condition (its §3.2 / §4 / §6).
- **Anti-circularity firewall (v1):** any Phase 1 predictor source family that overlaps a Tier-2 label component carries a strict temporal/categorical firewall; Tier-2 retail/review are graded on post-cutoff **deltas only**; the grade leans on the signals the predictor leaned on least.
- **Naive-momentum baseline (v2 — discovery Finding 1, the validity keystone):** delta-grading alone does **not** fully break circularity, because strong pre-cutoff momentum mechanically predicts post-cutoff deltas. So the case-frame lock must record, pre-registration, the **naive-momentum-extrapolation prediction** for each case (what "just extrapolate the pre-cutoff trajectory" would predict). A case supports the discrimination claim **only where momentum-extrapolation does *not* already give the right answer** — i.e., where continuation was **not** the obvious at-cutoff call. For a Stage 2 pair this means the pair must be **momentum-matched**: both on similar pre-cutoff trajectory, so trend-extrapolation cannot separate them (§7). The judgment call is **decide-grade only if it beats the momentum baseline** (§8, §12).
- **Naive baselines are plural — also the category/structural prior (post-Stage-1, owner 2026-06-10):** momentum is not the only cheap shortcut to the right answer without the target skill. A **category/structural prior** ("trend-/fad-tethered category → hollow; evergreen-need category → durable") can separate a pair by a blanket category rule that never reads the brand's own signal and would not generalize. The case-frame lock must **pre-register each applicable cheap prior** (momentum **and** the category/structural prior); a call is **decide-grade only when its reasoning is grounded in the brand's own retrievable signal**, beating those priors rather than matching them. Structural/category durability reasoning is **legitimate and credited when signal-grounded** — discounted only when it is the *sole* basis (a category-only call validates category priors, not the signal-reading capability under test). The handful (§5) must include pairs **not** separable by category alone.
- **Cheap-prior inventory + residual-prior risk (cross-vendor Round-3 Finding 3):** "pre-register each applicable cheap prior" is operationalized as a **per-case inventory** in the case-frame lock: list the *materially plausible* shortcut priors for the chosen pair (at minimum momentum and category/structural; plus, where applicable, founder pedigree, VC-backing / raise size, celebrity halo, retail-channel quality, retail-door-expansion rate, trade-press heat). A call **primarily supported by any inventoried prior without independent signal grounding is discounted to confirm-grade** (signal-grounding tested objectively by the §6 two-stage elicitation). The inventory cannot be exhaustive, so the calibration **logs residual unmodeled-prior risk as part of the result**, not a side note.
- **Decision rule (pre-registered before reveal):** `durable` = Tier-1-positive **OR** (no Tier-1 **AND** ≥2 of 3 Tier-2 delta-components above pre-set thresholds). Else `hollow`. Genuinely unresolved → `borderline`.
- **Borderline = label ungradeability only (v2 — discovery Finding 2):** a case is `borderline` **only** when its *outcome did not resolve* under the pre-registered criteria — judged **independently of how hard the case was to call**. Borderline must **never** be used to drop a hard-but-resolved case. Borderline handling is in §12.
- **Pre-registration:** thresholds, horizon, weights, firewalls, and the momentum-baseline prediction fixed **before** reveal, in the case-frame lock.
- **Two error types tracked separately:** false-`durable` (greenlit hype) worse than false-`hollow` (missed winner); the bar runs slightly strict; report which way the judge errs.

## 5. Staged design

- **Stage 1 — feasibility / face-validity (non-blind, ~1–2 days, ONE recent known-outcome brand).** Is the retrievable downstream substrate gettable at usable fidelity, and is the persist/collapse pattern visible against the known outcome? Non-blind → a **gate, not evidence of decision-gradeness**. Stage 1 is the retrievability gate (§11).
- **Stage 2 — proceed/stop gate (blind, zero-spoiler, recent-resolved, momentum-matched PAIR).** A single correct binary call (50% base rate) is **not** a discrimination claim and must also **beat the momentum baseline**; a correct, decide-grade, momentum-beating call labels "feasibility confirmed, not validated" and authorizes the handful.
- **Manual handful (~5–8 cases) — where the discrimination claim lives** (the N-floor, §12). Locks the cleaning protocol.
- **Volume deferred to the spine.** Out of scope here; gated on this probe.

## 6. Per-case phased structure (reuse the specimen template)

- **Phase 0 — case frame:** case identity, decision family = consumer-demand persistence, cutoff + fair-cutoff rationale, Phase-2 question, assumed decision-owner role (consumer investor / diligence / allocator), allowed/forbidden source families with §4 firewalls, **the pre-registered naive-momentum-extrapolation prediction**, blocker conditions, no-outcome boundary. Locked in the case-frame-lock artifact, not here.
- **Phase 1 — pre-cutoff downstream packet (time series):** capture pre-cutoff retrievable signal (search, community, reviews, retail/site), dated, with the specimen's source ledger, source caps, anti-leakage ledger. Preserve source identity / independence / timing non-destructively (§10). Paid-proxy traces best-effort where available.
- **Phase 2 — sealed at-cutoff blind memo, TWO-STAGE (the objective signal-grounding test — cross-vendor Round-3 Finding 1):** the call is produced in two sealed stages. **Stage A (signal-only):** given only the dated signal series (search / review-velocity / retail-presence curves), with brand name and category framing withheld/anonymized, make the persist/collapse call and justify it *from the curves*. **Stage B (full):** with brand + category context added, make the final call stated **relative to the pre-registered cheap priors** (does it beat momentum *and* the category/structural prior, and why), with explicit unknowns + uncertainty. **Decide-grade requires the Stage-A signal-only call to be correct and reasoned from the series**; a call correct only at Stage B (after category context) is *confirm-grade* — it rode a prior, not signal-reading. Both stages sealed before reveal.
- **Calibration:** grade the sealed call against the pre-registered delta-graded durable-label and the momentum baseline; produce a JSG-08 receipt (§9).

## 7. Case selection — recent-resolved, retrievability-screened, momentum-matched, label-screened

- **Recent-resolved:** spike *and* outcome recent enough for retrievability, long enough ago (~18mo default) that the label has resolved.
- **Downstream-retrievability screen (case admission):** admit only if the downstream substrate (search Trends, timestamped reviews, retail/Wayback) is reconstructable. Lossy paid-proxy/social is not a disqualifier.
- **Label-retrievability screen (v1, at case-frame lock):** verify a public Tier-1 marker **or** a constructable Tier-2 delta-composite for that brand, else reject the case at lock time.
- **Momentum-matched hardness (v2 — discovery Finding 1 + sanity Finding 3):** the Stage 2 pair must be screened for **multi-signal similarity including pre-cutoff trajectory/momentum** across all allowed source families, documented in the case-frame lock. The pre-registered **"hard case" criterion**: no single pre-cutoff signal — and not naive momentum-extrapolation — may cleanly separate the pair. An **independent reviewer not involved in selection** confirms the pair is genuinely hard (no "tells," and continuation is not the obvious call) before the blind call runs.
- **Latent-knowledge blindness (v2 — discovery Finding 4; enforced in §9):** prefer non-consensus / under-covered brands; enforce blindness via the §9 latent-knowledge protocol, including model-pretraining contamination, not aspiration.

## 8. Rubric dimensions

1. **Decide-vs-confirm, against the pre-registered naive baselines (v2; pluralized post-Stage-1):** did the pre-cutoff signal *decide* the call beyond what the cheap priors already predicted — both **momentum-extrapolation** and the applicable **category/structural prior** (§4)? A call that merely matches a naive baseline, **or rests solely on a category prior without grounding in the brand's own signal**, is **confirm-grade**, not decide-grade, and does not count toward the discrimination claim. **Signal-grounding is graded objectively by the two-stage elicitation (§6), not by subjectively reading the memo:** decide-grade requires the Stage-A (signal-only, category-withheld) call to be correct and reasoned from the curves; a call correct only at Stage B is confirm-grade. A call primarily supported by any inventoried cheap prior (§4) without independent signal grounding is likewise confirm-grade.
2. **Funnel-propagation:** did the read correctly detect downstream propagation vs top-only?
3. **Post-window persistence:** did the read correctly detect persistence vs collapse?
4. **Cross-signal consistency (best-effort manufactured flag, partial — v2):** recorded as supporting context, **not** a manufactured-vs-organic verdict (§3).
5. **Separability-tractability (required output):** logged with the minimum content spec — (a) typed taxonomy of pollution classes, (b) hand-rule per class, (c) FP/FN estimate per rule, (d) judgment-competency note where unformalizable. **This log is the cleaning-spine spec seed.**

**Head-to-head:** compare consumer cases' decide-gradeness to the existing B2B pricing cases on the **same decide-vs-confirm dimension (#1)**; criterion: consumer calls score **at least the median B2B case**; if B2B scores are unrecorded, qualitative with an explicit uncertainty note.

## 9. Zero-spoiler lanes, latent-knowledge blindness, and calibration receipt

- **Lane separation (per `product-proof.md`):** `participant_packet` (pre-cutoff only) → `facilitator_ledger` (sealed outcomes) → `blind_judgment` (sealed before reveal) → `outcome_calibration`. Contaminated participant material is rebuilt clean, not edited in place.
- **Latent-knowledge blindness protocol (v2 — discovery Finding 4):** disclosure of *declared* awareness is not enough — a judge (human or **LLM, via pretraining**) may **recognize** a brand's trajectory, consensus status, acquisition, or shutdown without consciously "knowing" the answer. Before the blind call, the judge completes a **pre-call knowledge probe** ("state anything you know or suspect about this brand's trajectory/outcome"), logged in the JSG-08 receipt under `judge_prior_knowledge`. Each case is assigned a **blindness result state**: `clean_cold` / `partial_recognition` / `contaminated` / `replaced_or_cold_judge`. `contaminated` (and `partial_recognition` above a pre-set threshold) cases are **excluded without improving the denominator** (§12). For LLM judges, prefer a knowledge-cutoff-before-outcome model and/or brands below pretraining salience; the judge-selection and blindness criteria are **specified in the case-frame lock**, not left to execution discretion. (A judge must be a fresh context that has never seen the facilitator ledger or any thread containing outcomes.)
- **Calibration receipt (per JSG-08):** at most `qualitative_outcome_calibration` (no JSG-07 scoring). Record sealed_blind_output (sealed before reveal), reveal_event, calibration_frame (declared before interpretive reveal use), comparison_inputs, `scoring_relationship: none_qualitative_only`, `judge_prior_knowledge`, `blindness_state`, `cheap_prior_predictions` (momentum + category/structural + inventoried), `stage_a_signal_only_call` (the objective signal-grounding result), `residual_unmodeled_prior_risk`, missing_evidence, claim_cap, non_claims.
- **Claim tier (per `product-proof.md`):** all probe output is `product_learning`.

## 10. Non-destructive cleaning discipline

Per the corroboration-vs-amplification discipline, Phase 1 cleaning **must be non-destructive**: preserve source identity, independence, count, timing — the persist-vs-collapse discrimination happens at **Judgment**, not in cleaning. Within-review heuristics catch cheap pollution; the robust separator is **cross-signal consistency**.

## 11. Stage 1 outputs and pass/fail

Outputs: a downstream-retrievability report, a face-validity read (persist/collapse pattern visible vs the known outcome?), a best-effort paid-proxy-recoverability note, and a first-draft cleaning/classification protocol.

- **Pass:** downstream substrate retrievable at usable fidelity **and** the pattern visibly consistent with the known outcome → proceed to Stage 2.
- **Fail:** downstream data ungettable, or the pattern invisible even with the outcome known → reconsider before Stage 2.
- **Boundary:** Stage 1 is non-blind → feasibility only.

## 12. Strong / weak / fail signals, N-floor, denominator integrity, borderline & contamination

- **N-floor:** a **strong** signal requires the judgment layer to correctly, **decide-gradely (beating *all* pre-registered cheap priors — momentum and category/structural — and passing the §6 Stage-A signal-only test)** discriminate on at least **≥4 of 5** clean-label, clean-blind calls across the handful (misses preserved as calibration), **not** the single Stage 2 pair.
- **Denominator integrity (v2 — discovery Findings 2 & 4):** the strong-signal fraction is computed **only** over cases that are both clean-label (not `borderline`) and clean-blind (`clean_cold`). Exclusions (`borderline`, `contaminated`, over-threshold `partial_recognition`) **cannot improve the strong-signal claim**, and the **excluded-case composition + borderline/contamination frequency are part of the result, not a side report**. A strong signal is **blocked** if exclusions removed the hardest cases (e.g., the momentum-unmatched ones). If borderline+contaminated exceed a pre-set fraction (e.g., 2 of 8), flag a **substrate-legibility** finding.
- **Weak:** calls collapse to "looks fine"; the read only works when the outcome is obvious or matches momentum-extrapolation; the judge cannot beat the baseline; memos read like trend summaries.
- **Fail:** post-window/outcome leakage into the sealed call; cases chosen because the outcome is persuasive; momentum-continuation counted as judgment; misses or excluded hard cases removed to inflate the claim; the work turns into a data-spine/dashboard/scraper.

## 13. Output expected from a probe run

Locked case frames (cutoff + fair-cutoff rationale + pre-registered delta-graded durable-label + firewalls + momentum-baseline prediction + judge-selection/blindness criterion); per-case pre-cutoff downstream packets; sealed blind persist-vs-collapse memos (each stated relative to the momentum baseline); JSG-08 calibration receipts (incl. `judge_prior_knowledge`, `blindness_state`, `momentum_baseline_prediction`); the separability/cleaning protocol log (with §8 minimum content); the handful-level discrimination result against the N-floor **with full excluded-case composition**; the head-to-head vs B2B; explicit non-claims.

## 14. Boundaries / out of scope (separate authorization required)

Cleaning/ECR spine build; any code/harness/scraper/automation/dashboard/scoring engine; case execution / evidence collection; the forward/live paid-proxy two-stream and manufactured-vs-organic capability; buyer or advisor outreach; commercial-frame or pricing decisions; the beauty ontology, label corpus, and advisor network.

## 15. Non-claims

Not validation, not willingness-to-pay, not readiness, not buyer proof, not ICP-proven, not Core Spine v0 validation, not judgment-quality evidence. **The backtest can support at most a bounded persistence-discrimination claim, NOT manufactured-vs-organic separation** (forward/live); cross-signal consistency is a best-effort, partial manufactured flag only. A small manual N proves *possibility, not reliability*. No buyer has paid Orca. Even a clean handful on US beauty/skincare does **not** license a broad consumer-demand claim. This spec is decision-prep for owner sign-off; it does not authorize execution, the spine, or any runtime work; the bounded same-vendor closure recheck completed (CA-adjudicated **keep**), so v2 is keep-cleared — keep-clearance is a review state, **not** validation or execution authority.

## 16. Next authorized step

1. **This spec (v2)** → the **bounded same-vendor closure recheck** (verified the 4 discovery findings closed and no new blocker/major in the changed sections) → CA adjudication → keep. **COMPLETED 2026-06-10 — recheck closed, CA-adjudicated keep; v2 is KEEP-CLEARED.** The cross-vendor discovery review is incorporated; v1 is superseded. (The actual next step is item 2 below.)
2. **Owner sign-off**, then **case identity lock + case-frame lock** — select the Stage 1 case and the momentum-matched Stage 2 pair from the screened candidate pool (sealed, facilitator-side); lock cutoff, fair-cutoff rationale, source-family boundaries + firewalls, the pre-registered delta-graded durable-label, the naive-momentum-extrapolation prediction, the hardness documentation, the label-retrievability confirmation, and the judge-selection / latent-knowledge-blindness criterion. Safe detail only.
3. **Stage 1 execution** — only after 1–2 clear, under separate authorization.

Do not run evidence replay or build any spine/harness from this spec. It frames and locks; it does not execute.

## 17. Review-response changelog

### Round 1 — same-vendor sanity review (Sonnet 4.6), adjudicated 2026-06-10 → v1

11 findings, all accepted. Resolutions (carried into v2): retail/review delta-grading + firewall (F1/F5); downstream-reframe (F2/F7); multi-signal hardness screen + independent check (F3); judge prior-knowledge disclosure + cold-judge (F4); N-floor on the handful, Stage 2 as a gate (F6); label-retrievability screen (F8); cleaning-log minimum content (F9); head-to-head definition (F10); borderline handling (F11). (Full table in the v1 artifact.)

### Round 2 — cross-vendor DISCOVERY review, adjudicated 2026-06-10 → v2

4 findings, all accepted (the stronger de-correlated bar). Unifying theme: *v1 could still pass for the wrong reason — by riding pre-cutoff momentum, not by judging.*

| # | Sev | Finding | Disposition in v2 |
|---|---|---|---|
| 1 | Critical | Residual circularity: pre-cutoff momentum mechanically predicts post-cutoff deltas | §4, §7, §8, §12 — **naive-momentum baseline** the call must beat; momentum-matched pair; cases where continuation is the obvious call don't support the claim |
| 2 | Major | Borderline + ≥4/5 denominator = cherry-pick loophole | §4, §12 — borderline = **label ungradeability only**, outcome-difficulty-independent; exclusions can't improve the claim; excluded composition is part of the result; strong signal blocked if hardest cases were excluded |
| 3 | Major | Downstream-reframe may gut the manufactured-vs-organic discriminator | §1, §3, §8, §15 — **claim narrowed (owner: lean)** to *persistence discrimination*; cross-signal consistency = best-effort/partial manufactured flag; manufactured-vs-organic = forward/live |
| 4 | Minor (elevated for LLM judges) | Blindness gameable for latent/pretraining knowledge | §9, §12 — **latent-knowledge protocol**: pre-call knowledge probe, blindness states (clean_cold/partial/contaminated/replaced), contaminated excluded without improving the denominator |

Residual risks carried forward: historical paid-proxy reconstruction stays out of scope (manufactured-vs-organic is forward/live); domain generalizability beyond US beauty/skincare not licensed; the durable/hollow dichotomy may be a false binary in "staircase"-demand populations (the `borderline`=ungradeable valve + substrate-legibility flag partially handle this). **Keep-state was pending the bounded same-vendor closure recheck; that recheck subsequently completed — CA-adjudicated keep, 2026-06-10 (see the Status line).**

### Post-Stage-1 owner correction (2026-06-10)

Stage-1 feasibility surfaced a proposed durable-label refinement — normalize the review-accumulation component for retailer-entry review spikes (distribution expansion ≠ demand persistence). **Owner declined.** Retail entry + sell-through is itself demand evidence (accessibility + social proof); durability is carried by the **persistence read** (does elevated retail/review activity hold after the entry bump), not by subtracting the entry effect. The locked durable-label (§4) is **unchanged in structure** — the decision keeps the Tier-2 delta grading as-locked and forecloses inserting a normalization step. Recorded at §4. Supersedes the Stage-1 report's retailer-entry-normalization condition (§3.2 / §4 cleaning-class / §6). Provenance: owner decision in the 2026-06-10 thread; not a review finding, so the v2 keep-state is unaffected.

### Post-Stage-1 owner correction 2 — category/structural prior as a second naive baseline (2026-06-10)

Surfaced by the preliminary independent hardness review of Stage-2 Pair A: the durable/hollow split can be predicted by a **category/structural prior** (trend-tethered → hollow, evergreen → durable) that never reads the brand's own signal and would not generalize — a second cheap shortcut alongside momentum. **Owner decision:** pre-register each applicable category/structural prior as a baseline the call must beat; a **decide-grade** call requires **brand-specific signal grounding**, not a category-only call; the handful must include **category-matched** pairs (both the same category-type, so the prior cannot separate them). Structural durability reasoning stays legitimate when signal-grounded. Recorded at §4 + §8. Provenance: owner decision, 2026-06-10; not a review finding.

### Round 3 — cross-vendor re-review of the Stage-2 validity logic (GPT-5.5 Thinking), adjudicated 2026-06-10

A no_repo cross-vendor (OpenAI GPT-5.5 Thinking) adversarial review of the category-prior settlement + the Stage-2 validity machinery. 4 findings, all accepted by the Opus CA. Patches applied (pending the bounded same-vendor post-patch recheck before keep):

| # | Sev | Finding | Disposition |
|---|---|---|---|
| 1 | Major | Pair A's true-outcome-aligned category prior made decide-grade hinge on a subjective memo-read (a fake-success path) | §6 / §8 + lock §5/§8 — **objective two-stage ablation elicitation**: decide-grade requires a correct **Stage-A (signal-only, category-withheld)** call; Pair A kept (owner decision) |
| 2 | Major | Lock result semantics still defined decide-grade/pass in **momentum-only** terms after the baselines were pluralized (a propagation miss in the category-prior correction) | lock §8/§9 + spec §12/§9 — decide-grade / pass / N-floor / receipt now require beating **all** pre-registered cheap priors **and** Stage-A grounding |
| 3 | Major | Other cheap priors (founder pedigree / VC / celebrity / channel / raise) were unbounded | §4 + lock §3 — **per-case cheap-prior inventory** + grade-discount of shortcut-dominated calls + **residual-unmodeled-prior-risk logged in the result** |
| 4 | Minor | "proves persistence discrimination" overclaimed an unrun `product_learning` probe | §1 / §15 — softened to "scoped to / can support bounded evidence for" |

Provenance: reviewed_by `gpt-5.5-thinking`, authored_by `claude-opus-4.8`, de_correlation_bar `cross_vendor_discovery`, access `no_repo` (advisory; the CA applied the patches). **Bounded same-vendor post-patch recheck completed (Sonnet): all 4 closed, no new blocker/major in the touched delta, CA-adjudicated keep — v2 re-kept. Durable record: `docs/review-outputs/adversarial-artifact-reviews/consumer_demand_probe_stage2_validity_crossfamily_review_v0.md`.**
