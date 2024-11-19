from cos.core.network.ORPCProxy import ORPCProxy


class Port(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def describe(self, id ):
		""" Describes a port
		Arguments
			id -- Unique identifier
		"""
		args={
			 'id':id
			}
		return ORPCProxy.Invoke(self,'describe', args)




