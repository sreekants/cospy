#!/usr/bin/python
# Filename: TargetResolver.py
# Description: Implementation of the TargetResolver class

from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.model.rule.Context import Context
from cos.model.vehicle.Vehicle import Vehicle
from cos.math.geometry.Distance import Distance
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

import inspect


class TargetResolver(Resolver):
	def __init__(self, OS:Vehicle=None, TS:Vehicle=None, range:float=0.0 ):
		""" Constructor
		Arguments
			OS -- TODO
			TS -- TODO
			range -- TODO
		""" 
		Resolver.__init__(self, '(OwnShip,TargetShip).')

		self.OS			= OS
		self.TS			= TS
		self.range		= range
		self.distance	= None
		self.velocity	= None
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		self.range		= 0.0
		self.distance	= None
		self.velocity	= None
		situation		= rulectxt.situation

		if situation is not None:
			self.OS			= situation.os
			self.TS			= situation.ts
		else:
			self.OS			= None
			self.TS			= None
		return

		return

	def is_valid(self):
		""" TODO: is_valid
		""" 
		if (self.OS is None) or (self.OS is None):
			return False

		return True

	@simproperty
	def InRange(self):
		""" Symbol property - InRange
		""" 
		return self.Distance() <= self.range

	@simproperty
	def OutOfRange(self):
		""" Symbol property - OutOfRange
		""" 
		return self.Distance() > self.range

	@simproperty
	def Distance(self):
		""" Symbol property - Distance
		""" 
		if self.distance is None:
			self.distance	= Distance.euclidean(self.OS.location, self.TS.location)
		return self.distance

	@simproperty
	def Velocity(self)->float:
		""" Symbol property - Velocity
		""" 
		if self.velocity is None:
			Vos				= self.OS.velocity
			self.velocity	= math.sqrt(Vos[0]**2+Vos[1]**2)

		return self.velocity

	@simproperty
	def Approach(self)->float:
		""" Symbol property - Approach
		""" 
		todeg		= 180/np.pi
		Vos			= self.OS.velocity
		Vts			= self.TS.velocity
		return math.atan2( Vos[1]-Vts[1], Vos[0]-Vts[0] )*todeg

	@simproperty
	def Cargo(self)->str:
		""" Symbol property - Cargo
		""" 

		return self.OS.cargo


	@simproperty
	def Draught(self)->str:
		""" Symbol property - Draught
		""" 
		clearance		= self.OS.underkeel_clearance + \
						  self.OS.motion_allowance + \
						  self.OS.squat

		return clearance
	@simproperty
	def Weight(self)->float:
		""" Symbol property - Weight
		""" 

		return self.OS.weight

	@simproperty
	def Undercurrent(self)->float:
		""" Symbol property - Undercurrent
		""" 

		return 400

	@simproperty
	def TargetVelocity(self)->float:
		""" Symbol property - TargetVelocity
		""" 
		Vts			= self.TS.velocity
		return math.sqrt(Vts[0]**2+Vts[1]**2)

	@simproperty
	def TargetApproach(self)->float:
		""" Symbol property - TargetApproach
		""" 
		todeg		= 180/np.pi
		Vos			= self.OS.velocity
		Vts			= self.TS.velocity
		return math.atan2( Vts[1]-Vos[1], Vts[0]-Vos[0] )*todeg

	@simproperty
	def Detect(self):
		""" Symbol property - Detect
		""" 
		return ['Signal.FogHorn']

	@simproperty
	def Position(self):
		""" Symbol property - Position
		""" 
		return 'Position.Abeam'

	@simproperty
	def TimeToEncounter(self):
		""" Symbol property - TimeToEncounter
		""" 
		return 1000

	@simproperty
	def Visible(self):
		""" Symbol property - Visible
		""" 
		return True

if __name__ == "__main__":
	test = TargetResolver()

