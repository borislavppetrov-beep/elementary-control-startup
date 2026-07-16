# ELEMENTARY Professional Execution Prompt Standard

## Status

```text
STANDARD=ACTIVE
POLICY=contracts/governance/professional-execution-policy-v1.json
PROFILE_CATALOG=contracts/governance/professional-execution-profile-catalog-v1.json
SOURCE_OF_TRUTH=live GitHub main
CONTROL_PLANE=ELEMENTARY ADCP
POLICY_AUTHORITY=ELEMENTARY Agent Governance
```

This document is the human-readable companion to the machine-readable professional execution policy. It does not create a second startup mechanism, scheduler, dispatcher, evidence authority or control plane.

## Mandatory activation

Before any architecture decision, code mutation, workflow mutation, repository mutation, production mutation, server mutation, cloud-storage mutation, destructive action, security-sensitive action or data migration:

1. Read the complete live startup bundle and its complete `read_order`.
2. Select the exact specialized profile from the canonical catalog.
3. Load every source and contract required by that profile.
4. Create the execution charter.
5. Prove the required attestation.
6. Block mutation when any proof is missing, stale or inconsistent.

A generic profile is prohibited when a specialized profile applies. Unknown profiles fail closed.

## Required attestation

```text
PROFESSIONAL_EXECUTION_PROFILE_ACTIVATED=PASS
PROFESSIONAL_EXECUTION_PROFILE_ID=<exact catalog id>
PROFESSIONAL_EXECUTION_PROFILE_VERSION=<exact catalog version>
PROFESSIONAL_ROLES_LOADED=<non-empty exact role set>
EXECUTION_CHARTER_CREATED=PASS
SOURCE_OF_TRUTH_RESOLVED=PASS
ROLLBACK_PLAN_PRESENT=PASS
CLEANUP_PLAN_PRESENT=PASS
```

Missing, malformed or non-PASS fields produce:

```text
MUTATION_GATE=BLOCK_MUTATION
```

## Execution charter

The charter must identify:

- exact task;
- source of truth;
- in-scope and out-of-scope actions;
- acceptance criteria;
- stop conditions;
- mutation and destructive-action policy;
- rollback policy;
- evidence policy;
- cleanup policy;
- temporary-file policy;
- conflict and overlap policy;
- exact-main binding;
- delivery-truth policy.

An unstructured chat intention is not an execution charter.

## Canonical profile selection

Use the most specific matching profile:

- `SOFTWARE_ENGINEERING_REMEDIATION`
- `PRODUCTION_INCIDENT_RECOVERY`
- `REPOSITORY_CONSOLIDATION`
- `SECURITY_REMEDIATION`
- `INFRASTRUCTURE_AND_RUNNER_OPERATIONS`
- `CLOUD_STORAGE_AND_INFORMATION_GOVERNANCE`
- `DATABASE_AND_DATA_MIGRATION`
- `UI_AND_DESIGN_SYSTEM`
- `LEGAL_OR_FINANCIAL_DOCUMENT_PROCESSING`
- `RESEARCH_AND_ARCHITECTURE`

`REPOSITORY_CONSOLIDATION` is mandatory for repository-wide inventory, workflow consolidation, code cleanup and delivery-truth recovery.

## Delivery truth

Track these states independently:

```text
ACCEPTED
CONTRACTED
IMPLEMENTED
PROVISIONED
RUNTIME_ACTIVE
VISIBLE
E2E_VERIFIED
PRODUCTION_ACCEPTED
```

A source contract, implementation, merge, CI run, preview, dry-run or isolated acceptance does not prove `RUNTIME_ACTIVE` or `PRODUCTION_ACCEPTED`.

`RUNTIME_ACTIVE` requires all of:

```text
EXACT_CURRENT_MAIN_BINDING=PASS
LIVE_RUNTIME_PRESENT=true
LIVE_RUNTIME_ENABLED=true
FRESH_HEALTH_READBACK=PASS
ROLLBACK_DISABLED_STATE=false
E2E_OPERATION_EXECUTED=PASS
EVIDENCE_RECONCILED=PASS
```

Acceptance followed by rollback to disabled is not active. A weighted completion percentage is forbidden without a published machine-readable acceptance matrix and explicit weights.

## Repository mutation rules

- No direct write to `main`.
- No force push.
- No stale-head merge.
- No reuse of CI from an older head.
- No second control plane.
- No second startup or professional-profile mechanism.
- No new validator when the canonical validator can be extended.
- No new workflow for each individual defect.
- No production mutation from a source PR.
- Use exact-head validation and expected-head merge.
- Record rollback, cleanup and terminal evidence.
- Close operational request PRs without merge when their evidence-trigger role is complete.

## Destructive actions

Destructive actions default to prohibited. They require separate exact-batch authority, dependency and retention clearance, recovery proof, rollback, independent verification and post-action audit. Historical evidence must not be deleted merely because it is no longer active source.

## Failure behavior

Fail closed only for the affected scope. Record sanitized evidence and continue independent read-only or path-disjoint work. Never fabricate PASS, collapse delivery states or claim live activation from source evidence.
