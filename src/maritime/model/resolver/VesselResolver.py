#!/usr/bin/python
# Filename: VesselResolver.py
# Description: Implementation of the VesselResolver class

from maritime.model.vessel.Vessel import Vessel, Status, Operation
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
		self.acceleartion	= None
		return

	@simproperty
	def Intent(self):
		""" Returns the vessel intent property set
		""" 
		return self.vessel.intent

	@simproperty
	def Signal(self):
		""" Lights, shapes and sound signals the vessel is showing (REQ.036)
		"""
		return getattr( self.vessel, 'signal', None )

	@simproperty
	def Signal_ON(self):
		""" Signals shown, as COLREG Rules 23-25 name them: OS.Signal.ON has 'Light.Sidelight'
		"""
		return self.Signal()

	@simproperty
	def Mode(self):
		""" Returns the vessel intent property set
		""" 
		return self.vessel.intent

	@simproperty
	def Type(self):
		""" The vessel's Type enum, as Vessel.Type.PowerDriven resolves
		""" 
		return getattr( self.vessel, 'vessel_type', self.vessel.type )

	@simproperty
	def Status(self):
		""" Navigational status, e.g. Vessel.Status.ANCHORED
		"""
		return self.vessel.status

	@simproperty
	def Operation(self):
		""" Operation the vessel is engaged in, e.g. Vessel.Operation.FISHING
		"""
		value	= self.vessel.operation
		return Operation(value) if isinstance(value, int) else value

	@simproperty
	def Restriction(self):
		""" Restriction on the vessel's ability to manoeuvre, e.g. Vessel.Restriction.DRAUGHT
		"""
		return self.vessel.restriction

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
		if self.acceleartion is None:
			A				= self.vessel.acceleration
			self.acceleration	= math.sqrt(A[0]**2+A[1]**2)
		return self.acceleration

	@simproperty
	def Heading(self)->float:
		""" Returns the heading
		""" 
		if self.heading is None:
			self.heading	= self.vessel.heading
			if self.heading < 0:
				self.heading	= self.heading + 360

		return self.heading

	@simproperty
	def Position_Territory(self):
		""" Symbol property - Position.Territory
		""" 
		return 'Territory.HighSea'

	@simproperty
	def Draft(self):
		""" Returns the draft
		""" 
		return self.vessel.model.draft if self.vessel.model is not None else 0.0

	@simproperty
	def Mass(self):
		""" Displacement in tonnes, the vessel's own or its category's
		""" 
		return getattr( self.vessel, 'weight', None )

	@simproperty
	def Length(self):
		""" Returns the draft
		""" 
		return self.vessel.model.ship.length if self.vessel.model is not None else 0.0

	@simproperty
	def Width(self):
		""" Returns the draft
		""" 
		return self.vessel.model.ship.width if self.vessel.model is not None else 0.0

if __name__ == "__main__":
	test = VesselResolver()

