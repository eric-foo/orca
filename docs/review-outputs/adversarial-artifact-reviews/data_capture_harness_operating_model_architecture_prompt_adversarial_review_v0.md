# Data Capture Harness Operating Model Architecture Prompt Adversarial Review v0

```yaml
retrieval_header_version: 1
artifact_role: Review report
scope: Adversarial review of the Data Capture Harness operating-model architecture prompt for structural fitness to launch, with emphasis on the three-subagent requirement, source-loading economy, output contract, and boundary discipline.
use_when:
  - Deciding whether to launch the Data Capture Harness operating-model architecture lane.
  - Checking structural and launch-environment fit of the architecture prompt before use.
authority_boundary: retrieval_only
stale_if:
  - The target prompt is materially revised or superseded.
  - Orca prompt-orchestration, review-lane, or template-registry rules are materially revised.
```

- Review target: `docs/prompts/product-planning/data_capture_harness_operating_model_architecture_prompt_v0.md`
- Review prompt: `docs/prompts/reviews/data_capture_harness_operating_model_architecture_prompt_adversarial_review_prompt_v0.md`
- Report path: `docs/review-outputs/adversarial-artifact-reviews/data_capture_harness_operating_model_architecture_prompt_adversarial_review_v0.md`
- Reviewer: read-only. Patch execution not authorized. Architecture execution not authorized. Source-of-truth promotion not claimed.
- Created: 2026-05-28.

---

## Source Readiness Declaration

`SOURCE_CONTEXT_READY` with dirty/untracked caveats.

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom S3 adversarial review pack
  edit_permission: read-only (review report write under docs/review-outputs/ only)
  target_scope:
    - docs/prompts/product-planning/data_capture_harness_operating_model_architecture_prompt_v0.md
  dirty_state_checked: yes
  blocked_if_missing:
    - AGENTS.md
    - .agents/workflow-overlay/README.md
    - target prompt
```

Method status:
- `workflow-deep-thinking`: REFERENCE-LOADED before source loading; APPLIED after `SOURCE_CONTEXT_READY` to frame the boundary problem, hidden assumptions, prompt failure modes, and decision criteria.
- `workflow-adversarial-artifact-review`: REFERENCE-LOADED before source loading; APPLIED after `SOURCE_CONTEXT_READY` for findings.
- `workflow-architecture-planning`: available as skill; used as reference for understanding the three-subagent requirement structure. Not applied as architecture execution.
- `workflow-prompt-orchestrator`: not read as a separate file; prompt-orchestration overlay loaded as authority for prompt validation gates.

---

## Source-Read Ledger

| Source | Why read | Claim supported | Status |
|---|---|---|---|
| `AGENTS.md` | Orca authority, overlay requirement, docs-only default | Docs-only boundary; no implementation without explicit scope | clean |
| `.agents/workflow-overlay/README.md` | Overlay entrypoint and binding rule | Orca overlay wins for Orca project facts | modified |
| `.agents/workflow-overlay/source-of-truth.md` | Source hierarchy and missing-source rules | No jb or generic authority imported | modified |
| `.agents/workflow-overlay/source-loading.md` | Source-pack economy, capsule budget, preflight rules | Source pack economy check; 4-file budget rule for capsules; new-thread trigger | modified |
| `.agents/workflow-overlay/artifact-roles.md` | Artifact role bindings and permissions | Full prompt artifact role; review report role and destination | modified |
| `.agents/workflow-overlay/retrieval-metadata.md` | Retrieval header contract | Header checks for target prompt and this report | clean |
| `.agents/workflow-overlay/prompt-orchestration.md` | Prompt validation gates, review doctrine, source-gated method contract | Source-gated sequencing check; review prompt doctrine; output mode rules | modified |
| `.agents/workflow-overlay/review-lanes.md` | Review lane rules and doctrine | Adversarial artifact review lane; read-only; report destination | modified |
| `.agents/workflow-overlay/communication-style.md` | Courier YAML shape, review closeout pattern | Report chat shape after durable write | modified |
| `.agents/workflow-overlay/template-registry.md` | Template registry | adversarial-artifact-review template; generic-claude-opus template registration | untracked |
| `docs/prompts/product-planning/data_capture_harness_operating_model_architecture_prompt_v0.md` | Primary review target | All findings; prompt fitness assessment | untracked |
| `docs/prompts/templates/review/adversarial_artifact_review_v0.md` | Template basis for the review prompt | Whether review prompt correctly applies the registered template | git status not checked |
| `docs/prompts/templates/_generic/claude_opus_prompting_best_practices_v0.md` | Template basis for the target prompt | Whether target prompt correctly implements the Opus scaffold | git status not checked |
| `docs/product/data_capture_obligation_baseline_decision_v0.md` | Accepted baseline decision; product context | Whether the prompt is correctly pinned to the accepted baseline; boundary check | untracked |
| `docs/product/data_capture_harness_product_goal_direction_signal_decision_v0.md` | Direction signal demotion decision | Whether the prompt correctly treats the direction signal as advisory only | untracked |
| `docs/product/core_spine_v0_data_capture_spine_obligation_contract_v0.md` | Obligation contract text | Whether the prompt's hard boundaries align with the contract's scope and non-claims | clean |

---

## Dirty / Untracked Source Caveats

All `.agents/workflow-overlay/` sources read for this review are modified in the working tree. The template registry is untracked. The target prompt is untracked. The product-method context sources (baseline decision, direction signal decision) are untracked.

The review prompt explicitly allows dirty and untracked sources for advisory review: "Dirty and untracked prompt/overlay sources are allowed for advisory review. Modified or untracked sources may support advisory findings, but do not claim prompt readiness, validation, approval, acceptance, or source-of-truth promotion from dirty evidence alone."

These caveats apply to advisory findings only. No readiness, acceptance, validation, or source-of-truth promotion is claimed.

---

## Review Boundary And Excluded Scope

**Reviewed:** Structure, launch efficacy, three-subagent requirement executability, source-loading economy, output contract, method sequencing, boundary discipline, internal consistency, and output usefulness of the target prompt as a prompt artifact.

**Not reviewed:** Architecture content (not yet produced); correctness of the obligation contract, baseline decision, or direction signal decisions (owner-accepted; used as boundary context only); ECR, Cleaning, Judgment, or runtime design (out of scope); whether the target artifact path already exists; whether the architecture produced by this prompt would be correct.

**Excluded:** `docs/_inbox/`; method-validation replays; proof-run packets; all product, prompt, and review files not named in the required source list.

---

## Deep-Thinking Frame

Using `workflow-deep-thinking`.

**Real question:** Does the prompt structure give a receiving Claude Opus or agent-enabled architecture lane the best realistic chance of producing a non-fake, boundary-disciplined operating-model architecture — specifically under the hard three-subagent requirement and 15+ file source pack?

**Hidden assumptions in the target prompt:**

1. The receiving environment has agent tooling. The prompt requires three advisory subagents and hard-blocks on `BLOCKED_SUBAGENT_UNAVAILABLE` without providing a self-contained local-fallback path. Claude.ai paste-into-Opus would trigger this block immediately.

2. 15+ file reads won't exhaust effective context before synthesis. The `<required_source_loading>` lists 19 sources across four categories. Even with targeted section reads, this is high context load before the architecture synthesis pass.

3. Each subagent can receive adequate source coverage. The prompt says subagents "must receive the same required source pack, or a bounded source capsule that names every included and excluded source" — but no capsule is defined.

4. A 17-section artifact contract produces synthesis. A model following a detailed section list may fill sections rather than synthesize from evidence. Section 6 "Cartographer Route Consumed" has no synthesis requirement — it mirrors the prompt's own `<cartographer_route>` block.

**Key failure modes:**

- Hard block in paste-into-Opus environments: no subagent tooling → `BLOCKED_SUBAGENT_UNAVAILABLE` → no architecture output.
- Context saturation from 15+ required file reads before synthesis begins.
- Subagents produce under-sourced advisory input due to undefined capsule, making the three-lane synthesis unreliable.
- Section 6 produces mechanical restatement rather than architecture interpretation.
- AO-5 options analysis produces detailed runtime-architecture reasoning before rejection, creating implementation gravity even when the conclusion is "reject."

**Decision criteria for this review:**

1. Can the prompt launch and produce output in its named environments?
2. Is the three-subagent requirement executable with adequate source coverage?
3. Is source loading proportionate and context-safe?
4. Does the output contract drive synthesis or form-filling?
5. Is boundary discipline tight enough to prevent ECR/Cleaning/Judgment/runtime leakage?
6. Are method sequencing, output mode, dirty-state, write path, and non-claims internally consistent?

---

## Findings

Ordered by materiality. `critical`, `major`, `minor` are finding-priority labels only; they are not approval, rejection, readiness, validation, or mandatory-remediation authority.

---

### AR-01 — Launch environment ambiguity: subagent requirement will block in most paste-into-Opus environments

- **Finding id:** AR-01
- **Phase:** correctness
- **Severity:** major
- **Location:** `<required_method_sequence>`, subagent requirement block; `<target_artifact_contract>` Section 4.
- **Issue:** The prompt targets "Claude Opus or another source-grounded architecture-planning lane" and is labeled paste-ready. It requires three advisory subagents and hard-blocks on `BLOCKED_SUBAGENT_UNAVAILABLE` if subagent tooling is unavailable. The only escape hatch is "unless the current launch instruction explicitly authorizes local fallback," but the prompt body defines no local-fallback path, no artifact-section modifications for fallback mode, and no guidance on what constitutes sufficient fallback authorization. In the most common paste-into-Opus environments (Claude.ai, direct API), agent tooling is unavailable.
- **Evidence:** Target prompt: "If subagent tooling is unavailable, rejected, or blocked, return `BLOCKED_SUBAGENT_UNAVAILABLE` or the nearest strict blocker instead of silently substituting local perspectives, unless the current launch instruction explicitly authorizes local fallback." Template basis listed as `generic-claude-opus` (paste-ready-chat), implying paste launch is the primary scenario. `<target_artifact_contract>` Section 4 requires "Subagent source-readiness receipts for all three lanes" and "If any required subagent cannot be launched, record the blocker and do not emit a target architecture."
- **Impact on launch efficacy:** The architecture run produces `BLOCKED_SUBAGENT_UNAVAILABLE` in most paste environments, yielding no architecture output at all. The conservative block prevents fake architecture claims, which is correct in principle. But the prompt provides no self-contained path for a user who adds a fallback authorization to their launch instruction — the artifact sections requiring subagent receipts (Section 4) and conditioning target architecture on subagent launch would still need modification.
- **minimum_closure_condition:** Either (a) the prompt explicitly defines a local-fallback path: what "three local perspectives" replaces in Section 4 and Section 9, what evidence-quality caveats attach, and what the authorization phrase should say; or (b) the prompt body restricts itself explicitly to agent-enabled launch environments and includes a user-facing notice that plain-Opus paste will produce `BLOCKED_SUBAGENT_UNAVAILABLE` with no architecture output.
- **next_authorized_action:** Owner decision on whether to add a self-contained local-fallback path or to restrict the prompt to agent-enabled launch environments. A separately authorized prompt-patching lane may then implement the chosen path.

---

### AR-02 — Subagent source capsule undefined: risks inconsistent or under-sourced advisory input

- **Finding id:** AR-02
- **Phase:** correctness
- **Severity:** major
- **Location:** `<required_method_sequence>`, "Each subagent must receive the same required source pack, or a bounded source capsule that names every included and excluded source."
- **Issue:** The prompt allows subagents to receive "a bounded source capsule" as an alternative to the full source pack, but no capsule is defined anywhere in the prompt. If subagents are launched in environments without filesystem access, or if the main planner assigns them a capsule, there is no defined capsule to include. The three subagents could arrive at advisory input based on different, incomparable source subsets.
- **Evidence:** No source capsule is defined in the target prompt. The full required pack lists 19 files, far exceeding the source-loading.md 4-file capsule budget and the "at most eight targeted section reads" limit. source-loading.md states: "If more than four target artifacts appear necessary, switch to a source capsule or new-thread handoff instead of bulk-reading."
- **Impact on source grounding:** Subagents may use different source subsets, making directional, adversarial, and grounding advisory inputs incomparable. Or subagents without filesystem access return `SOURCE_CONTEXT_INCOMPLETE`, blocking the main planner. The three-subagent evidence mode may then produce architecture input of inconsistent or unknown quality, which the self-check ("claiming standard three-subagent evidence when the directional, adversarial, and grounding subagents were not actually launched") would flag but not prevent.
- **minimum_closure_condition:** The prompt defines a bounded source capsule for subagent use that names at minimum: the obligation contract (`core_spine_v0_data_capture_spine_obligation_contract_v0.md`), the baseline decision (`data_capture_obligation_baseline_decision_v0.md`), the direction signal decision (`data_capture_harness_product_goal_direction_signal_decision_v0.md`), and the data/cleaning boundary note. The capsule must list included and excluded files and stay within source-loading.md capsule budget rules.
- **next_authorized_action:** Patch the target prompt to add a defined source capsule under `<required_method_sequence>` for subagent or local-perspective use.

---

### AR-03 — Required source pack exceeds source-loading.md economy limits

- **Finding id:** AR-03
- **Phase:** friction
- **Severity:** major
- **Location:** `<required_source_loading>` section.
- **Issue:** The required source pack lists 19 files (8 control/operating, 3 product-method, 4 boundary/product, 4 pressure/review evidence) as required before answering. This far exceeds source-loading.md's "at most four full-file reads" rule and triggers the "switch to a source capsule or new-thread handoff" rule when more than four target artifacts are necessary.
- **Evidence:** source-loading.md: "Use at most four full-file reads" and "If more than four target artifacts appear necessary, switch to a source capsule or new-thread handoff instead of bulk-reading." The `<required_source_loading>` lists 15+ required files with no tiering between core and conditional expansion. Even the "optional expansion" category adds 4 more files.
- **Impact on output usefulness:** Context load before the architecture synthesis pass reduces effective context available for three-subagent synthesis. A model that reads all required files before applying `workflow-architecture-planning` has less effective synthesis context than one that reads a core pack of 4-6 files and expands only on identified source gaps. This is a friction issue that directly affects architecture output quality.
- **minimum_closure_condition:** The `<required_source_loading>` is tiered into a core pack (4-6 most controlling files, required before any answering) and a conditional expansion list (expand only when a specific source gap is identified). Or the prompt adopts a formal source capsule with excerpts per source-loading.md capsule budget.
- **next_authorized_action:** Patch `<required_source_loading>` to identify a minimal core read pack and demote remaining sources to conditional expansion.

---

### AR-04 — Section 6 "Cartographer Route Consumed" invites mechanical restatement rather than synthesis

- **Finding id:** AR-04
- **Phase:** friction
- **Severity:** minor
- **Location:** `<target_artifact_contract>`, item 6, "Cartographer Route Consumed."
- **Issue:** The artifact must include a section covering "Boundary, goal, starting point, route shape, checkpoints, forks/handoff signals" — all of which are given verbatim in the prompt's `<cartographer_route>` section. The section requires field-for-field transcription, not architecture synthesis or interpretation.
- **Evidence:** The `<cartographer_route>` and artifact Section 6 describe identical fields. No transformation, synthesis, or architecture-judgment application is required of the receiver.
- **Impact on output usefulness:** Produces artifact bloat and may anchor the receiver to the prompt's framing rather than encouraging synthesis from loaded sources. A model following the 17-section contract may treat Section 6 as a copy-paste task, establishing a form-filling posture for the subsequent synthesis sections.
- **minimum_closure_condition:** Section 6 is revised to require a brief summary (2-4 bullets) of how the cartographer route shaped the specific architectural choices made in the artifact — not a field-for-field restatement of the route.
- **next_authorized_action:** Patch Section 6 in `<target_artifact_contract>`.

---

### AR-05 — AO-5 runtime/tooling option may produce implementation gravity in options analysis

- **Finding id:** AR-05
- **Phase:** friction
- **Severity:** minor
- **Location:** `<options_to_consider>`, AO-5 "Runtime/tooling-first harness."
- **Issue:** AO-5 is listed as a candidate for the options analysis. The decision criteria and hard boundaries clearly prohibit runtime/tooling architecture, but listing it as a named option invites detailed analysis before rejection. A model that analyzes all six options in parallel may produce implementation-gravity reasoning in the "Options Compared" artifact section even when the conclusion is rejection.
- **Evidence:** `<options_to_consider>` preamble: "Treat these as candidates, not defaults." `<decision_criteria>`: "It stays future-runtime-aware only as deferred implications, not runtime authorization." `<hard_boundaries>`: prohibit runtime, tooling, source systems, scrapers, APIs, etc. The self-check ("treating the operating model as a runtime/tooling architecture") acts after the analysis rather than before it.
- **Impact on boundary control:** Minor risk that the architecture artifact's "Options Compared" section includes runtime-design reasoning. The self-check and hard boundaries counterbalance this, but at the cost of having produced the boundary-adjacent reasoning first.
- **minimum_closure_condition:** AO-5 is either removed and replaced with a note ("Runtime/tooling-first: fast-rejected under current commission; not analyzed"), or a fast-reject instruction is added to `<options_to_consider>` directing boundary-violating options to be dismissed without detailed analysis.
- **next_authorized_action:** Patch AO-5 in `<options_to_consider>` or add a fast-reject instruction to the section preamble.

---

## Non-Findings That Matter

- **Method sequencing is correct.** The `<required_method_sequence>` correctly follows: REFERENCE-LOAD both methods → do not apply → SOURCE-LOAD → declare SOURCE_CONTEXT_READY → APPLY deep-thinking → APPLY architecture-planning. This matches the source-gated method contract in prompt-orchestration.md.

- **Output mode and write path are explicit and matched.** `file-write` is the named mode. `docs/product/data_capture_harness_operating_model_architecture_v0.md` is the named destination. The `<chat_closeout_contract>` is well-formed and includes path, result, subagent receipt, gaps, next step, and implementation non-claim.

- **Boundary prohibitions are comprehensive.** `<hard_boundaries>` explicitly prohibits patching the obligation contract, ECR schema, Cleaning, Judgment, source systems, scrapers, APIs, dashboards, storage, schemas, tests, packages, runtime services, deployment, commits, pushes, PRs, and validation/readiness/buyer-proof/implementation-authority claims. `<operating_mode>` reinforces these prohibitions at the opening.

- **Self-check covers the most dangerous failure modes.** The `<self_check>` explicitly guards against "claiming standard three-subagent evidence when the directional, adversarial, and grounding subagents were not actually launched" and "producing a generic operating model that does not pin to the accepted obligation baseline." These are the two most likely synthesis failures.

- **Decision criteria are well-calibrated to the commission.** The nine decision criteria correctly emphasize obligation-baseline exercise without mutation, layer discipline, failure-state visibility, raw-observable preservation, source-family satellite discipline, rejection of fake-success signals (source volume, checklist completion, review theater), and future-runtime-awareness as deferred implication only.

- **Retrieval header is correct.** The target prompt has a retrieval header with `retrieval_only` authority boundary, relevant `open_next` files, and `stale_if` conditions tied to the controlled sources. No forbidden header fields.

- **Goal handoff and thread operating target are correctly formed.** `thread_operating_target.lifecycle_status` is `active_thread_local`; the drift guard explicitly prohibits runtime/tooling substitution; `conflict_behavior: call_out_conflict_before_proceeding` is correct.

- **Dirty-state allowance is explicitly stated.** The `<repo_preflight>` allows dirty and untracked sources with the correct non-claim framing.

- **The target prompt does not leak into product-proof, buyer-proof, or commercial-readiness claims.** The non-implementation boundaries are stated multiple times across the prompt body.

- **No jb policy or lifecycle mechanics are imported.** The `<orca_authority>` block explicitly prohibits jb rules, paths, lifecycle mechanics, product policy, validation habits, model lanes, review labels, handoff rules, and artifact roles. None appear in the prompt body.

---

## Not-Proven Boundaries

- Whether the target prompt path already exists (not checked; not in scope for this review).
- Whether any required source file is stale relative to the review date (not verified beyond session git status).
- Whether `workflow-architecture-planning` is executable in the target launch environment (available as a skill in Claude Code; behavior in plain-Opus paste is not verified).
- Whether the three-subagent advisory synthesis would produce a meaningfully better architecture than a single well-sourced local analysis (architecture quality claim; not provable by this review).
- Whether the 17-section artifact structure produces synthesis vs. form-filling in practice (depends on model behavior and source quality under load).
- Whether the obligation contract, baseline decision, and direction signal decision are fresh as of 2026-05-28 (treated as current per their untracked status and the owner-accepted decision recorded in the baseline decision artifact).

---

## Advisory Recommendation

`patch_before_launch`

The prompt is structurally sound in its method sequencing, output mode, write path, boundary prohibitions, decision criteria, self-check, and overall architecture-planning scope. The three-subagent requirement is clearly specified and internally consistent. No ECR, Cleaning, Judgment, runtime, or implementation leakage is present in the prompt body.

Three material issues limit launch efficacy:

**AR-01** (major, correctness): The prompt will produce `BLOCKED_SUBAGENT_UNAVAILABLE` in most paste-into-Opus environments. The local-fallback escape hatch exists but is undefined — the user cannot reliably add a fallback authorization without knowing what the prompt expects in return. This is the highest-priority fix because it determines whether the architecture lane can launch at all outside Claude Code.

**AR-02** (major, correctness): The subagent source capsule is undefined. If subagents or local perspectives lack filesystem access, there is no defined capsule for them to use. This leaves the evidence quality of the three-lane synthesis undefined.

**AR-03** (major, friction): The source pack exceeds source-loading.md economy limits. The full required list creates context-bloat risk before the architecture synthesis pass, reducing effective synthesis quality.

Two minor friction issues (AR-04, AR-05) are correctable but do not block launch.

A full split into separate agent-enabled and plain-Opus versions is not required if: (a) a local-fallback path is clearly defined in the prompt, and (b) the source pack is tiered. The fundamental architecture question, decision criteria, hard boundaries, and output contract do not change between agent-enabled and local-fallback modes.

---

## Smallest Next Authorized Step

The owner or a separately authorized prompt-patching lane should address the following in order:

1. Decide whether the prompt will support a local-fallback authorization path or restrict to agent-enabled environments only. This decision determines the shape of the patch for AR-01.

2. If local fallback is authorized, patch Section 4 of `<target_artifact_contract>` to define what "local perspective receipts" replace "subagent receipts" and what evidence-quality caveats attach to local-fallback runs.

3. Define a bounded source capsule for subagent or local-perspective use (AR-02), covering the 4-6 most controlling files from the full pack, with explicit included/excluded lists honoring source-loading.md capsule budget.

4. Tier the `<required_source_loading>` section into core (required before any answering) and conditional expansion (expand only if source gap identified), to address AR-03.

5. Optionally patch AR-04 (Section 6 restatement → brief summary of route-shaped decisions) and AR-05 (AO-5 fast-reject instruction).

No new overlay decisions, new architecture lanes, or implementation authority are required for these patches.

---

## Review-Use Boundary

This is a read-only adversarial artifact review. Findings are decision input for the owner or a separately authorized prompt-patching lane. They are not approval, validation, readiness, mandatory remediation, patch authority, architecture execution, or implementation authority. The advisory recommendation is a reviewer summary; it does not constitute acceptance, rejection, or lifecycle closure of the target prompt.
