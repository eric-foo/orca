# GPT-5.5 Adversarial Review Prompt: Core Spine v0 Proof Packet Preparation

- Prompt type: Review prompt
- Requested reviewer model: GPT-5.5
- Output mode: review-report
- Edit permission: read-only
- Workspace: `C:\Users\vmon7\Desktop\projects\orca`
- Target artifacts:
  - `docs/product/core_spine_v0_proof_packet_preflight_v0.md`
  - `docs/product/core_spine_v0_first_proof_packet_preparation_v0.md`

## Objective

Run one narrow adversarial artifact review of the accepted preflight and the
first proof-packet preparation artifact.

The review should answer whether either artifact still creates a blocker around
self-authorization, boundary leakage, `jb` authority leakage, or backtest
leakage. Do not run proof, collect evidence, patch files, or prepare a patch
queue.

## Required Reads

Read first:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/project-authority.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/artifact-roles.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/validation-gates.md`
- `.agents/workflow-overlay/safety-rules.md`
- `.agents/workflow-overlay/communication-style.md`

Then read:

- `docs/decisions/turn_08_product_thesis_v0.md`
- `docs/product/core_spine_v0_product_contract.md`
- `docs/product/engagement_logic_registry_v0.md`
- `docs/product/core_spine_v0_information_production_foundation_v0.md`
- `docs/product/core_spine_v0_proof_protocol_v0.md`
- `docs/product/core_spine_v0_proof_input_selection_v0.md`
- `docs/product/core_spine_v0_proof_packet_preflight_v0.md`
- `docs/product/core_spine_v0_first_proof_packet_preparation_v0.md`

Also check:

- `git status --short --branch`
- `git log --oneline -5`

## Current Decision Context

The owner accepted the corrected preflight in chat on 2026-05-21 for
proof-packet preparation only.

Accepted scope:

- the preflight defines the proof-prep gate;
- the Information Production Foundation is conditionally accepted as the manual
  proof-prep standard;
- proof execution remains unauthorized;
- evidence collection remains unauthorized;
- feature planning remains unauthorized;
- implementation remains unauthorized.

The first proof-packet preparation artifact was created after that acceptance
and currently carries verdict `READY_FOR_PROOF_PACKET_PREPARATION_REVIEW`.

## Dirty State Allowance

Dirty state is allowed. Modified and untracked Orca docs and overlay files may
exist. Do not clean, revert, stage, commit, or switch branches.

If a required target artifact is missing, unreadable, or conflicts with the
accepted scope above, return a blocked result instead of reviewing a substitute.

## Review Scope

Review only these risks:

- self-authorization: an artifact accepts itself, bypasses owner acceptance, or
  turns a proposed gate into proof authority;
- boundary leakage: an artifact authorizes proof execution, evidence
  collection, source maps, decision memos, feature planning, implementation, or
  tooling;
- `jb` authority leakage: an artifact imports `jb` paths, lifecycle mechanics,
  templates, validation habits, or success logic into Orca or Core Spine;
- backtest leakage: an artifact allows case selection, cutoff choice, or
  post-window evidence to be shaped after outcome knowledge.

After correctness findings, optionally note friction only if it affects the
next Chief Architect decision. Do not expand into broad product critique.

## Excluded Scope

Do not review implementation, code, tests, runtime architecture, source
collection systems, dashboards, scrapers, APIs, databases, scoring engines,
automation, feature plans, or commercial willingness to pay.

Do not judge whether competitor narrative evidence exists or is strong. Do not
judge whether the backtest will pass. Do not claim proof-run readiness.

## Output Style

Follow `.agents/workflow-overlay/communication-style.md`.

Use short headers. Use bullets with a small explanation for each bullet. Do not
bold bullet leads by default.

Decision first, scope second, next action third.

## Output Contract

Return a review report with:

1. Review target and source-read ledger.
2. Dirty sources relied on.
3. Scope and excluded scope.
4. Correctness findings first.
5. Friction findings only if material.
6. Not-proven boundaries.
7. Blockers or no-blocking-finding statement.
8. Next authorized step.
9. Review-use boundary.

Finding format:

- `AR-01`: one-sentence finding title.
- Location: file and stable section heading or search key.
- Evidence: quote or short paraphrase from the artifact.
- Why it matters: concrete effect on acceptance, boundary control, or proof-prep
  safety.
- Next action: advisory only; no patch execution.

If there are no blocking findings, say so directly. Do not claim the artifacts
are approved, accepted, validated, proof-ready, feature-ready, implementation
ready, or committed.

Findings are decision input for the Chief Architect. They are not mandatory
remediation unless separately accepted and authorized.

