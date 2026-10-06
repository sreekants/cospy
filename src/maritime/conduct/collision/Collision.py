#!/usr/bin/python
# Filename: Collision.py
# Description: Implementation of the Collision class

from maritime.core import situation
from maritime.core.situation.MaritimeConductSituation import MaritimeConductSituation
from cos.core.kernel.Context import Context
from cos.core.kernel.Object import TERM_WRITE
from cos.model.rule.Situation import Situation as RuleSituation
from cos.model.rule.Context import Context as RuleContext
from maritime.core.situation.Types import Encounter as EncounterType
from cos.core.utilities.ArgList import ArgList
from cos.model.situation.EpisodeWatcher import EpisodeWatcher, epoch_of

class Collision(MaritimeConductSituation):
	watcher		= None		# Set up in setup()

	def __init__(self):
		""" Constructor
		Arguments
			"""
		MaritimeConductSituation.__init__( self )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.setup(ctxt, config)
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		self.for_each_in_range( ctxt, rule_ctxt,
				self.interest_range,
				rule_ctxt.subjects,
				rule_ctxt.vessels,
				self.on_monitor_vessel )

		self.for_each_in_range( ctxt, rule_ctxt,
				self.interest_range,
				rule_ctxt.subjects,
				rule_ctxt.bodies,
				self.on_monitor_obstacle )

		if self.watcher is not None:
			self.context	= ctxt
			self.watcher.lapse( ctxt.sim.tickcount() )		# Pairs gone out of the range of interest
		return

	def setup(self, ctxt:Context, config):
		""" Sets up the parameters of the situations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		args					= ArgList(config['arg'])

		# Overridable implementation
		self.interest_range		= args.ToFloat('interest')	# Range of interest
		self.tracking_range		= args.ToFloat('track')		# Range at visibility (must be greater than collision range)
		self.collision_range	= args.ToFloat('collision')	# Range at collision

		# Distance per pair within the tracking range; its peak is the closest approach
		self.watcher	= EpisodeWatcher( self.tracking_range, self.on_epoch, span=epoch_of(args), below=True )
		self.context	= None
		return

	def on_monitor_vessel(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler to evaluate vessel collision
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		lhs			= info[0]	# First vessel
		rhs			= info[1]	# Second vessel
		distance	= info[2]	# Distance between them


		if distance > self.interest_range:
			return

		if self.watcher is not None:
			self.context	= ctxt
			self.watcher.observe( (lhs.vid, rhs.vid), distance, ctxt.sim.tickcount(), (lhs, rhs) )

		if distance < self.collision_range:
			ctxt.sim.data.push(f'fact_collision', (lhs.recid, rhs.recid, ctxt.sim.seconds(), round(distance, 4)))

		return

	def on_epoch(self, epoch):
		""" Regulates and records the closest approach of an epoch within the tracking range
		Arguments
			epoch -- Ended epoch; its peak is the closest distance, its detail the pair
		"""
		ctxt		= self.context
		lhs, rhs	= epoch.detail

		self.regulate( ctxt, lhs, "vessel.approach", (EncounterType.CPA, lhs, rhs, epoch.peak) )
		ctxt.sim.data.push(f'fact_approach', (lhs.recid, rhs.recid, epoch.peak_at * ctxt.sim.clock.step, round(epoch.peak, 4)))
		return

	def on_term(self, ctxt:Context, runlevel):
		""" Regulates and records the approaches still open, before the DataManager writes out
		Arguments
			ctxt -- Simulation context
			runlevel -- Termination run level; this acts at TERM_WRITE
		"""
		if runlevel != TERM_WRITE:
			return

		if self.watcher is not None:
			self.context	= ctxt
			self.watcher.flush( ctxt.sim.tickcount() )
		return

	def on_monitor_obstacle(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler to evaluate obstacle collision
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		lhs		= info[0]
		rhs		= info[1]

		# print( f'COLLISION! {lhs.config["name"]} and {rhs.config["name"]} at distance {info[2]:0.2}')
		return


if __name__ == "__main__":
	test = Collision("XXX")


