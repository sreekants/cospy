#!/usr/bin/python
# Filename: ZoneResolver.py
# Description: Implementation of the ZoneResolver class

from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.geography.TrafficSeparationScheme import TrafficSeparationScheme
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np

class ZoneResolver(Resolver):
	def __init__(self, vessel:Vessel, zone:TrafficSeparationScheme, prefix:str=None):
		""" Constructor
		Arguments
			vessel -- TODO
			zone -- TODO
			prefix -- TODO
		""" 
		Resolver.__init__(self, prefix)

		self.zone		= zone
		self.vessel		= vessel
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		self.zone		= None
		self.vessel		= None
		return

	@simproperty
	def InRange(self):
		""" TODO: InRange
		""" 
		if self.zone is None:
			return False
		return self.zone.contains( self.vessel.location )

	@simproperty
	def SafeDistance(self):
		""" TODO: SafeDistance
		""" 
		if self.zone is None:
			return 0.0
		return self.zone.safe_distance

	@simproperty
	def SafeHeading(self):
		""" TODO: SafeHeading
		""" 
		if self.zone is None:
			return 0.0

		return self.zone.safe_heading


class MaritimeZoneResolver(ZoneResolver):
	def __init__(self, vessel:Vessel, zone:TrafficSeparationScheme, prefix:str=None):
		""" Constructor
		Arguments
			vessel -- TODO
			zone -- TODO
			prefix -- TODO
		""" 
		ZoneResolver.__init__(self, vessel, zone, prefix)
		return


if __name__ == "__main__":
	test = ZoneResolver()

