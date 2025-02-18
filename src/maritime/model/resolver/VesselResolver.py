#!/usr/bin/python
# Filename: VesselResolver.py
# Description: Implementation of the VesselResolver class

from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.model.vehicle.Vehicle import Vehicle
from cos.math.geometry.Distance import Distance
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class VesselResolver(Resolver):
	def __init__(self, vessel:Vessel, prefix:str):
		""" Constructor
		Arguments
			vessel -- TODO
			prefix -- TODO
		""" 
		Resolver.__init__(self, prefix)


		self.vessel		= vessel
		self.velocity	= None
		self.heading	= None
		return

	@simproperty
	def Intent(self):
		""" Returns the vessel intent property set
		""" 
		return self.vessel.intent

	@simproperty
	def Type(self):
		""" Returns the type of the vessel
		""" 
		return self.vessel.type

	@simproperty
	def EngineState(self):
		""" Returns the Engine state
		""" 
		return self.vessel.engine.state

	@simproperty
	def Position(self):
		""" Returns the position
		""" 
		return self.vessel.location

	@simproperty
	def Velocity(self)->float:
		""" Returns the velocity
		""" 
		if self.velocity is None:
			V				= self.vessel.velocity
			self.velocity	= math.sqrt(V[0]**2+V[1]**2)

		return self.velocity

	@simproperty
	def Acceleration(self)->float:
		""" Returns the acceleration
		""" 
		return self.vessel.acceleration

	@simproperty
	def Heading(self)->float:
		""" Returns the heading
		""" 
		if self.heading is None:
			self.heading	= self.vessel.heading

		return self.heading


if __name__ == "__main__":
	test = VesselResolver()

