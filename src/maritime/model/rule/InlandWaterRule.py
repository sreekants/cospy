#!/usr/bin/python
# Filename: GenericRule.py
# Description: Implementation of the generic maritime inland waters rule class

from cos.model.rule.Rule import Rule
from cos.model.rule.Automata import Automata
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.core.utilities.ArgList import ArgList
from cos.model.logic.Decision import Decision
from cos.model.rule.Situation import Situation

import queue, fnmatch



class InlandWaterRule(Rule):
	def __init__(self, zonetype):
		""" Constructor
		Arguments
			type -- Zone type
		"""
		Rule.__init__(self, None)

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
				if h.config['key'] == zonekey:
					self.zones.append(h)
		else:
			self.zones	= zones
		

		return


	def add_situation(self, situation):
		""" TODO: add_situation
		Arguments
			situation -- TODO
		""" 
		self.sitations.put(situation)
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
			for z in self.zones:
				if z.intersect(v.boundary):
					evt			= Situation(v, None)
					evt.zone	= z
					self.add_situation( evt )


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
		imo		= int(rule_ctxt.situation.os.imo)
		score	= self.scorecard.evaluate(clausename) 
		if score is None:
			return
		
		now		= ctxt.sim.clock.utc
		fact	= score["fact"]
		concern	= score["concern"]
		penalty	= score["penalty"]

		self.data(ctxt, fact, [now,10000,now, imo, penalty])
		self.data(ctxt, 'ro', [now,10000,f'\'{concern}\'',now, imo, penalty])

		# Override the function to score the violation
		ctxt.log.error( self.regulation, f'Violated clause {clausename} for {concern}')
		return

		

if __name__ == "__main__":
	test = InlandWaterRule()

