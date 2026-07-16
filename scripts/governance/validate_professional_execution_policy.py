#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[2]
POLICY=ROOT/"contracts/governance/professional-execution-policy-v1.json"
BUNDLE=ROOT/"contracts/governance/chat-startup-context-bundle-v1.json"
DOC=ROOT/"docs/governance/PROFESSIONAL_EXECUTION_PROMPT_STANDARD.md"
PROFILE_FIELDS={"profile_id","version","applicable_task_classes","required_roles","required_sources","required_preflight","required_acceptance","required_rollback","required_cleanup","destructive_action_policy","evidence_requirements","forbidden_shortcuts","stop_conditions"}
PROFILES={"SOFTWARE_ENGINEERING_REMEDIATION","PRODUCTION_INCIDENT_RECOVERY","REPOSITORY_CONSOLIDATION","SECURITY_REMEDIATION","INFRASTRUCTURE_AND_RUNNER_OPERATIONS","CLOUD_STORAGE_AND_INFORMATION_GOVERNANCE","DATABASE_AND_DATA_MIGRATION","UI_AND_DESIGN_SYSTEM","LEGAL_OR_FINANCIAL_DOCUMENT_PROCESSING","RESEARCH_AND_ARCHITECTURE"}
ATTEST={"PROFESSIONAL_EXECUTION_PROFILE_ACTIVATED","PROFESSIONAL_EXECUTION_PROFILE_ID","PROFESSIONAL_EXECUTION_PROFILE_VERSION","PROFESSIONAL_ROLES_LOADED","EXECUTION_CHARTER_CREATED","SOURCE_OF_TRUTH_RESOLVED","ROLLBACK_PLAN_PRESENT","CLEANUP_PLAN_PRESENT"}
PREFIX=["contracts/governance/owner-resource-authorization-v1.json","contracts/governance/professional-execution-policy-v1.json","docs/governance/ELEMENTARY_CHAT_CAPABILITY_BOOTSTRAP.md"]
LEGACY={"docs/governance/ELEMENTARY_CHAT_CAPABILITY_BOOTSTRAP.md","contracts/governance/owner-resource-authorization-v1.json","contracts/governance/canonical-software-runtime-inventory-v1.json","contracts/governance/chatgpt-plus-capability-profile-v1.json","contracts/governance/codex-capability-profile-v1.json","contracts/governance/memory-kernel-v1.json","contracts/governance/generated/startup-memory-hotset-v1.json","contracts/governance/generated/problem-solution-router-v1.json","contracts/governance/generated/problem-solution-index-v1.jsonl","contracts/governance/result-artifact-writeback-policy-v1.json","contracts/governance/result-artifact-registry-v1.jsonl","contracts/governance/generated/result-artifact-router-v1.json"}

def load(path:Path)->dict[str,Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def select(policy:dict[str,Any],task_class:str)->str:
    result=policy["selection"]["task_class_to_profile"].get(task_class)
    if not result: raise ValueError("PROFESSIONAL_PROFILE_NO_MATCH")
    return result

def gate(policy:dict[str,Any],a:dict[str,Any],task_class:str)->tuple[bool,str]:
    try: selected=select(policy,task_class)
    except ValueError: return False,"BLOCK_MUTATION:NO_PROFILE"
    if a.get("PROFESSIONAL_EXECUTION_PROFILE_ACTIVATED")!="PASS": return False,"BLOCK_MUTATION:PROFILE_NOT_ACTIVE"
    if a.get("PROFESSIONAL_EXECUTION_PROFILE_ID")!=selected: return False,"BLOCK_MUTATION:PROFILE_ID"
    if a.get("PROFESSIONAL_EXECUTION_PROFILE_VERSION")!=policy["version"]: return False,"BLOCK_MUTATION:PROFILE_VERSION"
    for field in ATTEST-{"PROFESSIONAL_EXECUTION_PROFILE_ACTIVATED","PROFESSIONAL_EXECUTION_PROFILE_ID","PROFESSIONAL_EXECUTION_PROFILE_VERSION","PROFESSIONAL_ROLES_LOADED"}:
        if a.get(field)!="PASS": return False,f"BLOCK_MUTATION:{field}"
    profile=next(x for x in policy["profiles"] if x["profile_id"]==selected)
    if not set(profile["required_roles"]).issubset(set(a.get("PROFESSIONAL_ROLES_LOADED",[]))): return False,"BLOCK_MUTATION:ROLES"
    return True,"PASS"

def validate()->None:
    p,b=load(POLICY),load(BUNDLE)
    assert p["schema"]=="elementary.professional-execution-policy.v1" and p["status"]=="ACTIVE"
    assert p["selection"]["generic_profile_allowed"] is False
    assert set(p["required_attestation_fields"])==ATTEST
    assert set(p["role_catalog"])=={"PSA","SSE","DPE","SRE","ASE","TA","RM","TPM"}
    ids=[x["profile_id"] for x in p["profiles"]]
    assert set(ids)==PROFILES and len(ids)==len(set(ids))
    for x in p["profiles"]:
        assert PROFILE_FIELDS.issubset(x)
        assert x["version"]==p["version"]
        assert set(x["required_roles"]).issubset(p["role_catalog"])
        assert x["destructive_action_policy"]["default"]=="DENY"
    pe=b["professional_execution"]
    assert pe["policy_ref"]==POLICY.relative_to(ROOT).as_posix()
    assert pe["required"] is True and pe["mode"]=="fail_closed"
    assert pe["mutation_gate"]=={"required_status":"PASS","on_failure":"BLOCK_MUTATION"}
    assert set(pe["required_attestation_fields"])==ATTEST
    assert ATTEST.issubset(b["required_startup_attestation_fields"])
    order=b["read_order"]; paths=[x["path"] for x in order]
    assert [x["order"] for x in order]==list(range(1,len(order)+1))
    assert paths[:3]==PREFIX and len(paths)==len(set(paths))
    assert LEGACY.issubset(paths) and paths.count(POLICY.relative_to(ROOT).as_posix())==1
    assert b["read_order_migration"]["all_preexisting_paths_preserved"] is True
    assert POLICY.relative_to(ROOT).as_posix() in b["transfer_packaging_rule"]["must_include_or_reference_files"]
    assert DOC.is_file()
    allowed,reason=gate(p,{},"repository_consolidation")
    assert not allowed and reason.startswith("BLOCK_MUTATION:")
    profile=next(x for x in p["profiles"] if x["profile_id"]=="REPOSITORY_CONSOLIDATION")
    a={"PROFESSIONAL_EXECUTION_PROFILE_ACTIVATED":"PASS","PROFESSIONAL_EXECUTION_PROFILE_ID":"REPOSITORY_CONSOLIDATION","PROFESSIONAL_EXECUTION_PROFILE_VERSION":p["version"],"PROFESSIONAL_ROLES_LOADED":profile["required_roles"],"EXECUTION_CHARTER_CREATED":"PASS","SOURCE_OF_TRUTH_RESOLVED":"PASS","ROLLBACK_PLAN_PRESENT":"PASS","CLEANUP_PLAN_PRESENT":"PASS"}
    assert gate(p,a,"repository_consolidation")== (True,"PASS")
    print("PROFESSIONAL_EXECUTION_POLICY=PASS")
    print("PROFESSIONAL_POLICY_IN_STARTUP_BUNDLE=PASS")
    print("PROFESSIONAL_POLICY_IN_READ_ORDER=PASS")
    print("BACKWARD_COMPATIBILITY=PASS")
    print("MUTATION_WITHOUT_PRO_PROFILE_BLOCKED=PASS")

if __name__=="__main__": validate()
