#!/usr/bin/python
# Filename: EEZResolver.py
# Description: Implementation of the EEZResolver class

from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.resolver.ZoneResolver import MaritimeZoneResolver
from maritime.model.geography.ExclusiveEconomicZone import ExclusiveEconomicZone
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class EEZResolver(MaritimeZoneResolver):
	def __init__(self, vessel:Vessel=None, EEZ:ExclusiveEconomicZone=None):
		""" Constructor
		Arguments
			vessel -- TODO
			EEZ -- TODO
		""" 
		MaritimeZoneResolver.__init__(self, vessel, EEZ, '[OwnShip,EEZ]')
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		if rulectxt.situation is not None:
			self.zone	= rulectxt.situation.eez
		else:
			self.zone	= None
		return

	@property
	def eez(self):
		""" TODO: eez
		""" 
		return self.zone

if __name__ == "__main__":
	test = EEZResolver()
