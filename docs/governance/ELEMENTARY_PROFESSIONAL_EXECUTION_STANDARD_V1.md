# ELEMENTARY Professional Execution Standard V1

**Status:** ACTIVE  
**Profile:** `REPOSITORY_CONSOLIDATION`  
**Canonical policy:** `contracts/governance/professional-execution-policy-v1.json`

## Purpose

This standard is the default execution profile for repository consolidation, governance, coding, review, validation, evidence, startup delivery and controlled release work across ELEMENTARY.

## Authority

```text
SOURCE_AND_RELEASE_TRUTH=GitHub main
LIFECYCLE_AND_ORCHESTRATION_AUTHORITY=ADCP
POLICY_AUTHORITY=ELEMENTARY Agent Governance
LOCAL_EXECUTION_AUTHORITY=existing BoCore governed paths
PRIMARY_REPOSITORY=borislavppetrov-beep/elementary-construction-os
STARTUP_REPOSITORY=borislavppetrov-beep/elementary-control-startup
```

The startup repository is a generated public mirror. It does not become an independent source of truth.

## Mandatory roles

Every admitted task must cover the following responsibilities, whether performed by one worker or several isolated workers:

1. repository architecture;
2. governance engineering;
3. delivery management;
4. security review;
5. schema and consumer impact review;
6. test and acceptance engineering;
7. release engineering;
8. evidence and cleanup ownership.

## Execution charter

Before mutation:

- read the complete startup bundle and every `read_order` file;
- bind the task to exact current `main`;
- inventory relevant repositories, open PRs and active execution lines;
- inspect schema and consumer impact;
- prove that no duplicate canonical mechanism is being introduced;
- define rollback, cleanup, validation and evidence ownership.

During mutation:

- never write directly to `main`;
- use one governed branch and one isolated worktree per admitted write task;
- preserve exact-base and exact-head identity;
- keep primary and startup repository changes in separate pull requests;
- do not weaken tests, approval gates, path scopes or evidence rules;
- do not expose secrets, private keys or raw environment dumps;
- do not create a second control plane, scheduler, dispatcher, registry, data spine or evidence authority.

Acceptance requires terminal exact-head checks, no unresolved review threads, rollback and cleanup evidence, result/artifact registration and a separate accepted startup PR whenever startup payload changes.

## Delivery truth integration

This policy does not create another delivery-state contract. It integrates with `elementary.operational-reality-audit.v1` when that contract is present on canonical `main`.

Until that contract is present and current, `RUNTIME_ACTIVE`, `E2E_VERIFIED` and `PRODUCTION_ACCEPTED` claims remain fail-closed and require exact immutable evidence from the existing capability, acceptance and result-artifact contracts. Source validation, merged code and historical runtime evidence do not prove current runtime or production acceptance.

## Startup delivery

The public startup mirror must be delivered through:

```text
PRIMARY_MAIN_CHANGE
  -> primary governed branch and PR
  -> validated payload build
  -> startup sync branch
  -> separate startup PR
  -> startup PR validation
  -> explicit merge under active authority
```

Direct pushes from the primary sync workflow to startup `main` are forbidden. Automatic startup PR merge is forbidden.

## Rollback and cleanup

- Source rollback: close or revert the governed PR without altering `main` directly.
- Startup rollback: close the startup PR or reset only the dedicated sync branch to startup `main`.
- Runtime or production rollback: use the separately governed runtime/deployment rollback contract.
- Retain only bounded evidence; remove private runner-temp data.
- Close or mark superseded stale PRs after a clean exact-main replacement is accepted.

## Required startup attestation

```text
PROFESSIONAL_EXECUTION_POLICY_LOADED=PASS
```
