---
retrieval_header_version: 1
artifact_role: >
  Prompt artifact — Chief-Architect commission for a DELEGATED, cross-vendor
  (de-correlated) adversarial REVIEW-AND-PATCH pass (repo mode) on the Beauty Pie
  #3 paired participant packets, to close R6-AR-01 (residual response/reaction
  framing). NOT validation, readiness, verdict authority, or a bound review lane.
scope: >
  Commission a non-Claude delegate to review + patch the two paired packets'
  shared lines 7 + 10, neutralizing the contestant-visible market-response/reaction
  framing to a pure whitelist/cutoff boundary, identical in both arms, preserving
  the single-hunk org-motion byte-identity. Delegate returns a unified diff +
  per-change citations + verdict + residual-risk; the CA adjudicates.
use_when:
  - Commissioning the de-correlated PATCH that closes R6-AR-01 before the final R6 re-scan.
authority_boundary: retrieval_only
created_at: 2026-06-13
created_by_lane: judgment-spine / org-motion Beauty Pie #3 pilot continuation
stale_if:
  - origin/main moves past b463c3c on the named packet blobs (re-pin + re-verify).
  - R6-AR-01's minimum_closure_condition changes in the re-scan report.
  - The delegated-review-patch convention is amended in .agents/workflow-overlay/delegated-review-patch.md.
---

# Beauty Pie #3 — R6-AR-01 De-Leak: Delegated Adversarial Review-and-Patch Commission v0

> Provisional, opt-in convention (`.agents/workflow-overlay/delegated-review-patch.md`),
> commissioned explicitly by the Chief Architect. The delegate is a commissioned
> bounded executor (review + patch its named scope), **not** a read-only review
> lane. This commission names the bounded scope; the CA adjudicates the returned
> diff before anything is kept.

## Why delegated review-and-patch (not home patch, not another findings-only review)
The R6 gate already returned findings (`use_for_blind_contestant_exposure: no`,
blocking `R6-AR-01`). What is needed now is the **fix**, authored **de-correlated
from the original packet author**. Evidence this matters: `git log -S` shows the
residual leak phrasing entered at the **de-leak commit itself** (`5db7feb`,
"apply R5 whitelist/decision-framing") — i.e., the home author re-expressed the
withheld-reaction concept in new fields while removing the explicit blacklist,
and home self-verification did not see it. A same-vendor (Claude) home patch
would re-run that exact correlated blind spot and would still owe a fresh
cross-vendor discovery pass. Routing the **patch authorship** to a non-Claude
delegate de-correlates the fix; the CA then adjudicates.

This packet is a high-stakes **authored eval/calibration instrument** whose author
encoded the guardrail and reintroduced the failure mode it exists to prevent —
the exact category this convention targets.

## Commission (per delegated-review-patch)
- **access: `repo`** — the delegate patches the named targets in-repo and returns a unified diff. (`no_repo` is not used here.)
- **De-correlation (who-constraint, recorded; not model routing):**
  - `author_vendor: anthropic` (the packets are Claude-authored).
  - `delegate_vendor:` **must be non-Anthropic** (e.g., the GPT lineage). Cross-vendor discovery bar = author_vendor != delegate_vendor. A Claude delegate does **not** satisfy it. Record both vendors in the return.
- **Named target files (bounded scope — see pairing note):**
  - `orca-harness/cases/product_learning/beautypie_repricing_2023_v0/participant_packet_baseline.md` — blob `912cc2843fa6` @ `b463c3c`
  - `orca-harness/cases/product_learning/beautypie_repricing_2023_v0/participant_packet_augmented.md` — blob `2b679c59dc9d` @ `b463c3c`
  - **Pairing note:** the convention defaults to a single target file. This commission deliberately names the **paired** packets because they are byte-identical by construction except the org-motion block; the de-leak MUST be applied **identically to both** or the single-hunk byte-identity breaks. This is the justified bounded scope; it is not license to touch anything else.
- **Bounded patch scope (the ONLY edits authorized):**
  - **Line 7 — `capability_constraints`:** remove the "before any market response to the decision is observable" clause; keep only a pure pre-cutoff-evidence / cutoff-rule framing.
  - **Line 10 — `permitted_assumptions`:** reword "Distinguish a pre-existing base rate from a reaction to this specific move" so it no longer names a *reaction/response* class, while preserving the base-rate-vs-company-specific reasoning hygiene.
  - Apply **identical** text to both packet files. Nothing else changes.
- **Explicitly OUT of scope (flag-only if you see an issue; do NOT edit):**
  - Line 41 body ("before any decision is announced") — this is the decision's own pre-announcement premise, not a withheld post-decision class; the R6 reviewer did not flag it. Leave it.
  - The `## Organizational Motion Signal` block (augmented-only) — do not touch; it is the only intended inter-arm delta.
  - **No anonymization.** Owner has decided this case is **never** anonymized (the ratified defense is the JSG-08 trace tell-audit, not anonymization). Do not rename the brand or scrub identifying specifics.
  - Every other file, field, ledger, schema, and the sealed outcome — read-only / flag-only.
- **Protected paths:** per `.agents/workflow-overlay/delegated-review-patch.md` + `safety-rules.md` — the two named packets are the only editable targets; all else is read-only/flag-only.

## Closure target (what "fixed" means — attack the bar too)
`R6-AR-01` minimum closure condition (from the re-scan report,
`docs/review-outputs/adversarial-artifact-reviews/beautypie_repricing_2023_r6_independent_leak_rescan_v0.md`):

> "Contestant-visible packet text names only the allowed evidence boundary and
> cutoff rule, without naming market response/reaction as an unavailable
> post-decision class or explaining what kind of post-cutoff material is withheld."

Constraints on the fix:
- **Lossless:** the contestant must still know they decide on pre-cutoff evidence only (≤ 2023-02-28) and must retain the base-rate-vs-specifics reasoning hygiene. Do not over-strip (the R6 reviewer's over-strip check must stay PASS).
- **Whitelist-only:** the only surviving meta-instruction stays the generic "decide using only the information in this packet" form. Introduce no new enumerated forbidden categories (that is itself a leak — the R5 lesson).
- **Byte-identity:** after the patch, the two packets must still differ by **exactly one hunk** = the org-motion block. Run `git diff --no-index <baseline> <augmented>` and confirm one hunk; report it.
- The closure condition is an **alignment axis to attack**, not a pass-if-matches bar: if you judge the bar wrong (e.g., line 10 is legitimate hygiene that should be kept verbatim), say so in your verdict rather than silently complying or silently refusing.

## Method (Source-Gated; you are a commissioned executor, not a read-only reviewer)
1. **REFERENCE-LOAD** `workflow-deep-thinking` discipline + the adversarial review method (if you lack Orca skill access, use the portable method, registry id `portable-adversarial-artifact-review-method`). Read the authority excerpts below as binding rules.
2. **SOURCE-LOAD** the two target packets at the pinned blobs (verify `git hash-object` matches `912cc2843fa6` / `2b679c59dc9d`; if not, stop and report drift).
3. Declare `SOURCE_CONTEXT_READY`.
4. **Review** for the material failure mode (residual withheld-class framing), then **patch** within the bounded scope, then **self-check** (closure condition met; over-strip PASS; byte-identity one hunk).
5. If the problem is design-level rather than this bounded patch (e.g., the leak cannot be closed without changing the case), return **`NEEDS_ARCHITECTURE_PASS`**, stop patching, and return findings only; do not keep a partial diff.

## Required return (paste-ready courier to the CA)
- A **unified diff** of the two files (the patch you applied in your repo workspace).
- **Per-change source citations** — neutral, factual (cite the target line + the authority excerpt the change satisfies); argument goes in the verdict, not the citations.
- **Verdict:** does the patch close `R6-AR-01` under the closure condition? Plus your read on whether the closure bar is itself right.
- **Residual-risk note.**
- **Provenance:** `author_vendor: anthropic`, `delegate_vendor: <your vendor+model+version>`, `de_correlation_bar: cross_vendor_discovery`, `access: repo`.
- **Byte-identity result:** the `git diff --no-index` hunk count (must be 1) + the single hunk's identity.

The diff + verdict are **decision input only**. The CA (Claude) adjudicates and reserves final authority to keep, veto, or modify any change.

## Authority excerpts (binding rules the patch must satisfy)
### A. R6-AR-01 minimum closure condition
(quoted above — the exact end state the patch must reach)

### B. R5 whitelist leak-safety (conductor v1, blob `ede291484835`)
> The participant packet is a genuine decision brief, never a test. Whitelist,
> never blacklist: the only surviving meta-instruction is generic ("decide using
> only the information in this brief; not outside or later knowledge"). No
> enumerated forbidden categories on any contestant-readable surface — an
> enumerated forbidden list is itself a leak. The spoiler taxonomy lives only in
> the sealed facilitator-only record.

### C. Orca `AGENTS.md` kernel — Smallest Complete Intervention
> Default to the smallest complete intervention: solve the actual request
> completely with the narrowest sufficient scope. `Complete` is load-bearing — do
> not underfix (leave a related instance that re-opens the finding). `Smallest`
> is load-bearing — no unrelated cleanup, no over-strip, no scope inflation.
> Every changed line traces to the request. Never create fake success paths.

## Preflight (this commission's authoring state)
```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom   # S0 overlay + delegated-review-patch + named judgment-spine targets @ b463c3c
  edit_permission: docs-write   # author this commission only; the DELEGATE holds the bounded patch authority on the two packets
  target_scope: >
    Author one delegated-review-patch commission under docs/prompts/patches/. Does
    not itself edit the packets, change doctrine, or claim readiness -> no
    direction_change_propagation receipt required.
  dirty_state_checked: yes
  blocked_if_missing: none
```
- Source-of-truth: commit `b463c3c` (`origin/main`); patch in a clean checkout/worktree off main. Do NOT use `ecr-sp3-timing-deriver-slice1`.
- Authoring workspace: worktree `orca-r6-rescan-commission-wt` @ `b463c3c`.

## After the patch (sequence — still owner-gated)
1. CA adjudicates the delegate's diff (keep / veto / modify).
2. **Final R6 re-scan (cross-vendor discovery)** on the patched packets via
   `workflow-adversarial-artifact-review` — only an independent PASS flips
   `use_for_blind_contestant_exposure: no -> yes`. (Note: with the patch authored
   by a non-Claude delegate, a Claude R6 re-scan would itself be cross-vendor to
   the latest author; the operator chooses the reviewer, recording vendors.)
3. Then (still owner-gated): option_value separate-family second-label, conductor
   v1 ratification, seal/capture/freeze — and **STOP before Phase 6**.

## Non-claims
- Provisional convention; a delegated diff + verdict is **decision input only** —
  not validation, readiness, formal review authority, or a kept change until the
  CA adjudicates and it is committed.
- Product-learning tier, N=1. JSG-01 frozen; pinned scoring key unchanged. Not
  live-API; not buyer-proof; not judgment-quality.
- Names model **families** only (the cross-vendor who-constraint); recommends,
  ranks, and routes **no runtime model**.
