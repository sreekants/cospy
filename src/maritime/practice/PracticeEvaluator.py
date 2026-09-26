#!/usr/bin/python
# Filename: PracticeEvaluator.py
# Description: Drives the examiners under /Faculty/Practice/Examiners (REQ.028)

from maritime.regulation.colreg.Resolver import Resolver
from maritime.regulation.colreg.API import API
from maritime.situation.undertest.UnderTest import UnderTest
from maritime.model.zone.Location import Location
from cos.model.rule.Context import Context as RuleContext
from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.core.utilities.ArgList import ArgList

PRACTICE	= '/Faculty/Practice/Examiners'


class PracticeEvaluator(Service):
	def __init__(self):
		""" Constructor
		"""
		Service.__init__(self, "Practice", "Evaluator")

		self.timer		= None
		self.examiners	= []
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
		self.timer		= Ticker( int(poll_at) ) if poll_at is not None else None
		self.resolver.init( ctxt, args["resolvers"] )
		self.location	= Location.shared( ctxt, args["location"] )		# Fatal when absent (REQ.022)
		ctxt.log.info( self.id, f'Nominal depth {self.location.nominal_depth:.0f} m from {self.location.path}' )

		objmgr			= ctxt.sim.objects
		self.world		= ctxt.sim.world
		self.vessels	= objmgr.get_all( "/World/Vehicle/Vessel" )
		self.examiners	= objmgr.get_all( PRACTICE )
		self.filter		= UnderTest.find( ctxt )

		# Pump the examiner namespace here, not in the COLREG evaluator (COS.023 L2)
		self.poll_ipc( ctxt, [PRACTICE] )

		ctxt.log.info( self.id, f'Driving {len(self.examiners)} examiner(s) every {poll_at} s' )
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
		""" Runs one pass over every examiner, each isolated from the others' failures
		Arguments
			ctxt -- Simulation context
		"""
		rule_ctxt	= self.context( ctxt )
		self.passes	+= 1

		for phase in ('begin', 'evaluate', 'end'):
			for examiner in self.examiners:
				try:
					getattr( examiner, phase )( ctxt, rule_ctxt )
				except Exception as e:
					ctxt.log.error( self.id, f'{examiner.id}.{phase}: {e}' )
		return


if __name__ == "__main__":
	test = PracticeEvaluator()
