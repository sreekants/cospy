#!/usr/bin/python
# Filename: HarbourResolver.py
# Description: Implementation of the HarbourResolver class

from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.resolver.ZoneResolver import MaritimeZoneResolver
from maritime.model.geography.Harbour import Harbour
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class HarbourResolver(MaritimeZoneResolver):
	def __init__(self, vessel:Vessel=None, harbour:Harbour=None):
		""" Constructor
		Arguments
			vessel -- TODO
			harbour -- TODO
		""" 
		MaritimeZoneResolver.__init__(self, vessel, harbour, '[OwnShip,Harbour]')
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		if rulectxt.situation is not None:
			self.zone	= rulectxt.situation.harbour
		else:
			self.zone	= None
		return

	@property
	def harbour(self):
		""" TODO: harbour
		""" 
		return self.zone

if __name__ == "__main__":
	test = HarbourResolver()

