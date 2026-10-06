#!/usr/bin/python
# Filename: ZoneRule.py
# Description: Implementation of the generic maritime zone rule class: a Legata rule set for any zone types

from maritime.model.rule.InlandWaterRule import InlandWaterRule
from cos.core.kernel.Context import Context
from cos.model.rule.Rule import Rule
from cos.core.utilities.ArgList import ArgList
from cos.model.rule.Context import Context as RuleContext

class ZoneRule(InlandWaterRule):
	def __init__(self):
		""" Constructor
		"""
		InlandWaterRule.__init__(self, 'Internal.Zone')
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule, loading its configurations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes: types=<Sea.Type names, comma separated> zonekey=<key pattern>
				automata=<.legata file> scorecard=<score.yaml>
		"""
		Rule.setup(self, ctxt, config)

		types	= config['types']
		if not types:
			raise ValueError( f'{self.__class__.__name__}: types= names no zone types' )

		# Create a list of the relevant zones
		InlandWaterRule.setup_zone(self, ctxt, config, [t.strip() for t in str(types).split(',') if t.strip()])
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		return InlandWaterRule.evaluate(self, ctxt, rule_ctxt)


if __name__ == "__main__":
	test = ZoneRule()
