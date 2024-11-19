from cos.core.network.ORPCProxy import ORPCProxy


class Vessel(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def describe(self, id ):
		""" Describes a vessel
		Arguments
			id -- Unique identifier
		"""
		args={
			 'id':id
			}
		return ORPCProxy.invoke(self,'describe', args)

	def init(self, id, config ):
		""" Initializes a vessel
		Arguments
			id -- Unique identifier
			config -- Configuration attributes
		"""
		args={
			 'id':id,
			 'config':config
			}
		ORPCProxy.invoke(self,'init', args)
		return

	def update(self, id, state ):
		""" Updates a vessel
		Arguments
			id -- Unique identifier
		"""
		args={
			 'id':id,
			 'state':state
			}
		return ORPCProxy.invoke(self,'update', args)


	def ioctl(self, id, op, arg ):
		""" Sends control signal to the vessel
		Arguments
			id -- Unique identifier
			op -- Operation code
			arg -- arguments for the operation
		"""
		args={
			 'id':id,
			 'op':op,
			 'arg':arg
			}
		return ORPCProxy.invoke(self,'ioctl', args)



