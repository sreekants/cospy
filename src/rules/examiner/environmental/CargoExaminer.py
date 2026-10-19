#!/usr/bin/python
# Filename: CargoExaminer.py
# Description: Implementation of the CargoExaminer class

from maritime.model.zone.ZoneAwareness import ZoneAware
from cos.model.examiner.Examination import ExaminationType
from cos.model.examiner.ConcernExaminer import ConcernExaminer
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

# REQUIREMENT:
# Cargo: a vessel carrying a class of payload the zone does not admit.
#
# Vehicle.cargo is a ValueSet built from the vessel's own 'settings', else from
# its ship model's cargo.manifest, so the manifest is already in the
# simulation; what is missing is the jurisdiction's
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
#
# Both are scored on entry to a zone that bars a class no zone the vessel was in
# already barred, not on every pass; a vessel's first pass is an entry (COS.050).


class CargoExaminer(ZoneAware, ConcernExaminer):
	EXAMINES	= ExaminationType.CARGO
	TOPIC		= '/Faculty/Concern/Cargo'
	MESSAGE		= 'vessel.cargo'

	RESTRICTED	= 'cargo.restricted'
	UNDECLARED	= 'cargo.undeclared'

	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Environmental')

		self.inside		= {}		# Vessel key -> cargo-checking shapes it was in at its last pass
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

	def judge(self, ctxt:Context, rule_ctxt):
		""" Judges rule_ctxt.situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		vessel		= rule_ctxt.situation.os
		shapes, rules, _depth	= self.survey( vessel )

		entered		= self.entered( vessel, shapes )
		if len( entered ) == 0:
			return			# No zone with new restrictions entered this pass

		restricted	= self.restricted( rules )
		if len( restricted ) == 0:
			return			# The zone admits everything

		self.examine( ctxt, vessel, shapes, restricted, self.zone_name(entered) )
		return

	def entered(self, vessel, shapes)->list:
		""" Cargo-checking shapes a vessel entered since its last pass, settling those it left
		Arguments
			vessel -- Vessel under examination
			shapes -- Map shapes enclosing the vessel
		Returns
			The entered shapes that bar a class none of its previous shapes barred, outermost first
		"""
		key			= self.identify( vessel )
		checking	= [ s for s in shapes if self.restricted(self.rules.rules_at([s])) ]
		before		= self.inside.get( key, [] )
		self.inside[key]	= checking

		for shape in before:
			if shape not in checking:
				# A later return is a new entry, whatever the guard's release window
				self.settle( vessel, self.UNDECLARED, None, self.zone_name([shape]) )
				self.settle( vessel, self.RESTRICTED, None, self.zone_name([shape]) )

		known		= { c for s in before for c in self.restricted(self.rules.rules_at([s])) }
		return [ s for s in checking if (s not in before)
				 and (set(self.restricted(self.rules.rules_at([s]))) - known) ]

	@staticmethod
	def restricted(rules)->list:
		""" Cargo classes merged zone rules bar
		Arguments
			rules -- Zone rules
		"""
		restricted	= rules.get( 'restricted_cargo' ) or []
		if isinstance( restricted, str ):
			restricted	= [ c.strip() for c in restricted.split(',') if c.strip() ]
		return restricted

	def examine(self, ctxt:Context, vessel, shapes, restricted, subject=None):
		""" Compares a vessel's manifest against the zone's restrictions
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel under examination
			shapes -- Map shapes enclosing the vessel
			restricted -- Cargo classes the zone bars
			subject -- Zone entered, the finding's subject; the innermost zone by default
		"""
		zone	= subject or self.zone_name( shapes )
		manifest	= self.manifest( vessel )

		if len( manifest ) == 0:
			if self.report_empty:
				self.violate( ctxt, vessel, self.UNDECLARED, shapes,
							  detail=f'vessel declares no cargo manifest entering {zone}', subject=zone )
			return

		carried	= sorted( set(manifest).intersection(restricted) )
		if len( carried ) == 0:
			return

		penalty	= self.violate( ctxt, vessel, self.RESTRICTED, shapes, value=len(carried),
								detail=f'carrying {", ".join(carried)} where '
									   f'{", ".join(sorted(restricted))} is barred', subject=zone )

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
