#!/usr/bin/python
# Filename: VesselResolver.py
# Description: Implementation of the VesselResolver class

from maritime.model.resolver.VesselResolver import VesselResolver
from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.model.vehicle.Vehicle import Vehicle
from cos.math.geometry.Distance import Distance
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class TargetShipResolver(VesselResolver):
	def __init__(self, resolver=None, TS:Vessel=None):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			TS -- Target ship
		"""
		VesselResolver.__init__(self, TS,'TargetShip.')
		self.os			= None
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		"""
		self.velocity	= None
		self.heading	= None

		if rulectxt.situation is not None:
			self.vessel		= rulectxt.situation.ts
			self.os			= rulectxt.situation.os
		else:
			self.vessel		= None
			self.os			= None
		return

	@simproperty
	def RelativeSize(self):
		""" Symbol property - RelativeSize, the target ship's size relative to
		the own ship, by displacement weight
		"""
		if (self.vessel is None) or (self.os is None):
			return None

		return 'large' if self.vessel.weight >= self.os.weight else 'small'

	@simproperty
	def FogSignal(self):
		""" Symbol property - FogSignal, whether the target ship is sounding its fog signal
		"""
		if self.vessel is None:
			return None

		return self.vessel.is_signaled('Signal', 'FogHorn')

	@simproperty
	def PersonsOnBoard(self):
		""" Symbol property - PersonsOnBoard

		Not part of the vessel's core schema (Vessel.__init__ has no field for
		it), so it comes from the free-form 'settings' string the same way
		ZoneRules.overrides() reads per-shape overrides, defaulting to none
		declared rather than failing the resolve.
		"""
		if self.vessel is None:
			return None

		settings	= ArgList( self.vessel.config.get('settings', '') )
		return settings.ToInt( 'persons_on_board', 0 )

if __name__ == "__main__":
	test = TargetShipResolver()

