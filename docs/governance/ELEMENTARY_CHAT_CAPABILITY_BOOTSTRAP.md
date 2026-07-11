# ELEMENTARY Chat Capability Bootstrap

This file is the canonical capability, software-runtime, owner-authorization and ecosystem-learning bootstrap for every ELEMENTARY controlled chat, specialist chat, resume package, transfer package and governed agent dispatch.

## Mandatory identity

```text
PROJECT_IDENTITY=ELEMENTARY Automation & Control Plane
ORCHESTRATION_ENGINE=ELEMENTARY Autonomous Delivery Control Plane / ADCP
GOVERNANCE_SUBSYSTEM=ELEMENTARY Agent Governance
REPOSITORY=borislavppetrov-beep/elementary-construction-os
CANONICAL_BRANCH=main
OWNER_RESOURCE_AUTHORIZATION=contracts/governance/owner-resource-authorization-v1.json
CANONICAL_SOFTWARE_INVENTORY=contracts/governance/canonical-software-runtime-inventory-v1.json
ECOSYSTEM_LEARNING_LEDGER=docs/governance/ELEMENTARY_ECOSYSTEM_LEARNING_LEDGER.md
MACHINE_READABLE_PROBLEM_LEDGER=contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl
```

## Standing owner authorization

The owner authorizes unrestricted use of all technically available project resources when reasonably necessary to execute assigned tasks and serve the needs of the ELEMENTARY project.

This authorization includes direct chat tools and connectors, plus indirect governed execution paths implemented by the control plane. Agents must use resources proactively and must not repeatedly require the owner to explain known capabilities.

## Capability-resolution rule

The visible native connector inventory is not the complete capability boundary.

Before claiming that an action cannot be performed, the chat or agent must check, as applicable:

1. Direct tools and connected applications available in the current chat.
2. Repository contracts, allowlists and merged workflows.
3. BoCore and self-hosted runner capabilities.
4. Windows, WSL and PowerShell interop paths.
5. Controlled browser and CDP paths.
6. Secret-backed workflows whose secret values remain unreadable and undisclosed.
7. Current transfer packages and verified runtime evidence.
8. The ecosystem learning ledger for prior problem/solution evidence.

A capability must not be declared unavailable merely because it lacks a native connector button.

## Canonical software and runtime inventory

Every chat and governed agent must load:

```text
contracts/governance/canonical-software-runtime-inventory-v1.json
```

The inventory covers the production server, application stack, database, package/build tools, BoCore Windows workstation, WSL, PowerShell, self-hosted GitHub runner, browsers and development utilities.

It distinguishes:

- exact verified live versions;
- dependency constraints declared in `composer.json` or `package.json`;
- standards such as HTML, CSS and ECMAScript that do not have an installed executable version;
- components whose current version still requires live BoCore readback.

Unknown versions must be reported as `UNVERIFIED_CURRENT_VERSION`; they must never be guessed from memory. A newer live readback supersedes stale documentation.

The BoCore collector is:

```text
scripts/bocore/collect_canonical_software_inventory.ps1
```

It collects bounded version evidence for Windows, PowerShell, WSL, Linux distributions, Node.js, npm, npx, Python, PHP, Composer, Java, .NET, Git, GitHub CLI, Docker, Codex CLI, Edge, Chrome and the GitHub Actions runner without dumping environment variables, credentials, tokens or secret values.

## Ecosystem learning ledger

Every chat and governed agent must load:

```text
docs/governance/ELEMENTARY_ECOSYSTEM_LEARNING_LEDGER.md
contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl
```

The learning ledger is the canonical operational memory for encountered problems, root causes, failed assumptions, evidence artifacts, fixes and follow-up actions.

It is the project-backed self-learning mechanism. It does not rely on private chat memory and it does not expose secrets. It makes future chats better by requiring them to read and update a shared repository record before repeating the same mistake.

## Mandatory capability, version and problem-solution drift update rule

Every ELEMENTARY chat, specialist chat, governed agent or transfer/resume package that discovers, verifies or loses a capability, software/runtime fact or material problem/solution fact must update the canonical source of truth.

This rule is triggered by any of the following:

```text
new connector or tool becomes available
connector/tool capability is removed, blocked or reduced
new indirect governed execution path is proven
previously known execution path stops working
new software/runtime version is verified
software/runtime version changes or becomes unavailable
package constraint changes in composer.json, package.json or equivalent
production, BoCore, runner, browser, database or server fact changes
new operational problem is encountered
root cause is proven or disproven
workaround becomes available
workaround is replaced by a final fix
workflow, service, runner or bridge assumption fails
```

Required action:

1. Update `contracts/governance/owner-resource-authorization-v1.json` when the capability boundary changes.
2. Update `contracts/governance/canonical-software-runtime-inventory-v1.json` when runtime, software, dependency, browser, database, server or workstation facts change.
3. Update `docs/governance/ELEMENTARY_ECOSYSTEM_LEARNING_LEDGER.md` and `contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl` when a material problem, root cause, workaround or final fix is discovered.
4. Update this bootstrap file when the global rule, propagation behavior or mandatory chat behavior changes.
5. Create a governed branch and PR that references the evidence source.
6. If write access is unavailable in the current chat, create or append to a GitHub issue with exact evidence and mark the canonical update as pending.

It is forbidden to leave newly discovered capability, version, failure or solution information only in chat text. The canonical repository files must be updated or a blocking follow-up issue must record why the update could not be made.

## Known governed capabilities

### Windows and terminal execution

The project has a governed execution path:

```text
chat or governed dispatch
-> GitHub Actions
-> BoCore self-hosted runner
-> WSL
-> Windows interop or Windows-side service channel
-> PowerShell and Windows filesystem
```

This includes access to `C:\` within the permissions and scope of the selected bounded operation. It is not equivalent to an ungoverned free shell, but it is a real terminal and filesystem capability.

When direct WSL execution of Windows `.exe` files fails, use a Windows-side governed service channel rather than arbitrary shell workarounds.

### GitHub Projects V2

The project has verified secret-backed GitHub Projects V2 access through governed workflows using `ELEMENTARY_GITHUB_PROJECTS_TOKEN` without exposing its value.

Proven operations include:

```text
owner identity and project-scope readback
project-list readback
createProjectV2
updateProjectV2 title-only
linkProjectV2ToRepository
```

Canonical Projects:

```text
ELEMENTARY Platform V1
ELEMENTARY Studio V1
ELEMENTARY Node V1
```

### Connected resource classes

Authorized resource classes include GitHub, GitHub Actions and artifacts, GitHub Projects V2, BoCore, self-hosted runners, Windows/WSL/PowerShell, Windows-side service channels, controlled browser execution, connected cloud storage, documents, spreadsheets, presentations, email, calendar, contacts, Teams, Adobe, Canva, Figma, local sandbox/container and any subsequently connected project resource.

## Mandatory behavior for chats and agents

- Discover and use the best available capability path proactively.
- Prefer execution and verified results over explanations of tool limitations.
- Do not ask the owner to repeat known access or capability information.
- Distinguish direct chat access from indirect governed runtime access.
- Load the canonical software inventory before making runtime or software-version claims.
- Load the ecosystem learning ledger before diagnosing repeated operational problems.
- Distinguish exact installed versions from declared package constraints.
- Record discovered capability/version/problem/solution drift in the canonical governance files, not only in chat text.
- Open a governed PR for canonical updates, or a blocking evidence issue when the current chat cannot write.
- Preserve evidence for consequential operations.
- Use the least destructive effective action.
- Keep secret and token values undisclosed.
- State an actual limitation only after checking the relevant indirect paths and the learning ledger.

## Limits that remain in force

The owner authorization does not authorize:

```text
secret or token value disclosure
fabricated evidence
illegal or policy-prohibited activity
bypass of mandatory platform controls
uncontrolled irreversible or destructive actions
operations unrelated to the assigned task or project need
```

Governance, evidence, rollback, recovery and explicit task-scope requirements remain applicable.

## Transfer and resume requirement

Every newly generated ELEMENTARY controlled chat transfer or resume package must include or explicitly reference:

```text
docs/governance/ELEMENTARY_CHAT_CAPABILITY_BOOTSTRAP.md
contracts/governance/owner-resource-authorization-v1.json
contracts/governance/canonical-software-runtime-inventory-v1.json
docs/governance/ELEMENTARY_ECOSYSTEM_LEARNING_LEDGER.md
contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl
```

The resume attestation must confirm that all five canonical files were considered before the chat reports capability boundaries, runtime versions, repeated problems or begins execution. It must also confirm that any newly discovered capability, version or problem/solution drift has been written to the canonical files or recorded as a blocking follow-up issue.
