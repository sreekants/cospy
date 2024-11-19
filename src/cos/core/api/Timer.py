# Generated code

from cos.core.network.ORPCProxy import ORPCProxy


class Timer(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def get_utc(self):
		""" Returns the simulation time in UTC
		"""
		args={
			}
		return int(ORPCProxy.invoke(self,'get_utc', args))

	def get_tickcount(self):
		""" Returns the total number oc clock ticks passed
		"""
		args={
			}
		return int(ORPCProxy.invoke(self,'get_tickcount', args))




