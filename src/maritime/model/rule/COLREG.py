#!/usr/bin/python
# Filename: COLREG.py
# Description: Base class for all COLREG rules

from cos.model.rule.Rule import Rule
from cos.model.rule.Automata import Automata
from maritime.model.rule.ScoredRule import ScoredRule
from maritime.model.zone.Ledger import Ledger, SOURCE_COLREG
from cos.core.utilities.ArgList import ArgList
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.lang.logic.Decision import Decision

import queue, fnmatch

class COLREG(ScoredRule, Rule):
	SOURCE		= SOURCE_COLREG

	def __init__(self):
		""" Constructor
		"""
		Rule.__init__(self, "COLREG")

		self.sitations	= queue.Queue()
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule, loading its automata and joining the ledger
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Rule.setup( self, ctxt, config )
		self.init_scoring( ctxt )
		return

	def begin(self, ctxt:Context, rule_ctxt):
		""" Triggers the begining of a situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		Rule.begin(self, ctxt, rule_ctxt)

		if self.automata is not None:
			self.automata.begin(rule_ctxt)			
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		Rule.evaluate(self, ctxt, rule_ctxt)

		self.__evaluate_rule( ctxt, rule_ctxt )
		return

	def add_situation(self, situation):
		""" TODO: add_situation
		Arguments
			situation -- TODO
		""" 
		self.sitations.put(situation)
		return

	def __evaluate_rule(self, ctxt:Context, rule_ctxt:RuleContext):
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

				# Reset the resolver with the new context properties
				resolver.reset( ctxt, rule_ctxt )

				# Evaluate the automata
				result		= self.automata.evaluate(rule_ctxt)
				if result.error is None:
					continue

				for err in result.error:
					self.on_violate( ctxt, rule_ctxt, err )

		finally:
			rule_ctxt.situation	= saved
			resolver.reset( ctxt, rule_ctxt )

		return

	def score(self, ctxt:Context, situation, event:str):
		""" Prices a violated clause
		Arguments
			ctxt -- Simulation context
			situation -- Situation reference
			event -- Name of the violated clause
		Returns
			The scorecard entry, or None when the clause is unpriced
		Note
			The rule's own scorecard wins; otherwise the penalties in zones.yaml
		"""
		entry	= Rule.score( self, ctxt, situation, event )
		if entry is not None:
			return entry

		penalty	= self.ledger.rules.penalty( event )
		if penalty <= 0.0:
			return None

		return {'penalty': penalty}

	def on_violate(self, ctxt:Context, rule_ctxt:RuleContext, err:Decision):
		""" Scores and records a violated clause
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			err -- The failed decision
		"""
		clause		= self.clause_name( err )
		situation	= rule_ctxt.situation

		entry		= self.score( ctxt, situation, clause )
		if entry is None:
			self.note_unpriced( ctxt, clause )
			return

		# One finding per encounter
		target		= getattr( situation, 'ts', None )
		subject		= Ledger.identify( target ) if target is not None else None

		self.record_violation( ctxt, self.__class__.__name__, situation.os, clause, subject,
							   entry['penalty'], entry.get('concern') )
		return

if __name__ == "__main__":
	test = COLREG()


