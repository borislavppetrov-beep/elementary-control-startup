# ELEMENTARY Chat Startup Read Sequence

Every ELEMENTARY controlled chat, specialist chat, governed agent, Codex task, transfer package and resume package must load the startup context bundle before reporting capabilities, runtime versions, Codex state, repeated problem diagnoses, result claims or execution plans.

Canonical startup bundle:

```text
contracts/governance/chat-startup-context-bundle-v1.json
```

Mandatory startup read order:

```text
1. docs/governance/ELEMENTARY_CHAT_CAPABILITY_BOOTSTRAP.md
2. contracts/governance/owner-resource-authorization-v1.json
3. contracts/governance/canonical-software-runtime-inventory-v1.json
4. contracts/governance/codex-capability-profile-v1.json
5. contracts/governance/memory-kernel-v1.json
6. contracts/governance/generated/startup-memory-hotset-v1.json
7. contracts/governance/generated/problem-solution-router-v1.json
8. contracts/governance/generated/problem-solution-index-v1.jsonl
9. contracts/governance/result-artifact-writeback-policy-v1.json
10. contracts/governance/result-artifact-registry-v1.jsonl
11. contracts/governance/generated/result-artifact-router-v1.json
```

For Codex repository work, `AGENTS.md` is additionally mandatory and must be obeyed.

Required startup attestation fields include:

```text
CHAT_STARTUP_CONTEXT_BUNDLE_LOADED=PASS
CAPABILITY_BOOTSTRAP_LOADED=PASS
OWNER_RESOURCE_AUTHORIZATION_LOADED=PASS
CANONICAL_SOFTWARE_INVENTORY_LOADED=PASS
CODEX_CAPABILITY_PROFILE_LOADED=PASS
MEMORY_KERNEL_LOADED=PASS
STARTUP_MEMORY_HOTSET_LOADED=PASS
PROBLEM_SOLUTION_ROUTER_LOADED=PASS
PROBLEM_SOLUTION_INDEX_LOADED=PASS
RESULT_ARTIFACT_WRITEBACK_POLICY_LOADED=PASS
RESULT_ARTIFACT_REGISTRY_LOADED=PASS
RESULT_ARTIFACT_ROUTER_LOADED=PASS
LIVE_GITHUB_SOURCE_OF_TRUTH_CHECKED=PASS
RUNTIME_INVENTORY_CHECKED_BEFORE_VERSION_CLAIM=PASS
CODEX_RUNTIME_READBACK_CHECKED_BEFORE_RUNTIME_CLAIM=PASS
RESULT_ARTIFACT_WRITEBACK_CHECKED_BEFORE_RESULT_CLAIM=PASS
TRANSFER_PACKAGE_INSTRUCTS_NEW_CHAT_TO_READ_STARTUP_BUNDLE=PASS
```

A chat or agent must not claim that a capability is unavailable, guess a runtime version, collapse Codex product availability into runtime activation, repeat a known diagnosis or claim a durable result until the required startup sources have been checked.

## Transfer packaging rule

Whenever an active chat is packaged, rolled over, transferred or resumed in a new chat, the generated package must explicitly instruct the receiving chat to read the live startup bundle and its complete `read_order`. For Codex work it must also reference `AGENTS.md`.

A transfer package is invalid if it omits the startup instruction, fails to preserve the read order, omits the Codex profile when Codex is involved, or omits result/artifact writeback requirements.

When any startup file changes, the next transfer/resume package must cite the new state and include the current startup attestation.
