#!/usr/bin/python
# Filename: test_Practice.py
# Description: Test cases for the practice namespace, its evaluator, faculties and examination delivery (REQ.027, REQ.028, REQ.051, COS.023, COS.005, COS.006)

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
PracticeFaculty		= source_module( 'maritime.practice.PracticeFaculty' )
EpochFaculty		= source_module( 'maritime.practice.EpochFaculty' ).EpochFaculty
Examination			= source_module( 'cos.model.examiner.Examination' )

ExaminationType		= Examination.ExaminationType

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
		mq, rule, examiner, faculty	= MessageQueue(), Listener(), Listener(), Listener()
		mq.subscribe( '/Faculty/Regulation/Rules/COLREG/Rule14', rule )
		mq.subscribe( '/Faculty/Practice/Examiners/Navigation/CollisionExaminer', examiner )
		mq.subscribe( '/Faculty/Situation/Practice/Checks/Encounters.Faculty', faculty )
		return mq, rule, examiner, faculty

	def pump(self, mq):
		for root in ('/Faculty/Regulation', '/Faculty/Practice', '/Faculty/Situation/Practice'):
			mq.pump_node( mq.get_node(root) )

	def test_examiners_live_under_practice(self):
		self.assertEqual( Examiner.category.fget(None), 'Practice/Examiners' )

	def test_a_post_to_regulation_reaches_no_examiner(self):
		mq, rule, examiner, faculty	= self.queue()
		mq.push( '/Faculty/Regulation', 'vessel.approach', None, None, 8 )
		self.pump( mq )
		self.assertEqual( rule.received, ['vessel.approach'] )
		self.assertEqual( examiner.received, [] )

	def test_situations_are_addressed_to_rules_and_practice_faculties_not_examiners(self):
		mq, rule, examiner, faculty	= self.queue()
		for topic in MaritimeSituation.REGULATION_TOPICS:
			mq.push( topic, 'vessel.crossing', None, None, 8 )
		self.pump( mq )
		self.assertEqual( rule.received, ['vessel.crossing'] )
		self.assertEqual( faculty.received, ['vessel.crossing'] )
		self.assertEqual( examiner.received, [] )

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
	""" REQ.028, REQ.051 """

	class Faculty:
		def __init__(self, name, fail=False, LAST=False):
			self.id		= name
			self.fail	= fail
			self.LAST	= LAST
			self.calls	= []
		def evaluate(self, ctxt, rule_ctxt):
			if self.fail:
				raise RuntimeError( 'boom' )
			self.calls.append( 'evaluate' )

	class Examiner:
		def __init__(self, name):
			self.id		= name
			self.calls	= []
		def __getattr__(self, name):
			if name in ('begin', 'evaluate', 'end'):
				return lambda *a: self.calls.append( name )
			raise AttributeError( name )

	class Filter:
		def select(self, vessels):
			return vessels[:1]

	def evaluator(self, faculties=(), examiners=(), inspectors=()):
		pe				= PracticeEvaluator.__new__( PracticeEvaluator )
		pe.id			= 'Evaluator'
		pe.resolver		= None
		pe.world		= None
		pe.API			= None
		pe.vessels		= ['a', 'b']
		pe.filter		= self.Filter()
		pe.faculties	= list( faculties )
		pe.examiners	= list( examiners )
		pe.inspectors	= list( inspectors )
		pe.passes		= 0
		pe.delivered	= 0
		def deliver(ctxt):
			pe.delivered	+= 1
		pe.deliver		= deliver
		return pe

	def test_one_failing_faculty_does_not_stop_the_others(self):
		bad, good	= self.Faculty('bad', fail=True), self.Faculty('good')
		self.evaluator( [bad, good] ).evaluate( Ctxt() )
		self.assertEqual( good.calls, ['evaluate'] )

	def test_examinations_are_delivered_after_each_faculty(self):
		pe	= self.evaluator( [self.Faculty('a'), self.Faculty('b', fail=True), self.Faculty('c')] )
		pe.evaluate( Ctxt() )
		self.assertEqual( pe.delivered, 3 )

	def test_examiners_are_never_driven(self):
		exam	= self.Examiner( 'e' )
		self.evaluator( [self.Faculty('f')], examiners=[exam] ).evaluate( Ctxt() )
		self.assertEqual( exam.calls, [] )

	def test_inspectors_run_in_each_phase(self):
		insp	= self.Examiner( 'i' )
		self.evaluator( [self.Faculty('f')], inspectors=[insp] ).evaluate( Ctxt() )
		self.assertEqual( insp.calls, ['begin', 'evaluate', 'end'] )

	def test_own_context_with_subjects_from_the_filter(self):
		pe		= self.evaluator()
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


def faculty(examination, situations):
	""" A practice faculty, as Practice.Evaluator drives it """
	f			= PracticeFaculty.PracticeFaculty.__new__( PracticeFaculty.PracticeFaculty )
	f.id		= f'{examination}.Faculty'
	f.callbacks	= {}
	f.encounters	= queue.Queue()
	f.setup( None, {'examination': examination, 'situations': situations} )
	return f


class Posts:
	""" IPC that keeps what is pushed """
	def __init__(self):
		self.posts	= []
	def push(self, topic, msg, ctxt, arg, depth=1):
		self.posts.append( (topic, msg, arg) )


class DeliveryTestCase(unittest.TestCase):
	""" REQ.051; COS.023 L3–L5 """

	def test_examiner_registers_its_examination_type(self):
		exam	= examiner( GroundingExaminer, Ctxt() )
		self.assertIn( ExaminationType.GROUNDING, exam.examinations )

	def test_examiner_ignores_raw_messages_and_other_types(self):
		ctxt	= Ctxt()
		exam	= examiner( GroundingExaminer, ctxt )
		a, b	= Ship('A'), Ship('B')
		Examiner.notify( exam, ctxt, 'vessel.approach', ('CPA', a, b, 5.0) )
		situation	= Situation( a, None )
		situation.context	= RuleContext( [a] )
		exam.on_examination( ctxt, Examination.Examination(ExaminationType.BERTHING, situation) )
		self.assertEqual( exam.judged, [] )

	def test_an_examination_type_must_be_an_enumeration(self):
		with self.assertRaises( TypeError ):
			Examination.Examination( 'vessel.grounding', None )

	def test_encounter_faculty_posts_each_queued_encounter_once(self):
		ctxt		= Ctxt()
		ctxt.ipc	= Posts()
		f			= faculty( 'ENCOUNTER', 'encounters' )
		a, b, c		= Ship('A'), Ship('B'), Ship('C')

		class Event:
			TS	= c
		f.notify( ctxt, 'vessel.approach', ('CPA', a, b, 5.0) )
		f.notify( ctxt, 'vessel.approach', ('CPA', a, b, 4.0) )
		f.notify( ctxt, 'vessel.crossing', ('CR', a, Event()) )

		rule_ctxt	= RuleContext( [a, b, c] )
		f.evaluate( ctxt, rule_ctxt )
		posted	= [ arg for topic, msg, arg in ctxt.ipc.posts ]
		self.assertEqual( {topic for topic, msg, arg in ctxt.ipc.posts}, {'/Faculty/Practice/Examiners'} )
		self.assertEqual( {msg for topic, msg, arg in ctxt.ipc.posts}, {Examination.EXAMINATION} )
		self.assertEqual( sorted((e.body.os.id, e.body.ts.id) for e in posted), [('A', 'B'), ('A', 'C')] )
		self.assertTrue( all(e.type is ExaminationType.ENCOUNTER and e.body.context is rule_ctxt for e in posted) )

		f.evaluate( ctxt, rule_ctxt )
		self.assertEqual( len(ctxt.ipc.posts), 2 )

	def test_subjects_faculty_posts_each_subject_alone_and_ignores_encounters(self):
		ctxt		= Ctxt()
		ctxt.ipc	= Posts()
		f			= faculty( 'GROUNDING', 'subjects' )
		a, b		= Ship('A'), Ship('B')
		f.notify( ctxt, 'vessel.approach', ('CPA', a, b, 5.0) )
		self.assertTrue( f.encounters.empty() )

		f.evaluate( ctxt, RuleContext([a, b], subjects=[a]) )
		self.assertEqual( [(e.type, e.body.os.id, e.body.ts) for t, m, e in ctxt.ipc.posts], [(ExaminationType.GROUNDING, 'A', None)] )

	def test_a_situation_leaves_the_vessel_once_posted(self):
		ctxt		= Ctxt()
		ctxt.ipc	= Posts()
		a			= Ship('A')
		a.situations	= []
		faculty( 'SPEED', 'subjects' ).evaluate( ctxt, RuleContext([a]) )
		self.assertEqual( a.situations, [] )
		self.assertEqual( len(ctxt.ipc.posts), 1 )

	def test_epoch_faculty_posts_an_epoch_once_it_has_lasted(self):
		ctxt		= Ctxt()
		ctxt.ipc	= Posts()
		f			= EpochFaculty.__new__( EpochFaculty )
		f.id, f.callbacks, f.episode	= 'Epoch.Faculty', {}, None
		f.setup( None, {'ticks': '2'} )
		rule_ctxt	= RuleContext( [Ship('A')] )
		start		= ctxt.sim.tickcount()
		for tick in range( 5 ):
			f.evaluate( ctxt, rule_ctxt )
			ctxt.sim.advance( 1 )
		epochs	= [ e for t, m, e in ctxt.ipc.posts ]
		self.assertEqual( [e.type for e in epochs], [ExaminationType.EPOCH_EPISODE]*2 )
		self.assertEqual( [e.body.began - start for e in epochs], [0, 2] )
		self.assertTrue( all(e.body.context is rule_ctxt for e in epochs) )

	def test_epoch_examination_ends_the_examiners_periods(self):
		ctxt	= Ctxt()
		exam	= examiner( GroundingExaminer, ctxt )
		ended	= []
		exam.end	= lambda c, r: ended.append( r )
		rule_ctxt	= RuleContext( [] )
		episode		= source_module( 'maritime.core.episode.EpochEpisode' ).EpochEpisode( 1 )
		episode.context	= rule_ctxt
		exam.on_examination( ctxt, Examination.Examination(ExaminationType.EPOCH_EPISODE, episode) )
		self.assertEqual( ended, [rule_ctxt] )

	def test_a_failing_examiner_is_isolated(self):
		ctxt	= Ctxt()
		exam	= examiner( GroundingExaminer, ctxt )
		def boom(c, r):
			raise RuntimeError( 'boom' )
		exam.judge	= boom
		situation	= Situation( Ship('A'), None )
		situation.context	= RuleContext( [] )
		exam.on_examination( ctxt, Examination.Examination(ExaminationType.GROUNDING, situation) )

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

		rule_ctxt	= RuleContext( [vessel] )
		saved		= rule_ctxt.situation
		situation	= Situation( vessel, None )
		situation.context	= rule_ctxt
		exam.on_examination( ctxt, Examination.Examination(ExaminationType.GROUNDING, situation) )
		self.assertEqual( [row[1][8] for row in ctxt.sim.data.rows if row[0] == 'fact_ro'], ['grounding.contact'] )
		self.assertIs( rule_ctxt.situation, saved )


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
		encounters	= faculty( 'ENCOUNTER', 'encounters' )
		exams		= [ examiner(CollisionExaminer, ctxt), examiner(LaneDisciplineExaminer, ctxt) ]
		ctxt.ipc.subscribe( '/Faculty/Regulation/Rules/COLREG/Rule13', rule )
		ctxt.ipc.subscribe( '/Faculty/Situation/Practice/Checks/Encounters.Faculty', encounters )
		for exam in exams:
			ctxt.ipc.subscribe( f'/Faculty/Practice/Examiners/Navigation/{exam.id}', exam )
			exam.subscribe( Examination.EXAMINATION, exam.on_examination )

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

			# Each evaluator pumps its own namespaces every tick; the practice pass runs every third
			for root in ('/Faculty/Regulation/Rules', '/Faculty/Situation/Practice'):
				ctxt.ipc.pump_node( ctxt.ipc.get_node(root) )
			if tick % 3 == 0:
				encounters.evaluate( ctxt, RuleContext([a, b, c, d]) )
				ctxt.ipc.pump_node( ctxt.ipc.get_node('/Faculty/Practice/Examiners') )

		self.assertEqual( len(rule.pairs), posted )
		for exam in exams:
			with self.subTest(examiner=exam.id):
				judged	= [ (o.id, t.id) for o, t in exam.judged ]
				self.assertEqual( set(judged), set(rule.pairs) )
				# A pair repeated within one pass is judged once; A→B spans both passes
				self.assertEqual( judged.count(('A', 'B')), 2 )


class BoundaryTestCase(unittest.TestCase):
	""" REQ-051-06: faculties never name or import an examiner """

	def test_no_faculty_module_imports_an_examiner(self):
		src		= os.path.join( os.path.dirname(__file__), '..', '..', '..', '..', 'src' )
		found	= []
		for package in ( 'maritime/conduct', 'maritime/core/situation', 'maritime/core/episode', 'maritime/practice' ):
			for root, dirs, files in os.walk( os.path.join(src, package) ):
				for name in files:
					if name.endswith( '.py' ):
						with open( os.path.join(root, name) ) as f:
							if 'rules.examiner' in f.read():
								found.append( os.path.join(package, name) )
		self.assertEqual( found, [] )

	def examiners(self):
		with open( os.path.join(CONFIG, 'rules.examiner.yaml') ) as f:
			modules	= yaml.safe_load( f )['packages']['modules']
		with open( os.path.join(CONFIG, 'rules.risk.yaml') ) as f:
			modules	+= yaml.safe_load( f )['packages']['modules']
		classes	= [ source_module(m['module']).__dict__[m['module'].split('.')[-1]] for m in modules if m['module'].startswith('rules.examiner.') ]
		faculties	= [ m for m in modules if m['module'].startswith('maritime.practice.') and m['module'] != 'maritime.practice.PracticeEvaluator' ]
		return classes, faculties

	def test_no_examiner_shadows_the_examination_hooks(self):
		classes, _	= self.examiners()
		for klass in classes:
			for hook in ( 'handle_examination', 'on_examination', 'on_epoch_episode' ):
				with self.subTest(examiner=klass.__name__, hook=hook):
					self.assertIs( getattr(klass, hook), getattr(Examiner, hook) )

	def test_every_check_has_a_faculty_and_an_examiner(self):
		classes, faculties	= self.examiners()
		posted		= { m['config'].split('examination=')[1].split()[0] for m in faculties if 'examination=' in m['config'] }
		examined	= { klass.EXAMINES.name for klass in classes if getattr(klass, 'EXAMINES', None) is not None }
		checks		= { t.name for t in ExaminationType if t.value > 100 }
		self.assertEqual( posted, checks )
		self.assertEqual( examined, checks )


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
