# Turn 07 Branch Casing Decision

- Decision ID: T7-AW-04
- Status: PROPOSED_LOCK
- Decision date: 2026-05-13
- Decision: Orca default branch casing is main.
- Prior branch observed before rename: Main
- Branch observed after rename: main
- Commit state before decision: no commits
- Action: renamed unborn branch Main to main before first commit.
- Rationale: lowercase main avoids avoidable cross-workspace friction in prompts, scripts, remotes, and future automation. No Orca-specific reason to keep Main was identified.
- Publication boundary: no commit, push, remote setup, branch publication, or PR is authorized in this turn.
- Rollback: reverse the branch rename only before the first commit and only with explicit approval.
