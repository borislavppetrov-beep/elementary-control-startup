# ELEMENTARY Chat Startup Read Sequence

Every ELEMENTARY controlled chat, specialist chat, governed agent, transfer package and resume package must load the startup context bundle before reporting capabilities, runtime versions, repeated problem diagnoses or execution plans.

Canonical startup bundle:

```text
contracts/governance/chat-startup-context-bundle-v1.json
```

Mandatory startup read order:

```text
1. docs/governance/ELEMENTARY_CHAT_CAPABILITY_BOOTSTRAP.md
2. contracts/governance/owner-resource-authorization-v1.json
3. contracts/governance/canonical-software-runtime-inventory-v1.json
4. docs/governance/ELEMENTARY_ECOSYSTEM_LEARNING_LEDGER.md
5. contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl
```

Required startup attestation fields:

```text
CHAT_STARTUP_CONTEXT_BUNDLE_LOADED=true
CAPABILITY_BOOTSTRAP_LOADED=true
OWNER_RESOURCE_AUTHORIZATION_LOADED=true
CANONICAL_SOFTWARE_INVENTORY_LOADED=true
ECOSYSTEM_LEARNING_LEDGER_LOADED=true
PROBLEM_SOLUTION_LEDGER_LOADED=true
TRANSFER_PACKAGE_INSTRUCTS_NEW_CHAT_TO_READ_STARTUP_BUNDLE=true
```

A chat or agent must not claim that a capability is unavailable, must not guess a runtime version, and must not repeat a diagnosis for a known ecosystem problem until this startup bundle and the ledger have been checked.

## Transfer packaging rule

Whenever an active chat is packaged, rolled over, transferred or resumed in a new chat, the generated transfer package must include an explicit instruction for the new chat:

```text
Before continuing work, read contracts/governance/chat-startup-context-bundle-v1.json and then read all files in its read_order. Confirm the required startup attestation fields before capability claims, runtime-version claims, repeated-problem diagnoses or execution.
```

The package must include or reference:

```text
contracts/governance/chat-startup-context-bundle-v1.json
docs/governance/ELEMENTARY_CHAT_CAPABILITY_BOOTSTRAP.md
contracts/governance/owner-resource-authorization-v1.json
contracts/governance/canonical-software-runtime-inventory-v1.json
docs/governance/ELEMENTARY_ECOSYSTEM_LEARNING_LEDGER.md
contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl
```

A transfer package is invalid if it omits the startup bundle instruction or fails to preserve the startup read order.

When any of the startup files changes, the next transfer/resume package must cite the new file state and include the startup attestation.
