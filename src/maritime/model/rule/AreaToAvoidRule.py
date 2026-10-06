#!/usr/bin/python
# Filename: GenericRule.py
# Description: Implementation of the generic maritime harbor rule class

from maritime.model.rule.InlandWaterRule import InlandWaterRule
from cos.model.rule.Rule import Rule
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.core.utilities.ArgList import ArgList

class AreaToAvoidRule(InlandWaterRule):
	def __init__(self):
		""" Constructor
		"""
		InlandWaterRule.__init__(self, 'Internal.AreaToAvoid')
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule, loading its configurations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Rule.setup(self, ctxt, config)

		# Create a list of the relevant zones
		InlandWaterRule.setup_zone(self, ctxt, config, 'AREA_TO_AVOID')
		return

	def evaluate_rule(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.automata is not None:
			return InlandWaterRule.evaluate_rule( self, ctxt, rule_ctxt )

		# No rule set: every vessel inside an area to avoid is a NO_ENTRY violation
		saved	= rule_ctxt.situation
		try:
			while not self.sitations.empty():
				rule_ctxt.situation	= self.sitations.get()
				if rule_ctxt.situation.zone.contains( rule_ctxt.situation.os.location ):
					self.on_violate( ctxt, rule_ctxt, 'NO_ENTRY' )
		finally:
			rule_ctxt.situation	= saved
		return



if __name__ == "__main__":
	test = AreaToAvoidRule()

