#!/usr/bin/python
# Filename: EncounterWatch.py
# Description: Feeds a COLREG rule one situation per encounter of a kind, after its closest approach

from maritime.regulation.colreg.Classification import classify, NAMES
from cos.model.rule.Situation import Situation

import numpy as np


class EncounterWatch:
	roles	= {}		# (own id, target id) -> role of the encounter in progress, shared by every watch

	def __init__(self, role, dcpa:float, range:float):
		""" Constructor
		Arguments
			role -- Encounter type that begins an encounter, e.g. Encounter.OTGW
			dcpa -- Metres of predicted passing distance that is a risk of collision
			range -- Metres within which an onset is recorded
		"""
		self.role		= role
		self.name		= NAMES[role]
		self.dcpa		= dcpa
		self.range		= range
		self.onsets		= {}		# (own id, target id) -> [onset time, last distance]
		return

	def observe(self, ctxt, rule_ctxt, rule):
		""" Records onsets and queues each encounter on the rule once its range opens
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			rule -- COLREG rule the situations are added to
		"""
		vessels		= rule_ctxt.vessels or []
		subjects	= getattr( rule_ctxt, 'subjects', None ) or vessels
		now			= ctxt.sim.now()

		for own in subjects:
			for target in vessels:
				if own is target:
					continue

				key			= ( own.id, target.id )
				distance	= float( np.linalg.norm(EncounterWatch.offset(own, target)) )
				onset		= self.onsets.get( key )

				if onset is None:
					if self.begins( own, target ):
						self.onsets[key]	= [now, distance]
					continue

				if distance > onset[1]:
					del self.onsets[key]
					EncounterWatch.roles.pop( key, None )
					if distance <= self.range:
						situation	= Situation( own, target )
						situation.maneuvers[self.name]	= onset[0]		# The role at onset, read by EncounterSituation
						rule.add_situation( situation )
					continue

				onset[1]	= distance
		return

	def begins(self, own, target)->bool:
		""" Whether an encounter of this kind with a risk of collision begins
		Arguments
			own -- Own ship
			target -- Target ship
		"""
		if EncounterWatch.formation( own, target ) or (classify( own, target )[2] != self.role):
			return False

		# An encounter keeps the role it began with (Rule 13(d)); another watch has it already
		key		= ( own.id, target.id )
		if EncounterWatch.roles.get( key, self.name ) != self.name:
			return False

		if EncounterWatch.at_risk( own, target, self.dcpa, self.range ) == False:
			return False

		EncounterWatch.roles[key]	= self.name
		return True

	@staticmethod
	def formation(own, target)->bool:
		""" Whether two vessels sail together: members of one fleet, or a fleet and its member
		Arguments
			own -- Own ship
			target -- Target ship
		"""
		fo, ft	= getattr( own, 'fleet', None ), getattr( target, 'fleet', None )
		return ((fo is not None) and (fo is ft)) or (fo is target) or (ft is own)

	@staticmethod
	def offset(own, target):
		""" Target position relative to own ship
		Arguments
			own -- Own ship
			target -- Target ship
		"""
		return (np.asarray( target.location, dtype=float ) - np.asarray( own.location, dtype=float ))[:2]

	@staticmethod
	def at_risk(own, target, dcpa:float, range:float)->bool:
		""" Closing within range with a predicted passing distance under dcpa (Rule 7)
		Arguments
			own -- Own ship
			target -- Target ship
			dcpa -- Metres of predicted passing distance that is a risk of collision
			range -- Metres beyond which there is no risk
		"""
		d		= EncounterWatch.offset( own, target )
		v		= (np.asarray( target.velocity, dtype=float ) - np.asarray( own.velocity, dtype=float ))[:2]
		speed	= float( v @ v )

		if (float( np.linalg.norm(d) ) > range) or (speed == 0.0):
			return False

		tcpa	= -float( d @ v ) / speed
		if tcpa <= 0.0:
			return False

		return float( np.linalg.norm(d + v*tcpa) ) <= dcpa


if __name__ == "__main__":
	test = EncounterWatch( None, 500.0, 4000.0 )
