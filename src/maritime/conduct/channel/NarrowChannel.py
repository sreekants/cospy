#!/usr/bin/python
# Filename: NarrowChannel.py
# Description: Implementation of the NarrowChannel class

from maritime.core.situation.MaritimeConductSituation import MaritimeConductSituation
from cos.model.rule.Situation import Situation as RuleSituation
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

class NarrowChannel(MaritimeConductSituation):
	def __init__(self):
		""" Constructor
		Arguments
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
		""" Sets up the parameters of the situations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Overridable implementation
		return


if __name__ == "__main__":
	test = NarrowChannel("XXX")


