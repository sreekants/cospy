from cos.core.network.ORPCProxy import ORPCProxy


class Sea(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def describe(self, id ):
		""" Describes a sea
		Arguments
			id -- Unique identifier
		"""
		args={
			 'id':id
			}
		return ORPCProxy.invoke(self,'describe', args)




