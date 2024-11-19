# Generated code

from cos.core.network.ORPCProxy import ORPCProxy


class MQ(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def push(self, domain, queuename, message, config ):
		""" Pushes a message to queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			message -- Message data
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'message':message,
			 'config':config
			}
		ORPCProxy.invoke(self,'push', args)
		return


	def pop(self, domain, queuename, config ):
		""" Pops a message from the queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		ORPCProxy.invoke(self,'pop', args)
		return ORPCProxy.GetResponseBody(self)

	def peek(self, domain, queuename, config ):
		""" Reads a message from a queue without popping it.
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		ORPCProxy.invoke(self,'peek', args)
		return ORPCProxy.GetResponseBody(self)

	def move(self, domain, criteria, sourcequeuename, targetqueuename, config ):
		""" Moves a queue
		Arguments
			domain -- Domain namespace
			criteria -- Criteria of selection
			sourcequeuename -- Source queue name
			targetqueuename -- Destination queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'criteria':criteria,
			 'sourcequeuename':sourcequeuename,
			 'targetqueuename':targetqueuename,
			 'config':config
			}
		ORPCProxy.invoke(self,'move', args)
		return

	def is_empty(self, domain, queuename, config ):
		""" Checks if a queue is empty
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		return (ORPCProxy.invoke(self,'is_empty', args)=='true')

	def getcount(self, domain, queuename, config ):
		""" Returns the number of messages in the queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		return int(ORPCProxy.invoke(self,'getcount', args))

	def exists(self, domain, queuename, config ):
		""" Checks if a queue exists
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		return (ORPCProxy.invoke(self,'exists', args)=='true')

	def purge(self, domain, queuename, config ):
		""" Removes all messages from a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		ORPCProxy.invoke(self,'purge', args)
		return

	def create(self, domain, queuename, config ):
		""" Creates a new queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		ORPCProxy.invoke(self,'create', args)
		return

	def delete(self, domain, queuename, config ):
		""" Deletes a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		ORPCProxy.invoke(self,'delete', args)
		return

	def locate(self, domain, criteria, config ):
		""" Finds a queue given a criteria
		Arguments
			domain -- Domain namespace
			criteria -- Criteria to search for
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'criteria':criteria,
			 'config':config
			}
		return ORPCProxy.invoke(self,'locate', args)

	def list(self, domain, queuename, config ):
		""" List all queue within a scope
		Arguments
			domain -- Domain namespace
			queuename -- Queue name scope
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		return ORPCProxy.invoke(self,'list', args)

	def get_property(self, domain, queuename, name, config ):
		""" Returns a property of a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			name -- Name of the object
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'name':name,
			 'config':config
			}
		return ORPCProxy.invoke(self,'get_property', args)

	def set_property(self, domain, queuename, name, value, config ):
		""" Sets a property of the queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			name -- Name of the object
			value -- Value to assign
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'name':name,
			 'value':value,
			 'config':config
			}
		ORPCProxy.invoke(self,'set_property', args)
		return

	def describe(self, domain, queuename, config ):
		""" Describes a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'config':config
			}
		return ORPCProxy.invoke(self,'describe', args)

	def add_route(self, domain, queuename, route, config ):
		""" Adds a queue route
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			route -- Route to add
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'route':route,
			 'config':config
			}
		ORPCProxy.invoke(self,'add_route', args)
		return

	def delete_route(self, domain, queuename, route, config ):
		""" deletes a queue route
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			route -- Route to remove
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'route':route,
			 'config':config
			}
		ORPCProxy.invoke(self,'delete_route', args)
		return

	def is_route(self, domain, queuename, route, config ):
		""" Checks if a route exists between a queue and a path
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			route -- Route queue path
			config -- Configuration attributes
		"""
		args={
			 'domain':domain,
			 'queuename':queuename,
			 'route':route,
			 'config':config
			}
		return (ORPCProxy.invoke(self,'is_route', args)=='true')




