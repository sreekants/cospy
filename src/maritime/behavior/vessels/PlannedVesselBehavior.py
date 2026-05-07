#!/usr/bin/python
# Filename: VesselBehavior.py
# Description: Implementation of the VesselBehavior class

from maritime.navigation.cartography.Map import Map
from maritime.model.vessel.Vessel import Vessel, Operation
from cos.core.time.Ticker import Ticker
from cos.behavior.motion.PathFollowingMotionBehavior import PathFollowingMotionBehavior
from cos.behavior.motion.VesselModel import VesselModel
from cos.math.geometry.Distance import Distance

from io import StringIO
from math import atan2, cos, sin, degrees, radians

import csv, random
import numpy as np


class PlannedVesselBehavior(PathFollowingMotionBehavior):
	def __init__(self, ctxt, config):
		PathFollowingMotionBehavior.__init__(self, ctxt, config)
		self.map	= ctxt.sim.objects.get("/Services/Controls/Navigation/Map")
		self.model	= VesselModel()
		self.mode	= Operation.TRANSPORT

		self.mode 			= Operation.TRANSPORT
		self.xscale			= 1.0

		# Sequence of behavior operations
		self.ops 			= None
		self.postops		= None

		# Behavior watchdogs
		self.watchdogs	= {}


		return

	def intialize(self, ctxt, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			ctxt -- Simulation context
			actor -- Actor to initialize the behavior for
			vehicle -- Vehicle object to create the actor for
			config -- Configuration attributes
		"""
		PathFollowingMotionBehavior.intialize(self, ctxt, actor, vehicle, config)

		# Watch the course every 5 seconds
		self.add_watch( 'course', 5, self.on_watch_course )

		self.ranges	= [
			(1, 2, 0)		# Default velocity range
			]


		# Load the ship model
		args		= self.get_settings( config )
		if ('ship.model' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load_model( ctxt, ctxt.sim.config.resolve(args['ship.model']) )

		return

	def add_watch(self, key, duration, fn, ctxt=None):
		self.watchdogs[key]	= (Ticker(duration), fn, ctxt)
		return

	def remove_watch(self, key):
		self.watchdogs[key]	= None
		return


	def load_model(self, ctxt, filename):
		""" Loads a simulation model
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""

		self.model.load(self.get_file(ctxt, filename))
		return


	def update(self, world, t, config):
		self.saved_x      	= self.x
		self.saved_rect   	= self.rect

		rect, dx	=  PathFollowingMotionBehavior.update(self, world, t, config)

		# Check for watchs		
		for v in self.watchdogs.values():
			if (v is not None) and (v[0].signaled() == True):
				v[1](v[2])

		return rect, dx

	
	def anchor(self, duration):
		self.movable        = False
		self.add_watch( 'anchor', duration, self.on_end_anchor )
		self.vehicle.anchored()
		return


	def move(self, world, t, config):
		"""Follow the planned path, applying vessel-specific adjustments and momentum."""

		pos = self.get_pos(world, t)
		if pos is None:
			self.dx = np.zeros(3)
			return self.rect, self.dx


		target_dx = pos[2]

		# Apply the simulated operation to the vessel
		if self.ops is not None:
			for fn in self.ops:
				target_dx = fn(self, world, t, target_dx)
	
		self.dx   = target_dx

		# Check for any collision with rigid bodies (land, flotillas etc.)
		center    = self.rect.center
		newpos    = self.x + self.dx + self.d2x/2.0
		self.rect = self.rect.move(newpos[0] - center[0], newpos[1] - center[1])

		if self.can_move(world, self.rect):
			self.last = self.rect
			self.x    = newpos
		else:
			self.rect = self.last

		# Apply post-operation methods. These methods are expected to not
		# interfere with the simulated position of the vessel
		if self.postops is not None:
			for fn in self.postops:
				fn(self, world, t, self.dx)

		return self.rect, self.dx


	# Navigation path management
	def heading(self):
		"""Advance to next waypoint if close enough and return target velocity vector."""
		if (self.next is None) or (self.current is None):
			return None

		sog = self.current[2][0]
		if Distance.euclidean(self.x, self.next[1]) <= sog:
			self.atpoint += 1
			if self.atpoint >= len(self.path):
				self.current = None
				self.next    = None
				if self.looprun:
					self.restart()
				return None
			self.current = self.next
			self.next    = self.path[self.atpoint]

		theta = atan2(self.next[1][1] - self.x[1], self.next[1][0] - self.x[0])
		return np.array((sog * cos(theta), sog * sin(theta), 0.0))

	def randomize_direction(self):
		""" Randomize the direction of the vehicle
		"""
		V		= self.ranges[0]
		vmax	= max(V[0], V[1])	# Maxmum velocity
		vmin	= vmax*0.1			# Minimum velocity
		vrange	= vmax - vmin		# Range of velocity

		self.dx[0]	= vmin+vrange*float(random.randint(0, 100))/100.0
		self.dx[1]	= vmin+vrange*float(random.randint(0, 100))/100.0

		if random.randint(-1,0) :
			self.dx[0]	= self.dx[0] * -1.0

		if random.randint(-1,0) :
			self.dx[1]	= self.dx[1] * -1.0

		return 


	@staticmethod
	def random_walk(path, dist, next, nways):
		for n in range(0, nways):
			tn   = 0
			x    = next[1][0]+dist*float(random.randint(0, 100))/100.0
			y    = next[1][1]+dist*float(random.randint(0, 100))/100.0
			z    = 0
			
			PathFollowingMotionBehavior.waypoint(path, tn, x, y, z, 0.0, 0.0)

		return path


	# Overridable callbacks
	def on_watch_course(self, ctxt):
		return

	def on_end_anchor(self, ctxt):
		self.movable        = True
		self.remove_watch('anchor')
		self.vehicle.under_way()
		return

if __name__ == "__main__":
	test = PlannedVesselBehavior(None, None)
