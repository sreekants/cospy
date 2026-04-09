#!/usr/bin/python
# Filename: GenericRule.py
# Description: Implementation of the generic maritime inland waters rule class

from cos.model.rule.Rule import Rule
from cos.model.rule.Automata import Automata
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.core.utilities.ArgList import ArgList
from cos.lang.logic.Decision import Decision
from cos.model.rule.Situation import Situation

from typing import Any
import queue, fnmatch



class InlandWaterRule(Rule):
	def __init__(self, zonetype):
		""" Constructor
		Arguments
			type -- Zone type
		"""
		Rule.__init__(self, None)

		assert(zonetype is not None)
		
		self.sitations	= queue.Queue()
		self.zones		= None
		self.zonetype	= zonetype
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""

		self.regulation	= module['name']

		# Bind the service to all the category
		Rule.bind(self, self.category, self.zonetype, self.regulation)
	
		Rule.on_init(self, ctxt, module)
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Rule.on_start(self, ctxt, config)

		self.subscribe("vessel.overtaking", self.on_overtaking)
		self.subscribe("vessel.crossing", self.on_crossing)
		self.subscribe("vessel.approach", self.on_close_encounter)
		return

	def notify(self, ctxt:Context, method:str, arg:Any):
		""" Triggers a method
		Arguments
			ctxt -- Simulation context
			method -- Method name
			arg -- Message argumnt
		"""
		Rule.notify(self, ctxt, method, arg)
		return

	def setup_zone(self, ctxt:Context, config:ArgList, typename:str):
		""" Sets up the rule, loading its configurations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Rule.setup(self, ctxt, config)

		zonekey		= config['zonekey']
		objmgr		= ctxt.sim.objects
		zones		= objmgr.get_all(f"/World/Sea/{typename}")

		# Match keys to all zones
		if zonekey is not None:
			self.zones	= []
			for h in zones:
				if fnmatch.fnmatch(h.config['key'], zonekey):
					self.zones.append(h)
		else:
			self.zones	= zones
		

		return


	def add_situation(self, evt):
		""" TODO: add_situation
		Arguments
			evt -- TODO
		""" 
		for z in self.zones:
			if z.intersect(evt.os.boundary):
				evt.zone	= z
				self.sitations.put(evt)
		return


	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""

		Rule.evaluate(self, ctxt, rule_ctxt)

		if self.zones is None:
			return
		
		for v in rule_ctxt.vessels:
			self.add_situation( Situation(v, None) )

		self.evaluate_rule( ctxt, rule_ctxt )
		return

	def evaluate_rule(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if (self.automata is None)  or (self.sitations.empty()):
			self.sitations.queue.clear()
			return

		resolver	= rule_ctxt.resolver

		while self.sitations.empty() == False:
			# Assign a new situation to the rule contxt
			rule_ctxt.situation	= self.sitations.get()

			# Reset the resolver with the new context properties
			resolver.reset( ctxt, rule_ctxt )

			# Evaluate the automata
			result		= self.automata.evaluate(rule_ctxt)
			if result.error is None:
				continue

			for err in result.error:
				self.on_violate( ctxt, rule_ctxt, err.parent.name )

		return

	def on_violate(self, ctxt:Context, rule_ctxt:RuleContext, clausename:str):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			err -- Error attribute
		"""
		os		= rule_ctxt.situation.os
		ts		= rule_ctxt.situation.ts
		imo		= int(os.imo)
		score	= self.scorecard.evaluate(clausename) 
		if score is None:
			return
		
		now		= ctxt.sim.now()
		fact	= score.get('fact', 'InlandWaterViolation.generic')
		concern	= score.get('concern', 'Generic')
		penalty	= score.get('penalty', 0)
		filter 	= score.get('filter', [])


		# Match the vessel if a filter is specified.
		if len(filter):
			if os.id not in filter:
				return

		# Log the error in the database
		# self.data(ctxt, fact, [os.recid, ts.recid if ts is not None else 0, now, now])
		self.data(ctxt, 'ro', [f'\'{concern}\'',now, imo, penalty])

		# Override the function to score the violation
		ctxt.log.error( self.regulation, f'Violated clause {clausename} for {concern}')
		return

	def on_overtaking(self, ctxt:Context, evt):
		""" Event handler for overtaking
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		#self.add_situation( Situation(evt[2].OS, evt[2].TS) )
		return

	def on_crossing(self, ctxt:Context, evt):
		""" Event handler for crossing
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		#print( f'{self.__class__.__name__}.crossing:{evt[2].OS.config["name"]}' )
		#self.add_situation( Situation(evt[2].OS, evt[2].TS) )
		return

	def on_close_encounter(self, ctxt:Context, evt):
		""" Event handler for close encounters
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		self.add_situation( Situation(evt[1], evt[2]) )
		return
		

if __name__ == "__main__":
	test = InlandWaterRule()

