#!/usr/bin/python
# Filename: Obstruction.py
# Description: Implementation of the Obstruction class

from maritime.core.situation.MaritimeConductSituation import MaritimeConductSituation
from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation as RuleSituation
from cos.model.rule.Context import Context as RuleContext

class Obstruction(MaritimeConductSituation):
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
		self.for_each_in_range( ctxt, rule_ctxt,
				self.range,
				rule_ctxt.vessels,
				rule_ctxt.vessels,
				self.on_obstruct )

		self.for_each_in_range( ctxt, rule_ctxt,
				self.range,
				rule_ctxt.vessels,
				rule_ctxt.bodies,
				self.on_obstruct )
		return

	def setup(self, ctxt:Context, config):
		""" Sets up the parameters of the situation
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Overridable implementation
		self.range	= 5
		return

	def on_obstruct(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler for obstruct
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		lhs		= info[0]
		rhs		= info[1]

		# print( f'OBSTRUCTION! {lhs.config["name"]} and {rhs.config["name"]} at distance {info[2]:0.2}')
		return

if __name__ == "__main__":
	test = Obstruction("XXX")


