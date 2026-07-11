# ELEMENTARY Ecosystem Learning Ledger

This is the canonical problem/solution memory for ELEMENTARY chats, governed agents and controlled transfer/resume packages.

It exists because chat text alone is not a durable operational memory. Future chats and agents must use this ledger to avoid rediscovering the same capability boundaries, runner behavior, service paths, failure modes and repairs.

## Canonical machine-readable ledger

```text
contracts/governance/ecosystem-problem-solution-ledger-v1.jsonl
```

Each line is one JSON object with this minimum shape:

```json
{
  "schema": "elementary.ecosystem-problem-solution-ledger.entry.v1",
  "id": "stable-entry-id",
  "status": "OPEN|RESOLVED|MITIGATED|SUPERSEDED",
  "scope": ["area"],
  "problem": "Short exact problem statement",
  "evidence": ["issue/PR/run/artifact/file references"],
  "root_cause": "Known or UNVERIFIED",
  "solution": "Implemented or planned resolution",
  "next_action": "Exact next action when not resolved",
  "canonical_files": ["paths updated or requiring update"]
}
```

## Mandatory usage rule

Every ELEMENTARY chat, specialist chat, governed agent, workflow or transfer/resume package that encounters a material problem must do one of the following before claiming the problem is solved:

1. append or update the ledger entry with the problem, evidence, root cause and resolution;
2. cite the existing ledger entry and update it if the facts changed;
3. create a blocking GitHub issue if the current chat cannot write to the ledger.

It is forbidden to leave operational lessons only in chat text.

## What belongs here

Record:

- connector capability changes;
- indirect capability discoveries;
- runner queue/capacity failures;
- WSL/PowerShell/Windows interop behavior;
- browser bridge/CDP failures and fixes;
- GitHub Projects V2 access and mutation path facts;
- cPanel/production runtime gotchas;
- workflow design mistakes and corrections;
- failed assumptions;
- exact artifacts proving failures or repairs;
- workaround status and final fix status.

Do not record:

- secret values;
- raw environment dumps;
- passwords, tokens, cookies or browser profiles;
- personal data unrelated to project operation;
- speculative conclusions without evidence.

## Current seed from July 2026 autonomy work

The initial seed captures the verified lessons from Issues #551, #553, #555, PR #552, PR #554, PR #556 and earlier autonomy/BoCore/PR313 work:

- visible chat connectors are not the full capability boundary;
- GitHub Projects V2 access is real through secret-backed governed workflows;
- BoCore has self-hosted runner lanes under ADCP governance:
  - `github-actions-runner-01` on machine `BoCore`, labels include `self-hosted,Linux,X64,elementary-ci`;
  - `github-actions-runner-02`, WSL/Linux capacity relief lane, labels include `self-hosted,Linux,X64,elementary-ci,elementary-ci-fast,elementary-governance`;
  - `github-actions-runner-03-windows`, Windows-native extended lane, labels include `self-hosted,Windows,X64,elementary-bocore-windows,elementary-bocore-extended,elementary-service-channel`;
- `github-actions-runner-03-windows` is operational in scheduled-task background mode through `\ELEMENTARY\GitHub Runner 03 Windows` with log `C:\ELEMENTARY\LocalRunner\logs\runner03-scheduled.log`;
- direct WSL execution of Windows `.exe` files currently fails with `Invalid argument` on the original Linux runner despite visible Windows filesystem and `WSL_INTEROP` evidence;
- the correct path for Windows-only commands is the Windows-native runner lane or a Windows-side governed service channel, not arbitrary WSL `.exe` workarounds;
- PR313 bridge workflows must not globally trigger on unrelated pull requests;
- production cPanel has PHP/Composer but no Node/npm/npx runtime;
- new or changed capabilities/versions must be written to canonical files or blocking issues.

## Transfer/resume requirement

Every controlled chat transfer package must include or reference this ledger, in addition to:

```text
docs/governance/ELEMENTARY_CHAT_CAPABILITY_BOOTSTRAP.md
contracts/governance/owner-resource-authorization-v1.json
contracts/governance/canonical-software-runtime-inventory-v1.json
```

The resume attestation must state whether any newly observed problem/solution drift was written to the ledger or captured as a blocking follow-up issue.
