#!/usr/bin/python
# Filename: ObjectManager.py
# Description: Inplementation of the COS kernel object manager

from cos.core.utilities.Tree import Tree, TreeNode
from cos.core.utilities.Errors import ErrorCode
from enum import Enum
import threading

class ObjectType(Enum):
	TYPE_NULL_OBJECT				= 0x00000000,

	TYPE_ACCESS_TOKEN				= 0x00000010, # The access rights for an object.
	TYPE_ADAPTER					= 0x00010020, #
	TYPE_CALLBACK_FUNC				= 0x00000030, #
	TYPE_CONTROLLER					= 0x00010050, #
	TYPE_DEBUG_OBJECT				= 0x00000060, #
	TYPE_DEVICE						= 0x00010080, #
	TYPE_DIRECTORY					= 0x00040090, #
	TYPE_DRIVER						= 0x010100A0, #
	TYPE_EVENT						= 0x000200B0, # An object which encapsulates some information= 0x00000000, to be used for notifying processes of something.
	TYPE_EVENT_PAIR					= 0x000200C0, #
	TYPE_FILE						= 0x000100D0, # An open file or an I/O device.
	TYPE_FILE_SYSTEM				= 0x000100E0, #
	TYPE_FILTER_COMMUNICATION_PORT	= 0x00121000, #
	TYPE_FILTER_CONNECTION_PORT		= 0x00121010, #
	TYPE_IO_COMPLETION_PORT			= 0x00111020, #
	TYPE_JOB						= 0x00081030, # A collection of processes.
	TYPE_KEY						= 0x00001040, # A registry key.
	TYPE_KEYED_EVENT				= 0x00021050, #
	TYPE_MEMORY_MAP					= 0x00001055, # File mapping object	A region of memory mapped to a file.
	TYPE_MESSAGE_QUEUE				= 0x00001061, # Message queue handle.
	TYPE_MESSAGE_QUEUE_TOPIC		= 0x00001062, # Message queue topic.
	TYPE_MUTEX						= 0x00021070, # Objects which serialize access to other resources.
	TYPE_PORT						= 0x00121080, # A handle to an I/O port
	TYPE_PROCESS					= 0x00081090, # A collection of executable threads along with virtual addressing and control information.
	TYPE_PROFILE					= 0x000810A0, #
	TYPE_SECTION					= 0x000810B0, # A handle to a critical section
	TYPE_SEMAPHORE					= 0x000210C0, # Objects which serialize access to other resources.
	TYPE_SYMBOLIC_LINK				= 0x000410D0, # A reference to other objects= 0x00000000, via which the referred object can be used.
	TYPE_THREAD						= 0x000810E0, # An entity containing code in execution= 0x00000000, inside a process.
	TYPE_TIMER						= 0x00022018, # An objects which notifies processes at fixed intervals.
	TYPE_TOKEN						= 0x00082018, #
	TYPE_TYPE						= 0x00042020, #
	TYPE_WAITABLE_PORT				= 0x00022030, #


	# Non-standard objects
	TYPE_SERVICE_OBJECT				= 0x02102061, # An object programmable via IPC/RPC
	TYPE_SERVICE_ADDRESS			= 0x00102062, # An string address reference
	TYPE_OPAQUE_OBJECT				= 0x00000001, # An object handle, unknown to the kernel

	TYPE_ANY_OBJECT_TYPE			= 0x0FFFFFFF,
	TYPE_INVALID_OBJECT				= 0xFFFFFFFF

class ObjectQuery:
	def __init__(self, text):
		""" Constructor
		Arguments
			text -- #TODO
		"""
		self.text	= text
		self.match	= None
		return

class ObjectNode(TreeNode):
	def __init__(self, name:str=None, parent=None, type=ObjectType.TYPE_NULL_OBJECT, ref=None):
		""" Constructor
		Arguments
			name -- Name of the object
			parent -- #TODO
			type -- Type of the object
			ref -- #TODO
		"""
		TreeNode.__init__(self, name, parent)
		self.type	= type
		self.ref	= ref
		return

	def __del__(self):
		""" #TODO: __del__
		"""
		self.ref is None
		return

	@property
	def handle(self):
		""" #TODO: handle
		"""
		return self.ref

	def construct( self, name:str=None, parent=None ):
		""" #TODO:
		Arguments
				name=None -- #TODO
			parent=None -- #TODO
		"""
		return ObjectNode( name, parent, ObjectType.TYPE_DIRECTORY )

class ObjectTree(Tree):
	def __init__(self):
		""" Constructor
		"""
		Tree.__init__(self, ObjectNode())
		return

	def construct( self, name=None, parent=None ):
		""" #TODO:
		Arguments
				name=None -- #TODO
			parent=None -- #TODO
		"""
		return ObjectNode( name, parent, ObjectType.TYPE_DIRECTORY )

class ObjectManager:
	def __init__(self):
		""" Constructor
		"""
		self.lock	= threading.Lock()
		self.ot		= ObjectTree()
		return

	def dump(self):
		""" #TODO: dump
		"""
		return self.ot.dump()

	def register( self, path:str, name:str, obj:any, type:ObjectType=ObjectType.TYPE_SERVICE_OBJECT ):
		""" #TODO: register
		Arguments
			path -- #TODO
			name -- Name of the object
			obj -- #TODO
			type -- Type of the object
		"""
		parent	= self.ot.get( path )
		node	= ObjectNode( name, parent, type, obj )
		with self.lock: return parent.add( node )

	def unregister( self, path:str, name:str ):
		""" #TODO: unregister
		Arguments
			path -- #TODO
			name -- Name of the object
		"""
		node	= self.ot.get( path )
		if node is None:
			return False

		with self.lock: return node.parent.remove(node)

	def link( self, path:str, name:str, target:str ):
		""" #TODO: link
		Arguments
			path -- #TODO
			name -- Name of the object
			target -- #TODO
		"""
		return self.register( path, name, target, ObjectType.TYPE_SYMBOLIC_LINK )

	def get( self, path:str, deref=8, flags=0 ):
		""" #TODO: get
		Arguments
			path -- #TODO
			deref -- #TODO
			flags -- #TODO
		"""
		with self.lock:
			node	= self.ot.find( path )
			node 	= self.__resolve( node, deref, flags )
			if node is None:
				return None

			return node.handle

	def get_node( self, path:str, deref=8, flags=0 ):
		""" #TODO: get_node
		Arguments
			path -- #TODO
			deref -- #TODO
			flags -- #TODO
		"""
		with self.lock:
			node	= self.ot.find( path )
			return self.__resolve( node, deref, flags )


	def exists(self, path:str):
		""" #TODO: exists
		Arguments
			path -- #TODO
		"""
		with self.lock: return (self.ot.find(path) is not None)

	def traverse(self, path:str, fn, ctxt=None, depth=1 ):
		""" #TODO: traverse
		Arguments
			path -- #TODO
			fn -- #TODO
			ctxt -- Simulation context
			depth -- #TODO
		"""
		with self.lock:
			node	= self.ot.find( path )
			if node is None:
				return ErrorCode.ERROR_PATH_NOT_FOUND

			result = fn( ctxt, node )
			if result == ErrorCode.S_OK:
				# Return immediately
				return ErrorCode.S_OK

			return node.traverse( fn, ctxt, depth )

	def clear(self, path:str, fn=None, ctxt=None):
		""" #TODO: clear
		Arguments
			path -- #TODO
			fn -- #TODO
			ctxt -- Simulation context
		"""
		with self.lock:
			node	= self.ot.find( path )
			if node is None:
				return None

			node.clear()
			return

	def dump(self):
		""" #TODO: dump
		"""
		result = []
		self.ot.traverse( self.__get_all_node, result, 0xFFFF )
		return result

	def get_all(self, path:str):
		""" #TODO: get_all
		Arguments
			path -- #TODO
		"""
		result = []
		self.traverse( path, self.__get_all_object, result, 0xFFFF )
		return result

	def find(self, path:str, id:str):
		""" Finds a decendant node with a matching name under a path
		Arguments
			path -- Root path
			id -- Name of the child node
		"""
		query = ObjectQuery(id)

		self.traverse(path, self.__match_node_by_name, query, 0xFFFF )
		return query.match

	@staticmethod
	def __get_all_node(result, node:ObjectNode):
		""" #TODO: __get_all_node
		Arguments
			result -- #TODO
			node -- #TODO
		"""
		if node.type != ObjectType.TYPE_SERVICE_OBJECT:
			return ErrorCode.ERROR_CONTINUE

		if node.handle is None:
			return ErrorCode.ERROR_CONTINUE

		# Append the object to the list
		result.append(node.get_path())
		return ErrorCode.ERROR_CONTINUE

	@staticmethod
	def __get_all_object(result, node:ObjectNode):
		""" #TODO: __get_all_object
		Arguments
			result -- #TODO
			node -- #TODO
		"""
		if node.type != ObjectType.TYPE_SERVICE_OBJECT:
			return ErrorCode.ERROR_CONTINUE

		if node.handle is None:
			return ErrorCode.ERROR_CONTINUE

		# Append the object to the list
		result.append(node.handle)
		return ErrorCode.ERROR_CONTINUE

	def __resolve(self, node:ObjectNode, depth=64, flags=0 ):
		""" #TODO: __resolve
		Arguments
			node -- #TODO
			depth -- #TODO
			flags -- #TODO
		"""
		if node is None:
			return None

		if node.type != ObjectType.TYPE_SYMBOLIC_LINK:
			return node

		for i in range(0, depth):
			if node.type != ObjectType.TYPE_SYMBOLIC_LINK:
				return node

			node	= self.ot.find( node.handle );
			if node is None:
				return None

		return None


	@staticmethod
	def __match_node_by_name(result:ObjectQuery, node:ObjectNode):
		""" Finds a matching vessel with a name
		Arguments
			result -- #TODO
			node -- #TODO
		"""
		if node.type != ObjectType.TYPE_SERVICE_OBJECT:
			return ErrorCode.ERROR_CONTINUE

		if node.name != result.text:
			return ErrorCode.ERROR_CONTINUE

		# Return the match immediately
		result.match	= node.handle
		return ErrorCode.S_OK

if __name__ == "__main__":
	test = ObjectManager()


