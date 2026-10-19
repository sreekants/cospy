#!/usr/bin/python
# Filename: ZoneResolver.py
# Description: Implementation of the ZoneResolver class

from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.geography.TrafficSeparationScheme import TrafficSeparationScheme
from maritime.model.zone.Location import Location
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np

class ZoneResolver(Resolver):
	def __init__(self, vessel:Vessel, zone:TrafficSeparationScheme, prefix:str=None):
		""" Constructor
		Arguments
			vessel -- TODO
			zone -- TODO
			prefix -- TODO
		""" 
		Resolver.__init__(self, prefix)

		self.zone		= zone
		self.vessel		= vessel
		self.ctxt		= None
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		self.ctxt	= ctxt
		if rulectxt.situation is not None:
			self.zone		= rulectxt.situation.zone
			self.vessel		= rulectxt.situation.os
		else:
			self.zone		= None
			self.vessel		= None
		return

	@simproperty
	def Name(self):
		""" TODO: InRange
		""" 
		if self.zone is None:
			return ''
		return self.zone.name

	@simproperty
	def InRange(self):
		""" TODO: InRange
		""" 
		if self.zone is None:
			return False
		return self.zone.contains( self.vessel.location )

	@simproperty
	def SafeDistance(self):
		""" Metres to keep from other vessels in the lane, from location.yaml sea.tss; 0 when unset
		"""
		return self.tss( 'safe_distance' )

	@simproperty
	def SeparationDistance(self):
		""" Metres to keep clear of the scheme's separation line or zone, from location.yaml sea.tss; 0 when unset
		"""
		return self.tss( 'separation_distance' )

	@simproperty
	def SafeHeading(self):
		""" Simulator heading of the lane's traffic flow, from location.yaml sea.tss.lanes; 0 when unset
		"""
		return self.tss( 'safe_heading' )

	def tss(self, key:str)->float:
		""" A TSS setting of the situation's zone, 0 when there is no zone or the location sets none
		Arguments
			key -- safe_distance, safe_heading or separation_distance
		"""
		if (self.zone is None) or (self.ctxt is None):
			return 0.0

		value	= Location.shared( self.ctxt ).lane( self.zone.name, key )
		return value if value is not None else 0.0


class MaritimeZoneResolver(ZoneResolver):
	def __init__(self, vessel:Vessel, zone:TrafficSeparationScheme, prefix:str=None):
		""" Constructor
		Arguments
			vessel -- TODO
			zone -- TODO
			prefix -- TODO
		""" 
		ZoneResolver.__init__(self, vessel, zone, prefix)
		return


if __name__ == "__main__":
	test = ZoneResolver()

