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

import math

# REQUIREMENT:
# Grounding: a vessel at sea standing into water too shallow for its draught.
#
# The map reports a nominal depth per sea shape, so the test is the under-keel
# clearance - depth less draught less the vessel's own allowance - against the
# margin the zone demands. Contact with the seabed is scored only when certain:
# when even the deep edge of the depth band (depth_max) leaves no clearance.
# Any other clearance under the margin, a possible contact included, is a near
# miss, scored more lightly.
#
# NOTE:
# Berthing is the same arithmetic and lives in BerthingExaminer. The situation
# decides which answers: slow and close to land is berthing, anything else is
# grounding (COS.049). The zone type only picks the margin, through
# berthing_zones and grounding_zones in config/examiner/zones.yaml.



class GroundingExaminer(ZoneAware, NavigationExaminer):
	EXAMINES	= ExaminationType.GROUNDING
	TOPIC		= '/Faculty/Concern/Grounding'
	MESSAGE		= 'vessel.grounding'
	
	ZONES		= 'grounding_zones'
	MARGIN		= 'grounding_margin'
	CONTACT		= 'grounding.contact'
	NEAR_MISS	= 'grounding.margin'
	BERTHING	= False		# Answers for contacts outside a berthing situation

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

		# Berthing and grounding split by situation, in every zone
		if self.berthing( vessel, rules ) != self.BERTHING:
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
		margin	= self.margin( rules, shapes )
		key		= self.identify( vessel )

		if self.watcher is not None:
			self.context	= ctxt
			self.watcher.observe( key, clearance - margin, ctxt.sim.tickcount(), (vessel, shapes, depth, clearance, margin) )

		if clearance > margin:
			# Clear water ends the finding, so a regrounding counts again
			self.settle( vessel, self.CONTACT, shapes )
			self.settle( vessel, self.NEAR_MISS, shapes )
			return 0.0

		if self.certain( vessel, shapes, clearance ) == False:
			if self.watcher is not None:
				return 0.0		# A near miss is scored once per epoch, in on_epoch()
			return self.report( ctxt, vessel, self.NEAR_MISS, shapes, depth, clearance, margin )

		if self.watcher is not None:
			self.contacted.add( key )
		return self.report( ctxt, vessel, self.CONTACT, shapes, depth, clearance, margin )

	def certain(self, vessel, shapes, clearance)->bool:
		""" Whether a vessel is certainly on the seabed: no clearance even at the band's deep edge
		Arguments
			vessel -- Vessel under examination
			shapes -- Map shapes enclosing the vessel
			clearance -- Clearance at the band's shallow reading
		"""
		if clearance > 0.0:
			return False

		bound	= ZoneRules.depth_bound( shapes )
		if bound is None:
			return True			# A sounding, or a map without band edges

		deepest	= self.clearance( vessel, bound )
		return (deepest is not None) and (deepest <= 0.0)

	@staticmethod
	def margin(rules, shapes)->float:
		""" Under-keel margin the zone demands: berthing_margin in a berthing zone, else grounding_margin
		Arguments
			rules -- Merged zone rules
			shapes -- Map shapes enclosing the vessel
		"""
		key	= 'berthing_margin' if ZoneRules.applies_in( rules, 'berthing_zones', shapes ) else 'grounding_margin'
		return float( rules.get(key, 0.0) or 0.0 )

	def berthing(self, vessel, rules)->bool:
		""" Whether a vessel is berthing: at or below berthing_speed within berthing_distance of land
		Arguments
			vessel -- Vessel under examination
			rules -- Merged zone rules
		"""
		speed, distance	= rules.get( 'berthing_speed' ), rules.get( 'berthing_distance' )
		velocity		= getattr( vessel, 'velocity', None )
		if (speed is None) or (distance is None) or (velocity is None):
			return False

		if math.hypot( velocity[0], velocity[1] ) > float( speed ):
			return False

		land	= self.distance_to_land( vessel )
		return (land is not None) and (land <= float( distance ))

	def distance_to_land(self, vessel):
		""" Metres from a vessel to the nearest land boundary, or None without land, as (OwnShip,Map.Land).Distance
		Arguments
			vessel -- Vessel under examination
		"""
		position	= getattr( vessel, 'location', None )
		if (position is None) or (len( self.land or [] ) == 0):
			return None

		return min( shape.area.clearance(position[0], position[1]) for shape in self.land )

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
		bound	= ZoneRules.depth_bound( shapes )
		band	= f' (band to {bound:g} m)' if bound is not None else ''
		penalty	= self.violate( ctxt, vessel, event, shapes, value=clearance,
								detail=f'depth {depth:.1f} m{band}, clearance {clearance:.2f} m, '
									   f'margin {margin:.2f} m' )

		payload	= {
			'vessel'	: self.identify( vessel ),
			'time'		: ctxt.sim.now(),
			'zone'		: self.zone_name( shapes ),
			'event'		: event,
			'depth'		: depth,
			'clearance'	: clearance,
			'depth_max'	: bound,
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
