# Orca ICP Redo — DR Turn 1 (Breadth) Evidence Prompt v0

```yaml
retrieval_header_version: 1
artifact_role: Full prompt artifact
scope: Paste-ready evidence-gathering brief for an external deep-research model (Turn 1 / breadth of the ICP-redo DR campaign). Open cross-sector scan for recurring high-stakes decision-cores with cited density, stakes, and public-vs-private evidence.
use_when:
  - Running Turn 1 (breadth) of the ICP-redo evidence campaign.
  - Re-running or versioning the breadth pass.
authority_boundary: retrieval_only
open_next:
  - docs/research/orca_icp_redo_evidence_targets_v0.md
stale_if:
  - The decided frame, axes, or dial weights change.
  - Turn 1 returns and the campaign moves to Turn 2 (depth).
```

## Authoring preflight (this artifact)

```text
orca_start_preflight:
  agents_read: yes
  overlay_read: yes
  source_pack: S2 product anchor + prompt-orchestration + artifact-roles + the evidence-targets note
  edit_permission: docs-write (additive prompt artifact)
  output_mode: paste-ready-chat
  target_scope: draft Turn-1 (breadth) evidence-only DR prompt
  repo_map_decision: not_needed
  repo_map_reason: the receiver is an external, non-repo-aware deep-research model; the body is self-contained
  dirty_state_checked: yes — artifact untracked, consistent with the uncommitted product/research set
  external_receiver: GPT-style deep-research model (NOT repo-aware; researches the public web)
  non_claims: market-context evidence only; not validation, WTP, readiness, or ICP selection
```

Serves the evidence-targets note `docs/research/orca_icp_redo_evidence_targets_v0.md`.
Division of labor: the external model gathers cited evidence only; the owner
shuttles it back and Opus 4.8 synthesizes/prunes to the Turn-2 shortlist. The
model must not select, rank, or recommend.

## How to use

- Copy everything between the `=== PROMPT BODY ===` markers into the GPT
  deep-research model.
- Bring the returned evidence back. Opus 4.8 synthesizes it against the decided
  frame and produces the shortlist of cores that proceed to Turn 2 (depth).
- Do not ask this pass for depth, winnability, reachability, or a recommendation
  — those are later turns.

=== PROMPT BODY (paste into the deep-research model) ===

You are a market-evidence researcher. Your job is to GATHER and CITE evidence —
not to analyze, rank, score, select, or recommend. A separate step does the
judgment. Stay strictly inside the evidence-gathering role.

# Objective

Run an OPEN, cross-sector scan of the economy to surface the recurring,
high-stakes BUSINESS DECISIONS that companies repeatedly make ("decision-cores").
For each one, gather cited statistics on exactly three dimensions:

1. Recurrence / density — how often the decision happens: per company per year,
   and how widespread it is across the population of companies. (This is the
   "how often can it recur / how harvestable" dimension.)
2. Stakes / magnitude — how much is at stake when the decision is made: budget at
   risk, revenue / cost / churn exposure, or typical decision value.
3. Public-vs-private — is the decision typically informed by PUBLICLY observable
   signals (pricing pages, public customer/competitor/community reaction,
   reviews, changelogs, analyst/press coverage, public filings), or decided on
   PRIVATE/confidential data (internal financials, data-room diligence,
   proprietary usage)? Tag each core: "public-signal-affectable", "mixed", or
   "private/confidential".

# What counts as a "decision-core"

A recurring TYPE of consequential business decision an accountable owner makes.
Examples that show the unit (NOT the full list):

- pricing / packaging / monetization changes (incl. AI add-on or usage-based repricing)
- competitive response / positioning decisions
- category or market entry
- product launch / go-to-market timing

These are only examples of the *kind* of thing. Scan OPENLY across all sectors —
software, consumer/CPG, healthcare, financial services, industrials, retail,
media, energy, telecom, etc. — and surface ANY recurring high-stakes
decision-cores you find, especially ones not in the list above.

# Excluded class (still gather, but flag)

Decisions usually decided on private/confidential data — M&A, IPO / financing,
major capex, internal restructuring, anything decided in a data room — should be
INCLUDED in the scan but clearly tagged "private/confidential" so they can be set
aside later. Do not omit them; flag them.

# Sources (authoritative only)

Prioritize PRIMARY and AUTHORITATIVE sources: analyst primary reports (e.g.
Gartner, Forrester, IDC, Bessemer, ICONIQ, OpenView), primary surveys that state
a sample size, industry or government statistics, and official filings or
disclosures. Company pricing pages and changelogs are fine as concrete examples
but are company-specific (weak for a cross-sector *density* claim). AVOID SEO
content-farm blogs and low-authority aggregators; if only a secondary/aggregator
source exists for a point, label it as secondary and name the original source if
you can find it.

# Output format

Return a structured table or one block per decision-core. For each:

- Decision-core name
- Sector(s) where it is most prominent
- Recurrence / density — each data point as: claim — figure — publisher — date — URL — confidence (high / med / low)
- Stakes / magnitude — same format
- Public-vs-private tag — public-signal-affectable / mixed / private — with the cited evidence behind the tag
- Source-quality note — is each figure primary data, an analyst estimate, or your own inference?

Then add two sections:

- "Newly surfaced cores" — decision-cores you found in the open scan that were
  not in the example list, with the same fields.
- "Gaps" — dimensions or cores where you could not find authoritative evidence.

# Hard rules

- EVIDENCE ONLY. Do NOT rank the cores, score them, pick a best one, recommend an
  ICP or target, or write a synthesis/conclusion. Present cited evidence; the
  judgment happens in a separate step.
- Do NOT fabricate figures, publishers, dates, or URLs. If you cannot find
  something, put it in "Gaps".
- Use RANGES, not false precision. Clearly separate primary data from analyst
  estimates from your own reasoning.
- Breadth over depth: cover the option set across sectors with rough-but-cited
  stats on the three dimensions. Deep per-core profiling is a later step — not
  now.
- Every figure must be traceable to a named source with a date and a URL.

=== END PROMPT BODY ===

## Non-claims

This prompt gathers market-context evidence only. It does not assert, and must
not be read as, buyer validation, willingness-to-pay, readiness, buyer pull, or
an ICP/wedge selection. Selection and synthesis remain with the owner and
Opus 4.8.
