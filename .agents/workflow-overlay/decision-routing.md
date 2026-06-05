# Cynefin Routing Layer

```yaml
retrieval_header_version: 1
artifact_role: Orca overlay authority
scope: Lightweight Cynefin-based pre-planning router for non-trivial Orca work.
use_when:
  - Deciding whether to plan, delegate, review, patch, or implement.
  - Starting substantial, ambiguous, cross-thread, or doctrine-bearing work.
  - Recovering a drifting or messy workstream before more agents act.
authority_boundary: retrieval_only
```

This file owns Orca's lightweight Cynefin Routing Layer. It prevents agents
from planning or delegating before they have classified the uncertainty regime,
named the current constraint, and chosen a safe next move.

## Rule

Run Cynefin routing before planning, delegation, prompt execution, review,
patching, or infrastructure work when the task is non-trivial and could fail
because the wrong decomposition strategy is chosen.

Use the smallest complete router. This is not a full Bayesian planning system,
audit log, review lane, validation gate, or project-management ritual. It is a
short preflight that constrains the next move.

## Trigger Conditions

Run the router when any of these are true:

- the user asks for architecture, planning, scoping, route selection, or the
  next move;
- the user asks to spawn agents, delegate work, execute a prompt, perform
  review, apply a patch, or commission another lane;
- the task references another thread as evidence or continuity context;
- the task touches `AGENTS.md`, the Orca overlay, prompt templates, review
  lanes, validation gates, source hierarchy, or durable workflow doctrine;
- the task would build infrastructure before a material assumption has been
  proven;
- the worktree, source map, or ownership boundary is dirty enough that a safe
  commit, patch, or claim boundary is unclear;
- the current thread shows drift: many artifacts or actions, unclear
  bottleneck, weak convergence, or no visible stop condition.

## Bypass Conditions

Do not run the router for narrow, clear, already-scoped work:

- tiny edits, typo fixes, or mechanical formatting;
- direct command answers;
- already accepted implementation steps with bounded touch points and validation;
- narrow doc cleanup where ownership is obvious;
- simple bug fixes with an obvious test path and no doctrine or review impact.

If bypassing could be contested, state a one-line bypass reason before acting.

## Router Output

Use this compact shape:

```text
decision_routing:
  regime: clear | complicated | complex | chaotic
  why:
  decomposition:
  current_bottleneck:
  riskiest_assumption:
  stop_or_pivot_condition:
  allowed_next_move:
  disallowed_next_move:
  bypass_reason:
```

Omit `bypass_reason` when the router runs. Use `bypass_reason` only when the
router is intentionally skipped.

## Regimes

`clear`: the task is understood, bounded, and mechanically executable.
Use functional decomposition or direct execution.

`complicated`: the task needs expertise, source hierarchy, or layered ownership,
but the target can be reasoned through from current sources.
Use layer-based decomposition.

`complex`: key assumptions are uncertain, evidence could change the route, or
building first would create fragile infrastructure.
Use risk-first probes. Resolve the highest-uncertainty assumption before
expanding implementation or delegation.

`chaotic`: state is too unstable to plan safely, usually because scope, source
truth, repo state, or authority is disordered.
Stabilize first: classify dirty state, bind authority, narrow the target, or
name the hard stop before any broader task tree.

## Execution Contract

The router must produce an allowed next move and a disallowed next move before
planning continues. The disallowed move is load-bearing: it prevents the agent
from turning spare capacity into non-bottleneck work.

For complex work, the allowed next move should normally be a probe, source read,
owner decision, scoped contract, or narrow adapter/surface step that resolves
the riskiest assumption. Do not estimate end dates or build infrastructure
around unproven assumptions.

For chaotic work, do not assign parallel work until the bottleneck is visible.
Idle agents are acceptable when non-bottleneck work would increase WIP or blur
claim boundaries.

## Prompt Propagation

Repo-aware prompts, wrappers, handoffs, review prompts, patch prompts, and
reruns must include Cynefin routing when their task matches the trigger
conditions. Prompt artifacts should reference this file instead of restating
the whole router.

## Non-Claims

Cynefin routing is not validation, readiness, approval, acceptance, review,
implementation authorization, source-of-truth promotion, or proof that a route
will work. It is a pre-planning constraint on how the next move is chosen.
