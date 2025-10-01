#!/usr/bin/python
# Filename: BootLoader.py
# Description: Implementation of the boot loader for the simulation engine

from cos.core.kernel.Configuration import Configuration
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import sys, yaml, io

class BootLoader:
	def __init__(self):
		""" Constructor
		"""
		self.module 	= 'Loader'
		self.seq		= []
		return

	def startup(self, sim, config:Configuration):
		""" Starts up the simulation
		Arguments
			sim -- Reference ot the simulation
			config -- Configuration attributes
		"""
		# Mount the boot file system
		if config.bootimage is not None:
			config.bootimage.mount()
			sim.fs	= config.bootimage

		self.init(sim, config)
		self.start(sim)

		if config.bootimage is not None:
			config.bootimage.umount()
			sim.fs	= None
		return


	def shutdown(self, sim):
		""" Shutdown the sumulation
		Arguments
			sim -- Reference ot the simulation
		"""
		self.stop(sim)
		return

	def start(self, sim):
		""" Start the simulation
		Arguments
			sim -- Reference ot the simulation
		"""
		ctxt	= Context(sim, sim, sim.ipc)

		# Start the kernel subsystems
		for inst in sim.subsystems:
			inst.on_init( ctxt, None )
			inst.on_start( ctxt, None )

		for inst, config in self.seq:
			inst.on_start( ctxt, config )

		for runlevel in range(0,5):
			for inst in sim.subsystems:
				inst.on_run( ctxt, runlevel )

			for inst, config in self.seq:
				inst.on_run( ctxt, runlevel)

		return

	def stop(self, sim):
		""" Stops the simulation
		Arguments
			sim -- Reference ot the simulation
		"""
		ctxt	= Context(sim, sim, sim.ipc)

		for runlevel in range(5,0,-1):
			for inst in sim.subsystems:
				inst.on_term( ctxt, runlevel )

			for inst, config in self.seq:
				inst.on_term( ctxt, -1*runlevel)

		for inst, config in self.seq:
			inst.on_stop( ctxt, config )

		# Stop the kernel subsystems
		for inst in sim.subsystems:
			inst.on_stop( ctxt, None )
		return

	def init(self, sim, config:Configuration):
		""" Initializes the simulation
		Arguments
			sim -- Reference ot the simulation
			config -- Configuration attributes
		"""
		for scope in ['Kernel','Faculties', 'Services']:
			faculties	= config.get_value('Simulation', scope)
			sim.log.info( self.module, f'Loading {scope}: {faculties}' )

			for type in faculties.split(','):
				self.load_section( sim, config, scope, type )
		return

	def load_section(self, sim, config:Configuration, scope:str, section:str):
		""" Loads a section of the configuration
		Arguments
			sim -- Reference ot the simulation
			config -- Configuration attributes
			scope -- Scope namespace
			section -- Section string
		"""
		sim.log.info( self.module, f'Loading {section}' )
		for key in config.get_keys(section):
			self.load_file( sim, scope, section, key, config.get_file(section, key) )
		return

	def load_file(self, sim, scope:str, section:str, type:str, file:str):
		""" Loads a simulation file
		Arguments
			sim -- Reference ot the simulation
			scope -- Scope namespace
			section -- Section string
			type -- Type of the object
			file -- File path
		"""
		sim.log.info( self.module, f'  {type}: {file}.' )
		config		= yaml.safe_load( sim.fs.read_file_as_bytes(file) )
		self.load_modules( sim, config, scope, section, type, config['packages']['modules'] )

	def load_modules(self, sim, config:Configuration, scope:str, section:str, type:str, modules):
		""" Loads all the modules in a simulation file
		Arguments
			sim -- Reference ot the simulation
			config -- Configuration attributes
			scope -- Scope namespace
			section -- Section string
			type -- Type of the object
			modules -- List of modules
		"""
		objects = {}
		if modules is None or len(modules) == 0:
			return objects

		for module in modules:
			self.__load_package( sim, config, objects, module )

		return objects

	@staticmethod
	def load_class(package):
		""" Loads a python class
		Arguments
			package -- Name of the python package
		"""
		klassname = package.split('.')[-1]
		pkg = package
		mod = __import__(pkg, fromlist=[''])
		klass = getattr(mod, klassname)
		return klassname, klass

	def __load_package(self, sim, config:Configuration, objects, module ):
		""" Internal function to load a python package
		Arguments
			sim -- Reference ot the simulation
			config -- Configuration attributes
			objects -- Object list
			module -- Module information
		"""
		try:
			package				= module['module']
			klassname, klass	= BootLoader.load_class(package)

			argv				= module.get("args")

			if argv is not None:
				args	= dict( item.split('=') for item in argv.split(' ') )
				inst	= klass( args )
			else:
				argv	= ''
				inst	= klass()

			sim.log.info( self.module, f'   + Module: {package} {argv}' )

			objects[klassname]	= inst
			# sim.log.trace( self.module, f'    /{scope}/{section}/{type}/{klassname}: {name}' )
			inst.on_init( Context(sim, config, sim.ipc), module )

			# Append the class instance to the loaded list
			self.seq.append( (inst, module) )
		except Exception as e:
			sim.log.error( self.module, f'Failed to load [{package}]: {str(e)}' )

		return objects

if __name__ == '__main__':
	test = BootLoader()


