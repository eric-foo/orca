# Canoo Walmart Case Index

```yaml
retrieval_header_version: 1
artifact_role: Research artifact
scope: Case index for the Canoo/Walmart Judgment Spine candidate case track.
use_when:
  - Locating Canoo/Walmart case-track artifacts before source-packet or participant-packet work.
  - Checking what exists and what remains missing before blind use.
  - Avoiding accidental reuse of outcome, agreement, or post-cutoff material as participant input.
authority_boundary: retrieval_only
open_next:
  - docs/research/judgment-spine/cases/canoo-walmart/case_track_preflight_v0.md
  - docs/research/judgment-spine/cases/canoo-walmart/jsg_08_reveal_calibration_receipt_v0.md
  - docs/research/judgment-spine/manifest_v0.md
  - docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/fixture_authoring_receipt_v0.md
  - .agents/workflow-overlay/product-proof.md
```

## Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S1 plus Judgment Spine parent, product-proof zero-spoiler rules, v0.14 case-construction protocol, and one public source-loading unit
  edit_permission: docs-write
  target_scope: Initialize the Canoo/Walmart Judgment Spine case track after owner accepted Step A as plumbing only.
  dirty_state_checked: yes
  blocked_if_missing: no
```

## Case Snapshot

- case_name: Canoo/Walmart last-mile EV fleet commitment
- decision_family: strategic supplier selection, fleet electrification, startup counterparty risk, last-mile economics, exclusivity, and option-value discipline
- recommended_cutoff: before the July 2022 definitive agreement was announced
- spoiler_state: pre-reveal comparison sealed; facilitator ledger, reveal readout, and outcome calibration created
- learning_status: qualitative outcome calibration and JSG-08 companion receipt created; artifact volume is not readiness; draft v0.14 fixture pack exists and is blocked before scoring; judgment-quality validation not proven
- learnability_tier: Tier 0 case learning captured; not repeatability proof, scoreable fixture, or model validation

## Existing Artifacts

| Artifact | Path | Use |
| --- | --- | --- |
| Case-track preflight | `docs/research/judgment-spine/cases/canoo-walmart/case_track_preflight_v0.md` | Zero-spoiler source sufficiency and routing preflight |
| Source packet | `docs/research/judgment-spine/cases/canoo-walmart/source_packet_v0.md` | Clean pre-cutoff source substrate; adversarial review completed before participant packet |
| Safety receipt | `docs/research/judgment-spine/cases/canoo-walmart/safety_receipt_v0.md` | Zero-spoiler receipt for source-packet use; adversarial review completed |
| Adversarial source-packet review | `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_source_packet_safety_adversarial_artifact_review_v0.md` | Source packet accepted with friction for participant-packet authoring; not validation or readiness |
| Participant packet | `docs/research/judgment-spine/cases/canoo-walmart/participant_packet_v0.md` | Anonymized zero-spoiler candidate packet for blind judgment capture |
| Blind judgments | `docs/research/judgment-spine/cases/canoo-walmart/blind_judgments_v0.md` | User-supplied blind LLM contestant result with `no_reveal_seen` exposure declaration |
| Owner-context judgments | `docs/research/judgment-spine/cases/canoo-walmart/owner_context_judgments_v0.md` | Owner-assisted judgment; separate from clean blind result |
| Pre-reveal judgment comparison | `docs/research/judgment-spine/cases/canoo-walmart/pre_reveal_judgment_comparison_v0.md` | Compares blind LLM and owner-assisted judgments before facilitator/reveal/outcome material |
| Facilitator ledger | `docs/research/judgment-spine/cases/canoo-walmart/facilitator_ledger_v0.md` | Sealed facilitator-only actual-action, agreement, and outcome source ledger; not participant-facing |
| Reveal readout | `docs/research/judgment-spine/cases/canoo-walmart/reveal_readout_v0.md` | Facilitator-side qualitative comparison against sealed judgments; not scoring or outcome calibration |
| Calibration-gate adversarial review | `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_reveal_readout_calibration_gate_adversarial_artifact_review_v0.md` | Adversarial review of ledger/readout as outcome-calibration inputs; `accept_with_friction` |
| Outcome calibration | `docs/research/judgment-spine/cases/canoo-walmart/outcome_calibration_v0.md` | Qualitative split-axis calibration; no score, validation, or judgment-quality proof |
| JSG-08 reveal/calibration receipt | `docs/research/judgment-spine/cases/canoo-walmart/jsg_08_reveal_calibration_receipt_v0.md` | Companion receipt applying the JSG-08 owner contract; qualitative-only, not scoring or judgment-quality proof |
| Fixture-admission adversarial review | `docs/review-outputs/adversarial-artifact-reviews/canoo_walmart_fixture_admission_scoring_readiness_adversarial_artifact_review_v0.md` | Adversarial review for fixture admission and scoring readiness; admits fixture authoring only |
| Draft v0.14 fixture pack | `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/fixture_authoring_receipt_v0.md` | Docs-only v0.14 fixture-authoring pack; blocked before scoring |

## Missing Residue

No required Canoo/Walmart reveal-sequence artifact is currently missing from this index. A draft v0.14 fixture-authoring pack exists, but it is blocked before scoring. Do not infer that a scoreable fixture, clean harness-format model run, v0.14 scoring admission, or product-proof artifact exists.

Historical source, safety, participant, blind-judgment, pre-reveal, and facilitator-ledger artifacts may still contain creation-time non-claims that later artifacts did not yet exist. Treat those as true for their creation point, not as current inventory. This index defines the current artifact existence state.

Do not reconstruct missing residue from memory. Participant-facing artifacts must be built only from clean pre-cutoff sources and must exclude the definitive agreement announcement, agreement filings, post-cutoff facts, later outcome material, source titles, snippets, URLs, or filenames that leak the actual decision or outcome.

## Use Boundary

Use this case track to test whether a decision-maker should commit to a strategically attractive but counterparty-risky fleet supplier before the public announcement and later outcome are known.

Do not use this case track, source packet, participant packet, blind LLM result, owner-assisted judgment, facilitator ledger, reveal readout, outcome calibration, JSG-08 reveal/calibration receipt, fixture-admission review, or draft v0.14 fixture pack as proof that Orca has judgment quality, that Step A validates the harness, that Canoo/Walmart is participant-ready, or that any clean model run or score exists.

## Non-Claims

- No buyer validation.
- No willingness-to-pay proof.
- No repeatability proof.
- No product readiness.
- No feature readiness.
- No implementation readiness.
- No commercial readiness.
- No model-training readiness.
- No fine-tuning readiness.
- No human clean blind judgment.
- No score-ready v0.14 fixture.
- No proof that TR/Casetext plumbing demonstrates judgment quality.
