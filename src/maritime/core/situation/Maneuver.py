#!/usr/bin/python
# Filename: Maneuver.py
# Description: Implementation of the Maneuver class

from maritime.core.situation.MaritimeEncounterSituation import MaritimeEncounterSituation
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

class Maneuver(MaritimeEncounterSituation):
	def __init__(self, name:str, event:str, incidents ):
		""" Constructor
		Arguments
				name -- name of the maneuver
			event -- event to trigger on event
			incidents -- array of incidents to handle
		"""
		MaritimeEncounterSituation.__init__( self )
		self.incidents	= incidents
		self.name		= name
		self.event		= event
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		return self.for_each_maneuver_type( ctxt, rule_ctxt,
				self.incidents,
				self.on_trigger )

	def on_trigger(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler for trigger
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		# ctxt.log.debug( self.type, f'{self.name}: {info.OS.config["name"]} at {info.TS.config["name"]} at range {info.distance:0.2}' )

		# Apply regulations to the vessel
		self.regulate( ctxt, info.OS, self.event, arg )
		return


if __name__ == "__main__":
	test = Maneuver()


