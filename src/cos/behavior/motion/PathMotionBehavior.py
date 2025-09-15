#!/usr/bin/python
# Filename: PathMotionBehavior.py
# Description: A path motion based on path file

from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.core.kernel.Configuration import Configuration
import numpy as np
import csv
from io import StringIO

class PathMotionBehavior(MotionBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		MotionBehavior.__init__(self)

		self.path		= []
		self.tstart	= 0

		args		= self.get_settings( config )
		if ('pathfile' in args) and (ctxt is not None) and (ctxt.sim.config is not None):
			self.load( ctxt, ctxt.sim.config.resolve(args['pathfile']) )

		self.looprun	= args.IsTrue('loop')
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

			# Velocity
			dx		= float(waypoint[5])
			dy		= float(waypoint[6])
			dz		= float(waypoint[7])

			# Accelearation
			d2x		= float(waypoint[8])
			d2y		= float(waypoint[9])
			d2z		= float(waypoint[10])


			ψ		= float(waypoint[11])		# Yaw
			θ		= float(waypoint[12])		# Pitch
			φ		= float(waypoint[13])		# Roll

			dψ		= float(waypoint[14])		# Yaw velocity
			dθ		= float(waypoint[15])		# Pitch velocity
			dφ		= float(waypoint[16])		# Roll velocity

			d2ψ		= float(waypoint[17])		# Yaw acceleration
			d2θ		= float(waypoint[18])		# Pitch acceleration
			d2φ		= float(waypoint[19])		# Roll acceleration

			self.path.append( (t,
					# Location & Angular vectors
					np.array((x, y, z)),
					np.array((dx, dy, dz)),
					np.array((d2x, d2y, d2z)),

					# Rotational vectors
					np.array((ψ, θ, φ)),
					np.array((dψ, dθ, dφ)),
					np.array((d2ψ, d2θ, d2φ))
					) )

			if rownum == 1:		# First row has the start point
				self.x	= self.path[0][1]

			rownum	= rownum+1
		return

	def restart(self, t):
		if len(self.path) < 1:
			return
		
		self.tstart	= t
		self.x			= self.path[0][1]
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

		return self.rect, self.dx

	def translate(self, t):
		""" Moves the vehicle to a new point
		Arguments
			t -- Time on the simulation clock
		"""
		# Find the matching waypoint
		pos	= self.get_pos(t)
		if pos is None:			
			self.dx	= np.zeros(3)
			return self.x

		self.dx		= pos[2]
		return self.x + self.dx

	def get_pos(self, t):
		""" Returns position and orientation vector
		Arguments
			t -- Time on the simulation clock
		"""
		# Find the matching waypoint
		waypoint	= None
		for p in self.path:
			if (p[0]+self.tstart) > t:
				break

			waypoint	= p

		if (waypoint is None) and (self.looprun == True):
			self.restart(t)
			return
		
		return waypoint

if __name__ == "__main__":
	test = PathMotionBehavior()


