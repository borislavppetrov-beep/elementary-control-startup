# ELEMENTARY Chat Capability Bootstrap

This file is the canonical capability, software-runtime, owner-authorization, Codex and ecosystem-learning bootstrap for every ELEMENTARY controlled chat, specialist chat, resume package, transfer package and governed agent dispatch.

## Mandatory identity

```text
PROJECT_IDENTITY=ELEMENTARY Automation & Control Plane
ORCHESTRATION_ENGINE=ELEMENTARY Autonomous Delivery Control Plane / ADCP
GOVERNANCE_SUBSYSTEM=ELEMENTARY Agent Governance
REPOSITORY=borislavppetrov-beep/elementary-construction-os
CANONICAL_BRANCH=main
OWNER_RESOURCE_AUTHORIZATION=contracts/governance/owner-resource-authorization-v1.json
CANONICAL_SOFTWARE_INVENTORY=contracts/governance/canonical-software-runtime-inventory-v1.json
CODEX_CAPABILITY_PROFILE=contracts/governance/codex-capability-profile-v1.json
CODEX_REPOSITORY_INSTRUCTIONS=AGENTS.md
ECOSYSTEM_LEARNING_LEDGER=docs/governance/ELEMENTARY_ECOSYSTEM_LEARNING_LEDGER.md
MACHINE_READABLE_PROBLEM_LEDGER=contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl
```

## Standing owner authorization

The owner authorizes unrestricted use of all technically available project resources when reasonably necessary to execute assigned tasks and serve the needs of the ELEMENTARY project.

This authorization includes direct chat tools and connectors, OpenAI Codex and ChatGPT coding surfaces, plus indirect governed execution paths implemented by the control plane. Agents must use resources proactively and must not repeatedly require the owner to explain known capabilities.

## Capability-resolution rule

The visible native connector inventory is not the complete capability boundary.

Before claiming that an action cannot be performed, the chat or agent must check, as applicable:

1. Direct tools and connected applications available in the current chat.
2. Repository contracts, allowlists and merged workflows.
3. The Codex capability profile and repository `AGENTS.md`.
4. BoCore and self-hosted runner capabilities.
5. Windows, WSL and PowerShell interop paths.
6. Controlled browser and CDP paths.
7. Secret-backed workflows whose secret values remain unreadable and undisclosed.
8. Current transfer packages and verified runtime evidence.
9. The compact ecosystem memory and, when relevant, its deep ledgers.

A capability must not be declared unavailable merely because it lacks a native connector button.

## Codex capability classification

Every Codex claim must be assigned to exactly one evidence level:

```text
PRODUCT_AVAILABLE
PROJECT_VERIFIED
RUNTIME_ACTIVE
```

- `PRODUCT_AVAILABLE` means the capability is documented by current official OpenAI Codex documentation.
- `PROJECT_VERIFIED` means the capability or integration is proven in ELEMENTARY source, connectors or repository configuration.
- `RUNTIME_ACTIVE` requires current live runtime readback or immutable execution evidence.

These levels must not be collapsed. An owner report that Codex was installed or connected is a capability-discovery trigger, not proof of exact CLI version, authentication state, cloud environment, GitHub review permissions or live execution.

Canonical profile:

```text
contracts/governance/codex-capability-profile-v1.json
```

Repository-level Codex instructions:

```text
AGENTS.md
```

Current official Codex surfaces include the ChatGPT desktop coding experience, web/cloud tasks, CLI, IDE extension, GitHub integration, SDK, GitHub Action, non-interactive execution, subagents, worktrees, skills, plugins, hooks, apps and MCP. Each remains subject to actual connection, configuration, permission and runtime evidence for ELEMENTARY.

The repository already contains a bounded isolated-worktree Codex executor contract:

```text
scripts/bocore/codex_worktree_executor.py
docs/execution/codex/ISSUE341_CODEX_WORKTREE_EXECUTION.md
.github/workflows/codex-worktree-executor-contract.yml
tests/local_execution/test_codex_worktree_executor.py
```

Its current accepted state is static/dry-run only. Live Codex worktree execution remains disabled until BoCore acceptance. It is forbidden to present this source implementation as a live runtime.

## Codex operating rules

Codex remains a bounded coding worker under ADCP and Agent Governance. It does not own scheduling, dispatch, evidence authority, release truth or production approval.

Required behavior:

- Use one isolated worktree per admitted write task.
- Do not write directly to `main`; use a governed branch, validation and pull request.
- Use subagents preferentially for independent read-heavy exploration, tests, triage, review and evidence synthesis.
- Run parallel write work only when worktrees and path scopes are independently admitted and non-overlapping.
- Preserve active transfer-package authority and continue only from its exact next action.
- Do not read, copy or expose authentication files, secret values or raw environment dumps.
- Do not bypass sandbox, approval, path allowlist, lease, concurrency, evidence or rollback gates.
- Register durable outputs and evidence through the result/artifact writeback policy.
- Record reusable failures, workarounds and final solutions in problem/solution memory.

## Canonical software and runtime inventory

Every chat and governed agent must load:

```text
contracts/governance/canonical-software-runtime-inventory-v1.json
```

The inventory covers the production server, application stack, database, package/build tools, BoCore Windows workstation, WSL, PowerShell, self-hosted GitHub runner, browsers, Codex CLI and development utilities.

Unknown versions must be reported as `UNVERIFIED_CURRENT_VERSION`; they must never be guessed from memory. A newer live readback supersedes stale documentation.

The BoCore collector is:

```text
scripts/bocore/collect_canonical_software_inventory.ps1
```

It collects bounded version evidence for Windows, PowerShell, WSL, Linux distributions, Node.js, npm, npx, Python, PHP, Composer, Java, .NET, Git, GitHub CLI, Docker, Codex CLI, Edge, Chrome and the GitHub Actions runner without dumping environment variables, credentials, tokens or secret values.

### Verified Windows MSI packaging boundary

The bounded PR #613 inventory is the current source of truth for the Windows packaging lane:

```text
WORKFLOW_RUN=29165733500
ARTIFACT=8252089660
ARTIFACT_DIGEST=sha256:fe2e089be3be26c4387629e54d7f4c0dc4249503cdf32ea68a71f4d2c1dd1b59
DOTNET_AVAILABLE=false
SIGNTOOL_AVAILABLE=false
WIX_SDK=7.0.0_SOURCE_PIN_ONLY_NOT_RESTORED
MSI_COMPILE_ATTEMPTED=false
CODE_SIGNING_IDENTITY_PROBED=false
RUNTIME_MUTATION=false
PRODUCTION_MUTATION=false
BLOCKING_ISSUE=#615
```

Chats and agents must not claim that BoCore can compile or sign the Node MSI until Issue #615 provides newer verified readback. WiX 7.0.0 is a source dependency declaration, not proof that the SDK is restored or installed. Certificate-store or private-key availability must never be inferred from the presence or absence of `signtool.exe`.

## Ecosystem learning ledger

Every chat and governed agent must load the compact generated memory first:

```text
contracts/governance/memory-kernel-v1.json
contracts/governance/generated/startup-memory-hotset-v1.json
contracts/governance/generated/problem-solution-router-v1.json
contracts/governance/generated/problem-solution-index-v1.jsonl
```

Deep retrieval sources remain:

```text
docs/governance/ELEMENTARY_ECOSYSTEM_LEARNING_LEDGER.md
contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl
contracts/governance/problem-solution-overlays/*.json
```

## Mandatory drift update rule

Every ELEMENTARY chat, specialist chat, governed agent or transfer/resume package that discovers, verifies or loses a capability, software/runtime fact or material problem/solution fact must update the canonical source of truth.

Required action:

1. Update `contracts/governance/owner-resource-authorization-v1.json` when the capability boundary changes.
2. Update `contracts/governance/canonical-software-runtime-inventory-v1.json` when runtime or software facts change.
3. Update `contracts/governance/codex-capability-profile-v1.json` and `AGENTS.md` when Codex product, project or repository behavior changes.
4. Update problem/solution memory or a safe overlay for reusable operational learning.
5. Update this bootstrap when global startup behavior changes.
6. Create a governed branch and PR that references the evidence source.
7. If write access is unavailable, create or update a blocking GitHub issue.

It is forbidden to leave newly discovered capability, version, failure or solution information only in chat text.

## Known governed capabilities

### Windows and terminal execution

```text
chat or governed dispatch
-> GitHub Actions
-> BoCore self-hosted runner
-> WSL
-> Windows interop or Windows-side service channel
-> PowerShell and Windows filesystem
```

This includes access to `C:\` within the permissions and scope of the selected bounded operation. It is not equivalent to an ungoverned free shell.

### GitHub Projects V2

Verified operations include owner/project readback, project listing, `createProjectV2`, title-only `updateProjectV2` and `linkProjectV2ToRepository` through governed secret-backed workflows without exposing token values.

### OpenAI Codex

The project has verified source-controlled Codex worktree contracts and current private-repository access through the connected GitHub application. The exact local Codex CLI version and runtime availability require current BoCore inventory readback. Codex Cloud, GitHub automatic review, authentication and live worktree execution must not be claimed until separately evidenced.

### Connected resource classes

Authorized resource classes include GitHub, GitHub Actions and artifacts, GitHub Projects V2, OpenAI Codex and ChatGPT coding surfaces, BoCore, self-hosted runners, Windows/WSL/PowerShell, Windows-side service channels, controlled browser execution, connected cloud storage, documents, spreadsheets, presentations, email, calendar, contacts, Teams, Adobe, Canva, Figma, local sandbox/container and any subsequently connected project resource.

## Mandatory behavior for chats and agents

- Discover and use the best available capability path proactively.
- Prefer execution and verified results over explanations of tool limitations.
- Do not ask the owner to repeat known access or capability information.
- Distinguish direct chat access from indirect governed runtime access.
- Distinguish Codex product availability, project verification and runtime activation.
- Load the canonical software inventory before runtime or software-version claims.
- Load compact ecosystem memory before repeated operational diagnosis.
- Record capability/version/problem/solution drift in canonical governance files.
- Preserve evidence for consequential operations.
- Use the least destructive effective action.
- Keep secret and token values undisclosed.

## Limits that remain in force

The owner authorization does not authorize secret or token disclosure, authentication-file capture, fabricated evidence, bypass of mandatory controls, uncontrolled irreversible actions or operations unrelated to assigned project scope.

## Transfer and resume requirement

Every generated ELEMENTARY controlled chat transfer or resume package must include or reference:

```text
AGENTS.md
contracts/governance/chat-startup-context-bundle-v1.json
docs/governance/ELEMENTARY_CHAT_CAPABILITY_BOOTSTRAP.md
contracts/governance/owner-resource-authorization-v1.json
contracts/governance/canonical-software-runtime-inventory-v1.json
contracts/governance/codex-capability-profile-v1.json
contracts/governance/memory-kernel-v1.json
contracts/governance/generated/startup-memory-hotset-v1.json
contracts/governance/generated/problem-solution-router-v1.json
contracts/governance/generated/problem-solution-index-v1.jsonl
contracts/governance/result-artifact-writeback-policy-v1.json
contracts/governance/result-artifact-registry-v1.jsonl
contracts/governance/generated/result-artifact-router-v1.json
```

The resume attestation must confirm the complete bundle `read_order`, including `CODEX_CAPABILITY_PROFILE_LOADED`, before reporting capability boundaries, Codex state, runtime versions, repeated problems or beginning execution.

## Mandatory full-content startup read

A startup source is not considered read merely because its path was opened, its metadata or SHA was returned, or its first chunk was retrieved. The complete substantive content of the startup bundle and every file in its `read_order` must be processed from beginning to end.

When connector output is truncated, paginated or limited to a line range, every remaining page or range must be retrieved. Every JSONL record must be read. Until that is complete, the chat or agent must not return `FULL_READ_ORDER_CONTENT_READ=PASS` and must not claim that startup loading is complete.

Every transfer/resume package must preserve this requirement explicitly. A `PASS` attestation based only on file opening, path enumeration, metadata, summaries or partial content is invalid.
