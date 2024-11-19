from cos.core.network.ORPCProxy import ORPCProxy


class Radar(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def describe(self, id ):
		""" Describes a radar
		Arguments
			id -- Unique identifier
		"""
		args={
			 'id':id
			}
		return ORPCProxy.Invoke(self,'describe', args)




