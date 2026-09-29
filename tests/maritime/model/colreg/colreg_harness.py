#!/usr/bin/python
# Filename: colreg_harness.py
# Description: Shared scaffolding for judging COLREG legata through the real composite resolver

import os, types

import numpy as np

from tests.maritime.model.colreg.test_Rule14 import Ctxt, Vessel as Ship, Resolver, Automata, RuleContext, Situation
from tests.maritime.model.risk.test_ConcernWeights import source_module, CONFIG

VesselModel		= source_module( 'maritime.model.vessel.Vessel' )
Intent			= source_module( 'cos.model.vehicle.Intent' ).Intent
Type, Status	= VesselModel.Type, VesselModel.Status
Operation		= VesselModel.Operation
Restriction		= VesselModel.Restriction

COLREG	= os.path.join( CONFIG, 'maritime', 'regulation', 'colreg' )


class Vessel(Ship):
	""" A ship with the state the vessel terms read """
	def __init__(self, name, location, velocity, type=Type.POWER_DRIVEN, status=Status.UNDERWAY,
				 operation=0, restriction=Restriction.NONE):
		Ship.__init__( self, name, location, velocity )
		self.type			= type
		self.status			= status
		self.operation		= operation
		self.restriction	= restriction
		self.intent			= Intent()
		self.intents		= {'Signal': self.intent, 'Light': self.intent}
		self.is_signaled	= types.MethodType( VesselModel.Vessel.is_signaled, self )


class Pass:
	""" Rule context the encounter watch reads """
	def __init__(self, vessels, subjects=None):
		self.vessels	= vessels
		self.subjects	= subjects or vessels


def judge(rule:str, situation, visibility=None)->list:
	""" Names of the clauses a situation violates
	Arguments
		rule -- Legata file name, e.g. 'Rule13'
		situation -- Situation to judge
		visibility -- Scenario visibility in nautical miles, the resolver's default when None
	"""
	ctxt		= Ctxt()
	resolver	= Resolver()
	resolver.init( ctxt, '$(CONFIG)/legata.yaml' )
	if visibility is not None:
		resolver.get( 'target' ).visibility	= visibility

	automata	= Automata( None )
	automata.load( os.path.join(COLREG, f'{rule}.legata') )

	vessels		= [ v for v in (situation.os, situation.ts) if v is not None ]
	rule_ctxt	= RuleContext( ctxt, resolver, None, vessels, None )
	rule_ctxt.situation	= situation
	resolver.reset( ctxt, rule_ctxt )

	result		= automata.evaluate( rule_ctxt )
	return sorted( { e.parent.name for e in (result.error or []) } )


def encounter(rule, own, target, steps=600):
	""" Steps two ships one second at a time until the rule's watch queues their encounter
	Arguments
		rule -- COLREG rule with a watch
		own -- Own ship, the vessel under test
		target -- Target ship
		steps -- Seconds to run at most
	Returns
		The queued situation, or None when none was queued
	"""
	ctxt	= Ctxt()
	for _ in range( steps ):
		rule.watch.observe( ctxt, Pass([own, target], [own]), rule )
		if rule.sitations.empty() == False:
			return rule.sitations.get()
		own.step( 1.0 )
		target.step( 1.0 )

	return None
