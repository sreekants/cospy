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

	def stop(self, args ):
		""" Stops a service
		Arguments
			args -- List of arguments
		"""
		args={
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'stop', args))

	def start(self, args ):
		""" Start a service
		Arguments
			args -- List of arguments
		"""
		args={
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'start', args))

	def suspend(self, args ):
		""" Suspend a service
		Arguments
			args -- List of arguments
		"""
		args={
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'suspend', args))

	def resume(self, args ):
		""" Resume a service
		Arguments
			args -- List of arguments
		"""
		args={
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'resume', args))

	def command(self, name, args ):
		""" Invoke a command on a service
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
		""" Send a signal to a service
		Arguments
			event -- Event to send
			args -- List of arguments
		"""
		args={
			 'event':event,
			 'args':args
			}
		return int(ORPCProxy.invoke(self,'signal', args))

	def describe(self, scope, args ):
		""" Describes the service
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
		""" Lists all services
		Arguments
			arg -- Argument to the command
		"""
		args={
			 'arg':arg
			}
		return ORPCProxy.invoke(self,'list', args)

	def info(self, path ):
		""" Retrieves information about a service
		Arguments
			path -- Path to the service
		"""
		args={
			 'path':path
			}
		return ORPCProxy.invoke(self,'info', args)



