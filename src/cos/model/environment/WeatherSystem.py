#!/usr/bin/python
# Filename: WeatherSystem.py
# Description: Implementation of the WeatherSystem class

from cos.core.kernel.Object import Object
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.math.geometry.Distance import Distance
from cos.physics.force.DecayFunction import ExponentialDecay
from cos.model.environment.Actors import Actors, ActorType
from cos.core.utilities.ArgList import ArgList

from cos.model.environment.WeatherSystemGenerator import WeatherSystemGenerator

import numpy as np
import math, random

EPSILON = 0.0001


class WeatherSystem(Object):
	def __init__(self, system, config):
		""" Constructor
		Arguments
			system -- Type identifier of the weather system
			config -- Configuration attributes
		"""
		category	= f'Weather.{self.__class__.__name__}'
		Object.__init__( self, category )

		self.data	= []
		self.dirty	= False
		self.build	= False
		self.system	= system
		return

	# Simulation functions
	def sim_update(self, world):
		""" Updates the simulation
		Arguments
			world -- Reference ot the simulation world
		"""
		if (self.timer is None) or (self.timer.signaled() == False):
			return

		self.generate(world)
		self.update_actors(world)
		self.update_vectors(world)
		self.notify(world)
		return

	def generate(self, world, filename=None):
		""" Helper function to generate a weather system and safe it to a file
		Arguments
			world -- Reference ot the simulation world
			filename -- Name of the file to store the force tensors into
		"""
		if self.build == False:
			return

		if filename is None:
			filename	= f"{self.__class__.__name__}.csv"

		generator	= WeatherSystemGenerator()
		generator.generate(world)
		generator.save(filename)

		self.build = False
		return

	def update_actors(self, world):
		""" Updates all the actors in the simulation with weather vectors
		Arguments
			world -- Reference ot the simulation world
		"""
		actors:Actors = world.actors

		for group in actors.vehicles.values():
			for vehicle in group:
				self.update_vehicle( vehicle )
		return

	def notify(self, world):
		""" Notifies all clients about an update to the weather force fields
		Arguments
			world -- Reference ot the simulation world
		"""
		if self.dirty == False:
			return

		world.sim.ipc.push( '/IPC', 'weather.update', None, [self.describe()] )
		self.dirty	= False
		return


	def init_config(self, args:ArgList):
		""" Initializes the weather system configurations
		Arguments
			args -- List of arguments
		"""
		# Parse configurations
		self.poll_at		= args["Sample.Rate"]

		# Initialize timer ticks
		if self.poll_at is not None:
			self.timer	= Ticker( int(self.poll_at) )
		else:
			self.timer	= None
		return

	def scale_vector(self, V, scale ):
		""" Scales a weather vector
		Arguments
			V -- Force vector
			scale -- Scaling factor vector
		"""
		dims	= len(scale)
		for n in range(len(V)):
			V[n]	= V[n]*scale[n%dims]
		return V

	def load(self, ctxt:Context, args:ArgList, records, file:str):
		""" Loads weather configurations from a file
		Arguments
			ctxt -- Simulation context
			args -- List of arguments
			records -- Records loaded from a weather system
			file -- File path  #TODO: Remove
		"""
		self.init_config( args )

		# TODO: Should each weather system type (simulation-level) have a scale,
		# or should each weather database (file-level) have its own scale??
		scale	= ctxt.sim.world.scales.weather[self.system]

		for rec in records:
			pos	= self.scale_vector([float(x) for x in rec[1].split(',')][:3], scale)	# Position vectors
			Vx	= self.scale_vector([float(x) for x in rec[2].split(',')][:9], scale)	# Velocity vectors
			Vr	= [float(x) for x in rec[3].split(',')][:9]								# Rotational vectors (DO NOT SCALE!)

			args		= ArgList( rec[4] )
			decay		= args["force.decay"]

			if decay is None:
				decay	= 0.00001

			self.data.append([pos,
					 np.array(Vx).reshape(3,3), 	# Linear vector
					 np.array(Vr).reshape(3,3),		# Vortex vector
					 ExponentialDecay( decay )		# Force decay function
					 ])

		if ctxt and len(self.data) < 3:
			ctxt.sim.log.warning( self.type, f'Insuffucient datapoints to simulate weather in class [{self.__class__.__name__}].' )
		return

	def describe(self):
		""" Describes the weather system
		"""
		result		= []

		for sample in self.data:
			pos		= sample[0]
			Vx		= sample[1][0].tolist()
			Vr		= sample[2][0].tolist()

			result.append( { "P":pos, "X": Vx, "R": Vr} )

		return {
				"type":self.__class__.__name__,
				"guid":self.guid,
				"vectors":result
		}

	def at(self, x:float, y:float, z=None):
		""" Returns the force vector at a particular location
		Arguments
			x -- X coordinate
			y -- Y coordinate
			z -- Z coordinate
		"""
		Vx, Vr, dist, decay	= self.nearest(x, y, z)
		if Vx is None:
			return None

		# A minimalist exponential decay function
		Vx		= (decay(Vx,dist))
		Vx[Vx < EPSILON] = 0.0
		return Vx

	def nearest(self, x:float, y:float, z=None):
		""" Identifies the nearest vector in a force field
		Arguments
			x -- X coordinate
			y -- Y coordinate
			z -- Z coordinate
		"""
		matches 	= []
		matchdist	= None

		for sample in self.data:
			pos		= sample[0]
			dist	= Distance.euclidean( (x,y), sample[0] )

			if matchdist == None:
				matches.append( (sample,dist) )
				matchdist	= dist
				continue

			if dist < matchdist:
				matches[0]	= (sample,dist)

		if len(matches) == 0:
			return (None, None, None, None)

		Forces	= matches[0][0]
		dist	= matches[0][1]
		Vx		= Forces[1]
		Vr		= Forces[2]
		decay	= Forces[3]
		return (Vx[0], Vr[0], dist, decay)

	def update_vectors(self, world):
		""" Updates all the vectors in the force fields of a weather system
		Arguments
			world -- Reference ot the simulation world
		"""
		for n in range(0, len(self.data)):
			sample	= self.data[n]
			Vx		= sample[1]
			deg		= sample[2][0][0]

			if abs(deg) < EPSILON:
				continue

			x			= Vx[0][0]
			y			= Vx[0][1]
			Vxx			= math.cos(deg) * x - math.sin(deg) * y
			Vxy			= math.sin(deg) * x + math.cos(deg) * y
			Vnew		= np.array( [Vxx, Vxy, 0.0] )

			# Update the vector
			Vx[0]		= Vnew
			self.dirty	= True

		return

	def update_vehicle(self, vehicle):
		""" Overridable method to update a simulation vehicle
		Arguments
			vehicle -- Reference ot the simulation vehicle
		"""
		location	= vehicle.location
		if location is None:
			return

		force	= self.at( location[0], location[1], location[2] )
		if force is None:
			return

		vehicle.force( self.system, force )
		return

if __name__ == "__main__":
	test = WeatherSystem()


