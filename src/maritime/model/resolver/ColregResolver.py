#!/usr/bin/python
# Filename: ColregResolver.py
# Description: Implementation of the ColregResolver class

from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from maritime.regulation.colreg.Classification import classify, bearing, NAMES

import numpy as np
import math

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
	def AheadOfTarget(self)->bool:
		""" Simulation property: AheadOfTarget - own ship is forward of the target's beam; judged at
		the closest approach, own ship crossed ahead of the target (Rule 15)
		"""
		if (self.tr is None) or (self.tr.is_valid() == False) or (self.tr.ts is None):
			return None

		if not np.any( self.tr.ts.velocity ):
			return None

		return abs( bearing(self.tr.ts, self.tr.os) ) < 90.0

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

