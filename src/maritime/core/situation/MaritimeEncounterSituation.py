#!/usr/bin/python
# Filename: MaritimeEncounterSituation.py
# Description: Enumerations and states of encounter situations that occur in shipping

from maritime.core.situation.MaritimeSituation import MaritimeSituation
from cos.model.situation.EncounterSituation import *

class MaritimeEncounterSituation(MaritimeSituation):
	def __init__(self):
		""" Constructor
		"""
		MaritimeSituation.__init__(self, 'Encounter')
		return

	def for_each_maneuver_type(self, ctxt:Context, rule_ctxt:RuleContext, types, fn):
		""" Helper funcation to evaluate maneuver types
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			types -- Types of situations
			fn -- Callback to invoke when a maneuver is identified
		"""
		for incident in types:
			self.for_each_incident( ctxt, rule_ctxt,
					incident,
					rule_ctxt.situation.maneuvers,
					fn )
		return


if __name__ == "__main__":
	test = MaritimeEncounterSituation()


