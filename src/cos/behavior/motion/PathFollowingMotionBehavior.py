#!/usr/bin/python
# Filename: PathFollowingMotionBehavior.py
# Description: A path following motion based on path file

from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.core.kernel.Configuration import Configuration
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import cos,sin,atan2
from enum import Enum
import numpy as np
import csv

class OperationState(Enum):
	UNKNOWN			= -1
	START			= 1,
	END				= 9

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
		self.atstate	= OperationState.UNKNOWN

		args			= self.get_settings( config )

		self.delay		= args.ToFloat('delay')
		self.looprun	= args.IsTrue('loop')
		self.reverse	= args.IsTrue('reverse')


		if ('pathfile' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load( ctxt, ctxt.sim.config.resolve(args['pathfile']) )

		self.plans		= []	# Stack of plans 
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
			action	= waypoint[7]			# An action to simulate at waypoint

			self.path.append( (t,
					# Location & Angular vectors
					np.array((x, y, z)),
					np.array((sog, cog, 0.0)),
					action
					) )

			if rownum == 1:		# First row has the start point
				self.atpoint	= 0
				self.x			= self.path[0][1]

			rownum	= rownum+1

		if len(self.path) == 0:
			raise Exception( f'No path plan loaded in file [{path}]' )
		
		self.current	= None
		self.next		= None
		self.atstate	= OperationState.START
		return

	def restart(self, reverse=False):
		if len(self.path) < 2:
			return
		
		if reverse == True:
			self.path.reverse()

		self.current	= self.path[0]
		self.next		= self.path[1]
		self.atpoint	= 0
		self.x			= self.current[1]
		self.atstate	= OperationState.START
		return

	def plan(self, path, looprun=False, reverse=False):
		self.path		= path
		self.current	= self.path[0]
		self.next		= self.path[1]
		self.atpoint	= 0
		self.x			= self.current[1]
		self.looprun	= looprun
		self.reverse	= reverse

		# Do not reset self.x because you may be at another location
		return

	def push(self):
		self.atstate	= OperationState.END
		self.plans.append( (self.path, self.current, self.next, self.atpoint, self.looprun, self.reverse, self.atstate) )
		return

	def pop(self):
		if not self.plans:
			return False
		
		checkpoint		= self.plans.pop()

		self.path		= checkpoint[0]
		self.current	= checkpoint[1]
		self.next		= checkpoint[2]
		self.atpoint	= checkpoint[3]
		self.looprun	= checkpoint[4]
		self.reverse	= checkpoint[5]
		self.atstate	= checkpoint[6]

		# Do not reset self.x because you may be at another location
		return True


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
		if self.path is None:
			return False
		
		if self.current is None:
			self.current	= self.path[0]
			self.next		= self.path[1]
			self.x			= self.current[1]
			self.atstate	= OperationState.START
			self.on_at_waypoint(world, t, self.atpoint, self.current)
			return False
		
		if self.delay > t.timestep:
			return False
		
		sog		= self.current[2][0]
		p1		= self.x
		p2		= self.next[1]

		# If there is no more distance to cover in the current 
		# waypoint segment, we do not shift.
		if Distance.euclidean(p1, p2) > sog:
			return  True

		# print(f'{self.atpoint}{self.next}={self.atstate}')		
		if self.atstate == OperationState.START:
			self.on_at_waypoint( world, t, self.atpoint, self.next )

		self.atstate	= OperationState.START
		self.atpoint	= self.atpoint+1
		self.current	= self.next

		# Make sure that we have more waypoint segments
		if self.atpoint >= len(self.path):
			self.atstate	= OperationState.END

			# Notify the end of the run
			if self.on_end_path(world, t, self.atpoint, self.current) == True:
				return
			
			self.current	= None
			self.next		= None

			# Restart if a loop run is expected
			if self.looprun == True:
				self.restart(self.reverse)
				# We have reset the path we need to loop again. So return false
				return False	

			self.path	= None
			return False

		self.next		= self.path[self.atpoint]
		return True

	def get_pos(self, world, t):
		""" Returns position and orientation vector
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
		"""

		if self.move_next(world, t) == False:
			return None

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

	def on_end_path(self, world, t, n, pt):
		# Pop any plan that might be queued
		return self.pop()

	def on_at_waypoint(self, world, t, n, pt):
		return
	


	@staticmethod
	def waypoint(path, t, x, y, z, sog, cog, action=''):
		# Helper function to build a path from way points.
		path.append( (t,
				# Location & Angular vectors
				np.array((x, y, z)),
				np.array((sog, cog, 0.0)),
				action
				) )
		
		return path

if __name__ == "__main__":
	test = PathFollowingMotionBehavior()


