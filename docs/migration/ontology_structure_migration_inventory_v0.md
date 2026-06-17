# Ontology Structure Migration Inventory v0

```yaml
retrieval_header_version: 1
artifact_role: migration inventory
scope: >
  Docs-only inventory for future migration of ontology-related Orca artifacts
  into a spine-first structure. This pass classifies artifacts, names
  consumers, recommends a future ontology home, and does not move files.
authority_boundary: retrieval_only
use_when:
  - Planning the future physical home for Orca ontology artifacts.
  - Checking whether ontology should be treated as a shared substrate, registry, or spine.
  - Preparing a later move pass that must preserve current source authority and consumer boundaries.
open_next:
  - Decide the accepted spine-first root shape before moving any ontology artifact.
  - Reconcile this inventory with any landed Foundation rename before applying path moves.
stale_if:
  - docs/product/core_spine/orca_ontology_backbone_architecture_v0.md moves or is superseded.
  - A new ontology conductor, run lifecycle, or registry/resolver is accepted.
  - repo-structure.yaml changes the bound product lane structure.
```

## 1. Start-State Receipt

This lane was opened from `main` for docs-only migration marking. The original
root worktree was not edited because it had unrelated untracked files:
`.codex/hooks/run_orca_guard.py`, `_scratch/`, and `orca-worktrees/`. A fresh
worktree was created at:

`C:/Users/vmon7/Desktop/projects/orca/.codex/worktrees/ontology-structure-migration-inventory`

Start branch and base:

| Item | Observed value |
| --- | --- |
| Working branch | `codex/ontology-structure-migration-inventory` |
| Base branch | `main` |
| Start HEAD | `b139fa9f` |
| Start dirty state in lane | Clean |
| Root worktree unrelated state | Left untouched |

The preflight sources read for this inventory were:

- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/decision-routing.md`
- `.agents/workflow-overlay/artifact-folders.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/retrieval-metadata.md`
- `repo-structure.yaml`
- `docs/STRUCTURE.md`
- `docs/workflows/orca_repo_map_v0.md`
- current and pending structure records reachable from local branches

The current binding on `main` is still `docs/` plus `orca-harness/`. Current
`repo-structure.yaml` still names `docs/product/core_spine/` as the bound
foundation-like lane; the pending `codex/foundation-rename` branch renames that
lane to `docs/product/foundation/`. That pending rename moves ontology files as
inherited Core Spine contents; it does not prove Foundation should own ontology.

Pending structure branches observed before editing included:
`codex/commission-spine-structure`, `codex/foundation-rename`,
`codex/ecr-spine-first-migration-inventory`, `ontology-commission-refresh`,
and `origin/ontology-cards-graph-closers-v0`. Local branch records on
`codex/commission-spine-structure` include a spine-first / Commission Signal
Board migration plan and state that GitHub PR `#239` was open for that lane.
This inventory did not freshly verify that PR through GitHub because local
`gh auth status` reported an invalid keyring token.

Required searches run:

```powershell
rg --files | rg -i "ontology|backbone|venue_card|card_set|vertical_exploration|taxonomy|registry"
rg -n -i "ontology|ontology backbone|card set|venue card|vertical exploration|taxonomy|registry|entity|decision object|evidence object" docs .agents orca-harness --glob "!_scratch/**" --glob "!orca-worktrees/**"
```

The broad text search produced expected noise from raw inbox/source bundles and
runtime words such as `entity` and `registry`. This inventory excludes
`docs/_inbox/`, generated caches, copied source bundles, and old worktrees
unless they are needed as provenance examples.

No files were moved in this pass.

## 2. Ontology Scope Definition

For this migration inventory, "ontology" means Orca's governed shared naming,
relationship, and stable-ID grammar for product objects. The current load-bearing
source is `docs/product/core_spine/orca_ontology_backbone_architecture_v0.md`.
That source describes a shared semantic backbone, not a product feature, runtime
schema, validation result, registry service, or spine conductor.

In scope:

- the ontology architecture artifact;
- ontology object-card conventions and object-card examples;
- the ontology expansion backlog;
- ontology-specific commission, review, and review-output provenance;
- direct inputs that ontology consumes or points to, when needed as pointers;
- code or runtime artifacts only as pointer targets, not move candidates.

Out of scope for physical ontology migration:

- ECR/SCR mechanics and evidence registries, which may consume ontology terms
  but own derived-record mechanics separately;
- Judgment evaluation artifacts, which may consume ontology terms but own
  evaluation and gates;
- Capture/source-capture runtime code, which may back CapturePacket and
  EvidenceUnit objects but must not move in this docs-only pass;
- vertical venue/card sets, which can be ontology examples or consumers without
  becoming ontology authority;
- historical review outputs as current authority.

## 3. Artifact Inventory Table

Migration marks use only these values: `move_now`, `move_later`,
`pointer_only`, `do_not_move`, and `historical_only`.

| Current path | Artifact role | Owner / consumer | Future target path | Migration mark | Reason | Dependencies | Validation needed after move |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `docs/product/core_spine/orca_ontology_backbone_architecture_v0.md` | Ontology architecture and naming/relationship/ID-grammar authority | Shared ontology; consumers: Foundation, Judgment, ECR/SCR, Capture, Search, Product Lead, vertical satellites | `orca/product/shared/ontology/authority/orca_ontology_backbone_architecture_v0.md` | `move_later` | Current evidence frames ontology as a shared semantic backbone consumed across lanes. It is not proven to be a spine. | Demand taxonomy, buyer-proof sources, judgment ladder/gate map, source-truth overlay, artifact-folder rules, venue/card provenance | Retrieval header, repo map, placement check, moved-path index, reference rewrite, and no stale `core_spine` or `foundation` pointers |
| `docs/product/core_spine/ontology_cards/README.md` | Object-card convention and non-authority guardrails | Shared ontology; card authors and consumers | `orca/product/shared/ontology/cards/README.md` | `move_later` | The card convention belongs with ontology, but cards remain instance hints and not validation or registry authority. | Ontology architecture, card files | Retrieval header, card path references, moved-path index |
| `docs/product/core_spine/ontology_cards/brand_beautypie_v0.md` | Brand instance hint | Shared ontology; vertical satellites, Product Lead, Judgment | `orca/product/shared/ontology/cards/brand_beautypie_v0.md` | `move_later` | Brand card is an ontology example/hint and should move with the card set if ontology moves. | Architecture object roster, candidate-pool source, buyer/org reservation | Retrieval header, source pointer integrity, no claim escalation |
| `docs/product/core_spine/ontology_cards/case_beautypie_repricing_2023_v0.md` | Case instance hint | Shared ontology; Judgment, Product Lead, vertical satellites | `orca/product/shared/ontology/cards/case_beautypie_repricing_2023_v0.md` | `move_later` | Case is a shared object name consumed by Judgment but not owned by Judgment. | `orca-harness/cases/product_learning/beautypie_repricing_2023_v0/`, judgment ladder, facilitator ledger | Retrieval header, case alias pointers, no runtime movement |
| `docs/product/core_spine/ontology_cards/decision_beautypie_repricing_2023_v0.md` | DecisionEvent instance hint | Shared ontology; Judgment and Product Lead | `orca/product/shared/ontology/cards/decision_beautypie_repricing_2023_v0.md` | `move_later` | DecisionEvent belongs to the ontology object vocabulary, while evaluation remains outside ontology. | Case card, decision/event source pointers | Retrieval header, cross-card links, no readiness claim |
| `docs/product/core_spine/ontology_cards/outcome_beautypie_repricing_2023_v0.md` | Outcome instance hint | Shared ontology; Judgment, Product Lead, vertical satellites | `orca/product/shared/ontology/cards/outcome_beautypie_repricing_2023_v0.md` | `move_later` | Outcome is vocabulary shared across consumers; the card does not grade or validate the case. | Facilitator ledger, batch ledger, judgment claim-tier references | Retrieval header, source pointers, no graded-result claim |
| `docs/product/core_spine/ontology_cards/venue_basenotes_v0.md` | Venue instance hint | Shared ontology; Capture, Search, vertical satellites | `orca/product/shared/ontology/cards/venue_basenotes_v0.md` | `move_later` | Venue is in the object roster; the Basenotes card is an example and not a venue registry. | Beauty venue card set, venue registry rejection decision | Retrieval header, venue-card pointer, no capture/monitoring authorization |
| `docs/product/core_spine/ontology_cards/vertical_beauty_v0.md` | Vertical instance hint | Shared ontology; vertical satellites, Product Lead, Search | `orca/product/shared/ontology/cards/vertical_beauty_v0.md` | `move_later` | Vertical is a shared object; the beauty example should move only with ontology cards, not into a vertical authority folder by default. | Beauty thesis, wedge docs, venue card set | Retrieval header, source pointers, no validation/readiness claim |
| `docs/product/core_spine/ontology_expansion_backlog_v0.json` | Machine-readable deferred-card backlog | Shared ontology; `.agents/hooks/check_ontology_expansion.py` | `orca/product/shared/ontology/backlog/ontology_expansion_backlog_v0.json` | `move_later` | Backlog belongs with ontology, but a later move must update or bridge hook paths. | `check_ontology_expansion.py`, demand scan/core spec trigger, current cards directory | Hook path update or pointer stub, placement check, changed-file validation |
| `docs/prompts/product-planning/orca_ontology_backbone_architecture_pass_commission_prompt_v0.md` | Ontology architecture commission prompt | Prompt/orchestration provenance; shared ontology as subject | `orca/product/shared/ontology/prompts/orca_ontology_backbone_architecture_pass_commission_prompt_v0.md` | `move_later` | The prompt is not ontology authority, but it is source provenance for the current architecture artifact. | Prompt orchestrator rules, architecture doc, review prompt | Retrieval header, prompt path references, historical/provenance label |
| `docs/prompts/reviews/ontology_backbone_architecture_delegated_review_prompt_v0.md` | Review prompt for ontology architecture | Review provenance; shared ontology as subject | `orca/product/shared/ontology/reviews/prompts/ontology_backbone_architecture_delegated_review_prompt_v0.md` | `move_later` | It is live provenance for the architecture review path, but not the authority itself. | Architecture doc, review output | Retrieval header, review-output pointer, no authority escalation |
| `docs/prompts/reviews/ontology_commission_refresh_delegated_review_patch_prompt_v0.md` | Review/patch prompt for commission refresh | Review provenance; prompt orchestration | `orca/product/shared/ontology/reviews/prompts/ontology_commission_refresh_delegated_review_patch_prompt_v0.md` | `historical_only` | It reviews the commission prompt rather than defining ontology; keep only as historical provenance if archives move. | Commission prompt, review output | Historical label, path references |
| `docs/review-outputs/adversarial-artifact-reviews/ontology_backbone_architecture_review_v0.md` | Adversarial review output for architecture | Review provenance; owner/adjudication reader | `orca/product/shared/ontology/reviews/outputs/ontology_backbone_architecture_review_v0.md` | `historical_only` | Useful as review provenance, but not current ontology authority and not adoption proof. | Architecture doc, review prompt | Historical label, no current-authority wording |
| `docs/review-outputs/adversarial-artifact-reviews/ontology_commission_refresh_delegated_review_v0.md` | Adversarial review output for commission refresh | Review provenance; prompt owner | `orca/product/shared/ontology/reviews/outputs/ontology_commission_refresh_delegated_review_v0.md` | `historical_only` | Historical prompt-review output only. | Commission refresh review prompt | Historical label, no current-authority wording |
| `docs/product/search/orca_demand_read_taxonomy_v0.md` | Demand-read taxonomy and read grammar | Search; Product Lead; Judgment; ontology consumes names | `orca/product/spines/search/authority/orca_demand_read_taxonomy_v0.md` | `pointer_only` | Demand taxonomy informs ontology terms such as WindCaller, TrendVector, Call, and Reading, but the taxonomy is not the ontology package. | Search lane, demand read adjudication, scan spec | Ontology pointer update only; do not move with ontology |
| `docs/product/search/orca_demand_read_taxonomy_adjudication_v0.md` | Demand taxonomy adjudication | Search; Product Lead; Judgment | `orca/product/spines/search/adjudications/orca_demand_read_taxonomy_adjudication_v0.md` | `pointer_only` | Adjudication is an input/consumer boundary record, not ontology authority. | Demand taxonomy, owner decisions | Pointer integrity only |
| `docs/product/engagement_logic_registry_v0.md` | Engagement interpretation registry/rubric | Product logic; possible shared vocabulary consumer | `orca/product/shared/ontology/vocabularies/engagement_logic_registry_v0.md` if promoted; otherwise a Foundation/shared rubric home | `move_later` | It is registry-shaped and vocabulary-adjacent, but not yet proven as ontology authority. Move only after reconciling with demand taxonomy and ontology object roster. | Demand taxonomy, Product Lead logic, existing product-lane placement | Decide owner before move; retrieval header; reference rewrite |
| `docs/product/core_spine/beauty_venue_card_set_v0.md` | Bounded beauty venue card set | Vertical satellite / Foundation-like exploration support; ontology consumes Venue examples | Likely vertical or Foundation home after structure decision, not ontology authority | `pointer_only` | Venue cards can seed ontology examples, but the card set is vertical-specific and capped by separate decisions. | Venue registry rejection decision, promotion decision, vertical exploration guide | Ontology pointers only; do not merge with ontology |
| `docs/product/core_spine/orca_vertical_exploration_guide_v0.md` | Manual vertical exploration procedure | Foundation-like exploratory method; Search/Capture/Product Lead consumers | Future Foundation or relevant exploration-method home, not ontology authority | `pointer_only` | Procedure consumes venue provenance and card sets; it does not define ontology. | Beauty venue card set, venue decisions | Pointer integrity only |
| `docs/decisions/orca_venue_registry_rejection_decision_v0.md` | Decision rejecting standing venue registry/atlas | Decision authority for venue registry boundary | Stay in decisions or future decision archive | `pointer_only` | This decision is load-bearing boundary evidence for why ontology should not become a venue registry. | Venue/card set sources | Keep pointer from ontology recommendation |
| `docs/decisions/beauty_venue_card_set_promotion_decision_v0.md` | Decision promoting one bounded beauty venue card set | Decision authority for vertical venue asset | Stay in decisions or future decision archive | `pointer_only` | It governs one vertical card set; it does not create ontology authority. | Beauty venue card set, venue registry rejection decision | Keep pointer from venue-related cards |
| `docs/research/source_registry_practices_deep_research_report_v0.md` | Research report on registry practices | Research input; product/architecture readers | Research archive, not ontology package | `pointer_only` | Useful as anti-rot/registry-design input, but not an Orca ontology artifact. | Venue registry decision, registry/backbone discussions | Pointer only; no authority wording |
| `docs/research/daimler_advisory_001_source_registry_v0.md` | Case/source registry for Daimler advisory rebuild planning | Judgment/research provenance | Judgment/case research home if that lane migrates | `do_not_move` | Evidence/source registries are case provenance, not ontology. | Daimler advisory artifacts | Do not move in ontology pass |
| `docs/research/judgment-spine/harness/v0_14/fixtures/unity_runtime_fee_2023_v0_14/evidence_registry_draft_v0.md` | Draft EvidenceUnit registry | Judgment harness fixture provenance | Judgment/harness fixture home | `do_not_move` | EvidenceUnit may be an ontology object name, but this draft is Judgment fixture provenance. | Judgment v0.14 harness fixture | Do not move in ontology pass |
| `docs/research/judgment-spine/harness/v0_14/fixtures/daimler_corporate_structure_vote_2019_v0_14/evidence_registry_draft_v0.md` | Draft EvidenceUnit registry | Judgment harness fixture provenance | Judgment/harness fixture home | `do_not_move` | Case-specific evidence registry, not ontology. | Judgment v0.14 harness fixture | Do not move in ontology pass |
| `docs/research/judgment-spine/harness/v0_14/fixtures/canoo_walmart_2022_v0_14/evidence_registry_draft_v0.md` | Draft EvidenceUnit registry | Judgment harness fixture provenance | Judgment/harness fixture home | `do_not_move` | Case-specific evidence registry, not ontology. | Judgment v0.14 harness fixture | Do not move in ontology pass |
| `docs/prompts/reviews/daimler_v0_14_source_receipt_evidence_registry_adversarial_artifact_review_prompt_v0.md` | Review prompt for evidence registry artifact | Judgment review provenance | Judgment review archive if moved | `historical_only` | Evidence registry review prompt is not ontology authority. | Daimler evidence registry draft, review output | Historical label only |
| `docs/prompts/reviews/daimler_v0_14_source_receipt_evidence_registry_post_patch_adversarial_artifact_recheck_prompt_v0.md` | Post-patch review prompt for evidence registry | Judgment review provenance | Judgment review archive if moved | `historical_only` | Historical review prompt for Judgment evidence registry. | Daimler evidence registry draft, recheck output | Historical label only |
| `docs/review-outputs/adversarial-artifact-reviews/daimler_v0_14_source_receipt_evidence_registry_adversarial_artifact_review_v0.md` | Review output for evidence registry | Judgment review provenance | Judgment review archive if moved | `historical_only` | Historical review output, not ontology authority. | Evidence registry review prompt | Historical label only |
| `docs/review-outputs/adversarial-artifact-reviews/daimler_v0_14_source_receipt_evidence_registry_post_patch_adversarial_recheck_v0.md` | Post-patch review output for evidence registry | Judgment review provenance | Judgment review archive if moved | `historical_only` | Historical review output, not ontology authority. | Post-patch review prompt | Historical label only |
| `docs/review-outputs/adversarial-artifact-reviews/daimler_advisory_001_source_registry_adversarial_review_v0.md` | Review output for Daimler source registry | Judgment/research review provenance | Judgment review archive if moved | `historical_only` | Historical review output for a case source registry. | Daimler source registry | Historical label only |
| `orca-harness/source_capture/models.py` | Runtime models that may back CapturePacket and source objects | Capture runtime | Code stays in `orca-harness`; future docs may add pointer from Capture | `pointer_only` | Code is not moved in this docs-only pass. | Capture docs, ontology CapturePacket name | Pointer doc only; code tests if ever edited |
| `orca-harness/ecr/**`, `orca-harness/signal_content/**`, `orca-harness/evidence_binding/**`, `orca-harness/cleaning/**` | Runtime derived-record and evidence-binding mechanics | ECR/SCR, Signal Content, Judgment/Capture consumers | Code stays in `orca-harness`; future spine docs may point to it | `do_not_move` | ECR/SCR are derived-record mechanics and must not be merged into ontology. | ECR submap, evidence binding docs, runtime tests | No ontology move; code tests if ever edited |

## 4. Consumer Map

| Consumer | What it consumes from ontology | Boundary |
| --- | --- | --- |
| Foundation | Shared object names, ID grammar, EvidenceUnit/CapturePacket vocabulary, and market-agnostic semantic conventions | Foundation may host mechanics and methods, but current evidence does not make it sole ontology owner. |
| Judgment | Case, DecisionEvent, Outcome, EvidenceUnit, Reading, claim-tier crosswalks, and stable object references | Judgment owns evaluation and gates, not ontology vocabulary authority. |
| ECR/SCR | Stable source/evidence identifiers and object names needed by derived records | ECR/SCR own derived-record mechanics; do not merge them into ontology. |
| Capture | Venue, Observation, CapturePacket, EvidenceUnit, and source-capture object boundaries | Capture owns collection/runtime procedures; ontology does not authorize capture or monitoring. |
| Search | WindCaller, Call, TrendVector, Reading, demand-state grammar, and scan-spec-triggered card expansion | Search owns demand-read/scan behavior; ontology consumes terms and names shared objects. |
| Product Lead | Buyer, Memo, Case, Outcome, ICP/wedge/offer vocabulary, and buyer-proof references | Product Lead consumes shared semantics for product decisions; it does not validate schema readiness. |
| Vertical satellites | Vertical, Brand, Product, Venue, and example cards such as beauty and fragrance assets | Vertical assets can provide examples and provenance, but are not ontology authority by default. |

## 5. Future-Home Recommendation

Recommended future home: `orca/product/shared/ontology/`.

This is the smallest complete recommendation for the evidence currently in the
repo. The ontology architecture describes a repo-wide shared naming,
relationship, and ID-grammar substrate consumed by multiple lanes. It also
explicitly defers registry/resolver/index implementation and treats object
cards as hints rather than live authority. Current evidence therefore supports a
shared ontology package, not an ontology spine.

Candidate evaluation:

| Candidate home | Recommendation | Reason |
| --- | --- | --- |
| `orca/product/shared/ontology/` | Primary recommendation | Fits the pending spine-first shape's shared-package pattern and keeps ontology available to Foundation, Judgment, ECR/SCR, Capture, Search, Product Lead, and vertical satellites. |
| `orca/product/substrates/ontology/` | Semantically acceptable if the accepted root adds `substrates/` | "Substrate" is a precise label for shared naming/ID grammar, but this folder family is not present in the pending spine-first proposal observed by this lane. |
| `orca/product/registries/ontology/` | Do not use as the primary home now | The current ontology source says registry/resolver/index work is deferred and that ontology owns grammar, not live ID minting/resolution. |
| `orca/product/spines/foundation/ontology/` | Do not use as the primary home | Foundation may consume ontology and may temporarily inherit files through the pending rename, but ontology has cross-spine consumers and no source-proven spine lifecycle. |
| `orca/product/spines/ontology/` | Not recommended | No current source shows an ontology conductor, run lifecycle, claims surface, artifacts, or validation gates sufficient to make ontology an operating spine. |

If the accepted root structure later adopts both `shared/` and `substrates/`,
then `orca/product/substrates/ontology/` may be a better final label. Until that
target exists, `orca/product/shared/ontology/` is the lower-lock-in physical
choice.

## 6. Do-Not-Move List

Do not move these in an ontology migration pass:

- `orca-harness/ecr/**`, `orca-harness/signal_content/**`,
  `orca-harness/evidence_binding/**`, and `orca-harness/cleaning/**`.
- Judgment fixture evidence registries under
  `docs/research/judgment-spine/harness/v0_14/fixtures/**`.
- Daimler source/evidence registry review prompts and review outputs as ontology
  authority.
- `docs/product/search/orca_demand_read_taxonomy_v0.md` and its adjudication as
  ontology authority; keep them as Search-owned inputs/pointers.
- `docs/product/core_spine/beauty_venue_card_set_v0.md` as ontology authority.
- `docs/product/core_spine/orca_vertical_exploration_guide_v0.md` as ontology
  authority.
- Raw inbox/source bundles, generated caches, old worktrees, or copied
  review-input source bundles.

Do not merge ontology with ECR/SCR, Judgment, or vertical satellites. Each can
consume ontology while retaining its own authority boundary.

## 7. Migration Sequence

1. Land or reject the pending Foundation rename and spine-first structure work
   before moving ontology paths.
2. Bind the chosen future home explicitly. Recommended binding:
   `orca/product/shared/ontology/`.
3. Move the primary ontology package only after the root structure is accepted:
   architecture, `ontology_cards/`, and `ontology_expansion_backlog_v0.json`.
4. Preserve provenance by moving or pointing to ontology-specific prompts and
   review outputs with clear historical labels.
5. Update hook/path dependencies for `ontology_expansion_backlog_v0.json`, or
   add a temporary pointer/stub if code movement remains out of scope.
6. Add or update pointers from Foundation, Judgment, ECR/SCR, Capture, Search,
   Product Lead, and vertical satellite docs.
7. Rewrite only live references. Historical references can rely on the moved-path
   index when that is the project convention.
8. Run validation for the move pass: `git diff --check`,
   `check_retrieval_header.py --changed`, `check_repo_map_freshness.py
   --changed`, `check_placement.py --check`, and any hook/code tests required
   if paths used by executable hooks are changed.

## 8. Open Questions

- Will the accepted spine-first root include only `shared/`, or will it also add
  `substrates/` as a first-class product folder?
- If a future ontology registry/resolver is built, should it live under ontology
  as a subpackage or under a separate `registries/` family?
- If `codex/foundation-rename` lands first, should ontology move from
  `docs/product/foundation/` directly to `orca/product/shared/ontology/`, or
  should Foundation keep only a pointer after the shared home exists?
- Does `docs/product/engagement_logic_registry_v0.md` become ontology-controlled
  vocabulary, a Foundation rubric, or a Product Lead/Search-owned artifact?
- Which deferred object cards should be triggered by the accepted demand scan
  spec, and should the hook path change before or during the physical move?
- Should historical ontology prompts/reviews be co-located under
  `shared/ontology/` or remain in global prompt/review archives with pointers?

## 9. Non-Claims

This inventory is not validation, readiness, product proof, schema ratification,
runtime authorization, permission to move files, permission to build a registry,
or permission to treat ontology as a spine.

It does not claim that `orca/product/shared/ontology/` exists today. It only
marks it as the recommended future target under the observed spine-first
direction.

It does not claim that the pending Foundation rename or Commission Signal Board
structure branches have landed on `main`.

It does not claim that historical review outputs are current authority.

It does not authorize moving executable code.
