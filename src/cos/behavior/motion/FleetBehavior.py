#!/usr/bin/python
# Filename: FleetBehavior.py
# Description: Implementation of the FleetBehavior class

from typing import List

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

		self.members	= []	# List of vessel names in the fleet

		args		= self.get_settings( config )
		if ('membership' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load( ctxt, ctxt.sim.config.resolve(args['membership']) )
		
		return

	def intialize(self, ctxt, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			actor -- Actor to initialize the behavior for
		"""
		MotionBehavior.intialize(self, ctxt, actor, vehicle, config)

		self.resolve(ctxt.sim)
		return
		
	def load(self, ctxt, filename):
		""" Loads the behavior
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""
		data 			= ctxt.sim.fs.read_file(filename)
		memberlist 		= csv.reader(StringIO(data), delimiter=',')
		rownum 			= 0

		# Store the members for delayed resolution
		for member in memberlist:
			if rownum == 0:		# Skip the header
				rownum	= rownum+1
				continue

			self.append_member( ctxt, member[1].strip(), int(member[2]) )

		return
	
	def append_member(self, ctxt, vessel, type):
		""" Appends a member to the fleet
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel object to append
			type -- Type of the vessel (e.g., "leader", "follower")
		"""
		self.members.append((vessel, type))
		return

	def move(self, world, t, config):
		""" Moves the fleet
		Arguments
			world -- World object
			t -- Time step
			config -- Configuration attributes
		"""
		for vessel in self.vessels:
			self.move_vessel(world.ctxt, vessel)

		return

	
	def resolve(self, sim):
		""" Resolves the vessels in the fleet based on the member names
		Arguments
			ctxt -- Simulation context
		"""

		# If the vessels have already been resolved, do nothing
		if self.members is None:
			return

		#print(sim.objects.dump())

		# Resolve the vessel objects based on the member names
		self.vessels = []
		for id, type in self.members:
			vessel	= sim.objects.find("/World/Vehicle/Vessel", id )
			if vessel is not None:
				self.vessels.append((vessel, type))
			else:
				self.log.info( "Fleet", f"Warning: Vessel with id '{id}' not found in the simulation.")

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
	test = FleetBehavior()

