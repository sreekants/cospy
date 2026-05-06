#!/usr/bin/python
# Filename: PathFollowingMotionBehavior.py
# Description: A path following motion based on path file

from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.core.kernel.Configuration import Configuration
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import cos,sin,atan2
import numpy as np
import csv

class PathFollowingMotionBehavior(MotionBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		MotionBehavior.__init__(self)

		self.path		= []
		self.current	= None
		self.next		= None
		self.atpoint	= 0

		args		= self.get_settings( config )
		if ('pathfile' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load( ctxt, ctxt.sim.config.resolve(args['pathfile']) )

		self.looprun	= args.IsTrue('loop')
		self.reverserun	= args.IsTrue('reverse')
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

	def load(self, ctxt, filename):
		""" Loads the behavior
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""
		data = ctxt.sim.fs.read_file(filename)

		path 	= csv.reader(StringIO(data), delimiter=',')
		rownum	= 0
		for waypoint in path:
			if rownum == 0:		# Skip the header
				rownum	= rownum+1
				continue

			id		= int(waypoint[0])

			# Time
			t		= float(waypoint[1])

			# Location
			x		= float(waypoint[2])
			y		= float(waypoint[3])
			z		= float(waypoint[4])

			# Trajectory
			sog		= float(waypoint[5])	# Path over ground
			cog		= float(waypoint[6])	# Course over ground

			self.path.append( (t,
					# Location & Angular vectors
					np.array((x, y, z)),
					np.array((sog, cog, 0.0))
					) )

			if rownum == 1:		# First row has the start point
				self.current	= self.path[0]
				self.atpoint	= 0
				self.x			= self.current[1]


			if rownum == 2:		# Second row has the next point
				self.next		= self.path[1]

			rownum	= rownum+1
			
		return

	def restart(self, reverse=False):
		if len(self.path) < 2:
			return
		
		if reverse == True:
			self.path.reverse()

		self.current	= self.path[0]
		self.atpoint	= 0
		self.x			= self.current[1]
		self.next		= self.path[1]
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

		# print( f'at {t}:{self.rect}')

		# If we cannot move to a region on the map, revert back to the previous position
		if self.can_move(world, self.rect):
			self.last	= self.rect
			self.x		= newpos

		return self.rect, self.dx

	def translate(self, world, t):
		""" Moves the vehicle to a new point
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
		"""
		# Find the matching waypoint
		pos	= self.get_pos(world, t)
		if pos is None:
			self.dx	= np.zeros(3)
			return self.x

		self.dx		= pos[2]
		return self.x + self.dx + self.d2x/2.0

	def move_next(self, world, t):
		""" Moves to the next point
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
		"""
		if (self.next is None) or (self.current is None):
			return
		
		sog		= self.current[2][0]
		p1		= self.x
		p2		= self.next[1]

		# If there is more distance to cover in the current 
		# waypoint segment, we do not shift.
		if Distance.euclidean(p1, p2) > sog:
			return
		
		self.atpoint	= self.atpoint+1

		# Make sure that we have more waypoint segments
		if self.atpoint == len(self.path):
			self.current	= None
			self.next		= None

			# Restart if a loop run is expected
			if self.looprun == True:
				self.restart(self.reverserun)

			return
		
		self.current	= self.next
		self.next		= self.path[self.atpoint]

		self.on_waypoint( world, t, self.atpoint, self.current )
		return

	def get_pos(self, world, t):
		""" Returns position and orientation vector
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
		"""

		self.move_next(world, t)

		if (self.next is None) or (self.current is None):
			return None
		
		sog		= self.current[2][0]
		p1		= self.x
		p2		= self.next[1]
			
		theta 	= atan2(p2[1]-p1[1], p2[0]-p1[0])

		return (t,
				self.x,
				np.array((sog*cos(theta), sog*sin(theta), 0.0))
				)

	def on_waypoint(self, world, t, n, pt):
		return

if __name__ == "__main__":
	test = PathFollowingMotionBehavior()


