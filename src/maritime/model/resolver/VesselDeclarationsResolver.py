#!/usr/bin/python
# Filename: ZoneResolver.py
# Description: Implementation of the ZoneResolver class

from cos.model.resolver.Resolver import Resolver
from cos.model.resolver.NumericRange import NumericRange
from cos.model.rule.Context import Context
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.geography.TrafficSeparationScheme import TrafficSeparationScheme

import numpy as np


class VesselDeclarationsResolver(Resolver):
	def __init__(self, resolver=None):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			prefix -- Prefix for the resolver
		""" 
		Resolver.__init__(self, 'Vessel')
		self.methods	= self.get_methods()
		return


	def resolve(self, ctxt:Context, variable:str):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		""" 
		variable	= self.get_key(ctxt, variable)
		if variable == None:
			return None
		
		fn 		= self.methods.get( variable, None )
		if fn == None:
			return None
		
		return fn(ctxt)

	def get_methods(self):
		return {
			'Collision.TimeToEncounter.RadioRange':self.CollisionTimeToEncounterRadioRange,
			'Collision.TimeToEncounter.SonarRange':self.CollisionTimeToEncounterSonarRange,
			'Collision.TimeToEncounter.SafeRange':self.CollisionTimeToEncounterSafeRange,
			'Collision.TimeToEncounter.SituationRange':self.CollisionTimeToEncounterSituationRange,
			'Collision.TimeToEncounter.VisibleRange':self.CollisionTimeToEncounterVisibleRange,
			'Collision.TimeToEncounter.AlertRange':self.CollisionTimeToEncounterAlertRange
			}

	def CollisionTimeToEncounterRadioRange(self, ctxt):
		return NumericRange((0, 10))

	def CollisionTimeToEncounterSonarRange(self, ctxt):
		return NumericRange((0, 10))

	def CollisionTimeToEncounterSafeRange(self, ctxt):
		return NumericRange((0, 10))

	def CollisionTimeToEncounterSituationRange(self, ctxt):
		return NumericRange((0, 10))

	def CollisionTimeToEncounterVisibleRange(self, ctxt):
		return NumericRange((0, 10))

	def CollisionTimeToEncounterAlertRange(self, ctxt):
		return NumericRange((0, 10))


if __name__ == "__main__":
	test = VesselDeclarationsResolver()

