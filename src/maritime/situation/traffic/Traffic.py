#!/usr/bin/python
# Filename: Traffic.py
# Description: Implementation of the Traffic class

from maritime.core.situation.MaritimeConductSituation import MaritimeConductSituation
from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation as RuleSituation
from cos.model.rule.Context import Context as RuleContext

class Traffic(MaritimeConductSituation):
	def __init__(self):
		""" Constructor
		Arguments
			self -- reference to this instance
		"""
		MaritimeConductSituation.__init__( self )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.setup(ctxt, config)
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		return

	def setup(self, ctxt:Context, config):
		""" Sets up the parameters of the situation
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Overridable implementation
		return

if __name__ == "__main__":
	test = Traffic("XXX")


