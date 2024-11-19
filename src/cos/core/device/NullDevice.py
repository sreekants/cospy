#!/usr/bin/python
# Filename: NullDevice.py
# Description: Base class for all devices

from cos.core.kernel.Device import Device
from cos.core.utilities.Errors import ErrorCode


class NullDevice(Device):
	def __init__(self, type, name):
		""" Constructor
		Arguments
			type -- Type of the object
			name -- Name of the object
		"""
		Device.__init__(self, type, name)
		return

	def type(self):
		""" Returns the type name of the object
		"""
		return 'NullDevice'

	def open( self, devicename, type, info ):
		""" Opens the device
		Arguments
			devicename -- Namd of the device
			type -- Type of the object
			info -- String of name-value pair attributes
		"""
		return True

	def bind( self, addr ):
		""" Binds the device to an address
		Arguments
			addr -- Device address
		"""
		return True

	def listen( self, ibacklog=0 ):
		""" Sets the device to a listening mode
		Arguments
			ibacklog -- Number of packets to hold in the queue
		"""
		return True

	def accept( self, info ):
		""" Accepts a new connection
		Arguments
			info -- String of name-value pair attributes
		"""
		return self

	def connect( self, addr ):
		""" Connects to an address
		Arguments
			addr -- Device address
		"""
		return True

	def close( self ):
		""" Closes the device
		"""
		return True


	def set( self, level, optname, poptvalue ):
		""" Sets a property on the device
		Arguments
			level -- Option level
			optname -- Option name
			poptvalue -- Option value
		"""
		return ErrorCode.ERROR_NOT_SUPPORTED


	def get( self, level, optname ):
		""" Returns a property on the device
		Arguments
			level -- Option level
			optname -- Option name
		"""
		return None


	def ioctl( self, command, args ):
		""" Performs an IO control operation
		Arguments
			command -- Command to send
			args -- Argument for the command
		"""
		return ErrorCode.ERROR_NOT_SUPPORTED


	def is_accept_pending( self, timeout ):
		""" Checks if a connection is pending on the device
		Arguments
			timeout -- Timeout to wait for
		"""
		return True


	def is_read_pending( self, timeout ):
		""" Checks if any data is available on the device
		Arguments
			timeout -- Timeout to wait for
		"""
		return True


	def is_open(self):
		""" Checks if the device is open
		"""
		return True



	def extension(self, type):
		""" Gets an extension interface on the device
		Arguments
			type -- Type of the interface
		"""
		return None

    # data exchange operations
	def send( self, data, flags=0 ):
		""" Sends data on the device
		Arguments
			data -- Data to send
			flags -- Binary 32-bit flag
		"""
		return True

	def receive( self, nbytes, flags=0 ):
		""" Receives data from the device
		Arguments
			nbytes -- Number of bytes to receive
			flags -- Binary 32-bit flag
		"""
		return ''


	def sendto( self, data, destaddr, flags=0 ):
		""" Sends data to a specific adddress
		Arguments
			data -- Data to send
			destaddr -- Address of destination
			flags -- Binary 32-bit flag
		"""
		return True

	def recvfrom( self, nbytes, flags=0 ):
		""" Reveives data from an address
		Arguments
			nbytes -- Number of bytes to receive
			flags -- Binary 32-bit flag
		"""
		return None

    # low-level i/o functions
	def read_port( self, flags=0 ):
		""" Reads raw data from the device
		Arguments
			flags -- Binary 32-bit flag
		"""
		return None

	def write_port( self, data, flags=0 ):
		""" Writes raw data to the device
		Arguments
			data -- Data to send
			flags -- Binary 32-bit flag
		"""
		return True

	def write( self, data, flags=0 ):
		""" Writes data to the device
		Arguments
			data -- Data to send
			flags -- Binary 32-bit flag
		"""
		return True


	def read( self, flags=0 ):
		""" Reads data from the device
		Arguments
			flags -- Binary 32-bit flag
		"""
		return None


	def readex( self, flags=0 ):
		""" Read with no wait timeout

		Arguments
			flags -- Binary 32-bit flag
		"""
		return None


    # kernel functions
	def startio( self, irp ):
		""" Starts I.O operations
		Arguments
			irp -- I/O request packet
		"""
		return ErrorCode.NOERROR

	def unload( self, irp ):
		""" Unloads the device
		Arguments
			irp -- I/O request packet
		"""
		return ErrorCode.NOERROR

	def dispatch( self, command, event, irp=None ):
		""" Dispatches events to the driver
		Arguments
			command -- Command to dispatch
			event -- Event to handle
			irp -- I/O request packet
		"""
		return ErrorCode.NOERROR

class Creator:
	def create( self, name:str, type:str, info, data ):
		""" Creates the Null device
		Arguments
			name -- Name of the object
			type -- Type of the object
			info -- String of name-value pair attributes
			data -- Additional data to create the device
		"""
		return NullDevice(type, name)


if __name__ == "__main__":
	test = NullDevice()


