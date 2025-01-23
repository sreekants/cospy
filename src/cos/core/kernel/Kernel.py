#!/usr/bin/python
# Filename: Kernel.py
# Description: A class for micro kernel in the simulation environment

from cos.core.kernel.MessageQueue import MessageQueue
from cos.core.kernel.Logger import Logger
from cos.core.kernel.ObjectManager import ObjectManager
from cos.core.kernel.DeviceManager import DeviceManager
from cos.core.kernel.FileSystem import FileSystem
from cos.core.kernel.ParameterManager import ParameterManager
from cos.core.kernel.BootLoader import BootLoader
from cos.core.kernel.ThreadPool import ThreadPool
from cos.core.kernel.Configuration import Configuration
from cos.core.time.Clock import Clock
from cos.core.utilities.Patterns import Manager

class Kernel:
	def __init__(self):
		""" Constructor
		"""
		self.subsystems	= Manager()
		self.ipc		= MessageQueue()
		self.log		= None
		self.config		= None

		self.clock		= Clock()
		self.objects	= ObjectManager()
		self.devices	= DeviceManager()
		self.params		= ParameterManager()
		self.loader		= BootLoader()
		self.fs			= FileSystem()

		self.subsystems	= [
			self.devices,
			self.params,
		]

		self.__init_settings()
		return

	def now(self):
		""" Returns the current kernel time
		"""
		return self.clock.utc
	
	def start(self, configfile, configpath, settings):
		""" Starts the kernel
		Arguments
			configfile -- Name of the configuration file
			configpath -- Path to the configuration directory
		"""
		self.scheduler	= self.create_thread_pool()
		self.config	= Configuration(configfile, configpath, settings['image'],
							  ['LOCATION','SIMULATION','DB','MAP']
							  )
		self.log	= Logger( self.config )

		self.log.info( "Kernel", "Initializing...")
		self.loader.startup( self, self.config )

		# Initialize the thread pool
		MaxThreads	= self.config.get_int('ProcessManager','NumThreads')
		self.scheduler.create( MaxThreads )
		return

	def create_thread_pool(self):
		""" Creates the thread pool
		"""
		return ThreadPool(self)

	def stop(self):
		""" Stops the kernel
		"""
		self.log.info( "Kernel", "Shutting down...")

		# Shutdown the thread pool
		self.scheduler.close()

		# Bring down the modules
		self.loader.shutdown( self )
		return


	def __init_settings(self):
		""" Internal function to initialize the kernel settings
		"""
		self.__settings	= {
				"Folders":	{}
			}
		return

	@property
	def folders(self):
		""" Returns the folders for the OS
		"""
		return self.__settings["Folders"]

	@property
	def settings(self):
		""" Returns a setting for the Kernel
		"""
		return self._settings


	def get_component( self, type:str ):
		""" Returns a named component of the OS
		Arguments
			type -- Typename of the component
		"""
		return self.subsystems.get( type )

	def set_component( self, type:str, obj ):
		""" Assigns a named component of the OS
		Arguments
			type -- Typename of the component
		"""
		return self.subsystems.set( type, obj )



if __name__ == "__main__":
	test = Kernel()


