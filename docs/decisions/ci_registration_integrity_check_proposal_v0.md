# CI Registration-Integrity Check — Proposal v0

```yaml
retrieval_header_version: 1
artifact_role: Orca decision proposal
scope: >
  Proposes promoting ORCA's registration->artifact integrity signal to a CI check
  (the workspace-independent, false-positive-free half of the lane-health detector),
  landed on a focused branch off main. Carries the detector pointer and the ci.yml
  job. The detector is built and verified; nothing is wired into CI from this tree.
use_when:
  - Deciding or landing the ORCA CI registration-integrity check.
  - Adding the detector + ci.yml job on a branch rooted on origin/main.
  - Extending the detector with a new registry->artifact check.
authority_boundary: retrieval_only
open_next:
  - .agents/checks/registration_integrity.py                           # the detector this proposes (canonical; do not duplicate)
  - .github/workflows/ci.yml                                           # on origin/main; the job target
  - docs/decisions/overlay_enforcement_placement_classification_v0.md  # the enforcement-placement doctrine this instantiates
  - docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md    # structure-B, 403 server gate, focused-branch landing path
stale_if:
  - The detector or the ci.yml job is landed on origin/main (this becomes a record of how, not a proposal).
  - The .claude/settings.json hook-registration shape changes (the parse assumptions move).
  - A second registry->artifact check is added (update the Extension section).
```

## Status / non-claims

The detector `.agents/checks/registration_integrity.py` is **built and verified** in
this lane. This proposal **wires nothing into CI** — `.github/workflows/ci.yml` lives
on `origin/main`, which this integration tree (`ecr-sp3-*`, 27 commits behind `main`)
does not carry, so the job is delivered here as a diff for a branch rooted on `main`.
No push, no PR, no merge: landing is **off `main`, human-merged** (the protected-action
guard blocks an agent from merging its own PR). No readiness, validation, or
server-gate claim is made.

## Problem

A shared registry/config names an artifact by path; if the artifact is absent, a
**fresh clone breaks**. The sharpest ORCA instance: `.claude/settings.json` registers
hooks as `python .agents/hooks/<x>.py`; a registered script that does not exist in the
tree **errors on every matching tool call**. This session carried that "don't commit a
registration whose script isn't also committed" rule **by hand** (the dangling-
registration coupling). Hand-carried discipline is exactly what the enforcement-
placement doctrine says to promote to a deterministic substrate when the signal is
cheap and false-positive-free.

## Goal

Promote **only** the single workspace-independent, false-positive-free signal —
"every artifact a registry names exists in the tree" — to a CI check. Leave the
workspace-local health nudges (uncommitted pile-up, worktree sprawl, present-locally-
but-not-yet-on-`main`) **manual**: a clean CI checkout has no local pile-up, and a PR's
newly-added artifact legitimately is not on `main` yet, so those signals would
false-positive in CI.

## Solution

**Detector** → `.agents/checks/registration_integrity.py` (canonical; see `open_next`).
Contract:
- `--checks hook-registration` (default = all): every `.py` referenced by a hook
  `command` in `.claude/settings.json` must exist in the tree.
- **Decidable from the checked-out tree alone** — reads `settings.json` + the
  filesystem; **no base ref, no git, no network** (a shallow CI checkout works and
  cannot false-positive on "new in this PR").
- **Directional** — entry→file only; never flags a file that merely lacks a registry
  entry (READMEs / special-purpose files are legitimately unregistered).
- **Fails loud** — unknown/empty `--checks` or unreadable settings → exit `2`; never a
  silent no-op. Exit codes: `0` pass · `1` dangling reference (the defect) · `2` misuse.
- `settings.local.json` (gitignored) is intentionally not consulted — only the
  committed `settings.json` a fresh clone has.

**CI job** → add a **separate** job to `.github/workflows/ci.yml` (distinct red/green
from the pytest job), on a branch rooted on `origin/main`:

```yaml
  registration-integrity:
    name: registration-integrity
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Registration integrity (registry entry -> artifact exists)
        run: python .agents/checks/registration_integrity.py --checks hook-registration
```
(Stdlib-only — no `pip install` needed; `setup-python` only pins the version to match
the existing job.)

**Doctrine placement.** This is the **SUBSTRATE** verdict from the enforcement-placement
classification: an actor-carried rule (dangling-registration discipline) moved onto a
deterministic check. It is **not** a new doctrine — no overlay-authority rule is edited
— so no `direction_change_propagation` receipt is owed by the detector itself.

## Verification evidence (this lane, current tree)

- `python .agents/checks/registration_integrity.py --selftest` → **9/9 PASS** (incl.
  detects-missing-script and fail-loud-on-misuse).
- `python .agents/checks/registration_integrity.py --checks hook-registration` → `OK`,
  **exit 0** — green on a consistent tree (no false positive).
- `--checks bogus` → **exit 2** (loud), never a silent pass.
- Scoped against `origin/main` (correct vantage): `main`'s `settings.json` registers
  `guard_protected_actions.py`, `check_retrieval_header.py`, `check_repo_map_freshness.py`;
  `git ls-tree origin/main -- .agents/hooks/` confirms **all three present** → the check
  is **green on `main` today**, red only on a real defect.

## Enforcement reach (honesty)

A non-zero exit fails the PR's check run. ORCA branch protection is **403-blocked**
(private/free repo, per the dev-workflow doctrine), so this is a **strong signal under
merge-when-green / structure-B discipline, not a server-enforced merge gate** — it does
not, by itself, block a merge. This is a **defect check, not a nudge**: failing CI on a
real fresh-clone-breaking defect is correct and does not contradict the "lane-health
detector is advisory" stance, which governs the *local* nudges only.

## Landing steps (off `main`, human-merged)

1. Branch off `origin/main` (focused, not the `ecr-sp3` mega-batch — dev-workflow
   doctrine + PR #1 lesson).
2. Add the detector `.agents/checks/registration_integrity.py` (cherry-pick this lane's
   commit if committed, else copy the canonical file).
3. Apply the `ci.yml` job diff above.
4. Resolve the repo-map freshness signal for the new `.agents/checks/` area: add it to
   `docs/workflows/orca_repo_map_v0.md` **or** record `repo-map-ack: <reason>` in the
   commit message.
5. Add a one-line traceability receipt; narrow any stale doc line that says no CI
   registration check exists.
6. **Independent scoping review before landing** — a cold, cross-vendor pass on the
   detector's parse/scoping logic specifically (a buggy filter could mask the defect or
   false-fail a PR). Route via `workflow-delegated-review-patch` / the portable
   adversarial-artifact-review method — dog-foods ORCA's own review-lanes doctrine.
7. Human merges (the guard blocks an agent self-merge).

## Extension (documented, not shipped)

A second `--checks` value `template-registry` (template-registry.md "Registered
Templates" table → each Primary path exists) is the natural next check: same detector
pattern, same directional/no-network properties. Verified all **9** registered
templates exist on `origin/main` today, so it would also be green-on-`main`. Add it as a
new entry in `CHECKS` (callers default to all, so adding it is non-breaking) once it has
the same independent scoping review.
```
