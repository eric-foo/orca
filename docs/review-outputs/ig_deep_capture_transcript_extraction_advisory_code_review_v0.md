# IG Deep Capture Transcript Extraction — Advisory Code Review v0

```yaml
retrieval_header_version: 1
artifact_role: Review output (advisory implementation/code review)
scope: >
  Findings-first advisory adversarial code review of the IG deep-capture
  transcript extraction patch: making completed per-reel deep-capture transcript
  records feed product extraction and behavioral projection with exact source
  identity, idempotence, and failure visibility, without forcing shared IG/YT
  acquisition machinery.
authority_boundary: retrieval_only
source_prompt: docs/prompts/reviews/ig_deep_capture_transcript_extraction_adversarial_code_review_prompt_v0.md
review_lane: implementation/code review (workflow-code-review), zero-config findings-only advisory
output_mode: review-report (filesystem-output)
report_path: docs/review-outputs/ig_deep_capture_transcript_extraction_advisory_code_review_v0.md
reviewed_by: Anthropic Claude Opus 4.8 (claude-opus-4-8)
authored_by: OpenAI/Codex GPT-5
de_correlation_bar: cross_vendor_discovery
same_vendor_rationale: not_applicable
target_branch: codex/ig-deep-capture-transcript-extraction
target_commit: e5a5765408461ba42fa7b3eef850b9ef953497f6
base_commit: 32e2d888f07ce345abadd521dca0dff9db93e264
reviewer_verdict: NOT_CLAIMED
```

## Commission

- **Commissioned target/purpose:** read-only adversarial implementation/code review of the
  9-file patch on `codex/ig-deep-capture-transcript-extraction` @ `e5a5765` that makes
  completed per-reel deep-capture transcript records feed product extraction and behavioral
  projection. Find blocker/major correctness, scope, validation, boundary, idempotence, or
  false-confidence issues.
- **Authority:** advisory implementation/code review. Formal verdict, severity authority,
  readiness, approval, validation pass/fail, patch queue, runtime-model recommendation, and
  the survives-adversarial-review/no-new-seam claim are **NOT_CLAIMED** (the prompt withholds
  them). `critical`/`major`/`minor` below are finding-priority labels only and create no
  approval, blocker, or remediation authority.
- **Decision criteria (fitness reference, from the prompt):** completed deep-capture transcript
  records are discovered, source-keyed, extracted exactly once, carried into the lake/projection,
  and tested, without weakening standalone-audio or YouTube transcript extraction; IG and YT are
  *not* required to share acquisition method/ladder/packet/flow (transcript-feed/identity/projection
  parity only).
- **De-correlation:** author family = OpenAI/Codex GPT-5; reviewer family = Anthropic/Claude
  (Opus 4.8). Vendors differ → the `cross_vendor_discovery` who-constraint is satisfied. This
  records the who-constraint only; it is **not** a no-new-seam claim and **not** a runtime-model
  recommendation.

## Source Context

`SOURCE_CONTEXT_READY`.

Staleness gate (from the prompt) checked and clear: branch HEAD `= e5a5765…`, base `origin/main
= 32e2d88…`, working tree clean, and all 9 `target_blob_ids` matched verbatim via
`git ls-tree e5a5765 …`. The reviewer inspected the pinned worktree/branch directly.

### Source-read ledger

| Source | Why read | Status |
| --- | --- | --- |
| `git diff/ls-tree/status` on the pinned worktree | confirm HEAD/base/blob ids vs staleness gate | clean, all matched |
| `orca-harness/runners/run_ig_reels_product_extract.py` (full) | primary patch surface (243-line runner) | read |
| `orca-harness/cleaning/transcript_product_lake.py` (full) + diff | `mentions_record_id` source-key digest, payload identity fields | read |
| `orca-harness/cleaning/transcript_product_extractor.py` (full) + diff | `TranscriptInput` new optional fields, `joined_text` | read |
| `orca-harness/source_capture/ig_reels_behavioral_lake.py` (full) + diff | extraction-result identity propagation | read |
| `orca-harness/source_capture/ig_reels_behavioral_projection.py` (full) + diff | feed-eligibility flip, block/complete semantics, correlation | read |
| `orca-harness/source_capture/ig_reels_deep_capture_lake.py` (full) | deep-capture record-set write contract (record_id) | read (context) |
| `orca-harness/source_capture/ig_reels_deep_capture.py` (full) | `ReelDeepCaptureResult` posture vocabulary | read (context) |
| `orca-harness/data_lake/root.py` (full) | `append_record_set`/`is_record_set_complete`/`record_path` key+shard contract | read (context) — load-bearing for the silent-skip check |
| `orca-harness/runners/run_transcript_product_extract.py` (full) | YT runner — backward-compat / no-regression | read (context) |
| `orca-harness/source_capture/transcript/audio_asr.py` (lines ~60-90) | real ASR success posture (`transcribed`) | read (context) |
| `orca-harness/tests/contract/test_no_llm_imports.py` (full) | no-LLM runner boundary | read (context) |
| 4 changed test files (diffs) + grep of `_deep_transcript`/posture helpers | test adequacy axis | read |
| grep `"source_key"` across `orca-harness` | confirm vestigial alternate-key path | read |

### Validation run status

`validation_rerun_by_reviewer` (offline, fakes injected — `faster_whisper` never imported). Independently
reproduced the dispatcher-observed results on the pinned worktree:

- focused suite (`test_ig_reels_product_extract`, `test_ig_reels_behavioral_projection`,
  `test_ig_reels_behavioral_lake`, `test_transcript_product_lake`): **48 passed**.
- no-LLM contract (`test_no_llm_imports`): **1 passed**.
- shared/YT smoke (`test_transcript_product_extractor`, `test_youtube_caption_product_extract`,
  `test_youtube_behavioral_projection`): **54 passed**.

Total 103 green. This is evidence, not a formal validation/pass claim.

## Findings (ordered by materiality)

No **blocker** found. The core capability is correct on the reviewed scope (see "Verified correct"
below). One **major** review-confidence finding and four **minor** findings follow. `patch_queue_entry`
is **`no`** for every finding (this prompt authorizes no patch/queue).

---

### F1 — major (review confidence + latent contract ambiguity): the deep-capture success posture is ambiguous in-tree and the runner-grain test exercises only one of the two accepted tokens

- **Commissioned target/purpose:** "genuinely discovers completed deep-capture transcript record
  sets and does not silently skip a valid per-reel transcript"; "tests prove load-bearing behavior
  … deep-capture discovery."
- **Reviewed target / location:**
  - runner filter — [`run_ig_reels_product_extract.py:208`](../../../ig-deep-capture-transcript-extraction/orca-harness/runners/run_ig_reels_product_extract.py): `record.get("transcript_posture") not in {"ok", "transcribed"}`.
  - runner-grain test helper default — `test_ig_reels_product_extract.py:92-93` (`_commit_ig_deep_capture(..., posture="transcribed")`) and the only deep-capture runner test `test_runner_extracts_deep_capture_transcript_records` (`:190`).
  - contract vs implementation disagreement — `ig_reels_deep_capture.py:176` documents the deep-capture transcriber posture as `'ok'/'no_speech'/'failed'`; the only concrete ASR transcriber `audio_asr.py:88` emits `posture = "transcribed" if cues else "no_speech"` (never `'ok'`); the projection `_normalise_deep_posture` (`ig_reels_behavioral_projection.py:691-694`) maps `'ok'→'transcribed'` and the projection deep-capture tests default `_deep_transcript()` to `transcript_posture="ok"` (`test_ig_reels_behavioral_projection.py:70-75`).
- **Implementation evidence:** the success token for a transcribed deep-capture reel is written
  verbatim from `result.transcript_posture` into `REEL_TRANSCRIPT_LANE`
  (`ig_reels_deep_capture_lake.py:123-130`). Two in-tree sources disagree on what that token is:
  `'ok'` (the `ReelDeepCaptureResult` contract + the deep-capture unit-test fakes, e.g.
  `test_ig_reels_deep_capture.py:195,214`) vs `'transcribed'` (the real `audio_asr` transcriber).
  The runner correctly defends by accepting **both**. But the runner-grain end-to-end test commits
  only `"transcribed"`, and the projection-grain tests cover only `"ok"`. No single test pins the
  posture the production producer actually persists, and no runner test exercises `"ok"`.
- **Authority/evidence basis:** repo-visible code + tests (the live deep-capture producer wiring —
  which `transcribe_fn` is injected — is **outside the reviewed target/context scope**; only test
  callers of `run_reel_deep_capture` are visible).
- **Impact (review confidence / false confidence):** the accept-both set is load-bearing, not
  redundant, precisely because the two layers disagree. A later "cleanup" that narrows the runner
  to a single token (trusting either source-of-truth) would silently drop every real deep-capture
  transcript carrying the other token — the exact "silently skip a valid per-reel transcript"
  failure this patch exists to prevent — and **no runner test would fail** (the runner test would
  still pass on `"transcribed"`; projection tests don't exercise the runner). Current behavior is
  correct by inspection; the gap is regression protection + an unresolved posture contract.
- **`minimum_closure_condition`:** the production deep-capture success posture is pinned to one
  source of truth (reconcile `ReelDeepCaptureResult`'s documented `'ok'` against `audio_asr`'s
  `'transcribed'`), **and** a runner-grain test exercises discovery+extraction for that production
  posture (so a single-token narrowing of the runner filter is caught).
- **`next_authorized_action`:** home model / owner decision — reconcile the posture vocabulary and
  add the missing runner-grain coverage. No patch authorized by this prompt.
- **Verification expectation:** red-green — add a runner test committing the production posture and
  assert `count_pending_extractions == 1` + an `extracted` result; confirm it fails if the runner
  filter is narrowed to exclude that token.
- **`patch_queue_entry` authorized:** no.

---

### F2 — minor (clarity / vestigial code): `source_key` is read and indexed as an alternate exact key but is never written by any producer

- **Reviewed target / location:** `ig_reels_behavioral_lake.py:259` (`"source_key": _string_or_none(body.get("source_key"))`); `ig_reels_behavioral_projection.py:585` and `:607` (lookup + index on `"source_key"`); also pre-existing `youtube_capture/behavioral_projection.py:627`.
- **Implementation evidence:** the sole writer of the mentions payload, `extract_products_into_lake`
  (`transcript_product_lake.py:119-132`), writes `transcript_source_key`, `source_route`,
  `asr_record_id` — **never** `source_key`. A repo grep finds `source_key` read in 4 places and
  written in 0. The projection source dict (`_base_transcript_source`) likewise has
  `transcript_source_key` but no `source_key`, so `_result_for_source`'s `source.get("source_key")`
  is also always `None`.
- **Authority/evidence basis:** repo-visible code + grep.
- **Impact (review confidence):** harmless at runtime (every read is `None`-guarded), but it is dead
  alternate-key plumbing that implies a second exact-key channel which does not exist; a future
  reader may wire correlation to `source_key` and silently get no matches.
- **`minimum_closure_condition`:** either a producer writes `source_key`, or the `source_key` reads
  are removed / documented as reserved-unused.
- **`next_authorized_action`:** owner decision (drop or document). No patch authorized here.
- **Verification expectation:** grep shows `source_key` written by at least one producer, or removed
  from the read sites; existing exact-key tests still pass.
- **`patch_queue_entry` authorized:** no.

---

### F3 — minor (dead code from the feed-eligibility flip): `NON_ELIGIBLE_RESIDUAL_REASONS` is now empty and `"deep_capture_not_in_extraction_feed"` is unreachable

- **Reviewed target / location:** `ig_reels_behavioral_projection.py:34` (`NON_ELIGIBLE_RESIDUAL_REASONS: set[str] = set()`); reason emitted at `:386-387` inside `_eligibility`; residual branches keyed on the empty set at `:444` and `:636`.
- **Implementation evidence:** both callers of `_base_transcript_source` now pass
  `extraction_feed_eligible=True` (`_standalone_audio_source:297`, `_deep_capture_source:334`), so
  `_eligibility` never reaches the `return False, "deep_capture_not_in_extraction_feed"` branch, and
  the two `… in NON_ELIGIBLE_RESIDUAL_REASONS` checks are always `False`. (Tiny adjacent nit: the
  `or ()` on `run_ig_reels_product_extract.py:190` is inert — a generator is always truthy.)
- **Authority/evidence basis:** repo-visible code.
- **Impact (review confidence):** functionally correct — deep capture *is* in the feed now, so the
  "not in feed" residual should no longer fire. But the retained constant + unreachable reason +
  dead branches imply a state that can no longer occur, which can mislead future edits. The
  `extraction_feed_eligible` parameter is still a real extensibility seam (a future non-feed source
  could pass `False`); the dead pieces are the empty residual set and the now-unreachable reason
  string.
- **`minimum_closure_condition`:** the dead reason/branches are removed, or a comment records that
  the `extraction_feed_eligible=False` path is intentionally retained for a future source kind.
- **`next_authorized_action`:** owner decision. No patch authorized here.
- **Verification expectation:** projection tests still pass after removal/annotation.
- **`patch_queue_entry` authorized:** no.

---

### F4 — minor / residual (robustness-vs-docstring): discovery *enumeration* is not failure-isolated, contradicting the runner's "never aborts" contract

- **Reviewed target / location:** runner docstring claim `run_ig_reels_product_extract.py:6-9`
  ("per-item failure isolated at BOTH grains … the batch never aborts"); deep-capture enumeration
  `_deep_capture_transcripts` (`:188-229`) consumed in `run_extraction` at `:322` **outside** any
  try; packet enumeration `_candidate_packet_ids` consumed at `:303` likewise outside try.
- **Implementation evidence:** per-*packet* discovery and per-*transcript* extraction are isolated
  (try/except → `discovery_failed`/`failed`), but the directory walks themselves are not. A
  transient `iterdir()` `OSError` during the derived-tree scan (or a corrupt availability JSON in
  `list_available`, `root.py:900`, which is unguarded) propagates out of `run_extraction`, aborting
  the run and **discarding the already-accumulated `results` list** rather than returning partial
  status.
- **Authority/evidence basis:** repo-visible code. This is a **pre-existing pattern** — the YT
  runner (`run_transcript_product_extract.py:143`) and the behavioral-lake adapter
  (`ig_reels_behavioral_lake._collect_deep_capture_inputs`) share it; the new deep-capture phase
  follows it rather than worsening it.
- **Impact (residual risk):** low probability on a local single-operator lake, but it is a real gap
  between the advertised "never aborts" daemon contract and behavior under a transient FS error
  during enumeration.
- **`minimum_closure_condition`:** either enumeration errors are isolated (best-effort skip with a
  surfaced status) so the batch genuinely never aborts, or the docstring's "never aborts" scope is
  narrowed to per-item extraction.
- **`next_authorized_action`:** owner decision. No patch authorized here.
- **Verification expectation:** a test simulating an enumeration-time `OSError` returns a status list
  (or the docstring is corrected); existing tests unaffected.
- **`patch_queue_entry` authorized:** no.

---

### F5 — minor (test strength): backward-compat of the no-source-key `mentions_record_id` is asserted only by relative inequality, not pinned to a golden id

- **Reviewed target / location:** `test_transcript_product_lake.py` →
  `test_mentions_record_id_keys_on_content_model_and_optional_source_key`.
- **Implementation evidence:** the test proves stability, content-keying, model-keying, and
  source-key disambiguation, but does not pin the **no-key** id (`transcript_source_key is None`) to
  a fixed/golden value. Byte-for-byte backward compatibility of pre-existing YT/standalone mentions
  ids therefore rests on inspection of the `if transcript.transcript_source_key:` guard
  (`transcript_product_lake.py:88-90`) — which is correct — rather than a regression-locking
  assertion.
- **Authority/evidence basis:** repo-visible code + test.
- **Impact (review confidence):** low. The guard is obvious and correct (no key → digest =
  `sha256(joined_text)`, identical to pre-patch), but a future refactor of the digest input could
  silently re-key all legacy records without failing this test.
- **`minimum_closure_condition`:** a test pins the no-key id to an expected constant (or equivalently
  asserts it equals the pre-patch formula) so a digest-input change is caught.
- **`next_authorized_action`:** owner decision. No patch authorized here.
- **Verification expectation:** add the golden/equivalence assertion; confirm it fails if the digest
  input is altered.
- **`patch_queue_entry` authorized:** no.

## Verified correct (source-backed non-findings)

These are the prompt's review axes checked and found sound on the reviewed scope; recorded so the
home model can see coverage, not as approval.

- **Discovery has no key-mismatch silent skip.** `append_record_set` (`root.py:577-653`) writes every
  member lane **and** the completion marker under the **same** `record_id`, and
  `is_record_set_complete`/`record_path` recompute the same `anchor_shard(raw_anchor)`
  (`root.py:655-760`). So `_deep_capture_transcripts` iterating `DEEP_CAPTURE_SET_LANE` and then
  reading `REEL_TRANSCRIPT_LANE` by that same `record_id` (`:190-207`) reads the key that provably
  exists. Mirrors the established `_collect_deep_capture_inputs` pattern. (Posture-token coverage is
  the separate concern in F1.)
- **Filtered to the completed transcript shape.** Only `is_record_set_complete` sets with
  `transcript_posture ∈ {ok, transcribed}`, non-empty cues, and a shortcode are admitted
  (`:200-214`); failed/`no_audio_handle`/`download_failed`/`render_unavailable`/`no_speech` are not
  extracted.
- **Exact source key prevents false dedup.** The deep-capture source key embeds the content-addressed
  deepcap `record_id` (`_transcript_source_key`, `:143-146`), folded into the `mentions_record_id`
  digest (`transcript_product_lake.py:87-91`); two distinct renders of one reel → distinct keys →
  distinct mentions ids, stored under per-shortcode anchors. No accidental collision with the
  standalone-audio path (different anchor = `packet_id`, no source key).
- **`mentions_record_id` backward compatible.** With `transcript_source_key is None` (YT + standalone
  IG audio), the digest input is exactly `joined_text` — identical to pre-patch.
- **Identity persisted without becoming required.** The payload always carries the three identity
  fields (null for older flows; `transcript_product_lake.py:119-132`); all consumers read via
  `.get(...)`; no strict schema enforces them. The 54-test YT/shared smoke is green with the added
  null fields → no YT regression observed.
- **Lake → projection correlation by exact key.** The adapter lifts `transcript_source_key`/
  `source_route`/`asr_record_id` from the payload (`ig_reels_behavioral_lake.py:258-261`); the
  projection indexes by `transcript_source_key` and the deep-capture source key matches it exactly,
  with an anchor fallback guarded by `_duplicate_eligible_anchors` against ambiguity.
- **Projection blocks clean `complete` when unextracted, completes when extracted.** Deep capture is
  now `extraction_feed_eligible=True` (`:334`); unextracted → `not_attempted`/`incomplete` →
  `complete=False` (test `…blocks_complete_claim`), exact-key extraction → `complete` (test
  `…extraction_eligible_and_exact_keyed`, and the real-lake adapter test now asserts `complete`).
- **Failure states not hidden behind another source's success.** `failed`/`render_unavailable`/
  `no_audio_handle`/`download_failed` postures land in `SOURCE_POSTURE_PROBLEMS` →
  residual + `source_problem_count`, downgrading even an otherwise-extracted reel to
  `complete_with_residuals` (`_extraction_rollup`, `:410-484`).
- **No-LLM runner boundary preserved.** The runner imports only the cleaning driver + pure
  `source_capture` parsers (no `openai/anthropic/litellm/langchain`); `test_no_llm_imports`
  (direct-import AST check over `runners/`) is green. No live browser/network/Cleaning-ontology/
  Judgment/dashboard/creator-ledger import in the projection path.
- **No unauthorized parity/doctrine claims.** Runner and projection docstrings explicitly scope IG as
  its own runner and disclaim YT capture-machinery unification; no shared-capture-core, acquisition-
  parity, data-lake-propagation-doctrine, live-capture-completeness, or creator-ledger-readiness
  claim is implied.

## Not-proven boundaries / strict-only blockers

- No formal review verdict, severity authority, readiness, approval, validation pass/fail, no-new-seam,
  or patch authority is asserted (withheld by the prompt). The green test reruns are evidence, not a
  pass claim.
- The **live deep-capture producer wiring** (which `transcribe_fn` the production path injects, and
  therefore the posture token actually persisted) is outside the reviewed target/context scope — see
  F1. Correctness of the real production posture path is **not proven here**; it is mitigated, not
  closed, by the runner's accept-both.
- `reviewed_by`/`authored_by` are operator-confirmable provenance facts recorded here; they are not a
  model recommendation or ranking.

## Open questions

1. Which posture does the production deep-capture transcriber persist — `'ok'` (per the
   `ReelDeepCaptureResult` contract) or `'transcribed'` (per `audio_asr`)? (Drives F1 closure.)
2. Is `source_key` (F2) intended as a future alternate key, or leftover? If intended, which producer
   will write it?
3. Is the `extraction_feed_eligible=False` path (F3) retained deliberately for a future non-feed
   source kind, or should the dead reason/branches be removed?

## Residual risk

- F1 dominates: the safety of the headline production path currently rides on a defensive accept-both
  that only one test layer half-covers, atop an unreconciled posture vocabulary.
- Enumeration-time FS errors (F4) can abort a run on a local lake; low probability, pre-existing.
- Both discovery passes scan the full `derived/` tree per run/poll (`_iter_derived_lane_records`); a
  scaling cost, not a correctness issue, and explicitly outside this transcript-feed-parity scope.

## Review-use boundary

These findings are decision input only. They are **not** approval, validation, readiness, mandatory
remediation, or executor-ready patch authority until separately accepted or authorized. `critical`/
`major`/`minor` are priority labels, not gate states.

```yaml
review_courier:
  output_mode: filesystem-output
  report_path: docs/review-outputs/ig_deep_capture_transcript_extraction_advisory_code_review_v0.md
  commission: adversarial implementation/code review of IG deep-capture transcript extraction patch
  target_branch: codex/ig-deep-capture-transcript-extraction
  target_commit: e5a5765408461ba42fa7b3eef850b9ef953497f6
  target:
    - orca-harness/cleaning/transcript_product_extractor.py
    - orca-harness/cleaning/transcript_product_lake.py
    - orca-harness/runners/run_ig_reels_product_extract.py
    - orca-harness/source_capture/ig_reels_behavioral_lake.py
    - orca-harness/source_capture/ig_reels_behavioral_projection.py
    - orca-harness/tests/unit/test_ig_reels_behavioral_lake.py
    - orca-harness/tests/unit/test_ig_reels_behavioral_projection.py
    - orca-harness/tests/unit/test_ig_reels_product_extract.py
    - orca-harness/tests/unit/test_transcript_product_lake.py
  authority: advisory implementation/code review; formal review verdict NOT_CLAIMED
  decision_criteria: deep-capture transcript feed completeness, exact source identity, idempotence, projection failure visibility, boundary hygiene, offline test adequacy
  evidence_summary: >
    No blocker. Core capability correct on the reviewed scope and verified against the lake
    record-id/shard contract: deep-capture transcripts are discovered with a consistent
    record_id (no key-mismatch silent skip), filtered to completed/transcribed/cued shape,
    exact-source-keyed (content-addressed deepcap id in the digest, no false dedup),
    extracted once (idempotent skip-if-done), correlated into the projection by exact key,
    and they block a clean `complete` until the exact-key extraction exists. Backward compat
    holds (no key -> pre-patch digest); no-LLM boundary preserved; 103 focused/contract/shared
    tests reproduced green (no YT regression). One major review-confidence finding: the
    deep-capture success posture is ambiguous in-tree ('ok' per ReelDeepCaptureResult vs
    'transcribed' per audio_asr); the runner safely accepts both but the runner-grain test
    covers only 'transcribed', so a single-token narrowing would silently skip real
    transcripts uncaught. Four minors: vestigial `source_key` alternate-key reads; dead
    `NON_ELIGIBLE_RESIDUAL_REASONS`/`deep_capture_not_in_extraction_feed`; enumeration not
    failure-isolated vs the "never aborts" docstring; no golden-id pin for no-key backward compat.
  reviewed_by: Anthropic Claude Opus 4.8 (claude-opus-4-8)
  authored_by: OpenAI/Codex GPT-5
  de_correlation_bar: cross_vendor_discovery
  same_vendor_rationale: not_applicable
  validation_run: reviewer_reran_focused_48_passed__contract_1_passed__shared_yt_54_passed
  finding_ids: [F1, F2, F3, F4, F5]
  minimum_closure_conditions:
    F1: pin the production deep-capture success posture to one source of truth AND add runner-grain coverage for it
    F2: a producer writes `source_key`, or the `source_key` reads are removed/documented as reserved
    F3: remove the dead reason/branches, or document the retained `extraction_feed_eligible=False` extensibility seam
    F4: isolate enumeration errors, or narrow the "never aborts" docstring scope
    F5: pin the no-source-key mentions_record_id to a golden/equivalence assertion
  next_authorized_action: home model adjudicates findings before keeping or landing the branch
  non_claims:
    - not approval
    - not validation
    - not readiness
    - not patch authority
    - not live capture execution
    - not a no-new-seam / survives-adversarial-review claim
    - not a runtime model recommendation
```
