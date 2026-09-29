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
from maritime.model.rule.ScoredRule import ScoredRule
from maritime.model.zone.Ledger import SOURCE_LOCAL

from typing import Any
import queue, fnmatch



class InlandWaterRule(ScoredRule, Rule):
	SOURCE		= SOURCE_LOCAL

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

	def setup_zone(self, ctxt:Context, config:ArgList, typelist):
		""" Sets up the rule, loading its configurations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
			typelist -- Types of zones to watch
		"""
		Rule.setup(self, ctxt, config)
		self.init_scoring( ctxt )
		self.check_scorecard( ctxt )

		zonekey		= config['zonekey']
		objmgr		= ctxt.sim.objects

		# A single type name, not a string to iterate by character
		if isinstance( typelist, str ):
			typelist	= [ typelist ]

		zones		= []
		for typename in typelist:
			z	= objmgr.get_all(f"/World/Sea/{typename}")
			zones.extend(z)

		# Match keys to all zones
		if zonekey is not None:
			self.zones	= []
			for h in zones:
				if fnmatch.fnmatch(h.config['key'], zonekey):
					self.zones.append(h)
		else:
			self.zones	= zones
		

		return

	def check_scorecard(self, ctxt:Context):
		""" Checks every priced clause names a concern that maps into the vocabulary
		Arguments
			ctxt -- Simulation context
		"""
		problems	= []
		for clause, entry in self.scorecard.scores.items():
			named	= (entry or {}).get( 'concern' )
			if named is None:
				problems.append( f'clause {clause!r} names no concern' )
			elif self.ledger.rules.concern( named ) is None:
				problems.append( f'clause {clause!r} names {named!r}, which maps to no concern' )

		for problem in problems:
			ctxt.log.error( self.regulation, f'Scorecard: {problem}' )

		if problems:
			raise ValueError( f'{self.regulation}: {len(problems)} scorecard problem(s)' )
		return


	def add_situation(self, evt):
		""" TODO: add_situation
		Arguments
			evt -- TODO
		""" 
		if not self.zones:
			return
		
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
		
		for v in rule_ctxt.subjects:
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

		# The situation is shared by every rule and examiner in the pass (COS.007)
		saved		= rule_ctxt.situation

		try:
			while self.sitations.empty() == False:
				# Assign a new situation to the rule contxt
				rule_ctxt.situation	= self.sitations.get()

				#if rule_ctxt.situation.zone.name == 'Turkeli.TSS.SpeedZone1':

				# Reset the resolver with the new context properties
				resolver.reset( ctxt, rule_ctxt )

				# Evaluate the automata
				result		= self.automata.evaluate(rule_ctxt)
				if result.error is None:
					continue

				for err in result.error:
					self.on_violate( ctxt, rule_ctxt, err.parent.name )

		finally:
			rule_ctxt.situation	= saved
			resolver.reset( ctxt, rule_ctxt )

		return

	def on_violate(self, ctxt:Context, rule_ctxt:RuleContext, clausename:str):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			err -- Error attribute
		"""
		situation	= rule_ctxt.situation
		os			= situation.os

		score		= self.score( ctxt, situation, clausename )
		if score is None:
			self.note_unpriced( ctxt, clausename )
			return

		# Match the vessel if a filter is specified.
		filter 		= score.get('filter', [])
		if len(filter):
			if os.id not in filter:
				return

		zone		= getattr( situation, 'zone', None )
		self.record_violation( ctxt, self.regulation, os, clausename,
							   getattr(zone, 'name', None), score['penalty'], score.get('concern') )
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

