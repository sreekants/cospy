#!/usr/bin/python
# Filename: Tree.py
# Description: Generic implementation of a tree data structure

from cos.core.utilities.Errors import ErrorCode
import fnmatch

class TreeFindCtxt:
	def __init__(self, name:str, flag=0):
		""" Tree search context
		Arguments
			name -- Name of the tree
			flag -- Flags for the search
		"""
		self.name	= name
		self.flag	= flag
		self.result	= None
		return

class TreeNode:
	def __init__(self, name:str=None, parent=None, data=None):
		""" Constructor
		Arguments
			name=None -- Name of the node
			parent=None -- Parent node
			data=None -- Data associated with the node
		"""
		self._name	= name
		self._data	= data
		self._parent	= parent
		self.children	= []
		return

	def construct( self, name:str=None, parent=None ):
		""" Constructs the object
		Arguments
			name=None -- Name of the node
			parent=None -- Parent of the node
		"""
		return TreeNode( name, parent )

	def add( self, node ):
		""" Adds a new child node to the tree
		Arguments
			node -- Node to add
		"""
		if self.__can_add_node(node) == False:
			return None

		self.children.append( node )
		node._parent	= self
		return node

	def __can_add_node( self, node ):
		""" Overridable called to check if a node can be added
		Arguments
			node -- Node to validate
		"""

		# If this is an item that is not initialized,
		# the name string points to the global null-string.
		# We allow this special case to pass through. This is useful
		# when a node is retrieved from an archive and the
		# name is not yet known, while the node is in a
		# transitive state of construction.
		if len(node.name) > 0:
			if self.child(node.name):
				# Ensure that there are no duplicates
				raise Exception( f"A node with name {node.name} already exists." )

		return True

	def remove( self, node ):
		""" Removes a child node
		Arguments
			node -- Node to remove
		"""
		self.children.remove( node )
		node.parent	= None
		return True


	def move_to( self, target ):
		""" Move the children from one node to another.
		Arguments
			target -- Target node
		"""
		for node in self.children:
			node.parent	= target

		target.children.extend( self.children )
		self.children	= []
		return

	def clear( self ):
		""" Deletes all child nodes
		"""
		for node in self.children:
			self.destroy( node )

		self.children	= []
		return

	def destroy( self, node ):
		""" Destroys a node (does not remove it from the list)
		Arguments
			node -- Node to destroy
		"""
		if self.__can_destroy(node) == False:
			return

		node.parent	= None
		return

	def __can_destroy( self, node ):
		""" Overridable function used to control deletion of a tree node
		Arguments
			node -- Node to validate
		"""
		return (node is not None)

	def get( self, path:str, sep='/' ):
		""" Gets a node using a path notation. (New nodes are created if none exists).
		Arguments
			path -- Path of the node
			sep='/' -- Path separator
		"""
		path_part	= ''

		if path[0] != sep:
			raise Exception( f"Path{path} not found." )

		node		= self
		last_node	= self
		ndx			= 0

		while True:
			ndx		+=1

			if path[ndx] == '\0':
				break

			ndxSep	= path.find( sep, ndx )

			if ndxSep == -1:
				path_part	= path[ndx:]
			else:
				path_part	= path[ndx:ndxSep]

			ndx			= ndxSep
			last_node	= node
			node		= node.child( path_part )

			# Create a node if one does not exit
			if node==None:
				new_node	= self.construct( path_part )
				node		= last_node.add( new_node )


			if ndxSep == -1:
				break

		return node


	def find( self, path:str, sep='/' ):
		""" Returns a node associated with a gven path
		Arguments
			path -- Relative path of the node
			sep='/' -- Path separator
		"""

		if path[0] != sep:
			raise Exception( "Path not found." )

		node		= self
		last_node	= self
		ndx			= 0

		while True:
			ndx		+=1

			if path[ndx] == '\0':
				break

			ndxSep	= path.find( sep, ndx )

			if ndxSep == -1:
				path_part	= path[ndx:]
			else:
				path_part	= path[ndx:ndxSep]

			ndx			= ndxSep
			last_node	= node
			node		= node.child( path_part )

			if node is None:
				return None

			if ndxSep == -1:
				break

		return node

	def match( self, name:str, flags=0 ):
		""" Searches for the first node with a matching name
		Arguments
			name -- Name of the node
			flags=0 -- UNUSED
		"""

		ctxt		= TreeFindCtxt( name, flags )
		ctxt.result	= []
		self.traverse( TreeNode.__find_match, ctxt, 4096 )
		return ctxt.result

	@staticmethod
	def __find_match( ctxt, node ):
		""" Internal callback function to handle search for a node
		Arguments
			ctxt -- Context argument passed to the callback
			node -- Node to process
		"""
		if node.parent is None:
			return ErrorCode.ERROR_CONTINUE


		if ctxt.flag == 0:
			if node.name != ctxt.name:
				return ErrorCode.ERROR_CONTINUE
		elif ctxt.flag == 1:
			if fnmatch.fnmatch(node.name, ctxt.name) == False:
				return ErrorCode.ERROR_CONTINUE
		else:
			raise Exception( "Unsupported flag" )

		# A match is found so append it
		ctxt.result.append( node )
		return ErrorCode.ERROR_CONTINUE

	def traverse( self, fn, ctxt, maxlevel=1 ):
		""" Helper function to iterate through child nodes of a node and invoke a callback
		Arguments
			fn -- Function to call back
			ctxt -- Context argumen passed to the function
			maxleve=1 -- Maximum depth to recurse into
		"""
		if maxlevel == 0:
			return

		maxlevel	-= 1

		for node in self.children:
			result	= fn( ctxt, node )

			if result == ErrorCode.ERROR_NO_MORE_ITEMS:
				# Skip all remaining items
				return ErrorCode.ERROR_CONTINUE
			elif result == ErrorCode.ERROR_INVALID_LEVEL:
				# Skip the level for the processed node
				continue
			elif result == ErrorCode.S_OK:
				# Return immediately
				return ErrorCode.S_OK
			elif result != ErrorCode.ERROR_CONTINUE:
				return result

			if maxlevel > 0:
				result = node.traverse( fn, ctxt, maxlevel )
				if result != ErrorCode.ERROR_CONTINUE:
					# Stop further processing
					return result

		return ErrorCode.ERROR_CONTINUE

	def traverse_sibling( self, fn, ctxt ):
		""" Helper function to iterate through all the siblings of a node and invoke a callback
		Arguments
			fn -- Function to call back
			ctxt -- Context argumen passed to the function
		"""
		if self._parent is not None:
			self._parent.for_each_child( fn, ctxt )

		return

	def traverse_child( self, fn, ctxt ):
		""" Helper function to iterate through child nodes of a node and invoke a callback
		Arguments
			fn -- Function to call back
			ctxt -- Context argumen passed to the function
		"""
		for node in self.children:
			fn( ctxt, node )

		return

	def at( self, ndx:int ):
		""" Returns a child by index
		Arguments
			ndx -- Index of the child to return
		"""
		if ndx >= len(self.children):
			return None

		return self.children[ndx]

	def child( self, name:str ):
		""" Returns a child node with a matching name
		Arguments
			name -- Name of the node to search for
		"""

		for node in self.children:
			if node.name == name:
				return node

		return None

	def __getitem__(self, name:str):
		""" Returns a child node with a matching name
		Arguments
			name -- Name of the node to search for
		"""
		return self.child(name)

	@property
	def path( self ):
		""" Returns the path of the node
		"""
		return self.get_path()

	@property
	def level( self ):
		""" Returns the depth of the node
		"""
		depth		= 0
		node		= self
		parent		= node.parent

		while parent is not None:
			depth	= depth+1
			parent	= node.parent

		return depth

	def get_path( self, sep:str='/' ):
		""" Returns the path of the node
		Arguments
			sep='/' -- Path separator
		"""


		# If this is the root node return immediately
		if self._parent is None:
			return sep

		path	= None

		# Traverse to the root and construct a stack of parents
		node		= self
		parent		= node.parent

		while parent is not None:
			if path is None:
				path	= '{}{}'.format( sep, node.name )
			else:
				path	= '{}{}{}'.format( sep, node.name, path )

			node	= parent
			parent	= node.parent

		return path

	@property
	def size( self ):
		""" Returns the number of children of the node
		"""
		return len(self.children)

	@property
	def level( self ):
		""" Returns the number of parents to this node
		"""
		node	= self._parent
		level	= 0

		while node is not None:
			level	+=1
			node	= node.parent

		return level

	@property
	def parent( self ):
		""" Returns the parent of this node
		"""
		return self._parent

	@parent.setter
	def set_parent( self, parent ):
		""" Sets the parent of this node
		Arguments
			parent -- Parent node
		"""
		self._parent	= parent
		return

	@property
	def data( self ):
		""" Gets the data associated with the node
		"""
		return self._data

	@data.setter
	def data( self, data ):
		""" Sets the data associated with the node
		Arguments
			data -- Opaque data value
		"""
		self._data	= data
		return


	@property
	def name( self ):
		""" Returns the name of the node
		"""
		return self._name

	@name.setter
	def name( self, name ):
		""" Sets the name of the node
		Arguments
			name -- Name of the node
		"""
		self._name	= name
		return

class Tree:
	def __init__(self, root=None):
		""" Constructor
		Arguments
			root -- Optional root node
		"""
		if root is None:
			root	= TreeNode()

		self._root	= root
		return

	def add( self, path:str, node, sep='/' ):
		""" Adds a child node to a node a path
		Arguments
			path -- Path of the parent node
			node -- Node to attach
			sep='/' -- Path separator
		"""

		parent	= self.find( path, sep )

		if parent is None:
			raise Exception( "Cannot resolve parent node [{}].".format(path) )

		return parent.add( node )


	def remove( self, path:str, sep='/' ):
		""" Reemoves a node identifed by a path
		Arguments
			path -- Path of the node
			sep='/' -- Path separator
		"""
		node	= self.find( path, sep )

		if node==None:
			raise Exception( "Path not found." )

		parent	= node.get_parent()

		if parent is None:
			raise Exception( "Cannot remove root node." )

		return parent.remove( node )

	def match( self, name:str, wildcard=False ):
		""" Searches for a node with a matching name
		Arguments
			name -- Name of the node
			flags=0 -- UNUSED
		"""

		flag	= 1 if wildcard==True else 0
		return self._root.match( name, flag )

	def find( self, path:str, sep='/' ):
		""" Finds a node at a particular path
		Arguments
			path -- Path of the node
			sep='/' -- Path separator
		"""
		if path == sep:
			return self._root


		return self._root.find( path, sep )

	def get( self, path:str, sep='/' ):
		""" Gets a node using a path notation. (New nodes are created if none exists).
		Arguments
			path -- Path of the node
			sep='/' -- Path separator
		"""
		if path == sep:
			return self._root

		return self._root.get( path, sep )


	def traverse( self, fn, ctxt, maxdepth=4096 ):
		""" Helper function to iterate through child nodes of a node and invoke a callback
		Arguments
			fn -- Function to call back
			ctxt -- Context argumen passed to the function
			maxleve=1 -- Maximum depth to recurse into
		"""
		return self._root.traverse( fn, ctxt, maxdepth )


	def dump( self, flags=0 ):
		""" Dumps the tree to an output stream
		Arguments
			flags=0 -- Flag used to control the ouput
		"""
		result = []
		self.traverse( Tree.__append_node, result )
		return result

	@staticmethod
	def __append_node( result:list, node ):
		""" Internal callback function to handle dumping a tree node
		Arguments
			ctxt -- Context argument passed to the callback
			result -- Result list to append to
		"""
		result.append( node.get_path() )
		return ErrorCode.ERROR_CONTINUE


	@property
	def root(self):
		""" Returns the root node
		"""
		return self._root

	@root.setter
	def root( self, node ):
		""" Sets a new root node
		Arguments
			node -- new root node
		"""
		self.attach_root( node )

	def attach_root( self, node ):
		""" Attaches a new root node
		Arguments
			node -- new root node
		"""
		root				= self._root
		self._root			= node
		self._root.parent	= None
		return root

	def __str__(self):
		return '\n'.join(self.dump())



if __name__ == "__main__":
	t = Tree()
	n = t.get( '/Child1/GrandChild1.1/XXX' )
	t.get( '/Child2/GrandChild2.1/XXX2' )
	t.get( '/Child2/GrandChild2.1/Y' )
	t.get( '/Child2/GrandChild2.2' )

	print( '\n=========== Tree Dump ===========' )
	print(t)
	print( '=================================\n' )

	print( f'Path     = {n.get_path()}' )
	print( f'Parents  = {n.level}' )
	print( f'Path(Y)  = {t.match("Y")[0].path}' )
	print( f'Path(X*)  = {t.match("X*",True)[0].path}' )



