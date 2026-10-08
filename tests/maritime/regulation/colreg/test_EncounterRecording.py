#!/usr/bin/python
# Filename: test_EncounterRecording.py
# Description: Test cases for encounter range and once-per-encounter recording (COS.027)

import unittest

import numpy as np

from maritime.regulation.colreg.Encounter import Encounter
from maritime.situation.headon.Headon import Headon
from maritime.situation.crossing.Crossing import Crossing
from cos.model.rule.Context import Context as RuleContext
from maritime.core.situation.MaritimeSituation import REGULATION_TOPICS
from cos.core.kernel.Object import TERM_WRITE


class Vessel:
	def __init__(self, recid, x, y, vx, vy):
		self.id			= f'v{recid}'
		self.recid		= recid
		self.location	= np.array( (float(x), float(y), 0.0) )
		self.velocity	= np.array( (float(vx), float(vy), 0.0) )
		self.notices	= []

	def notify(self, ctxt, msg, arg):
		self.notices.append( msg )

	def step(self):
		self.location	= self.location + self.velocity


class IPC:
	def __init__(self):
		self.posts	= []
	def push(self, topic, msg, ctxt, arg, priority):
		self.posts.append( (topic, msg) )


class Data:
	def __init__(self):
		self.rows	= []
	def push(self, topic, row, context=None):
		self.rows.append( (topic, row) )


class Clock:
	step	= 1.0


class Sim:
	def __init__(self):
		self.data	= Data()
		self.clock	= Clock()
		self.tick	= 0
	def tickcount(self):
		return self.tick
	def seconds(self):
		return float(self.tick)


class Ctxt:
	def __init__(self):
		self.sim	= Sim()
		self.ipc	= IPC()


class RecordingTestCase(unittest.TestCase):
	def run_passes(self, vessels, passes, monitor):
		ctxt		= Ctxt()
		encounter	= Encounter()
		for n in range(passes):
			ctxt.sim.tick	= n
			rule_ctxt		= RuleContext( ctxt, None, None, vessels, None )
			encounter.evaluate( ctxt, rule_ctxt )
			monitor.evaluate( ctxt, rule_ctxt )
			for v in vessels:
				v.step()
		return ctxt

	def test_range_is_the_colreg_stage_2_range(self):
		self.assertEqual( Encounter().range, 4000.0 )

	def test_one_row_per_encounter_and_a_notice_every_pass(self):
		a, b	= Vessel(1, 0, 0, 10, 0), Vessel(2, 1000, 5, -10, 0)	# head-on until the 5 m offset bears over 13°, at pass 49
		monitor	= Headon()
		ctxt	= self.run_passes( [a, b], 80, monitor )

		rows	= [ row for topic, row in ctxt.sim.data.rows if topic == 'fact_head_on' ]
		self.assertEqual( sorted(r[:2] for r in rows), [(1, 2), (2, 1)] )
		for own, target, start, end in rows:
			self.assertEqual( start, 0 )
			self.assertEqual( end, 48 )

		self.assertEqual( a.notices.count('vessel.headon'), 49 )
		self.assertEqual( monitor.open, {} )

	def test_open_encounters_are_recorded_at_termination(self):
		a, b	= Vessel(1, 0, 0, 10, 0), Vessel(2, 1000, 5, -10, 0)
		monitor	= Headon()
		ctxt	= self.run_passes( [a, b], 10, monitor )
		self.assertEqual( ctxt.sim.data.rows, [] )

		monitor.on_term( ctxt, TERM_WRITE )
		rows	= [ row for topic, row in ctxt.sim.data.rows if topic == 'fact_head_on' ]
		self.assertEqual( sorted(rows), [(1, 2, 0, 9), (2, 1, 0, 9)] )

	def crossing_with_break(self, stopped):
		a, b	= Vessel(1, 0, 0, 0, -10), Vessel(2, 1500, -1500, -10, 0)	# crossing, target on starboard
		monitor	= Crossing()
		ctxt	= Ctxt()
		encounter	= Encounter()
		for n, moving in enumerate( [True]*5 + [False]*stopped + [True]*5 ):
			ctxt.sim.tick	= n
			b.velocity		= np.array( (-10.0 if moving else 0.0, 0.0, 0.0) )
			rule_ctxt		= RuleContext( ctxt, None, None, [a, b], None )
			encounter.evaluate( ctxt, rule_ctxt )
			monitor.evaluate( ctxt, rule_ctxt )
		monitor.on_term( ctxt, TERM_WRITE )
		return sorted( row for topic, row in ctxt.sim.data.rows if (topic == 'fact_crossing') and (row[0] == 1) ), a

	def test_a_short_break_is_one_encounter(self):
		rows, a	= self.crossing_with_break( 3 )
		self.assertEqual( rows, [(1, 2, 0, 12)] )
		self.assertEqual( a.notices.count('vessel.crossing'), 10 )

	def test_a_break_longer_than_the_release_is_two_encounters(self):
		rows, a	= self.crossing_with_break( 12 )
		self.assertEqual( rows, [(1, 2, 0, 4), (1, 2, 17, 21)] )

	def test_pairs_beyond_range_are_not_classified(self):
		a, b	= Vessel(1, 0, 0, 10, 0), Vessel(2, 5000, 5, -10, 0)
		monitor	= Headon()
		ctxt	= self.run_passes( [a, b], 5, monitor )
		monitor.on_term( ctxt, TERM_WRITE )
		self.assertEqual( ctxt.sim.data.rows, [] )
		self.assertEqual( a.notices, [] )



class Recorder(Vessel):
	""" Vessel that keeps the argument of each notice """
	def notify(self, ctxt, msg, arg):
		self.notices.append( (msg, arg) )


class ManeuverEpochTestCase(unittest.TestCase):
	def run_passes(self, vessels, passes, monitor, arg=''):
		ctxt		= Ctxt()
		monitor.on_start( ctxt, {'arg': arg} )
		encounter	= Encounter()
		for n in range(passes):
			ctxt.sim.tick	= n
			rule_ctxt		= RuleContext( ctxt, None, None, vessels, None )
			encounter.evaluate( ctxt, rule_ctxt )
			monitor.evaluate( ctxt, rule_ctxt )
			for v in vessels:
				v.step()
		return ctxt

	def test_the_rules_get_one_event_per_epoch_at_its_closest_range(self):
		a, b	= Recorder(1, 0, 0, 10, 0), Recorder(2, 1000, 5, -10, 0)		# head-on through pass 48
		monitor	= Headon()
		ctxt	= self.run_passes( [a, b], 80, monitor )

		closest	= [ float(np.hypot(1000 - 20*n, 5)) for n in (9, 19, 29, 39, 48) ]
		self.assertEqual( [m for m, arg in a.notices], ['vessel.headon']*5 )
		self.assertEqual( [round(arg[2].distance, 6) for m, arg in a.notices], [round(d, 6) for d in closest] )
		self.assertEqual( len(b.notices), 5 )
		self.assertEqual( [m for t, m in ctxt.ipc.posts].count('vessel.headon'), 10 * len(REGULATION_TOPICS) )		# 5 epochs per ship

	def test_the_encounter_rows_are_unchanged(self):
		a, b	= Recorder(1, 0, 0, 10, 0), Recorder(2, 1000, 5, -10, 0)
		monitor	= Headon()
		ctxt	= self.run_passes( [a, b], 80, monitor )
		rows	= [ row for topic, row in ctxt.sim.data.rows if topic == 'fact_head_on' ]
		self.assertEqual( sorted(rows), [(1, 2, 0, 48), (2, 1, 0, 48)] )

	def test_the_epoch_length_comes_from_the_yaml(self):
		a, b	= Recorder(1, 0, 0, 10, 0), Recorder(2, 1000, 5, -10, 0)
		monitor	= Headon()
		self.run_passes( [a, b], 80, monitor, 'epoch=25' )
		self.assertEqual( monitor.watcher.span, 25 )
		self.assertEqual( len(a.notices), 2 )						# passes 0-24 and 25-48

	def test_a_short_break_stays_in_one_epoch(self):
		a, b	= Recorder(1, 0, 0, 0, -10), Recorder(2, 1500, -1500, -10, 0)	# crossing, target on starboard
		monitor	= Crossing()
		ctxt	= Ctxt()
		monitor.on_start( ctxt, {'arg': 'epoch=50'} )
		encounter	= Encounter()
		for n, moving in enumerate( [True]*5 + [False]*3 + [True]*5 ):
			ctxt.sim.tick	= n
			b.velocity		= np.array( (-10.0 if moving else 0.0, 0.0, 0.0) )
			rule_ctxt		= RuleContext( ctxt, None, None, [a, b], None )
			encounter.evaluate( ctxt, rule_ctxt )
			monitor.evaluate( ctxt, rule_ctxt )
		monitor.on_term( ctxt, TERM_WRITE )
		self.assertEqual( [m for m, arg in a.notices], ['vessel.crossing'] )

	def test_open_epochs_are_sent_at_termination(self):
		a, b	= Recorder(1, 0, 0, 10, 0), Recorder(2, 1000, 5, -10, 0)
		monitor	= Headon()
		ctxt	= self.run_passes( [a, b], 5, monitor )
		self.assertEqual( a.notices, [] )
		monitor.on_term( ctxt, TERM_WRITE )
		self.assertEqual( [m for m, arg in a.notices], ['vessel.headon'] )


if __name__ == '__main__':
	unittest.main()
