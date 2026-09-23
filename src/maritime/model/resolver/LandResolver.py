#!/usr/bin/python
# Filename: LandResolver.py
# Description: Implementation of the LandResolver class

from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

# How far ahead the own ship's current course is projected to decide whether
# it is heading for land. Matches the order of magnitude of the other
# look-ahead placeholders in this vocabulary (see TargetResolver.TimeToEncounter).
GROUNDING_HORIZON = 300.0		# seconds

class LandResolver(Resolver):
	def __init__(self, resolver):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
		"""
		Resolver.__init__(self, '(OwnShip,Map.Land).')

		self.land		= None
		self.os			= None
		return


	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		"""
		situation	= rulectxt.situation
		self.os		= situation.os if situation is not None else None

		# The map is built once at startup, so the shape list is fetched only
		# the first time it is needed rather than on every reset.
		if self.land is None:
			self.land	= ctxt.sim.objects.get_all( "/World/Land" ) or []
		return

	@simproperty
	def Distance(self):
		""" Simulation property: distance from the own ship to the nearest land boundary
		"""
		if (self.os is None) or (len(self.land) == 0):
			return None			# Unresolved: the bound node keeps its prior

		x, y	= self.os.location[0], self.os.location[1]
		return min( shape.area.clearance(x, y) for shape in self.land )

	@simproperty
	def OnGroundingCourse(self):
		""" Simulation property: whether the own ship's current course runs into land
		"""
		if (self.os is None) or (len(self.land) == 0):
			return False

		x, y	= self.os.location[0], self.os.location[1]
		vx, vy	= self.os.velocity[0], self.os.velocity[1]
		future	= (x + vx*GROUNDING_HORIZON, y + vy*GROUNDING_HORIZON)

		for shape in self.land:
			if shape.contains( future ):
				return True

		return False

if __name__ == "__main__":
	test = LandResolver()

