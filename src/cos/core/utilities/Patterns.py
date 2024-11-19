#!/usr/bin/python
# Filename: Patterns.py
# Description: A collection of generic design patterns, mostly from the 'Gang of Four' book.


class GenericManager:
	def __init__(self):
		""" Constructor
		Arguments
			"""
		self.container	= []
		return

	def add(self, obj):
		""" Adds an object to the collection
		Arguments
			obj -- Object to add to the collection
		"""
		if obj in self.container:
			return

		self.container.append( obj )
		return

	def remove(self, obj):
		""" Removes an object from the collection
		Arguments
			obj -- Object to remove from the collection
		"""
		if obj not in self.container:
			return False

		self.container.remove( obj )
		return True

	def find(self, obj):
		""" Finds a matching object in the collection
		Arguments
			obj -- Object to match
		"""
		if obj in self.container:
			return True

		return False

	def size(self):
		""" Returns the number of objects in the collection
		Arguments
			"""
		return len(self.container)

	def clear(self):
		""" Removes all objects from the collection
		Arguments
			"""
		self.container	= []
		return

	def for_each(self, fn, ctxt=None):
		""" Iterates through each object in the collection
		Arguments
			fn -- Callback function called for each object
			ctxt=None -- Context argument passed to each function
		"""
		for obj in self.container:
			fn( obj, ctxt )

		return

	def for_each_first(self, fn, ctxt=None):
		""" Iterates through each object in the collection for the first successful call
		Arguments
			fn -- Callback function called for each object
			ctxt=None -- Context argument passed to each function
		"""
		for obj in self.container:
			if fn( obj, ctxt ) == True:
				return
		return

class Manager:
	def __init__(self):
		""" Constructor
		Arguments
			"""
		self.container	= {}
		return

	def add(self, key, obj):
		""" Adds an object to the collection
		Arguments
			key -- Key to identify the object
			obj -- Object to add
		"""
		if self.container.has_key(key) == True:
			return False

		self.container[key]	= obj
		return True

	def remove(self, key):
		""" Removes an object from the collection
		Arguments
			key -- Key to identify the object to remove
		"""
		if self.container.has_key(key) == False:
			del self.container[key]
			return True

		return False

	def get(self, key):
		""" Returns the object identified by a key
		Arguments
			key -- Key to match
		"""
		return self.container.get(key)

	def set(self, key, obj):
		""" Adds an object to the collection
		Arguments
			key -- Key to identify the object
			obj -- Object to add
		"""
		self.container[key]	= obj
		return

	def find_id(self, key):
		""" Checks if an object with a key exists. Returns True if found, else False
		Arguments
			key -- Key to match
		"""
		return self.container.has_key(key)

	def find_object_id(self, obj):
		""" Finds the key of an object
		Arguments
			obj -- Object to match
		"""
		for k, v in self.container.items():
			if v == obj:
				return k
		return None

	def size(self):
		""" Number of objects in the collection
		Arguments
			"""
		return len(self.container)

	def clear(self):
		""" Removes all objects from the collection
		Arguments
			"""
		self.container.clear()
		return

	def for_each(self, fn, ctxt=None):
		""" Iterates through each entity in the collection
		Arguments
			fn -- Callback function to call for each instance
			ctxt=None -- Context argument passed to the function
		"""
		for k, v in self.container.items():
			fn( k, v, ctxt )
		return


class Composite(GenericManager):
	def __init__(self):
		""" Constructor
		Arguments
			"""
		GenericManager.__init__(self)
		return

	def add_component(self, obj):
		""" Adds a component to the composite
		Arguments
			obj -- Object to add to the collection
		"""
		GenericManager.add(self, obj)
		return

	def remove_component(self, obj):
		""" Removes an object from the collection
		Arguments
			obj -- Object to remove
		"""
		GenericManager.remove(self, obj)
		return

class Publisher(GenericManager):
	def __init__(self):
		""" Constructor
		Arguments
			"""
		GenericManager.__init__(self)
		return

	def add_observer(self, obj):
		""" Adds an observer to the list
		Arguments
			obj -- Obsever to add
		"""
		GenericManager.add(self, obj)
		return

	def remove_observer(self, obj):
		""" Removes an observer from the list
		Arguments
			obj -- Observer to remove
		"""
		GenericManager.remove(self, obj)
		return

	def notify(self, fn, ctxt=None):
		""" Notifies all obects of an event
		Arguments
			fn -- Function object to callback to handle the notification
			ctxt=None -- Context argument passed to the function
		"""
		return GenericManager.for_each( self, fn, ctxt )

class Flyweight(Manager):
	def __init__(self):
		""" Constructor
		Arguments
			"""
		Manager.__init__(self)
		return


	def get_flyweight(self, key, ctxt=None):
		""" Returns a flyweight object for a given key
		Arguments
			key -- Key of the object to be retrieved
			ctxt=None -- Context argument passed to construct an object, if necessary.
		"""
		obj	= Manager.Get( self, key )

		if obj == None:
			obj	= self.create_flyweight( key, ctxt )

			if obj is not None:
				self.add_flyweight( key, obj )

		return obj

	def add_flyweight( self, key, obj ):
		""" Internal function to add the flyweight obect
		Arguments
			key -- Key identifying the object
			obj -- Object to add
		"""
		return Manager.add( self, key, obj )

	def remove_flyweight( self, key ):
		""" Removes a flyweight object matching a key
		Arguments
			key -- Key to search for
		"""
		return Manager.remove( self, key )

	def create_flyweight( self, key, ctxt ):
		""" Overridable function to create a new objects for a key
		Arguments
			key -- Key of the object
			ctxt -- Context argument passed to the constructor
		"""
		raise Exception( "Override create_flyweight." )

class ChainOfResponsibility:
	def __init__(self):
		""" Constructor
		Arguments
			"""
		self.next	= None
		return

	def run(self):
		""" Runs the chain (or pipeline)
		Arguments
			"""
		self.execute()
		if self.next is not None:
			self.next.run()
		return

	def set_next( self, nextcmd ):
		""" Adds a new command to the chain
		Arguments
			nextcmd -- The command following this command
		"""
		self.next = nextcmd
		return nextcmd

	def get_next(self):
		""" Returns the next command.
		Arguments
			"""
		return self.next

	def execute(self):
		""" Overridable function that is the concrete execution of the command
		Arguments
			"""
		raise Exception( "Override Execute." )


	@staticmethod
	def generate(cmdseq):
		""" Generates a chain of respoinsibility pipeline from an array of commands by linking them.
		Arguments
			cmdseq -- An array of commands to link into a pipeline
		"""
		pipeline	= None

		# Construct the pipeline
		last	= None
		for cmd in cmdseq:
			if pipeline == None:
				# If this is the front of the pipeline,
				# simply add the first command
				pipeline	= cmd
			else:
				# If this is not the front of the pipeline
				# append the current command to the last command
				last.SetNext( cmd )

			last			= cmd

		return pipeline




class ProductCreator:
	def __init__( self, spec, ctor ):
		""" Constructor
		Arguments
			spec -- Product specification
			ctor -- Product factory
		"""
		self.ctor	= ctor
		self.spec	= spec
		return

	def create( self, ctxt ):
		""" Creates a product
		Arguments
			spec -- Product specification
			ctxt -- Context argument passed to the factory
		"""
		return self.ctor( self.spec, ctxt )


class ProductRegistry(Manager):
	def __init__(self):
		""" Constructor
			"""
		Manager.__init__(self)
		return

	def add( self, spec, creator ):
		""" Adds a product specification
		Arguments
			spec -- Product specification
			creator -- Creator class
		"""
		return Manager.add(self, spec, creator)

	def remove( self, spec ):
		""" Removes a product specification
		Arguments
			spec -- Product specification
		"""
		return Manager.remove(self, spec)

	def substitute( self, spec, creator )	:
		""" Substitutes a product specification
		Arguments
			spec -- Product specification
			creator -- Creator class
		"""
		self.container[spec]	= creator
		return True

	def lookup( self, spec ):
		""" Finds a product specification
		Arguments
			spec -- Product specification
		"""
		if Manager.find_id(self, spec) == False:
			return None

		return Manager.get(self, spec)


class ProductTrader:
	def __init__(self):
		""" Constructor
		"""
		self.registry	= ProductRegistry()
		return

	def create( self, spec, ctxt ):
		""" Creates a product
		Arguments
			spec -- Product specification
			ctxt -- Creation context
		"""
		creator	= self.registry.lookup( spec )
		if creator == None:
			return None

		return creator.create( ctxt )

	def lookup( self, spec ):
		""" Finds a product specification
		Arguments
			spec -- Product specification
		"""
		return self.registry.lookup( spec )

	def add( self, spec, creator ):
		""" Adds a product specification
		Arguments
			spec -- Product specification
			creator -- Creator class
		"""
		return self.registry.add( spec, ProductCreator(spec, creator) )

	def substitute( self, spec, creator ):
		""" Substitutes a product specification
		Arguments
			spec -- Product specification
			creator -- Creator class
		"""
		return self.registry.substitute( spec, ProductCreator(spec, creator) )

	def remove( self, spec ):
		""" Removes a product specification
		Arguments
			spec -- Product specification
		"""
		return self.registry.remove( spec )



