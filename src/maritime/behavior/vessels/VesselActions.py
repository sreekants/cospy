#!/usr/bin/python
# Filename: VesselActions.py
# Description: Intents a vessel declares for the manoeuvres its behaviour is carrying out

from maritime.behavior.vessels.VesselManeuvers import VesselManeuvers

DECELERATE		= 'Manouever.CollisionAvoidance.Decelerate'
SLOWDOWN		= 'Speed.SlowdownForTraffic'				# Declared by VesselManeuvers.stop_for_safety
TSS_ENTER		= 'TrafficSeparationScheme.Enter'
TSS_EXIT		= 'TrafficSeparationScheme.Exit'
TSS_CROSSING	= 'TrafficSeparationScheme.Crossing'


class VesselActions:
	def __init__(self):
		return

	@staticmethod
	def declare(vessel, intent:str, held:bool):
		""" Sets an intent while it holds and resets it otherwise
		Arguments
			vessel -- Vessel
			intent -- Intent name
			held -- Whether the vessel is carrying it out
		"""
		if held:
			vessel.intent.set( intent )
		else:
			vessel.intent.reset( intent )
		return

	@staticmethod
	def slowing(b, world)->bool:
		""" Whether one of the behaviour's separation steps is slowing the vessel for another vessel
		Arguments
			b -- Vessel behaviour
			world -- Reference ot the simulation world
		"""
		ops		= b.ops or []
		if (VesselManeuvers.overtaking_distance in ops) and (VesselManeuvers.overtaking_separation(b) < 1.0):
			return True
		if (VesselManeuvers.crossing_slowdown in ops) and (VesselManeuvers.crossing_separation(b, world) < 1.0):
			return True

		return b.vehicle.intent.has( SLOWDOWN )

	@staticmethod
	def tss_legs(b):
		""" Whether the vessel is in a traffic separation scheme now, and at its next waypoint
		Arguments
			b -- Vessel behaviour
		Returns
			(inside, next inside); next inside is None without a next waypoint
		"""
		inside	= bool( b.map.in_tss(b.vehicle.boundary) )
		if b.next is None:
			return inside, None

		center	= b.rect.center
		target	= b.rect.move( b.next[1][0] - center[0], b.next[1][1] - center[1] )
		return inside, bool( b.map.in_tss(target) )

	@staticmethod
	def collision_avoidance(b, world, t, dx):
		""" Declares a deceleration while the behaviour slows the vessel for traffic
		Arguments
			b -- Vessel behaviour
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			dx -- Velocity the behaviour has set
		"""
		VesselActions.declare( b.vehicle, DECELERATE, VesselActions.slowing(b, world) )
		return dx

	@staticmethod
	def tss_lane(b, world, t, dx):
		""" Declares joining a scheme on the leg into it, and leaving it on the leg out (Rule 10(b)(iii))
		Arguments
			b -- Vessel behaviour
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			dx -- Velocity the behaviour has set
		"""
		inside, ahead	= VesselActions.tss_legs( b )
		VesselActions.declare( b.vehicle, TSS_ENTER, (not inside) and (ahead is True) )
		VesselActions.declare( b.vehicle, TSS_EXIT, inside and (ahead is False) )
		return dx

	@staticmethod
	def tss_crossing(b, world, t, dx):
		""" Declares crossing while in a scheme, for a vessel that crosses rather than follows lanes (Rule 10(c))
		Arguments
			b -- Vessel behaviour
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			dx -- Velocity the behaviour has set
		"""
		inside, _ahead	= VesselActions.tss_legs( b )
		VesselActions.declare( b.vehicle, TSS_CROSSING, inside )
		return dx


if __name__ == "__main__":
	test = VesselActions()
