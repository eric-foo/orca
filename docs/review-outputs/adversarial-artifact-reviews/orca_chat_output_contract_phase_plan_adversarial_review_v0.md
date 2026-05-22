# Adversarial Review: Orca Chat-Output Contract Phase Plan

```yaml
retrieval_header_version: 1
artifact_role: Review report
scope: Adversarial review of the proposed Orca chat-output contract phase plan before Phase 0 edits begin.
use_when:
  - Checking whether this phase plan is safe to proceed with for Phase 0 preflight.
  - Reviewing findings before Phase 1 patch specifications are written.
authority_boundary: retrieval_only
downstream_consumers:
  - docs/prompts/reviews/orca_chat_output_contract_phase_plan_adversarial_review_prompt_v0.md
stale_if: The accepted phase plan changes, any Phase 1/2 target file is patched, or review-report output-mode contract changes before this report is acted on.
```

- Review prompt:
  `docs/prompts/reviews/orca_chat_output_contract_phase_plan_adversarial_review_prompt_v0.md`
- Output mode: `review-report`
- Edit permission: read-only
- Workspace: `C:\Users\vmon7\Desktop\projects\orca`
- Branch: `main`
- HEAD at review: `fedafb7d60713020e1e628dbf0f484d79501c8d7` (matches prompt preparation commit)
- Dirty-state allowance: dirty state allowed per prompt
- Reviewer model: Claude Sonnet 4.6

---

## 1. Review Target and Source-Read Ledger

**Review target:** The embedded phase plan text in the review prompt. The plan proposes a phased docs-only patch route to add a general chat-output topology rule to Orca: human summary first, agent detail second, compact courier YAML last. The review covers the plan before Phase 0 begins; no files have been patched yet.

**Source-read ledger:**

| Path | Role | Status | Decision supported |
| --- | --- | --- | --- |
| `AGENTS.md` | Orca project authority | Clean (committed) | Overlay authority loaded gate |
| `.agents/workflow-overlay/README.md` | Overlay entrypoint | Modified (M) | Overlay authority loaded gate; dirty source noted |
| `.agents/workflow-overlay/source-of-truth.md` | Source hierarchy | Modified (M) | Conflict-resolution rules |
| `.agents/workflow-overlay/artifact-roles.md` | Role bindings | Modified (M) | Artifact role gate |
| `.agents/workflow-overlay/prompt-orchestration.md` | Output modes, review-report exception | Clean (committed) | Phase 1 target baseline; exception ownership |
| `.agents/workflow-overlay/communication-style.md` | Courier YAML shape, review summary pattern | Clean (committed) | Phase 1 target baseline; topology rule gap |
| `.agents/workflow-overlay/review-lanes.md` | Review lane rules | Modified (M) | Lane binding; dirty source noted |
| `.agents/workflow-overlay/validation-gates.md` | Validation gates | Clean (committed) | Phase 1 target baseline; existing review-report gate |
| `.agents/workflow-overlay/template-registry.md` | Template registry | Untracked (??) | Active template surface classification |
| `.agents/workflow-overlay/retrieval-metadata.md` | Retrieval header contract | Untracked (??) | Retrieval metadata boundary gate |
| `.agents/workflow-overlay/safety-rules.md` | Safety rules | Clean (committed) | Safety constraint check |
| `docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md` | Shared behavior contract | Untracked (??) | Phase 2 target baseline |
| `docs/prompts/templates/review/adversarial_artifact_review_v0.md` | Active review template | Untracked (??) | Phase 2 active surface |
| `docs/prompts/templates/_generic/gpt_5_5_general_prompt_v0.md` | Generic template | Untracked (??) | Phase 2 active surface; topology assessment |
| `docs/prompts/templates/research/o3_evidence_only_research_lane_v0.md` | Research evidence template | Untracked (??) | Phase 2 scope boundary assessment |
| `docs/prompts/templates/research/gpt_5_5_evidence_synthesis_v0.md` | Research synthesis template | Untracked (??) | Phase 2 scope boundary assessment |
| `docs/prompts/templates/wrappers/thin_wrapper_v0.md` | Thin wrapper template | Untracked (??) | Phase 2 active surface |
| `docs/prompts/reviews/orca_review_report_contract_topology_adversarial_review_prompt_v0.md` | Active review prompt | Untracked (??) | Phase 2 active review-report prompt surface |
| `docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md` | Active review prompt | Untracked (??) | Phase 2 active review-report prompt surface |
| `docs/prompts/reviews/core_spine_v0_method_validation_case_frame_locks_adversarial_review_gpt54_prompt_v0.md` | Active review prompt | Untracked (??) | Phase 2 active review-report prompt surface |
| `docs/prompts/hygiene-queue/precompact_orca_review_report_contract_topology.md` | Pre-compact checkpoint | Untracked (??) | Context for prior contract-topology work; not authority |
| `docs/prompts/product-planning/core_spine_v0_method_validation_case_frame_locks_prompt_v0.md` | Active product-planning prompt | Untracked (??) | Final Response pattern baseline |
| `docs/prompts/product-planning/core_spine_v0_method_validation_replay_packet_prompt_v0.md` | Active product-planning prompt | Untracked (??) | Final Response pattern baseline |
| `docs/prompts/reruns/core_spine_v0_method_validation_replay_packet_anti_leakage_rerun_prompt_v0.md` | Active rerun prompt | Untracked (??) | Final Response and non-claims pattern |
| `docs/prompts/wrappers/core_spine_v0_method_validation_fresh_replay_source_loading_wrapper_v0.md` | Active wrapper prompt | Untracked (??) | Non-claims pattern and stale-prompt boundary |
| `docs/prompts/deep-thinking/core_spine_v0_method_validation_case_hunting_prompt_v0.md` | Active deep-thinking prompt | Untracked (??) | chat-only output shape |

**Dirty overlay files relied on:** `.agents/workflow-overlay/README.md`, `.agents/workflow-overlay/review-lanes.md`, `.agents/workflow-overlay/artifact-roles.md`, `.agents/workflow-overlay/source-of-truth.md`, `.agents/workflow-overlay/artifact-folders.md`. These files are modified (M) but the prompt explicitly allows dirty state. None are Phase 1 or Phase 2 targets, so they do not create a target-collision risk. The core overlay authority for this review — `communication-style.md`, `prompt-orchestration.md`, `validation-gates.md` — is clean committed state.

**Untracked sources relied on:** All Phase 2 targets and the majority of active prompt surfaces are untracked. They exist on disk and were readable for this review. Per the prompt's dirty-state allowance, this is acceptable. The untracked status is itself a Phase 0 preflight concern and is flagged below.

---

## 2. Git Status and Dirty Sources

```
## main...origin/main [ahead 12]
M  .agents/workflow-overlay/README.md
M  .agents/workflow-overlay/artifact-folders.md
M  .agents/workflow-overlay/artifact-roles.md
M  .agents/workflow-overlay/review-lanes.md
M  .agents/workflow-overlay/source-of-truth.md
(5 modified overlay files — NOT Phase 1 targets)

?? .agents/workflow-overlay/product-proof.md
?? .agents/workflow-overlay/retrieval-metadata.md
?? .agents/workflow-overlay/template-registry.md
?? docs/prompts/deep-thinking/
?? docs/prompts/product-planning/
?? docs/prompts/reruns/
?? docs/prompts/reviews/orca_chat_output_contract_phase_plan_adversarial_review_prompt_v0.md
?? docs/prompts/templates/  (and all subdirectories)
?? docs/prompts/wrappers/
(multiple untracked prompt families and template directories)
```

**Phase 1 targets (communication-style.md, prompt-orchestration.md, validation-gates.md): all clean (committed in fedafb7). No target collision for Phase 1.**

**Phase 2 targets (docs/prompts/templates/*): all untracked. They exist as working-tree files but are not committed. This requires explicit Phase 0 classification.**

---

## 3. Scope and Excluded Scope

**In scope for this review:**
- Owner topology: does the proposed owner map put the general chat shape, output-mode exceptions, review routing, and closure gate in the right files?
- Phase boundaries: are Phase 1 and Phase 2 the smallest safe split without hiding dependency, rollback, or authority risk?
- Exception boundaries: does the plan preserve the `review-report` saved-report behavior explicitly and without weakening?
- Artifact-receipt distinction: does the plan avoid over-patching compact file-write receipts?
- Human-readable phase plans: does the plan establish the right forward-looking rule for future CA planning outputs?
- Process-key restraint: does the plan avoid adding ritual YAML keys or non-claim blocks?
- Active surface coverage: are the chosen template and prompt surfaces sufficient without broad-syncing stale one-offs?
- Retrieval metadata boundary: do headers remain retrieval-only?
- Leakage: is Orca authority protected from jb policy, GAP/CV Engine paths, lifecycle mechanics?

**Excluded scope:**
- Orca product strategy, product proof, buyer proof, customer discovery, Core Spine validation, method-validation case quality, or external evidence
- Implementation code, tests, runtime architecture, tooling, automation, packages, install/deploy behavior, resolver behavior, or workflow-kernel source
- Patch execution, patch queue preparation, or remediation authorization

---

## 4. Phase-Plan Decision Assessment

**Prior context (from precompact checkpoint):** The review-report contract-topology problem was solved and committed as `fedafb7`. That lane established the artifact-vs-courier boundary, the saved-report exception, and the failed-write failure mode. The current phase plan builds on that foundation by adding a broader human-facing topology rule (human summary first, agent detail second, courier YAML last) that governs decision-bearing chat beyond just the review-report case.

**Owner split assessment:** The proposed owner split is architecturally sound.

- `communication-style.md` owning the general chat rendering rule is correct because that file already governs Orca's human-facing chat shape (readability rules, closeout pattern, courier YAML shape). Adding the ordering rule here is an additive extension of existing scope.
- `prompt-orchestration.md` owning output-mode exceptions is correct because that file already owns the review-report exception in detail (saved-report prerequisite, write-failure behavior, valid YAML-only conditions). Binding other output-mode exceptions here is consistent.
- `validation-gates.md` owning the closure/collision gate is correct because that file already owns the review-report topology gate. A new broader chat-output topology gate belongs in the same file.
- The shared behavior contract pointing to the overlay rule (not duplicating it) is the right abstraction boundary.

**Phase split assessment:** The split between Phase 1 (overlay contract owners) and Phase 2 (shared contract and templates) is the minimal safe division. Phase 1 establishes the authoritative rule; Phase 2 adds pointers and alignments. The dependency is correctly ordered: templates should not be patched before the rule exists in the overlay.

**Frozen decisions assessment:** The five frozen decisions are consistent and internally coherent. Human prose first, compact courier YAML last, review-report exception preserved, no broad stale-sync, no ritual YAML keys. These decisions do not contradict each other.

---

## 5. Correctness Findings

### AR-01 — STEP-01 intent does not require an exceptions pointer in communication-style.md

- **Phase:** Correctness
- **Location:** Phase plan, STEP-01 intent; `communication-style.md` — to-be-patched section
- **Evidence:** STEP-01 intent: "add the general chat-output topology: human summary first, agent detail second, courier YAML last. Include the decision-bearing versus artifact-receipt distinction." No mention of requiring an exceptions pointer to `prompt-orchestration.md` from within the new topology section.
- **Current state:** The existing `communication-style.md` already demonstrates the cross-reference pattern — its Adversarial Review Summary Pattern section explicitly says: "The validity rules for `review-report` output mode, including when YAML-only chat is allowed and what to do when a required durable write fails, are owned by `.agents/workflow-overlay/prompt-orchestration.md`." This pointer is correctly scoped to the review-summary section but does not cover the to-be-written general topology rule.
- **Why it matters:** If STEP-01 adds a general topology rule at the top of `communication-style.md` without an exceptions pointer, an agent loading only `communication-style.md` will see "decision-bearing chat MUST start with human-readable prose" as an absolute rule. The `review-report` YAML-only exception lives in a sibling file. The two files can evolve independently. A future patch to the general rule that strengthens its language (e.g., "always") will implicitly override the exception without technically weakening the exception text. The existing cross-reference in the review-summary section will not rescue this because it is scoped to that section, not to the general topology rule.
- **Failure scenario:** Agent reads communication-style.md, sees general topology rule, flags valid YAML-only review-report chat as a violation, triggers an unnecessary "fix" that adds human prose before the courier YAML summary.
- **Next action (advisory):** Add to STEP-01's intent: "Include an exceptions pointer directing readers to `prompt-orchestration.md` for output-mode exceptions, specifically preserving the `review-report` YAML-only validity condition." This is a one-sentence addition to the new topology section, not a structural change to the phase plan.

---

### AR-02 — `paste-ready-chat` is used in template metadata but is not in prompt-orchestration.md's output modes list

- **Phase:** Correctness
- **Location:** Phase plan, STEP-02 intent; `.agents/workflow-overlay/prompt-orchestration.md` — Output Modes section; template registry entries
- **Evidence:** Current `prompt-orchestration.md` defines four output modes: `chat-only`, `file-write`, `review-report`, `patch-queue`. The template registry lists `paste-ready-chat` as the output mode for five of six active templates (generic, research-evidence, research-synthesis, thin-wrapper, and adversarial-artifact-review when using paste mode). STEP-02 intent proposes to "bind output-mode exceptions: review-report, file-write receipts, paste-ready-chat, chat-only, and patch-queue."
- **Why it matters:** STEP-02 will add `paste-ready-chat` to an exceptions list for a concept that is not yet an officially defined output mode in the canonical output-modes list. This creates an inconsistency: templates declare `paste-ready-chat` as their mode, but the overlay output modes list doesn't define it. An exception for an undefined mode cannot be verified against the mode's semantics. Future agents checking "which output modes require human-summary-first" will find the exception but not the mode definition, and may not be able to determine what constitutes a valid `paste-ready-chat` output.
- **Risk scoping:** This inconsistency pre-exists the phase plan (the template registry already uses `paste-ready-chat`). STEP-02 does not create the inconsistency, but it codifies an exception reference to an undefined mode, making the inconsistency load-bearing.
- **Next action (advisory):** During Phase 0 preflight, classify `paste-ready-chat` as either: (a) a template-metadata label only, not an Orca output mode, in which case STEP-02's exception should refer to it as "template-output paste-ready-chat" with a note that it is a template label, not a prompt-orchestration output mode; or (b) an output mode that should be added to the canonical list in `prompt-orchestration.md` alongside the exception. Either resolution prevents the exception from referencing a ghost term.

---

### AR-03 — Phase 2 template alignment scope does not explicitly exclude already-correct active review-report prompts

- **Phase:** Correctness
- **Location:** Phase plan, STEP-05 intent; Phase 2 allowed changes: "active reusable templates under docs/prompts/templates/"; three active review-report review prompts
- **Evidence:** STEP-05 intent: "align generic, research, wrapper, and review templates where output shape is open-ended or likely to spread the problem. Avoid stale one-offs and already-valid post-artifact receipts." The three active review prompts (`core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md`, `core_spine_v0_method_validation_case_frame_locks_adversarial_review_gpt54_prompt_v0.md`, `orca_review_report_contract_topology_adversarial_review_prompt_v0.md`) all correctly implement the review-report pattern: human value in the durable report, courier YAML in chat, YAML-only valid only after report write.
- **Why it matters:** For `review-report` prompts, adding "human summary first" to chat output would be incorrect: the human-readable value is in the durable report, not in chat. The chat output for these prompts is intentionally compact YAML only (after report write). If an implementer reads "align review templates" and adds human-summary-first instructions to these chat outputs, the patch conflicts with the saved-report exception. The "already-valid" exclusion in STEP-05 is implicit — it applies to "post-artifact receipts" but does not explicitly name correct review-report prompts as excluded.
- **Next action (advisory):** Add a clarifying note to STEP-05: "Do not add human-summary-first instructions to review-report prompts where the human value lives in the durable report; those prompts' chat topology is already correct (compact YAML after report write, per the review-report exception)."

---

## 6. Friction Findings

### AF-01 — Phase 1 stop condition does not guard against implicit contradiction

- **Phase:** Friction
- **Location:** Phase plan, Phase 1 stop condition: "Stop if the saved-report exception becomes weaker or moves away from review-report output-mode ownership."
- **Evidence:** The stop condition is scoped to "exception becomes weaker." It does not address the case where the exception text remains intact but the general rule in `communication-style.md` is written so broadly that it creates an implicit contradiction (not a technical weakening of the exception text).
- **Why it matters:** If AR-01 is not addressed and the general rule is written without an exceptions pointer, a future agent could read `communication-style.md`'s general rule as absolute. The stop condition would not trigger because `prompt-orchestration.md`'s exception text is unchanged. The contradiction lives between files, not within a file.
- **Next action (advisory):** Extend the Phase 1 stop condition to: "Stop if the saved-report exception becomes weaker, moves away from review-report output-mode ownership, or becomes implicitly inconsistent with the general topology rule written in STEP-01."

---

### AF-02 — Phase 3 validation-gates new topology gate scope is unspecified

- **Phase:** Friction
- **Location:** Phase plan, STEP-03 intent: "add a chat-output topology gate for prompt-policy and workflow patches before closure."
- **Evidence:** The existing `validation-gates.md` review-report topology gate checks a long list of specific behavioral properties (owner adjacency, artifact-vs-courier boundary, failed-write fields, no extra YAML keys, retrieval-only metadata, active surface coverage, hygiene handling, non-claims). The plan's new topology gate says only "prompt-policy and workflow patches." The plan does not specify whether this gate will check topology shape (prose before YAML) or enumerate specific YAML keys or process metrics.
- **Why it matters:** The frozen decision says: "Do not include an explicit non_claims YAML block such as files_edited, validation_run, or readiness_claimed unless a specific prompt contract requires it." If the new gate's checklist items enumerate process keys (e.g., "verify no non_claims block of type X"), the gate itself becomes a ritual key list — exactly what the frozen decision prohibits. The protection against this is implicit in the frozen decision but is not bound to the gate's specification.
- **Next action (advisory):** STEP-03 intent should specify that the new topology gate checks topology shape (does the output open with human-readable prose, is YAML compact and last) — not key presence or process metrics. A one-sentence scope note in STEP-03 would bind the frozen decision to the gate implementation.

---

### AF-03 — Research templates have defined structured output shapes that conflict with human-summary-first if applied

- **Phase:** Friction
- **Location:** Phase plan, STEP-05 intent; `docs/prompts/templates/research/o3_evidence_only_research_lane_v0.md`; `docs/prompts/templates/research/gpt_5_5_evidence_synthesis_v0.md`
- **Evidence:** The o3 evidence-only research lane explicitly specifies: "Return a structured table or grouped tables using only the requested fields. Do not add scoring, tiers, recommendations, or synthesis." The synthesis template also returns a structured required-output shape. STEP-05 says "align generic, research, wrapper, and review templates where output shape is open-ended." The qualifier "where output shape is open-ended" would exclude these templates, but the qualifier is implicit — an implementer reading "align research templates" without the qualifier could over-patch these templates.
- **Why it matters:** Adding "human summary first" to the o3 research lane would break its explicit output contract (table output, no synthesis, no prose). This would corrupt the evidence-gathering lane's defined behavior and could cause downstream synthesis to fail when it expects structured data.
- **Next action (advisory):** STEP-05 intent should name the exclusion criterion positively: "Exclude templates where the output shape is explicitly defined as structured data (tables, ledgers, or enumeration lists) rather than decision prose."

---

### AF-04 — Shared behavior contract "Report Shape" compactness guidance is not scoped to field presence

- **Phase:** Friction
- **Location:** Phase plan, STEP-04 intent; `docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md` — Report Shape section
- **Evidence:** Current shared behavior contract Report Shape section: "Prefer compact outputs that preserve: objective; scope and date boundary; source list or source URL table; missing-field labels; blocker states; non-claims; next authorized step." This guidance is about WHAT fields to include, not about ordering. STEP-04 will add a pointer to the overlay-owned topology rule.
- **Why it matters:** After STEP-04, a future author using this contract will see both "prefer compact outputs" and a pointer to "human summary first." Without explicit scoping, these could appear to be in tension. The "prefer compact" guidance is about field presence (include only what's needed), not ordering. But if an author treats "compact" as overriding "human summary first," they might skip the prose opening to be compact.
- **Next action (advisory):** When writing STEP-04, scope the existing "prefer compact" guidance with a parenthetical or adjacent note: "Compactness applies to field selection, not rendering order; see overlay topology rule for ordering."

---

## 7. Not-Proven Boundaries

- **"Agent detail" section naming:** The proposed topology (human summary first, agent detail second, courier YAML last) introduces "agent detail" as a named section type. No current Orca file defines what constitutes "agent detail" as distinct from "human summary." This term may need definition in STEP-01's patch to avoid inconsistent implementation. Not proven that the term is self-explanatory to future implementers.

- **`paste-ready-chat` as output mode:** Whether `paste-ready-chat` belongs in the official prompt-orchestration.md output modes list, or remains a template-metadata label only, is not resolved in the phase plan. This is correctly a Phase 0 classification question. Not proven that either resolution is preferred.

- **Active template scope for Phase 2:** The plan says "active reusable templates under `docs/prompts/templates/`." All templates in that directory are currently untracked (not in git). Whether they count as "active" under the overlay definition of active versus stale is not directly addressed. The template registry's `status: active` entries confirm they are active, but their untracked git state means they have no committed baseline. An implementer editing untracked files is not creating a git diff, which makes Phase 2's gate ("targeted rg/readback confirms...") harder to verify mechanically.

- **Stale one-off classification:** The plan says "avoid stale one-offs." No specific prompts are named as stale. The active prompts in `docs/prompts/product-planning/`, `docs/prompts/deep-thinking/`, and `docs/prompts/reruns/` were not explicitly classified as in-scope or out-of-scope for Phase 2. Their output shapes currently use "Final Response" sections (human-readable bulleted lists) that appear compatible with human-summary-first already. Not proven that any of these require Phase 2 alignment.

---

## 8. Blockers

**No blocking findings.**

The phase plan is structurally sound. The owner split is correct. The phase order is safe. The frozen decisions are internally consistent and do not contradict each other. The three correctness findings (AR-01 through AR-03) identify gaps in the plan's implementation specifications that should be addressed before Phase 1 patch writing begins, but none prevent Phase 0 preflight from proceeding.

The plan is safe to execute Phase 0 (read-only preflight). The correctness findings are advisory implementation guidance for Phase 1 and Phase 2 specifications, not reasons to reject the plan.

---

## 9. Next Authorized Step

**Phase 0 preflight may proceed.** The following items should be explicitly covered during Phase 0 classification before Phase 1 begins:

1. Classify `paste-ready-chat` as either a template-metadata label or an official output mode (AR-02). Record the classification decision before STEP-02 is written.

2. Record that all Phase 2 template targets are untracked. Confirm that the Phase 2 gate ("targeted rg/readback confirms...") accounts for untracked files without a committed baseline.

3. Address AR-01 before STEP-01 is written: add an exceptions pointer requirement to the STEP-01 specification. One sentence suffices.

4. Address AR-03 before STEP-05 is written: add an explicit exclusion note for correct review-report prompts.

5. The five modified overlay files (README.md, artifact-folders.md, artifact-roles.md, review-lanes.md, source-of-truth.md) are not Phase 1 or Phase 2 targets. Phase 0 should confirm they do not create an ownership conflict with the topology rule scope.

---

## 10. Review-Use Boundary

These findings are decision input for the Chief Architect. They are not mandatory remediation unless separately accepted and authorized. The advisory findings (AR-01 through AR-03, AF-01 through AF-04) describe implementation risks and recommended specification additions. None constitute a veto of the plan.

This review does not claim the phase plan is approved, accepted, validated, workflow-ready, merge-safe, product-ready, resolver-ready, implementation-ready, installed, deployed, or committed.

A separately authorized Phase 1 specification and patch execution turn is the next implementation step if the Chief Architect accepts this plan.
