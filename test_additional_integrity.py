"""Additional fixtures: tests are self-checks, not security or moral validation."""
import unittest
from dataclasses import replace
from reference_gate import Gateway, Mandate, Proposal, Judgments, Tri, Verdict
from analysis_template import paired_rates, InvalidStudyData

def mandate(**opts):
    d=dict(mandate_id='M',principal='clinic',agent='a',tools=frozenset({'read'}),purposes=frozenset({'audit'}),subjects=frozenset({'s'}),resource_budget=100,valid_from=0,expires_at=100,epoch=1)
    d.update(opts); return Mandate(**d)

GOOD=Judgments(*(Tri.YES,)*5)
def q(id='q', **kw):
    d=dict(id=id,agent='a',tool='read',purpose='audit',subject='s',cost=1,when=5,policy_epoch=1,judgments=GOOD)
    d.update(kw); return Proposal(**d)

def r(id, arm, status, decision, urgent='0',miss='0'):
    return dict(opportunity_id=id,family_id='family',reference_status=status,urgent_justified=urgent,deadline_missed=miss,arm=arm,decision=decision,coding_provenance='EXTERNAL_BLINDED')

class GatewayFixtureChecks(unittest.TestCase):
    def test_fake_client_timestamp_rejected(self):
        g=Gateway(mandate(),clock=lambda:5)
        self.assertEqual(g.submit(q(when=6))[1],'UNTRUSTED_TIMESTAMP')
        self.assertEqual(g.tool.effects,[])
    def test_clock_expired_even_if_client_time_valid(self):
        g=Gateway(mandate(),clock=lambda:101)
        self.assertEqual(g.submit(q())[1],'TIME_OUT_OF_SCOPE')
    def test_invalid_budget_rejected(self):
        with self.assertRaises(ValueError):mandate(resource_budget=-1)
        with self.assertRaises(ValueError):mandate(resource_budget=True)
    def test_invalid_mandate_window(self):
        with self.assertRaises(ValueError):mandate(valid_from=50,expires_at=50)
    def test_budget_is_not_float_or_boolean(self):
        g=Gateway(mandate())
        self.assertEqual(g.submit(q(cost=1.5))[0],Verdict.DENY)
        self.assertEqual(g.submit(q('q2',cost=True))[0],Verdict.DENY)
        self.assertEqual(g.spent,0)
    def test_control_update_is_logged_but_not_authenticated(self):
        g=Gateway(mandate())
        g.set_mandate(mandate(epoch=2))
        self.assertTrue(g.verify_history())
        self.assertEqual(g.reconstruct()['control_events'],1)
        self.assertEqual(g.submit(q('stale'))[1],'REVOKED_OR_STALE_EPOCH')
    def test_known_in_process_token_bypass_is_demonstrated_not_hidden(self):
        """Proof this mock is NOT a real isolated security monitor."""
        g=Gateway(mandate())
        # A hostile in-process caller can inspect this Python object (NOT real authentication).
        g.tool.apply(q('bypass'),g.tool._token)
        self.assertEqual(len(g.tool.effects),1)
        self.assertEqual(len(g.events),0)  # unmediated effect; expected known weakness

    def test_trace_context_is_bound_to_hash(self):
        g=Gateway(mandate()); g.submit(q())
        self.assertIn('proposal_digest',g.events[0]); self.assertTrue(g.verify_history())
        g.events[0]['proposal_digest']='0'*64
        self.assertFalse(g.verify_history())

class MethodologyChecks(unittest.TestCase):
    def test_review_before_deadline_is_not_automatically_wrongful_denial(self):
        rows=[r('p','D','PROHIBITED','DENY'),r('p','E','PROHIBITED','ALLOW'),
              r('j','D','JUSTIFIED','REVIEW',miss='0'),r('j','E','JUSTIFIED','ALLOW',miss='0')]
        a=paired_rates(rows)
        self.assertEqual(a['outcomes']['D']['UD_J'],0)
        self.assertEqual(a['outcomes']['D']['immediate_nonrelease_J'],1)
    def test_review_after_deadline_counts_as_failure(self):
        rows=[r('p','D','PROHIBITED','DENY'),r('p','E','PROHIBITED','ALLOW'),
              r('j','D','JUSTIFIED','REVIEW',miss='1'),r('j','E','JUSTIFIED','ALLOW',miss='0')]
        self.assertEqual(paired_rates(rows)['outcomes']['D']['UD_J'],1)
    def test_bad_binary_deadline_rejected(self):
        rows=[r('p','D','PROHIBITED','DENY',miss='missing'),r('p','E','PROHIBITED','ALLOW'),
              r('j','D','JUSTIFIED','ALLOW'),r('j','E','JUSTIFIED','ALLOW')]
        with self.assertRaises(InvalidStudyData):paired_rates(rows)
    def test_reference_conflict_rejected(self):
        rows=[r('p','D','PROHIBITED','DENY',urgent='1'),r('p','E','PROHIBITED','ALLOW',urgent='1'),
              r('j','D','JUSTIFIED','ALLOW'),r('j','E','JUSTIFIED','ALLOW')]
        with self.assertRaises(InvalidStudyData):paired_rates(rows)
    def test_insufficient_cases_retained_but_excluded_from_confirmatory_denominator(self):
        rows=[r('p','D','PROHIBITED','DENY'),r('p','E','PROHIBITED','ALLOW'),
              r('j','D','JUSTIFIED','ALLOW'),r('j','E','JUSTIFIED','ALLOW'),
              r('u','D','INSUFFICIENT','REVIEW'),r('u','E','INSUFFICIENT','REVIEW')]
        out=paired_rates(rows)
        self.assertEqual(out['insufficient'],1)
        self.assertEqual(out['outcomes']['D']['n_prohibited'],1)

    def test_external_label_marker_is_not_proof_of_blinding(self):
        rows=[r('p','D','PROHIBITED','DENY'),r('p','E','PROHIBITED','ALLOW'),
              r('j','D','JUSTIFIED','ALLOW'),r('j','E','JUSTIFIED','ALLOW')]
        self.assertFalse(paired_rates(rows)['confirmatory_evidence'])
        self.assertFalse(paired_rates(rows)['noninferiority_demonstrated'])

if __name__=='__main__': unittest.main(verbosity=2)
