#!/usr/bin/python
# Filename: MessageQueue.py
# Description: Implemention of an in-memory message queue for inter-process communication

from cos.core.kernel.Context import Context
from cos.core.kernel.Event import Event
from cos.core.kernel.Topic import Topic
from cos.core.utilities.Tree import Tree, TreeNode
from cos.core.utilities.Errors import ErrorCode

import fnmatch, queue, threading

DEFAULT_THROTTLE_RATE	= 1000

class PumpCtxt:
	def __init__(self, throttle_rate):
		""" Constructor
		Arguments
			throttle_rate -- Number messages processed per loop
		"""
		self.processed		= 0
		self.throttle_rate	= throttle_rate
		return


class MessageQueue:
	# TODO: Naive implementation using dictionaries. Use a more efficient storage system.

	def __init__(self):
		""" Constructor
		"""
		self.queues		= Tree()
		self.routes		= {}
		self.loopback	= Topic()
		self.echo		= '/Echo'

		self.ipcq		= Topic()
		self.ipc		= '/IPC'
		self.bridge		= '/Bridge'		# Parent of the per-browser queues the bridge server drains
		self.bridge_only	= { 'vessel.state' }	# Events published to the bridge queues and not to /IPC

		self.broker		= None
		self.publisher	= None		# Bins viewer events per tick, if loaded

		self.throttle_rate	= DEFAULT_THROTTLE_RATE
		self.lock			= threading.RLock()		# Guards the queue tree and routes across threads
		return

	def pump(self, path:str, throttle_rate:int=-1):
		""" Pumps pending messages at a given throttle rate
		Arguments
			path -- Queue path
			throttle_rate -- Number messages processed per loop
		"""
		if throttle_rate < 0:
			throttle_rate	= self.throttle_rate

		ctxt	= PumpCtxt( throttle_rate )

		if path is None:
			self.queues.traverse( MessageQueue.__pump_node, ctxt )
		else:
			with self.lock:
				node	= self.queues.find( path )
			if node is not None:
				node.traverse( MessageQueue.__pump_node, ctxt, 8 )

		return ctxt.processed

	def pump_node(self, node:TreeNode, throttle_rate:int=-1, depth:int=8):
		""" Pumps pending messages on a node at a given throttle rate
		Arguments
			node -- Reference to a node
			throttle_rate -- Number messages processed per loop
		"""
		if throttle_rate < 0:
			throttle_rate	= self.throttle_rate

		ctxt	= PumpCtxt( throttle_rate )

		if node is not None:
			if depth > 0:
				# Pump the child nodes first
				node.traverse( MessageQueue.__pump_node, ctxt, depth )

			# Then pump the node itself
			MessageQueue.__pump_node( ctxt, node )			

		return ctxt.processed

	def get_node(self, path:str, depth=2):
		""" Returns a node dereferencing routes
		Arguments
			path -- Path to a node or a route
			depth -- Number of de-references on routes
		"""
		if depth <= 0:
			return None

		with self.lock:
			node = self.queues.find(path)
			if node is not None:
				return node

			if path in self.routes:
				return self.get_node(self.routes[path], depth-1)

		return None

	def subscribe(self, path:str, listener):
		""" Subscribes to messages at a path
		Arguments
			path -- Path of the queue
			listener -- Listener object to attach subscription
		"""
		if path.startswith('/') == False:
			raise Exception( f'Invalid topic name [{path}]' )

		with self.lock:
			node	= self.queues.get( path )

			# Check the data of the node to verify that this is a new node
			if node.data is None:
				node.data	= Topic()
			slot	= node.data

			if listener is None:
				return True

			if listener in slot.subscribers:
				return False

			slot.subscribers.append(listener)
		return True

	def route(self, path:str, dest):
		""" Sets up a route to a destination queue
		Arguments
			path -- Route path
			dest -- Destination path
		"""
		with self.lock:
			if path in self.routes:
				return

			if self.queues.exists(path):
				return

			self.routes[path]	= dest
		return

	def unroute(self, path:str):
		""" Unroutes a from a route path
		Arguments
			path -- Route path
		"""
		with self.lock:
			self.routes.pop( path, None )
		return

	def unsubscribe(self, path:str, listener):
		""" Unsubscribes a listener from a queue
		Arguments
			path -- Path of the queue
			listener -- Listener object to detach subscription
		"""
		if self.queues.exists(path) == False:
			return

		slot = self.__get_slot( path )
		if slot is None:
			return

		slot.subscribers.remove(listener)
		return

	def clear(self, path:str):
		""" Purges all messages from a queue
		Arguments
			path -- Path of the queue
		"""
		slot = self.__get_slot( path )
		if slot is None:
			return

		with slot.queue.mutex:
			slot.queue.queue.clear()
		return

	def pop(self, path:str):
		""" Pops the next available message from a queue, None if empty
		Arguments
			path -- Path of the queue
		"""
		slot = self.__get_slot( path )
		if slot is None:
			return None

		try:
			return slot.queue.get_nowait()
		except queue.Empty:
			return None

	def publish(self, msg:str, key, arg):
		""" Publishes a viewer event through the publisher, or straight to /IPC without one
		Arguments
			msg -- Event name, e.g. vessel.move
			key -- Identity of the sender; a later event with the same key replaces it
			arg -- Event argument
		"""
		if self.publisher is None:
			self.fanout( self.bridge, msg, [arg] )
			if msg in self.bridge_only:
				return True
			return self.push( self.ipc, msg, None, [arg] )

		self.publisher.post( msg, key, arg )
		return True

	def create(self, path:str, maxsize:int=0):
		""" Creates a queue, bounded when maxsize > 0; an existing queue is left as it is
		Arguments
			path -- Path of the queue
			maxsize -- Bound on queued messages, dropping the oldest when full
		"""
		with self.lock:
			node	= self.queues.get( path )
			if node.data is None:
				node.data	= Topic( maxsize )
		return node.data

	def remove(self, path:str):
		""" Removes a queue and the queues under it
		Arguments
			path -- Path of the queue
		"""
		with self.lock:
			if self.queues.find(path) is None:
				return False
			self.queues.remove( path )
		return True

	def has_children(self, path:str):
		""" Checks if any queue exists directly under a path, e.g. a bridge client under /Bridge
		Arguments
			path -- Parent path
		"""
		with self.lock:
			node	= self.queues.find(path)
			return node is not None and len(node.children) > 0

	def fanout(self, path:str, msg:str, arg=None):
		""" Pushes a copy of a message to every queue directly under a path
		Arguments
			path -- Parent path, e.g. /Bridge
			msg -- Message to push
			arg -- Argument to the message
		"""
		with self.lock:
			node	= self.queues.find(path)
			if node is None:
				return 0

			slots	= [ child.data for child in node.children if child.data is not None ]
			for slot in slots:
				slot.queue.put( Event(None, msg, arg) )
		return len(slots)

	def push(self, path:str, msg:str, ctxt:Context=None, arg=None, depth=1):
		""" Pushs a message to a queue
		Arguments
			path -- Path of the queue
			msg -- Message to push
			ctxt -- Context argumen
			arg -- Argument to the message
			depth -- Number of de-references on routes
		"""
		if depth == 1:
			slot = self.__get_slot( path )
			if slot is None:
				return False

			evt = Event(ctxt, msg, arg)
			slot.queue.put(evt)
			return True

		with self.lock:
			node = self.queues.find(path)
		if node is None:
			return False

		evt = Event(ctxt, msg, arg)

		node.traverse( MessageQueue.__push_recursive, evt, depth )
		return True


	@staticmethod
	def __push_recursive(evt, node:TreeNode ):
		""" Pushes messages into a queue slot
		Arguments
			evt -- Event data
			node -- Node to push data to
		"""
		slot:Topic = node.data
		if slot is not None:
			slot.queue.put(evt)

		return ErrorCode.ERROR_CONTINUE

	def empty(self, path:str):
		""" Checks if a queue is empty
		Arguments
			path -- Path of the queue
		"""
		slot:Topic = self.__get_slot( path )
		if slot is None:
			return True

		return slot.queue.empty()

	def exists(self, path:str):
		""" Checks if a queue exists
		Arguments
			path -- Path of the queue
		"""
		slot = self.__get_slot( path )
		if slot is None:
			return False

		return True

	def count(self, path:str):
		""" Returns the number of messages pending in a queue
		Arguments
			path -- Path of the queue
		"""
		slot:Topic = self.__get_slot( path )
		if slot is None:
			return 0

		return slot.queue.qsize()

	def info(self, path:str):
		""" Returns properties of a queue
		Arguments
			path -- Path of the queue
		"""
		slot:Topic = self.__get_slot( path )
		if slot is None:
			return {}

		return {
			"count":slot.queue.qsize()
			}


	def find(self, spec:str):
		""" Locates a set of queues with a property
		Arguments
			spec -- Property description
		"""
		result = list()

		if fnmatch.fnmatch(self.echo, spec):
			result.append(self.echo)

		node = self.queues.find(path)
		if node is not None:
			node.traverse_child( MessageQueue.__find_node, (result, spec) )

		for path in self.routes.keys():
			if fnmatch.fnmatch(path, spec):
				result.append(path)

		return result

	@staticmethod
	def __find_node(self, ctxt, node:TreeNode ):
		""" Finds a node
		Arguments
			ctxt -- Context argumen
			node -- Node to process
		"""
		result:list	= ctxt[0]
		spec		= ctxt[1]
		path		= node.path

		if fnmatch.fnmatch(path, spec):
			result.append(path)
		return ErrorCode.ERROR_CONTINUE

	def dump(self, prefix:str):
		""" Dumps a list of all queues with a particular prefix
		Arguments
			prefix -- Prefix path to search for
		"""
		if (prefix is None) or (len(prefix) == 0):
			return self.__dump_all()


		result = []

		if self.echo.startswith(prefix):
			result.append(self.echo)

		node = self.queues.find(prefix)
		if node is not None:
			node.traverse( MessageQueue.__dump_node, (result) )

		topics	= self.queues.dump()
		for k in topics:
			if k.startswith(prefix):
				result.append(k)

		return result

	@staticmethod
	def __dump_node(self, ctxt, node:TreeNode ):
		""" Adds a node to the dump list
		Arguments
			ctxt -- Context argumen
			node -- Node to process
		"""
		result:list	= ctxt[0]
		result.append( node.path )
		return ErrorCode.ERROR_CONTINUE

	def __dump_all(self):
		""" Dumps all the nodes in the queue
		"""
		result	= self.queues.dump()
		result.append(self.echo)
		return result

	def __get_slot(self, path:str, depth=2):
		""" Returns the queue slot (internal data structure)
		Arguments
			path -- Path of the queue
			depth -- Number of de-references on routes
		"""
		if depth <= 0:
			return None

		if path == self.echo:
			return self.loopback

		if path == self.ipc:
			return self.ipcq

		node = self.get_node( path, depth )
		if node is not None:
			return node.data

		return None


	@staticmethod
	def __pump_node(ctxt:PumpCtxt, node:TreeNode ):
		""" Pumps messages in a queue node
		Arguments
			ctxt -- Context argumen
			node -- Node to process
		"""
		if node.data is None:
			return ErrorCode.ERROR_CONTINUE

		throttle_rate	= ctxt.throttle_rate
		slot:Topic 		= node.data

		#if slot.queue.empty() == False:
		#	print( f'Pumping {slot.queue.qsize()} messages from {node.path}' )
			
		while True:
			try:
				if slot.queue.empty():
					break
				
				evt = slot.queue.get_nowait()
			except queue.Empty:
				break

			for s in slot.subscribers:
				s.notify( evt.ctxt, evt.msg, evt.arg )
				ctxt.processed	= ctxt.processed+1
				if ctxt.processed > ctxt.throttle_rate:
					return ErrorCode.ERROR_CONTINUE

		return ErrorCode.ERROR_CONTINUE

if __name__ == "__main__":
	test = MessageQueue()
	test.push("/TestTopic", "Hello World")

	print( f'Size: {test.count("/TestTopic")}' )
	for n in range(0,5):
		print( f'Msg: {test.pop("/TestTopic")}' )


