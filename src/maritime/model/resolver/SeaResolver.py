#!/usr/bin/python
# Filename: SeaResolver.py
# Description: Implementation of the SeaResolver class

from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.zone.ZoneRules import ZoneRules
from maritime.model.zone.Location import Location
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class SeaResolver(Resolver):
	def __init__(self, resolver):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
		"""
		Resolver.__init__(self, '(OwnShip,Map.Sea).')

		# Unloaded - only the shape-geometry helpers (seabed_depth) are used
		# here, which need no zones.yaml, unlike ZoneAware's copy.
		self.rules		= ZoneRules()
		self.sea		= None
		self.os			= None
		self.shapes		= None
		self.location	= None
		self.ctxt		= None
		return


	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		"""
		situation	= rulectxt.situation
		self.os		= situation.os if situation is not None else None
		self.shapes	= None

		# The map is built once at startup, so the shape list is fetched only
		# the first time it is needed rather than on every reset.
		if self.sea is None:
			self.sea	= ctxt.sim.objects.get_all( "/World/Sea" ) or []
		self.ctxt	= ctxt
		return

	@simproperty
	def WaveHeight(self)->float:
		""" Simulation property: WaveHeight

		No live sea-state feed is wired into the simulation yet, so this
		reports calm water rather than leaving the term unresolved.
		"""

		return 0.0

	@simproperty
	def WindSpeed(self)->float:
		""" Simulation property: WindSpeed

		No live weather feed is wired into the simulation yet, so this reports
		still air rather than leaving the term unresolved.
		"""

		return 0.0

	@simproperty
	def Depth(self):
		""" Simulation property: shallowest seabed depth beneath the own ship, else the nominal depth
		"""
		if self.os is None:
			return None			# Unresolved: the bound node keeps its prior

		if self.location is None:
			self.location	= Location.shared( self.ctxt )
		return self.location.seabed_depth( self.rules.seabed_depth(self.__enclosing()) )

	def __enclosing(self):
		""" Map shapes enclosing the own ship, cached for this resolve cycle
		"""
		if self.shapes is None:
			position	= self.os.location if self.os is not None else None
			self.shapes	= ZoneRules.enclosing( self.sea, position )

		return self.shapes

if __name__ == "__main__":
	test = SeaResolver()

