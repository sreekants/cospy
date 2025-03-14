#!/usr/bin/python
# Filename: MEZResolver.py
# Description: Implementation of the MEZResolver class

from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.resolver.ZoneResolver import MaritimeZoneResolver
from maritime.model.geography.MaritimeExclusionZone import MaritimeExclusionZone
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class MEZResolver(MaritimeZoneResolver):
	def __init__(self, resolver=None, vessel:Vessel=None, MEZ:MaritimeExclusionZone=None):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			vessel -- Own ship
			MEZ -- Exclusion zone 
		""" 
		MaritimeZoneResolver.__init__(self, vessel, MEZ, '[OwnShip,MaritimeExclusionZone]')
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		""" 
		if rulectxt.situation is not None:
			self.zone	= rulectxt.situation.mez
		else:
			self.zone	= None
		return

	@property
	def mez(self):
		""" TODO: mez
		""" 
		return self.zone

if __name__ == "__main__":
	test = MEZResolver()

