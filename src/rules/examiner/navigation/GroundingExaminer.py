#!/usr/bin/python
# Filename: GroundingExaminer.py
# Description: Implementation of the GroundingExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from maritime.model.zone.ZoneRules import ZoneRules
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

# REQUIREMENT:
# Grounding: a vessel at sea standing into water too shallow for its draught.
#
# The map reports a nominal depth per sea shape, so the test is the under-keel
# clearance - depth less draught less the vessel's own allowance - against the
# margin the zone demands. Negative clearance is contact with the seabed; a
# positive clearance under the margin is a near miss, scored more lightly.
#
# NOTE:
# Berthing is the same arithmetic in inland water and lives in
# BerthingExaminer; which zone types each is answerable for is declared in
# config/examiner/zones.yaml, not here, so a jurisdiction can move the line.



class GroundingExaminer(ZoneAware, NavigationExaminer):
	TOPIC		= '/Faculty/Concern/Grounding'
	MESSAGE		= 'vessel.grounding'
	
	ZONES		= 'grounding_zones'
	MARGIN		= 'grounding_margin'
	CONTACT		= 'grounding.contact'
	NEAR_MISS	= 'grounding.margin'

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner. Deliberately does not chain to Examiner.setup:
		this examiner is driven by the map and zones.yaml, not by a Legata
		automaton, so it has no automata or scorecard to load.
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os'] )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		return

	def judge(self, ctxt:Context, rule_ctxt):
		""" Judges rule_ctxt.situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		vessel		= rule_ctxt.situation.os
		shapes, rules, depth	= self.survey( vessel )

		# Answerable only for the zone types this examiner owns.
		if ZoneRules.applies_in( rules, self.ZONES, shapes ) == False:
			return

		clearance	= self.clearance( vessel, depth )
		if clearance is None:
			return			# The map reports no depth here; nothing to judge

		self.score( ctxt, vessel, shapes, rules, depth, clearance )
		return

	def score(self, ctxt:Context, vessel, shapes, rules, depth, clearance):
		""" Scores the clearance against the zone's margin
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel under examination
			shapes -- Map shapes enclosing the vessel
			rules -- Merged zone rules
			depth -- Seabed depth beneath the vessel
			clearance -- Water left beneath the keel
		"""
		margin	= float( rules.get(self.MARGIN, 0.0) or 0.0 )
		zone	= self.zone_name( shapes )

		if clearance > margin:
			# Clear water ends the finding, so a regrounding counts again
			self.settle( vessel, self.CONTACT, shapes )
			self.settle( vessel, self.NEAR_MISS, shapes )
			return 0.0

		event	= self.CONTACT if clearance <= 0.0 else self.NEAR_MISS
		penalty	= self.violate( ctxt, vessel, event, shapes, value=clearance,
								detail=f'depth {depth:.1f} m, clearance {clearance:.2f} m, '
									   f'margin {margin:.2f} m' )

		self.announce( ctxt, self.TOPIC, self.MESSAGE, {
			'vessel'	: self.identify( vessel ),
			'time'		: ctxt.sim.now(),
			'zone'		: zone,
			'event'		: event,
			'depth'		: depth,
			'clearance'	: clearance,
			'margin'	: margin,
			'penalty'	: penalty,
		} )

		return penalty


if __name__ == "__main__":
	test = GroundingExaminer()
