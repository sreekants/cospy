#!/usr/bin/python
# Filename: test_IndividualRisk.py
# Description: Test cases for recording individual risk beside EL and P_HE (REQ.020)

import os, unittest

from tests.maritime.model.risk.test_ConcernWeights import source_module, CONFIG
from tests.examination import examine_pass
from cos.subsystem.data.Partition import AUDIT_FIELDS
from tests.maritime.model.risk.test_Rr import fields, report
from tests.maritime.model.risk.test_Encounters import examiner, Ctxt, RuleContext, Vessel

RiskModel		= source_module( 'rules.examiner.risk.RiskModel' )
NETWORK			= os.path.join( CONFIG, 'risk', 'risk.model.xdsl' )


class IndividualRiskTestCase(unittest.TestCase):
	def setUp(self):
		self.bn, self.engine	= RiskModel.load( NETWORK, RiskModel.HAZARDS )

	def marginal(self):
		return float( self.engine.posterior('harm_to_humans')[{'harm_to_humans': 'fatality'}] )

	def test_is_the_network_marginal(self):
		for evidence in ({}, {'humans_exposed': 'yes'}, {'humans_exposed': 'no'}):
			self.engine.setEvidence( evidence )
			self.engine.makeInference()
			ir	= RiskModel.individual_risk( self.engine )
			self.assertEqual( ir, self.marginal() )
			self.assertTrue( 0.0 <= ir <= 1.0 )

	def test_no_collision_records_zero_not_null(self):
		self.engine.setEvidence( {'collision': 'no'} )
		self.engine.makeInference()
		self.assertEqual( RiskModel.individual_risk(self.engine), 0.0 )

	def test_exposure_raises_it(self):
		self.engine.setEvidence( {'humans_exposed': 'yes'} ); self.engine.makeInference()
		exposed	= RiskModel.individual_risk( self.engine )
		self.engine.setEvidence( {'humans_exposed': 'no'} ); self.engine.makeInference()
		self.assertGreater( exposed, RiskModel.individual_risk(self.engine) )


class RecordTestCase(unittest.TestCase):
	def test_row_carries_all_three_baselines_in_declared_order(self):
		exam	= examiner()
		ctxt	= Ctxt()
		r		= report( {'safety': 1.0, 'traffic': 0.0, 'environmental': 0.0, 'operational': 0.0} )
		r['individual_risk']	= 0.0123
		exam.record( ctxt, r )

		row		= [ v for t, v in ctxt.sim.data.rows if t == 'fact_risk_assessment' ][0]
		names	= fields( 'fact_risk_assessment' )[AUDIT_FIELDS:]
		self.assertEqual( len(row), len(names) )
		values	= dict( zip(names, row) )
		self.assertEqual( values['individual_risk'], 0.0123 )
		self.assertEqual( values['p_any_hazard'], r['hazards']['any'] )
		self.assertEqual( values['rr'], r['cost'] )

	def test_assessment_uses_the_same_inference_as_cost(self):
		exam	= examiner()
		examine_pass( exam, Ctxt(), RuleContext([Vessel(1, 0, 0), Vessel(2, 50, 0)]) )
		r		= exam.reports[1]

		engine	= RiskModel.load( NETWORK, RiskModel.HAZARDS )[1]
		engine.setEvidence( r['evidence'] ); engine.makeInference()
		self.assertAlmostEqual( r['individual_risk'], RiskModel.individual_risk(engine), places=12 )


if __name__ == '__main__':
	unittest.main()
