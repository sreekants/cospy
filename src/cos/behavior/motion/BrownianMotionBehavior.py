#!/usr/bin/python
# Filename: BrownianMotionBehavior.py
# Description: Random walk motion behavior

from cos.behavior.motion.LinearMotionBehavior import LinearMotionBehavior
from cos.math.geometry.Rectangle import Rectangle
import random, math


class BrownianMotionBehavior(LinearMotionBehavior):
	# Default class behavior uses the linear vectors defined in the configuration to move the object
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		LinearMotionBehavior.__init__(self, ctxt, config)

		args		= self.get_settings( config )

		self.set_zone( args['zone'] )
		return

	def set_zone(self, zone):
		self.zone	= None
		if zone is None:
			self.zone	= None
			return

		parts 	= zone.split(',')
		x		= int(parts[0])
		y		= int(parts[1])
		width	= int(parts[2])
		height	= int(parts[3])

		self.zone	= Rectangle(x, y, width, height)
		return
	
	def move(self, world, t, config):
		""" Moves the vehicle
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			config -- Configuration attributes
		"""
		LinearMotionBehavior.move(self, world, t, config)

		if self.zone is not None:
			self.limit_to(self.zone, self.x)
				
		# Introduce more entropy into the direction
		toss	= random.randrange(0,100)
		if self.entropy and toss<self.entropy:
			self.randomize_direction()
		

		return self.rect, self.dx

	def limit_to(self, region, pos):
		if region.encloses(pos[0], pos[1]) == False:
			norm		= self.bound_norm(region, pos)
			dx			= self.lastdx
			dx[0]		= abs(self.dx[0])*norm[0]
			dx[1]		= abs(self.dx[1])*norm[1]
				
			self.rect	= self.last
			self.dx		= dx

		return
	
	def bound_norm(self, rect, pos):
		center 		= rect.center

		if center[0] < pos[0]:
			dx		= -1.0
		else:
			dx		= 1.0
		 
		if center[1] < pos[1]:
			dy		= -1.0
		else:
			dy		= 1.0

		return (dx, dy)


if __name__ == "__main__":
	test = BrownianMotionBehavior()


