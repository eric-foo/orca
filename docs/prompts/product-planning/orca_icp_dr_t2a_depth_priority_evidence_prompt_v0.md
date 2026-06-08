# Orca ICP Redo — DR Turn 2-A (Depth, Priority Pair) Evidence Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Full prompt artifact
scope: Paste-ready evidence-gathering brief for an external deep-research model (Turn 2-A / depth, priority pair). Per-core depth on Pricing/packaging and Competitive-response/positioning.
use_when:
  - Running Turn 2-A (depth, priority pair) of the ICP-redo evidence campaign.
  - Re-running or versioning the priority depth pass.
authority_boundary: retrieval_only
open_next:
  - docs/research/orca_icp_redo_evidence_targets_v0.md
stale_if:
  - The locked shortlist or depth axes change.
  - Turn 2-A returns and the campaign moves to Turn 3 (convergence/winnability).
```

## Authoring preflight (this artifact)

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: S2 product anchor + prompt-orchestration + the evidence-targets note + the T1 results
  edit_permission: docs-write (additive prompt artifact)
  output_mode: paste-ready-chat
  target_scope: draft Turn 2-A (depth, priority pair) evidence-only DR prompt
  repo_map_decision: not_needed
  repo_map_reason: the receiver is an external, non-repo-aware deep-research model; the body is self-contained
  dirty_state_checked: yes — artifact untracked, consistent with the uncommitted product/research set
  external_receiver: GPT-style deep-research model (NOT repo-aware; researches the public web)
  non_claims: market-context evidence only; not validation, WTP, readiness, or ICP selection
```

One of two concurrent Turn-2 depth passes (the other is Turn 2-B, secondary
pair). Cores here are the locked priority pair from the T1 synthesis. The model
gathers cited evidence only; the owner shuttles it back and Opus 4.8 synthesizes
and selects the Turn-3 finalists. Winnability, reachability, and WTP are NOT in
this pass — they are Turn 3.

## How to use

- Copy everything between the `=== PROMPT BODY ===` markers into the GPT
  deep-research model. This pass can run concurrently with Turn 2-B.
- Bring the returned evidence back. Opus 4.8 synthesizes Turn 2-A + Turn 2-B
  against the locked frame and narrows to the 1-2 finalists for Turn 3.

=== PROMPT BODY (paste into the deep-research model) ===

You are a market-evidence researcher. GATHER and CITE evidence only — do not
rank, score, select, recommend, or synthesize. A separate step does the
judgment.

This is one of two concurrent DEPTH passes. It covers two decision-cores. For
EACH core, gather cited evidence on four dimensions:

1. Recurrence / density (precise) — how often the decision happens per company
   per year, and population prevalence. Refine beyond rough rates where possible.
2. Stakes / magnitude — the money at risk / decision value / consequence size
   (revenue, margin, or churn exposure; typical decision budget).
3. Servability detail — WHICH publicly observable signal surfaces exist for this
   decision and how rich they are. Be specific about what is publicly visible vs
   not.
4. Decision-owner role — WHO owns this decision inside a company (title / role /
   function) and who is accountable for the budget or consequence.

# Core 1: Pricing / packaging / monetization

Scope: pricing changes, packaging / plan / tier changes, usage / consumption /
billing-model changes, add-on and AI-add-on monetization, and package
migrations. This recurs economy-wide, so gather CROSS-SECTOR coverage
(software/SaaS plus others such as CPG, retail, and services), not software
only.

Sources: official company pricing pages, changelogs, pricing-change
announcements and FAQs; analyst pricing studies; primary surveys.

- Servability detail to capture: pricing pages, changelogs, pricing-change
  announcements, competitor pricing moves, customer / developer / community
  reaction, review-site signals — which exist and how rich.
- Decision-owner role to capture: who owns a pricing/packaging decision (e.g.,
  pricing or packaging lead, VP Product, GM, monetization owner, PMM, founder)
  across company types.

# Core 2: Competitive-response / positioning

Scope: a decision to respond to a competitor's move (pricing, packaging,
feature, narrative, category) or to shift one's own positioning / messaging,
where public competitor or market signal is available.

IMPORTANT: population-wide recurrence statistics for this core generally do NOT
exist — it is not surveyed. Use a CASE-BASED approach:

- Find 6–10 concrete, documented instances across sectors of a company making a
  competitive-response or positioning decision. For EACH case capture: what the
  decision was; what public signal was available (competitor announcement,
  press, analyst note, community / customer reaction); the stakes / consequence;
  who owned it (role); and the date.
- Then gather any available FREQUENCY PROXIES (e.g., how often firms in a
  fast-moving category respond to competitor moves). If no denominator exists,
  say so — do NOT invent one.

Sources: company announcements, reputable press, analyst notes, primary case
write-ups.

# Output format

Per core, a structured block per dimension. Each data point as: claim —
figure/fact — publisher — date — URL — confidence (high / med / low). For Core 2,
also a case table: case | decision | public signal | stakes | owner role | date
| source. End with a "Gaps" section.

# Hard rules

- EVIDENCE ONLY: no ranking, scoring, selection, recommendation, or synthesis.
- No fabrication. Ranges, not false precision. Separate primary data from analyst
  estimates from your own inference.
- For Core 2, do NOT fabricate a population denominator; report cases + proxies +
  gaps.
- Every figure traceable to a named source with a date and URL.

=== END PROMPT BODY ===

## Non-claims

This prompt gathers market-context evidence only. It does not assert buyer
validation, willingness-to-pay, readiness, buyer pull, or an ICP/wedge
selection. Selection and synthesis remain with the owner and Opus 4.8.
