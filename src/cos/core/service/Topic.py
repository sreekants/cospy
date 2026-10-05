#!/usr/bin/python
# Source File: Topic.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation

import threading, time, uuid

DEFAULT_QUEUE_SIZE	= 256		# Events held per bridge client before the oldest is dropped
DEFAULT_IDLE_EXPIRY	= 30.0		# Wall seconds a bridge client may go without draining

def plain(value):
	""" Converts a payload to lists, dicts and scalars that JSON and msgpack can encode
	Arguments
		value -- Payload
	"""
	if value is None or isinstance(value, (bool, int, float, str)):
		return value
	if isinstance(value, dict):
		return { str(k): plain(v) for k, v in value.items() }
	if isinstance(value, (list, tuple, set)):
		return [ plain(v) for v in value ]
	if hasattr(value, 'tolist'):
		return plain( value.tolist() )		# numpy arrays and scalars
	if hasattr(value, 'isoformat'):
		return value.isoformat()
	return str(value)

class Topic(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		self.ipc		= Simulation.instance().ipc
		self.clients	= {}		# Bridge client id -> wall time of its last drain
		self.lock		= threading.Lock()
		self.queue_size	= DEFAULT_QUEUE_SIZE
		self.idle_expiry	= DEFAULT_IDLE_EXPIRY
		return

	def assert_path(self, path):
		""" Raises if a topic does not exist
		Arguments
			path -- Path of the topic
		"""
		if self.ipc.exists(path) == False:
			raise RuntimeError( f'Topic {path} does not exist.' )
		return path

	def pop( self, path ):
		""" Pops the next event from a topic
		Arguments
			path -- Path of the topic
		Returns
			{"m": message, "d": payload}, or None when the topic is empty
		"""
		self.assert_path( path )
		evt	= self.ipc.pop(path)
		if evt == None:
			return None

		return { "m": evt.msg, "d": plain(evt.arg) }

	def drain( self, path, max ):
		""" Pops up to max events from a topic, oldest first
		Arguments
			path -- Path of the topic
			max -- Maximum number of events to return
		Returns
			{"events": [{"m", "d"}, ...], "dropped": events lost to the queue bound since the last drain}
		"""
		client	= self.__client_of( path )
		if client is not None:
			with self.lock:
				if client not in self.clients:
					raise RuntimeError( f'Bridge client {client} expired; subscribe again.' )
				self.clients[client]	= time.monotonic()

		self.assert_path( path )
		events	= []
		for n in range(0, int(max)):
			evt	= self.ipc.pop(path)
			if evt is None:
				break
			events.append( { "m": evt.msg, "d": plain(evt.arg) } )

		slot	= self.ipc.create( path )
		dropped	= slot.queue.take_dropped() if hasattr(slot.queue, 'take_dropped') else 0
		return { "events": events, "dropped": dropped }

	def subscribe( self ):
		""" Creates a bridge client queue under /Bridge that receives every published batch
		Returns
			{"client": id, "path": queue path, "idle_expiry": seconds}
		"""
		self.expire()

		client	= uuid.uuid4().hex[:12]
		path	= f'{self.ipc.bridge}/{client}'
		self.ipc.create( path, self.queue_size )
		with self.lock:
			self.clients[client]	= time.monotonic()

		return { "client": client, "path": path, "idle_expiry": self.idle_expiry }

	def unsubscribe( self, client ):
		""" Removes a bridge client's queue
		Arguments
			client -- Client id returned by subscribe
		"""
		with self.lock:
			self.clients.pop( client, None )
		return self.ipc.remove( f'{self.ipc.bridge}/{client}' )

	def expire( self ):
		""" Removes bridge client queues not drained within the idle expiry
		Returns
			Number of queues removed
		"""
		now		= time.monotonic()
		with self.lock:
			stale	= [ c for c, t in self.clients.items() if now - t > self.idle_expiry ]
			for c in stale:
				self.clients.pop( c, None )

		for c in stale:
			self.ipc.remove( f'{self.ipc.bridge}/{c}' )
		return len(stale)

	def __client_of(self, path):
		""" Returns the bridge client id of a queue path, or None for other topics
		Arguments
			path -- Path of the topic
		"""
		prefix	= self.ipc.bridge + '/'
		if path.startswith(prefix):
			return path[len(prefix):]
		return None

	def push( self, path, msg ):
		""" Pushes a message to a topic
		Arguments
			path -- Path of the topic
			msg -- Message
		"""
		self.assert_path( path )
		self.ipc.push(path, msg)
		return

	def find( self, path ):
		""" Finds topics matching a pattern
		Arguments
			path -- Path pattern
		"""
		return self.ipc.find(path)

	def info( self, path ):
		""" Describes a topic
		Arguments
			path -- Path of the topic
		"""
		return self.ipc.info(path)

	def list( self, path ):
		""" Lists the topics under a path
		Arguments
			path -- Path prefix
		"""
		return self.ipc.dump(path)

	def type( self, path ):
		""" Returns the type of a topic
		Arguments
			path -- Path of the topic
		"""
		self.assert_path( path )
		return f'{path}:INFO'

	def route( self, src, dest ):
		""" Routes one topic path to another
		Arguments
			src -- Route path
			dest -- Destination path
		"""
		return self.ipc.route( src, dest )

	def unroute( self, path ):
		""" Removes a route
		Arguments
			path -- Route path
		"""
		return self.ipc.unroute( path )

