#!/usr/bin/python
# Filename: Device.py
# Description: Base class for all devices

from cos.core.kernel.Object import Object

from abc import ABC, abstractmethod
import uuid

class Device(ABC, Object):
	def __init__(self, type, name):
		""" Constructor
		Arguments
			type -- Type of the object
			name -- Name of the object
		"""
		category	= 'Devices'

		self.guid	= str(uuid.uuid1()).lower()
		if name == None:
			name	= self.guid

		scope	= f'{category}/{type}.{self.__class__.__name__}'
		Object.__init__( self, scope, name )
		return

	@staticmethod
	def throw_not_impl( self ):
		""" Helper function to throw an exception for an unimplemented function
		"""
		raise Exception("Function is not implemetnted")

	@abstractmethod
	def open( self, devicename, type, info ):
		""" Opens the device
		Arguments
			devicename -- Device name
			type -- Type of the object
			info -- String of name-value pair attributes
		"""
		pass

	@abstractmethod
	def bind( self, addr ):
		""" Binds a device to an address
		Arguments
			addr -- Device address
		"""
		pass

	@abstractmethod
	def listen( self, ibacklog ):
		""" Sets the device to listen mode
		Arguments
			ibacklog -- Backlog of events to hold while listening
		"""
		pass

	@abstractmethod
	def accept( self, info ):
		""" Accepts a connection to the device
		Arguments
			info -- String of name-value pair attributes
		"""
		pass

	@abstractmethod
	def connect( self, addr ):
		""" Connects a device to an address
		Arguments
			addr -- Device address
		"""
		pass

	@abstractmethod
	def close(self):
		""" Closes the socket
		"""
		pass

	@abstractmethod
	def set( self, level, optname, optvalue ):
		""" Sets an option on the device
		Arguments
			level -- Option level
			optname -- Option name
			optvalue -- Option value
		"""
		pass

	@abstractmethod
	def get( self, level, optname ):
		""" Returns the current option on a device
		Arguments
			level -- Option level
			optname -- Option name
		"""
		pass

	@abstractmethod
	def ioctl( self, command, arg ):
		""" Performs an I/O control operation on the device
		Arguments
			command -- Command
			arg -- Arguments to the command
		"""
		pass

	@abstractmethod
	def is_accept_pending( self, timeout ):
		""" Checks if a connection is pending
		Arguments
			timeout -- Wait timeout for the rrequest
		"""
		pass

	@abstractmethod
	def is_read_pending( self, timeout ):
		""" Checks if read data is pending on the socket
		Arguments
			timeout -- Wait timeout for the rrequest
		"""
		pass

	@abstractmethod
	def is_open(self ):
		""" Checks if the socket is open
		"""
		pass


	@abstractmethod
	def extension(self, type):
		""" Returs an extension interface supported bythe device
		Arguments
			type -- Interface type name supported bythe device
		"""
		pass

    # data exchange operations
	@abstractmethod
	def send( self, data, flags=0 ):
		""" Sends data on the socket
		Arguments
			data -- Data to send
			flags -- Additional transmisson flags
		"""
		pass

	@abstractmethod
	def receive( self, nbytes, flags=0 ):
		""" Receives bytes from the socket, blocking for till data arrives
		Arguments
			nbytes -- Bytes to receive
			flags -- Additional transmisson flags
		"""
		pass

	@abstractmethod
	def receiveex( self, nbytes, flags=0 ):
		""" Receives pending data from the socket, without blocking
		Arguments
			nbytes -- Bytes to receive
			flags -- Additional transmisson flags
		"""
		pass

	@abstractmethod
	def sendto( self, data, destaddr, flags=0 ):
		""" Sends data to an address
		Arguments
			data -- Data to send
			destaddr -- Destination address
			flags -- Additional transmisson flags
		"""
		pass

	@abstractmethod
	def recvfrom( self, nbytes, flags=0 ):
		""" Receives pending data from the socket, without blocking
		Arguments
			nbytes -- Bytes to receive
			flags -- Additional transmisson flags
		"""
		pass

	@abstractmethod
	def type(self):
		""" Returns the type of the device
		"""
		pass


    # low-level i/o functions
	def read_port( self, flags=0 ):
		""" Low level function to read from a port
		Arguments
			flags -- Additional transmisson flags
		"""
		self.throw_not_impl()
		return

	def write_port( self, flags=0 ):
		""" Low level function to write to a port
		Arguments
			flags -- Additional transmisson flags
		"""
		self.throw_not_impl()
		return

	def write( self, data, flags=0 ):
		""" Writes data to the socket
		Arguments
			data -- Data to send
			flags -- Additional transmisson flags
		"""
		self.throw_not_impl()
		return

	def read( self, flags=0 ):
		""" Reads from the socket, blocking for the first stream of data
		Arguments
			flags -- Additional transmisson flags
		"""
		self.throw_not_impl()
		return

	@abstractmethod
	def readex( self, flags=0 ):
		""" Reads a byte without blocking
		Arguments
			flags -- Additional transmisson flags
		"""
		self.throw_not_impl()
		return


    # kernel functions
	def startio( self, irp ):
		""" Initializes IO operations
		Arguments
			irp -- Interrupt request packet
		"""
		pass

	def start( self ):
		""" Starts the device
		"""
		pass

	def suspend( self ):
		""" Suspends the device
		"""
		pass

	def resume( self ):
		""" Resumes the device
		"""
		pass

	def term( self ):
		""" Terminates th device
		"""
		pass

	def unload( self, irp ):
		""" Unloads the device
		Arguments
			irp -- Interrupt request packet
		"""
		pass

	def dispatch( self, command, event, irp ):
		""" Dispatches commands to the device driver
		Arguments
			command -- Command to the driver
			event -- Event to be handled by the driver
			irp -- Interrupt request packet
		"""
		pass



if __name__ == "__main__":
	test = Device(self, )


