#!/usr/bin/python
# Filename: EnvironmentService.py
# Description: Implementation of the EnvironmentService class

from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context

class EnvironmentService(Service):
	def __init__(self, world, type):
		""" Constructor
		Arguments
			world -- Reference ot the simulation world
			type -- Type of the object
		"""
		Service.__init__(self, 'Weather/Environment', type)

		self.world	= world
		return

	def get_actor(self, ctxt:Context, path):
		""" #TODO: get_actor
		Arguments
			ctxt -- Simulation context
			path -- #TODO
		"""
		obj = ctxt.sim.objects.get_all(path)
		if obj == None:
			return []
		return obj

	def init_group(self, ctxt:Context, group, membership):
		""" #TODO: init_group
		Arguments
			ctxt -- Simulation context
			group -- #TODO
			membership -- #TODO
		"""
		for element in membership:
			group[element[0]]	= self.get_actor(ctxt, element[1])

		return

	def update_groups(self, groups):
		""" #TODO: update_groups
		Arguments
			groups -- #TODO
		"""
		# Update the position of our vessel, environment etc.
		for group in groups.values():
			for inst in group:
				inst.sim_update( self.world )
		return

if __name__ == "__main__":
	test = EnvironmentService()


