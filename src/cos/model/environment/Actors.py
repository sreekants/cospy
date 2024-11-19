#!/usr/bin/python
# Filename: Actors.py
# Description: Implementation of an orchestrator class that conducts the simulation

from cos.model.environment.EnvironmentService import EnvironmentService
from cos.core.kernel.Context import Context

from enum import Enum

class ActorType(Enum):
	VESSEL				= 1,
	COS					= 2


class Actors(EnvironmentService):
	def __init__(self, world):
		""" Constructor
		Arguments
			world -- Reference ot the simulation world
		"""
		EnvironmentService.__init__(self, world, 'Actors')

		self.vehicles 	= {}
		for type in ActorType:
			self.vehicles[type] = []
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		EnvironmentService.on_start(self, ctxt, config)

		# Adds an object to the world
		self.vehicles[ActorType.VESSEL]		= ctxt.sim.objects.get_all("/World/Vehicle")

		# Initialize all the vessels to simulate
		for vessel in self.vehicles[ActorType.VESSEL]:
			vessel.sim_init(self, None)

		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		self.update()
		return


	def init(self, obj):
		""" #TODO: init
		Arguments
			obj -- #TODO
		"""
		for vessel in self.vehicles[ActorType.VESSEL]:
			if vessel.id != obj["guid"]:
				continue

			vessel.sim_init(self, obj["rect"])
		return

	def update(self):
		""" #TODO: update
		"""
		self.update_groups(self.vehicles)
		return

	def get_collision(self, item, group):
		""" #TODO: get_collision
		Arguments
			item -- #TODO
			group -- #TODO
		"""
		# if pygame.sprite.spritecollideany(self.cos, self.vehicles[ActorType.VESSEL]):
		#	return True

		return []

	def play(self):
		""" #TODO: play
		"""
		vessels	= self.vehicles[ActorType.VESSEL]
		coss	= self.vehicles[ActorType.COS]

		for cos in coss:
			# Check if any vessel have collided with the COS
			if len(self.get_collision(cos, vessels)) != 0:
				# Stop the loop
				return False

		return True

if __name__ == "__main__":
	test = Actors()


