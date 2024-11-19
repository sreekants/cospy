# Generated code

from cos.core.network.ORPCProxy import ORPCProxy


class Service(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def stop(self, name, args ):
		""" Stops the simulation
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		args={
			 'name':name,
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'stop', args))

	def start(self, name, args ):
		""" Start the simulation
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		args={
			 'name':name,
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'start', args))

	def suspend(self, name, args ):
		""" Suspend the simulation
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		args={
			 'name':name,
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'suspend', args))

	def resume(self, name, args ):
		""" Resume a simulation
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		args={
			 'name':name,
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'resume', args))

	def command(self, name, args ):
		""" Send a command to the simulation
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		args={
			 'name':name,
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'command', args))

	def signal(self, event, args ):
		""" Sends an event to the simulation
		Arguments
			event -- Event data
			args -- List of arguments
		"""
		args={
			 'event':event,
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'signal', args))

	def describe(self, scope, args ):
		""" Describes components of the simulation
		Arguments
			scope -- Scope namespace
			args -- List of arguments
		"""
		args={
			 'scope':scope,
			 'args':args
			}
		return ORPCProxy.invoke(self,'describe', args)

	def list(self, arg ):
		""" Lists objects of a type in a simulation
		Arguments
			arg -- Argument to the list
		"""
		args={
			 'arg':arg
			}
		return ORPCProxy.invoke(self,'list', args)




