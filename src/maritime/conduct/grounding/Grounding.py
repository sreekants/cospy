#!/usr/bin/python
# Filename: Grounding.py
# Description: Implementation of the Grounding class

from maritime.core.situation.MaritimeConductSituation import MaritimeConductSituation
from maritime.model.vessel.Vessel import Vessel, Status
from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation as RuleSituation
from cos.model.rule.Context import Context as RuleContext
from cos.model.geography.Sea import Sea
from shapely import Polygon, geometry

class Event:
	def __init__(self, vessel:Vessel, seabed:Sea):
		""" Constructor
		Arguments
			vessel -- Reference to the vessel
			seabed -- Reference to the sea bed grounding
		"""
		self.vessel	= vessel
		self.seabed	= seabed
		return

class Grounding(MaritimeConductSituation):
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

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		self.for_each_pair( ctxt, rule_ctxt,
				rule_ctxt.vessels,
				rule_ctxt.world.environ.reliefs,
				self.on_ground )

		return

	def setup(self, ctxt:Context, config):
		""" Sets up the parameters of the situations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Overridable implementation
		self.range	= 5
		return

	def on_ground(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler for ground
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		vessel:Vessel	= info[0]
		seabed:Sea		= info[1]

		depth			= seabed.nominal_depth			# Nominal channel depth
		clearance		= vessel.underkeel_clearance + \
						  vessel.motion_allowance + \
						  vessel.squat

		if depth > clearance:
			return

		if seabed.intersect(vessel.boundary) == False:
			# Reset the state if the vessel is moving
			if vessel.status == Status.AGROUND:
				vessel.state( Status.UNDERWAY )
			return

		# Already aground
		if vessel.status == Status.AGROUND:
			return

		ctxt.log.debug( self.type, f'GROUNDING: {vessel.config["name"]} at {seabed.config["name"]} with depth {seabed.depth:0.2}' )

		# Set the vessel state
		vessel.aground()

		# Apply regulations to the vessel
		self.regulate( ctxt, vessel, 'vessel.aground', Event(vessel, seabed) )
		return

if __name__ == "__main__":
	test = Grounding()


