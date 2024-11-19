#!/usr/bin/python
# Filename: Harbour.py
# Description: Implementation of the Harbour class

from maritime.core.situation.MaritimeConductSituation import MaritimeConductSituation
from maritime.model.vessel.Vessel import Vessel

from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation as RuleSituation
from cos.model.rule.Context import Context as RuleContext
from cos.model.geography.TrafficZone import TrafficZone
from cos.math.geometry.Rectangle import Rectangle

class Harbour(MaritimeConductSituation):
	def __init__(self):
		""" Constructor
		Arguments
			"""
		MaritimeConductSituation.__init__( self )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.setup(ctxt, config)
		return

	def setup(self, ctxt:Context, config):
		""" Sets up the parameters of the situations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Overridable implementation
		objmgr				= ctxt.sim.objects
		self.world			= ctxt.sim.world

		self.zones			= {}


		self.zones['harbour']		= objmgr.get_all("/World/Sea/HARBOUR")
		self.zones['waterway']		= objmgr.get_all("/World/Sea/WATERWAY")
		self.zones['tss']			= objmgr.get_all("/World/Sea/TRAFFIC_SEPARATION_SCHEME")
		self.zones['tsl']			= objmgr.get_all("/World/Sea/TRAFFIC_LANE")
		self.zones['noentry']		= objmgr.get_all("/World/Sea/AREA_TO_AVOID")
		self.zones['caution']		= objmgr.get_all("/World/Sea/PRECAUTIONARY_AREA")
		self.zones['recommended']	= objmgr.get_all("/World/Sea/RECOMMENDED_ROUTE")
		self.zones['inshore']		= objmgr.get_all("/World/Sea/INSHORE_TRAFFIC_ZONE")
		self.zones['roundabout']	= objmgr.get_all("/World/Sea/ROUNDABOUT")
		self.zones['separator']		= objmgr.get_all("/World/Sea/SEPARATION_ZONE")
		return


	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""

		for zone_type, zones in self.zones.items():
			# Handle the zones
			if len(zones) <= 0:
				continue
			
			for lhs in rule_ctxt.vessels:
				for rhs in zones:
					self.on_oversee_zone( ctxt, rule_ctxt, (lhs, rhs), f'{zone_type}.enter' )

			return

	def on_oversee_zone(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler for zone activity
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Zone type event
		"""
		vessel:Vessel	= info[0]
		tss:TrafficZone	= info[1]

		self.regulate( ctxt, vessel, arg, (None, vessel, tss) )
		return


	@staticmethod
	def __enter_zone(vessel:Vessel, zone:TrafficZone, ctxt):
		""" Checks if two objects are in range
		Arguments
			vessel -- First object
			zone -- Second object
			ctxt -- Context argument (UNUSED)
		"""

		bbox:Rectangle	= vessel.boundary
		return zone.has_entered_rect( bbox )

if __name__ == "__main__":
	test = Harbour("XXX")


