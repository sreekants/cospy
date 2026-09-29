#!/usr/bin/python
# Filename: test_VesselTerms.py
# Description: Test cases for the vessel enums, state terms and encounter terms legata reads (COS.022)

import unittest

from tests.maritime.model.colreg.colreg_harness import (Vessel, Situation, Ctxt, Resolver, RuleContext,
														 Type, Status, Operation, Restriction, source_module)

VesselDeclarationsResolver	= source_module( 'maritime.model.resolver.VesselDeclarationsResolver' ).VesselDeclarationsResolver


def terms(own, target, maneuvers=None):
	""" A function resolving terms for a pair, as a clause would
	Arguments
		own -- Own ship
		target -- Target ship
		maneuvers -- Roles recorded on the situation
	"""
	ctxt		= Ctxt()
	resolver	= Resolver()
	resolver.init( ctxt, '$(CONFIG)/legata.yaml' )
	rule_ctxt	= RuleContext( ctxt, resolver, None, [own, target], None )
	rule_ctxt.situation	= Situation( own, target )
	rule_ctxt.situation.maneuvers.update( maneuvers or {} )
	resolver.reset( ctxt, rule_ctxt )
	return lambda term: resolver.resolve( rule_ctxt, term )


class EnumTestCase(unittest.TestCase):
	def test_members_resolve_by_name_or_in_camel_case(self):
		member	= VesselDeclarationsResolver.member
		self.assertIs( member('Type.PowerDriven'), Type.POWER_DRIVEN )
		self.assertIs( member('Status.ANCHORED'), Status.ANCHORED )
		self.assertIs( member('Status.NotUnderCommand'), Status.NOT_UNDER_COMMAND )
		self.assertIs( member('Operation.Fishing'), Operation.FISHING )
		self.assertIsNone( member('Type.AirCushion') )
		self.assertIsNone( member('Collision.PassingDistance') )

	def test_declarations_still_win(self):
		resolve	= terms( Vessel('A', (0, 0), (1, 0)), Vessel('B', (100, 0), (-1, 0)) )
		self.assertEqual( resolve('Vessel.Collision.PassingDistance'), 100.0 )
		self.assertIs( resolve('Vessel.Type.Sailing'), Type.SAILING )


class StateTestCase(unittest.TestCase):
	def test_status_operation_and_restriction(self):
		own		= Vessel( 'A', (0, 0), (1, 0), status=Status.ANCHORED, operation=Operation.FISHING.value,
						  restriction=Restriction.DREDGING )
		resolve	= terms( own, Vessel('B', (100, 0), (-1, 0)) )
		self.assertIs( resolve('OwnShip.Status'), Status.ANCHORED )
		self.assertIs( resolve('OwnShip.Operation'), Operation.FISHING )
		self.assertIs( resolve('OwnShip.Restriction'), Restriction.DREDGING )
		self.assertIs( resolve('TargetShip.Status'), Status.UNDERWAY )


class EncounterTestCase(unittest.TestCase):
	def test_beam(self):
		own		= Vessel( 'A', (0, 0), (1, 0) )
		for location, beam in [((100, 10), 'Position.Forward'), ((0, 100), 'Position.Abeam'), ((-100, 10), 'Position.Abaft')]:
			self.assertEqual( terms(own, Vessel('B', location, (0, 1)))('(OwnShip,TargetShip).Beam'), beam )

	def test_the_role_recorded_at_onset_is_the_encounter_situation(self):
		own, target	= Vessel( 'A', (0, 0), (1, 0) ), Vessel( 'B', (-100, 10), (0, 1) )		# Opening: no live role
		self.assertEqual( terms(own, target, {'GiveWay': 0})('(OwnShip,TargetShip).EncounterSituation'), 'GiveWay' )

	def test_ahead_of_target(self):
		target	= Vessel( 'B', (0, 0), (0, -5) )				# Northbound (y grows south)
		self.assertTrue( terms(Vessel('A', (0, -50), (5, 0)), target)('(OwnShip,TargetShip).AheadOfTarget') )
		self.assertFalse( terms(Vessel('A', (0, 50), (5, 0)), target)('(OwnShip,TargetShip).AheadOfTarget') )


if __name__ == '__main__':
	unittest.main()
