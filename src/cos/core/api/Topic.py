# Generated code

from cos.core.network.ORPCProxy import ORPCProxy


class Topic(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def pop(self, path ):
		""" Pops a message from the queue
		Arguments
			path -- IPC Topic path
		"""
		args={
			 'path':path
			}
		return ORPCProxy.invoke(self,'pop', args)

	def push(self, path, msg ):
		""" Pushes a message to queue
		Arguments
			path -- IPC Topic path
			msg -- Message to push
		"""
		args={
			 'path':path,
			 'msg':msg
			}
		return ORPCProxy.invoke(self,'push', args)

	def find(self, arg ):
		""" Finds a queue matching a criteria
		Arguments
			arg -- Search criteria
		"""
		args={
			 'arg':arg
			}
		return ORPCProxy.invoke(self,'find', args)

	def info(self, arg ):
		""" Returns information about a topic
		Arguments
			arg -- Topic argument
		"""
		args={
			 'arg':arg
			}
		return ORPCProxy.invoke(self,'info', args)

	def list(self, arg ):
		""" List all topics
		Arguments
			arg -- Filter criteria
		"""
		args={
			 'arg':arg
			}
		return ORPCProxy.invoke(self,'list', args)

	def type(self, arg ):
		""" Returns the type of a topic
		Arguments
			arg -- Filter criteria
		"""
		args={
			 'arg':arg
			}
		return ORPCProxy.invoke(self,'type', args)

	def route(self, src, dest ):
		""" Route a message from a source to a destination
		Arguments
			src -- Source path
			dest -- Destination path
		"""
		args={
			 'src':src,
			 'dest':dest
			}
		return ORPCProxy.invoke(self,'route', args)

	def unroute(self, path ):
		""" Removes a route
		Arguments
			path -- IPC Topic path
		"""
		args={
			 'path':path
			}
		return ORPCProxy.invoke(self,'unroute', args)


