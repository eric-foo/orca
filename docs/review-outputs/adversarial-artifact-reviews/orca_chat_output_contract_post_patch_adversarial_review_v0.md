# Adversarial Review: Orca Chat-Output Contract Post-Patch Diff

```yaml
retrieval_header_version: 1
artifact_role: Review report
scope: Adversarial review of the completed Orca chat-output contract Phase 1/2 patch set against the accepted phase plan and prior review findings.
use_when:
  - Checking whether the Phase 1/2 patch set correctly establishes the chat-output topology before any subsequent overlay or template work.
  - Reviewing prior findings remediation before accepting the patch set.
authority_boundary: retrieval_only
input_hashes:
  review_prompt: docs/prompts/reviews/orca_chat_output_contract_post_patch_adversarial_review_prompt_v0.md
  phase_plan_review: docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_phase_plan_adversarial_review_v0.md
branch_or_commit: main @ fedafb7d60713020e1e628dbf0f484d79501c8d7 (with working-tree patch set)
downstream_consumers:
  - docs/prompts/reviews/orca_chat_output_contract_post_patch_adversarial_review_prompt_v0.md
stale_if: Any Phase 1 or Phase 2 target file is further modified, chat-output contract ownership changes, or review-report output-mode contract changes before this report is acted on.
```

- Review prompt: `docs/prompts/reviews/orca_chat_output_contract_post_patch_adversarial_review_prompt_v0.md`
- Output mode: `review-report`
- Edit permission: read-only
- Workspace: `C:\Users\vmon7\Desktop\projects\orca`
- Branch: `main`
- HEAD at review: `fedafb7d60713020e1e628dbf0f484d79501c8d7` (with working-tree patch set applied but not committed)
- Dirty-state allowance: dirty state allowed per prompt; Phase 2 untracked templates treated as in-scope target artifacts
- Reviewer model: Claude Sonnet 4.6
- Deep-thinking: invoked; topology risk framing completed before source reads
- Adversarial-artifact-review: invoked; strict formal review mode — overlay authority fully bound

---

## 1. Review Target and Source-Read Ledger

**Review target:** The completed working-tree patch set for the Orca chat-output contract, covering Phase 1 overlay owners (three modified M files plus one modified template file) and Phase 2 reusable templates (five new untracked ?? files).

**Phase 1 targets (modified M in working tree):**
- `.agents/workflow-overlay/communication-style.md` — adds "Chat Output Topology" section
- `.agents/workflow-overlay/prompt-orchestration.md` — adds `paste-ready-chat` mode definition and output-mode exceptions block
- `.agents/workflow-overlay/validation-gates.md` — adds "Chat-output topology gate" as a collision gate
- `docs/prompts/templates/review/adversarial_artifact_review_v0.md` — adds `paste-ready-chat` guidance block

**Phase 2 targets (new, untracked ??):**
- `docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md`
- `docs/prompts/templates/_generic/gpt_5_5_general_prompt_v0.md`
- `docs/prompts/templates/research/o3_evidence_only_research_lane_v0.md`
- `docs/prompts/templates/research/gpt_5_5_evidence_synthesis_v0.md`
- `docs/prompts/templates/wrappers/thin_wrapper_v0.md`

**Source-read ledger:**

| Path | Role | Status | Decision supported |
| --- | --- | --- | --- |
| `AGENTS.md` | Orca project authority | Clean (committed) | Overlay authority gate |
| `.agents/workflow-overlay/README.md` | Overlay entrypoint | Modified (M) | Overlay binding; dirty source noted |
| `.agents/workflow-overlay/source-of-truth.md` | Source hierarchy | Modified (M) | Conflict-resolution rules; dirty source noted |
| `.agents/workflow-overlay/artifact-roles.md` | Role bindings | Modified (M) | Artifact role gate; dirty source noted |
| `.agents/workflow-overlay/communication-style.md` | Chat topology, courier YAML shape | Modified (M) — Phase 1 target | General rule and pointer placement |
| `.agents/workflow-overlay/prompt-orchestration.md` | Output modes, review-report exception | Modified (M) — Phase 1 target | Exception ownership, paste-ready-chat definition |
| `.agents/workflow-overlay/validation-gates.md` | Validation gates | Modified (M) — Phase 1 target | Collision gate correctness |
| `.agents/workflow-overlay/review-lanes.md` | Review lane rules | Modified (M) | Lane binding; dirty source noted |
| `.agents/workflow-overlay/template-registry.md` | Template registry | Untracked (??) | Template active-status classification |
| `.agents/workflow-overlay/retrieval-metadata.md` | Retrieval header contract | Untracked (??) | Retrieval metadata boundary gate |
| `.agents/workflow-overlay/safety-rules.md` | Safety rules | Clean (committed) | Safety constraint check |
| `docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md` | Shared behavior contract | Untracked (??) — Phase 2 target | Pointer placement, compactness scoping |
| `docs/prompts/templates/_generic/gpt_5_5_general_prompt_v0.md` | Generic GPT-5.5 template | Untracked (??) — Phase 2 target | Decision-bearing topology in template body |
| `docs/prompts/templates/research/o3_evidence_only_research_lane_v0.md` | Research evidence template | Untracked (??) — Phase 2 target | Task-native exemption correctness |
| `docs/prompts/templates/research/gpt_5_5_evidence_synthesis_v0.md` | Research synthesis template | Untracked (??) — Phase 2 target | Structured-artifact branch correctness |
| `docs/prompts/templates/wrappers/thin_wrapper_v0.md` | Thin wrapper template | Untracked (??) — Phase 2 target | CA/planning prose requirement |
| `docs/prompts/templates/review/adversarial_artifact_review_v0.md` | Active review template | Modified (M) — Phase 1 target | paste-ready-chat guidance block correctness |
| `docs/prompts/reviews/orca_chat_output_contract_phase_plan_adversarial_review_prompt_v0.md` | Prior review prompt | Untracked (??) | Phase plan context (not authority) |
| `docs/review-outputs/adversarial-artifact-reviews/orca_chat_output_contract_phase_plan_adversarial_review_v0.md` | Prior review report | Untracked (??) | Prior findings baseline |
| `docs/prompts/hygiene-queue/precompact_orca_chat_output_contract.md` | Hygiene queue context | Untracked (??) | Pre-compact context (not authority) |

**Dirty overlay files relied on for authority:** `.agents/workflow-overlay/README.md`, `.agents/workflow-overlay/source-of-truth.md`, `.agents/workflow-overlay/artifact-roles.md`, `.agents/workflow-overlay/review-lanes.md`. All are modified (M) but none are Phase 1 or Phase 2 targets; none create target collision. The dirty-state allowance explicitly permits this. Authority reads from these files are noted as coming from modified working-tree state.

**Untracked files relied on as Phase 2 targets:** Per the prompt's dirty-state allowance, all five Phase 2 templates are classified as in-scope target artifacts despite being untracked. They exist on disk and were read directly.

---

## 2. Git Status and Target Dirty-State Classification

```
## main...origin/main [ahead 12]

Phase 1 targets (modified M — patch set applied):
 M .agents/workflow-overlay/communication-style.md
 M .agents/workflow-overlay/prompt-orchestration.md
 M .agents/workflow-overlay/validation-gates.md
 M docs/prompts/templates/review/adversarial_artifact_review_v0.md

Non-target modified overlay files (not Phase 1 or Phase 2 targets):
 M .agents/workflow-overlay/README.md
 M .agents/workflow-overlay/artifact-folders.md
 M .agents/workflow-overlay/artifact-roles.md
 M .agents/workflow-overlay/review-lanes.md
 M .agents/workflow-overlay/source-of-truth.md
 M docs/README.md
 M docs/STRUCTURE.md
 M docs/decisions/turn_08_product_thesis_v0.md
 M docs/product/README.md
 M docs/product/core_spine_v0_product_contract.md
 M docs/prompts/README.md
 M docs/review-outputs/README.md

Phase 2 targets (untracked ?? — new files, no committed baseline):
?? docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md
?? docs/prompts/templates/_generic/gpt_5_5_general_prompt_v0.md
?? docs/prompts/templates/research/o3_evidence_only_research_lane_v0.md
?? docs/prompts/templates/research/gpt_5_5_evidence_synthesis_v0.md
?? docs/prompts/templates/wrappers/thin_wrapper_v0.md

Broad unrelated dirty state (excluded per prompt):
?? docs/_inbox/, docs/product/ (multiple files), docs/prompts/product-planning/,
   docs/prompts/deep-thinking/, docs/prompts/reruns/, docs/prompts/wrappers/,
   docs/research/, docs/review-outputs/method-validation/, and others
```

**Target isolation:** Phase 1 target files are isolated from unrelated dirty work. Phase 2 target files are new untracked files in `docs/prompts/templates/`, distinct from the unrelated untracked work in other directories. No target collision found.

---

## 3. Scope and Excluded Scope

**In scope:**
- Owner topology: whether communication-style.md, prompt-orchestration.md, and validation-gates.md correctly partition ownership of the general rule, output-mode exceptions, and collision gate.
- Exception adjacency: whether communication-style.md points to prompt-orchestration.md for output-mode exceptions without enumerating them inline.
- `review-report` preservation: whether YAML-only chat remains tied to successful durable report writes; whether failed writes use the correct fallback fields.
- `paste-ready-chat` classification: whether the mode is formalized without allowing CA/planning/scoping/phase-gate decisions to become machine-only prompt bodies.
- `file-write` receipts: whether compact receipts remain valid only when the durable artifact carries the human value.
- Research templates: whether evidence-only tables and structured synthesis outputs remain task-native and are not naively forced into human-summary-first.
- Template propagation: whether Phase 2 templates inherit the owner rule narrowly and whether already-correct active review-report prompts are excluded from broad sync.
- Process-key restraint: whether no extra courier keys, explicit `non_claims` YAML fields, or `files_edited` / `validation_run` / `readiness_claimed` keys were added.
- Retrieval metadata boundary: whether retrieval headers remain retrieval-only.
- Prior finding remediation: whether the patch set resolves AR-01, AR-02, AR-03, AF-01, AF-02, AF-03, and AF-04.
- Leakage: whether no `jb` project policy or GAP/CV Engine paths appear.

**Excluded scope:** Orca product strategy, product proof, buyer proof, customer discovery, Core Spine validation, method-validation case quality, external evidence, implementation code, tests, runtime architecture, tooling, automation, packages, install/deploy behavior, resolver behavior, workflow-kernel source, patch queue preparation, patch execution.

---

## 4. Prompt Validation Gate Results

| Gate | Result | Evidence |
| --- | --- | --- |
| Overlay authority loaded | PASS | AGENTS.md and .agents/workflow-overlay/README.md read |
| Artifact roles bound | PASS | Review prompt and review report roles in artifact-roles.md |
| Source resolution clean | PASS | No jb policy imported; installed skills are runtime copies |
| Worktree preflight present | PASS | Workspace, branch, HEAD, dirty-state allowance, targets, edit permission, report destination all stated |
| Output mode explicit | PASS | Exactly one: `review-report` |
| Chat-output topology gate | PASS | New gate present and correctly scoped as collision gate in validation-gates.md |
| Review-report topology gate | PASS | Gate present in validation-gates.md; exception adjacency checked |
| Retrieval metadata bounded | PASS | All retrieval headers use `authority_boundary: retrieval_only` |
| Leakage gate | PASS | No jb templates, GAP/CV Engine paths, handoff rules, or lifecycle mechanics found |

---

## 5. Prior Friction Remediation Assessment

### AR-01 — STEP-01 needed an exceptions pointer in communication-style.md

**Status: RESOLVED**

The new "Chat Output Topology" section in `communication-style.md` includes: "This file owns the general chat shape and exact courier YAML shapes it defines. Output-mode exceptions, including when `review-report` may use YAML-only chat, when `file-write` may return compact artifact receipts, and how `paste-ready-chat` behaves, are owned by `.agents/workflow-overlay/prompt-orchestration.md`."

This is a forward pointer to the owning file, not an inline exception enumeration. The pointer names the exceptions for readability and immediately delegates authority to prompt-orchestration.md. An agent loading only communication-style.md now receives explicit direction to read prompt-orchestration.md for exceptions, preventing the general rule from being read as absolute.

### AR-02 — paste-ready-chat was used in template metadata but not listed in prompt-orchestration.md output modes

**Status: RESOLVED**

The patch adds `paste-ready-chat` in three locations in `prompt-orchestration.md`:
1. In the Supported Prompt Families table (footnote: "Prompt templates may also use `paste-ready-chat`...").
2. In the Required Preflight Fields list (output mode enumeration now includes `paste-ready-chat`).
3. In the Output Modes section as a defined mode with explicit semantics ("return one prompt, wrapper, handoff, or review request body in chat for copying...") and a content constraint ("Do not use this mode to hide a Chief Architect, planning, scoping, phase-gate, or completion decision inside machine-only structure").

`paste-ready-chat` is now an officially defined Orca output mode, consistent with its use in the template registry.

### AR-03 — Phase 2 needed to exclude already-correct active review-report prompts from broad sync

**Status: RESOLVED via scope exclusion**

The Phase 2 target set is restricted to `docs/prompts/templates/` — the reusable template files. The active review-report prompts (e.g., `core_spine_v0_*` review prompts) live in `docs/prompts/reviews/` and were not touched by the patch set. No broad-sync of those prompts occurred.

Additionally, the new chat-output topology gate in `validation-gates.md` explicitly states: "already-correct active `review-report` prompts and stale one-offs must not be broad-synced." This makes the non-broad-sync rule a checkable gate condition, not just a comment. Resolution is structural (scope exclusion) plus prospective (gate-enforced rule for future propagation).

### AF-01 — Phase 1 needed to guard against implicit contradiction between the general rule and the exception

**Status: RESOLVED**

The patch creates a mutual ownership pointer pattern between the two files:
- `communication-style.md` points to `prompt-orchestration.md` for output-mode exceptions.
- `prompt-orchestration.md` adds: "The general human-summary / agent-detail / courier-YAML chat shape is owned by `.agents/workflow-overlay/communication-style.md`. This file owns output-mode exceptions to that shape."

An agent reading either file in isolation will encounter both the rule and a pointer to the other file's authority. An implicit contradiction — where the general rule could override the exception by being read as absolute — is prevented by the explicit ownership declaration and cross-reference in both files.

### AF-02 — New validation gate needed to be collision-focused, not a ritual key checklist

**Status: RESOLVED**

The new gate is explicitly labeled: "This is a collision gate, not a required-key checklist." It then lists behavioral properties to check (prose-first decision chat, separate agent detail, compact YAML last, review-report exception tied to durable writes, file-write receipts scoped to durable artifact, paste-ready-chat classified, task-native tables not rewritten, no broad-sync of correct prompts, no ritual fields). The gate checks output behavior, not field presence. No ritual YAML keys appear in the gate description.

### AF-03 — Research templates have structured output shapes that could conflict with naive human-summary-first patching

**Status: RESOLVED**

`o3_evidence_only_research_lane_v0.md` includes an explicit task-native exemption clause in its template body: "This evidence table is the task-native artifact shape. Do not add a human decision summary, agent-detail section, or courier YAML unless the launch instruction separately asks for routing context; if it does, keep that context brief and outside the evidence table."

`gpt_5_5_evidence_synthesis_v0.md` correctly distinguishes the two cases: "If the synthesis produces a decision, recommendation, or routing result, start with a human-readable summary before detailed evidence tables or classifications. If the required output is a structured artifact, preserve that structure and use compact routing YAML only at the end when requested or required."

Both templates preserve their task-native output shape and apply human-summary-first only when the output is decision-bearing, not when it is a structured evidence artifact.

### AF-04 — Shared behavior contract compactness guidance needed scoping to field presence, not YAML-only output

**Status: RESOLVED**

The shared behavior contract's Report Shape section now reads: "Compactness means omit unnecessary fields and full source echoes. It does not mean hiding a decision-bearing answer in YAML-only or agent-only structure. Artifact-native tables, paste-ready prompt bodies, and post-artifact receipts remain valid when the output mode permits them."

This directly scopes "compact" to field selection, not rendering order, and explicitly allows the topology rule to govern ordering for decision-bearing outputs.

---

## 6. Contract-Topology Decision Assessment

The patch set establishes this topology:

| Output mode | Human chat shape | YAML position | Human-value location |
| --- | --- | --- | --- |
| Default (decision-bearing) | Human summary first; agent detail second; courier YAML compact and last | Last | Chat |
| `review-report` (successful write) | YAML courier only | Only | Durable report file |
| `review-report` (failed write) | Human-readable routing detail; no `report_path`; `status: failed`; `recommendation: blocked` | None | Chat (fallback) |
| `paste-ready-chat` | Paste-ready body is deliverable; CA/planning/routing decisions remain human-readable | Inline or none | Task-native body or label |
| `file-write` receipt | Compact path/hash/status | Inline or last | Durable artifact |
| Task-native research table | Structured table; no human-summary-first prose; no agent-detail section unless launch instruction asks | None by default | Table itself |

**Owner topology:**
- `communication-style.md` owns the general rule and courier YAML shapes. Does not enumerate exceptions inline.
- `prompt-orchestration.md` owns exception definitions and write-failure behavior. Explicitly names all four exception modes.
- `validation-gates.md` owns the collision gate — behavioral check that exceptions do not silently conflict with the general rule.

This partition is correctly implemented in the patch set.

---

## 7. Correctness Findings

**No blocking correctness findings.**

The five correctness claims from the deep-thinking phase are all satisfied:

1. `communication-style.md` states the general rule with a forward pointer to `prompt-orchestration.md` — no inline exception list. ✓
2. `prompt-orchestration.md` names `paste-ready-chat` with an explicit content constraint — the mode is not just classified, its loophole is closed. ✓
3. `validation-gates.md` implements a collision detector — explicitly labeled as such, checking behavior not key presence. ✓
4. Phase 2 templates propagate narrowly — research templates preserve task-native shape with explicit exemption clauses; no review-report prompts were broad-synced. ✓
5. No ritual YAML keys (`non_claims`, `files_edited`, `validation_run`, `readiness_claimed`) were added anywhere in the patch set. ✓

---

## 8. Friction Findings

### FF-01 — AR-03 resolution depends on future authors checking the gate before extending Phase 2 scope

- **Phase:** Friction
- **Location:** `.agents/workflow-overlay/validation-gates.md` — Chat-output topology gate; Phase 2 scope boundary
- **Evidence:** The gate says "already-correct active `review-report` prompts and stale one-offs must not be broad-synced." AR-03 was resolved by restricting Phase 2 targets to `docs/prompts/templates/` rather than by explicitly labeling which specific active review-report prompts are already correct.
- **Why it matters:** A future author extending Phase 2 scope (e.g., adding a new template category that includes prompts from `docs/prompts/reviews/`) would need to check the gate and apply their own judgment about which prompts are "already correct." The gate is correctly worded and is the right mechanism, but it is retrospective (checks whether broad-sync happened) rather than prospective (guides an author deciding scope). If the template folder boundary is not maintained, the protection weakens to gate-enforcement alone.
- **Next action (advisory):** No change required to the current patch set — the gate is correctly written. If Phase 2 scope is later extended, the Chief Architect should explicitly classify which active review-report prompts are already correct at that time. The gate will catch violations retrospectively; the scope classification will prevent them prospectively.

---

### FF-02 — "Stage-native output contract" is an undefined term in communication-style.md

- **Phase:** Friction
- **Location:** `.agents/workflow-overlay/communication-style.md` — Chat Output Topology section, courier YAML paragraph
- **Evidence:** "Courier YAML is routable state, not the decision or report itself. It should stay compact and appear last unless a stage-native output contract explicitly requires YAML-first or YAML-only chat."
- **Why it matters:** The term "stage-native output contract" appears only in this one location across the entire overlay. The preferred term elsewhere in the patch set — including in `prompt-orchestration.md` and `validation-gates.md` — is "output-mode exception" or "stage-native exception." "Stage-native output contract" could be interpreted as permitting individual pipeline stages to define their own output-shape overrides without going through `prompt-orchestration.md`. The forward pointer two paragraphs later constrains this interpretation, but the terminology inconsistency creates a minor ambiguity for future authors who read the courier YAML sentence in isolation.
- **Next action (advisory):** Consider replacing "stage-native output contract" with "output-mode exception" or "stage-native exception" to align with the terminology used in `prompt-orchestration.md` and `validation-gates.md`. This is a one-phrase edit with no structural consequence.

---

## 9. Not-Proven Boundaries

- **"Stage-native output contract" interpretation:** Not proven that future authors will read this term as synonymous with "output-mode exception owned by prompt-orchestration.md" without also reading the forward pointer. The forward pointer mitigates the risk; the term itself is non-standard.

- **Evidence synthesis template structured-artifact branch:** `gpt_5_5_evidence_synthesis_v0.md` says "If the required output is a structured artifact, preserve that structure..." The determination of whether an output is "structured" depends on the launch instruction being clear. Not proven that all instantiations of this template will provide launch instructions explicit enough to trigger the correct branch. The two-branch structure is correct; the branch trigger is launch-instruction-dependent.

- **paste-ready-chat "different chat-only shape" in adversarial_artifact_review_v0.md:** The new clause says "unless the launch instruction binds a different chat-only shape." Not proven what constitutes a valid "different shape" in practice. No examples are given; the clause is a hook for future launch instructions to customize, but the customization boundary is not defined.

- **Active template git status:** All Phase 2 templates are untracked (not committed). Their template registry entries show `status: active`, but the absence of a committed baseline means future diffs cannot mechanically identify Phase 2 changes. This is a pre-existing workspace state; the prompt's dirty-state allowance accounts for it.

---

## 10. Blockers

**No blocking findings.**

The patch set is structurally correct. All five correctness claims are satisfied. All seven prior findings (AR-01 through AR-03, AF-01 through AF-04) are resolved. The two friction findings (FF-01, FF-02) identify minor risks that do not prevent the topology from functioning as designed.

---

## 11. Next Authorized Step

The patch set is ready for Chief Architect review and acceptance decision. No patches need to be applied before acceptance is considered — this is the post-patch review, and the files are already in their patched state in the working tree.

If the Chief Architect accepts the patch set:
1. Stage and commit the Phase 1 and Phase 2 target files: `communication-style.md`, `prompt-orchestration.md`, `validation-gates.md`, `adversarial_artifact_review_v0.md`, and all five Phase 2 templates.
2. The template-registry and retrieval-metadata overlay files (currently untracked) should also be committed as part of the same or an adjacent commit, since they are referenced by the patched files.
3. Optionally address FF-02 (terminology alignment) before or after commit — it is advisory.

If the Chief Architect wants FF-02 addressed before acceptance:
- Replace "stage-native output contract" with "output-mode exception" in the courier YAML sentence in `communication-style.md` Chat Output Topology section.

---

## 12. Review-Use Boundary

These findings are decision input for the Chief Architect. They are not mandatory remediation unless separately accepted and authorized. FF-01 and FF-02 are advisory friction findings — they describe residual risks and minor terminology inconsistency. Neither constitutes a veto of the patch set.

This review does not claim the patch set is approved, accepted, validated, workflow-ready, merge-safe, product-ready, resolver-ready, implementation-ready, installed, deployed, or committed.

A separately authorized commit and acceptance turn is the next implementation step if the Chief Architect accepts this review.
