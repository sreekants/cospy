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

		self.course_monitor	= Ticker( 0.5 )	# Monitor every half second	

		# Load the ship model
		args		= self.get_settings( config )
		if ('ship.model' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load_model( ctxt, ctxt.sim.config.resolve(args['ship.model']) )


		# Navigation path state (used in NAVIGATING mode)
		self.nav_path    	= []
		self.nav_current 	= None
		self.nav_next    	= None
		self.nav_at      	= 0
		self.nav_loop    	= False

		if ('pathfile' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load_nav_path(ctxt, ctxt.sim.config.resolve(args['pathfile']))
			self.nav_loop 	= args.IsTrue('loop')
			if self.nav_path:
				self.mode 	= Operation.TRANSPORT

		self.ranges	= [
			(1, 2, 0)		# Default velocity range
			]


		# Sequence of behavior operations
		self.ops 			= None
		self.postops		= None

		# Behavior watchdogs
		self.anchor_watch	= None
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
		# TODO: Generalize the watches.
		if self.anchor_watch is None:
			rect, dx	=  PathFollowingMotionBehavior.update(self, world, t, config)
			return rect, dx
		
		if self.anchor_watch.signaled() == True:
			self.movable        = True
			self.anchor_watch   = None
			self.vehicle.under_way()

		return self.rect, self.dx

	def anchor(self, duration):
		self.movable        = False
		self.anchor_watch	= Ticker( duration )
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
	def load_nav_path(self, ctxt, filename):
		data   = ctxt.sim.fs.read_file(filename)
		reader = csv.reader(StringIO(data), delimiter=',')
		rownum = 0
		for waypoint in reader:
			if rownum == 0:
				rownum += 1
				continue
			t   = float(waypoint[1])
			x   = float(waypoint[2])
			y   = float(waypoint[3])
			z   = float(waypoint[4])
			sog = float(waypoint[5])
			cog = float(waypoint[6])
			self.nav_path.append((t, np.array((x, y, z)), np.array((sog, cog, 0.0))))
			if rownum == 1:
				self.nav_current = self.nav_path[0]
				self.nav_at      = 0
				self.x            = self.nav_current[1]
			if rownum == 2:
				self.nav_next = self.nav_path[1]
			rownum += 1

	def nav_restart(self):
		if len(self.nav_path) < 2:
			return
		self.nav_current = self.nav_path[0]
		self.nav_at      = 0
		self.x            = self.nav_current[1]
		self.nav_next    = self.nav_path[1]

	def nav_heading(self):
		"""Advance to next waypoint if close enough and return target velocity vector."""
		if (self.nav_next is None) or (self.nav_current is None):
			return None

		sog = self.nav_current[2][0]
		if Distance.euclidean(self.x, self.nav_next[1]) <= sog:
			self.nav_at += 1
			if self.nav_at >= len(self.nav_path):
				self.nav_current = None
				self.nav_next    = None
				if self.nav_loop:
					self.nav_restart()
				return None
			self.nav_current = self.nav_next
			self.nav_next    = self.nav_path[self.nav_at]

		theta = atan2(self.nav_next[1][1] - self.x[1], self.nav_next[1][0] - self.x[0])
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




if __name__ == "__main__":
	test = PlannedVesselBehavior(None, None)
