# Overlay Enforcement-Placement Classification v0

```yaml
retrieval_header_version: 1
artifact_role: Orca decision record
scope: >
  Prepare-only classification of the Orca overlay's resident rules by enforcement
  placement (deterministic substrate vs genuine judgment), with proposed substrate
  for the code-enforceable rules and a proposed (not bound) overlay pointer to the
  shared enforcement-placement principle. Builds, installs, and authorizes nothing.
use_when:
  - Deciding which overlay rules to harden in a deterministic substrate vs keep resident.
  - Scoping owner authorization to build a governance hook / test / schema / lint.
  - Later binding the shared enforcement-placement doctrine to Orca (separate task).
authority_boundary: retrieval_only
open_next:
  - .agents/workflow-overlay/safety-rules.md        # owner gate for building any substrate
  - .agents/workflow-overlay/validation-gates.md    # current (resident) gate set
  - .agents/workflow-overlay/retrieval-metadata.md  # the jb-exemplar domain (header rule)
stale_if:
  - A governance substrate is actually built/installed (proposed rows become moved).
  - A cross-repo shared home for the enforcement-placement doctrine is created (the Step-4 pointer can then bind).
  - The overlay's resident rules materially change.
```

## Status

Prepare-only **proposal + classification**. It inventories and classifies rules that already exist in the overlay and proposes where each could be enforced. It **builds nothing, installs nothing, wires nothing into `.claude/settings.json`, edits no overlay-authority file, and authorizes no implementation.** It is **not a doctrine change** (no durable rule was edited; this is a classification of existing rules), so **no `direction_change_propagation` receipt is owed**. No readiness, validation, or proof claim is made. Building any proposed substrate is **owner-gated** under `.agents/workflow-overlay/safety-rules.md`.

Scope guard: this is the **enforcement-placement step only**. Binding the shared distillation doctrine to Orca is a separate later task and is explicitly out of scope here (see § Step 4).

## Update — 2026-06-09: EP-06 substrate built and wired

The retrieval-header substrate proposed here (EP-06; Appendix B) has since been
built and wired under explicit current-turn owner authorization (the
`safety-rules.md` owner gate named in § Owner gate):

- checker: `.agents/hooks/check_retrieval_header.py` — advisory + `--strict`
  CI/commit mode, forward-only, references `retrieval-metadata.md`; **EP-06
  presence/shape only** (EP-07 forbidden-field scan deferred);
- hook: a `PostToolUse` (`Write|Edit`) entry in `.claude/settings.json`;
- doctrine: a thin Enforcement Placement principle in
  `.agents/workflow-overlay/validation-gates.md` (cross-referenced from
  `decision-routing.md`), with discoverability + reinstall in the repo map's
  "Active Hooks" note.

This trips the `stale_if` "a governance substrate is actually built/installed":
EP-06 is now built; the remaining rows stay proposals, each still owner-gated.
See the `direction_change_propagation` receipt in
`.agents/workflow-overlay/source-of-truth.md`. This update adds no new claim;
the substrate is advisory tooling, not validation, readiness, or approval.

## Update — 2026-06-09: EP-01 + EP-03 floor built (config, no script)

The smallest-complete safety floor proposed here (EP-01 protected paths, EP-03
git lifecycle) is now built under explicit current-turn owner authorization, as
Claude Code `permissions` rules — deliberately config, not a script (the
bad-minimizing form):

- **`ask` — git lifecycle** (`git push`/`commit`/`remote`, `gh pr`,
  `git reset --hard`, `git clean`) for both the `Bash` and `PowerShell` tools,
  shared/tracked in `.claude/settings.json`. The approval prompt is the
  authorization (`safety-rules.md` "...unless explicitly authorized").
- **`deny` — protected paths** (writes/edits to `agent-workflow`, `jb*`,
  `~/.codex/{plugins,skills}`, `~/.claude/{plugins,skills}`, `~/.agents/skills`),
  machine-local in `.claude/settings.local.json` (machine-specific absolute
  paths; a fresh clone re-adds its own).
- **EP-02 deliberately excluded** from the floor (impl-dir blocking would
  false-block legitimate `orca-harness/` work; lower value).
- Discoverability: the repo map "Active Hooks" note was extended. Authority:
  `safety-rules.md` + validation-gates "Enforcement Placement".

This trips `stale_if` "a governance substrate is actually built/installed":
EP-01 and EP-03 are now built; the remaining rows stay proposals. **No new
doctrine** (no overlay rule changed; placement is not authority —
`safety-rules.md` already carried these rules and validation-gates already
carries the principle), so no new `direction_change_propagation` receipt is
owed. **Not yet live-verified:** Claude Code loads permissions at session start,
so the floor activates only after a restart, and PowerShell-tool matching is per
the Claude Code permissions reference, not live-fired in this session. Config
tooling, not validation, readiness, or approval.

## Update — 2026-06-09: EP-01 + EP-03 also enforced by a PreToolUse hook (auto-mode)

Live verification of the config floor showed the `ask` rules are **inert in auto
/ bypass mode** (no human to prompt — the agent's own `git remote -v` ran with no
gate). So under explicit current-turn authorization, EP-01 + EP-03 are now also
enforced by a **`PreToolUse` hook** that fires in ALL permission modes:

- `.agents/hooks/guard_protected_actions.py` (matcher
  `Bash|PowerShell|Write|Edit|MultiEdit|NotebookEdit` in `.claude/settings.json`);
  exit-2 blocks protected-path writes (`agent-workflow`, `jb*`, user-level
  plugin/skill caches) and dangerous git (`push`, `reset --hard`, `clean`) via
  either shell. Narrow: `commit` and generic deletion are not blocked. Fails open
  on internal error; has `--selftest`.
- The config `ask`/`deny` rules stay as interactive-mode belt-and-suspenders; the
  hook is the primary, mode-independent enforcement.
- **Logic verified this session** (selftest 15/15; live `git push` payload → exit
  2, `git status` → exit 0). **Hook wiring goes live after a Claude Code restart**
  (hooks load at session start); per the Claude Code docs, PreToolUse hooks run
  and block even under auto / bypass mode.
- No overlay rule changed → still no doctrine change / no DCP receipt. Config and
  hook tooling, not validation, readiness, or approval.

## Update — 2026-06-09: EP-32 repo-map freshness substrate built and wired

A new Enforcement Placement substrate — **EP-32, a handle beyond the EP-01..EP-31
overlay-rule table above** — is now built and wired under explicit current-turn
owner authorization. Unlike EP-06 (a rule already classified in the table), EP-32
hardens a rule that was **not** part of this record's overlay-rule classification:
the **repo map's own `stale_if:` block** in `docs/workflows/orca_repo_map_v0.md`
(a navigation artifact's freshness property, not an overlay-authority rule). It is
assigned the next stable handle here for traceability and later owner gating; the
EP-01..EP-31 table is left unchanged as the point-in-time classification it
declares itself to be.

- checker: `.agents/hooks/check_repo_map_freshness.py` — advisory + `--strict`
  commit/CI gate, forward-only, fails open; reads the repo map **as its own spec**
  and references the map's `stale_if` as authority, never restating it;
- hook: a second `PostToolUse` (`Write|Edit`) entry in `.claude/settings.json`,
  beside the EP-06 retrieval-header hook;
- discoverability + reinstall + acknowledgment + recheck recipe: the repo map's
  "Active Hooks" note was extended.

**Classification (stated inline, since EP-32 had no prior table row): PARTIAL.**
The mechanically-detectable structural subset is SUBSTRATE — a new top-level area
(`stale_if` #1) and a new `orca-harness/` runner/adapter (#2) are high-precision
gate triggers; a `source-of-truth.md` edit (#5) is an advisory nudge only. The
judgment-shaped staleness — "a spine was materially reorganized" (#3) and "routing
doctrine changed" (#4) — stays **resident**, owned by the Doctrine Change
Propagation contract in `.agents/workflow-overlay/source-of-truth.md` (which
already lists the repo map as a downstream surface). Per **PLACEMENT IS NOT
AUTHORITY** (the EP-29 over-edge rule), the substrate enforces map **shape, never
the truth or completeness of any route** — a clean run is not proof the map is
complete. A legitimate non-map change is acknowledged by a `repo-map-ack:`
commit-message token or by the map's "do not enumerate" exclusion list; updating
the map or a consolidation submap in the same change also satisfies the gate.

This is a further substrate built under the already-tripped `stale_if` "a
governance substrate is actually built/installed" (first tripped by EP-06, then
EP-01/EP-03); the remaining proposed rows stay proposals, each still owner-gated.
**No new doctrine** (no overlay rule changed; the Enforcement Placement principle
in `validation-gates.md` is unchanged; placement is not authority), so **no new
`direction_change_propagation` receipt is owed by this record** — the build's
receipt already lives in `.agents/workflow-overlay/source-of-truth.md` (trigger
`workflow_authority`, related `validation_philosophy`). **Live-verified this
session:** the `PostToolUse` hook fired on an actual edit (the advisory `stale_if`
#5 nudge) and `--selftest` passes; the `--strict` commit gate is
wired-but-not-installed by design (gate-on-demand, mirroring EP-06). Advisory
tooling, not validation, readiness, or approval.

## Update — 2026-06-09: guard re-placed to gate `main` (the merge), not the lane push

A coherence fix to the EP-03 guard (handoff from the CI/dev-workflow lane,
adjudicated here — I own this surface). The guard had been blocking the
*reversible* act (lane-branch `git push`) but **not** the *irreversible* one
(`gh pr merge` → `main`, which lived only in the auto-mode-inert `ask` config —
shown this session when PR #9 merged unblocked). Re-placed so the hard block
lands on the main-change:

- **now blocks** (exit 2, both shells): `gh pr merge` (+ `gh api .../merge`),
  push to `main`, force-push, bare/ambiguous push, plus `reset --hard` / `clean`;
- **now allows** an explicit non-main, non-force lane push
  (`git push -u origin <lane>`) — per-lane PR flow in
  `docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md` (verified on
  `main`; its server-side merge gate is 403-blocked on this private/free repo, so
  this hook is the local stand-in);
- also fixed a false-positive: a *mention* of these phrases inside a quoted
  string / echo no longer blocks;
- design: the simple/string fork (no `gh` API call) — preserves the guard's
  fast / fail-open / no-network design; under the missing server gate, blocking
  all `gh pr merge` (human/authorized action lands the PR) is the safe reading.
- **Verified live**: guard already active (fired in auto mode, no restart);
  selftest 32/32; live `gh pr merge` → exit 2, `git push -u origin <lane>` → exit 0.
- **Flagged for owner:** the doctrine's literal interim wording is "lane
  *self*-merges when green"; this guard implements the stricter
  "human/authorized action lands to `main`" as a compensating control for the
  403-blocked server gate. If you intend agent self-merge-when-green, relax the
  `gh pr merge` block.

## Update — 2026-06-11: EP-04 substrate built (placement check) — hook wiring pending owner

The folder-allowlist substrate proposed in the EP-04 row is now built under
explicit current-turn owner authorization ("do all phases", the repo-structure
binding turn), following the EP-32 house pattern:

- checker: `.agents/hooks/check_placement.py` — advisory `--hook` (PostToolUse,
  always exit 0), `--strict` commit/CI gate (exit 1 on non-legacy violations,
  map<->tree inconsistency in either direction, or a missing/unparseable map —
  a missing spec must not read as a pass), `--check`, `--selftest`; fail-open
  on internal error in advisory paths; references authority, never restates it;
- rule source: `repo-structure.yaml` (the machine map; router only) — the
  checker hardcodes no homes or tolerances. The map's `legacy_tolerated` list
  carries the declared pre-move debt (flat `docs/product/*.md`,
  `orca-harness/**`) as WARN-only; a tolerance-breadth sanity guard rejects
  blanket globs so the tolerance cannot quietly become a fake pass;
- binding + parameters: `docs/decisions/orca_repo_structure_binding_v0.md`
  (invariant core restated as Orca doctrine; product lanes; surface tiering);
  DCP receipt inline in `.agents/workflow-overlay/artifact-folders.md`;
- the EP-04 PARTIAL judgment edge stays resident: a new folder/lane is allowed
  only by a recorded decision, and the checker enforces placement SHAPE, never
  the truth, value, or authority of any artifact (PLACEMENT IS NOT AUTHORITY).

**Verified this session:** `--selftest` 16 cases + 6 fake-pass guards green
(one real bug caught and fixed during build: bare `fnmatch` let `*` cross `/`,
which would have silently tolerated lane subfolders under the flat-product
debt glob); live tree `--strict` exited 1 on the 3 root strays, then 0 after
their `docs/_inbox/` quarantine; `--hook` payload tests produced the WARN /
lane-nudge / silent behaviors. **NOT wired:** the `.claude/settings.json`
PostToolUse edit was permission-denied this session (self-modification
requires specific owner authorization), so the write-boundary hook is
build-complete but inactive; the registration snippet is in the repo map's
"Active Hooks" note and the Phase-2 runbook, and activation requires a session
restart after wiring. This trips `stale_if` (a further substrate built); the
remaining proposed rows stay proposals. Advisory tooling — not validation,
readiness, or approval.

## Update — 2026-06-09: EP-33 (secrets-in-plaintext write guard) proposed — deferred until production

A new Enforcement Placement substrate handle — **EP-33, beyond the EP-01..EP-32
set** — is recorded here as a **proposal only**, surfaced while assessing an
external Claude Code PreToolUse-guardrails write-up against this repo. Every
load-bearing recommendation in that write-up was already covered by EP-01/EP-03
(`guard_protected_actions.py`), EP-06 (`check_retrieval_header.py`), and EP-32
(`check_repo_map_freshness.py`); the **one** idea not covered anywhere in the
EP-01..EP-32 set was a secrets-in-plaintext write guard.

- **What it would be:** a `PreToolUse` content check on `Write`/`Edit` that
  blocks saving a high-confidence credential shape (e.g. `BEGIN … PRIVATE KEY`,
  `sk-…`/`ghp_…`/`AKIA…`-style tokens, `.env` assignments) and names a
  non-tracked destination instead — a sibling to `guard_protected_actions.py`,
  fail-open.
- **Classification: PARTIAL.** High-confidence shapes → substrate; "is this
  actually a secret vs a test fixture / example key?" stays resident judgment
  (PLACEMENT IS NOT AUTHORITY — a green scan is not proof no secret leaked).
- **Owner decision this turn: deferred until production.** Rationale: this is a
  docs/decisions/prompts repo not handling live credentials, so the base rate is
  low; the residual risk (lane-branch pushes are allowed and a pushed secret is
  effectively irreversible) was judged not worth the substrate yet. **Revisit
  trigger: heading into production.**

This does **not** trip the `stale_if` "a governance substrate is actually
built/installed": EP-33 is **proposed, not built** — nothing was authored,
wired, or installed. No overlay rule changed (placement is not authority), so
**no `direction_change_propagation` receipt is owed**. Not validation,
readiness, or approval; recording a deferred proposal, nothing more.

## Current Task Receipt

```yaml
orca_start_preflight:
  agents_read: yes
  overlay_read: yes            # all 17 .agents/workflow-overlay/ sections read this turn
  source_pack: custom          # full overlay + substrate probe (.claude/, orca-harness/)
  edit_permission: docs-write
  target_scope: [docs/decisions/overlay_enforcement_placement_classification_v0.md]
  dirty_state_checked: yes      # source-of-truth.md modified; many untracked docs; this is a new file, no overlay edit
  blocked_if_missing: no
```

## Problem (Orca-bound)

The Orca overlay (`.agents/workflow-overlay/`, the always-on governance layer loaded for project work) carries many rules as **resident model instructions** that a deterministic substrate could enforce at a boundary instead. Each such rule (a) fires only when the model attends to it — unreliable — and (b) spends a slot of the scarce, reliability-bounded always-on instruction budget that a genuinely judgment-based rule needs. The recurring miss is reaching for a "be careful to…" instruction by reflex when a hook, gate, schema, or test could enforce the rule by construction.

## Goal

The overlay enforces, in a deterministic substrate at a boundary, every rule that can be — reserving the resident instruction budget for genuinely judgment-based rules. Concretely: each overlay rule classified (code-enforceable → substrate; judgment-only → resident); the code-enforceable ones moved to or **proposed** for a hook/gate/schema/test; the judgment remainder kept resident and subject to VERIFY FIRING; the overlay pointing at the shared principle as a single source, not a restated fork.

## The enforcement-placement core (referenced, not forked)

Provenance: this core is the agnostic principle supplied with the task, derived from jb's `docs/doctrine/enforcement_placement_doctrine.md` (candidate). It is repo-invariant and carries no jb specifics. It is carried inline **only because the cross-repo shared home is TBD** (see § Step 4); the intent is to reference it as a single source, never to fork or weaken it. It is cited as provenance, not imported as Orca authority.

- **ENFORCEMENT PLACEMENT** — when a rule must hold at a boundary, prefer enforcing it in a deterministic substrate (tool-boundary hook · gate/assertion · schema/typed boundary token · deterministic test) over a resident model instruction. Code-enforced fires always at zero model budget; actor-carried is flexible but unreliable and competes for budget.
- **CLASSIFY SUBSTRATE-FIRST** — before installing any rule as a resident instruction, ask whether a deterministic substrate can enforce it at its boundary; if yes, harden it there and don't also carry it in the model.
- **RESERVE THE BUDGET** — the always-on budget is scarce and degrades with rule count/position; reserve it for judgment rules with no deterministic check.
- **ACTOR-CARRIED REMAINDER OWES FIRING** — carry as an instruction only the remainder with no deterministic check; it still owes VERIFY FIRING (present in the prompt ≠ fired).
- **PLACEMENT IS NOT AUTHORITY (over-edge)** — this decides WHERE a rule is enforced, never WHETHER it's correct/validated. Forcing a judgment rule into brittle code to "always fire" is the over-edge failure.

Decision rule, applied per overlay rule R:

```text
INPUT: an overlay rule R that must hold.
TEST:  is there a deterministic substrate that can enforce R at its boundary
       (tool-boundary hook / gate / schema·typed token / deterministic test)?
  → YES: enforce R in that substrate; do NOT also carry it as an instruction.
  → NO (genuine judgment): keep R resident; it owes VERIFY FIRING.
```

## Method and the load-bearing finding

The verdicts use four values:

- **SUBSTRATE** — fully code-enforceable at a boundary; deterministic; a clear win to propose.
- **PARTIAL** — the checkable shell (presence / shape / path / count / enum / hash) goes to a substrate; the judgment core stays resident. The substrate enforces **shape, never truth**.
- **JUDGMENT** — no deterministic check; stays resident; owes VERIFY FIRING.
- **OVER-EDGE** flag — a brittle check is technically possible but would manufacture false confidence; keep resident (PLACEMENT IS NOT AUTHORITY).

Substrate types: `hook` (Pre/PostToolUse tool-boundary guard — the only always-fires/zero-budget option; needs `.claude/settings.json` wiring), `test` (deterministic pytest, e.g. an `orca-harness` governance target), `schema` (typed-token / receipt-shape validation), `lint` (forbidden-token / forbidden-key / exact-string scan). These overlap (a forbidden-token scan can run as a hook or a test).

**Load-bearing finding — Orca has zero governance substrate today.** Verified this turn:

- **No hooks configured.** `.claude/settings.json` is plugin/marketplace config only; `.claude/settings.local.json` is a permission allowlist; there is no `PreToolUse`/`PostToolUse` block anywhere in-repo.
- **The only deterministic code (`orca-harness/`) is domain-scoped** (Judgment Spine v0.14 + Source Capture: `pytest`, a `Makefile`, fail-closed runners). It proves Orca *can* host deterministic tests and fail-closed assertions, but nothing in it enforces overlay governance.
- Every overlay "gate / contract / boundary" is therefore a **resident instruction**. None fires by construction.

Consequence: in Orca **right now**, every SUBSTRATE/PARTIAL verdict names a substrate that **does not exist yet**, and building it is **owner-gated**. So the "moved" column is empty by construction — this deliverable is inventory + classification + **proposals**, with one explicit owner gate. (This is exactly the prepare-only, owner-gated boundary the task set.)

## Per-rule classification

IDs are stable handles for later owner gating. Where a rule appears in several overlay files, the row cites the controlling one and notes the others. "Win" marks the clear code-enforceable proposals.

| ID | Rule (overlay source) | Boundary | Verdict | Proposed substrate (does not exist yet — owner-gated) |
| --- | --- | --- | --- | --- |
| EP-01 | Do not edit `jb` / external reference folders / installed-user-plugin-external skills (`safety-rules`; also `artifact-roles` Protected Roles, `skill-adoption` Protected Skill Boundary, `delegated-review-patch` protected_path_list) | write/edit/delete tool call | **SUBSTRATE** · Win | `PreToolUse` path-deny hook → `BLOCKED_PROTECTED_PATH`. Collapses 4 rules into one boundary. **Sampled, App A.** |
| EP-02 | No implementation dirs (`src`/`app`/`packages`/`tests`/runtime) unless authorized (`artifact-folders`; also `validation-gates`, `safety-rules`) | write / mkdir | **SUBSTRATE** · Win | `PreToolUse` path guard + `test`; "unless authorized" = a flag the guard reads → `BLOCKED_IMPL_DIR_UNAUTHORIZED`. **Sampled, App A.** |
| EP-03 | No commit/push/remote/PR/destructive cleanup unless authorized (`safety-rules`) | Bash `git`/`gh` call | **SUBSTRATE** · Win | `PreToolUse` command-pattern deny → `BLOCKED_GIT_LIFECYCLE_UNAUTHORIZED`. **Sampled, App A.** |
| EP-04 | Durable writes land in accepted folders (`artifact-folders` accepted list) | write path | **PARTIAL** | `hook`/`test` folder-allowlist; judgment edge: new folders allowed by a later decision. |
| EP-05 | No `jb` / forbidden-import leakage in prompts & artifacts (`validation-gates` leakage gate; `prompt-orchestration` anti-import; `template-registry`; `project-authority` forbidden drift) | artifact content at write | **SUBSTRATE** (token/path patterns) / PARTIAL ("as authority" semantics) · Win | `lint` forbidden-token scan (jb paths, GAP/CV Engine, compiler paths) as hook or test. |
| EP-06 | Retrieval header present on in-scope durable artifacts (`retrieval-metadata` applicability; also `validation-gates`, `artifact-folders`) | durable doc write | **SUBSTRATE** (presence) / PARTIAL ("in scope?" edge) · Win | `lint`/`test`. **The jb exemplar.** **Sampled, App B.** |
| EP-07 | Header well-formed: `retrieval_header_version: 1`, `authority_boundary: retrieval_only` exact, no forbidden fields, core ≤5 unless justified (`retrieval-metadata`) | header block | **SUBSTRATE** (exact-value + forbidden-key + count) / PARTIAL ("triggered field justified") · Win | `lint`/`test`. **Sampled, App B.** |
| EP-08 | `orca_start_preflight` receipt present + required fields on repo-aware / docs-write / source-change / completion (`source-loading`; also `validation-gates`, `prompt-orchestration`) | prompt / closeout | **PARTIAL** | `schema` presence/shape. Truth of `agents_read`/`overlay_read` → resident (non-self-cert, EP-29). |
| EP-09 | `direction_change_propagation` receipt or blocker present on doctrine-changing edits (`source-of-truth` DCP contract; also `validation-gates`, `prompt-orchestration` gate 12, `communication-style`) | doctrine-change closeout | **PARTIAL** · OVER-EDGE | `schema` receipt presence/shape; the `stale_language_search` field is a literal `rg` → re-runnable by `test`. But "is this edit doctrine-changing?" and "are downstream surfaces really checked?" stay resident — a hook must **not** decide doctrine-ness. |
| EP-10 | `review_summary` shape + forbidden-keys + `recommendation` enum + `report_path` valid only if the file exists (`communication-style`) | review summary YAML | **SUBSTRATE** · Win | `schema`/`lint`; `report_path` existence is a real file check. |
| EP-11 | Exactly one output mode from the closed set (`prompt-orchestration`; `validation-gates` output-mode gate) | prompt artifact | **SUBSTRATE** · Win | `schema`: token-in-set ∧ count == 1. |
| EP-12 | Typed tokens valid: `BLOCKED_*`, `SOURCE_CONTEXT_READY`, prompt verdicts, `access` enum (`artifact-roles` failure states; `prompt-orchestration`; `delegated-review-patch`) | artifact | **PARTIAL** | `schema` token-spelling / enum membership; correct application → resident. |
| EP-13 | Every prompt role bound in `artifact-roles` (`validation-gates` artifact-role gate; `prompt-orchestration` gate 2) | prompt | **SUBSTRATE** (existence lookup) / PARTIAL ("right role") | `test`/`schema` role-table lookup → `BLOCKED_UNBOUND_ARTIFACT_ROLE`. |
| EP-14 | Default path assignment: versioned filename in accepted folder; collision → next version (`prompt-orchestration`) | write path | **PARTIAL** | `hook`/`test` exists-check + folder allowlist; "narrowest / descriptive" → judgment. |
| EP-15 | Hash pins verifiable: skill-source sha256, migration input hashes (`skill-adoption`; `validation-gates`) | pinned artifact | **SUBSTRATE** · Win | `test` recomputes and compares the hash — fully deterministic. |
| EP-16 | Source-capsule budget counts (≤4 full / ≤8 targeted / ≤10 excerpts) (`source-loading`; `validation-gates`) | capsule artifact | **PARTIAL** | `schema` count check; "right narrowing" → judgment. |
| EP-17 | Template-registry integrity: each registry path exists; unbound kinds (`direct-implementation`/`repo-code-review`/`automation-runtime`) unused absent authorization (`template-registry`) | registry + template use | **SUBSTRATE** (path-existence test) / PARTIAL (use-guard) | `test` registry integrity; `hook` use-guard. |
| EP-18 | Subagent runtime payload safety: no explicit `default`/`null`/same-as-parent `agent_type`/`model`/etc. on forked spawns (`decision-routing`) | spawn payload | **PARTIAL → SUBSTRATE** if the spawn passes a checkable boundary | `schema` payload reject. |
| EP-19 | De-correlation who-constraint: author family ≠ delegate family recorded; Opus author ⇒ non-Opus delegate (`delegated-review-patch`) | commission record | **PARTIAL** | `schema` field-inequality assertion; truth of the recorded family → resident (self-cert). |
| EP-20 | `no_repo` review package: verbatim attachment hash-confirmable; freshness gate hash-compares `derived_from` pins (`delegated-review-patch`) | review package | **SUBSTRATE** · Win | `test` hash compare — deterministic. |
| EP-21 | Reviewer threads source-read-only unless assigned patch execution (`review-lanes`; AGENTS kernel) | write in a review lane | **PARTIAL** · OVER-EDGE-adjacent | enforceable as `hook` only if the lane is machine-tagged (it is not today) → resident/partial now. |
| EP-22 | No runtime-model recommendation / ranking in review prompts/closeouts (`review-lanes`; `prompt-orchestration`) | review artifact content | **PARTIAL** · OVER-EDGE | `lint` phrase tripwire is brittle/advisory; do not hard-block on a phrase match. Mostly judgment. |
| EP-23 | Source-hierarchy precedence & conflict resolution (`source-of-truth`) | reasoning | **JUDGMENT** (PARTIAL only for "referenced required source missing → fail" = missing-file check) | resident; owes VERIFY FIRING. |
| EP-24 | Cynefin routing: run-vs-bypass, regime, bottleneck, riskiest assumption, stop/pivot, allowed/disallowed (`decision-routing`) | pre-planning | **JUDGMENT** | resident; owes VERIFY FIRING. Output-shape presence = weak partial only. |
| EP-25 | Smallest complete intervention / scope discipline (`AGENTS.md`; `safety-rules`) | every change | **JUDGMENT** | resident; owes VERIFY FIRING. |
| EP-26 | Source-gated method contract: `REFERENCE-LOAD` vs `APPLY`; no method-derived conclusions before `SOURCE_CONTEXT_READY` (`prompt-orchestration`) | prompt sequencing | **JUDGMENT** (token presence = weak partial) | resident; owes VERIFY FIRING. |
| EP-27 | Product-proof semantics: `trust_objection` vs `trust_refusal`; kill-criteria; pull-vs-praise; claim tier; weakest-cleared-gate; non-claims (`product-proof`; `validation-gates` product gates) | proof reasoning | **JUDGMENT** (non-claims presence = weak partial) | resident; owes VERIFY FIRING. |
| EP-28 | Zero-spoiler backtest: no reveal of decision/recommendation/outcome in participant-facing material (`product-proof`; `validation-gates`) | participant artifact | **JUDGMENT** · OVER-EDGE | resident. A keyword leak-scan is at best a noisy advisory tripwire and must never be treated as a pass/clear. |
| EP-29 | Receipt-field provenance / non-self-certification (`validation-gates`) | any gate clearing on a field | **JUDGMENT** (PARTIAL corollary: "single-source duplicated enumerations" = dup-enumeration lint) | resident. **This rule is itself the formalization of PLACEMENT IS NOT AUTHORITY for receipts: a substrate checks a field's shape, never its truth.** |
| EP-30 | Chat-output topology / communication style: human-summary-first, decision-first, readability (`communication-style`) | chat output | **JUDGMENT** | resident; owes VERIFY FIRING. |
| EP-31 | Checkpoint-artifact lifecycle: non-authoritative; single-consumption/burn; one live instance per lane; point-don't-copy (`source-of-truth`) | checkpoint files | **PARTIAL** | `test` can detect "one live instance / no `_v2`/`_v3`"; "re-confirm volatile claims / burn after consumption" → judgment/behavioral. |

Distribution: **clear SUBSTRATE wins** — EP-01, EP-02, EP-03, EP-05, EP-06, EP-07, EP-10, EP-11, EP-13, EP-15, EP-20. **PARTIAL (shape→substrate, core→resident)** — EP-04, EP-08, EP-09, EP-12, EP-14, EP-16, EP-17, EP-18, EP-19, EP-21, EP-22, EP-29(corollary), EP-31. **JUDGMENT (resident, owes VERIFY FIRING)** — EP-23, EP-24, EP-25, EP-26, EP-27, EP-28, EP-29(core), EP-30.

## The clear code-enforceable wins (proposed, prioritized)

These are the proposals worth the owner's authorization first, highest leverage downward. None exists yet.

1. **One `PreToolUse` protected-path guard** (EP-01, EP-02, EP-03; partial EP-21). A single tool-boundary hook collapses the largest cluster of "do not edit X / do not run Y unless authorized" rules into one always-fires check at zero model budget. Highest leverage; smallest surface. Sample in App A.
2. **Retrieval-header lint** (EP-06, EP-07). The jb exemplar, near-verbatim for Orca: presence + `version: 1` + exact `authority_boundary: retrieval_only` + forbidden-field scan. Pure shape; runs as a `PostToolUse` hook or an `orca-harness` test. Sample in App B.
3. **Forbidden-import / `jb`-leakage lint** (EP-05). A forbidden-token scan enforces "do not copy jb templates/paths/Engine/compiler paths" by construction.
4. **Receipt-shape schemas** (EP-08, EP-09, EP-10, EP-11, EP-12, EP-13). Validate presence/shape/enum of `orca_start_preflight`, `direction_change_propagation`, `review_summary`, output mode, typed tokens, bound roles. **Shape only — truth stays resident (EP-29).**
5. **Hash-pin verification** (EP-15, EP-20). A test recomputes pinned sha256s (skill source, migration inputs, no_repo attachments) and fails on drift.

## Over-edge cautions (PLACEMENT IS NOT AUTHORITY, in Orca)

Do not push these into brittle code to "always fire" — doing so manufactures false confidence:

- **Zero-spoiler leak detection (EP-28).** A keyword scan cannot reliably tell a spoiler from clean pre-cutoff evidence; a green scan would falsely read as "no leak." Keep resident; a scan may exist only as a noisy advisory tripwire, never a clear.
- **"Is this edit doctrine-changing?" (EP-09 trigger).** A hook may demand the DCP receipt once doctrine-ness is asserted, but must not be the thing that decides doctrine-ness.
- **Receipt truthfulness (EP-29).** Already Orca doctrine: a self-asserted field value does not clear a gate. Substrate enforces a receipt's shape; it never certifies the value is true.
- **Runtime-model phrasing (EP-22), reviewer-lane writes (EP-21).** Enforceable only as advisory/partial until lanes are machine-tagged; a hard block on phrase-match or untagged lane is over-edge today.

## Step 4 — proposed overlay pointer (blocked-on; not bound this turn)

Step 4 ("point the overlay at the shared principle as its single source") is **blocked by design** and is therefore proposed, not performed:

- The cross-repo **shared home is TBD** (per the task, part of the later distillation change) — there is no canonical source to point at yet.
- **Binding the doctrine to Orca is the separate later task**, explicitly out of scope here.
- Editing an overlay-authority file to add a new resident rule is itself **doctrine-changing** (it would owe a DCP receipt and likely owner gating) — and adding a *resident* restatement of an enforcement-placement principle would also spend budget, the very thing the principle warns against.

Proposed binding, to be lifted **verbatim** by the later task once a shared home exists (reference, do not fork):

> **ENFORCEMENT PLACEMENT (referenced).** When an overlay rule must hold at a boundary, prefer enforcing it in a deterministic substrate (tool-boundary hook · gate/assertion · schema/typed token · deterministic test) over a resident instruction; classify substrate-first; reserve the resident budget for judgment rules; the actor-carried remainder still owes VERIFY FIRING; placement decides WHERE, never WHETHER. Single source: `<shared doctrine path — TBD>`.

Proposed landing site: one short pointer (≈4 lines) — most naturally a sub-note under `validation-gates.md` (it governs what clears a gate) cross-referenced from `decision-routing.md`. It should be a **pointer to the shared source**, not a copy. Until the shared home and an owner decision exist, this stays a proposal here.

## Owner gate — what authorization would move propose → build

Each item is bounded and independent; none is implied by this record.

- **Authorize the `PreToolUse` protected-path guard** (App A) and its `.claude/settings.json` wiring (EP-01/02/03). This is "deployed automation" under `safety-rules` and needs explicit bounded authorization.
- **Authorize the retrieval-header lint** (App B) as an `orca-harness` governance test target or a `PostToolUse` hook (EP-06/07).
- **Authorize the leakage lint and the receipt-shape schemas** (EP-05, EP-08–EP-13) as tests/hooks.
- **Create (elsewhere) the shared doctrine home**, then run the separate binding task to add the Step-4 pointer.

## Non-claims

- Not validation, readiness, acceptance, approval, or proof of anything.
- Not a doctrine change and not an overlay edit; no DCP receipt owed.
- Not implementation, deployment, install, or resolver authorization; the sample drafts in App A/B are illustrative and run/install nothing.
- Not a binding of the shared doctrine to Orca (that is the separate later task).
- The classification is of Orca's **real** overlay rules as read this turn; substrate availability is reported as found (none exists), not assumed.

---

## Appendix A — SAMPLE substrate draft: `PreToolUse` protected-path guard (prepare-only)

**SAMPLE — prepare-only.** NOT wired into `.claude/settings.json`, NOT added to `orca-harness`, runs nothing. Adopting it is owner-gated (EP-01/02/03). The load-bearing part is the **forbidden-target decision logic**; the hook I/O envelope is illustrative and must be confirmed against the Claude Code hook contract at build time.

```python
# orca_protected_path_guard.py  (SAMPLE — not installed, not wired, owner-gated)
# Intended use: a PreToolUse hook. Denies writes/edits/deletes to protected paths
# and unauthorized git/gh lifecycle commands. Authorization is an explicit per-session
# opt-in (ORCA_BOUNDED_IMPL_AUTHORIZED=1), mirroring the overlay's "unless explicitly
# authorized" boundary — the guard fails closed when the flag is absent.
import json, os, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]  # adjust at build time
AUTHORIZED = os.environ.get("ORCA_BOUNDED_IMPL_AUTHORIZED") == "1"

WRITE_TOOLS = {"Write", "Edit", "NotebookEdit", "MultiEdit"}
SHELL_TOOLS = {"Bash", "PowerShell"}

# Always read-only / flag-only (safety-rules, artifact-roles, skill-adoption, delegated-review-patch):
PROTECTED_SUBSTRINGS = (
    "agent-workflow",                         # external workflow source
    os.path.join(".codex", "plugins"),        # installed plugin cache
    os.path.join(".codex", "skills"),         # user-level skill shadow
    os.path.join(".claude", "plugins"),       # installed plugin cache
)
# Implementation dirs forbidden unless authorized (artifact-folders / validation-gates / safety-rules):
IMPL_DIRS = ("src", "app", "packages", "tests", "runtime")
# Lifecycle commands forbidden unless authorized (safety-rules):
GIT_LIFECYCLE = re.compile(r"\bgit\s+(push|commit|remote)\b|\bgh\s+pr\b|\bgit\s+clean\s+-[a-z]*f", re.I)


def deny(reason_token, detail):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "deny",
        "permissionDecisionReason": f"{reason_token}: {detail}"}}))
    sys.exit(0)  # confirm deny envelope/exit code against Claude Code hook docs at build time


def is_outside_repo(p: Path) -> bool:
    try: p.resolve().relative_to(REPO); return False
    except ValueError: return True


def main():
    ev = json.load(sys.stdin)
    tool, ti = ev.get("tool_name", ""), ev.get("tool_input", {}) or {}

    if tool in WRITE_TOOLS:
        raw = ti.get("file_path") or ti.get("path") or ti.get("notebook_path") or ""
        if not raw: return
        if any(s in raw for s in PROTECTED_SUBSTRINGS) or is_outside_repo(Path(raw)):
            deny("BLOCKED_PROTECTED_PATH", raw)
        parts = Path(raw).resolve().relative_to(REPO).parts if not is_outside_repo(Path(raw)) else ()
        if parts and parts[0] in IMPL_DIRS and not AUTHORIZED:
            deny("BLOCKED_IMPL_DIR_UNAUTHORIZED", raw)

    elif tool in SHELL_TOOLS:
        cmd = ti.get("command", "")
        if GIT_LIFECYCLE.search(cmd) and not AUTHORIZED:
            deny("BLOCKED_GIT_LIFECYCLE_UNAUTHORIZED", cmd.strip()[:120])
    # else: allow (no output = allow)


if __name__ == "__main__":
    main()
```

Notes / known gaps (resolve at build time): the single-target restriction for a delegated-review-patch commission (delegate may edit only the one named file) would be an extra check keyed off the commission record; the exact `PreToolUse` deny envelope and exit-code semantics must be confirmed against the Claude Code hook docs; `REPO` resolution and the protected-substring list should be reviewed against the live machine layout in `skill-adoption.md`.

## Appendix B — SAMPLE substrate draft: retrieval-header lint (prepare-only)

**SAMPLE — prepare-only.** NOT installed, runs nothing. Adopting it (as an `orca-harness` test target or a `PostToolUse` hook) is owner-gated (EP-06/07). This one is pure file parsing + assertions; it enforces header **shape only**, never the truth of any field.

```python
# test_retrieval_header.py  (SAMPLE — not installed, owner-gated)
# Enforces .agents/workflow-overlay/retrieval-metadata.md: in-scope durable artifacts
# carry a well-formed retrieval header. Shape only — not validation of any claim.
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]  # adjust at build time
IN_SCOPE = ("docs/decisions", "docs/product", "docs/workflows",
            "docs/review-outputs", ".agents/workflow-overlay")
FORBIDDEN_HEADER_FIELDS = {  # retrieval-metadata.md "Forbidden Header Fields"
    "approval", "approval_status", "validation", "validation_status", "readiness",
    "lifecycle", "lifecycle_state", "deployment", "install", "resolver",
    "edit_permission", "executor_authorization", "review_verdict", "source_of_truth"}


def first_yaml_block(text: str) -> str | None:
    m = re.search(r"^```ya?ml\s*\n(.*?)\n```", text, re.S | re.M)
    return m.group(1) if m else None


def header_violations(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    block = first_yaml_block(text)
    if block is None:
        return [f"{path}: no retrieval header (yaml block) found"]
    top_keys = re.findall(r"^([A-Za-z0-9_]+):", block, re.M)
    out = []
    if "retrieval_header_version: 1" not in block:
        out.append(f"{path}: retrieval_header_version must be 1")
    if not re.search(r"^authority_boundary:\s*retrieval_only\s*$", block, re.M):
        out.append(f"{path}: authority_boundary must be exactly 'retrieval_only'")
    for k in top_keys:
        if k.lower() in FORBIDDEN_HEADER_FIELDS:
            out.append(f"{path}: forbidden header field '{k}'")
    return out


def iter_in_scope():
    for rel in IN_SCOPE:
        for p in (REPO / rel).rglob("*.md"):
            if p.name.lower() == "readme.md":   # simple folder READMEs are excluded
                continue
            yield p


def test_retrieval_headers():
    violations = [v for p in iter_in_scope() for v in header_violations(p)]
    assert not violations, "Retrieval-header violations:\n" + "\n".join(violations)


if __name__ == "__main__":
    for p in iter_in_scope():
        for v in header_violations(p):
            print(v)
```

Notes / known gaps (resolve at build time): "in scope" is intentionally conservative and should be reconciled with `retrieval-metadata.md` § Applicability / Exclusions (e.g. `docs/_inbox/` scratch, generated outputs, raw evidence units are excluded); the core-field-count (≤5 unless a triggered field passes the value test) and "triggered field justified" checks are deliberately omitted because the justification is a judgment call (PARTIAL, not pure shape).
