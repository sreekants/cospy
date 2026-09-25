#!/usr/bin/python
# Filename: CollisionExaminer.py
# Description: Implementation of the CollisionExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware, ENCOUNTERS
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

# REQUIREMENT:
# Collision cost: the summed value of the two vessels involved, multiplied by a
# penalty rate held in config/examiner/zones.yaml.
#
#     cost = (value(OwnShip) + value(TargetShip)) * penalty_rate
#
# The rate expresses what a collision destroys as a fraction of the hulls
# involved, which keeps a scenario from needing a per-pair damage table. It is
# an expected cost, not a prediction: the examiner scores whenever an encounter
# is close enough to matter, so downstream consumers get a cost curve over the
# approach rather than a single number at the moment of contact.
#
# A vessel that declares no value falls back to a configured default rather
# than contributing zero, since a zero would quietly make a collision with an
# unpriced vessel look free.



class CollisionExaminer(ZoneAware, NavigationExaminer):
	TOPIC		= '/Faculty/Concern/Collision'
	MESSAGE		= 'vessel.collision.cost'
	EVENT		= 'collision.cost'
	SITUATIONS	= ENCOUNTERS

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)

		self.rate		= 0.0
		self.fallback	= 0.0
		self.report_topic	= self.TOPIC
		self.report_at	= None		# DCPA under which an encounter is costed
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os', 'ts'] )

		settings		= self.rules.section( 'collision' )

		self.rate		= float( settings.get('penalty_rate', 0.35) )
		self.fallback	= float( settings.get('default_vessel_value', 0.0) )
		self.report_topic	= settings.get( 'report_topic', self.TOPIC )

		at				= config["report.dcpa"]
		self.report_at	= float( at ) if at is not None else None
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
		# Requires both ships: a collision cost is a property of an encounter,
		# not of a vessel, so the precondition names 'os' and 'ts' together.
		if self.applicable( rule_ctxt ) == False:
			return

		situation	= rule_ctxt.situation
		dcpa		= rule_ctxt.resolve( '(OwnShip,TargetShip).DCPA' )

		if (self.report_at is not None) and (dcpa is not None) and (dcpa > self.report_at):
			return

		self.cost( ctxt, rule_ctxt, situation.os, situation.ts, dcpa )
		return

	def cost(self, ctxt:Context, rule_ctxt, own, target, dcpa):
		""" Values a collision between two vessels
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			own -- Own ship
			target -- Target ship
			dcpa -- Distance at closest point of approach, may be None
		Returns
			The expected cost in the currency of the vessel values
		"""
		values		= ( self.value(own), self.value(target) )
		cost		= sum( values ) * self.rate

		shapes, _rules, _depth	= self.survey( own )
		zone		= self.zone_name( shapes )

		# One finding per encounter with this target
		self.violate( ctxt, own, self.EVENT, shapes, value=cost,
					  detail=f'{values[0]:,.0f} + {values[1]:,.0f} at rate {self.rate}',
					  subject=self.identify(target) )

		self.announce( ctxt, self.report_topic, self.MESSAGE, {
			'own'		: self.identify( own ),
			'target'	: self.identify( target ),
			'time'		: ctxt.sim.now(),
			'zone'		: zone,
			'dcpa'		: dcpa,
			'tcpa'		: rule_ctxt.resolve( '(OwnShip,TargetShip).TCPA' ),
			'values'	: values,
			'rate'		: self.rate,
			'cost'		: cost,
		} )

		return cost

	def value(self, vessel)->float:
		""" What a vessel is worth
		Arguments
			vessel -- Vessel
		Note
			Read from the vessel's own settings so a scenario can price a hull
			individually; the configured default covers vessels that do not.
		"""
		if vessel is None:
			return self.fallback

		config	= getattr( vessel, 'config', None ) or {}
		args	= ArgList( config.get('settings', None) )

		for key in ('value', 'hull_value', 'insured_value'):
			declared	= args[key]
			if declared is not None:
				try:
					return float( declared )
				except (TypeError, ValueError):
					break

		return self.fallback


if __name__ == "__main__":
	test = CollisionExaminer()
