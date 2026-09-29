#!/usr/bin/python
# Filename: test_Practice.py
# Description: Test cases for the practice namespace, its evaluator and examiner delivery (REQ.027, REQ.028, COS.023, COS.005, COS.006)

import os, queue, tempfile, unittest

import numpy as np
import yaml

from tests.maritime.model.risk.test_ConcernWeights import source_module, CONFIG
from tests.maritime.model.zone.test_Ledger import Ctxt, Shape, Vessel as LedgerVessel

MessageQueue		= source_module( 'cos.core.kernel.MessageQueue' ).MessageQueue
Examiner			= source_module( 'cos.model.examiner.Examiner' ).Examiner
Situation			= source_module( 'cos.model.rule.Situation' ).Situation
PreconditionSet		= source_module( 'cos.model.examiner.Precondition' ).PreconditionSet
MaritimeSituation	= source_module( 'maritime.core.situation.MaritimeSituation' )
ZoneAwareness		= source_module( 'maritime.model.zone.ZoneAwareness' )
PracticeEvaluator	= source_module( 'maritime.practice.PracticeEvaluator' ).PracticeEvaluator
CollisionExaminer	= source_module( 'rules.examiner.navigation.CollisionExaminer' ).CollisionExaminer
GroundingExaminer	= source_module( 'rules.examiner.navigation.GroundingExaminer' ).GroundingExaminer
RiskExaminer		= source_module( 'rules.examiner.risk.RiskExaminer' ).RiskExaminer
SignalExaminer		= source_module( 'rules.examiner.navigation.SignalExaminer' ).SignalExaminer

ZoneAware	= ZoneAwareness.ZoneAware


class Listener:
	def __init__(self):
		self.received	= []
	def notify(self, ctxt, msg, arg):
		self.received.append( msg )


class Ship:
	def __init__(self, name, fleet=None):
		self.id		= name
		self.name	= name
		self.fleet	= fleet


class NamespaceTestCase(unittest.TestCase):
	""" REQ.027 """

	def queue(self):
		mq, rule, examiner	= MessageQueue(), Listener(), Listener()
		mq.subscribe( '/Faculty/Regulation/Rules/COLREG/Rule14', rule )
		mq.subscribe( '/Faculty/Practice/Examiners/Navigation/CollisionExaminer', examiner )
		return mq, rule, examiner

	def pump(self, mq):
		for root in ('/Faculty/Regulation', '/Faculty/Practice'):
			mq.pump_node( mq.get_node(root) )

	def test_examiners_live_under_practice(self):
		self.assertEqual( Examiner.category.fget(None), 'Practice/Examiners' )

	def test_a_post_to_regulation_reaches_no_examiner(self):
		mq, rule, examiner	= self.queue()
		mq.push( '/Faculty/Regulation', 'vessel.approach', None, None, 8 )
		self.pump( mq )
		self.assertEqual( rule.received, ['vessel.approach'] )
		self.assertEqual( examiner.received, [] )

	def test_situations_are_addressed_to_both_namespaces(self):
		mq, rule, examiner	= self.queue()
		for topic in MaritimeSituation.REGULATION_TOPICS:
			mq.push( topic, 'vessel.crossing', None, None, 8 )
		self.pump( mq )
		self.assertEqual( rule.received, ['vessel.crossing'] )
		self.assertEqual( examiner.received, ['vessel.crossing'] )

	def test_signal_topic_is_a_list_and_announce_takes_either(self):
		self.assertEqual( SignalExaminer.TOPIC, ['/Faculty/Regulation/Rules'] )

		class IPC:
			def __init__(self):
				self.pushed	= []
			def push(self, topic, *args):
				self.pushed.append( topic )

		ctxt		= Ctxt()
		ctxt.ipc	= IPC()
		ZoneAware.announce( None, ctxt, '/A', 'm', {} )
		ZoneAware.announce( None, ctxt, ['/B', '/C'], 'm', {} )
		self.assertEqual( ctxt.ipc.pushed, ['/A', '/B', '/C'] )


class PracticeEvaluatorTestCase(unittest.TestCase):
	""" REQ.028 """

	class Examiner:
		def __init__(self, name, fail=False):
			self.id		= name
			self.fail	= fail
			self.calls	= []
		def begin(self, ctxt, rule_ctxt):
			self.calls.append( 'begin' )
		def evaluate(self, ctxt, rule_ctxt):
			if self.fail:
				raise RuntimeError( 'boom' )
			self.calls.append( 'evaluate' )
		def end(self, ctxt, rule_ctxt):
			self.calls.append( 'end' )

	class Filter:
		def select(self, vessels):
			return vessels[:1]

	def evaluator(self, examiners):
		pe				= PracticeEvaluator.__new__( PracticeEvaluator )
		pe.id			= 'Evaluator'
		pe.resolver		= None
		pe.world		= None
		pe.API			= None
		pe.vessels		= ['a', 'b']
		pe.filter		= self.Filter()
		pe.examiners	= examiners
		pe.inspectors	= []
		pe.passes		= 0
		return pe

	def test_one_failing_examiner_does_not_stop_the_others(self):
		bad, good	= self.Examiner('bad', fail=True), self.Examiner('good')
		self.evaluator( [bad, good] ).evaluate( Ctxt() )
		self.assertEqual( good.calls, ['begin', 'evaluate', 'end'] )
		self.assertEqual( bad.calls, ['begin', 'end'] )

	def test_own_context_with_subjects_from_the_filter(self):
		pe		= self.evaluator( [] )
		a, b	= pe.context( Ctxt() ), pe.context( Ctxt() )
		self.assertIsNot( a, b )
		self.assertEqual( a.subjects, ['a'] )
		self.assertEqual( a.vessels, ['a', 'b'] )

	def test_not_in_the_colreg_package(self):
		self.assertFalse( PracticeEvaluator.__module__.startswith('maritime.regulation.colreg') )


class RuleContext:
	def __init__(self, vessels, subjects=None):
		self.vessels	= vessels
		self.subjects	= subjects if subjects is not None else vessels
		self.situation	= Situation()
		self.resolver	= None


def examiner(klass, ctxt):
	exam			= klass.__new__( klass )
	exam.id			= klass.__name__
	exam.callbacks	= {}
	exam.init_zones( ctxt, {'zones': None, 'territory': None}, requires=['os'] )
	exam.judged		= []
	exam.judge		= lambda c, r: exam.judged.append( (r.situation.os, r.situation.ts) )
	return exam


class DeliveryTestCase(unittest.TestCase):
	""" COS.023 L3–L5 """

	def test_every_examiner_subscribes_to_the_encounter_messages(self):
		exam	= examiner( GroundingExaminer, Ctxt() )
		self.assertTrue( set(ZoneAwareness.ENCOUNTER_MESSAGES) <= set(exam.callbacks) )

	def test_unhandled_message_is_a_no_op(self):
		exam	= examiner( GroundingExaminer, Ctxt() )
		Examiner.notify( exam, Ctxt(), 'vessel.unknown', None )

	def test_encounter_examiner_judges_each_queued_encounter_once(self):
		ctxt	= Ctxt()
		exam	= examiner( CollisionExaminer, ctxt )
		a, b, c	= Ship('A'), Ship('B'), Ship('C')

		class Event:
			TS	= c
		exam.notify( ctxt, 'vessel.approach', ('CPA', a, b, 5.0) )
		exam.notify( ctxt, 'vessel.approach', ('CPA', a, b, 4.0) )
		exam.notify( ctxt, 'vessel.crossing', ('CR', a, Event()) )

		rule_ctxt	= RuleContext( [a, b, c] )
		saved		= rule_ctxt.situation
		exam.evaluate( ctxt, rule_ctxt )

		self.assertEqual( sorted((o.id, t.id) for o, t in exam.judged), [('A', 'B'), ('A', 'C')] )
		self.assertIs( rule_ctxt.situation, saved )
		self.assertTrue( exam.situations.empty() )

		exam.evaluate( ctxt, rule_ctxt )
		self.assertEqual( len(exam.judged), 2 )

	def test_single_vessel_examiner_iterates_subjects_and_ignores_encounters(self):
		ctxt	= Ctxt()
		exam	= examiner( GroundingExaminer, ctxt )
		a, b	= Ship('A'), Ship('B')
		exam.notify( ctxt, 'vessel.approach', ('CPA', a, b, 5.0) )
		self.assertTrue( exam.situations.empty() )

		exam.evaluate( ctxt, RuleContext([a, b], subjects=[a]) )
		self.assertEqual( [(o.id, t) for o, t in exam.judged], [('A', None)] )

	def test_real_examiner_fires_on_a_subject(self):
		ctxt	= Ctxt( [Shape('Turkeli.Strait', 'STRAIT')] )
		exam	= GroundingExaminer.__new__( GroundingExaminer )
		exam.id, exam.callbacks	= 'Grounding', {}
		exam.init_zones( ctxt, {'zones': None, 'territory': None}, requires=['os'] )
		exam.cache_shapes( ctxt )

		shoal	= Shape( 'Shoal', 'STRAIT' )
		shoal.nominal_depth	= 3.0
		exam.sea	= [shoal]
		vessel	= LedgerVessel( 1 )
		vessel.draft	= 8.0

		exam.evaluate( ctxt, RuleContext([vessel]) )
		self.assertEqual( [row[1][4] for row in ctxt.sim.data.rows], ['grounding.contact'] )


class ParityTestCase(unittest.TestCase):
	""" COS.023 acceptance: rules and encounter examiners receive the same encounters """

	class Rule:
		def __init__(self):
			self.pairs	= []
		def notify(self, ctxt, msg, evt):
			self.pairs.append( (evt[1].id, getattr(evt[2], 'TS', evt[2]).id) )

	class Event:
		def __init__(self, target):
			self.TS	= target

	def test_same_encounters_reach_rules_and_examiners(self):
		LaneDisciplineExaminer	= source_module( 'rules.examiner.navigation.LaneDisciplineExaminer' ).LaneDisciplineExaminer

		ctxt		= Ctxt()
		ctxt.ipc	= MessageQueue()
		rule		= self.Rule()
		exams		= [ examiner(CollisionExaminer, ctxt), examiner(LaneDisciplineExaminer, ctxt) ]
		ctxt.ipc.subscribe( '/Faculty/Regulation/Rules/COLREG/Rule13', rule )
		for exam in exams:
			ctxt.ipc.subscribe( f'/Faculty/Practice/Examiners/Navigation/{exam.id}', exam )

		situation	= MaritimeSituation.MaritimeSituation.__new__( MaritimeSituation.MaritimeSituation )
		a, b, c, d	= Ship('A'), Ship('B'), Ship('C'), Ship('D')
		ticks		= [
			[ ('vessel.approach', ('CPA', a, b, 9.0)) ],
			[ ('vessel.approach', ('CPA', a, b, 7.0)), ('vessel.crossing', ('CR', c, self.Event(d))) ],
			[ ('vessel.overtaking', ('OT', b, self.Event(a))) ],
			[ ('vessel.approach', ('CPA', a, b, 5.0)) ],
			[ ('vessel.crossing', ('CR', a, self.Event(c))) ],
			[ ('vessel.headon', ('HO', c, self.Event(b))) ],
		]

		posted	= 0
		for tick, posts in enumerate( ticks, start=1 ):
			for msg, evt in posts:
				MaritimeSituation.MaritimeSituation.regulate( situation, ctxt, None, msg, evt )
				posted	+= 1

			# Each evaluator pumps its own namespace every tick; examiners are judged every third
			for root in ('/Faculty/Regulation/Rules', '/Faculty/Practice/Examiners'):
				ctxt.ipc.pump_node( ctxt.ipc.get_node(root) )
			if tick % 3 == 0:
				for exam in exams:
					exam.evaluate( ctxt, RuleContext([a, b, c, d]) )

		self.assertEqual( len(rule.pairs), posted )
		for exam in exams:
			with self.subTest(examiner=exam.id):
				judged	= [ (o.id, t.id) for o, t in exam.judged ]
				self.assertEqual( set(judged), set(rule.pairs) )
				self.assertTrue( exam.situations.empty() )
				# A pair repeated within one pass is judged once; A→B spans both passes
				self.assertEqual( judged.count(('A', 'B')), 2 )


class ClearanceTestCase(unittest.TestCase):
	def test_draft_is_read_from_the_vessel_model(self):
		class Model:
			draft	= 8.0
		class Hull:
			model	= Model()
		self.assertEqual( ZoneAware.clearance(None, Hull(), 5.0), -3.0 )


class FleetTestCase(unittest.TestCase):
	""" COS.005, COS.006 """

	def test_situation_has_no_fleet(self):
		self.assertFalse( hasattr(Situation(Ship('A', fleet='F0'), Ship('B', fleet='F1')), 'fleet') )

	def test_fleet_precondition_names_a_vessel(self):
		gate	= PreconditionSet( {'os': ['os.fleet'], 'ts': ['os', 'ts.fleet']} )
		self.assertTrue( gate.holds('ts', Situation(Ship('A'), Ship('B', fleet='F1'))) )
		self.assertFalse( gate.holds('os', Situation(Ship('A'), Ship('B', fleet='F1'))) )
		self.assertTrue( gate.holds('os', Situation(Ship('A', fleet='F0'), None)) )

	def test_bare_fleet_precondition_is_refused(self):
		with self.assertRaisesRegex( ValueError, 'ts.fleet' ):
			PreconditionSet( {'auv': ['os', 'fleet']} )

	def test_binding_to_an_absent_node_is_dropped_at_load(self):
		class BN:
			def names(self):
				return ['auv_asv_distance', 'collision']

		class Log:
			def __init__(self):
				self.errors	= []
			def error(self, module, text):
				self.errors.append( text )
			def info(self, module, text):
				pass
			def debug(self, module, text):
				pass

		ctxt		= Ctxt()
		ctxt.log	= Log()
		exam		= RiskExaminer.__new__( RiskExaminer )
		exam.id		= 'Risk'
		exam.bn		= BN()
		exam.bindings	= {'auv_operation': []}

		# The shipped bindings no longer name an absent node (COS.006), so add one to a copy
		with open( os.path.join(CONFIG, 'risk', 'risk.model.yaml') ) as f:
			config	= yaml.safe_load( f )
		config['risk']['auv_operation'].append( {'node': 'not_a_node', 'term': 'OwnShip.Nothing', 'discretize': 'state'} )
		with tempfile.NamedTemporaryFile( 'w', suffix='.yaml', delete=False ) as f:
			yaml.safe_dump( config, f )
		self.addCleanup( os.unlink, f.name )
		exam._RiskExaminer__load_bindings( ctxt, f.name )

		self.assertEqual( [b['node'] for b in exam.bindings['auv_operation']], ['auv_asv_distance'] )
		self.assertTrue( any('not_a_node' in e for e in ctxt.log.errors) )


if __name__ == '__main__':
	unittest.main()
