# Orca ICP Redo — DR Turn 2-B (Depth, Secondary Pair) Evidence Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Full prompt artifact
scope: Paste-ready evidence-gathering brief for an external deep-research model (Turn 2-B / depth, secondary pair). Per-core depth on Product-launch/GTM-timing and Marketing/paid-media mix.
use_when:
  - Running Turn 2-B (depth, secondary pair) of the ICP-redo evidence campaign.
  - Re-running or versioning the secondary depth pass.
authority_boundary: retrieval_only
open_next:
  - docs/research/orca_icp_redo_evidence_targets_v0.md
stale_if:
  - The locked shortlist or depth axes change.
  - Turn 2-B returns and the campaign moves to Turn 3 (convergence/winnability).
```

## Authoring preflight (this artifact)

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: S2 product anchor + prompt-orchestration + the evidence-targets note + the T1 results
  edit_permission: docs-write (additive prompt artifact)
  output_mode: paste-ready-chat
  target_scope: draft Turn 2-B (depth, secondary pair) evidence-only DR prompt
  repo_map_decision: not_needed
  repo_map_reason: the receiver is an external, non-repo-aware deep-research model; the body is self-contained
  dirty_state_checked: yes — artifact untracked, consistent with the uncommitted product/research set
  external_receiver: GPT-style deep-research model (NOT repo-aware; researches the public web)
  non_claims: market-context evidence only; not validation, WTP, readiness, or ICP selection
```

One of two concurrent Turn-2 depth passes (the other is Turn 2-A, priority
pair). Cores here are the locked secondary pair from the T1 synthesis. The model
gathers cited evidence only; the owner shuttles it back and Opus 4.8 synthesizes
and selects the Turn-3 finalists. Winnability, reachability, and WTP are NOT in
this pass — they are Turn 3.

## How to use

- Copy everything between the `=== PROMPT BODY ===` markers into the GPT
  deep-research model. This pass can run concurrently with Turn 2-A.
- Bring the returned evidence back. Opus 4.8 synthesizes Turn 2-A + Turn 2-B
  against the locked frame and narrows to the 1-2 finalists for Turn 3.

=== PROMPT BODY (paste into the deep-research model) ===

You are a market-evidence researcher. GATHER and CITE evidence only — do not
rank, score, select, recommend, or synthesize. A separate step does the
judgment.

This is one of two concurrent DEPTH passes. It covers two decision-cores. For
EACH core, gather cited evidence on four dimensions:

1. Recurrence / density (precise) — how often the decision happens per company
   per year, and population prevalence.
2. Stakes / magnitude — the money at risk / decision value / consequence size.
3. Servability detail — WHICH publicly observable signal surfaces exist for this
   decision and how rich they are; be specific about public vs private.
4. Decision-owner role — WHO owns this decision (title / role / function) and who
   is accountable for the budget or consequence.

# Core 1: Product launch / go-to-market timing

Scope: the DECISION of when and how to launch or time a product / feature / GTM
move (not the R&D work itself). This is mixed public/private:

- Capture what PUBLIC signal informs the launch / timing decision (competitor
  launches, market or community reaction, analyst signal, seasonality, category
  momentum).
- Note the private side (internal readiness, development financing, internal-
  finance constraints) but flag it as private.

Sources: launch announcements, issuer disclosures tying launches to results,
analyst / industry studies, primary innovation surveys.

# Core 2: Marketing budget / paid-media and channel mix

Scope: allocation of marketing / paid-media budget across channels and campaigns
— the decision of where and how to spend.

- Servability detail to capture precisely: what is publicly observable
  (competitor ads via Meta Ad Library and Google Ads Transparency Center; public
  creative / campaign signals) vs private (first-party data, internal ROAS, data
  clean rooms). Capture the cadence too (annual budget cycle vs in-flight
  reallocation).

Sources: analyst CMO-spend surveys, ad-transparency platforms, industry bodies
(e.g., IAB), primary studies.

# Output format

Per core, a structured block per dimension. Each data point as: claim —
figure/fact — publisher — date — URL — confidence (high / med / low). End with a
"Gaps" section.

# Hard rules

- EVIDENCE ONLY: no ranking, scoring, selection, recommendation, or synthesis.
- No fabrication. Ranges, not false precision. Separate primary data from analyst
  estimates from your own inference.
- Every figure traceable to a named source with a date and URL.

=== END PROMPT BODY ===

## Non-claims

This prompt gathers market-context evidence only. It does not assert buyer
validation, willingness-to-pay, readiness, buyer pull, or an ICP/wedge
selection. Selection and synthesis remain with the owner and Opus 4.8.
