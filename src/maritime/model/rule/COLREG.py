#!/usr/bin/python
# Filename: COLREG.py
# Description: Base class for all COLREG rules

from cos.model.rule.Rule import Rule
from cos.model.rule.Automata import Automata
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.model.logic.Decision import Decision

import queue, fnmatch

class COLREG(Rule):
	def __init__(self):
		""" Constructor
		"""
		Rule.__init__(self, "COLREG")

		self.sitations	= queue.Queue()
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

		return

	def on_violate(self, ctxt:Context, rule_ctxt:RuleContext, err:Decision):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			err -- Error attribute
		"""

		# Override the function to score the violation
		ctxt.log.error( 'COLREG', f'Violated rule {err}')
		return

if __name__ == "__main__":
	test = COLREG()


