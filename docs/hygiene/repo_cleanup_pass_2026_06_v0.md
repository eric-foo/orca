# Repo-Wide Hygiene Cleanup Pass — 2026-06 v0

```yaml
retrieval_header_version: 1
artifact_role: Hygiene cleanup report (docs/hygiene/; one bounded repo-wide pass)
scope: >
  Repo-wide hygiene inventory + classification for the cleanup lane commissioned
  by docs/prompts/handoffs/repo_wide_hygiene_cleanup_lane_handoff_prompt_v0.md.
  Records checker outputs, a repo-wide dead-pointer/stale-language sweep, the
  three-class triage, the (empty) mechanically-safe fix set with its evidence,
  the queue rows opened, and the owner decision memo. Navigability/routing only.
use_when:
  - Reviewing what the 2026-06 hygiene pass found, fixed, routed, and left to the owner.
  - Deciding the owner-gated items (header backlog, Phase-2 reference debt, branch/worktree pruning, debris disposal).
authority_boundary: retrieval_only
open_next:
  - docs/hygiene/queue.md                              # rows 015/016/017 opened here; live triage state
  - docs/migration/repo_structure_phase2_consolidation_v0/moved_paths_index.md  # old->new resolution table for the Phase-2 reference debt
branch_or_commit: ecr-sp3-timing-deriver-slice1 @ 130a68b at intake (repo churns daily; re-verify on read)
stale_if:
  - The hygiene queue's open/settled row set changes (this is a dated snapshot; the queue is live state).
  - A new Phase-2-style move or a header-backfill policy decision lands (re-run the sweeps).
```

This is one bounded hygiene pass. It is **not** validation, readiness, acceptance,
a reorganization mandate, deletion/pruning authority, or doctrine change. Every
finding below is a hygiene/routing defect; fixing one proves navigability only,
never validation or product proof. The lane ends at this report.

---

## Intake / Preflight Record

```text
orca_start_preflight:
  agents_read: AGENTS.md + Mini God Tier + Smallest Complete Intervention kernel (in-context, re-read on intake)
  overlay_read: .agents/workflow-overlay/README.md (fresh) + source-of-truth, artifact-folders,
                retrieval-metadata, source-of-truth Checkpoint Artifacts + DCP contract
  source_pack: hygiene queue + open_next pins + the three checker scripts (read in full) + moved_paths_index
  edit_permission: docs-write (mechanically-safe class only; everything else routed)
  target_scope: repo-wide hygiene inventory + bounded safe fixes + queue rows + owner memo
  dirty_state_checked: yes — concurrent churn confirmed; censused, not assumed (see below)
  commits: NOT committed. Default per handoff: fixes/outputs left uncommitted and listed; owner authorizes commit.
intake_reverification_of_capsule:
  - Queue open/settled set MATCHES capsule: resolved 001/002/004/005/008/009/011/012/013/014;
    open 003, 010; dormant event-triggered 006/007. Next free ID = ORCA-HYGIENE-015.
  - CAPSULE CORRECTION (load-bearing absence claim): the capsule names
    `.agents/workflow-overlay/safety-rules.md` as the overlay header gap. Fresh run shows
    safety-rules.md now CARRIES a valid retrieval header; the lone current overlay header
    gap is `.agents/workflow-overlay/project-authority.md`. Verified by direct head-read of both.
  - CAPSULE UNDERCOUNT: capsule cited "three" dead open_next pointers. A repo-wide sweep finds
    the true Phase-2 reference debt is ~3,299 stale-flat-path refs across ~170 targets (detail below).
    The capsule's "three" were the live-hub fixes already landed by ORCA-HYGIENE-009/013.
```

Branch/commit at intake: `ecr-sp3-timing-deriver-slice1 @ 130a68b` (handoff was authored at
`48c00ca`; HEAD advanced during intake — concurrent commits land on this branch too).

---

## Phase A — Inventory (read-only). Actual checker + sweep outputs

### Checker 1 — Placement (`check_placement.py --check`)
```
summary: 0 violation(s), 0 freshness, 761 legacy-tolerated (warn-only), 14258 scratch-excluded file(s)
```
**Clean.** No placement violations, no map↔tree inconsistency, no `_inbox` age warnings.
(761 "legacy" + 14,258 "scratch" are the tolerated `orca-harness/**` tree incl. its `.venv` —
expected, warn-only by design.) Selftest of the checker not re-run; the tree gate passed.

### Checker 2 — Repo-map freshness (`check_repo_map_freshness.py --changed`)
```
repo-map-freshness: new top-level area `_scratch/` is not in the repo map (stale_if #1)
repo-map-freshness: a map/submap was also updated in this change - gate satisfied (...)
```
One structural signal: **`_scratch/`** is a top-level area absent from the repo map. The gate is
currently *satisfied only incidentally* because a concurrent lane has `docs/workflows/orca_repo_map_v0.md`
modified in the working tree. `_scratch/` is also **not gitignored** (`git check-ignore _scratch` → no match).
Routed (owner): row 017.

### Checker 3 — Retrieval headers (forward-only; fed all in-scope `*.md`)
**117 durable artifacts** flagged: ~100 **missing** a retrieval header, ~17 with a **non-`retrieval_only`
`authority_boundary`** (e.g. `decision_record`, `prompt_only`, `planning_only`, `review_output_only`,
`non_authoritative`). These are overwhelmingly **pre-existing** artifacts predating the forward-only EP-06
check. The retrieval-metadata contract itself says *"Do not backfill every existing file by default."*
Routed (owner): row 015. Reproduce:
`find docs .agents/workflow-overlay -name '*.md' -print0 | xargs -0 python .agents/hooks/check_retrieval_header.py`

### Sweep 4 — Dead pointers (repo-wide, context-tagged; read-only analysis script)
Across committed, in-scope `*.md` (excluding `_inbox/`, the migration ledgers, and `_archive/`):
**3,299 references resolve to a non-existent path**, over **170 unique missing targets**. By reference context:

| Context | Count | Disposition |
| --- | --- | --- |
| prose / table / narrative mention | 1,756 | resolved-by-design (historical) |
| historical receipt (`controlling_sources_updated`, `input_hashes`, `supersedes`, `stale_language_search`) | 777 | **never rewrite** (provenance/DCP) |
| `open_next`-context (sticky-tagged; includes PROV lines) | 548 | mostly historical records / concurrent-lane |
| `stale_if`-context condition lines | 218 | mostly historical / frozen conditions |

Nearly all are **old flat `docs/product/<file>.md` paths** relocated by the Phase-2 by-lane move
(commit `1b0f3fc`, 99 files). The Phase-2 migration is **forward-only by design**: it shipped
`docs/migration/.../moved_paths_index.md`, whose header states *"Historical records reference old paths
by design; resolve them here."* Restricting the sweep to **shared-routing / current-nav surfaces only**
yields 282 hits — and inspection shows even those are dominated by frozen content: e.g.
`docs/product/judgment_spine/judgment_spine_gate_ownership_map_v0.md` L29–32 are **SHA hash-pins**,
L52–54 are `stale_if` conditions, L206/210/276 are DCP-receipt `- path:` entries;
`docs/product/source_capture_toolbox/README.md` hits sit inside `direction_change_propagation`
receipts and `stale_language_search` commands; `communication-style.md` L135/167 reference an
illustrative `example_adversarial_review_v0.md` that never existed. **None of these are safe to rewrite.**
Routed (owner): row 016. Reproduce: see `_scratch`-free analysis in the receipts section.

### Census — dirty / concurrent-lane state (do not touch)
```
 M docs/decisions/beauty_subtle_decision_screen3_ledger_v0.md        (concurrent: beauty lane)
 M docs/product/core_spine/orca_venue_exploration_procedure_v0.md    (concurrent)
 M docs/workflows/orca_repo_map_v0.md                                (concurrent: high-contention shared map)
?? _scratch/                                                          (scratch; fresh gijn_toolkit.html)
?? docs/decisions/beauty_venue_card_set_promotion_decision_v0.md     (concurrent: beauty lane)
?? docs/decisions/orca_doctrine_index_v0.md                          (concurrent)
?? docs/product/core_spine/beauty_venue_card_set_v0.md               (concurrent: beauty lane)
?? docs/prompts/handoffs/repo_wide_hygiene_cleanup_lane_handoff_prompt_v0.md  (this lane's own courier)
?? docs/prompts/product-planning/icp_product_direction_lane_commission_prompt_v0.md  (concurrent: ICP lane)
?? docs/research/creator_momentum_data_landscape_v0.md               (concurrent: capsule-flagged live file)
```
All modified/untracked files except this lane's own courier belong to concurrent lanes and were
**not** read for bodies, edited, moved, committed, or "fixed."

### Branch / worktree inventory
17 local branches; 15 worktrees. Merged-into-`main` (prunable, owner-gated): `capture-probe-tiktok-demand`
(tip == `main` HEAD `f15de94`, in worktree), `codex/data-capture-sourcing-architecture` (in worktree),
`dcp-restatement-integrity-port` (plain branch, no worktree). `capture-armory-readme-slice1`: upstream
`[gone]`, last commit 2026-06-09, **not** merged into local `main`. Oldest: `codex/data-capture-sourcing-architecture`
(2026-05-25), `codex/orca-doctrine-health` (2026-05-29). Local `main` is **behind origin/main by 14**.
Detail in the owner memo (D3). **Zero branch/worktree mutations performed.**

### Debris
- `orca-harness/_test_runs/`: gitignored (confirmed: `git check-ignore` matched), 149 entries. Disk only.
- `_scratch/gijn_toolkit.html`: 98 KB saved external webpage, mtime today (2026-06-11). Untracked, **not** gitignored, not in repo map.
- `docs/_inbox/`: README + a **tracked** operator-evidence tree
  `data_capture_pressure_test_operator_supplied_2026_05_29/slot3_recapture_2026_06_01/` (~38 files: CSV/JSON
  receipts, reddit media, WSO HTML/screenshots). Dated 2026-05-29/06-01 → ~13 days old, **under** the 30-day
  advisory aging line (no checker INBOX warning fired). Row-010's three strays (`di_dd.html`, two slot
  workfiles) are **absent** from tracked and untracked trees — already disposed since row 010 was opened.

---

## Phase B — Classification

Every finding placed in exactly one class.

| # | Finding | Class | Action |
| --- | --- | --- | --- |
| F1 | Placement: 0 violations / 0 freshness | — | none (clean) |
| F2 | 117 durable artifacts missing/wrong retrieval header | owner_gated | row 015 + memo D1 |
| F3 | ~3,299 stale flat-path refs (Phase-2), resolved-by-design via moved_paths_index | owner_gated | row 016 + memo D2 |
| F4 | `project-authority.md` lone overlay header gap | owner_gated | memo D1 (folds into F2) |
| F5 | `_scratch/` untracked + unignored + unmapped | owner_gated | row 017 + memo D5 |
| F6 | 17 branches / 15 worktrees; 3 merged, 1 upstream-gone, main behind 14 | owner_gated | memo D3/D9 |
| F7 | `orca-harness/_test_runs/` 149 gitignored entries | owner_gated | memo D4 |
| F8 | `docs/_inbox/` tracked operator-evidence tree (not yet aged) | owner_gated | memo D6 |
| F9 | Row-010 strays verified disposed | owner_gated | memo D7 (owner confirm + close 010) |
| F10 | LinkedIn lane index: 4 dead live pointers, but active data_capture lane | owner_gated | memo D8 (ready-to-apply, routed for concurrency) |

### Class 1 — `mechanically_safe` (docs-write, meaning-preserving): **0 fixes applied**

No fix was both mechanically-safe **and** lane-neutral **and** not already harvested. This is the honest
outcome, not under-delivery. Evidence per candidate class:

- **Live navigation hubs** (overlay files, repo map, the two consolidation maps, the judgment-spine
  manifest, the queue) carry **no** dead live pointers — prior passes ORCA-HYGIENE-009/013 already
  re-pointed them (the manifest's nine, the charter's open_next). The sweep confirms they are clean.
- **The Phase-2 reference tail** is frozen-by-design: hash-pins, DCP receipts, `stale_language_search`
  commands, `supersedes`/`input_hashes`, and prose mentions the migration explicitly resolves via the
  moved-paths index. Rewriting them would corrupt provenance and is a "broad rewrite" the lane forbids.
- **The one genuinely-live candidate** (`data_capture_spine_linkedin_lane_index_v0.md`, 4 pointers) is in
  the demonstrably-active data_capture lane (committed today; multiple `capture-*` worktrees). Per the hard
  concurrent-lane rule it is **routed** (memo D8) with the exact one-line fix, not applied here.
- **The overlay header gap** (`project-authority.md`) is excluded by the retrieval-metadata contract's own
  "do not backfill existing files by default," and the analogous case (`safety-rules.md`) was previously
  left owner-gated. Routed (D1), not backfilled.

### Class 2 — `queue_routed`: rows ORCA-HYGIENE-015, 016, 017 (appended to `docs/hygiene/queue.md`)

### Class 3 — `owner_gated`: memo decisions D1–D9 below. Includes ALL deletions, branch/worktree pruning,
`_test_runs` disposal, inbox disposition, header policy, the Phase-2 repoint policy, and `.gitignore`/repo-map edits.

---

## Phase C — Fixes applied

**Durable writes by this lane:**
1. This report (`docs/hygiene/repo_cleanup_pass_2026_06_v0.md`) — new.
2. Three queue rows appended to `docs/hygiene/queue.md` (015/016/017).

**Class-1 content fixes applied: 0** (see Class 1 above for the evidence-backed reason).
Nothing was committed; outputs are listed for the owner to commit on word.

---

## Owner Decision Memo

One decision list. Each item: recommendation + blast radius. The lane recommends only.

- **D1 — Retrieval-header backlog (117 artifacts; ties row 015).** ~100 missing headers + ~17 wrong
  `authority_boundary`, plus the lone overlay gap `project-authority.md`. **Recommend:** keep the
  forward-only posture (EP-06 catches new writes) and backfill *opportunistically* when each file is next
  materially touched — **except** fix `project-authority.md` now as a one-line overlay-maintenance patch
  (every sibling overlay file already has a header; the gap is conspicuous on an authority file).
  *Blast radius:* low per-file; a full backfill is ~117 files and not worth a single sweep.

- **D2 — Phase-2 reference debt (~3,299 refs / ~170 targets; ties row 016).** **Recommend:** keep the
  accepted **forward-only-resolve-via-`moved_paths_index.md`** posture. Do **not** mass-repoint: the corpus
  is dominated by hash-pins, DCP receipts, and historical records the migration deliberately did not rewrite,
  and `artifact-folders.md` already lists several of these files `intentionally_not_updated`. If you ever
  want live `open_next` pointers repointed, commission a separate reference-aware lane with an explicit
  exclusion list (provenance pins + DCP receipts + superseded records). *Blast radius:* a repoint touches
  ~100 files incl. decision records — high; the do-nothing path is already safe via the index.

- **D3 — Branch pruning (owner-gated; zero deletions by this lane).** Prunable (merged into `main`):
  `dcp-restatement-integrity-port` (plain branch — safe `git branch -d`); `capture-probe-tiktok-demand`
  and `codex/data-capture-sourcing-architecture` (merged but **checked out in worktrees** — remove the
  worktree first). Review separately: `capture-armory-readme-slice1` (upstream `[gone]`, not merged to local
  `main` — confirm it merged to origin before deleting). *Blast radius:* low if merged-status re-checked at
  prune time; worktree removal must precede branch delete.

- **D4 — `orca-harness/_test_runs/` (149 gitignored entries).** Disk debris, each a copy of test scaffolding.
  **Recommend:** delete the directory contents to reclaim disk; gitignored, so no history impact. *Blast radius:*
  disk only; confirm no in-flight harness run is reading it.

- **D5 — `_scratch/` (ties row 017).** Untracked, **not** gitignored, **not** in the repo map; holds a fresh
  `gijn_toolkit.html`. **Recommend:** add `_scratch/` to `.gitignore` **and** to the repo map's
  "do not enumerate" list (so the freshness checker stops flagging it). Leave the file. *Blast radius:* tiny
  (`.gitignore` + repo-map edit — both owner/shared-routing surfaces).

- **D6 — `docs/_inbox/` operator-evidence tree.** ~38 tracked files (slot-3 recapture media/receipts), ~13 days
  old (under the 30-day line). **Recommend:** decide whether this raw evidence should be promoted to a durable
  evidence folder or left to age and be triaged by the `_inbox` aging signal. *Blast radius:* low; tracked, so
  a move is reference-aware.

- **D7 — Row-010 strays disposed.** `di_dd.html` + the two slot workfiles are absent from tracked and untracked
  trees (verified). **Recommend:** confirm intentional disposal and mark ORCA-HYGIENE-010 resolved. The lane did
  not close it (open-row owner disposition). *Blast radius:* none (status-only).

- **D8 — LinkedIn lane index (ready-to-apply, routed for concurrency).** `docs/product/data_capture_spine/
  data_capture_spine_linkedin_lane_index_v0.md` has 4 dead live pointers (lines 14, 34, 79, 81) to files now
  under `docs/product/data_capture_spine/` (same folder). Exact fix = drop the flat `docs/product/<file>` →
  `docs/product/data_capture_spine/<file>` per moved_paths_index. **Recommend:** let the data_capture lane (or
  you) apply it, since that lane is actively committing to this file (last commit today). *Blast radius:* 1 file,
  4 lines; risk is collision with the live lane, hence routed not applied.

- **D9 — Remote reconciliation.** Local `main` is **behind origin/main by 14**; `capture-armory-readme-slice1`
  upstream is gone. **Recommend:** `git fetch` + reconcile `main`, and confirm the armory-readme branch's PR
  state before any prune. *Blast radius:* none until you act.

---

## Validation Gates / Receipts

- `orca_start_preflight` recorded above; all three checkers ran with their **actual** output shown
  (none was a blocker — queue and scripts were readable). Python 3.11.15, PyYAML present.
- Absence claims are search-backed: header set via the `check_retrieval_header.py` sweep; dead-pointer
  counts via a context-tagged repo-wide scan over `git ls-files docs .agents/workflow-overlay`; row-010
  disposal via `git ls-files | grep` + `git ls-files --others --exclude-standard | grep` (both empty);
  `_test_runs` ignore via `git check-ignore`; `_scratch` non-ignore via `git check-ignore` (no match).
- Class-1 applied = 0, by evidence, not omission. No sealed material was opened beyond headers; no
  concurrent-lane file was read for body, edited, moved, committed, or deleted; no branch/worktree mutated.
- **Non-claims:** navigability/routing only. Not validation, readiness, acceptance, product proof,
  source-of-truth promotion, deletion/pruning authority, or doctrine change.

## Reproduction

```text
dead_pointer_sweep: context-tagged scan of git-tracked docs/ + .agents/workflow-overlay/ *.md;
  flag (docs|.agents|orca-harness)/...(.md|.yaml|.py) references with no file on disk;
  tag by YAML key context (open_next / historical-receipt / stale_if / prose).
header_sweep:  find docs .agents/workflow-overlay -name '*.md' -print0 | xargs -0 python .agents/hooks/check_retrieval_header.py
placement:     python .agents/hooks/check_placement.py --check
freshness:     python .agents/hooks/check_repo_map_freshness.py --changed
```

---

## Owner Sign-off & Execution (2026-06-11)

Owner reviewed the memo and authorized D1, D2, D3/D9, D7, D8 + commit. Executed and verified:

- **D8 (applied):** Re-pointed the 4 dead live pointers in
  `docs/product/data_capture_spine/data_capture_spine_linkedin_lane_index_v0.md` (L14/L34/L79/L81)
  to their `docs/product/data_capture_spine/` homes (targets confirmed on disk; sweep now shows 0 dead refs from this file).
- **D1 (applied, scoped):** Added the missing retrieval header to
  `.agents/workflow-overlay/project-authority.md` (lone overlay gap; passes `check_retrieval_header.py --strict`).
  The remaining ~116 pre-existing artifacts stay forward-only/opportunistic per owner — **not** backfilled (row 015 → partially done).
- **D2 (decided):** Owner kept the forward-only-resolve-via-`moved_paths_index.md` posture; no mass repoint (row 016 → resolved).
- **D7 (closed):** ORCA-HYGIENE-010 marked resolved — strays verified disposed.
- **D9 (applied):** Local `main` fast-forwarded to `origin/main` (`a7025b2`; was behind 14, ahead 0).
- **D3 (partial):** Deleted merged branch `dcp-restatement-integrity-port` (verified ancestor of `main`; commits preserved).
  **Held** `capture-probe-tiktok-demand` and `codex/data-capture-sourcing-architecture` — both merged but their
  worktrees carry **uncommitted work** (removal would destroy it); owner should commit/clear those worktrees first.
  **Held** `capture-armory-readme-slice1` — **not** merged into `origin/main`; confirm its PR state before any delete.

This addendum records execution only; it asserts no validation, readiness, or acceptance.
