# Adversarial Review Report: Orca Review-Report Contract Topology

```yaml
retrieval_header_version: 1
artifact_role: Review report
scope: Adversarial review of Phase 1 overlay patches and Phase 2 active prompt/template patches for the Orca review-report contract topology.
use_when:
  - Deciding whether to accept the Phase 1 and Phase 2 contract-topology patches.
  - Checking which active prompt surfaces still need remediation before full contract compliance.
authority_boundary: retrieval_only
input_hashes:
  .agents/workflow-overlay/prompt-orchestration.md: 9A5846F379C6FD635DAFF96544C2D15CB31ABE5FC425DD9D7BA0F3DD84B2CFA8
  .agents/workflow-overlay/communication-style.md: D429215695118D49D9B2551731B3A7DEB3E054B2D11C58CCABAE19D37503A5F8
  .agents/workflow-overlay/validation-gates.md: 5906ACFAB33F93C951E550A643D8345E8FD4295F4957CF6C33C64C41A95DF956
  docs/prompts/templates/review/adversarial_artifact_review_v0.md: 3476A7D0F1E2FDCE2EE76594615111FEE822BCDFC3B9E8B9E1884D1C16CE6E9C
  docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md: AFB4CEE573ADCB2F244C9733D8F0CF107DD0304CCF1B5529D30F9F4FB002C4A9
  docs/prompts/reviews/core_spine_v0_method_validation_case_frame_locks_adversarial_review_gpt54_prompt_v0.md: 316B96BC95DA06CE598E354A8456F78DDD5571900C4270B7F5C715AD27820F42
branch_or_commit: main @ 3bf5c45cfa6879ae65c8f822eff9c185dcba8b3c
downstream_consumers:
  - docs/prompts/reviews/orca_review_report_contract_topology_adversarial_review_prompt_v0.md
stale_if: Any input hash changes or further patches to the reviewed files are applied.
```

- Review date: 2026-05-22
- Reviewer: Claude Sonnet 4.6 (model-neutral slot)
- Output mode: review-report
- Edit permission: read-only
- Workspace: `C:\Users\vmon7\Desktop\projects\orca`
- Review prompt: `docs/prompts/reviews/orca_review_report_contract_topology_adversarial_review_prompt_v0.md`

---

## 1. Review Target and Source-Read Ledger

### Phase 1 Overlay Patch Targets (reviewed as canonical owners)

| File | Git status | Role in this review | Hash verified |
|---|---|---|---|
| `.agents/workflow-overlay/prompt-orchestration.md` | Modified (M) | Canonical owner of `review-report` validity, saved-report prerequisite, and failed-write behavior | Yes — matches pinned hash |
| `.agents/workflow-overlay/communication-style.md` | Modified (M) | Canonical owner of courier YAML shape and forbidden extra keys | Yes — matches pinned hash |
| `.agents/workflow-overlay/validation-gates.md` | Modified (M) | Owner of the review-report topology gate checklist | Yes — matches pinned hash |

### Phase 2 Active Surface Targets (reviewed for alignment with Phase 1)

| File | Git status | Role in this review | Hash verified |
|---|---|---|---|
| `docs/prompts/templates/review/adversarial_artifact_review_v0.md` | Untracked (??) | Active adversarial review template | Yes — matches pinned hash |
| `docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md` | Modified (M) | Active `review-report` prompt (GPT-5.5) | Yes — matches pinned hash |
| `docs/prompts/reviews/core_spine_v0_method_validation_case_frame_locks_adversarial_review_gpt54_prompt_v0.md` | Untracked (??) | Active `review-report` prompt (GPT-5.4) | Yes — matches pinned hash |

### Authority Sources Read

| File | Git status | Authority role |
|---|---|---|
| `AGENTS.md` | Clean | Orca project operating instructions |
| `.agents/workflow-overlay/README.md` | Modified (M) | Overlay entrypoint and binding rule |
| `.agents/workflow-overlay/source-of-truth.md` | Modified (M) | Source hierarchy and conflict rules |
| `.agents/workflow-overlay/artifact-roles.md` | Modified (M) | Review prompt and review report role bindings |
| `.agents/workflow-overlay/review-lanes.md` | Modified (M) | Review lane rules, reviewer permissions, report destinations |
| `.agents/workflow-overlay/template-registry.md` | Untracked (??) | Template registry; lists adversarial review template as active |
| `.agents/workflow-overlay/retrieval-metadata.md` | Untracked (??) | Retrieval-header contract |
| `.agents/workflow-overlay/safety-rules.md` | Clean | Project safety rules |
| `docs/prompts/hygiene-queue/precompact_orca_review_report_contract_topology.md` | Untracked (??) | Continuity only — not authority |

### Worktree Preflight Result

- Workspace: `C:\Users\vmon7\Desktop\projects\orca` — correct.
- Branch: `main`.
- HEAD: `3bf5c45cfa6879ae65c8f822eff9c185dcba8b3c` — matches pinned `branch_or_commit`.
- All six pinned input hashes verified against disk — all match exactly.
- Dirty state: allowed per review prompt. All modified and untracked sources are acknowledged below.
- Target files: accessible.
- Preflight result: **pass**.

---

## 2. Git Status and Dirty Sources Relied On

Branch is `main`, 11 commits ahead of `origin/main` (no remote pushes have occurred).

**Dirty sources relied on as authority:**

- `.agents/workflow-overlay/prompt-orchestration.md` — Modified (M). Phase 1 patched. Used as the canonical owner of `review-report` validity and failed-write behavior. Hash verified; used as authoritative working-tree state.
- `.agents/workflow-overlay/communication-style.md` — Modified (M). Phase 1 patched. Used as the canonical owner of courier YAML shape. Hash verified.
- `.agents/workflow-overlay/validation-gates.md` — Modified (M). Phase 1 patched. Used as the topology gate checklist. Hash verified.
- `docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md` — Modified (M). Phase 2 patched. Hash verified.

**Untracked sources relied on:**

- `.agents/workflow-overlay/template-registry.md` — Untracked. Used to confirm template registration status.
- `.agents/workflow-overlay/retrieval-metadata.md` — Untracked. Used as retrieval-header contract authority.
- `docs/prompts/templates/review/adversarial_artifact_review_v0.md` — Untracked. Phase 2 target; hash verified.
- `docs/prompts/reviews/core_spine_v0_method_validation_case_frame_locks_adversarial_review_gpt54_prompt_v0.md` — Untracked. Phase 2 target; hash verified.
- `docs/prompts/hygiene-queue/precompact_orca_review_report_contract_topology.md` — Untracked. Read for continuity; not used as authority.

Git diff was run against all six patch targets. Three overlay files (prompt-orchestration.md, communication-style.md, validation-gates.md) and one active prompt (GPT-5.5) show diffs. The two untracked files (template and GPT-5.4 prompt) have no git diff because they are untracked. Contents were read directly.

---

## 3. Scope and Excluded Scope

**In scope:**

- Contract ownership: does `prompt-orchestration.md` own `review-report` validity, saved-report prerequisite, and failed-write behavior?
- Schema ownership: does `communication-style.md` own the exact `review_summary` YAML shape and forbidden extra keys?
- Artifact-vs-courier boundary: does human-readable review detail belong in the durable report, not chat YAML?
- YAML-only validity: is `review-report` YAML-only chat allowed only after successful durable report write?
- Failed-write behavior: do failed durable writes use `status: failed`, `recommendation: blocked`, `review_location: chat_only_current_thread`, no `report_path`, failed path named, and enough human-readable routing detail?
- Active surface coverage: do the active adversarial review template and two active `review-report` prompts align with the overlay contract?
- Stale one-off handling: is checkpoint/one-off language absent from overlay authority files?
- Retrieval metadata boundary: do headers remain retrieval-only without implying authority, validation proof, approval, readiness, or lifecycle completion?
- Leakage gate: are `jb` project policy, GAP/CV Engine paths, lifecycle mechanics, and handoff rules absent from the reviewed files?
- Non-claims: do the patches avoid claiming validation, approval, readiness, resolver behavior, installation, deployment, or implementation completion?

**Excluded scope:**

Orca product strategy, proof quality, buyer proof, customer discovery, Core Spine validation, method-validation case quality, external evidence, implementation code, tests, runtime architecture, tooling, automation, packages, install/deploy behavior, resolver behavior, or workflow-kernel source.

---

## 4. Contract-Topology Decision Assessment

The Phase 1 patches establish a correct and internally consistent ownership split:

- **`prompt-orchestration.md`** owns the behavioral rule: when a durable report is required, when YAML-only chat is valid, and what fields constitute a failed-write response. It cross-references `communication-style.md` for the YAML schema.
- **`communication-style.md`** owns the exact YAML shape and forbidden extra keys. It explicitly redirects validity semantics back to `prompt-orchestration.md`.
- **`validation-gates.md`** owns the topology gate checklist, which serves as the collision checklist for future prompt-policy patches.

This split is valid. The behavioral rule owner and the schema owner are different files, and both cross-reference each other. A prompt author reading `prompt-orchestration.md` is told to consult `communication-style.md` for the YAML shape. A reader of `communication-style.md` is told that validity rules live in `prompt-orchestration.md`. The bidirectional reference is present and explicit.

The adjacency requirement is satisfied: the saved-report exception and failed-write behavior are in the same section of `prompt-orchestration.md` as the `review-report` output-mode rule.

The Phase 2 patches align the active surfaces on the core contract topology (durable destination binding, YAML-only-after-write gate, failed-write field set) but leave two active surfaces without the `workflow-deep-thinking` invocation requirement, which is also part of the overlay contract for review prompts.

---

## 5. Correctness Findings

### AR-01: GPT-5.5 proof-packet preparation prompt is missing the required `workflow-deep-thinking` skill invocation.

- **Location:** `docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md` — between the Objective section and the Required Reads section. The GPT-5.4 method-validation prompt has a `## Required Skill Invocation` section; the GPT-5.5 prompt has none.
- **Evidence:** The GPT-5.5 prompt goes directly from "## Objective" to "## Required Reads" without any skill invocation. The GPT-5.4 prompt contains: "## Required Skill Invocation — Use `workflow-deep-thinking` first. Then use `workflow-adversarial-artifact-review`."
- **Why it matters:** `prompt-orchestration.md` (the canonical authority) states: "All Orca review prompts must explicitly trigger `workflow-deep-thinking` before the relevant review skill." `review-lanes.md` echoes this. This is a hard requirement ("must"), not a recommendation ("should"). An executor running the GPT-5.5 prompt without deep thinking produces a review that violates the overlay contract while appearing to follow the prompt. The Phase 2 patch addressed the failed-write contract but did not address this requirement.
- **Next action:** Add a `## Required Skill Invocation` section to the GPT-5.5 prompt, between Objective and Required Reads, instructing the reviewer to use `workflow-deep-thinking` first and then `workflow-adversarial-artifact-review`.

---

### AR-02: Active adversarial review template is missing the `workflow-deep-thinking` invocation requirement.

- **Location:** `docs/prompts/templates/review/adversarial_artifact_review_v0.md` — the template text block. No mention of deep thinking anywhere in the template body.
- **Evidence:** The template begins "You are performing a read-only adversarial artifact review for Orca." and proceeds directly to review checks and findings. The overlay requirement ("All Orca review prompts must explicitly trigger `workflow-deep-thinking`") is not surfaced to the reviewer filling in the template.
- **Why it matters:** The template is the source material for future review prompts. If it does not include the deep-thinking invocation requirement, new review prompts derived from it will also omit it, systematically propagating the gap. The template is registered in `template-registry.md` as active. A prompt author following the template as a guide would produce a non-compliant prompt.
- **Next action:** Add a `Required Skill Invocation` instruction to the template's review instructions block, before the Review Checks section, specifying that `workflow-deep-thinking` must be used first and `workflow-adversarial-artifact-review` second.

---

### AR-03: `communication-style.md` was materially touched in Phase 1 but has no retrieval header.

- **Location:** `.agents/workflow-overlay/communication-style.md` — top of file, before `## Default Shape`.
- **Evidence:** The file begins directly with `# Communication Style` followed by prose. The git diff shows a Phase 1 patch that materially changed the Adversarial Review Summary Pattern section. No retrieval header was added. By contrast, both `prompt-orchestration.md` and `validation-gates.md` received retrieval headers in Phase 1.
- **Why it matters:** `validation-gates.md` includes the gate: "New or materially touched durable human-authored workflow artifacts follow `.agents/workflow-overlay/retrieval-metadata.md` or are clearly outside that contract." `communication-style.md` is unambiguously inside that contract (it is a durable overlay authority file that affects routing, review, and prompt handoffs). The missing header means future agents navigating from `prompt-orchestration.md`'s cross-reference to `communication-style.md` cannot rely on the standard retrieval mechanism to confirm they have the right file or understand its scope at a glance. It also means the Phase 1 patch did not fully satisfy the retrieval-metadata gate for this file.
- **Next action:** Add a retrieval header to `communication-style.md` with `artifact_role: Orca overlay authority`, `scope: Orca response style, courier YAML shape, and adversarial review summary pattern`, `use_when` bullets covering review closeouts and prompt handoffs, and `authority_boundary: retrieval_only`.

---

### AR-04: GPT-5.5 proof-packet preparation prompt was materially touched in Phase 2 but has no retrieval header.

- **Location:** `docs/prompts/reviews/core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md` — top of file.
- **Evidence:** The file begins with `# GPT-5.5 Adversarial Review Prompt: Core Spine v0 Proof Packet Preparation` with no retrieval header block. The GPT-5.4 method-validation prompt has a full retrieval header including `input_hashes`, `branch_or_commit`, `downstream_consumers`, and `stale_if`.
- **Why it matters:** The same retrieval-metadata gate applies to this file as AR-03. The asymmetry between the two active `review-report` prompts means the GPT-5.5 prompt cannot be navigated to or verified by the same retrieval method as the GPT-5.4 prompt. It also leaves `downstream_consumers` and `stale_if` information absent, which increases future maintenance risk when the target artifacts are updated.
- **Next action:** Add a retrieval header to the GPT-5.5 prompt consistent with the GPT-5.4 prompt's header, including `artifact_role: Review prompt`, `input_hashes` for the target artifacts, `branch_or_commit`, `downstream_consumers`, and `stale_if`.

---

## 6. Friction Findings

### AF-01: `prompt-orchestration.md` behavioral prose omits `review_location: chat_only_current_thread` from the failed-write field enumeration.

- **Location:** `.agents/workflow-overlay/prompt-orchestration.md` — `## Review Prompt Defaults` and `## Output Modes` sections (both prose blocks describing failed-write behavior).
- **Evidence:** Review Prompt Defaults: "Return a failed blocked result in chat, do not use `report_path`, name the failed report path, and include enough human-readable failure detail to route." Output Modes row: "return `status: failed` and `recommendation: blocked` in chat without `report_path`, name the failed path, and include enough human-readable failure detail to route." Neither prose block names `review_location: chat_only_current_thread`.
- **Why it matters:** The complete failed-write field set requires `review_location: chat_only_current_thread`. This field appears in `validation-gates.md`'s topology gate and in `communication-style.md`'s YAML shape, but not in the behavioral prose of the owner file. A prompt author relying only on `prompt-orchestration.md`'s prose (without reading the gate or the schema) would produce a failed-write YAML without `review_location`. Since `prompt-orchestration.md` is the owner of the behavioral rule, omitting this field from the behavioral prose creates a gap between the rule and the gate. This is currently bridged by the cross-reference to `communication-style.md` for the schema, but the cross-reference is indirect. A future patch to the behavioral prose that does not consult `communication-style.md` could inadvertently drop this field.
- **Next action:** Add `review_location: chat_only_current_thread` explicitly to both failed-write prose blocks in `prompt-orchestration.md`.

---

### AF-02: Failure YAML schema is prose-only in `communication-style.md` while the two active prompts each provide a full inline example.

- **Location:** `.agents/workflow-overlay/communication-style.md` — `## Adversarial Review Summary Pattern` section, failure case description.
- **Evidence:** `communication-style.md` provides an inline YAML block for the success case (`status: completed`, `report_path`, etc.) but describes the failure case in prose only: "use the same shape with `status: failed`, `review_location: chat_only_current_thread`, and `recommendation: blocked`." Both GPT-5.5 and GPT-5.4 active prompts provide full inline failure YAML blocks with all nine fields enumerated.
- **Why it matters:** The schema owner (`communication-style.md`) is currently the only file in the contract topology that does not show the failure YAML concretely. Future schema authors updating `communication-style.md` may not realize the failure case carries all nine fields when they see only the three-field prose description. If `communication-style.md`'s failure description diverges from the active prompts' inline examples, neither version is clearly authoritative.
- **Next action:** Add an inline YAML block for the failure case to `communication-style.md`'s Adversarial Review Summary Pattern, matching the shape in the two active prompts.

---

## 7. Not-Proven Boundaries

- No claim is made that the Phase 1 or Phase 2 patches were applied correctly to the committed history. The review covers the working-tree state as of the pinned hashes. Whether these changes have been or should be committed is outside the review scope.
- No claim is made that the existing retrieval headers in `prompt-orchestration.md` and `validation-gates.md` contain correct hash values for their own inputs. The review verified the Phase 1 patches produced correct contract topology; it did not audit every header field in every overlay file.
- No claim is made about whether past review runs (before Phase 1) produced artifacts that violated the contract. The review is forward-looking: does the current patch set preserve the contract for future runs?
- No claim is made about whether the stale one-off files in `docs/prompts/product-planning/` or prior precompact notes contain language that could be misread as authority. They were not read. The review relied on the hygiene checkpoint's identification of these as hygiene candidates not broad-synced into overlay files.
- No claim is made about the `core_spine_v0_proof_packet_preparation_adversarial_review_gpt55_prompt_v0.md` prompt's review accuracy, scope coverage, or fitness for its intended product-proof review task. This review assesses only its contract-topology alignment.

---

## 8. Blockers and No-Blocking-Finding Statement

**No blocking findings.** The Phase 1 overlay patches correctly establish the review-report contract ownership topology. The four correctness findings (AR-01 through AR-04) are contract-gap findings that require patching the active Phase 2 surfaces before those surfaces can be considered fully contract-compliant, but they do not block use of the Phase 1 overlay patches as authority.

**AR-01 and AR-02** (missing `workflow-deep-thinking` invocations) mean the GPT-5.5 prompt and the template are not fully overlay-compliant as review launch prompts. A reviewer executing either without deep thinking would violate the overlay contract. These are patch-before-acceptance gaps for the Phase 2 surface.

**AR-03 and AR-04** (missing retrieval headers on `communication-style.md` and the GPT-5.5 prompt) mean the retrieval-metadata gate was not fully satisfied for those two files. These are maintenance-hygiene gaps that do not affect the correctness of the contract topology itself.

**AF-01 and AF-02** are friction findings that create future-patch risk but do not break the current contract. The complete information is accessible by following cross-references.

---

## 9. Next Authorized Step

The next authorized step is to patch the two Phase 2 surfaces that are missing the `workflow-deep-thinking` invocation requirement (AR-01, AR-02) and add retrieval headers to `communication-style.md` and the GPT-5.5 prompt (AR-03, AR-04), then optionally add the inline failure YAML to `communication-style.md` (AF-02) and extend `prompt-orchestration.md`'s behavioral prose to name `review_location` explicitly (AF-01).

These are all docs-only overlay maintenance and prompt-artifact edits. No implementation, installation, deployment, or workflow-kernel changes are involved.

Whether to accept the Phase 1 patches and authorize Phase 2 remediation is the Chief Architect's decision. This review provides decision input; it does not accept, approve, or authorize.

---

## 10. Review-Use Boundary

These findings are decision input for the Chief Architect. They are not mandatory remediation unless separately accepted and authorized. The review is read-only and does not claim that the patch set is approved, accepted, validated, workflow-ready, merge-safe, product-ready, resolver-ready, implementation-ready, installed, deployed, or committed.

The Phase 1 overlay patches correctly preserve the review-report contract topology. The Phase 2 active surfaces are partially aligned, with four gaps enumerated above. No further review authority or implementation authority follows from this report.
