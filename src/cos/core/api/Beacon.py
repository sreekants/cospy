from cos.core.network.ORPCProxy import ORPCProxy


class World(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def describe(self, id ):
		""" Describes an object
		Arguments
			id -- Unique object identifier
		"""
		args={
			 'id':id
			}
		return ORPCProxy.invoke(self,'describe', args)




