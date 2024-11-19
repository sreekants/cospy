#!/usr/bin/python
# Source File: MQ.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService

class MQ(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		return

	def push( self, domain, queuename, message, config ):
		""" Pushes a message to queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			message -- Message data
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def pop( self, domain, queuename, config ):
		""" Pops a message from the queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def peek( self, domain, queuename, config ):
		""" Reads a message from a queue without popping it.
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def move( self, domain, criteria, sourcequeuename, targetqueuename, config ):
		""" Moves a queue
		Arguments
			domain -- Domain namespace
			criteria -- Criteria of selection
			sourcequeuename -- Source queue name
			targetqueuename -- Destination queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def is_empty( self, domain, queuename, config ):
		""" Checks if a queue is empty
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def getcount( self, domain, queuename, config ):
		""" Checks if a queue exists
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def exists( self, domain, queuename, config ):
		""" Removes all messages from a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def purge( self, domain, queuename, config ):
		""" Removes all messages from a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def create( self, domain, queuename, config ):
		""" Creates a new queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def delete( self, domain, queuename, config ):
		""" Deletes a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def locate( self, domain, criteria, config ):
		""" Finds a queue given a criteria
		Arguments
			domain -- Domain namespace
			criteria -- #TODO
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def list( self, domain, queuename, config ):
		""" List all queue within a scope
		Arguments
			domain -- Domain namespace
			queuename -- Queue name scope
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def get_property( self, domain, queuename, name, config ):
		""" Returns a property of a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			name -- Name of the object
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def set_property( self, domain, queuename, name, value, config ):
		""" Sets a property of the queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			name -- Name of the object
			value -- #TODO
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def describe( self, domain, queuename, config ):
		""" Describes a queue
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456

	def add_route( self, domain, queuename, route, config ):
		""" Adds a queue route
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			route -- Route to add
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def delete_route( self, domain, queuename, route, config ):
		""" deletes a queue route
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			route -- Route to remove
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def is_route( self, domain, queuename, route, config ):
		""" Checks if a route exists between a queue and a path
		Arguments
			domain -- Domain namespace
			queuename -- Queue name
			route -- Route queue path
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return 123456




