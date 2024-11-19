from cos.core.network.ORPCProxy import ORPCProxy


class World(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def init(self, bodies ):
		""" Initializes the world
		Arguments
			bodies -- Bodies to add to the simulation
		"""
		args={
			 'bodies':bodies
			}
		ORPCProxy.invoke(self,'init', args)
		return

	def has_collision(self, shape ):
		""" Checks for collisions in a region
		Arguments
			shape -- Shape of the region
		"""
		args={
			 'shape':shape
			}
		return int(ORPCProxy.invoke(self,'has_collision', args))

	def add(self, type, obj ):
		""" Adds an object to the world
		Arguments
			type -- Type of the object
			obj -- Object description
		"""
		args={
			 'type':type,
			 'obj':obj
			}
		ORPCProxy.invoke(self,'add', args)
		return


	def play(self):
		""" Runs a play loop
		"""
		args={
			}
		ORPCProxy.invoke(self,'play', args)
		return

	def describe(self, type ):
		""" Describes the world
		Arguments
			type -- Type of the object
		"""
		args={
			 'type':type
			}
		return ORPCProxy.invoke(self,'describe', args)


