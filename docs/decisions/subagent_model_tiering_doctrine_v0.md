# Subagent Model-Tiering Doctrine v0

```yaml
retrieval_header_version: 1
artifact_role: Orca decision/doctrine (delegation model-tiering)
scope: >
  How Orca chooses which model tier a spawned subagent runs on, so mechanical /
  delegable work defaults to a cheaper tier (Sonnet, or Haiku for trivial rote)
  and Opus is reserved for genuine judgment — without over-restraining (Opus stays
  one explicit dispatch away). Enforcement is by pinned agent definitions, not a
  global hard cap.
use_when:
  - Spawning a subagent (Agent/Task tool) and choosing its model.
  - Authoring or reviewing custom agent definitions under `.claude/agents/`.
  - Deciding whether a delegated task needs Opus or a cheaper tier.
authority_boundary: retrieval_only
open_next:
  - .claude/agents/worker.md          # Sonnet default workhorse
  - .claude/agents/mechanical.md      # Haiku trivial-rote tier
  - .agents/workflow-overlay/decision-routing.md   # delegation routing owner
stale_if:
  - Claude Code changes the subagent model-resolution order or the agent-definition `model` field.
  - The tier mapping (mechanical→Haiku, default→Sonnet, judgment→Opus) is re-decided.
```

## Problem this fixes

A subagent spawned via the Agent/Task tool with **no `model` set** falls through
to the parent's model. When the parent (main loop) is Opus, ordinary delegated
work — captures, builds, rote edits — silently runs on **Opus**, which is
expensive overkill. The failure is an expensive *default*, not a missing gate.

## Decision

Tier by task, default cheap, keep Opus an easy opt-in:

- **Default delegated work → Sonnet.** Most delegable work (build to a stated
  pattern, capture/gather + verify, multi-step research, doc drafting) is
  Sonnet-grade. Route it to the **`worker`** agent type (pinned `model: sonnet`).
- **Trivial rote → Haiku.** Run-a-command, move/rename, precise find-replace →
  the **`mechanical`** type (pinned `model: haiku`).
- **Genuine judgment → Opus.** Novel design, compounding multi-step reasoning,
  subtle correctness on shared/contract-bearing surfaces, adversarial review →
  `general-purpose` (which inherits the main Opus tier) or an explicit
  `model: opus`. This stays available; it is a conscious choice, not the default.

**Do not collapse "mechanical" to Haiku.** Most delegated work needs Sonnet-grade
judgment (e.g. the Wayback capture builds had to pin domains, choose cutoffs,
handle rate-limits). Forcing Haiku there causes wrong results and redo — a false
economy worse than the Opus it avoids. Sonnet is the workhorse; Haiku is only
for genuinely trivial rote.

## Enforcement: pinned agent definitions, NOT a global cap

Verified Claude Code model-resolution order (highest → lowest):

1. `CLAUDE_CODE_SUBAGENT_MODEL` env var
2. per-call `model` arg on the Agent/Task tool
3. the agent definition's `model` frontmatter
4. inherit the parent (main loop) model

Enforcement is **(3)**: pin the model in the agent definition. Once work is
routed to `worker`/`mechanical`, the tier holds even if the orchestrator passes
no `model` — it can no longer silently inherit Opus.

**Rejected: `CLAUDE_CODE_SUBAGENT_MODEL` as a global default.** It sits at the
TOP of resolution and overrides even an explicit `model: opus` request, so
setting it to `sonnet` would make Opus subagents *impossible*. That is
over-restraint (it removes the escalation path), so Orca does **not** set it.
The control we want is "cheap by default, easy to escalate," not "block Opus."

**Hooks (optional, not adopted now).** A PreToolUse hook on the Agent tool can
inspect and even rewrite the model. Reserve it for a future *soft* signal (e.g.
log Opus spawns) if routing discipline proves insufficient — not a hard block,
which would re-introduce the over-restraint this doctrine avoids.

## Operating rule (for the orchestrator)

Default delegated work to `worker` (Sonnet). Use `mechanical` (Haiku) for
trivial rote. Reach for Opus (`general-purpose` / explicit `model: opus`) only
when the task earns it — and when it does, do so without hesitation.

## Non-claims

Advisory delegation doctrine. Not validation, readiness, a cost guarantee, or a
hard gate. It does not change any project's source hierarchy, review lanes, or
lifecycle authority; it governs only which model tier delegated subagents use.

## Propagation

- Added: `.claude/agents/worker.md` (sonnet), `.claude/agents/mechanical.md` (haiku).
- Pointer added in `.agents/workflow-overlay/decision-routing.md` (delegation routing owner).
