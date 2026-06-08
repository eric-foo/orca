# Orca ICP Redo — DR Convergence (Sharpened) Evidence Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Full prompt artifact
scope: Paste-ready evidence-gathering brief for an external deep-research model. Sharpened convergence pass that discriminates the two first-proof finalists — (A) pricing's outside-in slice and (B) break-in / competitor-customer / win-loss intelligence — on winnability / reachability / WTP, brings finalist B up to evidence parity, and pulls a cited TAM / market-size.
use_when:
  - Running the sharpened convergence pass of the ICP-redo evidence campaign.
  - Re-running or versioning the convergence pass.
authority_boundary: retrieval_only
open_next:
  - docs/research/orca_icp_redo_evidence_targets_v0.md
stale_if:
  - The two finalists, the buyer frame, or the convergence axes change.
  - The pass returns and the campaign moves to owner + Opus selection.
```

## Authoring preflight (this artifact)

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: S2 product anchor + prompt-orchestration + the evidence-targets note (Convergence section) + the T1/T2 results
  edit_permission: docs-write (additive/replacing prompt artifact)
  output_mode: paste-ready-chat
  target_scope: rewrite the convergence pass to the pricing-vs-break-in discriminator + outside-in-dependence probe + TAM sizing
  repo_map_decision: not_needed
  repo_map_reason: the receiver is an external, non-repo-aware deep-research model; the body is self-contained
  dirty_state_checked: yes — artifact untracked, consistent with the uncommitted product/research set
  external_receiver: GPT-style deep-research model (NOT repo-aware; researches the public web)
  non_claims: market-context evidence only; not validation, WTP, readiness, or ICP selection
```

The sharpened convergence pass. The field has converged to two first-proof
finalists, both served by one engine (outside-in competitive & market
intelligence): (A) pricing's outside-in slice, and (B) break-in /
competitor-customer / win-loss intelligence. The model GATHERS cited evidence on
both; the owner shuttles it back and Opus 4.8 discriminates and selects. The
discrimination and selection are NOT the model's job — it only gathers.

## How to use

- Copy everything between the `=== PROMPT BODY ===` markers into the GPT
  deep-research model. One pass, both finalists + a market-size block.
- Bring the returned evidence back. Opus 4.8 runs the best-evidenced (A) vs
  best-fit (B) discrimination against the locked frame and supports the owner's
  final selection.

=== PROMPT BODY (paste into the deep-research model) ===

You are a market-evidence researcher. GATHER and CITE evidence only — do not
rank, score, select, recommend, compare, or synthesize. A separate step does all
judgment.

Gather cited evidence on TWO decision-cores and ONE market-size block.

# Core A: Pricing — outside-in slice

Scope: pricing / packaging / monetization decisions where the TRIGGER or decisive
input comes from OUTSIDE the company — a competitor's pricing or packaging move, a
first-time AI-feature monetization with little internal history, or public
customer/community backlash to a pricing change. (Routine internal-data-driven
repricing is out of scope for this pass.)

Gather, for this slice:
1. Recurrence / density — how often firms make externally-triggered pricing moves
   (competitor-driven, AI-monetization-driven, backlash-driven).
2. Stakes / magnitude — money/consequence at risk in these moves.
3. Servability — which PUBLIC surfaces inform the decision (competitor pricing
   pages, changelogs, customer/community reaction, review sites) and how rich.
4. Decision-owner role — who owns it (title/function) and who is accountable.
5. Provider landscape / new-entrant evidence — who currently supplies help with
   these decisions (consultancies, pricing boutiques, pricing/monetization
   software, in-house); how concentrated; named new/recent entrants with traction.
6. Willingness-to-pay — published prices/fees for pricing decision support across
   consulting, boutique sprints, and tooling (incl. any AI-pricing tooling).
7. In-house-vs-bought evidence — evidence on whether firms do the OUTSIDE-IN read
   (competitor/market) internally or buy it (internal roles/teams vs external
   vendors; any adoption rates).

# Core B: Break-in / competitor-customer / win-loss intelligence

Scope: the decision to win customers away from competitors or break into a market
by understanding WHY prospects buy from competitors and not from you, and what
would move them. This core is NEWER to this campaign, so gather the foundational
dimensions too — do not assume prior coverage.

Gather, for this core:
1. Recurrence / density — how often firms run win/loss analysis, competitor-
   customer / switching research, or market-entry research; any prevalence data.
   If no clean denominator exists, say so and use case-based evidence — do NOT
   fabricate a rate.
2. Stakes / magnitude — consequence size of getting break-in / competitive
   displacement / market-entry right or wrong.
3. Servability — which PUBLIC surfaces reveal why a competitor's customers choose
   them and what they dislike (review sites such as G2/Trustpilot/Capterra,
   "why I switched / why I left X" content, community forums, social, comparison
   sites, app-store reviews); how rich and how reliable.
4. Decision-owner role — who owns win/loss, competitive intelligence, or
   market-entry (e.g., product marketing, competitive-intelligence lead, growth,
   CMO, founder) and who holds the budget.
5. Provider landscape / new-entrant evidence — who supplies win/loss and
   competitor-customer intelligence today (win/loss agencies and vendors,
   competitive-intelligence software, research firms, in-house teams); how
   concentrated; named new/recent entrants with traction.
6. Willingness-to-pay — published prices/fees for win/loss programs, competitive-
   intelligence subscriptions/tools, and competitor/market research.
7. In-house-vs-bought evidence — evidence on whether firms do this internally or
   buy it (internal CI/win-loss roles vs external providers; adoption rates).

# Market-size block (for both, plus the umbrella)

Gather cited market-size figures (ranges, with sources and dates) for:
- Competitive-intelligence market (software and/or services).
- Market-research industry.
- Win/loss analysis market, if any sizing exists.
- Pricing / strategy consulting market.
- Any population proxies for the umbrella buyer: how many companies per year
  enter a new market, launch a new product line, or face a newly surfaced
  competitor (entrant/challenger proxies). If only partial proxies exist, report
  them and say what is missing — do NOT fabricate a total.

# Output format

Per core, a structured block per dimension. Each data point as: claim —
figure/fact — publisher — date — URL — confidence (high / med / low). For each
core's provider landscape, include a table: provider/vendor | type (consultancy /
boutique / agency / software / in-house) | new-or-established | traction signal |
source. Put the market-size block in its own section with a table. End with a
"Gaps" section.

# Hard rules

- EVIDENCE ONLY: no ranking, scoring, selection, recommendation, comparison, or
  synthesis.
- No fabrication. Ranges, not false precision. Separate primary data from analyst
  estimates from your own inference.
- Do NOT fabricate denominators or prices. For Core B recurrence and for the
  market-size proxies, report cases + proxies + gaps if no clean figure exists.
- Keep Core A and Core B evidence clearly separated.
- Every figure traceable to a named source with a date and URL.

=== END PROMPT BODY ===

## Non-claims

This prompt gathers market-context evidence only. It does not assert buyer
validation, willingness-to-pay, readiness, buyer pull, newcomer-winnability,
market size as demand, or an ICP/wedge selection. Discrimination, synthesis, and
selection remain with the owner and Opus 4.8, after this pass returns.
