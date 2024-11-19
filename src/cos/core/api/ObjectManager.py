# Generated code

from cos.core.network.ORPCProxy import ORPCProxy


class ObjectManager(ORPCProxy):
	def __init__(self,arg=None):
		""" Constructor
		Arguments
			arg -- Unused
		"""
		ORPCProxy.__init__(self,arg)
		return

	def create(self, path, name, type, config ):
		""" Creates an object
		Arguments
			path -- Path of the object
			name -- Name of the object
			type -- Type of the object
			config -- Configuration attributes
		"""
		args={
			 'path':path,
			 'name':name,
			 'type':type,
			 'config':config
			}
		ORPCProxy.invoke(self,'create', args)
		return

	def register(self, path, name, type, objref, config ):
		""" Registers an object
		Arguments
			path -- Path of the object
			name -- Name of the object
			type -- Type of the object
			objref -- Reference to an object
			config -- Configuration attributes
		"""
		args={
			 'path':path,
			 'name':name,
			 'type':type,
			 'objref':objref,
			 'config':config
			}
		ORPCProxy.invoke(self,'register', args)
		return

	def link(self, path, name, target, config ):
		""" Creates a symbolic link to an object
		Arguments
			path -- Path of the object
			name -- Name of the object
			target -- Target object path
			config -- Configuration attributes
		"""
		args={
			 'path':path,
			 'name':name,
			 'target':target,
			 'config':config
			}
		ORPCProxy.invoke(self,'link', args)
		return

	def unregister(self, path, config ):
		""" Unregisters an object or link
		Arguments
			path -- Path of the object
			config -- Configuration attributes
		"""
		args={
			 'path':path,
			 'config':config
			}
		ORPCProxy.invoke(self,'unregister', args)
		return

	def get(self, path, depth, config ):
		""" Returns a reference to the object
		Arguments
			path -- Path of the object
			depth -- Recursive depth to search for (for symbolic links)
			config -- Configuration attributes
		"""
		args={
			 'path':path,
			 'depth':depth,
			 'config':config
			}
		return ORPCProxy.invoke(self,'get', args)

	def find(self, path, depth, config ):
		""" Finds an object
		Arguments
			path -- Path of the object
			depth -- Recursive depth to search for (for symbolic links)
			config -- Configuration attributes
		"""
		args={
			 'path':path,
			 'depth':depth,
			 'config':config
			}
		return ORPCProxy.invoke(self,'find', args)

	def exists(self, path, config ):
		""" Checks if an object exists exists
		Arguments
			path -- Path of the object
			config -- Configuration attributes
		"""
		args={
			 'path':path,
			 'config':config
			}
		return int(ORPCProxy.invoke(self,'exists', args))




