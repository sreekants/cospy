#!/usr/bin/python
# Filename: Actor.py
# Description: Impmenentation of a controller class for all sumulation objectsRunnerThread

from cos.core.simulation.Behavior import Behavior, ActorBehavior
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ArgList import ArgList
from cos.core.kernel.Context import Context

import numpy as np


class Actor:
	def __init__(self, ctxt:Context, config:dict):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.behaviors	= None
		self.loop		= -1 	# Loop count
		self.name		= config["name"]

		# Initialize the simulation states
		null_vector		= np.zeros(3)
		self.loop		= 0 	# Loop count
		self.rect		= None
		self.x			= null_vector
		self.dx			= null_vector
		self.d2x		= null_vector
		
		return

	def create(self, ctxt:Context, vehicle, config:dict):	
		""" Creates the actor behaviors
		Arguments
			vehicle -- Vehicle object to create the actor for
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.create_behavior( ctxt, vehicle, config )
		return
	
	def init( self, rect ):
		""" Initializes an actor
		Arguments
			rect -- Bounding box of the initial position of the actor body
		"""
		# Initialize the simulation states
		null_vector		= np.zeros(3)
		self.loop		= 0 	# Loop count
		self.rect		= rect
		self.x			= null_vector
		self.dx			= null_vector
		self.d2x		= null_vector

		# print( f"Initializing {self.name} to {self.rect}")

		# Initialize the behavior
		motion			= self.behaviors.get(ActorBehavior.MOTION)
		if motion is not None:
			motion.init( rect )
			self.x		= motion.position
			self.dx		= motion.velocity
		return

	def update(self, world, config):
		""" Update the simulant controlled by the actor
		Arguments
			world -- Reference ot the simulation world
			config -- Configuration attributes
		"""
		if self.loop == -1:
			return None, None, None

		self.loop	= self.loop+1
		for behavior in self.behaviors.values():
			if behavior.type not in [ActorBehavior.MOTION, ActorBehavior.DYNAMICS]:
				continue
					
			pos, dx		= behavior.update( world, self.loop, config )

			self.d2x	= (dx-self.dx)/2.0	# Acceleration
			self.dx		= dx				# Velocity
			self.x		= behavior.position
			self.rect	= pos				# Position

		return self.rect, self.dx, None

	def get_position(self):
		""" Returns the position vector of the simulant
		"""
		return self.x

	def get_velocity(self):
		""" Returns the velocity vector of the simulant
		"""
		return self.dx

	def get_acceleration(self):
		""" Returns the velocity vector of the simulant
		"""
		return self.d2x

	@property
	def motion(self):
		""" Returns the motion behavior of the actor
		"""
		return self.behaviors.get(ActorBehavior.MOTION)

	def create_behavior(self, ctxt, vehicle, config:dict):
		""" Creates a behavior from a configuration
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.behaviors	= {}

		modules		= ArgList(config.get("behavior"))
		if len(modules) == 0:
			return self.behaviors


		behavior_types = [
				(ActorBehavior.MOTION, 				"motion"),
				(ActorBehavior.DYNAMICS,			"dynamics"),
				(ActorBehavior.SENSOR, 				"sensor"),

				(ActorBehavior.CONTROL_MOTION, 		"control.motion"),
				(ActorBehavior.CONTROL_DYNAMICS, 	"control.dynamics"),
				(ActorBehavior.CONTROL_SENSOR, 		"control.sensor")
			]

		for type in behavior_types:
			pkg		= modules[type[1]]
			if pkg is None:
				continue

			klassname, klass	= BootLoader.load_class( pkg )

			self.behaviors[type[0]] = klass(ctxt, config)


		# Initialize all behaviors after initial creation
		for b in self.behaviors.values():
			b.intialize( self, vehicle, config )

		return self.behaviors


	def runnable(self, ctxt:Context, config):
		""" Checks if the object is runnable
		Arguments
			ctxt -- Simulation context
			config -- Config information
		"""

		for behavior in self.behaviors.values():
			if behavior.runnable(ctxt, config) == False:
				return False
		return True

	def notify(self, ctxt:Context, method:str, arg:dict):
		for behavior in self.behaviors.values():
			behavior.notify( ctxt, method, arg )
		return


if __name__ == "__main__":
	test = Actor()


