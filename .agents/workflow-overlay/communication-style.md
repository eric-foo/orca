# Communication Style

This file records Orca-specific response style for Chief Architect sequencing,
review closeouts, and prompt handoffs. It applies to user-facing chat and
Orca-authored prompts unless a later user instruction asks for a different
shape.

## Default Shape

Use short headers when they improve scanning.

Prefer bullets when they reduce parsing, but give each bullet a small
explanation. Do not bold the bullet lead by default.

Lead with the decision, then the scope, then the next action. Keep status and
file-state language secondary unless exact repository state is the point.

## Readability Rules

- Use plain decision language. Say what is accepted, blocked, deferred, or
  authorized before naming artifact status.
- Separate now, next, and later. Acceptance, review, commit, and proof execution
  must not blur together.
- Explain boundaries in terms of what they mean. For example: this prepares the
  proof shape; it does not run proof or collect evidence.
- Use exact file or git-state language only when it matters. Prefer "accepted in
  chat, not committed" over abstract phrases like "persistence caveat."
- Avoid process-heavy nouns when an action phrase is clearer. Watch for
  "review state," "coherent set," "artifact adequacy," and similar phrasing.
- Keep template output readable. Use the required shape, but do not sound like a
  form is being filled in.

## Goldilocks Bullet Pattern

- Name the action or issue. Add one sentence explaining why it matters.
- Keep bullets short enough to scan, but not so short that the reader has to
  infer the decision.
- Use prose when the sequence is the point and bullets would make it choppy.

## Preferred Closeout Pattern

Use this order for sequencing decisions:

1. Decision.
2. Scope or boundary.
3. Next action.
4. What remains blocked.

## Adversarial Review Summary Pattern

For adversarial artifact reviews, prefer a compact copy-pasteable YAML summary
before any detailed findings. This lets later threads recover the review state
without reading a long chat block.

Use this shape when the review writes or references a durable report:

```yaml
review_summary:
  status: completed
  report_path: docs/review-outputs/example_adversarial_review_v0.md
  recommendation: accept | accept_with_friction | patch_before_acceptance | reject | blocked
  findings_count: 0
  blocking_findings: []
  advisory_findings:
    - FF-01: Short finding title
  prior_findings_remediated: []
  next_recommended_action: "One concrete next step"
```

If no durable report exists because the review is chat-only, replace
`report_path` with `review_location: chat_only_current_thread` and keep the
same remaining fields.

Do not include these fields in Orca adversarial review summaries:

- `report_written`
- `protected_path_check`
- `hidden_ledger_read`
- `runtime_code_changed`
- `fixture_expansion_performed`
- `harness_or_compiler_or_path_b_run`

Detailed review prose may follow when useful, but the YAML summary should be
sufficient for another thread to know the review status, where to read it, the
blocking/advisory finding IDs, and the next action.
