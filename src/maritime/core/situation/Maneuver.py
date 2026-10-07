#!/usr/bin/python
# Filename: Maneuver.py
# Description: Implementation of the Maneuver class

from maritime.core.situation.MaritimeEncounterSituation import MaritimeEncounterSituation
from cos.core.kernel.Context import Context
from cos.subsystem.data.DataContext import DataContext
from cos.core.kernel.Object import TERM_WRITE
from cos.model.rule.Context import Context as RuleContext
from cos.model.situation.EpisodeWatcher import EpisodeWatcher, epoch_of
from cos.core.utilities.ArgList import ArgList
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
		self.watcher	= None		# Range per pair; the rules get the event at the closest range once per epoch
		self.release	= 0			# Encounter release window, in ticks
		self.context	= None		# Simulation context, for the epoch callback
		return

	def init_watcher(self, ctxt:Context, config):
		""" Creates the watcher; its epoch comes from 'epoch=' in the module's arg
		Arguments
			ctxt -- Simulation context
			config -- Module configuration
		"""
		args			= ArgList( (config or {}).get('arg', '') or '' )
		self.release	= Classification.THRESHOLDS.release / ctxt.sim.clock.step
		self.watcher	= EpisodeWatcher( Classification.THRESHOLDS.range, self.on_epoch,
										  span=epoch_of(args), below=True )
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
		now		= ctxt.sim.seconds()
		release	= Classification.THRESHOLDS.release
		self.close( ctxt, [key for key, e in self.open.items() if (key not in self.seen) and (now - e[3] > release)] )

		if self.watcher is not None:
			self.context	= ctxt
			self.watcher.lapse( ctxt.sim.tickcount(), self.release )
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

		# Regulate once per epoch, at its closest range; record once per encounter
		if self.watcher is None:
			self.regulate( ctxt, info.OS, self.event, arg )
		else:
			self.context	= ctxt
			self.watcher.observe( (info.OS.id, info.TS.id), info.distance, ctxt.sim.tickcount(), (info.OS, arg) )
		self.track( ctxt, info )
		return

	def on_epoch(self, epoch):
		""" Sends the rules the encounter event observed at the epoch's closest range
		Arguments
			epoch -- Ended epoch; its detail is the peak's (own ship, event argument)
		"""
		own, arg	= epoch.detail
		self.regulate( self.context, own, self.event, arg )
		return

	def track(self, ctxt:Context, event):
		""" Opens or extends the encounter of a pair
		Arguments
			ctxt -- Simulation context
			event -- EncounterEvent
		"""
		key		= ( event.OS.id, event.TS.id )
		now		= ctxt.sim.seconds()
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
				self.data( ctxt, self.table, (own, target, start, end), DataContext( own ) )	# No single position for an episode
		return

	def on_term(self, ctxt:Context, runlevel):
		""" Records encounters still open, before the DataManager writes out
		Arguments
			ctxt -- Simulation context
			runlevel -- Termination run level; this acts at TERM_WRITE
		"""
		if runlevel != TERM_WRITE:
			return

		self.close( ctxt, list(self.open) )

		if self.watcher is not None:
			self.context	= ctxt
			self.watcher.flush( ctxt.sim.tickcount() )
		return


if __name__ == "__main__":
	test = Maneuver()


