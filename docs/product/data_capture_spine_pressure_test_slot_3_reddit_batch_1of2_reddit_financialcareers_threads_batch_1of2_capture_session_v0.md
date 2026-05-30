# Capture: non_target_us_domestic_resume_driven_interview_getting_pain / reddit_financialcareers_threads_batch_1of2 / 2026-05-31

## Decision Frame
- Decision question: For the five owner-supplied `r/FinancialCareers` thread JSON slices in this sub-batch, what raw observable discourse is present around non-target / resume-driven interview-getting pain, without blending threads or deciding downstream use?
- Owner or owner-context: Slot 3 Reddit sub-batch 1of2 under the authorized Data Capture pressure-test batch; downstream owner-context remains the owner-pinned `non_target_us_domestic_resume_driven_interview_getting_pain` frame.
- Consequence: If thread hierarchy, modality limits, deleted rows, or mutable-thread posture are flattened, downstream layers will misread how the pain was expressed and what context was actually visible at capture.
- Allowed decision verbs (if relevant): not_supplied
- Cutoff posture: Use each supplied local raw JSON file state as the source cutoff for its thread. No live continuation, archive, or cross-venue fetches were performed in this session.
- Downstream-use intent: Bounded categorical capture handoff posture for these five Reddit slices only. No Cleaning, Judgment, or ECR schema design is performed here.

## Source Boundary
- Source surfaces in scope:
  - `R01` `reddit_t3_1tmu6ft.json` -> `/r/FinancialCareers/comments/1tmu6ft/200_applications_no_job/`
  - `R02` `reddit_t3_1r38dch.json` -> `/r/FinancialCareers/comments/1r38dch/i_wish_i_could_kick_the_shit_out_of_my_15_yearold/`
  - `R03` `reddit_t3_1tj8f96.json` -> `/r/FinancialCareers/comments/1tj8f96/is_it_worth_giving_up_a_target_school_to_go_to_a/`
  - `R04` `reddit_t3_1qw3ufa.json` -> `/r/FinancialCareers/comments/1qw3ufa/junior_year_at_nontarget_and_no_internshipswork/`
  - `R05` `reddit_t3_1p6hhbb.json` -> `/r/FinancialCareers/comments/1p6hhbb/nontarget_working_in_a_bb_in_riskdreaming_the_fo/`
- Boundary compliance (discoverable-or-entitled / free or account-created / disclosable / no obvious spillover once noticed / no hard-stop access path): In-bounds. This session used only owner-supplied local JSON copies of public `r/FinancialCareers` threads. No live login, account spillover, scraping bypass, or undisclosable method was used in-session.
- Out-of-bounds material observed and excluded:
  - live Reddit state after the supplied local JSON cutoff;
  - linked media binaries and gallery assets not present as local files;
  - thread continuation or expansion beyond what the supplied JSON already contains;
  - external venue coverage, other subreddits, WSO, user-profile traversal, and claim verification outside the five supplied files.

## Capture Mode
- Initial mode (human-led / agent-assisted / structured access / archive-history / automated extraction / multimodal / mixed): agent-assisted
- Material mode changes during the session (each with reason): none

## Per-Obligation Discharge States

| # | Obligation | State | Reason (required for non-`met`) |
| --- | --- | --- | --- |
| 1 | Commissioning Gate | met |  |
| 2 | Boundary Compliance | met |  |
| 3 | Capture-Event Provenance | met |  |
| 4 | Capture Mode Disclosure | met |  |
| 5 | Mode-Change Rule | met |  |
| 6 | Raw Observable Fidelity | partial | `R01` is a gallery thread and includes comment-linked preview-image rows; the supplied JSON preserves media metadata and preview URLs but not binary gallery/image assets. `R03` also includes preview-image-only comment rows. |
| 7 | Source Identity And Actor Context | met |  |
| 8 | Decomposed Timing | met |  |
| 9 | Cutoff Posture | met |  |
| 10 | Archive / Historical Posture | met |  |
| 11 | Source Visibility And Access Limits | met |  |
| 12 | Related Context Preservation | partial | Thread hierarchy and OP/comment/reply context are preserved per slice, but `R01` gallery meaning and `R03` linked-image meaning are only partially inspectable from JSON metadata/preview URLs. |
| 13 | Bundled-Offer Structure Observables | not_applicable | The five supplied slices are forum threads about school choice, internships, resume presentation, and role progression, not source-presented multi-term offers or bundles. |
| 14 | Capture Failure And Blocker Visibility | met |  |
| 15 | Re-Capture Semantics | not_applicable | No earlier same-slice capture artifact or prior-source snapshot was supplied in this session, so no supersede/supplement/conflict relation could be mapped here. |
| 16 | Categorical Handoff Readiness | partial | The five slices are inspectable as a bounded Reddit sub-batch, but `R01` remains materially image-limited and `R03` includes linked-image-only rows. Media-preserving recapture should be considered before treating those slices as fully inspectable for layout-dependent meaning. |

## Per-Slice Posture
- Archive/history per slice:
  - `R01` `1tmu6ft`: `not_attempted`. Post created `2026-05-25T01:16:36Z`. Local file cutoff `2026-05-29T09:08:26.1943027Z`. Gallery post with 3 gallery items, 120 captured comment rows, 2 `[deleted]` rows, 3 comment rows with preview-image metadata, and one empty `more` placeholder under parent `t1_onte3yw`.
  - `R02` `1r38dch`: `not_attempted`. Post created `2026-02-12T23:00:14Z`, post edited `2026-02-12T23:12:18Z`, local file cutoff `2026-05-29T08:38:42.8733945Z`. Self-post with 118 captured comment rows, 4 `[deleted]` rows, and 1 stickied AutoModerator row.
  - `R03` `1tj8f96`: `not_attempted`. Post created `2026-05-21T03:30:54Z`, post edited `2026-05-21T04:16:42Z`, local file cutoff `2026-05-29T08:37:06.4785801Z`. Self-post with 42 captured comment rows, 1 stickied AutoModerator row, and 2 comment rows carrying preview-image metadata only.
  - `R04` `1qw3ufa`: `not_attempted`. Post created `2026-02-04T22:54:29Z`. Local file cutoff `2026-05-29T09:08:39.679474Z`. Self-post with 13 captured comment rows and 1 stickied AutoModerator row. No edited rows are visible in the supplied JSON.
  - `R05` `1p6hhbb`: `not_attempted`. Post created `2025-11-25T16:47:28Z`. Local file cutoff `2026-05-29T09:08:30.923168Z`. Self-post with 26 captured comment rows, 1 stickied AutoModerator row, and 1 edited comment row.
- Source visibility/access per slice:
  - All five slices are owner-supplied local JSON snapshots of public `r/FinancialCareers` threads. No live in-session visibility check was attempted after the local file cutoff.
  - `R01` is a Reddit gallery post (`is_gallery=true`) rather than a text-only self-post. Gallery items and comment-linked images are visible as metadata/preview URLs only.
  - `R02`, `R03`, `R04`, and `R05` are self-posts. `R02` includes 4 visible `[deleted]` rows. `R03` includes preview-image metadata in comment rows. `R01` includes 2 visible `[deleted]` rows and one empty continuation placeholder.
- Related context per slice:
  - `R01`: 53 top-level comments, max depth 9, gallery post plus reply chain `onpvctq -> onpvdh3 -> onpvewz` carrying preview-image-only replies.
  - `R02`: 68 top-level comments, max depth 4, OP post edited in-thread, multiple OP replies, one stickied AutoModerator row, four visible `[deleted]` rows.
  - `R03`: 23 top-level comments, max depth 4, OP clarification reply chain about USC as semi-target, one stickied AutoModerator row, and image-bearing comment rows `on3hkw8` and `on4cvqd`.
  - `R04`: 5 top-level comments, max depth 3, one stickied AutoModerator row, and OP follow-up replies on lack of work experience and schedule pressure.
  - `R05`: 6 top-level comments, max depth 4, one stickied AutoModerator row, and OP replies on dissatisfaction with risk work, geography, and compensation.
- Re-capture relationship per slice:
  - `R01`: Future recapture should be considered if downstream needs actual gallery/image binaries or a live-thread continuation check beyond the supplied JSON snapshot.
  - `R02` to `R05`: No earlier same-slice capture was supplied in this session. If later re-captured, these listed JSON hashes should be treated as the first bounded snapshot for relation-mapping purposes.

## Raw Observable Pointers
- Capture-session source files and hashes:
  - `R01` `C:\Users\vmon7\Desktop\projects\orca\docs\_inbox\data_capture_pressure_test_operator_supplied_2026_05_29\slot3_reddit_b1\raw\thread_json\reddit_t3_1tmu6ft.json` `SHA256 88826922CFC3E85E58F73AE153CCB43325408C0705B29AE82C7DACA5A25111CA`
  - `R02` `C:\Users\vmon7\Desktop\projects\orca\docs\_inbox\data_capture_pressure_test_operator_supplied_2026_05_29\slot3_reddit_b1\raw\thread_json\reddit_t3_1r38dch.json` `SHA256 D0981D8106F3155DC0EA7BCCC45B4CBE66713671FC43435DA82E77A95A924562`
  - `R03` `C:\Users\vmon7\Desktop\projects\orca\docs\_inbox\data_capture_pressure_test_operator_supplied_2026_05_29\slot3_reddit_b1\raw\thread_json\reddit_t3_1tj8f96.json` `SHA256 19EB89BA44A45A0F1FE9DEDB034839970199691703C47D214ED739EFE1B33B14`
  - `R04` `C:\Users\vmon7\Desktop\projects\orca\docs\_inbox\data_capture_pressure_test_operator_supplied_2026_05_29\slot3_reddit_b1\raw\thread_json\reddit_t3_1qw3ufa.json` `SHA256 9170303139CB0F9B88368A99FF40D600E5F6B866A84FA25602B7537BD4BB0E5A`
  - `R05` `C:\Users\vmon7\Desktop\projects\orca\docs\_inbox\data_capture_pressure_test_operator_supplied_2026_05_29\slot3_reddit_b1\raw\thread_json\reddit_t3_1p6hhbb.json` `SHA256 44FDC066E7A96DED5D7972F9581C3F377191665C4AEA3E603A42EC14A98F41C9`
- Per-slice raw pointers:
  - `R01` `1tmu6ft` `200+ applications no job`:
    - post surface: gallery post in `r/FinancialCareers`, flair `Breaking In`, score `87`, `upvote_ratio 0.85`, declared `128` comments, captured `120` comment rows, max depth `9`;
    - post body reports `200+` applications, `1` offer later rescinded, and asks for advice;
    - high-score reply pointers: `onpgr09` (score `176`), `onppeff` (score `99`), `onqbtdf` (score `36`), `onpzf9j` OP reply (score `43`);
    - deleted-row pointers: `onpkhaq`, `onprp54`;
    - image/linked-media pointers: post gallery media IDs `oj6h6ojyp63h1`, `annloojyp63h1`, `qskwiojyp63h1`; comment image chain `onpvctq`, `onpvdh3`, `onpvewz`; preview URLs and media metadata are present in JSON, but binary assets were not fetched.
  - `R02` `1r38dch` `I wish I could kick the shit out of my 15 year-old self.`:
    - post surface: self-post in `r/FinancialCareers`, flair `Off Topic / Other`, score `154`, `upvote_ratio 0.74`, declared `116` comments, captured `118` comment rows, max depth `4`;
    - post body centers on non-target regret, target-school prestige, and fear of back-office outcomes; post edit visible in-source;
    - high-score reply pointers: `o52hpon` (score `338`), `o52hngm` (score `142`, edited), `o52piui` (score `134`), `o5315id` (score `120`);
    - AutoModerator pointer: `o52geho` (stickied);
    - deleted-row pointers: `o52kci7`, `o52mbob`, `o52mhe4`, `o52n7rg`.
  - `R03` `1tj8f96` `Is it worth giving up a target school to go to a non target with a full ride?`:
    - post surface: self-post in `r/FinancialCareers`, flair `Education & Certifications`, score `16`, `upvote_ratio 0.9`, declared and captured `42` comment rows, max depth `4`;
    - post body weighs USC prestige/network against Northeastern full-ride economics; post edit clarifies USC was meant as semi-target rather than target;
    - high-score reply pointers: `omzt2ap` (score `57`), `omzq850` (score `45`), `on2gtg4` (score `17`), `on2nkex` (score `14`), `omzv3hw` (score `13`);
    - AutoModerator pointer: `omzowbo` (stickied);
    - linked-media pointers: `on3hkw8` and `on4cvqd` carry preview-image metadata/URLs in comment rows; binaries were not fetched.
  - `R04` `1qw3ufa` `Junior Year at Non-Target and No Internships/Work Experience - What Should I Do?`:
    - post surface: self-post in `r/FinancialCareers`, flair `Education & Certifications`, score `8`, `upvote_ratio 0.91`, declared and captured `13` comment rows, max depth `3`;
    - post body states junior-year finance major, weak first two college years, no internships or work experience, worry about 2026 internship closings, and asks whether the situation is already too late;
    - high-score reply pointers: `o3m9njc` (score `7`), `o3m9q6p` (score `3`), `o3ng9mb` OP reply (score `3`), `o3oapjh` (score `2`);
    - AutoModerator pointer: `o3m8x6x` (stickied).
  - `R05` `1p6hhbb` `Non-target, working in a BB in Risk...Dreaming the FO`:
    - post surface: self-post in `r/FinancialCareers`, flair `Career Progression`, score `11`, `upvote_ratio 0.87`, declared and captured `26` comment rows, max depth `4`;
    - post body states non-target European background, BB market-risk role, wish to move to front office/trading, and concern about staying stuck in back office;
    - high-score reply pointers: `nqqg8dj` (score `35`), `nqrqhp9` (score `33`), `nqrujf1` (score `15`), `nqqw4ci` OP reply (score `10`), `nquoy01` (score `9`);
    - AutoModerator pointer: `nqq9zbf` (stickied);
    - edited-row pointer: `nqzja8e` (edited comment discussing MBA versus trading recruiting posture).
- Bounded source-language raw observable anchors:
  - Source basis for this subsection: supplied local `readable.md` thread views under `docs/_inbox/data_capture_pressure_test_operator_supplied_2026_05_29/slot3_reddit_b1/cleansed/threads/`. These are bounded anchors for artifact-internal inspection only, not full-thread restatement.
  - `R01` `1tmu6ft` `200+ applications no job`:
    - OP title anchor: `200+ applications no job`
    - OP body anchor: `I've applied to about 200 jobs since January preparing for graduation. I have had no luck and managed to land only 1 and about 10 interviews but the offer got it rescinded. Any advice?`
    - excerpt `onpgr09` score `176`: `It's a pretty bad market for fresh grads and even moreso for those from just no offense no name schools... where is your GPA?... You do not need a summary for an entry level resume... Remove the random bolding... Add some quantitative lens to your California internship...`
    - excerpt `onppeff` score `99`: `The random bold text makes it seem like you copied your whole resume from ChatGPT.`
    - excerpt `onpzf9j` OP reply score `43`: `I had 3.28 as to why I didn't list it. Thanks for the advice`
    - remaining visible limitations: deleted rows remain pointer-only as `onpkhaq` and `onprp54`; linked-media rows `onpvctq`, `onpvdh3`, and `onpvewz` remain preview-URL / metadata-only without local image binaries.
  - `R02` `1r38dch` `I wish I could kick the shit out of my 15 year-old self.`:
    - OP title anchor: `I wish I could kick the shit out of my 15 year-old self.`
    - OP body anchor: `Junior year of a B.A in Economics, 3.87 GPA, and now I'm staring down the barrel of unemployment... I feel so stuck... I'm transfering to a handful of targets now but it seems like if I don't make it I'm stuck in BO for life.`
    - excerpt `o52hpon` score `338`: `35 year old you: I wish I could kick the shit out of my 21 year old self`
    - excerpt `o52piui` score `134`: `you have a 3.9 at a state school -- it may not be harvard but you will still have good opportunities when you graduate... once you graduate, after 3-5 years you can apply to business school... if you lock in, and apply yourself, you will be fine.`
    - excerpt `o52hngm` score `142`, edited: `I graduated in political science with a 3.2 at super non-target school, make a good bit more than that at one of KKR's main rivals... Wayyyy too early to say if you're cooked lol.`
    - remaining visible limitations: AutoModerator row remains separately visible as pointer `o52geho`; deleted rows remain pointer-only as `o52kci7`, `o52mbob`, `o52mhe4`, and `o52n7rg`.
  - `R03` `1tj8f96` `Is it worth giving up a target school to go to a non target with a full ride?`:
    - OP title anchor: `Is it worth giving up a target school to go to a non target with a full ride?`
    - OP body anchor: `I got into usc and northeastern... I was able to get a full ride to northeastern. How much should I weigh the two options between prestige and the benefit of getting free tuition?... Edit: Made the mistake of calling usc a target school I guess it isn't.`
    - excerpt `omzq850` score `45`: `Northeastern just as good as USC. Neither are elite. Take the $$$`
    - excerpt `on2gtg4` score `17`: `USC is like a high semi target but northeastern is a non target completely`
    - excerpt `omzv3hw` score `13`: `USC will get more opportunities, but it's still brutal competition especially to stay in LA or get to SF...`
    - excerpt `omztgjk` OP reply score `6`: `My bad (semi target) I just know Marshall is pretty good in getting placement`
    - remaining visible limitations: AutoModerator row remains separately visible as pointer `omzowbo`; linked-media row `on3hkw8` is preview-image URL only, and `on4cvqd` includes text plus a preview-image URL without a locally preserved image binary.
  - `R04` `1qw3ufa` `Junior Year at Non-Target and No Internships/Work Experience - What Should I Do?`:
    - OP title anchor: `Junior Year at Non-Target and No Internships/Work Experience - What Should I Do?`
    - OP body anchor: `I wasn't on my stuff for the first 2 years of my college... I've got all A's since and have a 3.6 GPA now... I didn't do any internships so far... I feel like it's too late now and there's nothing I can do.`
    - excerpt `o3m9njc` score `7`: `Start applying to McDonald's. Jkjk, start mass-emailing small boutique firms to try to find some position, any position. If it isn't cost-prohibitive, take an extra year...`
    - excerpt `o3ng9mb` OP reply score `3`: `No work experience in general sadly... All I could put would be some group projects I did in class...`
    - excerpt `o3qzxqe` score `2`: `You're still a junior... Find anything local that can just let you shadow and see stuff... Check on campus for work too... You're not cooked...`
    - remaining visible limitations: AutoModerator row remains separately visible as pointer `o3m8x6x`; no deleted-row or linked-media anchor text is visible in this slice beyond the preserved readable thread.
  - `R05` `1p6hhbb` `Non-target, working in a BB in Risk...Dreaming the FO`:
    - OP title anchor: `Non-target, working in a BB in Risk...Dreaming the FO`
    - OP body anchor: `I come from a non-target school... I currently work in a bulge bracket (morgan stanley) as a market risk analyst... I want to work in front office (ideally trading)... What else can I do? I don't want to stay stuck in a back office for the rest of my life`
    - excerpt `nqqg8dj` score `35`: `Whats with the obsession with FO investment roles? Trust me working in risk is actually extremely lucrative down the line... You got an extremely sweet deal...`
    - excerpt `nqqw4ci` OP reply score `10`: `I'm not satisfied with what I do... I often have to over work, like 10-12 hours a day... I don't feel compensated enough...`
    - excerpt `nqrqhp9` score `33`: `Right. A FO junior would say exactly the same, plus more abuse.`
    - excerpt `nqsqliv` score `2`: `It’s possible. I have seen people move from market risk on to a desk... Just need to be smart and hustle.`
    - remaining visible limitations: AutoModerator row remains separately visible as pointer `nqq9zbf`; edited comment row remains separately visible as pointer `nqzja8e`.
- Notes on modality preservation where text-only would lose signal:
  - `R01` is the strongest modality-risk slice because the post is a gallery and the reply chain includes preview-image-only comments. JSON preserves media IDs, preview URLs, hierarchy, scores, timestamps, and edit state, but not the gallery binaries.
  - `R03` also includes preview-image-only comment rows, but the dominant thread meaning remains text-visible in the supplied JSON.

## Failures, Blockers, and Limitations
- Capture-owned failures observed:
  - no linked-media binary fetch was performed for `R01` or `R03`;
  - no live-thread continuation or archive/history fetch was performed for any slice;
  - `R01` includes one empty `more` placeholder, so continuation completeness beyond the supplied JSON is not proven from this session alone.
- Visible limitations to travel downstream:
  - local JSON file state, not live Reddit state, is the operative cutoff for each slice;
  - deleted rows are preserved only as visible `[deleted]` placeholders where the JSON exposed them;
  - actor identity remains limited to Reddit-visible usernames, visible flair text where present, and moderator/bot markers where present;
  - layout-dependent meaning is strongest in `R01` and partially present in `R03`, where preview-image metadata exists without local binary assets.
- Out-of-bounds material treated as out of bounds (not worked around):
  - no live Reddit fetches after the supplied cutoff;
  - no user-profile traversal;
  - no external venue expansion;
  - no linked-media binary retrieval from preview URLs;
  - no cross-venue or cross-thread synthesis beyond the five supplied slices.

## Agent-Assistance Context
- Allowed agent verbs used:
  - fetch supplied local files;
  - mechanically group exact supplied source locators;
  - transcribe source-visible post/comment structure, timestamps, scores, deleted rows, edit flags, and media metadata into this capture artifact.
- Discarded candidates and discard reason categories:
  - live Reddit fetches, archive/history fetches, linked-media fetches, user-profile expansion, and cross-venue expansion were discarded as out-of-scope against the owner-pinned `local_file_path` mode and cutoff posture.
- Any cross of the allow/forbid line (must be `blocked` on the relevant obligation):
  - none observed

## Categorical Handoff Or Visible Stop
- Handoff state: `re-capture_posture`
- Reason if not categorical_handoff_to_ECR: `R01` is materially image-dependent and the supplied JSON preserves only gallery metadata / preview URLs rather than binary gallery assets. `R03` also contains preview-image-only comment rows. The five slices are captured as a bounded first Reddit snapshot, but media-preserving recapture should be considered before treating the sub-batch as fully inspectable for layout-dependent source meaning.

## LLM Capture-Visibility Checker Output
- Output: `visible_capture_limitation`
- Specifics: Obligations 6, 12, and 16 carry visible capture limitations: `R01` is gallery/image-dependent with only media metadata and preview URLs preserved, and `R03` has preview-image rows without local image binaries. The artifact also makes local JSON cutoff, no live/archive continuation, pointer-only deleted rows, and limited Reddit-visible actor context explicit. These limitations are declared in the obligation table, per-slice posture, raw observable pointers, and handoff section, and the handoff state is categorical as `re-capture_posture` without defining ECR fields, IDs, schemas, storage, or runtime data shapes.
- Remediation taken by capture operator (if any): Added OP-title / OP-body anchors plus 2-4 source-language comment or OP-reply excerpts per slice, while leaving deleted, AutoModerator, linked-media, and continuation limitations explicit as pointers where full content is unavailable.
- Post-remediation re-invocation output (if any): This `visible_capture_limitation` result is the post-remediation checker output.
