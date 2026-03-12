#!/usr/bin/python
# Filename: PreyBehavior.py
# Description: Implementation of the PreyBehavior class

from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.behavior.swarm.Prey import Prey, Config as PreyConfig
from cos.behavior.swarm.Predator import Predator, Config as PredatorConfig
from cos.behavior.swarm.Swarm import Swarm
from cos.math.geometry.Rectangle import Rectangle
from cos.math.geometry.Point import Point
from cos.math.geometry.Vector import Vector
from maritime.traffic import actor

class WorldAdapter:
	""" Adapter class to provide a consistent interface for the swarm behavior to interact with the simulation world.
	"""
	def __init__(self, world, predators=None):
		self.world = world
		self.predatorList = predators if predators is not None else []
		return

	@property
	def predators(self):
		return self.predatorList

	def bound(self, obj, pos: Point, vel: Vector):
		"""Wrap position around zone (toroidal world)."""
		actor 		= obj.ref.actor
		boundary	= actor.rect
		rect		= Rectangle(pos.x - boundary.w/2, pos.y - boundary.h/2, boundary.width, boundary.height)

		if self.world.has_collision(rect) == True:
			obj.vel = vel * -1.0
			return obj.last_pos

		x 				= pos.x + vel.x
		y 				= pos.y + vel.y
		nextpos 		= Point(x, y)
		obj.last_pos 	= pos
		return nextpos
	

	def shortestBoundedPathTo(self, a: Vector, b: Vector):
		"""
		Shortest displacement vector from a -> b in a toroidal world.
		Arguments
			a -- start point
			b -- end point
		"""
		dx = b.x - a.x
		dy = b.y - a.y

		return Vector(dx, dy)


	def boundedDist(self, a: Vector, b: Vector) -> float:
		return self.shortestBoundedPathTo(a, b).norm()

class VesselAdapter:
	""" Adapter class to provide a consistent interface for the swarm behavior to interact with the vessel objects in the simulation.
	"""
	def __init__(self, vessel):
		self.vessel = vessel
		return

	def move(self, pos, vel):
		self.vessel.locate_at( [pos.x, pos.y, 0] )
		self.vessel.heading_towards( [vel.x, vel.y, 0] )
		return
	
class PreyAdapter(Prey, VesselAdapter):
	def __init__(self, pos: Point, vel: Vector, ref=None):
		Prey.__init__(self, pos, vel, ref)
		VesselAdapter.__init__(self, ref)
		return

	def move( self, tooClose, tooFar, avgDist, meanHeading, predatorList, world, cfg ):	
		Prey.move( self, tooClose, tooFar, avgDist, meanHeading, predatorList, world, cfg )
		VesselAdapter.move(self, self.pos, self.vel)
		return

class PredatorAdapter(Predator, VesselAdapter):
	def __init__(self, pos: Point, vel: Vector, ref=None):
		Predator.__init__(self, pos, vel, ref)
		return

	def move( self, tooClose, tooFar, avgDist, meanHeading, predatorList, world, cfg ):	
		Predator.move( self, tooClose, tooFar, avgDist, meanHeading, predatorList, world, cfg )
		VesselAdapter.move(self, self.pos, self.vel)
		return

class PreyBehavior(FleetBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		FleetBehavior.__init__(self, ctxt, config)

		self.swarm			= Swarm()
		self.preys			= []
		self.predators		= [] 
		self.predList		= []
		return

	def intialize(self, ctxt, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			actor -- Actor to initialize the behavior for
		"""
		FleetBehavior.intialize(self, ctxt, actor, vehicle, config)

		preycfg = PreyConfig()
		predcfg = PredatorConfig()

		preycfg.speed  = 0.5
		predcfg.speed  = 0.5

		preys = []
		predators = []


		for v in self.vessels:
			vessel		= v[0]
			type 		= v[1]

			pose		= vessel.config['pose']	
			position	= pose['position']
			X			= pose['X']
			pos			= Point(position[0], position[1])
			vel			= Vector(X[0], X[1])

			if type == 100000:
				preys.append(PreyAdapter(pos, vel, vessel))
			elif type == 200000:
				predators.append(PredatorAdapter(pos, vel, vessel))	

		# Resolve the members to the swarm behavior
		self.swarm.setPreys(preycfg, preys )
		self.swarm.setPredators(predcfg, predators )
		self.predList = predators
		return


	def append_member(self, ctxt, vessel, type):
		""" Appends a member to the fleet
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel object to append
			type -- Type of the vessel (e.g., "leader", "follower")
		"""
		FleetBehavior.append_member(self, ctxt, vessel, type)

		if type == 100000:	
			self.preys.append(vessel)
		elif type == 200000:	
			self.predators.append(vessel)
		return


	def update(self, world, t, config, obstacles=None):
		""" Updates the behavior
		Arguments
			world -- World object
			t -- Current time step
			config -- Configuration attributes
			obstacles -- List of obstacles in the world (optional)
		"""

		# Update the swarm behavior
		self.swarm.move(WorldAdapter(world, self.predList))
		return None, None
		

if __name__ == "__main__":
	test = PreyBehavior()

