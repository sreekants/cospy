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
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

from cos.core.utilities.ArgList import ArgList

import numpy as np
import math, yaml

METRES_PER_NM	= 1852.0
PROFILES		= '$(CONFIG)/weather/profiles.yaml'

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

		self.collision_dcpa	= 100.0		# Metres; evaluator.yaml r_min_cpa
		self.visibility		= 10.0		# Nautical miles, until the weather profile says otherwise
		return

	def init(self, ctxt, cfg):
		""" Reads thresholds from legata.yaml and visibility from the scenario's weather profile
		Arguments
			ctxt -- Simulation context
			cfg -- This resolver's legata.yaml entry
		"""
		args	= ArgList( (cfg or {}).get('config') )
		self.collision_dcpa	= float( args['collision.dcpa'] or self.collision_dcpa )
		self.visibility		= float( args['visibility.default'] or self.visibility )

		weather	= ( getattr(ctxt.sim.config, 'env', None) or {} ).get( 'WEATHER', None )
		try:
			path		= ctxt.sim.config.resolve( args['profiles'] or PROFILES )
			profiles	= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(path) ).get( 'profiles', {} )
			low, high	= profiles[weather]['visibility']
			self.visibility	= (float(low) + float(high)) / 2.0
		except Exception as e:
			ctxt.log.warning( 'TargetResolver', f'No visibility for weather {weather!r} ({e}); using {self.visibility} nm' )
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
		""" Closest approach from now on: (steps to it, distance at it, closing)
		"""
		if self.cpa is not None:
			return self.cpa

		d		= ( np.asarray(self.ts.location, dtype=float) - np.asarray(self.os.location, dtype=float) )[:2]
		v		= ( np.asarray(self.ts.velocity, dtype=float) - np.asarray(self.os.velocity, dtype=float) )[:2]
		speed	= float( v @ v )
		t		= -float( d @ v ) / speed if speed > 0.0 else 0.0

		future	= max( 0.0, t )
		self.cpa	= ( future, float(np.linalg.norm(d + v*future)), t > 0.0 )
		return self.cpa

	def is_valid(self):
		""" Whether both ships are in scope
		"""
		return (self.os is not None) and (self.ts is not None)

	def bearing(self):
		""" Bearing of the target relative to own ship's course, degrees, positive to starboard (y grows south)
		"""
		h	= np.asarray( self.os.velocity, dtype=float )[:2]
		d	= ( np.asarray(self.ts.location, dtype=float) - np.asarray(self.os.location, dtype=float) )[:2]
		return float( np.degrees(math.atan2(h[0]*d[1] - h[1]*d[0], h[0]*d[0] + h[1]*d[1])) )

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
		""" Symbol property - Detect: the signals the target is making
		"""
		if not self.is_valid():
			return None

		return list( getattr(self.ts, 'intent', None) or [] )

	@simproperty
	def Position(self):
		""" Symbol property - Position: sector of own ship's bow the target is in
		"""
		if (not self.is_valid()) or (not np.any(self.os.velocity)):
			return None

		b	= self.bearing()
		if abs(b) <= 22.5:
			return 'Position.Ahead'
		if abs(b) > 112.5:
			return 'Position.Astern'
		return 'Position.Starboard' if b > 0.0 else 'Position.Port'

	@simproperty
	def Direction(self):
		""" Symbol property - Direction, as Position (Rule 15)
		"""
		return self.Position()

	@simproperty
	def TimeToEncounter(self):
		""" Symbol property - TimeToEncounter, as TCPA
		"""
		return self.TCPA()

	@simproperty
	def Visible(self):
		""" Symbol property - Visible: the target is within visual range (Rule 3(k))
		"""
		if not self.is_valid():
			return None

		return self.Distance() <= self.Visibility() * METRES_PER_NM

	@simproperty
	def Visibility(self):
		""" Symbol property - Visibility in nautical miles, from the weather profile
		"""
		return self.visibility

	@simproperty
	def DCPA(self):
		""" Symbol property - DCPA in map units (metres at 1:1)
		"""
		if not self.is_valid():
			return None

		return self.get_cpa()[1]

	@simproperty
	def ClosestApproachPoint(self):
		""" Symbol property - ClosestApproachPoint, the distance at CPA
		"""
		return self.DCPA()

	@simproperty
	def TCPA(self):
		""" Symbol property - TCPA in simulation steps; 0 once the CPA has passed
		"""
		if not self.is_valid():
			return None

		return self.get_cpa()[0]

	@simproperty
	def OnCollisionCourse(self):
		""" Symbol property - OnCollisionCourse: closing, with DCPA under collision.dcpa
		"""
		if not self.is_valid():
			return None

		_t, dcpa, closing	= self.get_cpa()
		return closing and (dcpa <= self.collision_dcpa)

if __name__ == "__main__":
	test = TargetResolver()

