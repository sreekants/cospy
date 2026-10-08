#!/usr/bin/python
# Filename: test_ExtremeWeatherExaminer.py
# Description: Test cases for the ExtremeWeatherExaminer class: its inputs and fact_capsize (COS.043)

import types, unittest

import numpy as np

from tests.maritime.model.risk.test_ConcernWeights import source_module, CONFIG
from tests.examination import examine, examine_subjects, end_epoch

import os
from tests.maritime.model.zone.test_Ledger import Ctxt, Shape, IPC
from tests.maritime.model.zone.test_Practice import RuleContext
from cos.core.kernel.Object import TERM_WRITE

ExtremeWeatherExaminer	= source_module( 'rules.examiner.navigation.ExtremeWeatherExaminer' ).ExtremeWeatherExaminer
VesselModel				= source_module( 'cos.behavior.motion.VesselModel' ).VesselModel

FOG, CLEAR	= 0.27, 15.0			# Visibility of the foggy and clear-sky profiles, nautical miles
FIELDS		= 13					# fact_capsize fields after the four audit fields


class Field:
	""" A SEA_WAVE field giving the same wave everywhere """
	def __init__(self, hs):
		self.hs	= hs
	def at(self, x, y):
		return np.array( (self.hs, 0.0, 0.0) )


def model(name):
	""" A ship model from config/vehicle/ship """
	m	= VesselModel()
	with open( os.path.join(CONFIG, 'vehicle', 'ship', f'{name}.yaml'), 'rb' ) as f:
		m.load( f.read() )
	return m


class Ship:
	def __init__(self, imo, category=None, weight=None, settings=''):
		self.id			= str( imo )
		self.guid		= str( imo )
		self.recid		= imo
		self.location	= (0.0, 0.0)
		self.config		= {'identifier': {'imo': imo}, 'settings': settings}
		self.model		= model( category ) if category else None
		self.weight		= weight if weight is not None else (self.model.mass if self.model else None)


class Pass(RuleContext):
	""" Rule context with the scenario's visibility and no target ship """
	def __init__(self, ship, visibility=CLEAR):
		RuleContext.__init__( self, [ship] )
		self.terms	= { '(OwnShip,TargetShip).Visibility': visibility,
						'OwnShip.Length': ship.model.ship.length if ship.model else 0.0 }

	def resolve(self, expr):
		return self.terms.get( expr )


class ExtremeWeatherExaminerTestCase(unittest.TestCase):
	def setUp(self):
		self.ctxt	= Ctxt( [Shape('Turkeli.Strait', 'STRAIT')] )
		self.exam	= ExtremeWeatherExaminer()
		self.exam.id, self.exam.callbacks	= 'ExtremeWeather', {}
		self.exam.setup( self.ctxt, {'zones': None, 'territory': None,
									 'network': '$(CONFIG)/risk/capsize.model.xdsl',
									 'bindings': '$(CONFIG)/risk/capsize.model.yaml'} )
		self.exam.cache_shapes( self.ctxt )

	def judge(self, ship, hs=None, visibility=CLEAR):
		self.exam.waves	= [ Field(hs) ] if hs is not None else []
		examine_subjects( self.exam, self.ctxt, Pass(ship, visibility) )

	def rows(self, table):
		return [ row[1] for row in self.ctxt.sim.data.rows if row[0] == table ]

	def capsize(self):
		""" The last fact_capsize row as a dictionary """
		names	= ( 'time', 'vessel', 'zone', 'wave_height', 'wave_state', 'visibility', 'visibility_state',
					'payload', 'payload_state', 'length', 'size_state', 'p_capsize', 'threshold' )
		row		= self.rows( 'fact_capsize' )[-1]
		self.assertEqual( len(row), FIELDS )
		return dict( zip(names, row) )

	def test_visibility_is_read_without_a_target_ship(self):
		self.judge( Ship(1), 0.3, FOG )
		row	= self.capsize()
		self.assertEqual( (row['visibility'], row['visibility_state']), (FOG, 'poor') )

		self.judge( Ship(1), 0.3, CLEAR )
		self.assertEqual( self.capsize()['visibility_state'], 'good' )

	def test_every_assessment_is_recorded_below_the_alarm(self):
		self.judge( Ship(1), 0.3 )
		row	= self.capsize()
		self.assertLess( row['p_capsize'], row['threshold'] )
		self.assertEqual( (row['vessel'], row['zone'], row['wave_height'], row['wave_state']), (1, 'Turkeli.Strait', 0.3, 'calm') )
		self.assertEqual( self.rows('fact_ro'), [] )

	def test_no_wave_field_leaves_the_wave_unobserved(self):
		self.judge( Ship(1) )
		row	= self.capsize()
		self.assertEqual( (row['wave_height'], row['wave_state']), (None, None) )

	def test_a_vessel_without_a_ship_model_has_no_length(self):
		self.judge( Ship(1), 0.3 )
		row	= self.capsize()
		self.assertEqual( (row['length'], row['size_state']), (None, 'small') )		# The configured default

	def test_a_container_ship_is_large_and_a_motorboat_small(self):
		self.judge( Ship(1, 'container'), 0.3 )
		self.assertEqual( (self.capsize()['length'], self.capsize()['size_state']), (294.0, 'large') )

		self.judge( Ship(2, 'motorboat'), 0.3 )
		self.assertEqual( (self.capsize()['length'], self.capsize()['size_state']), (10.0, 'small') )

	def test_payload_without_a_deadweight_is_the_default(self):
		self.judge( Ship(1, weight=500.0), 0.3 )
		row	= self.capsize()
		self.assertEqual( (row['payload'], row['payload_state']), (None, 'laden') )

	def test_a_vessel_at_its_category_weight_is_laden(self):
		self.judge( Ship(1, 'ferry'), 0.3 )
		row	= self.capsize()
		self.assertEqual( (row['payload'], row['payload_state']), (1.0, 'laden') )

	def test_payload_is_load_over_deadweight(self):
		# Ferry: lightship 1200 - 350 = 850 t; 850 + 70 t carried = 20 % of 350 t
		self.judge( Ship(1, 'ferry', weight=920.0), 0.3 )
		row	= self.capsize()
		self.assertAlmostEqual( row['payload'], 0.2 )
		self.assertEqual( row['payload_state'], 'light' )

	def test_a_vessel_deadweight_overrides_its_category(self):
		# 850 t lightship + 175 t on a declared 250 t deadweight = 70 %
		self.judge( Ship(1, 'ferry', weight=1025.0, settings='deadweight=250'), 0.3 )
		self.assertAlmostEqual( self.capsize()['payload'], 0.7 )

	def test_a_small_overladen_vessel_in_a_hurricane_in_fog_capsizes(self):
		ship	= Ship( 1, 'motorboat', weight=7.0 )		# 4.5 t lightship + 2.5 t on 1.5 t deadweight
		self.judge( ship, 12.0, FOG )
		row	= self.capsize()
		self.assertGreaterEqual( row['p_capsize'], row['threshold'] )
		self.assertEqual( [ r[8] for r in self.rows('fact_ro') ], ['weather.capsize_risk'] )


class Posts(IPC):
	""" IPC stand-in that keeps what was pushed, and clears violations as the shared stub does """
	def __init__(self):
		IPC.__init__( self )
		self.posts	= []
	def push(self, topic, message, ctxt, payload, priority=None):
		self.posts.append( (topic, message, payload) )
		IPC.push( self, topic, message, ctxt, payload, priority )


class CapsizeEpochTestCase(unittest.TestCase):
	def setUp(self):
		self.ctxt	= Ctxt( [Shape('Turkeli.Strait', 'STRAIT')] )
		self.ctxt.ipc	= Posts()
		self.exam	= ExtremeWeatherExaminer()
		self.exam.id, self.exam.callbacks	= 'ExtremeWeather', {}
		self.exam.setup( self.ctxt, {'zones': None, 'territory': None,
									 'network': '$(CONFIG)/risk/capsize.model.xdsl',
									 'bindings': '$(CONFIG)/risk/capsize.model.yaml'} )
		self.exam.cache_shapes( self.ctxt )

	def assess(self, risks):
		""" Reports one P(capsize) per tick, ending each pass as the evaluator does """
		ship	= Ship( 1 )
		for capsize in risks:
			self.exam.report( self.ctxt, ship, {}, capsize )
			self.exam.end( self.ctxt, None )
			self.ctxt.sim.advance( 1 )

	def epochs(self):
		return [ p for t, m, p in self.ctxt.ipc.posts if m == ExtremeWeatherExaminer.EPOCH_MESSAGE ]

	def test_an_epoch_at_or_above_the_alarm_is_published_with_its_peak(self):
		self.assess( [0.1, 0.3, 0.6, 0.4, 0.1] )
		epochs	= self.epochs()
		self.assertEqual( len(epochs), 1 )
		self.assertEqual( epochs[0]['threshold'], 0.25 )
		self.assertEqual( epochs[0]['zone'], 'Turkeli.Strait' )
		self.assertEqual( (epochs[0]['epoch']['peak'], epochs[0]['epoch']['samples'], epochs[0]['epoch']['reason']), (0.6, 3, 'released') )

	def test_findings_are_unchanged(self):
		self.assess( [0.3]*3 + [0.1] )
		self.assertEqual( [ r[1][8] for r in self.ctxt.sim.data.rows if r[0] == 'fact_ro' ], ['weather.capsize_risk'] )

	def test_a_long_epoch_is_cut_at_ten_ticks(self):
		self.assess( [0.3]*25 + [0.1] )
		self.assertEqual( [ e['epoch']['reason'] for e in self.epochs() ], ['span', 'span', 'released'] )

	def test_open_epochs_are_published_at_termination(self):
		self.assess( [0.3]*3 )
		self.ctxt.sim.advance( -1 )
		self.exam.on_term( self.ctxt, TERM_WRITE )
		self.assertEqual( [ e['epoch']['reason'] for e in self.epochs() ], ['stop'] )

if __name__ == '__main__':
    unittest.main()
