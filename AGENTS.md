# ELEMENTARY Repository Instructions for Codex

These instructions apply to every Codex task, subagent, review, CLI run, IDE task, cloud task and SDK-driven operation in this repository.

## Mandatory startup

Before analysis, review, planning, mutation or capability claims:

1. Read `contracts/governance/chat-startup-context-bundle-v1.json` from the live `main` branch when available.
2. Read every file in its `read_order` completely from beginning to end.
3. Load `contracts/governance/professional-execution-policy-v1.json` and apply profile `REPOSITORY_CONSOLIDATION`.
4. Load `contracts/governance/codex-capability-profile-v1.json`.
5. If a controlled transfer/resume package is active, accept it as the operational context and continue only from its `EXACT_NEXT_ACTION`.
6. Return the startup attestation required by the bundle before mutation, including `PROFESSIONAL_EXECUTION_POLICY_LOADED=PASS`.

## Authority

```text
SOURCE_AND_RELEASE_TRUTH=GitHub main
LIFECYCLE_AND_ORCHESTRATION_AUTHORITY=ADCP
POLICY_AUTHORITY=ELEMENTARY Agent Governance
LOCAL_EXECUTION_AUTHORITY=existing BoCore governed paths
CODEX_ROLE=bounded coding/review worker
PROFESSIONAL_EXECUTION_PROFILE=REPOSITORY_CONSOLIDATION
```

Do not create a second scheduler, dispatcher, runner backlog, browser service, evidence authority or control plane.

## Professional execution profile

For repository consolidation, governance, startup delivery, coding, review, validation, evidence and release work:

- bind the task to exact current `main` before mutation;
- inventory relevant repositories, open PRs and active execution lines;
- complete schema and consumer impact review;
- prove that no duplicate canonical mechanism is being introduced;
- use one governed branch and one isolated worktree per admitted write task;
- keep primary and startup repository changes in separate pull requests;
- never push directly to primary or startup `main`;
- define rollback, cleanup, validation and evidence ownership;
- do not create a second delivery-truth contract; integrate with `elementary.operational-reality-audit.v1` when present;
- fail closed on runtime and production claims when current exact evidence is absent.

The public startup repository is a generated mirror. It is not an independent source of truth, and startup sync must use branch-and-pull-request delivery with no automatic merge.

## Capability truth

Always distinguish:

```text
PRODUCT_AVAILABLE
PROJECT_VERIFIED
RUNTIME_ACTIVE
```

Official Codex documentation or an owner installation report does not prove exact local CLI version, authentication, cloud configuration, GitHub review permissions or runtime activation. Use live runtime inventory and immutable execution evidence for `RUNTIME_ACTIVE`.

## Repository mutation

- Never write directly to `main`.
- Use one governed branch and one isolated worktree per admitted write task.
- Preserve the expected base SHA and stop if the live base or active PR head has moved unexpectedly.
- Keep changes inside the admitted path scope.
- Use existing validation commands and workflows; do not weaken gates to obtain green CI.
- Do not merge your own work unless the active authority explicitly permits it and all required checks and exact-head guards pass.
- Do not mutate production from a source/capability PR.
- When startup payload changes, open and validate a separate pull request in `borislavppetrov-beep/elementary-control-startup`.

## Subagents and parallel work

Use subagents for independent read-heavy work such as repository exploration, test analysis, issue triage, security review and evidence synthesis.

Parallel write work is permitted only when:

- each task has an independently admitted worktree;
- branches, leases and concurrency groups are distinct;
- path scopes are non-overlapping;
- reconciliation and evidence ownership are explicit.

Do not allow multiple agents to write to the same branch, worktree or overlapping files.

## Review priority

Prioritize findings that can cause:

1. security or secret exposure;
2. data loss or irreversible mutation;
3. governance, approval or capability-boundary bypass;
4. correctness failures;
5. concurrency, replay or idempotency defects;
6. rollback or recovery failure;
7. missing tests or misleading evidence.

Cite exact files and lines. Do not block solely on stylistic preferences unless style is part of the requested acceptance contract.

## Evidence and writeback

Every durable output must have:

- canonical location;
- task or issue reference when available;
- producer identity;
- evidence reference;
- validation state;
- commit SHA, artifact digest or SHA-256 when applicable.

Register durable outputs through the result/artifact registry or a safe overlay. Record reusable blockers, root causes, workarounds and final fixes in problem/solution memory or a safe overlay.

## Security

Never read, copy, print or commit:

- secret or token values;
- Codex authentication files;
- private keys;
- raw environment dumps;
- credential stores.

Do not bypass sandbox, approval, network, path allowlist, lease, concurrency, evidence or rollback controls.
