#!/usr/bin/python
# Filename: BasicHydrodynamicBehavior.py
# Description: Implementation of the BasicHydrodynamicBehavior class

from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.math.geometry.Rectangle import Rectangle
from cos.behavior.motion.MotionBehavior import DynamicForce
from cos.behavior.motion.VesselModel import VesselModel

import numpy as np


class BasicHydrodynamicBehavior(MotionBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		MotionBehavior.__init__(self)

		self.rect	= Rectangle( -2, -1, 4, 2 )
		self.model	= VesselModel()

		args		= self.get_settings( config )

		if ('ship.model' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load_model( ctxt, ctxt.sim.config.resolve(args['ship.model']) )

		pose 	  	= config["pose"]

		self.initialize_dynamics(pose["position"], pose["X"], pose["R"])
		return

	def initialize_dynamics(self, loc, X, R):
		""" Initializes the dynamics vector
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

	def get_file(self, ctxt, filename):
		""" Returns the content of a simulation file
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""
		if ctxt is None:
			return open(filename, 'r').read()

		return ctxt.sim.fs.read_file_as_bytes(filename)

	def load_model(self, ctxt, filename):
		""" Loads a simulation model
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""

		self.model.load(self.get_file(ctxt, filename))

		self.t			= 0

		# Initial states
		self.states 	= [self.model.north, self.model.east, self.model.yaw, self.model.speed, self.model.yaw_rate]

		# Data capture
		self.time			= [self.t]
		self.stored_states	= []
		self.speeds			= [self.states[3]]
		self.norths			= [self.states[0]]
		self.easts			= [self.states[1]]
		self.stored_states.append( self.states )
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
		newpos		= self.translate(t)
		self.rect	= self.rect.move( newpos[0]-center[0], newpos[1]-center[1] )

		# If we cannot move to a region on the map, revert back to the previous position
		if self.can_move(world, self.rect):
			self.last	= self.rect
			self.x		= newpos
		else:
			self.rect	= self.last

		return self.rect, self.dx

	def translate(self, t):
		""" Translates the vector
		Arguments
			t -- Time on the simulation clock
		"""
		self.states = self.model.ship.dynamics(
						states=self.states,
						wind_speed=self.get_wind(),
						speed_ref=self.model.speed_ref,
						heading_ref=self.model.yaw_ref, time_step=self.model.dt )

		north	= self.states[0]
		east	= self.states[1]

		self.stored_states.append(self.states)
		self.speeds.append(self.states[3])
		self.norths.append(north)
		self.easts.append(east)
		self.t = self.t + self.model.dt
		self.time.append(self.t)

		self.dx	= np.array((east, north, 0.0))
		return self.x + self.dx

	def get_wind(self):
		""" Returns the wind vector
		"""
		return self.forces[DynamicForce.WIND_CURRENT]

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

	def ioctl(self, op, arg):
		""" Handles operation signals
		Arguments
			op -- Operation code
			arg -- arguments for the operation
		"""
		if op == 'motion.thrust':
			self.x	= self.x + arg.x
			return
		
		if op == 'motion.heading':
			self.x	= self.x + arg.x
			return

		return

if __name__ == "__main__":
	test = BasicHydrodynamicBehavior()


