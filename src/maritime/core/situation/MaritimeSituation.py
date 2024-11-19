#!/usr/bin/python
# Filename: EncounterSituation.py
# Description: Enumerations and states of encounter situations that occur in shipping

from maritime.model.vessel.Vessel import Vessel
from maritime.core.situation.Types import *
from cos.model.situation.EncounterSituation import *
from cos.core.kernel.Context import Context
from cos.math.geometry.Distance import Distance


class MaritimeSituation(EncounterSituation):
	def __init__(self, type, scope='Situation/Maritime'):
		""" Constructor
		Arguments
			type -- Type of the object
			scope -- Scope namespace
		"""
		EncounterSituation.__init__(self, scope, type)
		return

	def regulate(self, ctxt:Context, vessel:Vessel, msg, arg):
		""" Invokes a regulation event for a vessel
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel that triggered the regulation event
			msg -- Message describing the regulation event
			arg -- Opaque argument to pass as context
		"""
		# Notify regulations
		self.post( ctxt, ['/Faculty/Regulation/Rules'], msg, arg )

		# Notify the vessel
		if vessel is not None:
			vessel.notify( ctxt, msg, arg )
		return

	def for_each_in_range(self, ctxt:Context, rule_ctxt:RuleContext, range, vessels, objects, fn, arg=None):
		""" Helper funcation to evaluate vessels and other objects within a certain range
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			range -- Range value
			vessels -- List of vessels to evaluate
			objects -- List of objects to evaluate
			fn -- Function to call back when a vehicle is in range
			arg -- Opaque argument to pass to the callback
		"""
		return self.for_each_pair_if(
				ctxt,
				rule_ctxt,
				MaritimeSituation.__in_range, range,
				vessels, objects,
				fn,
				arg
			)

	def for_each_incident(self, ctxt:Context, rule_ctxt:RuleContext, type:Encounter, collection:map, fn, arg=None):
		""" Invoke a callback for each incident in a collection
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			type -- Type of the object
			collection -- collection of incidents to match
			fn -- Callback to invoke for each incident
			arg -- Opaque argument to pass to the callback
		"""
		incidents = collection.get(type)
		if incidents is None:
			return False

		for incident in incidents:
			fn( ctxt, rule_ctxt, incident[2], incident )

		return True

	@staticmethod
	def __in_range(lhs, rhs, range):
		""" Checks if two objects are in range
		Arguments
			lhs -- First object
			rhs -- Second object
			range -- Range value
		"""
		dist = Distance.euclidean(lhs.location, rhs.location)
		if dist > range:
			return False, dist

		return True, dist



if __name__ == "__main__":
	test = MaritimeSituation()


