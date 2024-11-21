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
		""" TODO: Intent
		""" 
		return ['Operation.Lookout.XXX']

	@simproperty
	def Type(self):
		""" TODO: Type
		""" 
		return self.vessel.type

	@simproperty
	def EngineState(self):
		""" TODO: EngineState
		""" 
		return 'Engine.State.ON'

	@simproperty
	def Position(self):
		""" TODO: Position
		""" 
		return self.vessel.location

	@simproperty
	def Velocity(self)->float:
		""" TODO: Velocity
		""" 
		if self.velocity is None:
			V				= self.vessel.velocity
			self.velocity	= math.sqrt(V[0]**2+V[1]**2)

		return self.velocity

	@simproperty
	def Acceleration(self)->float:
		""" TODO: Acceleration
		""" 
		return self.vessel.acceleration

	@simproperty
	def Heading(self)->float:
		""" TODO: Heading
		""" 
		if self.heading is None:
			self.heading	= self.vessel.heading

		return self.heading


if __name__ == "__main__":
	test = VesselResolver()

