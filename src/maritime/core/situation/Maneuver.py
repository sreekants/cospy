#!/usr/bin/python
# Filename: Maneuver.py
# Description: Implementation of the Maneuver class

from maritime.core.situation.MaritimeEncounterSituation import MaritimeEncounterSituation
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
import maritime.regulation.colreg.Classification as Classification

class Maneuver(MaritimeEncounterSituation):
	def __init__(self, name:str, event:str, incidents, table:str=None ):
		""" Constructor
		Arguments
			name -- name of the maneuver
			event -- event to trigger on event
			incidents -- array of incidents to handle
			table -- Fact table given one row per encounter, if any
		"""
		MaritimeEncounterSituation.__init__( self )
		self.incidents	= incidents
		self.name		= name
		self.event		= event
		self.table		= table
		self.open		= {}		# (own id, target id) -> [own recid, target recid, first seen, last seen]
		self.seen		= set()		# Pairs classified in this pass
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		self.seen	= set()
		result		= self.for_each_maneuver_type( ctxt, rule_ctxt,
				self.incidents,
				self.on_trigger )

		# An encounter ends once unclassified for longer than the release window
		now		= ctxt.sim.tickcount()
		release	= Classification.THRESHOLDS.release
		self.close( ctxt, [key for key, e in self.open.items() if (key not in self.seen) and (now - e[3] > release)] )
		return result

	def on_trigger(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler for trigger
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		# ctxt.log.debug( self.type, f'{self.name}: {info.OS.config["name"]} at {info.TS.config["name"]} at range {info.distance:0.2}' )

		# Notify on every pass; record once per encounter
		self.regulate( ctxt, info.OS, self.event, arg )
		self.track( ctxt, info )
		return

	def track(self, ctxt:Context, event):
		""" Opens or extends the encounter of a pair
		Arguments
			ctxt -- Simulation context
			event -- EncounterEvent
		"""
		key		= ( event.OS.id, event.TS.id )
		now		= ctxt.sim.tickcount()
		self.seen.add( key )

		episode	= self.open.get( key )
		if episode is None:
			self.open[key]	= [ event.OS.recid, event.TS.recid, now, now ]
		else:
			episode[3]		= now
		return

	def close(self, ctxt:Context, keys):
		""" Records and forgets ended encounters
		Arguments
			ctxt -- Simulation context
			keys -- Pairs whose encounter ended
		"""
		for key in keys:
			own, target, start, end	= self.open.pop( key )
			if self.table is not None:
				self.data( ctxt, self.table, (own, target, start, end) )
		return

	def on_stop(self, ctxt:Context, config):
		""" Records encounters still open when the simulation stops
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.close( ctxt, list(self.open) )
		return


if __name__ == "__main__":
	test = Maneuver()


