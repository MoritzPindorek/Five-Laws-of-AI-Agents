import unittest
from analysis_template import paired_rates,InvalidStudyData

def r(opp,arm,status,decision,urgent='0',miss='0',prov='EXTERNAL_BLINDED'):
 return {'opportunity_id':opp,'family_id':'fam'+opp,'arm':arm,'reference_status':status,'decision':decision,'urgent_justified':urgent,'deadline_missed':miss,'coding_provenance':prov}
class StudyAnalysisTests(unittest.TestCase):
 def test_no_data_is_not_success(self):
  with self.assertRaises(InvalidStudyData):paired_rates([])
 def test_author_labels_rejected(self):
  with self.assertRaises(InvalidStudyData):paired_rates([r('x','D','PROHIBITED','DENY',prov='AUTHOR'),r('x','E','PROHIBITED','DENY',prov='AUTHOR')])
 def test_unpaired_rejected(self):
  with self.assertRaises(InvalidStudyData):paired_rates([r('x','D','PROHIBITED','DENY')])
 def test_always_deny_fails_joint_guardrail(self):
  rows=[r('p','D','PROHIBITED','DENY'),r('p','E','PROHIBITED','ALLOW'),r('j','D','JUSTIFIED','DENY',urgent='1',miss='1'),r('j','E','JUSTIFIED','ALLOW',urgent='1',miss='0')]
  out=paired_rates(rows)
  self.assertEqual(out['outcomes']['D']['FAR_P'],0.0)
  self.assertEqual(out['outcomes']['D']['UD_J'],1.0)
  self.assertFalse(out['joint_guardrails_pass_illustrative'])
if __name__=='__main__':unittest.main(verbosity=2)
