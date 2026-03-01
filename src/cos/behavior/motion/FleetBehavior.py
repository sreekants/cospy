#!/usr/bin/python
# Filename: FleetBehavior.py
# Description: Implementation of the FleetBehavior class

from typing import List

from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.core.kernel.Configuration import Configuration
from cos.model.vehicle.Vehicle import Vehicle
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import cos,sin,atan2
import numpy as np
import csv

class FleetBehavior(MotionBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		MotionBehavior.__init__(self)

		args		= self.get_settings( config )
		if ('membership' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load( ctxt, ctxt.sim.config.resolve(args['membership']) )
		
		self.members	= None	# List of vessel names in the fleet
		self.vessels	= None	# List of vessel objects in the fleet
		return

		
	def load(self, ctxt, filename):
		""" Loads the behavior
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""

		self.members 	= []
		data 			= ctxt.sim.fs.read_file(filename)
		memberlist 		= csv.reader(StringIO(data), delimiter=',')
		rownum 			= 0

		# Store the members for delayed resolution
		for member in memberlist:
			if rownum == 0:		# Skip the header
				rownum	= rownum+1
				continue

			self.members.append(member[0])

		return

	def move(self, world, t, config):
		""" Moves the fleet
		Arguments
			world -- World object
			t -- Time step
			config -- Configuration attributes
		"""
		if self.vessels is None:
			self.__resolve(world.ctxt)

		for vessel in self.vessels:
			self.move_vessel(world.ctxt, vessel)

		return

	
	def __resolve(self, ctxt):
		""" Resolves the behavior
		Arguments
			ctxt -- Simulation context
		"""
		if self.members is None:
			return

		self.vessels = []
		for member in self.members:
			vessel = ctxt.sim.get_vessel(member)
			if vessel is not None:
				self.vessels.append(vessel)

		self.members = None	# Clear the members list to save memory
		return
	
	def move_vessel(self, ctxt, world, t, vessel, newvelocity=None):
		""" Moves the vessel
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel object
		"""
		# Send the notification to the vessel to move.

		return

	def update(self, world, t):
		"""Update all vehicles based on current behavior."""
		if obstacles is None:
			obstacles = []

		positions 	= self.get_positions()
		velocities	= {}


		# Precompute all the velocities before moving any vessel to ensure simultaneous updates
		for vessel, location, velocity in positions:
			velocities[vessel] = self.compute_velocity(vessel, location, velocity, positions, world, t)

		# Move all vessels based on the computed velocities
		for vessel, velocity in velocities.items():
			self.move_vessel(world.ctxt, world, t, vessel, velocity)

		# Nothing to do here since the actual movement is handled 
		# in move_vessel, which is called for each vessel with 
		# its computed velocity.
		return None, None
    
	def get_positions(self):
		"""Return current positions of all vehicles."""
		return [(v, v.location, v.velocity) for v in self.vessels]

if __name__ == "__main__":
	test = FleetBehavior()

