# Orca Break-In Lock — Verification (Decisive-Axis + Substitution/Servability) Evidence Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Full prompt artifact
scope: Paste-ready evidence-gathering brief for an external deep-research model. Verifies the break-in-first lock's weakest links before the product-doc cascade — (1) DE-VENDOR the decisive in-house-vs-bought axis with INDEPENDENT sources, and (2) the load-bearing crux the lock never tested - whether anyone buys a PUBLIC-SIGNAL (non-interview) competitor-customer / market-entry read, and whether the public substrate is rich enough to produce one.
use_when:
  - Verifying the break-in-first lock before hardening / cascading.
  - Re-running or versioning the verification pass.
authority_boundary: retrieval_only
open_next:
  - docs/decisions/orca_icp_wedge_convergence_break_in_first_v0.md
  - docs/research/orca_icp_redo_evidence_targets_v0.md
stale_if:
  - The lock's decisive axis or narrow framing changes.
  - The verification returns and the cascade proceeds.
```

## Authoring preflight (this artifact)

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: S2 product anchor + prompt-orchestration + the decision record (poke amendment) + the ledger
  edit_permission: docs-write (additive prompt artifact)
  output_mode: paste-ready-chat
  target_scope: verify the break-in lock's decisive axis + the public-signal substitution/servability crux
  repo_map_decision: not_needed
  repo_map_reason: external, non-repo-aware deep-research model; the body is self-contained
  dirty_state_checked: yes — artifact untracked, consistent with the uncommitted product/research set
  external_receiver: GPT-style deep-research model (NOT repo-aware; researches the public web)
  non_claims: market-context evidence only; not validation, WTP, readiness, or ICP selection
```

This pass exists because the break-in-first lock's decisive evidence was
asymmetrically sourced (one side vendor-published, the other a logged gap) and
its hardest assumption — that buyers will pay for a PUBLIC-SIGNAL read rather
than buyer INTERVIEWS — was never tested. SOURCE INDEPENDENCE is the point of
this pass: flag every figure as VENDOR (sold by a firm that profits from the
answer) vs INDEPENDENT (government, academic, neutral analyst, or a party with no
stake).

## How to use

- Copy everything between the `=== PROMPT BODY ===` markers into the deep-research
  model. Bring the result back to its own clearly-named file.
- Opus 4.8 synthesizes it against the locked frame; selection stays with the
  owner + Opus.

=== PROMPT BODY (paste into the deep-research model) ===

You are a market-evidence researcher. GATHER and CITE evidence only — do not
rank, score, select, recommend, or synthesize. For EVERY figure, tag the source
as INDEPENDENT (government, academic, neutral analyst, or a party with no
commercial stake in the answer) or VENDOR (published by a firm that sells the
service in question). Source independence is the primary concern of this pass.

# Core 1: De-vendor the decisive axis (external-help purchase rates)

Find INDEPENDENT (non-vendor) evidence on how often companies buy EXTERNAL help
vs do it in-house for:
1a. Competitor-customer / win-loss / competitive-market intelligence.
1b. Pricing / packaging / monetization decisions.
Prefer government, academic, or neutral cross-industry surveys. For any rate that
exists only from a vendor (e.g., a win/loss software firm's survey), say so and
mark it VENDOR. If no independent denominator exists, say so explicitly — do NOT
fill the gap with a vendor figure presented as neutral.

# Core 2: The substitution crux (PUBLIC-SIGNAL vs INTERVIEW demand)

The existing win/loss market is built on INTERVIEWING the lost buyer. The
question: is there demand for a PUBLIC-SIGNAL-ONLY read (no interviews) of why a
competitor's customers choose it / what would move them / whether to enter a
market?
- Find any providers/products that sell a PUBLIC-SIGNAL-derived competitor-
  customer or market-entry decision artifact (NOT interview-based, NOT a raw
  monitoring dashboard). Capture what they sell, to whom, and published prices.
- Find evidence on whether buyers treat public-signal competitor-customer reads
  as decision-grade, or insist on interviews / first-party data for the decision.
- If the evidence shows demand is essentially interview-gated, say so plainly.

# Core 3: Substrate servability for the narrow form

How rich, fresh, and reliable is the PUBLIC substrate for producing a
competitor-displacement / market-entry read — specifically incumbent-customer
complaint clusters, switching narratives ("why I left X"), and unmet-need signal
across review sites, forums, communities, app stores, and changelogs?
- Capture coverage/volume and any reliability problems (fake/selective reviews,
  staleness, self-selection). Be specific about which categories have thick vs
  thin public switching signal.

# Core 4: The narrow-form buyer + retainer density

For the "challenger deciding whether to enter / attack a market where it has NO
existing pipeline" buyer:
4a. Who owns that decision (title/function) and how often companies make it.
4b. Crucially: is there any buyer class that makes it ON A CADENCE (serial
    acquirers, multi-product platform companies, PE/portfolio operators, agencies
    serving many clients) — i.e., a RECURRING buyer for episodic market-entry
    reads? This tests whether the narrow wedge can support a retainer.
4c. What such buyers currently do / buy for this, and any published prices.

# Core 5 (secondary): Commercial / market-side diligence adjacency

Size and describe the market for OUTSIDE-IN commercial due diligence (the market/
competitive/customer-sentiment read for an investment or acquisition — NOT the
financial data room): who buys it, who supplies it, published prices/market size.
Mark independent vs vendor.

# Output format

Per core, a structured block. Each data point: claim — figure/fact — source type
(INDEPENDENT / VENDOR) — publisher — date — URL — confidence. End with a "Gaps"
section listing what could not be found independently.

# Hard rules

- EVIDENCE ONLY: no ranking, scoring, selection, recommendation, or synthesis.
- Tag INDEPENDENT vs VENDOR on every figure. Do NOT present a vendor figure as
  neutral.
- No fabrication. Ranges, not false precision. If a denominator/price/size does
  not exist publicly, say so.
- Every figure traceable to a named source with a date and URL.

=== END PROMPT BODY ===

## Non-claims

This prompt gathers market-context evidence only. It does not assert buyer
validation, willingness-to-pay, readiness, buyer pull, newcomer-winnability, or
an ICP/wedge selection. Synthesis and selection remain with the owner and
Opus 4.8.
