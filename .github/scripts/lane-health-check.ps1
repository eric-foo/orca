#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Read-only lane health check: early detection of lane-isolation drift and of
    enforcement that lives only on this machine (not on origin/main).

.DESCRIPTION
    Backs the lane-isolation rule in AGENTS.md and the per-lane PR flow in
    docs/decisions/dev_workflow_ci_branch_protection_doctrine_v0.md. Lane
    isolation is a JUDGMENT rule, so this is a DETECTOR, not a gate: it surfaces
    drift early instead of hard-blocking. Run it yourself (or wire it into a
    periodic check); a non-zero exit is a nudge, not a block.

    Read-only with respect to the working tree, index, and local branches/commits:
    it never writes, stages, commits, pushes, or changes your checkout. It runs
    `git status` / `worktree list` / `ls-tree` / `ls-files` / `rev-parse`. `-Fetch`
    additionally performs a network `git fetch origin`, which updates only
    remote-tracking refs (refs/remotes/origin/*) and FETCH_HEAD - never the working
    tree, index, or local branches - so the not-on-main check sees current origin/main.

    Checks:
      1. dirty-volume          - modified + untracked count vs -DirtyThreshold.
                                 A large uncommitted pile-up on a shared base is the
                                 lane-isolation drift the rule guards against.
      2. worktree-sprawl       - linked-worktree count (the main worktree excluded)
                                 vs -WorktreeThreshold. Lanes are meant to be
                                 cleaned up at close.
      3. machine-local-        - any .agents/hooks/*.py physically present in the
         enforcement             working tree (tracked, untracked, or git-ignored)
                                 but NOT tracked on origin/main. Such a hook enforces
                                 only on this machine; a fresh clone of main would
                                 not have it, so any doctrine that calls it
                                 "enforced" is ahead of main's durable state.

    Exit codes: 0 = healthy (no warnings); 1 = one or more warnings (detection
    nudge); 2 = usage/abort error (no git, not a repo). Use -Json for machine
    output, -SelfTest to validate the detection logic without touching git.

.PARAMETER RepoPath
    Repository working tree to inspect. Default: the git toplevel of the cwd.

.PARAMETER DirtyThreshold
    Warn when modified+untracked file count exceeds this. Default 30.

.PARAMETER WorktreeThreshold
    Warn when the repo has more than this many linked worktrees (the main worktree
    is not counted). Default 4.

.PARAMETER Fetch
    Run `git fetch origin` first so the not-on-main check compares against an
    up-to-date origin/main. Off by default (no network). The fetch updates only
    remote-tracking refs and FETCH_HEAD, not the working tree, index, or local
    branches; the report notes when origin/main is only the local ref.

.PARAMETER Json
    Emit findings as JSON instead of human-readable text.

.PARAMETER SelfTest
    Run the detection logic against synthetic inputs and exit (0 ok / 1 fail).

.EXAMPLE
    pwsh .github/scripts/lane-health-check.ps1

.EXAMPLE
    pwsh .github/scripts/lane-health-check.ps1 -RepoPath C:\path\to\repo -Fetch

.EXAMPLE
    pwsh .github/scripts/lane-health-check.ps1 -SelfTest
#>
[CmdletBinding()]
param(
    [string]$RepoPath,
    [int]$DirtyThreshold = 30,
    [int]$WorktreeThreshold = 4,
    [switch]$Fetch,
    [switch]$Json,
    [switch]$SelfTest
)

$ErrorActionPreference = 'Stop'

# --- pure detection logic (no git, no IO; this is what -SelfTest exercises) --

function New-Finding([string]$Check, [string]$Level, [string]$Message) {
    [pscustomobject]@{ check = $Check; level = $Level; message = $Message }
}

function Test-DirtyVolume([int]$Modified, [int]$Untracked, [int]$Threshold) {
    $total = $Modified + $Untracked
    if ($total -gt $Threshold) {
        return New-Finding 'dirty-volume' 'warn' (
            "$total uncommitted files (modified=$Modified, untracked=$Untracked) exceed " +
            "threshold $Threshold - looks like lane pile-up on a shared base. Isolate work " +
            "in its own worktree/branch off main and land via the per-lane PR flow.")
    }
    New-Finding 'dirty-volume' 'ok' (
        "$total uncommitted files (modified=$Modified, untracked=$Untracked) within threshold $Threshold.")
}

function Test-WorktreeSprawl([int]$Count, [int]$Threshold) {
    if ($Count -gt $Threshold) {
        return New-Finding 'worktree-sprawl' 'warn' (
            "$Count linked worktrees exceed threshold $Threshold - stale lanes may not have " +
            "been cleaned up at close.")
    }
    New-Finding 'worktree-sprawl' 'ok' "$Count linked worktrees within threshold $Threshold."
}

function Test-MachineLocalEnforcement([string[]]$LocalHooks, [string[]]$MainHooks, [bool]$MainAvailable = $true) {
    if (-not $MainAvailable) {
        return New-Finding 'machine-local-enforcement' 'ok' (
            'skipped: origin/main not available locally (run with -Fetch to compare).')
    }
    $mainSet = @{}
    foreach ($h in $MainHooks) { if ($h) { $mainSet[$h] = $true } }
    $local = @($LocalHooks | Where-Object { $_ })
    $orphan = @($local | Where-Object { -not $mainSet.ContainsKey($_) })
    if ($orphan.Count -gt 0) {
        return New-Finding 'machine-local-enforcement' 'warn' (
            "enforcement hook(s) present locally but NOT tracked on origin/main: " +
            ($orphan -join ', ') + " - these enforce only on this machine; a fresh clone of " +
            "main lacks them, so any doctrine that calls them 'enforced' is ahead of main's " +
            "durable state. Land the hook on main, or state the liveness boundary in doctrine.")
    }
    if ($local.Count -eq 0) {
        return New-Finding 'machine-local-enforcement' 'ok' 'no .agents/hooks/*.py present in the working tree.'
    }
    New-Finding 'machine-local-enforcement' 'ok' (
        "all $($local.Count) local enforcement hook(s) are tracked on origin/main.")
}

# --- selftest ---------------------------------------------------------------

function Invoke-SelfTest {
    $cases = @(
        @{ name = 'dirty-under';  got = (Test-DirtyVolume 3 5 30).level;   expect = 'ok'   }
        @{ name = 'dirty-over';   got = (Test-DirtyVolume 10 40 30).level;  expect = 'warn' }
        @{ name = 'dirty-edge';   got = (Test-DirtyVolume 15 15 30).level;  expect = 'ok'   }  # total 30, not > 30
        @{ name = 'wt-under';     got = (Test-WorktreeSprawl 3 4).level;    expect = 'ok'   }
        @{ name = 'wt-over';      got = (Test-WorktreeSprawl 7 4).level;    expect = 'warn' }
        @{ name = 'wt-edge';      got = (Test-WorktreeSprawl 4 4).level;    expect = 'ok'   }  # 4, not > 4
        @{ name = 'enf-clean';    got = (Test-MachineLocalEnforcement @('.agents/hooks/a.py') @('.agents/hooks/a.py')).level; expect = 'ok' }
        @{ name = 'enf-orphan';   got = (Test-MachineLocalEnforcement @('.agents/hooks/guard.py') @('.agents/hooks/other.py')).level; expect = 'warn' }
        @{ name = 'enf-partial';  got = (Test-MachineLocalEnforcement @('.agents/hooks/a.py', '.agents/hooks/b.py') @('.agents/hooks/a.py')).level; expect = 'warn' }
        @{ name = 'enf-none';     got = (Test-MachineLocalEnforcement @() @('.agents/hooks/a.py')).level; expect = 'ok' }
        @{ name = 'enf-no-main';  got = (Test-MachineLocalEnforcement @('.agents/hooks/guard.py') @() $false).level; expect = 'ok' }
    )
    $ok = $true
    foreach ($c in $cases) {
        $pass = $c.got -eq $c.expect
        if (-not $pass) { $ok = $false }
        Write-Host ("{0}  {1,-12} expect={2,-5} got={3,-5}" -f ($(if ($pass) { 'PASS' } else { 'FAIL' })), $c.name, $c.expect, $c.got)
    }
    if ($ok) { Write-Host 'SELFTEST OK' -ForegroundColor Green; return 0 }
    Write-Host 'SELFTEST FAILED' -ForegroundColor Red
    return 1
}

if ($SelfTest) { exit (Invoke-SelfTest) }

# --- IO: gather real state (read-only) --------------------------------------

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host 'ABORTED: git not found on PATH.' -ForegroundColor Red; exit 2
}
if (-not $RepoPath) {
    $RepoPath = git rev-parse --show-toplevel 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $RepoPath) {
        Write-Host 'ABORTED: not inside a git repository (pass -RepoPath).' -ForegroundColor Red; exit 2
    }
}
if (-not (Test-Path $RepoPath)) {
    Write-Host "ABORTED: path does not exist: $RepoPath" -ForegroundColor Red; exit 2
}
$RepoPath = (Resolve-Path $RepoPath).Path
git -C $RepoPath rev-parse --show-toplevel *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Host "ABORTED: not a git repository: $RepoPath" -ForegroundColor Red; exit 2
}

if ($Fetch) { git -C $RepoPath fetch origin --quiet 2>&1 | Out-Null }

$branch = git -C $RepoPath rev-parse --abbrev-ref HEAD 2>$null

# 1) dirty volume
$porcelain = @(git -C $RepoPath status --porcelain 2>$null)
$modified  = @($porcelain | Where-Object { $_ -and $_ -notmatch '^\?\?' }).Count
$untracked = @($porcelain | Where-Object { $_ -match '^\?\?' }).Count

# 2) worktrees - exclude the main worktree (always the first entry) so the count
#    reflects lane worktrees only
$wtTotal  = @(git -C $RepoPath worktree list --porcelain 2>$null | Where-Object { $_ -match '^worktree ' }).Count
$wtLinked = [Math]::Max(0, $wtTotal - 1)

# 3) machine-local enforcement: local hooks vs origin/main hooks. No
#    --exclude-standard, so a hook that is both untracked AND git-ignored (the most
#    invisible machine-local enforcement) is still seen.
git -C $RepoPath rev-parse --verify --quiet origin/main *> $null
$mainAvailable = ($LASTEXITCODE -eq 0)
$localHooks = @(git -C $RepoPath ls-files --others --cached -- '.agents/hooks/' 2>$null |
    Where-Object { $_ -match '\.py$' } | Sort-Object -Unique)
$mainHooks = @()
if ($mainAvailable) {
    $mainHooks = @(git -C $RepoPath ls-tree -r --name-only origin/main -- '.agents/hooks/' 2>$null |
        Where-Object { $_ -match '\.py$' })
}

$findings = @(
    Test-DirtyVolume $modified $untracked $DirtyThreshold
    Test-WorktreeSprawl $wtLinked $WorktreeThreshold
    Test-MachineLocalEnforcement $localHooks $mainHooks $mainAvailable
)
$warns = @($findings | Where-Object { $_.level -eq 'warn' })

if ($Json) {
    [pscustomobject]@{
        repoPath      = $RepoPath
        branch        = $branch
        originMainRef = $(if ($Fetch) { 'fetched' } elseif ($mainAvailable) { 'local-ref (use -Fetch to refresh)' } else { 'unavailable' })
        findings      = $findings
        warnings      = $warns.Count
    } | ConvertTo-Json -Depth 5
    exit $(if ($warns.Count -gt 0) { 1 } else { 0 })
}

Write-Host "Lane health check - $RepoPath"
Write-Host "  branch: $branch    origin/main: $(if ($Fetch) { 'fetched' } elseif ($mainAvailable) { 'local ref (use -Fetch to refresh)' } else { 'unavailable' })"
Write-Host ''
foreach ($f in $findings) {
    $isWarn = $f.level -eq 'warn'
    Write-Host ("  [{0}] {1,-26} {2}" -f ($(if ($isWarn) { 'WARN' } else { ' ok ' })), $f.check, $f.message) -ForegroundColor ($(if ($isWarn) { 'Yellow' } else { 'Green' }))
}
Write-Host ''
if ($warns.Count -gt 0) {
    Write-Host "$($warns.Count) warning(s) - detection nudge, not a block." -ForegroundColor Yellow
    exit 1
}
Write-Host 'healthy.' -ForegroundColor Green
exit 0
