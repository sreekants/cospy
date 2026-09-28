#!/usr/bin/python
# Filename: test_Encounters.py
# Description: Test cases for per-vessel risk evidence (COS.008)

import os, unittest

import numpy as np
import yaml

from tests.maritime.model.risk.test_ConcernWeights import source_module, CONFIG
from tests.maritime.model.risk.test_Rb import Ctxt as RbCtxt

RiskExaminer	= source_module( 'rules.examiner.risk.RiskExaminer' ).RiskExaminer
RiskModel		= source_module( 'rules.examiner.risk.RiskModel' )

PAIR_NODES		= { 'dcpa', 'tcpa', 'target_on_collision', 'size_other_vessel', 'humans_present' }


class Vessel:
	def __init__(self, imo, x, y):
		self.id			= f'v{imo}'
		self.name		= f'Vessel {imo}'
		self.location	= np.array( (float(x), float(y), 0.0) )
		self.config		= { 'identifier': { 'imo': imo } }


class RuleContext:
	""" Resolves terms from the positions of situation.os and situation.ts """
	def __init__(self, vessels, subjects=None):
		self.vessels	= vessels
		self.subjects	= subjects if subjects is not None else vessels
		self.situation	= 'shared'
		self.resolver	= None
		self.size		= 'large'

	def resolve(self, term):
		os, ts	= self.situation.os, self.situation.ts
		own		= { '(OwnShip,Map.Sea).WaveHeight': 1.0, '(OwnShip,Map.Sea).WindSpeed': 5.0,
					'(OwnShip,Map.Sea).Depth': 50.0, '(OwnShip,Map.Land).Distance': 300.0,
					'(OwnShip,Map.Land).OnGroundingCourse': False }
		if term in own:
			return own[term] if os is not None else None
		if ts is None:
			return None

		distance	= float( np.linalg.norm(os.location - ts.location) )
		pair		= { '(OwnShip,TargetShip).DCPA': distance, '(OwnShip,TargetShip).TCPA': 20.0,
						'(OwnShip,TargetShip).OnCollisionCourse': distance < 100.0,
						'TargetShip.RelativeSize': self.size, 'TargetShip.PersonsOnBoard': 20 }
		return pair.get( term )


class Spatial:
	order	= ['open_sea']
	def classify(self, shapes):
		return 'open_sea'


class Matrix:
	""" Rl stand-in: loss proportional to each hazard's posterior """
	def row(self, engine, zone):
		return { h: 1.0e6 * float(engine.posterior(h)[{h: 'yes'}]) for h in RiskModel.HAZARDS }
	def matlab(self, engine, order):
		return '[0];'


class Ctxt(RbCtxt):
	def __init__(self):
		RbCtxt.__init__( self )
		self.sim.now	= lambda: '2026-09-25 12:00:00'
		self.sim.seconds	= lambda: 43200.0


class Always:
	def signaled(self):
		return True


def examiner():
	exam			= RiskExaminer()
	exam.bn, exam.engine	= RiskModel.load( os.path.join(CONFIG, 'risk', 'risk.model.xdsl'), RiskModel.HAZARDS )
	with open( os.path.join(CONFIG, 'risk', 'risk.model.yaml') ) as f:
		risk		= yaml.safe_load( f )['risk']
	for group in exam.bindings:
		exam.bindings[group]	= [ RiskModel.Binding(b) for b in risk.get(group, []) ]
	exam.survey		= lambda vessel: ( [], None, None )
	exam.spatial	= Spatial()
	exam.matrix		= Matrix()
	exam.timer		= Always()
	exam.reports	= {}
	exam.publish	= lambda ctxt, vessel, report: exam.reports.__setitem__( int(report['imo']), report )	# keyed by guid since COS-029-02
	return exam


class EncounterTestCase(unittest.TestCase):
	def run_pass(self, vessels, subjects=None, size='large', errors=0):
		exam		= examiner()
		rule_ctxt	= RuleContext( vessels, subjects )
		rule_ctxt.size	= size
		ctxt		= Ctxt()
		exam.evaluate( ctxt, rule_ctxt )
		exam.evaluate( ctxt, rule_ctxt )
		self.assertEqual( len(ctxt.log.errors), errors, ctxt.log.errors )
		self.assertEqual( rule_ctxt.situation, 'shared' )
		return exam.reports

	def test_vessels_in_different_situations_get_different_rows(self):
		reports	= self.run_pass( [Vessel(1, 0, 0), Vessel(2, 50, 0), Vessel(3, 20000, 0)] )

		self.assertEqual( sorted(reports), [1, 2, 3] )
		self.assertEqual( reports[1]['target'], 'v2' )
		self.assertEqual( reports[2]['target'], 'v1' )
		self.assertIsNone( reports[3]['target'] )
		self.assertGreater( reports[1]['hazards']['collision'], reports[3]['hazards']['collision'] )
		self.assertNotEqual( reports[1]['cost'], reports[3]['cost'] )

	def test_vessel_with_no_encounter_has_no_pair_evidence(self):
		reports	= self.run_pass( [Vessel(1, 0, 0), Vessel(2, 50, 0), Vessel(3, 20000, 0)] )

		self.assertFalse( PAIR_NODES & set(reports[3]['evidence']) )
		self.assertTrue( PAIR_NODES <= set(reports[1]['evidence']) )

	def test_encounter_cost_is_invariant_to_bystanders(self):
		pair		= lambda: [ Vessel(1, 0, 0), Vessel(2, 50, 0) ]
		alone		= self.run_pass( pair() )
		crowded		= self.run_pass( pair() + [ Vessel(10 + n, 20000 + 1000*n, 0) for n in range(5) ] )

		for imo in (1, 2):
			self.assertAlmostEqual( alone[imo]['cost'], crowded[imo]['cost'] )
			self.assertAlmostEqual( alone[imo]['cumulative'], crowded[imo]['cumulative'] )

	def test_worst_encounter_is_charged(self):
		reports	= self.run_pass( [Vessel(1, 0, 0), Vessel(2, 3000, 0), Vessel(3, 40, 0)], subjects=None )
		self.assertEqual( reports[1]['target'], 'v3' )

	def test_predicates_become_yes_no(self):
		reports	= self.run_pass( [Vessel(1, 0, 0), Vessel(2, 50, 0)] )
		self.assertEqual( reports[1]['evidence']['target_on_collision'], 'yes' )
		self.assertEqual( reports[1]['evidence']['vessel_on_grounding'], 'no' )

	def test_unknown_state_is_left_unobserved_and_logged_once(self):
		reports	= self.run_pass( [Vessel(1, 0, 0), Vessel(2, 50, 0)], size='huge', errors=1 )
		self.assertNotIn( 'size_other_vessel', reports[1]['evidence'] )
		self.assertIn( 'dcpa', reports[1]['evidence'] )

	def test_vessels_sharing_an_imo_keep_separate_tracks(self):
		twin		= Vessel(1, 20000, 0)
		twin.id		= 'twin'
		exam		= examiner()
		exam.evaluate( Ctxt(), RuleContext([Vessel(1, 0, 0), Vessel(2, 50, 0), twin]) )
		self.assertEqual( sorted(exam.tracks), ['twin', 'v1', 'v2'] )
		self.assertEqual( exam.tracks['v1'].charges, 1 )

	def test_only_subjects_are_assessed(self):
		vessels	= [ Vessel(1, 0, 0), Vessel(2, 50, 0) ]
		reports	= self.run_pass( vessels, subjects=vessels[:1] )
		self.assertEqual( list(reports), [1] )
		self.assertEqual( reports[1]['target'], 'v2' )


if __name__ == '__main__':
	unittest.main()
