# Orca Prompt Behavior Contract v0

```yaml
retrieval_header_version: 1
artifact_role: Prompt template
scope: Shared Orca behavior contract for project-local prompt templates.
use_when:
  - A prompt template needs common Orca source, boundary, and non-claim rules.
authority_boundary: retrieval_only
```

Use this contract only when a prompt explicitly references it.

## Source Authority

- Current user instruction for the turn wins.
- Orca `AGENTS.md` and `.agents/workflow-overlay/` own Orca project facts.
- Orca docs under `docs/` are subordinate to the overlay when conflicts appear.
- `agent-workflow` may provide reusable mechanics only.
- `jb` paths, product rules, lifecycle mechanics, templates, validation habits,
  and handoffs are not Orca authority.

## Output Discipline

- Name exactly one output mode.
- For decision-bearing chat, follow the chat-output topology in
  `.agents/workflow-overlay/communication-style.md`: human summary first,
  agent-readable detail second, and compact courier YAML last when useful or
  required.
- Use `.agents/workflow-overlay/prompt-orchestration.md` for output-mode
  exceptions, including `review-report`, `file-write`, `paste-ready-chat`, and
  `patch-queue`.
- Keep missing source fields as `not_found`, `not_bound`, or `UNKNOWN - requires owner input`.
- Do not turn evidence collection into synthesis unless the prompt is a synthesis template.
- Do not claim validation, readiness, approval, deployment, install, resolver, buyer validation, willingness to pay, implementation readiness, feature readiness, or commercial readiness unless an accepted Orca source and current evidence explicitly bind that claim.

## Source-Heavy Work

For public web or source-heavy tasks:

- define the unit of work before source loading starts;
- keep evidence URLs stable and citeable;
- avoid long pasted source text;
- separate evidence, synthesis, backtestability, and anonymous marketing claims;
- stop rather than continue if source loading becomes unbounded.

## Report Shape

Prefer compact outputs that preserve:

- objective;
- scope and date boundary;
- source list or source URL table;
- missing-field labels;
- blocker states;
- non-claims;
- next authorized step.

Compactness means omit unnecessary fields and full source echoes. It does not
mean hiding a decision-bearing answer in YAML-only or agent-only structure.
Artifact-native tables, paste-ready prompt bodies, and post-artifact receipts
remain valid when the output mode permits them.
