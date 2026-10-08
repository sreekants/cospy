#!/usr/bin/python
# Filename: test_CollisionExaminer.py
# Description: Test cases for the CollisionExaminer class

import unittest

from rules.examiner.navigation.CollisionExaminer import CollisionExaminer
from cos.model.rule.Situation import Situation
from cos.core.utilities.ArgList import ArgList
from tests.maritime.model.zone.test_Ledger import Ctxt, Shape, Vessel
from tests.rules.examiner.navigation.test_ExtremeWeatherExaminer import Posts


class Encounter:
	""" Rule context for one pair, with the DCPA given """
	def __init__(self, own, target, dcpa):
		self.situation	= Situation( own, target )
		self.dcpa		= dcpa
	def resolve(self, term):
		return self.dcpa if term.endswith( 'DCPA' ) else 30.0


class CollisionEpochTestCase(unittest.TestCase):
	def setUp(self):
		self.ctxt	= Ctxt( [Shape('Turkeli.Strait', 'STRAIT')] )
		self.ctxt.ipc	= Posts()
		self.exam	= CollisionExaminer()
		self.exam.id, self.exam.callbacks	= 'Collision', {}
		self.exam.setup( self.ctxt, {'zones': None, 'territory': None, 'report.dcpa': '500'} )
		self.exam.cache_shapes( self.ctxt )
		self.own, self.target	= Vessel( 1 ), Vessel( 2 )

	def approach(self, dcpas):
		""" Judges the pair once per tick, ending each pass as the evaluator does; None skips the pair """
		for dcpa in dcpas:
			if dcpa is not None:
				self.exam.judge( self.ctxt, Encounter(self.own, self.target, dcpa) )
			self.exam.end( self.ctxt, None )
			self.ctxt.sim.advance( 1 )

	def epochs(self):
		return [ p for t, m, p in self.ctxt.ipc.posts if m == CollisionExaminer.EPOCH_MESSAGE ]

	def test_an_approach_under_report_dcpa_is_one_epoch_with_its_closest_point(self):
		self.approach( [800, 400, 300, 200, 350, 700] )
		epochs	= self.epochs()
		self.assertEqual( len(epochs), 1 )
		self.assertEqual( (epochs[0]['own'], epochs[0]['target'], epochs[0]['threshold']), ('1', '2', 500.0) )
		self.assertEqual( (epochs[0]['epoch']['peak'], epochs[0]['epoch']['samples']), (200, 4) )
		self.assertEqual( epochs[0]['epoch']['peak_at'] - epochs[0]['epoch']['start'], 2 )

	def test_findings_are_unchanged(self):
		self.approach( [400, 300, 200, 700] )
		self.assertEqual( [ r[1][8] for r in self.ctxt.sim.data.rows if r[0] == 'fact_ro' ], ['collision.cost'] )

	def test_a_pair_no_longer_in_an_encounter_ends_its_epoch(self):
		self.approach( [400, 300, None] )
		self.assertEqual( [ e['epoch']['reason'] for e in self.epochs() ], ['lapsed'] )

	def test_no_report_dcpa_means_no_watcher(self):
		exam	= CollisionExaminer()
		exam.id, exam.callbacks	= 'Collision', {}
		exam.setup( self.ctxt, ArgList('') )
		self.assertIsNone( exam.watcher )


class CollisionExaminerTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

if __name__ == '__main__':
    unittest.main()
