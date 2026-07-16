from __future__ import annotations
import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("v",ROOT/"scripts/governance/validate_professional_execution_policy.py")
assert spec and spec.loader
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.p=v.load(v.POLICY)
 def test_missing_blocks(self): self.assertFalse(v.gate(self.p,{},"repository_consolidation")[0])
 def test_unknown_blocks(self):
  with self.assertRaises(ValueError): v.select(self.p,"unknown")
 def test_deterministic(self): self.assertEqual(v.select(self.p,"repository_consolidation"),"REPOSITORY_CONSOLIDATION")
 def test_wrong_profile_blocks(self):
  self.assertEqual(v.gate(self.p,{"PROFESSIONAL_EXECUTION_PROFILE_ACTIVATED":"PASS","PROFESSIONAL_EXECUTION_PROFILE_ID":"RESEARCH_AND_ARCHITECTURE","PROFESSIONAL_EXECUTION_PROFILE_VERSION":"1.0.0"},"repository_consolidation")[1],"BLOCK_MUTATION:PROFILE_ID")
 def test_complete_passes(self):
  x=next(x for x in self.p["profiles"] if x["profile_id"]=="REPOSITORY_CONSOLIDATION")
  a={"PROFESSIONAL_EXECUTION_PROFILE_ACTIVATED":"PASS","PROFESSIONAL_EXECUTION_PROFILE_ID":"REPOSITORY_CONSOLIDATION","PROFESSIONAL_EXECUTION_PROFILE_VERSION":"1.0.0","PROFESSIONAL_ROLES_LOADED":x["required_roles"],"EXECUTION_CHARTER_CREATED":"PASS","SOURCE_OF_TRUTH_RESOLVED":"PASS","ROLLBACK_PLAN_PRESENT":"PASS","CLEANUP_PLAN_PRESENT":"PASS"}
  self.assertEqual(v.gate(self.p,a,"repository_consolidation"),(True,"PASS"))
if __name__=="__main__": unittest.main()
