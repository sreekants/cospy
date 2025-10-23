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
	def __init__(self, resolver=None, vessel:Vessel=None, harbour:Harbour=None):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			vessel -- Own ship
			harbour -- Harbour
		""" 
		MaritimeZoneResolver.__init__(self, vessel, harbour, '[OwnShip,Harbour]')
		return

	@property
	def harbour(self):
		""" TODO: harbour
		""" 
		return self.zone

if __name__ == "__main__":
	test = HarbourResolver()

