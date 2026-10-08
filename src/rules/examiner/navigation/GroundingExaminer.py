#!/usr/bin/python
# Filename: GroundingExaminer.py
# Description: Implementation of the GroundingExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from cos.model.examiner.Examination import ExaminationType
from maritime.model.zone.ZoneRules import ZoneRules
from cos.core.kernel.Context import Context
from cos.core.kernel.Object import TERM_WRITE
from cos.core.utilities.ArgList import ArgList
from cos.model.situation.EpisodeWatcher import EpisodeWatcher, epoch_of

# REQUIREMENT:
# Grounding: a vessel at sea standing into water too shallow for its draught.
#
# The map reports a nominal depth per sea shape, so the test is the under-keel
# clearance - depth less draught less the vessel's own allowance - against the
# margin the zone demands. Negative clearance is contact with the seabed; a
# positive clearance under the margin is a near miss, scored more lightly.
#
# NOTE:
# Berthing is the same arithmetic in inland water and lives in
# BerthingExaminer; which zone types each is answerable for is declared in
# config/examiner/zones.yaml, not here, so a jurisdiction can move the line.



class GroundingExaminer(ZoneAware, NavigationExaminer):
	EXAMINES	= ExaminationType.GROUNDING
	TOPIC		= '/Faculty/Concern/Grounding'
	MESSAGE		= 'vessel.grounding'
	
	ZONES		= 'grounding_zones'
	MARGIN		= 'grounding_margin'
	CONTACT		= 'grounding.contact'
	NEAR_MISS	= 'grounding.margin'

	watcher		= None		# Set up in setup(); without it a near miss is scored on every pass

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)

		self.watcher	= None		# Clearance less margin per vessel; a near miss is scored once per epoch
		self.contacted	= set()		# Vessels whose open epoch touched the seabed
		self.context	= None		# Simulation context, for the epoch callback
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner. Deliberately does not chain to Examiner.setup:
		this examiner is driven by the map and zones.yaml, not by a Legata
		automaton, so it has no automata or scorecard to load.
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os'] )
		self.watcher	= EpisodeWatcher( 0.0, self.on_epoch, span=epoch_of(config), below=True )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		return

	def judge(self, ctxt:Context, rule_ctxt):
		""" Judges rule_ctxt.situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		vessel		= rule_ctxt.situation.os
		shapes, rules, depth	= self.survey( vessel )

		# Answerable only for the zone types this examiner owns.
		if ZoneRules.applies_in( rules, self.ZONES, shapes ) == False:
			return

		# A nominal reading is clear water, whichever layer set it (REQ-022-A4)
		if ZoneRules.seabed_depth( shapes ) is None:
			self.settle( vessel, self.CONTACT, shapes )
			self.settle( vessel, self.NEAR_MISS, shapes )
			return

		clearance	= self.clearance( vessel, depth )
		if clearance is None:
			return			# The vessel declares no draught; nothing to judge

		self.score( ctxt, vessel, shapes, rules, depth, clearance )
		return

	def score(self, ctxt:Context, vessel, shapes, rules, depth, clearance):
		""" Scores the clearance against the zone's margin
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel under examination
			shapes -- Map shapes enclosing the vessel
			rules -- Merged zone rules
			depth -- Seabed depth beneath the vessel
			clearance -- Water left beneath the keel
		"""
		margin	= float( rules.get(self.MARGIN, 0.0) or 0.0 )
		key		= self.identify( vessel )

		if self.watcher is not None:
			self.context	= ctxt
			self.watcher.observe( key, clearance - margin, ctxt.sim.tickcount(), (vessel, shapes, depth, clearance, margin) )

		if clearance > margin:
			# Clear water ends the finding, so a regrounding counts again
			self.settle( vessel, self.CONTACT, shapes )
			self.settle( vessel, self.NEAR_MISS, shapes )
			return 0.0

		if clearance > 0.0:
			if self.watcher is not None:
				return 0.0		# A near miss is scored once per epoch, in on_epoch()
			return self.report( ctxt, vessel, self.NEAR_MISS, shapes, depth, clearance, margin )

		if self.watcher is not None:
			self.contacted.add( key )
		return self.report( ctxt, vessel, self.CONTACT, shapes, depth, clearance, margin )

	def report(self, ctxt:Context, vessel, event:str, shapes, depth, clearance, margin, epoch=None):
		""" Records a finding and announces it
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel under examination
			event -- CONTACT or NEAR_MISS
			shapes -- Map shapes enclosing the vessel
			depth -- Seabed depth beneath the vessel
			clearance -- Water left beneath the keel
			margin -- Margin the zone demands
			epoch -- Epoch the near miss closes, if any
		"""
		penalty	= self.violate( ctxt, vessel, event, shapes, value=clearance,
								detail=f'depth {depth:.1f} m, clearance {clearance:.2f} m, '
									   f'margin {margin:.2f} m' )

		payload	= {
			'vessel'	: self.identify( vessel ),
			'time'		: ctxt.sim.now(),
			'zone'		: self.zone_name( shapes ),
			'event'		: event,
			'depth'		: depth,
			'clearance'	: clearance,
			'margin'	: margin,
			'penalty'	: penalty,
		}
		if epoch is not None:
			payload['epoch']	= epoch.summary()

		self.announce( ctxt, self.TOPIC, self.MESSAGE, payload )
		return penalty

	def on_epoch(self, epoch):
		""" Scores one near miss for an epoch inside the margin that never touched the seabed
		Arguments
			epoch -- Ended epoch; its detail is the peak's (vessel, shapes, depth, clearance, margin)
		"""
		if epoch.key in self.contacted:
			self.contacted.discard( epoch.key )
			return

		vessel, shapes, depth, clearance, margin	= epoch.detail
		self.report( self.context, vessel, self.NEAR_MISS, shapes, depth, clearance, margin, epoch )
		self.settle( vessel, self.NEAR_MISS, shapes )		# The next epoch scores again
		return

	def end(self, ctxt:Context, rule_ctxt):
		""" Ends the epochs of vessels not judged this pass
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.watcher is not None:
			self.context	= ctxt
			self.watcher.lapse( ctxt.sim.tickcount() )
		return

	def on_term(self, ctxt:Context, runlevel):
		""" Scores the epochs still open, before the DataManager writes out
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


if __name__ == "__main__":
	test = GroundingExaminer()
