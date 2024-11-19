#!/usr/bin/python
# Filename: LinearMotionBehavior.py
# Description:  Default motion behavior uses the linear vectors defined in the configuration to move the object

from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.subsystem.world.World import World

import numpy as np
import random, math


class LinearMotionBehavior(MotionBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		MotionBehavior.__init__(self)

		args		= self.get_settings( config )
		pose 	  	= config["pose"]

		self.initialize_dynamics(pose["position"], pose["X"], pose["R"])

		if 'entropy' in args:
			self.entropy	= int(args['entropy'])
		else:
			self.entropy	= 100	# Percentage of entropy introduced into the behavior

		self.has_forces	= True
		return

	def initialize_dynamics(self, loc, X, R):
		""" Initialize the dynamics vectors
		Arguments
			loc -- Location
			X -- Linear vector
			R -- Rotational vector
		"""
		self.x		= np.array( (loc[0], loc[1], loc[2]) )	# Position vector
		self.dx		= np.array( (X[0], X[1], X[2]) )		# Velocity vector
		self.d2x	= np.array( (X[3], X[4], X[5]) )		# Acceleration vector

		self.θ		= np.array( (R[0], R[1], R[2]) )	# Rotational velocity vector
		self.dθ		= np.array( (R[3], R[4], R[5]) )	# Rotational vector

		return

	def move(self, world, t, config):
		""" Moves the vehicle
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			config -- Configuration attributes
		"""
		# If the sprite is animated using a velocity vector, we
		#  move it relative to the original position
		center		= self.rect.center
		newpos		= self.translate(world, t)
		self.rect	= self.rect.move( newpos[0]-center[0], newpos[1]-center[1] )

		# If the sprite has collided, reverse the vehicle
		if world.has_collision(self.rect) == False:
			self.last	= self.rect
			self.x		= newpos
		else:
			# Randomly accelerate
			scale		= float(random.randint(25, 100)-50)/100.0
			self.loop	= 0
			self.dx		= self.dx * -(1.0+scale)	# Reverse the direction

			if self.entropy and random.randrange(0,100)<self.entropy:
				self.randomize_direction()

			# Move the sprite to the last known good position
			self.rect	= self.last

		return self.rect, self.dx

	def translate(self, world, t):
		""" Translates the behicle to a new location
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
		"""
		if not np.any(self.θ):
			return self.x + self.dx

		θ			= np.radians( self.θ[0] )
		cosθ, sinθ	= np.cos(θ), np.sin(θ*(t/100))

		grad		= self.apply_force(world, self.dx)
		dx 			= grad[0]
		dy 			= grad[1]
		delta		= np.array(
					(cosθ*dx - sinθ*dy,
					sinθ*dx + cosθ*dy,
					 0))

		return self.x + delta

	def apply_force(self, world:World, delta):
		""" Applies environmental forces to the vehicle
		Arguments
			world -- Reference ot the simulation world
			delta -- Offset if the vehicle
		"""
		if self.has_forces == False:
			return delta

		for type, force in self.forces.items():
			if not np.any(force):
				continue

			force	= force * world.scales.weather[type]
			delta	= delta+force

		return delta


	def randomize_direction(self):
		""" Randomize the direction of the vehicle
		"""
		minvel	= 2
		maxvel	= 5
		self.dx[1]	= self.dx[1]+float(random.randint(minvel, maxvel))/float(maxvel)
		self.dx[0]	= self.dx[0]+float(random.randint(minvel, maxvel))/float(maxvel)


		if self.dx[0] > maxvel:
			self.dx[0]	= math.copysign(random.randint(minvel, maxvel), self.dx[0])

		if self.dx[1] > maxvel:
			self.dx[1]	= math.copysign( random.randint(minvel, maxvel), self.dx[1])
		return

	@property
	def position(self):
		""" Returns the current position
		"""
		return self.x

	@property
	def velocity(self):
		""" Returns the current velocity
		"""
		return self.dx

if __name__ == "__main__":
	test = LinearMotionBehavior()


