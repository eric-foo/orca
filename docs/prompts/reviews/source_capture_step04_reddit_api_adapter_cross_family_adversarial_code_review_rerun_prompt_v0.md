# Cross-Family Adversarial Re-Review (Patch Recheck) — STEP-04 Reddit API Adapter

```yaml
retrieval_header_version: 1
artifact_role: Cross-family re-review prompt
scope: Prompt for STEP-04 Reddit API adapter post-patch cross-family re-review.
use_when:
  - Running or auditing the STEP-04 Reddit API adapter re-review prompt.
  - Finding the prompt that checks prior STEP-04 patch closure.
authority_boundary: retrieval_only
```


```yaml
artifact_role: Cross-family adversarial patch-recheck prompt (bounded rerun)
review_lane: independent adversarial re-check (DIFFERENT model family from the author, which is Claude; read-only; reviewer does NOT patch)
prior_review: the first cross-family pass returned findings; the adapter + tests were patched. This recheck verifies the patches and scans only the touched scope.
decisive_criterion: do the patches close their intent (secret-leakage first), and did they introduce any NEW blocker/major in the touched scope?
load_rule: confirm-don't-trust — read the named files at current state before any firm claim.
authority_boundary: independent signal for owner adjudication only — not a completion gate that clears itself.
workspace: C:\Users\vmon7\Desktop\projects\orca
expected_branch: main
dirty_state: STEP-04 is uncommitted working-tree edits + untracked files; read in place; do not switch worktrees.
output: return findings in chat to the owner; write no files.
scope: BOUNDED. Verify the 5 patches below are sound + close their intent, then scan ONLY the touched functions for patch-caused or newly-visible blocker/major issues. Do NOT re-litigate the architecture or re-review untouched, previously-clean areas. Minor/nit outside the patched scope is out of scope.
```

## Frozen (do not re-open unless you find a NEW blocker)

- The adapter architecture (thin `RedditApiClient` seam; batch-over-posts; result types) is accepted for this recheck.
- Untouched, previously-clean code is out of scope.

## The 5 patches — verify each is SOUND and closes its intent

Files: `orca-harness/source_capture/adapters/reddit_api.py` and `orca-harness/tests/unit/test_source_capture_reddit_api.py`.

1. **Post-identity validation** (`_fetch_post_comments`, ~line 339): a `/comments` response is rejected as `MALFORMED_RESPONSE` unless the resolved post id is a string, matches `_POST_ID_RE`, AND equals the requested `post_id`. Verify it closes response-substitution. **Adversarial angle:** could it *false-reject valid live posts* if Reddit's id form differs between the listing child (`data.id`) and the `/comments` post `data.id` (e.g., a `t3_` prefix, casing)? Is that a correctness risk worth flagging for the live dry-run?
2. **Authenticated HTTPError body dropped** (`_RedditOAuthClient.get`, ~line 462): a non-2xx now returns `RedditApiResponse(status, body=b"")`. Verify no secret/echoed-header can flow via an error body, and that status-only is sufficient for the adapter's mapping. **Adversarial angle:** is there any *other* path where a real-client response body could carry echoed auth (the 2xx body? redirects?).
3. **API transport reason redacted + `from None`** (`get`, ~line 470): the `URLError` message is generic and the chain is suppressed. Verify the `exc.reason` cannot surface anywhere — message, `__cause__`, `__context__`, traceback, or `_transport_failure_kind` (which inspects `reason` only to pick an enum — confirm it never returns/logs it).
4. **Malformed token JSON → typed `AUTH_FAILED`** (`_ensure_token`, ~line 496): non-JSON token responses raise a typed transport error, not a crash. Verify the except ordering (JSON vs `HTTPError` vs `_BodyTooLargeError` vs `URLError`) cannot mis-catch or leak, and that a hostile token body can't crash or leak the secret.
5. **Token transport reason redacted + `from None`** (`_ensure_token`, ~line 513): same redaction for the token request. Verify no `reason`/credential leaks.

## Touched scope to scan for NEW blocker/major

- `_fetch_post_comments` (the new identity check), `_RedditOAuthClient.get`, `_RedditOAuthClient._ensure_token`.
- The added tests (mismatched-post-id, HTTPError-body-not-returned, transport-reason-redaction, malformed-token-JSON): are they real, or do they pass vacuously / assert the wrong thing?

Ask: did any patch introduce a regression, a new leak, a new crash path, or a false-passing test? Does the post-identity equality risk dropping valid posts?

## Output (return in chat to the owner)

- **VERDICT:** `closed-clean` | `closed-with-new-minor` | `not-closed-or-new-blocking`.
- For **each** of the 5 patches: `SOUND/CLOSED` or `NOT-CLOSED`, with `file:line` evidence.
- **SECRET-LEAKAGE re-statement:** after the patches, can any auth material reach a result/metadata/note/error/response/log? Yes/no with evidence.
- Any **NEW** blocker/major in the touched scope: `file:line`, severity, real-vs-theoretical, one-line fix.
- **UNVERIFIABLE:** anything you could not confirm (e.g., live Reddit id forms / live OAuth — the real client is exercised only against a fake `urlopen`).

Keep findings concrete and source-grounded. Authority boundary: independent signal for the owner, not an authorization or completion gate.
