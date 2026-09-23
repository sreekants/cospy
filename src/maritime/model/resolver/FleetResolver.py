#!/usr/bin/python
# Filename: FleetResolver.py
# Description: Implementation of the FleetResolver class

from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.math.geometry.Distance import Distance
from cos.math.geometry.Vector import Vector
from cos.math.geometry.Position import Position
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class FleetResolver(Resolver):
	def __init__(self, resolver):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
		"""
		Resolver.__init__(self, '(OwnShip,Fleet).')

		self.os			= None
		self.fleet		= None
		self.nearest	= None
		return


	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		"""
		self.nearest	= None

		situation		= rulectxt.situation
		if situation is None:
			self.os		= None
			self.fleet	= None
			return

		self.os		= situation.os

		# While an encounter is in scope, the AUV link of interest is the target
		# ship's escort rather than the own ship's, mirroring how TargetResolver
		# switches context for the duration of the encounter.
		if situation.ts is not None:
			self.fleet	= situation.ts.fleet
		else:
			self.fleet	= None
		return

	@simproperty
	def Distance(self):
		""" Simulation property: horizontal distance to the nearest vessel in the fleet
		"""
		vessel	= self.GetNearestVessel()
		if vessel is None:
			return None		# Unresolved: the bound node keeps its prior

		return Distance.euclidean(self.os.location, vessel.location)

	@simproperty
	def MinimumDepth(self):
		""" Simulation property: smallest vertical separation to the nearest vessel in the fleet
		"""
		vessel	= self.GetNearestVessel()
		if vessel is None:
			return None		# Unresolved: the bound node keeps its prior

		return abs(self.os.location[2] - vessel.location[2])

	def GetNearestVessel(self):
		""" Finds the fleet vessel closest to the own ship, caching the result
		for the remainder of this resolve cycle.
		"""
		if self.nearest is not None:
			return self.nearest

		if self.os is None:
			return None

		best, bestdist	= None, None

		for vessel in self.__members():
			if (vessel is None) or (vessel is self.os) or (vessel.location is None):
				continue

			d	= Distance.euclidean(self.os.location, vessel.location)
			if (bestdist is None) or (d < bestdist):
				best, bestdist	= vessel, d

		self.nearest	= best
		return self.nearest

	def __members(self):
		""" Normalizes situation.fleet into a flat list of vessels.

		situation.fleet has no established shape yet - nothing in the conduct
		tree assigns it (see RiskExaminer.requirements.md COM-X-04) - so this
		accepts whatever a future assignment turns out to produce: a bare
		vessel, an iterable of vessels, or an iterable of (vessel, type, id)
		tuples as FleetBehavior builds internally.
		"""
		fleet	= self.fleet
		if fleet is None:
			return []

		if not isinstance(fleet, (list, tuple, set)):
			return [fleet]

		return [ item[0] if isinstance(item, tuple) else item for item in fleet ]

if __name__ == "__main__":
	test = FleetResolver()

