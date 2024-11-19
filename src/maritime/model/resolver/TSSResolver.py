#!/usr/bin/python
# Filename: TSSResolver.py
# Description: Implementation of the TSSResolver class

from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.resolver.ZoneResolver import MaritimeZoneResolver
from maritime.model.geography.TrafficSeparationScheme import TrafficSeparationScheme
from maritime.model.geography.TrafficLane import TrafficLane
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class TSSResolver(MaritimeZoneResolver):
	def __init__(self, vessel:Vessel=None, TSS:TrafficSeparationScheme=None):
		""" Constructor
		Arguments
			vessel -- TODO
			TSS -- TODO
		""" 
		MaritimeZoneResolver.__init__(self, TSS, '[OwnShip,TrafficSeparationScheme]')
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		if rulectxt.situation is not None:
			self.zone	= rulectxt.situation.tss
		else:
			self.zone	= None
		return

	@property
	def tss(self):
		""" TODO: tss
		""" 
		return self.zone

class LaneResolver(MaritimeZoneResolver):
	def __init__(self, vessel:Vessel=None, TSS:TrafficLane=None):
		""" Constructor
		Arguments
			vessel -- TODO
			TSS -- TODO
		""" 
		MaritimeZoneResolver.__init__(self, TSS, '[OwnShip,TrafficLane]')
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		if rulectxt.situation is not None:
			self.zone	= rulectxt.situation.lane
		else:
			self.zone	= None
		return

	@property
	def lane(self):
		""" TODO: lane
		""" 
		return self.zone

if __name__ == "__main__":
	test = TSSResolver()

