# Cross-Family Adversarial Code Review — STEP-04 Reddit API Adapter

```yaml
retrieval_header_version: 1
artifact_role: Cross-family adversarial code review prompt
scope: Prompt for STEP-04 Reddit API adapter cross-family adversarial code review.
use_when:
  - Commissioning or auditing the STEP-04 Reddit API adapter review.
  - Finding the prompt for Reddit API adapter review context.
authority_boundary: retrieval_only
```


```yaml
artifact_role: Cross-family adversarial code-review prompt
review_lane: independent adversarial check (DIFFERENT model family from the author, which is Claude; read-only; reviewer does NOT patch)
decisive_criterion: secret-leakage safety first, then correctness + honest-limitation + contract fit
load_rule: confirm-don't-trust — read every named file before any firm claim; name anything you could not verify.
authority_boundary: independent signal for owner adjudication only — not a verdict that authorizes, validates, or unblocks anything on its own.
workspace: C:\Users\vmon7\Desktop\projects\orca
expected_branch: main
dirty_state: STEP-04 is UNCOMMITTED working-tree files (new); read in place; do not switch or create worktrees.
output: return findings in chat (transcript) to the owner; write no files.
```

## Your job

You are an **independent reviewer from a different model family than the author** (the author is Claude). Catch what a same-family reviewer would share a blind spot on. **A same-family review was NOT seeded into this prompt — attack the code fresh and unanchored.** Be **adversarial**: try to **refute** the claim that this Reddit API capture adapter is safe and correct. This handles API **secrets** (an OAuth client_secret + a bearer token), so the **top priority is secret-leakage**. Default to skeptical; if you cannot access a file, say so.

## Background (verify against the files)

A source-capture harness added an application-only (read-only public data) Reddit API adapter. Design: a free function `fetch_reddit_api_capture(...) -> Success | Failure` over a **thin `RedditApiClient` Protocol seam** (`get(path, params) -> RedditApiResponse(status, body)`); tests inject a **fake** client (no network); the **real `_RedditOAuthClient`** (stdlib `urllib`) does the OAuth (client_credentials grant → 1-hr bearer) behind the seam and is meant to keep all auth material inside itself. Post = one captured unit; each post's verbatim `/comments/{id}` response is the preserved payload (batch-over-posts, partial failures surfaced per post). The adapter never writes a packet (a runner, not yet built, does that).

## Files to read (read each fully)

- `orca-harness/source_capture/adapters/reddit_api.py` — the adapter, the result types, the Protocol seam, and the real `_RedditOAuthClient` + `build_reddit_oauth_client`.
- `orca-harness/tests/unit/test_source_capture_reddit_api.py` — the offline tests (judge whether they actually prove safety; what's NOT covered).
- `orca-harness/tests/contract/test_source_capture_reddit_api_contract.py` — the import allowlist.
- `orca-harness/source_capture/adapters/__init__.py` — exports.
- Behavior/contract references: `orca-harness/source_capture/adapters/direct_http.py` (result-type + transport precedent), `orca-harness/source_capture/adapters/media_asset.py` (batch precedent), `orca-harness/source_capture/reddit_credentials.py` (the credentials the real client consumes), `orca-harness/docs/adapter_author_contract.md` (the adapter contract + invariants).

## Hard invariants — try to BREAK each

1. **No secret escapes the seam (TOP PRIORITY).** The `client_secret`, the HTTP Basic header, and the bearer token must never reach any **result field**, any **`metadata` dict**, any **`warning_notes`/`limitation_notes`**, any **error message / `RedditApiTransportError`**, any **`RedditApiResponse`**, or a log/`repr`. Trace every path. Probe: an `HTTPError` body echoing the request; a malformed-response branch; the token-request failure messages; the cached token; `RedditApiResponse` returned to the adapter; the `request_descriptor`. Find any leak, even theoretical.
2. **The seam genuinely hides auth.** `RedditApiResponse` carries only `status` + `body`. Confirm the real client never returns the token/secret to the adapter, and the adapter (which has no credentials) cannot reconstruct them.
3. **Graceful failure, never a crash.** A non-2xx (403/404/429/5xx), a transport error, an empty body, or a **malformed/hostile JSON shape** (None, missing keys, wrong types, a non-list `children`, an empty `[post, comments]`) must become a typed `Failure`/per-post failure — not an unhandled exception. Try to crash the parser.
4. **No path/query injection.** `subreddit` and `post_id` flow into the request path (`/r/{sub}/{listing}`, `/comments/{id}`). Attack the validation regexes + `urlencode`: can a crafted value escape the path, inject a query, or hit a different endpoint?
5. **OAuth client correctness.** Token caching + expiry (monotonic logic, the 60s buffer) — can a stale/expired token be used, or a token be fetched every call? Basic-auth construction, the `grant_type`, the bearer header, the size-cap read, and the auth-vs-network-vs-timeout error mapping — all correct?
6. **Honest limitations + contract fit.** Is the "comments not recursively expanded (`more` stubs preserved)" limitation honest and present? Does a partial failure surface as both a per-post failure AND a capture-level limitation? Does it follow `adapter_author_contract.md` (never imports the writer; `fetch_* -> Success|Failure`; no `praw`/`requests`/SDK)?
7. **Tests prove what they claim.** Are the unit tests circular/shallow? Does the fake-`urlopen` test actually prove Basic→token / bearer→api and no-secret-back? What real case is NOT covered (e.g., token expiry/refresh, size-cap, a 5xx, a hostile JSON shape, the `more`-stub preservation)?

## Output (return in chat to the owner)

- **VERDICT:** `clean` | `minor-issues` | `blocking-issues`.
- **SECRET-LEAKAGE STATEMENT (explicit):** can any auth material (`client_secret` / Basic header / bearer token) reach a result field, metadata, note, error, response, or log? Yes/no, with `file:line` evidence either way.
- **FINDINGS:** numbered. Each: `file:line`, severity (`blocking`/`major`/`minor`/`nit`), the concrete problem, **real** vs theoretical, one-line fix.
- **STRONGEST SINGLE CONCERN.**
- **UNVERIFIABLE:** anything you could not confirm (e.g., live Reddit JSON shapes, live OAuth behavior — the real client is exercised only against a fake `urlopen`, never live).

Keep findings concrete and source-grounded; cite line numbers you read. Authority boundary: your output is an independent signal for the owner, not an authorization or a completion gate. Note that the no-secret-in-**packet** test belongs to the not-yet-built runner (STEP-05/07); here, judge the adapter's part of the secret path (no secret in any **result**).
