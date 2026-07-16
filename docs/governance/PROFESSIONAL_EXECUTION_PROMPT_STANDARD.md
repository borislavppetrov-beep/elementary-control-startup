# ELEMENTARY Professional Execution Prompt Standard

**Status:** ACTIVE  
**Policy:** `contracts/governance/professional-execution-policy-v1.json`  
**Mode:** fail-closed  
**Authority:** ELEMENTARY Agent Governance / ADCP  
**Incremental licence budget:** 0 €

Before consequential analysis, capability status, architecture decisions or any mutation, select the most specific registered profile, load its required roles through `role_catalog`, create the full execution charter and attest:

```text
PROFESSIONAL_EXECUTION_PROFILE_ACTIVATED=PASS
PROFESSIONAL_EXECUTION_PROFILE_ID=<registered profile>
PROFESSIONAL_EXECUTION_PROFILE_VERSION=1.0.0
PROFESSIONAL_ROLES_LOADED=<all required role ids>
EXECUTION_CHARTER_CREATED=PASS
SOURCE_OF_TRUTH_RESOLVED=PASS
ROLLBACK_PLAN_PRESENT=PASS
CLEANUP_PLAN_PRESENT=PASS
```

No match, ambiguous match, generic substitution, incomplete roles, missing charter, source drift, missing rollback or missing cleanup means `BLOCK_MUTATION`.

Valid delivery states are independent: `ACCEPTED`, `CONTRACTED`, `IMPLEMENTED`, `PROVISIONED`, `RUNTIME_ACTIVE`, `VISIBLE`, `E2E_VERIFIED`, `PRODUCTION_ACCEPTED`. Source, merge, test, preview or rollback-to-disabled evidence cannot substitute for a later state.

Direct `main` writes, force-push, unbounded shell, secret/private-key output, raw environment dumps and unbounded destructive actions are forbidden. Temporary work requires owner, purpose, TTL, deletion condition and cleanup proof.

Validation:

```text
python scripts/governance/validate_professional_execution_policy.py
python -m unittest tests.governance.test_professional_execution_policy
```
