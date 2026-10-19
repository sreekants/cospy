#!/usr/bin/python
# Filename: ColregResolver.py
# Description: Implementation of the ColregResolver class

from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList
from cos.model.rule.Context import Context as RuleContext
from maritime.regulation.colreg.Classification import classify, bearing, NAMES

import numpy as np
import math

STOPPING_LENGTHS	= 15.0		# Ship lengths of track reach in a full-astern stop (IMO MSC.137(76), 5.3.1)
METRES_PER_NM		= 1852.0
MS_PER_KNOT			= 1852.0 / 3600.0

class ColregResolver(Resolver):
	def __init__(self, resolver):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
		""" 
		Resolver.__init__(self, '(OwnShip,TargetShip).COLREG.')


		self.tr			= resolver.get('target')
		self.situation	= None
		self.encounter	= None		# The rule situation being judged
		self.stopping	= STOPPING_LENGTHS
		return

	def init(self, ctxt, cfg):
		""" Reads the stopping distance from legata.yaml
		Arguments
			ctxt -- Simulation context
			cfg -- This resolver's legata.yaml entry
		"""
		args			= ArgList( (cfg or {}).get('config') )
		self.stopping	= float( args['stopping.lengths'] or self.stopping )
		return

	
	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		""" 
		self.tr.reset( ctxt, rulectxt )
		self.situation	= None
		self.encounter	= getattr( rulectxt, 'situation', None )
		return

	@simproperty
	def HeadOn(self)->bool:
		""" Simulation property: HeadOn - the rule recorded a head-on onset for this pair (Rule 14(b))
		"""
		maneuvers	= getattr( self.encounter, 'maneuvers', None ) or {}
		return 'HeadOn' in maneuvers

	@simproperty
	def PassingSide(self)->str:
		""" Simulation property: PassingSide - 'Port' or 'Starboard' side of own ship the target is on
		"""
		if (self.tr is None) or (self.tr.os is None) or (self.tr.ts is None):
			return 'Unknown'

		return passing_side( self.tr.os, self.tr.ts )

	@simproperty
	def Tack(self)->str:
		""" Simulation property: Tack - side own ship had the wind on at onset, 'Port', 'Starboard' or 'Unknown' (Rule 12)
		"""
		return (getattr( self.encounter, 'onset', None ) or {}).get( 'tack', 'Unknown' )

	@simproperty
	def TargetTack(self)->str:
		""" Simulation property: TargetTack - side the target had the wind on at onset (Rule 12)
		"""
		return (getattr( self.encounter, 'onset', None ) or {}).get( 'target_tack', 'Unknown' )

	@simproperty
	def Windward(self)->bool:
		""" Simulation property: Windward - own ship was upwind of the target at onset; false in a calm (Rule 12)
		"""
		return (getattr( self.encounter, 'onset', None ) or {}).get( 'windward' ) or False

	@simproperty
	def Paired(self)->bool:
		""" Simulation property: Paired - the situation has a target ship
		"""
		return getattr( self.encounter, 'ts', None ) is not None

	@simproperty
	def SafeSpeed(self)->float:
		""" Simulation property: SafeSpeed - metres per second at which own ship stops within half the
		visibility; stopping distance grows with the square of speed to STOPPING_LENGTHS at service speed;
		0 without a service speed or length (Rule 19(b))
		"""
		os		= self.tr.os if self.tr is not None else None
		model	= getattr( os, 'model', None )
		service	= getattr( model, 'service_speed', None )
		length	= float( model.ship.length ) if model is not None else 0.0
		if (service is None) or (length <= 0.0) or (self.tr.visibility is None):
			return 0.0

		half	= self.tr.visibility * METRES_PER_NM / 2.0
		return float( service ) * MS_PER_KNOT * math.sqrt( half / (self.stopping * length) )

	@simproperty
	def WithinSafeSpeed(self)->bool:
		""" Simulation property: WithinSafeSpeed - own ship is no faster than SafeSpeed; true without one (Rule 19(b))
		"""
		safe	= self.SafeSpeed()
		if safe <= 0.0:
			return True

		return float( np.linalg.norm(np.asarray(self.tr.os.velocity, dtype=float)[:2]) ) <= safe

	@simproperty
	def SlowedSinceOnset(self)->bool:
		""" Simulation property: SlowedSinceOnset - own ship is slower than at the onset of the encounter;
		true without an onset (Rule 19(e))
		"""
		onset	= self.OnsetSpeed()
		os		= self.tr.os if self.tr is not None else None
		if (onset <= 0.0) or (os is None):
			return True

		return float( np.linalg.norm(np.asarray(os.velocity, dtype=float)[:2]) ) < onset

	@simproperty
	def OnsetSpeed(self)->float:
		""" Simulation property: OnsetSpeed - own ship's speed at the onset of the encounter; 0 without one (Rule 19(e))
		"""
		return (getattr( self.encounter, 'onset', None ) or {}).get( 'speed' ) or 0.0

	@simproperty
	def ForwardAtOnset(self)->bool:
		""" Simulation property: ForwardAtOnset - the target was forward of own ship's beam at onset; false without one (Rule 19(e))
		"""
		return (getattr( self.encounter, 'onset', None ) or {}).get( 'forward' ) or False

	@simproperty
	def InSightAtOnset(self)->bool:
		""" Simulation property: InSightAtOnset - the target was within visual range at onset; true when unknown (Rule 19(a))
		"""
		sight	= (getattr( self.encounter, 'onset', None ) or {}).get( 'in_sight' )
		return True if sight is None else sight

	@simproperty
	def AheadOfTarget(self)->bool:
		""" Simulation property: AheadOfTarget - own ship is forward of the target's beam; judged at
		the closest approach, own ship crossed ahead of the target (Rule 15)
		"""
		if (self.tr is None) or (self.tr.is_valid() == False) or (self.tr.ts is None):
			return None

		ts	= self.tr.ts
		if not np.any( ts.velocity ):
			# A target stopped since the closest approach keeps the course it last held under way
			v	= getattr( self.encounter, 'ts_course', None )
			if v is None:
				return None
			ts	= Heading( ts.location, v )

		return abs( bearing(ts, self.tr.os) ) < 90.0

	@simproperty
	def EncounterSituation(self)->str:
		""" Simulation property: EncounterSituation
		""" 
		if self.tr is None:
			return None

		if self.tr.is_valid() == False:
			return None

		if self.situation is not None:
			return self.situation

		if self.tr.ts is None:
			return None

		# The role a rule recorded at onset outlives the geometry at the closest approach
		maneuvers	= getattr( self.encounter, 'maneuvers', None ) or {}
		for name in NAMES.values():
			if name and (name in maneuvers):
				self.situation	= name
				return self.situation

		situation	= NAMES[ classify(self.tr.os, self.tr.ts)[2] ]

		self.situation	= situation
		return self.situation


class Heading:
	def __init__(self, location, velocity):
		""" A vessel's position with a course it no longer holds
		Arguments
			location -- Position
			velocity -- Velocity
		"""
		self.location	= location
		self.velocity	= velocity
		return


def passing_side(os, ts)->str:
	""" Side of own ship's course the target lies on; map y grows south
	Arguments
		os -- Own ship
		ts -- Target ship
	"""
	h		= np.asarray( os.velocity, dtype=float )[:2]
	d		= (np.asarray( ts.location, dtype=float ) - np.asarray( os.location, dtype=float ))[:2]
	cross	= h[0]*d[1] - h[1]*d[0]

	if (not np.any(h)) or (cross == 0.0):
		return 'Unknown'

	return 'Starboard' if cross > 0.0 else 'Port'


if __name__ == "__main__":
	test = ColregResolver()

