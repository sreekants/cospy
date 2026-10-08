#!/usr/bin/python
# Filename: PracticeEvaluator.py
# Description: Drives the practice faculties and the inspectors; examiners act only on the examinations delivered here (REQ.028, REQ.051)

from maritime.regulation.colreg.Resolver import Resolver
from maritime.regulation.colreg.API import API
from rules.assurance.inspection.TestInspector import TestInspector
from maritime.model.vessel.Vessel import afloat
from maritime.model.zone.Location import Location
from cos.model.rule.Context import Context as RuleContext
from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.core.utilities.ArgList import ArgList
from maritime.core.situation.MaritimeSituation import PRACTICE_FACULTIES

import sys

PRACTICE	= ['/Faculty/Practice/Examiners', '/Faculty/Practice/Inspectors']


class PracticeEvaluator(Service):
	def __init__(self):
		""" Constructor
		"""
		Service.__init__(self, "Practice", "Evaluator")

		self.timer		= None
		self.faculties	= []
		self.examiners	= []
		self.inspectors	= []
		self.vessels	= []
		self.world		= None
		self.filter		= None
		self.resolver	= Resolver()
		self.API		= API()
		self.passes		= 0
		self.location	= None
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Service.on_start(self, ctxt, config)

		args			= ArgList( config["config"] )
		poll_at			= args["sample.frequency"]
		self.timer		= Ticker( float(poll_at), ctxt.sim.clock ) if poll_at is not None else None
		self.resolver.init( ctxt, args["resolvers"] )
		self.location	= Location.shared( ctxt, args["location"] )		# Fatal when absent (REQ.022)
		ctxt.log.info( self.id, f'Nominal depth {self.location.nominal_depth:.0f} m from {self.location.path}' )

		objmgr			= ctxt.sim.objects
		self.world		= ctxt.sim.world
		self.vessels	= afloat( objmgr.get_all("/World/Vehicle/Vessel") )
		self.examiners	= objmgr.get_all( PRACTICE[0] )
		self.faculties	= sorted( objmgr.get_all( PRACTICE_FACULTIES ), key=lambda f: getattr(f, 'LAST', False) )
		self.inspectors	= objmgr.get_all( PRACTICE[1] )
		if len( self.inspectors ) == 0:
			ctxt.log.error( self.id, 'No inspector loaded: add Assurance=$(CONFIG)/rules.assurance.yaml to [Rules] in cos.ini' )
		self.filter		= TestInspector.under_test( ctxt )

		# Pump the practice namespaces here, not in the COLREG evaluator (COS.023 L2)
		self.poll_ipc( ctxt, PRACTICE + [PRACTICE_FACULTIES] )

		ctxt.log.info( self.id, f'Driving {len(self.faculties)} practice faculties for {len(self.examiners)} examiner(s), and {len(self.inspectors)} inspector(s), every {poll_at} s' )
		return

	def on_stop(self, ctxt:Context, unused):
		""" Reports how often the nominal depth stood in for the map (REQ-022-03)
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		if self.location is not None:
			ctxt.log.info( self.id, self.location.describe() )
		return Service.on_stop( self, ctxt, unused )

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Service.on_timer(self, ctxt, unused)

		if (self.timer is None) or (self.timer.signaled() == False):
			return

		self.evaluate( ctxt )
		return

	def context(self, ctxt:Context)->RuleContext:
		""" A rule context of its own, with the vessels under test as subjects (REQ.024)
		Arguments
			ctxt -- Simulation context
		"""
		rule_ctxt	= RuleContext( ctxt, self.resolver, self.world, self.vessels, self.API )

		if self.filter is not None:
			rule_ctxt.subjects	= self.filter.select( self.vessels )

		return rule_ctxt

	def evaluate(self, ctxt:Context):
		""" Runs one pass: each practice faculty posts its examinations, delivered to the examiners at once; then every inspector.
		Each faculty and inspector is isolated from the others' failures.
		Arguments
			ctxt -- Simulation context
		"""
		rule_ctxt	= self.context( ctxt )
		self.passes	+= 1

		for faculty in self.faculties:
			if self.running == False:
				return
			try:
				faculty.evaluate( ctxt, rule_ctxt )
			except Exception as e:
				ctxt.log.error( self.id, f'{faculty.id}.evaluate: {e}' )
			self.deliver( ctxt )

		for phase in ('begin', 'evaluate', 'end'):
			for inspector in self.inspectors:
				if self.running == False:
					return
				try:
					getattr( inspector, phase )( ctxt, rule_ctxt )
				except Exception as e:
					ctxt.log.error( self.id, f'{inspector.id}.{phase}: {e}' )
		return

	def deliver(self, ctxt:Context):
		""" Delivers every pending examination to the examiners, unthrottled, within the pass
		Arguments
			ctxt -- Simulation context
		"""
		ctxt.ipc.pump_node( ctxt.ipc.get_node( PRACTICE[0] ), sys.maxsize )
		return


if __name__ == "__main__":
	test = PracticeEvaluator()
