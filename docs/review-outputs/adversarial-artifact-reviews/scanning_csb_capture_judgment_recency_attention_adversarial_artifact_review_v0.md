# Scanning / CSB / Capture / Judgment Recency-Attention Adversarial Artifact Review v0

```yaml
retrieval_header_version: 1
artifact_role: Review output (adversarial artifact review)
scope: >
  Read-only adversarial artifact review of PR #354 recency/currentness
  propagation changes at commit 13a1becb3841a2596430dc345674c86fa697e098
  across Commission Signal Board prompt, CSB adjudication packet amendment,
  Capture source playbook, Judgment demand-read core architecture, and repo map.
use_when:
  - CA adjudicating whether the PR #354 recency/currentness propagation is safe
    to accept, needs a small patch, or should be held.
  - Checking whether any changed surface makes recency proof, scoring,
    gate clearance, classifier mapping, graph weight, route binding, or access
    authorization.
authority_boundary: retrieval_only
stale_if:
  - PR #354 is rebased or amended after commit 13a1becb.
  - Any target file changes after this review is authored.
  - A separate owner decision supersedes this review's findings.
```

## Review Header

- **Reviewed by:** claude-sonnet-4-6
- **Authored by:** codex-gpt-5 (dispatcher-supplied provenance, accepted per review prompt)
- **De-correlation bar:** cross_vendor_discovery
- **Same-vendor rationale:** not applicable — reviewed_by (Claude/Anthropic) and authored_by (codex-gpt-5/OpenAI/GPT) are different vendor families; the cross-vendor discovery bar is met
- **Commit reviewed:** 13a1becb3841a2596430dc345674c86fa697e098
- **Branch:** codex/scanning-broad-scout-recency-default
- **Source context:** SOURCE_CONTEXT_READY (see Sources section)
- **Review lane:** adversarial artifact review (docs, decisions, product architecture, prompt artifacts)
- **Output mode:** review-report
- **Edit permission:** read-only; this report is the only write authorized by this review

## Cynefin Routing (Compact)

Complicated domain: bounded propagation review of a doctrine-adding change to three product spines and a repo map. Methods known; expertise required to identify boundary-crossing wording. Allowed next move: read-only adversarial review plus report write. Disallowed: patching, architecture redesign, scope widening into full scanning-spine redesign.

## Preflight

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: custom review S3 (named authority sources + 5 target files at commit 13a1becb)
  edit_permission: read-only review; write only this report
  target_scope: >
    Adversarial review of PR #354 recency/currentness propagation across
    CSB prompt, CSB adjudication packet, Capture playbook, Judgment demand-read
    core, and repo map at commit 13a1becb.
  dirty_state_checked: yes
  dirty_state_result: >
    HEAD is 2de522377c (two commits beyond 13a1becb). git diff 13a1becb..HEAD
    over all 5 target files returned empty — target files are identical at HEAD
    and at 13a1becb. Review proceeds against 13a1becb semantics; files read via
    git show 13a1becb:<path>.
  blocked_if_missing: all required sources confirmed present
```

## Sources Read

Authority sources (working tree, confirmed clean relative to target):
- AGENTS.md
- .agents/workflow-overlay/README.md
- .agents/workflow-overlay/source-of-truth.md
- .agents/workflow-overlay/source-loading.md
- .agents/workflow-overlay/review-lanes.md
- .agents/workflow-overlay/prompt-orchestration.md
- .agents/workflow-overlay/validation-gates.md
- .agents/workflow-overlay/communication-style.md
- docs/prompts/templates/review/adversarial_artifact_review_v0.md

Target files at commit 13a1becb (via git show):
- docs/workflows/orca_repo_map_v0.md
- orca/product/spines/commission_signal_board/authority/orca_commission_signal_board_prompt_adjudication_packet_v0.md
- orca/product/spines/commission_signal_board/prompts/orca_commission_signal_board_prompt_v0.md
- orca/product/spines/capture/core/source_capture_toolbox/source_capture_playbook_v0.md
- orca/product/spines/judgment/demand_read/core/judgment_spine_demand_read_machinery_architecture_v0.md

Exact diff for Judgment file read to confirm C2 and INV-1 addition text:
- git diff 8e79d18d..13a1becb -- judgment_spine_demand_read_machinery_architecture_v0.md

Validation runs (working tree at 13a1becb target state):
- git diff 8e79d18d..13a1becb --stat: 5 files changed, 204 insertions(+), 10 deletions(-) — expected
- git diff 8e79d18d..13a1becb --check: passed (no whitespace errors)
- python check_retrieval_header.py --changed: empty output (passed)
- python check_repo_map_freshness.py --changed: empty output (passed)
- python check_map_links.py --strict: OK, 0 findings (33 annotated non-resolving as debt, not failures)
- python check_commission_signal_board_output.py --selftest: SELFTEST OK (10 test cases passed)
- Cross-spine stale/leakage search (rg patterns from review prompt): no recency-as-proof/gate/scoring/classifier-mapping hits found across CSB, Scanning, Capture, Judgment, or repo map

## Sources Intentionally Not Read

- orca/product/spines/scanning/README.md — adjacent; seen via stale-search hits showing correct "not proof" language; DCP receipts confirm checked and not updated
- orca/product/spines/scanning/scan_core/orca_scanning_intelligent_walk_mgt_operating_model_v0.md — adjacent; stale-search confirmed "Recency is a hard attention-priority rule, not proof" at line 168
- orca/product/spines/judgment/claim_ladder/judgment_spine_evidence_ladder_architecture_v0.md — intentionally_not_updated per Judgment DCP with valid reason (claim tiers unchanged)
- orca/product/spines/judgment/conductor/judgment_spine_gate_ownership_map_v0.md — intentionally_not_updated per Judgment DCP with valid reason (no JSG gate gains a recency proof shortcut)
- orca/product/spines/judgment/demand_read/grading/judgment_spine_demand_read_grading_rubric_v0.md — not in required sources for this review; Judgment DCP claims it was checked and not updated
- docs/workflows/data_capture_spine_consolidation_map_v0.md — retrieval-only pointer; Capture DCP claims it was checked, not updated
- docs/research/judgment-spine/judgment_spine_consolidation_map_v0.md — retrieval-only pointer; Judgment DCP claims it was checked, not updated
- .agents/hooks/check_commission_signal_board_output.py — validator source not read; behavior confirmed via selftest
- All review outputs not named by this prompt, all research corpus, all implementation/runtime code except the named validator script

---

## Findings — Phase 1 (Correctness)

### Non-Finding: No proof, gate, scoring, classifier, or route-binding leakage

The primary attack question was whether any changed surface makes recency/currentness a demand proof, gate clearance, classifier mapping, graph weight, numeric/ordinal weight, scoring shortcut, claim-tier evidence, Capture route selection, or access authorization. The adversarial review found no such leakage across any of the five changed files.

**Evidence summary by file:**

**CSB prompt v0:** Fields `recency_status` and `recency_attention` are defined with inline explanation "source-route priority, not truth." The Signal Collection Allocation section uses "elevated effort" (not proof-weight) for recent signals. Final Rules: "Keep recency attention separate from proof, classifier mapping, and graph weight; it routes attention, not truth." The DCP receipt's non-claims list includes "not demand classification," "not buyer proof," and "not source-access authorization." No proof/scoring language found.

**CSB adjudication packet amendment:** Adds a narrow pointer-level note: "the durable CSB prompt now records recency/currentness as source-route attention metadata... that attention is not buyer proof, demand classification, classifier mapping, evidence weighting, or graph weight." The amendment is a secondary report pointing to the CSB prompt as the controlling source — not a second source of doctrine. Consistent with the durable prompt; no split-brain created.

**Capture playbook — new "Recency / Current-State Preservation Priority" section (verbatim):**
> "When a scanning or CSB handoff marks a URL or venue as recent/current-state high-attention, Capture treats that as preservation urgency and source-drift risk. Prefer preserving the current visible state before older context when the request is otherwise within scope and route-matched… This priority does not prove demand, change the access-control gate, select a route by itself, or let scanning bind Capture's route. Capture still runs Step 0, chooses the cheapest matching route, and records the captured state as source facts, not proof."

The phrase "within scope and route-matched" preserves Step 0 and the route catalog as independent gates. Recency affects only capture ordering after route selection is complete. No route-binding or access-authorization leak.

**Judgment demand-read architecture — C2 addition (verbatim from diff):**
> "Recent/current source states are an attention and relevance input here: same-strength newer signals normally deserve more read attention than older context, including when direction differs. That attention weighting is not gate proof, numeric weight, or a scoring shortcut."

**INV-1 addition (verbatim from diff):**
> "Recency/currentness may raise scan/read attention for same-strength signals, but it must not be encoded as a numeric/ordinal weight or deterministic rule."

The C2 addition uses "attention and relevance input" — unambiguously in the attention domain. The phrase "including when direction differs" correctly states that attention recency is direction-agnostic (a recent "no-demand" signal is as attention-worthy as a recent "yes-demand" signal), which is the right semantics. INV-1 provides a hard invariant: no numeric or ordinal encoding, no deterministic rule. No scoring shortcut or gate proof created.

**Repo map:** Navigation-only wording at lines 420, 422, and 549 correctly summarizes attention/preservation/read-relevance semantics and explicitly states "not proof or scoring," "not proof," and "without changing proof or route binding." No authority overstated.

**Cross-spine stale/leakage search:** Ran the prompt-specified rg pattern across CSB, Scanning, Capture, Judgment, and repo map. All hits were:
- Accepted recency/attention language
- DCP receipt stale-language queries (part of the receipts themselves)
- Explicit "not proof" guard clauses

No surface found that converts recency/currentness into proof, gate, scoring, classifier mapping, numeric weight, or graph weight.

---

### AR-01 — MINOR — DCP stale-language search coverage is patchwork across spines

**Phase:** Correctness (DCP receipt honesty)

**Location:** CSB prompt DCP receipt (`stale_language_search` field); Capture DCP receipt; Judgment DCP receipt

**Issue:** Each file's DCP receipt runs its stale-language search over its own spine's surfaces only. The CSB prompt DCP searches `orca/product/spines/commission_signal_board`, `orca/product/spines/scanning`, and `docs/workflows/orca_repo_map_v0.md` — but not Capture or Judgment. The Capture DCP searches Capture, Scanning, and consolidation maps — but not CSB or Judgment. The Judgment DCP searches Judgment, Scanning, and consolidation maps — but not CSB or Capture. No single DCP receipt states cross-spine coverage.

**Evidence:** CSB prompt DCP `stale_language_search` field names only three scope paths; Capture and Judgment follow the same per-spine pattern.

**Strongest defense:** The per-spine receipts are internally complete and mutually complementary. Together they do cover the three spines plus scanning plus the repo map. The review prompt's own cross-spine stale search (which this review ran) found no leakage. This patchwork is a documentation style issue, not a correctness failure. The DCP contract does not require a single cross-spine receipt.

**Why the defense does not fully eliminate the finding:** A future reader examining only one DCP receipt to understand propagation scope cannot determine whether the other two spines were searched. The receipts provide no cross-reference to confirm their scope is collectively complete rather than accidentally patchwork. This is a mild DCP honesty gap — the `stale_language_search_result` wording ("No controlling CSB/scanning surface was found...") could mislead a reader who doesn't realize Capture and Judgment were not in that receipt's scope.

**Impact:** Documentation gap only; behavioral correctness not affected. The cross-spine search this review performed confirms no leakage.

**Minimum closure condition:** CA accepts the patchwork as adequate given this review's cross-spine search results, or one DCP receipt (e.g., the CSB prompt's, as the origin receipt for the change) explicitly notes that Capture and Judgment surfaces were searched separately under their own DCP receipts.

**Next authorized action:** CA notes and accepts, or optionally adds a cross-reference note to the CSB prompt DCP's stale_language_search_result.

**Recommended correction (advisory):** In the CSB prompt's DCP stale_language_search_result, add one sentence: "Capture and Judgment surfaces were searched under their own DCP receipts; no cross-spine leakage found." This closes the reading gap without changing any doctrine.

**patch_queue_entry:** Not authorized in this read-only lane.

---

### AR-02 — MINOR — Judgment DCP downstream check of grading rubric unverifiable in this review's source pack

**Phase:** Correctness (DCP receipt honesty, provenance gate)

**Location:** Judgment demand-read DCP receipt, `downstream_surfaces_checked` list, entry `orca/product/spines/judgment/demand_read/grading/judgment_spine_demand_read_grading_rubric_v0.md`

**Issue:** The Judgment DCP receipt claims this grading rubric was checked as a downstream surface. This file is not in this review's required source pack (not named by the review prompt's required sources, not in the target commit's diff). The DCP claim is a secondary report that cannot be directly verified in this review pass.

**Evidence:** The claim appears at line level in the Judgment DCP's `downstream_surfaces_checked` list with no `intentionally_not_updated` entry and no reason given for not updating. The review prompt's required sources list did not include this file.

**Strongest defense:** The grading rubric is not a controlling doctrine surface for proof/scoring semantics — it grades demand-read quality, not evidence tier. Even if recency semantics were present in it, they would be grading criteria, not proof-pathway enablers. The impact of an unchecked stale-language hit in the rubric would be low. The DCP claim is specific (named file) and therefore CA-checkable in one lookup.

**Why the defense does not fully eliminate the finding:** Under the validation-gates.md receipt-field provenance gate, a claimed downstream check that cannot be independently verified is `indeterminate_until_authored`. The grading rubric claim is checkable but not verified in this review.

**Impact:** Low — the rubric is a non-controlling surface unlikely to carry recency-as-proof language; but the DCP receipt cannot be taken as self-certifying under the provenance gate.

**Minimum closure condition:** CA reads `orca/product/spines/judgment/demand_read/grading/judgment_spine_demand_read_grading_rubric_v0.md` and confirms it contains no stale recency-as-proof/scoring language.

**Next authorized action:** CA spot-checks the grading rubric for recency wording before accepting this DCP receipt as fully verified.

**Recommended correction (advisory):** Either add a brief stale_language_search_result line for the rubric in the DCP receipt, or move the rubric to `intentionally_not_updated` with a reason (e.g., "grading quality criteria; no recency-as-proof language to update").

**patch_queue_entry:** Not authorized in this read-only lane.

---

## Findings — Phase 2 (Friction)

### AR-03 — MINOR (optional hardening) — C2 phrase "attention weighting" uses "weighting" without a disambiguating adjacent note

**Phase:** Friction

**Location:** Judgment demand-read core, C2 step, added text: "That attention weighting is not gate proof, numeric weight, or a scoring shortcut."

**Issue:** The noun phrase "attention weighting" (meaning the distribution of attention across signals based on recency) uses the word "weighting," which could create a momentary parsing ambiguity: a fast reader might initially parse "attention weighting" as a form of evidence weighting rather than as a modifier on how attention is distributed. The guard sentence is clear and complete, but the phrase structure could prompt a double-read.

**Evidence:** The full sentence is: "That attention weighting is not gate proof, numeric weight, or a scoring shortcut." INV-1 provides the authoritative constraint. The ambiguity is at the phrase level, not the sentence level.

**Strongest defense:** The full sentence is unambiguous as written. The guard clause "is not gate proof, numeric weight, or a scoring shortcut" directly addresses the scoring concern. INV-1 adds "must not be encoded as a numeric/ordinal weight or deterministic rule." No reader following both sources could conclude this is evidence weighting. This is friction, not correctness.

**Impact:** Minimal — no behavioral consequence found; the ambiguity does not create a proof or scoring path even under an adversarial reading of the phrase alone, given the surrounding guard text and INV-1.

**Minimum closure condition:** Optional — this finding does not require closure for acceptance.

**Next authorized action:** CA accepts as-is, or optionally rewrites to "That attention-priority rule is not gate proof, numeric weight, or a scoring shortcut" for disambiguation.

**patch_queue_entry:** Not authorized in this read-only lane. Advisory only.

---

## Fitness Reference Assessment

**Goal stated in review prompt:** Make recency/currentness increase attention and preservation priority across Scanning/CSB, Capture, and Judgment, without treating it as demand proof or downstream authority.

**Observable success signal stated in review prompt:** A fresh reader can start from Scanning/CSB, understand that newer/current URL-backed signals deserve more attention than same-strength older context, and see the exact downstream limits: CSB metadata only, Capture preservation urgency only, Judgment qualitative read attention only.

**Assessment:** The patch achieves the stated goal. All three spine changes correctly scope recency to attention/preservation/read-relevance. The downstream limits are explicit and consistent:
- CSB: `recency_status` and `recency_attention` as "source-route priority, not truth"
- Capture: "preservation urgency and source-drift risk" with explicit "does not prove demand, change the access-control gate, select a route by itself"
- Judgment C2: "attention and relevance input" with "not gate proof, numeric weight, or a scoring shortcut" and INV-1 hard constraint

A fresh reader following CSB → Capture → Judgment would encounter consistent, escalating boundary statements at each transition point.

**Axis-to-attack finding:** Whether the goal and signal are themselves correct. The goal is consistent with Orca's product thesis (outside-in consumer-demand decision intelligence that distinguishes durable demand from transient/manufactured). Making recency an attention prioritizer (not a proof escalator) is the correct semantic for a system that values source freshness without overclaiming from it. No axis-to-attack finding on the goal or signal.

---

## Residual Risks and Test Gaps

1. **Grading rubric unverified** (see AR-02): The Judgment grading rubric was not in this review's source pack. If it contains stale recency-as-proof language, it could create a routing inconsistency when demand-reads are graded. CA spot-check recommended before acceptance.

2. **Cross-spine stale search ran at HEAD state, not exactly at 13a1becb:** The stale/leakage search ran over the working tree, which is at HEAD (2de52237). The two commits between 13a1becb and HEAD were confirmed to not change the target files, but adjacent files may have changed. The search results are reliable for the 5 target files; adjacent files in between commits are not fully characterized. This residual is low-impact given the small delta (two commits) and the narrow review scope.

3. **Scanning README and MGT model not directly read end-to-end:** Stale-search confirms these contain correct "not proof" language, and both are named in the CSB and Capture DCP receipts as intentionally not updated. End-to-end read was not performed in this review. If those docs carry any stale language outside the search pattern, it would not have been caught here.

4. **Validator schema future drift:** The CSB validator selftest passed for existing test cases. If future board runs add `recency_attention: high` rows to handoff packets (Section 8), the validator does not check those rows for recency-boundary compliance (it checks cutoff, AEO, and future-info compliance only). An agent that misreads `recency_attention: high` in a handoff packet as evidence weight would not be caught by the validator. This is a future-design gap, not a current defect.

---

## Review-Use Boundary

This is a read-only adversarial artifact review. Findings and non-findings are Chief Architect decision input only. They are not approval, validation, readiness, mandatory remediation, source-of-truth promotion, product proof, implementation authorization, or executor-ready patch authority unless a separate authorized Orca decision or execution lane accepts them.

AR-01 and AR-02 are minor findings that may be accepted as-is or addressed before acceptance at CA discretion. AR-03 is optional hardening. The non-finding on proof/scoring/gate-binding leakage is the load-bearing result of this review.
