#!/usr/bin/python
# Filename: BasicHydrodynamicBehavior.py
# Description: Implementation of the BasicHydrodynamicBehavior class

from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.behavior.motion.HydrodynamicModel import Ship
from cos.math.geometry.Rectangle import Rectangle
from cos.behavior.motion.MotionBehavior import DynamicForce
from cos.core.kernel.Configuration import Configuration

import numpy as np
import yaml


class BasicHydrodynamicBehavior(MotionBehavior):
	def __init__(self, ctxt, config=None):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		MotionBehavior.__init__(self)

		self.ship	= None
		self.rect	= Rectangle( -2, -1, 4, 2 )

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

		config	= yaml.safe_load( self.get_file(ctxt, filename) )

		dynamics		= config['hydrodynamics']

		self.north 		= dynamics['north']
		self.east 		= dynamics['east']
		self.yaw 		= dynamics['yaw'] * np.pi/180
		self.yaw_ref 	= dynamics['yaw_ref'] * np.pi/180
		self.speed 		= dynamics['speed']
		self.speed_ref 	= dynamics['speed_ref']
		self.yaw_rate 	= dynamics['yaw_rate']
		self.dt 		= dynamics['dt']
		self.t			= 0

		# Initial states
		self.states 	= [self.north, self.east, self.yaw, self.speed, self.yaw_rate]

		physics			= config['physics']
		self.ship 		= Ship(mass=physics['mass'],
							linear_damping_coeff=physics['linear_damping_coeff'],
							length=physics['length'],
							width=physics['width'],
							dt=self.dt )

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

		# print( f'at {t}:{self.rect}')
		# If we have collided, revert back to the previous position
		if world.has_collision(self.rect) == False:
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
		self.states = self.ship.dynamics(
						states=self.states,
						wind_speed=self.get_wind(),
						speed_ref=self.speed_ref,
						heading_ref=self.yaw_ref, time_step=self.dt )

		north	= self.states[0]
		east	= self.states[1]

		self.stored_states.append(self.states)
		self.speeds.append(self.states[3])
		self.norths.append(north)
		self.easts.append(east)
		self.t = self.t + self.dt
		self.time.append(self.t)

		self.dx	= np.array((east, north, 0.0))
		return self.x + self.dx

	def get_wind(self):
		""" Returns the wind vector
		"""
		return self.force[DynamicForce.WIND_CURRENT]

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


