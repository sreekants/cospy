#!/usr/bin/python
# Filename: VesselResolver.py
# Description: Implementation of the VesselResolver class

from maritime.model.resolver.VesselResolver import VesselResolver
from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.model.vehicle.Vehicle import Vehicle
from cos.math.geometry.Distance import Distance
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math


class OwnShipResolver(VesselResolver):
	def __init__(self, resolver=None, OS:Vessel=None):
		""" Constructor
		Arguments
			OS -- TODO
		""" 
		VesselResolver.__init__(self, OS,'OwnShip.')
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		self.velocity	= None
		self.heading	= None

		if rulectxt.situation is not None:
			self.vessel		= rulectxt.situation.os
		else:
			self.vessel		= None
		return


if __name__ == "__main__":
	test = OwnShipResolver()

