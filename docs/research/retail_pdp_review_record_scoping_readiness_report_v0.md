# Retail PDP Review Record Scoping Readiness Report v0

```yaml
retrieval_header_version: 1
artifact_role: Capture-lane scoping-readiness report
scope: >
  Decides whether a retail_pdp individual review_record adapter can move to
  implementation scoping by resolving or sharply routing three blockers:
  Attachment Record writer/storage binding, Sephora native Bazaarvoice review ID
  mapping, and Ulta PowerReviews DOM ID semantics. Non-authorizing decision input.
use_when:
  - Deciding whether the retail_pdp review_record adapter is ready for implementation scoping.
  - Routing the Attachment Record blocker and the Sephora/Ulta native-ID risks to their owning lanes.
  - Checking which bounded verification runs or upstream decisions must precede adapter code.
authority_boundary: retrieval_only
open_next:
  - docs/research/retail_pdp_review_record_capture_recon_v0.md
  - orca/product/spines/data_lake/authority/core_spine_v0_data_lake_attachment_record_implementation_contract_v0.md
  - orca/product/spines/capture/source_families/retail_pdp/retail_pdp_projection_contract_v0.md
input_hashes:
  docs/research/retail_pdp_review_record_capture_recon_v0.md: 692aa51bfb42df57017c71c8bd1497805c7cbaa9b75db1683220b8777c33a057
branch_or_commit: codex/retail-pdp-review-recon @ a9dadb90650c9855e93c21a0ffa24ce48b931788
stale_if:
  - The retail PDP review_record recon (input hash above) is superseded or re-patched.
  - The Attachment Record writer/storage physicalization seam is bound, implemented, or changed.
  - A bounded run verifies Sephora Bazaarvoice display-API or Ulta PowerReviews read-API native review IDs (resolves the selector blocker).
  - Sephora or Ulta review DOM/API substrate is rerun or materially changes.
```

## 1. Status and Non-Authorizing Boundary

- Status: `SCOPING_READINESS_ASSESSED`.
- Primary recommendation label: **`PARTIAL_READY_ATTACHMENT_BLOCKED`**.
- Secondary label: **`BLOCKED_SELECTOR_ID_VERIFICATION`** (review-identity key only; the
  descriptive review fields are source-visible).
- Compound form: `SELECTORS_PARTIAL__ATTACHMENT_BLOCKED__ID_VERIFICATION_REQUIRED`.

This report is a decision input only. It is **not** implementation authorization,
runtime authorization, source-access boundary amendment, Attachment Record
architecture acceptance, validation, readiness, product proof, fixture
admission, ECR/Cleaning/Judgment, production storage, scheduler work, or PR/merge
authority. `GO`/`PARTIAL`/`READY` language anywhere below describes
source-access and scoping posture, never build authorization.

## 2. Source Readiness and Missing Sources

`SOURCE_CONTEXT_READY` for the scoping-readiness decision, with the material
gaps disclosed below.

Read and reasoned-from directly on this branch (`codex/retail-pdp-review-recon`
@ `a9dadb90`):

- `docs/research/retail_pdp_review_record_capture_recon_v0.md` (the recon; the
  patched/adjudicated version, hash `692aa51b…`).
- `docs/review-outputs/adversarial-artifact-reviews/retail_pdp_review_record_capture_recon_delegated_adversarial_review_v0.md`
  (cross-vendor review that validated the recon's accuracy and bounded the three blockers).
- `orca/product/spines/data_lake/authority/core_spine_v0_data_lake_attachment_record_implementation_contract_v0.md`
  (controlling source for blocker 1).
- Overlay governance: `README.md`, `decision-routing.md`, `retrieval-metadata.md`,
  `validation-gates.md`, `artifact-folders.md`, `source-of-truth.md`.

Confirmed at primary source (not relied on as secondary report):

- `orca-harness/source_capture/retail_pdp_projection.py` exposes exactly five
  aggregate row kinds (`retail_pdp_product`, `retail_variant_offer`,
  `retail_review_substrate`, `retail_embedded_structured_json`,
  `retail_carried_module`; lines 66-70, 300-445) and **no** `review_record` row
  kind or Attachment Record writer.
- `orca-harness/source_capture/models.py` `PreservedFile` (line 108) carries
  `relative_packet_path`, `sha256`, and a validator-bound `hash_basis`
  restricted to `raw_stored_bytes` (lines 57-66, 116-124) = sha256 over the
  complete unmodified stored bytes at the packet-relative path.

Material gaps (do not block the decision, but bound its strict-claim ceiling):

- **Local-scratch packet evidence.** All Sephora/Ulta per-review findings below
  come from `orca-harness/_test_runs/retail_pdp_review_recon_20260620/`, which is
  gitignored and untracked. These are reported local evidence, **not**
  repo-reproducible fixtures, and cannot clear a strict readiness gate.
- **Storage/core lake contracts read via the implementation contract's summary.**
  The Attachment Record *implementation* contract is the most specific blocker-1
  source and was read in full; its faithful "Current Source Evidence" summary of
  `core_spine_v0_data_lake_storage_contract_v0.md` and `…core_contract_v0.md` was
  relied on rather than re-reading those two directly. The adversarial review
  independently verified that contract chain (its Source-Read Ledger).
- **`review_record` source-family definition is branch-only.** The commission
  prompt and the review-capture spec that define `review_record` field semantics
  live only in the `.claude/worktrees/distracted-ishizaka-01eff5` worktree (recon
  finding AR-01); they are not on this branch or `origin/main`. The body shape
  below is therefore scoped from **raw source-visible fields only**, which is
  exactly what the Attachment Record contract requires regardless.

## 3. Cynefin Routing Result

```text
Smallest complete outcome: A non-authorizing readiness report that tells the
  owner/next CA whether retail_pdp review_record adapter implementation scoping
  can start, and if not, exactly which blocker remains and who owns it.
Regime: Mixed (Complicated + Complex).
Why: Blocker 1 and the source-map are reasoned from current contracts/code
  (Complicated); the Sephora/Ulta native-ID identity is Complex — a live API
  probe could change the route and cannot be settled from the captured packets.
Decomposition: Split and classify — reason the attachment binding and source-map
  from sources; risk-first probe the two ID-identity unknowns.
Current bottleneck: Two distinct gates — (a) the Attachment Record physical
  writer/layout seam is unbound (Data Lake physicalization lane), and (b) the
  native review-ID identity for Sephora non-image rows and Ulta is unverified.
Riskiest assumption: That the Ulta `pr-rd-review-headline-<N>` numeric suffix and
  a per-row Sephora native ID are bindable as native review IDs — unconfirmed.
Stop or pivot condition: If a bounded read-API probe shows the DOM/photo IDs do
  NOT map to native review IDs, the adapter identity key must be redesigned, not
  bound to those tokens.
Allowed next move: Write this report; recommend the two bounded ID-verification
  runs; name the Data Lake physicalization decision; optionally scope a read-only
  source-map design that marks the identity field as candidate/residual.
Disallowed next move: Start adapter implementation; run live capture without
  explicit owner authorization; bind code to the unverified DOM/photo IDs as
  native; or select an Attachment Record physical backend/layout.
```

## 4. ELI5 Summary of the Three Blockers

- **Writing a review durably (Attachment Record).** We know the *shape* a stored
  review record must take (a small keyed index entry pointing to an immutable,
  hash-checked body). We have *not* yet decided exactly *how/where* those bytes
  get written — that physical decision belongs to the Data Lake lane, and no
  writer exists in the harness today. So we can design the adapter's fields, but
  we cannot finish a durable write path yet.
- **Sephora: which ID belongs to each review.** The captured page only carries
  native Bazaarvoice review IDs for reviews that have **photos** (in an embedded
  blob). The plain visible review rows have no ID attached. We need one small,
  legal API check to get a per-review ID for the non-photo rows.
- **Ulta: are those numbers real review IDs?** The page shows numbers like
  `pr-rd-review-headline-580013849`. They *look* like native IDs (big, spread
  out), but nothing else in the page confirms it, and the structured JSON has no
  review ID at all. One small read-API check would confirm or deny it.

## 5. Attachment Record Binding Analysis (Blocker 1)

**Does the contract bind enough to scope a `review_record` writer?** Partly. The
implementation contract
(`…attachment_record_implementation_contract_v0.md`, status
`BLOCKER_1_IMPLEMENTATION_CONTRACT_RECORDED_V0`) binds the **Required Shape** —
enough to scope the adapter's *body field shape and keying* — but explicitly
**defers** the physical writer seam. So adapter source-map and candidate-body
scoping can proceed; a durable `review_record` write path cannot be scoped to
completion until the Data Lake physicalization lane binds the seam.

**Smallest acceptable Attachment Record shape for retail PDP `review_record`
bodies (raw source-visible fields only):** an immutable, hash-checkable body
carrying the per-review raw source-visible payload (reviewer display label,
rating/stars, title, review text, submission/timestamp, variant attributes,
verified-purchase flag, incentive/recommendation flags, helpful counts, media
presence, and the native-or-candidate review ID) — with **no** normalized,
cleaned, deduped, or judged values. Absent or unverified fields are marked as
per-field residuals, not invented (contract Required Shape items 2-3, 7; recon
"Recommended Minimal Next Scope" items 2-3).

**Required keys in the compact manifest/index entry** (contract Required Shape
item 1): `packet_id`, `slice_id` (when applicable), a packet-scoped
attachment/file key (when needed), source family, payload kind, payload schema
version, replay/version pins, attachment reference, `hash`, `hash_basis`, and an
absence/refusal/residual posture summary.

**What must be hash-checkable, immutable, and packet-relative:** the attachment
body must be immutable and verifiable from the entry under the recorded
`hash_basis` (contract item 3). The current `PreservedFile` discipline is the
viable evidence pattern — packet-relative path + `sha256` + `hash_basis =
raw_stored_bytes` (models.py:57-66, 108-124) — but is evidence of viable
discipline, **not** the final Attachment Record schema.

**Decisions owned by the Data Lake / Attachment Record lane (not the retail_pdp
adapter lane)** — all deferred by the contract:

- exact packet-member vs sidecar vs equivalent body layout;
- exact manifest/index serialization (and any Manifest v2 mechanics);
- physical backend (database, object store, warehouse, lakehouse, queue);
- migration/replay plan for incumbent direct fields;
- the writer seam itself and Availability-Index rebuild mechanics;
- lawful-erasure / retention / WORM mechanics.

The adapter lane owns: per-retailer source mapping, raw-field extraction, residual
marking, and producing **candidate** review bodies that conform to the Required
Shape — strictly packet-local (consume preserved bytes + projection context only;
no fetch, paginate, dedupe, score, identify actors, or downstream calls).

Per the contract's Rejected Shapes, the adapter must not push payload bodies into
new lake-core fields, create un-keyed loose sidecars, or make a mutable DB row
the canonical body. No physical backend/layout may be selected in scoping.

## 6. Sephora ID Mapping Analysis (Blocker 2)

Packet: `sephora_pdp_review_recon_01` (lip-sleeping-mask P420652), **local-scratch**.

- **Where the native ID is:** native Bazaarvoice review IDs appear **only** inside
  the embedded `<script id="linkStore" type="text/json" data-comp="PageJSON">`
  blob, in its `reviewImages[]` array as `{reviewId, photoId, thumbnailImageUrl}`
  tuples (e.g. `"reviewId":"393913515"`, `"reviewId":"393764708"`). 100
  `reviewId` occurrences / ~76 unique — all photo-bearing.
- **Coverage = media rows only (in this packet).** The six rendered review-row
  containers (`data-comp="Review Review BaseComponent"`) carry **no** `id`,
  `data-review-id`, or BV token. Direct grep of the full 2.3 MB DOM confirms
  `"Results": 0`, no BV review-object keys (`UserNickname`/`ReviewText`/`Rating`),
  and `"reviewImages": 1` — i.e. the captured page contains the photo substrate
  but **not** a full per-review list with IDs.
- **Selector a future adapter would use:** descriptive fields are extractable
  per-row from the rendered DOM; the per-review native ID is available only via
  the photo substrate (photo rows) or, for all rows, the Bazaarvoice display API
  (config + token are present in the PageJSON blob).
- **Still unverified:** whether the Bazaarvoice display API returns a per-review
  `Id` for non-photo rows (it almost certainly does, but this is not in the
  captured packet).
- **Smallest bounded verification:** with owner authorization, issue one read of
  the Bazaarvoice display API for product `P420652` (the `api.bazaarvoice.com`
  v5.4 endpoint whose config is in the PageJSON blob) and confirm `Results[].Id`
  is present for each review. This resolves non-image-row ID coverage.

Net: the recon's `GO_WITH_NATIVE_ID_MAPPING_RISK` holds and is sharpened —
photo-row IDs are in-packet; **non-image-row native IDs are not present in the
captured evidence** and require one bounded API read.

## 7. Ulta ID Semantics Analysis (Blocker 3)

Packet: `ulta_pdp_review_recon_01` (night-shift-overnight-lip-mask, sku 2645443),
**local-scratch**.

- **The DOM numeric IDs:** five unique `id="pr-rd-review-headline-<N>"` tokens —
  `575373729, 576140820, 578859756, 579948269, 580013849`. The values are
  **sparse/large** (gaps up to ~2.7M), the signature of external-system native
  IDs rather than sequential UI ordinals.
- **No corroboration in-packet:** each number appears **only** as the headline
  element `id`, its `data-testid="headline-<N>"`, and `aria-describedby` — never
  in an href/permalink, a `review_id`/`ugc_id` field, Apollo state, or the
  projection JSON. So the "native ID" read is suggestive but unconfirmed.
- **JSON-LD cannot key identity:** the 5 schema.org `Review` objects carry
  `name`, `datePublished`, `author.name`, `locationCreated`, `reviewRating` — and
  **no** `@id`, `url`, `identifier`, or `reviewId`. The only quasi-key
  (`datePublished + author.name + name`) is not collision-resistant. An adapter
  cannot reliably key per-review identity off JSON-LD.
- **Verdict:** `unresolved_candidate` (moderate-high confidence it is native,
  unconfirmed). The DOM numeric suffix is the **only** per-review identity token
  available; binding code to it without confirmation is the risk.
- **Smallest bounded verification:** with owner authorization, issue one read of
  the PowerReviews read API for the product
  (`readservices-b2c.powerreviews.com/m/6406/l/en_US/product/pimprod2046225/reviews`;
  merchant/page IDs extracted from the DOM) and compare returned `review_id`/`id`
  values against the five DOM suffixes. Match ⇒ native; mismatch/absence ⇒ UI id.

Net: the recon's `GO_WITH_ID_SEMANTICS_RISK` holds and is sharpened — bind to the
DOM numeric suffix only after one read-API confirmation; JSON-LD is not a fallback
identity source.

## 8. Amazon Partial-Scope Note (Blocker 4 / scope boundary)

From the recon Field Verdicts (packet `amazon_pdp_control_01`, local-scratch) and
the access probes:

- **PDP-embedded top reviews remain usable.** Per-review blocks expose
  `data-reviewid` (a native-looking per-row ID — the most directly attached of the
  three retailers), plus reviewer name, rating, title, date, variant, verified
  badge, and text.
- **All-review pagination remains blocked** under the tested no-gate-defeat routes
  (rendered + direct-HTTP both hit continue-shopping/`opfcaptcha` interstitials).
  Do not claim a full Amazon corpus path under this boundary.
- **Recommendation:** include Amazon only as a **partial source — PDP top reviews
  only** in first scoping; hold full-corpus pagination as blocked. Amazon's
  identity risk is the lowest (ID is attached per row), but its corpus is the
  smallest; Sephora/Ulta offer fuller row coverage pending one ID probe each.

## 9. Recommendation Label

**Primary: `PARTIAL_READY_ATTACHMENT_BLOCKED`** — the source side (per-retailer
descriptive-field source-map + the Required-Shape body) is bounded enough to
scope, but the durable write path is blocked because the Attachment Record
physical writer/layout seam is an unbound Data Lake-lane decision.

**Secondary: `BLOCKED_SELECTOR_ID_VERIFICATION`** — the review-**identity** key is
unverified for Sephora non-image rows and for Ulta; each needs one bounded read-API
confirmation before code treats those tokens as native review IDs.

Ruled out: `READY_FOR_IMPLEMENTATION_SCOPING` (write seam + identity unresolved);
`BLOCKED_NEEDS_DATA_LAKE_BINDING_DECISION` as *primary* (the contract already binds
the Required Shape — what is missing is physicalization, not the binding, so the
adapter source-map can still be scoped); `RUN_REQUIRED_NO_AUTHORITY` as the whole
verdict (only the identity sub-question needs a run); `NO_GO_RECON_STALE` (the
recon is the current, adjudicated, hash-stable `692aa51b…` version).

## 10. Minimal Implementation-Scoping Surface and Exact Next Blockers

**Can be scoped now (read-only, no authorization needed)** — a selector-level
source-map design that:

1. Locks per-retailer descriptive-field selectors: Amazon PDP top-review blocks,
   Sephora rendered review rows, Ulta JSON-LD + PowerReviews rows.
2. Defines the `review_record` candidate body against the Attachment Record
   Required Shape, keyed by `packet_id`/`slice_id`/retailer/product-or-SKU/source
   URL and **native-or-candidate** review ID, raw source-visible fields only.
3. Marks the review-identity field as `candidate` (Ulta DOM suffix; Sephora
   non-photo rows) until a verification run promotes it, and marks absent fields
   as per-field residuals.
4. Keeps the extractor strictly packet-local.

**Exact remaining blockers before full adapter implementation scoping is `READY`:**

- **B1 (upstream lane/owner):** Data Lake physicalization lane binds the
  Attachment Record writer seam (layout/serialization/backend) per the contract's
  Deferred Decisions. Until then, only candidate bodies, not durable records.
- **B2 (bounded run, owner-authorized):** Sephora Bazaarvoice display-API read
  confirming per-review `Id` for non-photo rows.
- **B3 (bounded run, owner-authorized):** Ulta PowerReviews read-API read
  confirming the `pr-rd-review-headline-<N>` suffix equals the native `review_id`.

## 11. Evidence Table

| Claim | Tier | Source |
| --- | --- | --- |
| No `review_record` row kind / Attachment Record writer exists in the harness | repo-verifiable | `orca-harness/source_capture/retail_pdp_projection.py:66-70,300-445` |
| Attachment Record Required-Shape keys + immutable hash-checkable body; layout/backend/writer seam deferred | repo-verifiable | `…attachment_record_implementation_contract_v0.md` (Required Shape; Deferred Decisions) |
| `PreservedFile` hash discipline = packet-relative path + sha256 + `hash_basis=raw_stored_bytes` | repo-verifiable | `orca-harness/source_capture/models.py:57-66,108-124` |
| Recon is current, adjudicated, hash-stable | repo-verifiable | `git show HEAD:…recon_v0.md` sha256 `692aa51b…`; HEAD `a9dadb90` |
| Sephora native BV IDs present for photo rows only (`reviewImages[]`); no full per-review list / `Results` in captured DOM | local-scratch | `sephora_pdp_review_recon_01` DOM (`"reviewId"`×100, `"reviewImages"`×1, `"Results"`×0) |
| Sephora rendered review-row containers carry no ID attribute | local-scratch | `sephora_pdp_review_recon_01` DOM (`data-comp="Review Review BaseComponent"`, no `id`/`data-review-id`) |
| Ulta DOM `pr-rd-review-headline-<N>` IDs are sparse/large; absent elsewhere in packet | local-scratch | `ulta_pdp_review_recon_01` DOM (5 unique tokens; no href/`review_id`/Apollo match) |
| Ulta JSON-LD `Review` objects carry no `@id`/`url`/`identifier`/`reviewId` | local-scratch | `ulta_pdp_review_recon_01` DOM `ld+json[1]` (5 Review objects) |
| Amazon PDP top reviews expose `data-reviewid`; all-review pagination blocked | local-scratch | recon Field Verdicts; packets `amazon_pdp_control_01`, `amazon_review_page_*` |
| Sephora non-image-row native ID coverage | unverified | needs Bazaarvoice display-API read for P420652 (`Results[].Id`) |
| Ulta DOM numeric suffix == native `review_id` | unverified | needs PowerReviews read-API read for `pimprod2046225` |

## 12. Owner Decisions Needed

1. **Authorize (or decline) the two bounded ID-verification reads** (B2, B3
   above). They are single read-only API GETs, no auth/proxy/CAPTCHA/gate-defeat,
   but they are live network and therefore require explicit per-run owner
   authorization. Without them, the identity key stays `candidate`.
2. **Sequence the Data Lake physicalization lane** (B1) that binds the Attachment
   Record writer seam — a separate Data Lake-lane decision, not the adapter lane's.
3. **Confirm first-scope retailer set** — recommended: scope all three
   source-maps; treat Amazon as PDP-top-reviews-only; do not commit a durable
   write path for any retailer until B1 lands.
4. **Optional hygiene:** register this report in `docs/workflows/orca_repo_map_v0.md`
   to satisfy the forward-only retrieval-header CI orphan gate. Left undone here
   because this commission's edit permission was scoped to the report file only.

## 13. Required Follow-up Prompt / Report / Run

- **If owner authorizes B2/B3:** a single bounded verification-run prompt that
  reads the two read-APIs and writes a short evidence note promoting or demoting
  the identity key per retailer (commit the returned IDs as committed provenance,
  resolving the recon AR-02 local-scratch durability gap for identity).
- **In parallel/independently:** a Data Lake physicalization scoping/decision
  prompt for the Attachment Record writer seam (B1).
- **After B1 + (B2/B3):** an `workflow-implementation-scoping` pass producing the
  `STEP-*` route for the retail_pdp `review_record` adapter. Not before.
- **No run is authorized by this report.** A read-only source-map design patch
  (Section 10) may proceed without a run if the owner prefers to advance scoping
  before the probes.

## 14. Non-Claims

This report is not implementation authorization, runtime authorization,
source-access boundary amendment, Attachment Record architecture acceptance,
validation, readiness, product proof, commercial authorization, fixture
admission, ECR, Cleaning, Judgment, production storage, scheduler work, or PR
merge authority. Local-scratch packet evidence is reported, not repo-reproducible,
and does not clear a strict gate. Verdict tokens describe source-access and
scoping posture only. The two bounded verification runs are recommendations, not
execution authority.
```
