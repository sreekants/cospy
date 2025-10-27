#!/usr/bin/python
# Filename: GenericRule.py
# Description: Implementation of the generic maritime harbor rule class

from maritime.model.rule.InlandWaterRule import InlandWaterRule
from cos.core.kernel.Context import Context
from cos.model.rule.Rule import Rule
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class TrafficSeparationSchemeRule(InlandWaterRule):
	def __init__(self):
		""" Constructor
		"""
		InlandWaterRule.__init__(self, 'Internal.TrafficSeparationScheme')
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule, loading its configurations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Rule.setup(self, ctxt, config)

		# Create a list of the relevant zones
		InlandWaterRule.setup_zone(self, ctxt, config, 'TRAFFIC_LANE')
		return
		

if __name__ == "__main__":
	test = HarbourRule()

