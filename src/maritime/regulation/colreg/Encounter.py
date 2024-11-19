#!/usr/bin/python
# Filename: Evaluator.py
# Description: Implementation of the Evaluator class for COLREG evaluation

from maritime.model.vessel.Vessel import Vessel, Status
from maritime.core.situation.Types import Encounter as Type
from maritime.core.situation.Events import EncounterEvent
from cos.model.situation.EncounterSituation import *
from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation as RuleSituation
from cos.model.rule.Context import Context as RuleContext
from cos.math.geometry.Distance import Distance

import numpy as np
import math

class Event:
	def __init__(self, type:Type, vessel:Vessel, args:Vessel):
		""" Constructor
		Arguments
			type -- Type of the object
			vessel -- Reference to the vessel
			args -- List of arguments
		"""
		self.type	= type
		self.vessel	= vessel
		self.args	= args
		return

class Encounter(EncounterSituation):
	def __init__(self):
		""" Constructor
		Arguments
			"""
		EncounterSituation.__init__(self, 'Situation/Maritime', 'Incident')
		self.range		= 10.0
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		self.for_each_in_range( ctxt, rule_ctxt,
				self.range,
				rule_ctxt.vessels,
				rule_ctxt.vessels,
				self.on_encounter )
		return

	def on_encounter(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler for encounter
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		lhs			= info[0]
		rhs			= info[1]
		distance	= info[2]

		# Add all the vessels in potential encounters (in-range)
		rule_ctxt.encounters.append( (lhs, rhs, distance) )

		# Add akk the situations in the encounter
		self.situate( rule_ctxt, lhs, rhs, distance)
		return

	def situate(self, rule_ctxt:RuleContext, OS:Vessel, TS:Vessel, distance:float):
		""" Triggers a situation event
		Arguments
			rule_ctxt -- Rule context
			OS -- Own ship
			TS -- Target ship
			distance -- distance from the target
		"""
		α, β, situation	= Encounter.maneuver( OS, TS )

		self.trigger_maneuver( rule_ctxt, situation, OS, TS,
						EncounterEvent(situation, OS,TS, distance, α, β)
						)

		return True

	@staticmethod
	def maneuver(OS:Vessel, TS:Vessel):
		""" Compute the maneuver of two ships
		Arguments
			OS -- Own ship
			TS -- Target ship
		"""
		todeg	= 180/np.pi
		Vos		= OS.velocity
		Vts		= TS.velocity

		α		= math.atan2( Vos[1]-Vts[1], Vos[0]-Vts[0] )*todeg
		β		= math.atan2( Vts[1]-Vos[1], Vts[0]-Vos[0] )*todeg

		uα		= math.sqrt(Vos[0]**2+Vos[1]**2)
		uβ		= math.sqrt(Vts[0]**2+Vts[1]**2)

		situation = Type.NAR
		if abs(β)<13 and abs(α)<13:
			situation = Type.HO			# Head On
		elif abs(β)<112.5 and abs(α)<45 and (uβ>uα):
			situation = Type.OTSO		# Overtaken
		elif abs(α)<112.5 and abs(β)<45 and (uα<uβ):
			situation = Type.OTGW		# Overtaking
		elif (-112.5 < β < 0.0) and (-10 < α < 112.5):
			situation = Type.CRSO		# Stand On
		elif (-112.5 <  α < 0.0) and ( -10 < β < 112.5):
			situation = Type.CRGW		# Give Way

		# print( f'DEFAULT: α={α}, β={β}, uα={uα}, uβ={uβ}')
		return α, β, situation

	def trigger_maneuver(self, rule_ctxt:RuleContext, type, OS:Vessel, TS:Vessel, args ):
		""" Trigger a maneuver event
		Arguments
			rule_ctxt -- Rule context
			type -- Type of the object
			OS -- Own ship
			TS -- Target ship
			args -- List of arguments
		"""
		incidents	= rule_ctxt.situation.maneuvers.get(type)
		if incidents is None:
			incidents	= []
			rule_ctxt.situation.maneuvers[type]	= incidents
			incidents.append( (type, OS, args) )
			return

		for incident in incidents:
			event:EncounterEvent	= incident[2]

			iOS		= event.OS
			iTS		= event.TS
			if iOS == OS and iTS == TS:
				return


		incidents.append( (type, OS, args) )
		return

	def for_each_in_range(self, ctxt:Context, situation:RuleContext, distance, list1, list2, fn, arg=None):
		""" Helper function to process permutations of two list of objects
		Arguments
			ctxt -- Simulation context
			situation -- Situation information
			distance -- distance
			list1 -- List of objects to match
			list2 -- List of objects to match against
			fn -- Function to call back when a vehicle is in range
			arg -- Opaque argument to pass to the callback
		"""
		return self.for_each_pair_if(
				ctxt,
				situation,
				Encounter.__in_range, distance,
				list1, list2,
				fn,
				arg
			)

	@staticmethod
	def __in_range(lhs, rhs, range):
		""" Checs if two vessels are in range
		Arguments
			lhs -- First vessel
			rhs -- Second vessel
			range -- In-range limit
		"""
		dist = Distance.euclidean(lhs.location, rhs.location)
		if dist > range:
			return False, dist

		return True, dist


if __name__ == "__main__":
	test = Encounter()


