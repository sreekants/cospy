#!/usr/bin/python
# Filename: CargoExaminer.py
# Description: Implementation of the CargoExaminer class

from maritime.model.zone.ZoneAwareness import ZoneAware
from cos.model.examiner.ConcernExaminer import ConcernExaminer
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

# REQUIREMENT:
# Cargo: a vessel carrying a class of payload the zone does not admit.
#
# Vehicle.cargo is a ValueSet built from the vessel's own 'settings', so the
# manifest is already in the simulation; what is missing is the jurisdiction's
# list of what it will not accept, which lives per zone in
# config/examiner/zones.yaml.
#
# NOTE:
# Two situations are scored:
#   RESTRICTED - Carrying a restricted class is the violation proper.
#   UNDECLARED - Carrying nothing at all is reported separately 
# 
# Note: UNDECLARED manifest, is reported separately because an empty value set and
#    a genuinely empty hold look identical, and silently treating the first 
#    as compliant would let a misconfigured vessel pass every cargo rule.


class CargoExaminer(ZoneAware, ConcernExaminer):
	TOPIC		= '/Faculty/Concern/Cargo'
	MESSAGE		= 'vessel.cargo'

	RESTRICTED	= 'cargo.restricted'
	UNDECLARED	= 'cargo.undeclared'

	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Environmental')
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os'] )
		self.report_empty	= config.IsTrue( 'report.undeclared' )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		return

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		vessel		= rule_ctxt.situation.os
		shapes, rules, _depth	= self.survey( vessel )

		restricted	= rules.get( 'restricted_cargo' ) or []
		if isinstance( restricted, str ):
			restricted	= [ c.strip() for c in restricted.split(',') if c.strip() ]

		if len( restricted ) == 0:
			return			# The zone admits everything

		self.examine( ctxt, vessel, shapes, restricted )
		return

	def examine(self, ctxt:Context, vessel, shapes, restricted):
		""" Compares a vessel's manifest against the zone's restrictions
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel under examination
			shapes -- Map shapes enclosing the vessel
			restricted -- Cargo classes the zone bars
		"""
		zone	= self.zone_name( shapes )
		manifest	= self.manifest( vessel )

		if len( manifest ) == 0:
			if self.report_empty:
				self.violate( ctxt, vessel, self.UNDECLARED, shapes,
							  detail='vessel declares no cargo manifest' )
			return

		carried	= sorted( set(manifest).intersection(restricted) )
		if len( carried ) == 0:
			return

		penalty	= self.violate( ctxt, vessel, self.RESTRICTED, shapes, value=len(carried),
								detail=f'carrying {", ".join(carried)} where '
									   f'{", ".join(sorted(restricted))} is barred' )

		self.announce( ctxt, self.TOPIC, self.MESSAGE, {
			'vessel'	: self.identify( vessel ),
			'time'		: ctxt.sim.now(),
			'zone'		: zone,
			'event'		: self.RESTRICTED,
			'carried'	: carried,
			'restricted': sorted( restricted ),
			'penalty'	: penalty,
		} )

		return penalty

	@staticmethod
	def manifest(vessel):
		""" A vessel's cargo classes as a plain list
		Arguments
			vessel -- Vessel
		Note
			Vehicle.cargo is a ValueSet, which derives from StringSet, which is
			a list - so this is a copy, not a conversion.
		"""
		cargo	= getattr( vessel, 'cargo', None )
		if cargo is None:
			return []

		return [ str(c) for c in cargo ]


if __name__ == "__main__":
	test = CargoExaminer()
