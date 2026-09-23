#!/usr/bin/python
# Filename: TargetResolver.py
# Description: Implementation of the TargetResolver class

from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.model.rule.Context import Context
from cos.model.vehicle.Vehicle import Vehicle
from cos.math.geometry.Distance import Distance
from cos.math.geometry.Vector import Vector
from cos.math.geometry.Position import Position
from cos.math.geometry.CPA import CPA
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

import inspect


class TargetResolver(Resolver):
	def __init__(self, resolver=None, os:Vehicle=None, ts:Vehicle=None, range:float=0.0 ):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			os -- Own ship
			ts -- Target ship
			range -- Range of interest
		""" 
		Resolver.__init__(self, '(OwnShip,TargetShip).')

		self.os			= os
		self.ts			= ts
		self.range		= range
		self.distance	= None
		self.velocity	= None
		self.cpa		= None

		self.visibility_threshold	= 0.8
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		""" 
		self.range		= 0.0
		self.distance	= None
		self.velocity	= None
		self.cpa		= None
		situation		= rulectxt.situation

		if situation is not None:
			self.os			= situation.os
			self.ts			= situation.ts
		else:
			self.os			= None
			self.ts			= None
		return

	def get_cpa(self):
		""" TODO: is_valid
		""" 
		if self.cpa is not None:
			return self.cpa

		self.cpa = CPA(self.os.location, self.os.velocity, self.ts.location, self.ts.velocity)
		return self.cpa

	def is_valid(self):
		""" TODO: is_valid
		""" 
		if (self.os is None) or (self.os is None):
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
		if self.ts is None:
			return  float('inf')
		
		if self.distance is None:
			self.distance	= Distance.euclidean(self.os.location, self.ts.location)
		return self.distance

	@simproperty
	def Velocity(self)->float:
		""" Symbol property - Velocity
		""" 
		if self.velocity is None:
			Vos				= self.os.velocity
			self.velocity	= math.sqrt(Vos[0]**2+Vos[1]**2)

		return self.velocity

	@simproperty
	def Approach(self)->float:
		""" Symbol property - Approach
		""" 
		todeg		= 180/np.pi
		Vos			= self.os.velocity
		Vts			= self.ts.velocity
		return math.atan2( Vos[1]-Vts[1], Vos[0]-Vts[0] )*todeg

	@simproperty
	def Cargo(self)->str:
		""" Symbol property - Cargo
		""" 

		return self.os.cargo


	@simproperty
	def Draught(self)->str:
		""" Symbol property - Draught
		""" 
		clearance		= self.os.underkeel_clearance + \
						  self.os.motion_allowance + \
						  self.os.squat

		return clearance
	@simproperty
	def Weight(self)->float:
		""" Symbol property - Weight
		""" 

		return self.os.weight

	@simproperty
	def Undercurrent(self)->float:
		""" Symbol property - Undercurrent
		""" 

		return 400

	@simproperty
	def TargetVelocity(self)->float:
		""" Symbol property - TargetVelocity
		""" 
		Vts			= self.ts.velocity
		return math.sqrt(Vts[0]**2+Vts[1]**2)

	@simproperty
	def TargetApproach(self)->float:
		""" Symbol property - TargetApproach
		""" 
		todeg		= 180/np.pi
		Vos			= self.os.velocity
		Vts			= self.ts.velocity
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
		if self.visibility_threshold > self.Visibility():
			return True
		
		return False

	@simproperty
	def Visibility(self):
		""" Symbol property - Visibility
		""" 
		return 1.0

	@simproperty
	def DCPA(self):
		""" Symbol property - Visibility
		"""
		return 1.0

	@simproperty
	def TCPA(self):
		""" Symbol property - Visibility
		"""
		return 1.0

	@simproperty
	def OnCollisionCourse(self):
		""" Symbol property - Visibility
		""" 
		return False
	
if __name__ == "__main__":
	test = TargetResolver()

