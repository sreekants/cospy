#!/usr/bin/python
# Filename: DeviceManager.py
# Description: Implementation of a generic device manager

from cos.core.kernel.Context import Context
from cos.core.kernel.Subsystem import Subsystem
from cos.core.kernel.ObjectManager import ObjectManager, ObjectNode, ObjectType
from cos.core.kernel.Device import Device
from cos.core.utilities.Tree	import Tree, TreeNode, ErrorCode

class DeviceManager(Subsystem):
	def __init__(self):
		""" Constructor
		"""
		Subsystem.__init__(self, "Kernel", "DeviceManager")
		self.types		= {}
		self.sim		= None
		self.resolver	= None
		self.objects:ObjectManager	= None
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		self.sim		= ctxt.sim
		self.objects	= ctxt.sim.objects
		return

	def on_term(self, ctxt:Context, module):
		""" Callback for simulation termination
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		for dev in self.objects.get_all("/Devices"):
			if isinstance(dev, Device):
				dev.term()

		self.sim	= None
		return

	def create( self, name:str, type:str, info, data )->Device:
		""" Creates a device
		Arguments
			name -- Name of the object
			type -- Type of the object
			info -- String of name-value pair attributes
			data -- Additional arguments passed to the device during construction
		"""
		if self.resolver is not None:
			info	= self.resolver(info)

		creator = self.types.get(type)
		if creator is None:
			return None

		dev		= creator.create( name, type, info, data)
		return dev

	def get( self, name:str, type:str, flag=0 )->Device:
		""" Gets a loaded device by name
		Arguments
			name -- Name of the object
			type -- Type of the object
			flag -- Binary 32-bit flag
		"""
		if name.startswith('/') == False:
			name = f'/Devices/{name}'

		return self.objects.get( name, 4, flag )

	def exists( self, name:str, type:str, flag=0 )->bool:
		""" Checks if a device exists
		Arguments
			name -- Name of the object
			type -- Type of the object
			flag -- Binary 32-bit flag
		"""
		return (self.get(name, type, flag) is not None)

	def assert_valid( self, name:str, type:str, flag=0 ):
		""" Asserts if a device is valid
		Arguments
			name -- Name of the object
			type -- Type of the object
			flag -- Binary 32-bit flag
		"""
		if self.get(name, type, flag) == None:
			raise Exception( f"Unknown device [{name}] of type [{type}]" )
		return

	def register( self, type, creator ):
		""" Register a factory for a device type
		Arguments
			type -- Type of the object
			creator -- Factory for the device
		"""
		self.types[type]	= creator
		return

	def unregister( self, type )->bool:
		""" Unregistrs a device factory
		Arguments
			type -- Type of the object
		"""
		if type not in self.types:
			return False

		self.types.pop(type)
		return True



if __name__ == "__main__":
	test = DeviceManager()


