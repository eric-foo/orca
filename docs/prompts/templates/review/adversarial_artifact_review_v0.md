# Adversarial Artifact Review Template v0

```yaml
retrieval_header_version: 1
artifact_role: Prompt template
scope: Read-only adversarial review template for non-code Orca artifacts.
use_when:
  - Reviewing prompts, research artifacts, product docs, decisions, or workflow artifacts.
authority_boundary: retrieval_only
```

Model target: model-neutral

Output mode: `review-report` or `paste-ready-chat`

Use shared contract:
`docs/prompts/templates/shared/orca_prompt_behavior_contract_v0.md`

```text
You are performing a read-only adversarial artifact review for Orca.

Review target:
[FILL_ARTIFACT_PATH_OR_TEXT]

Review purpose:
[FILL_REVIEW_PURPOSE]

Required source hierarchy:
- `AGENTS.md`
- `.agents/workflow-overlay/README.md`
- `.agents/workflow-overlay/source-of-truth.md`
- `.agents/workflow-overlay/artifact-roles.md`
- `.agents/workflow-overlay/review-lanes.md`
- `.agents/workflow-overlay/prompt-orchestration.md`
- `.agents/workflow-overlay/communication-style.md`
- `.agents/workflow-overlay/validation-gates.md`
- `.agents/workflow-overlay/template-registry.md`
- [FILL_ADDITIONAL_REQUIRED_SOURCES]

Edit permission:
Read-only unless the launch instruction explicitly assigns patch execution.

Required skill invocation:
Use `workflow-deep-thinking` first.

Then use `workflow-adversarial-artifact-review`.

The deep-thinking step should frame the boundary problem, failure modes, and
decision criteria before findings are listed. It does not widen review scope or
authorize patching.

Output mode and report contract:
Use exactly one output mode for the run.

If output mode is `review-report`, bind a durable report destination under
`docs/review-outputs/` or a typed child folder before review work starts. The
human-readable review belongs in that durable report. Chat YAML is courier
output only and is valid only after the required durable report has been
successfully written.

After a successful report write, return the compact `review_summary` YAML from
`.agents/workflow-overlay/communication-style.md` with `status: completed` and
`report_path` pointing to the written report.

If the required report cannot be written after `review-report` is selected,
do not use `report_path` and do not treat chat YAML as a substitute report.
Return a failed blocked `review_summary` with `status: failed`,
`review_location: chat_only_current_thread`, and `recommendation: blocked`;
name the failed path and include enough human-readable failure detail in
`summary` or `next_action` to route the issue. Do not add extra YAML keys.

If no write authority or report destination is bound before review work starts,
use `paste-ready-chat` instead of `review-report`.

Review checks:
- Source hierarchy and authority boundary.
- Internal consistency.
- Missing required inputs or unbound roles.
- Output mode and destination correctness.
- Downstream executability.
- Leakage of `jb` project policy or template language.
- Overclaims, readiness claims, validation claims, buyer-proof claims, or commercial claims.

Findings:
List findings first, ordered by severity:
- critical
- major
- minor

For each finding include:
- severity;
- location;
- issue;
- evidence;
- impact;
- recommended correction.

If no issues are found, say so and list residual risks or test gaps.

Non-claims:
Do not claim approval, validation, readiness, implementation authorization, or
product proof unless the prompt and Orca sources explicitly bind that claim.
```
