#!/usr/bin/python
# Filename: MagneticCompass.py
# Description: Implementation of the MagneticCompass device

from cos.core.kernel.Device import Device
from cos.core.utilities.Errors import ErrorCode


class MagneticCompass(Device):
	def __init__(self, type, name):
		""" Constructor
		Arguments
			type -- Type of the object
			name -- Name of the object
		"""
		Device.__init__(self, type, name)
		return

	def type(self):
		""" #TODO: type
		"""
		return 'MagneticCompass'

	def open( self, devicename, type, info ):
		""" #TODO: open
		Arguments
			devicename -- #TODO
			type -- Type of the object
			info -- String of name-value pair attributes
		"""
		return True

	def bind( self, addr ):
		""" #TODO: bind
		Arguments
			addr -- Device address
		"""
		return True

	def listen( self, ibacklog ):
		""" #TODO: listen
		Arguments
			ibacklog -- #TODO
		"""
		return True

	def accept( self, info ):
		""" #TODO: accept
		Arguments
			info -- String of name-value pair attributes
		"""
		return self

	def connect( self, addr ):
		""" #TODO: connect
		Arguments
			addr -- Device address
		"""
		return True

	def close(self):
		""" #TODO: close
		"""
		return True


	def set( self, level, optname, poptvalue ):
		""" #TODO: set
		Arguments
			level -- Option level
			optname -- Option name
			poptvalue -- Option value
		"""
		return ErrorCode.ERROR_NOT_SUPPORTED


	def get( self, level, optname ):
		""" #TODO: get
		Arguments
			level -- Option level
			optname -- Option name
		"""
		return ErrorCode.ERROR_NOT_SUPPORTED


	def ioctl( self, command, pargument ):
		""" #TODO: ioctl
		Arguments
			command -- #TODO
			pargument -- #TODO
		"""
		return ErrorCode.ERROR_NOT_SUPPORTED


	def is_accept_pending( self, timeout ):
		""" #TODO: is_accept_pending
		Arguments
			timeout -- #TODO
		"""
		return True


	def is_read_pending( self, timeout ):
		""" #TODO: is_read_pending
		Arguments
			timeout -- #TODO
		"""
		return True


	def is_open(self):
		""" #TODO: is_open
		"""
		return True



	def extension(self, type):
		""" #TODO: extension
		Arguments
			type -- Type of the object
		"""
		return None

    # data exchange operations
	def send( self, data, flags=0 ):
		""" #TODO: send
		Arguments
			data -- #TODO
			flags -- #TODO
		"""
		return True

	def receive( self, nbytes, flags=0 ):
		""" #TODO: receive
		Arguments
			nbytes -- #TODO
			flags -- #TODO
		"""
		return ''

	def receiveex( self, nbytes, flags=0 ):
		""" #TODO: receiveex
		Arguments
			nbytes -- #TODO
			flags -- #TODO
		"""
		return ''

	def sendto( self, data, destaddr, flags=0 ):
		""" #TODO: sendto
		Arguments
			data -- #TODO
			destaddr -- #TODO
			flags -- #TODO
		"""
		return True

	def recvfrom( self, nbytes, flags=0 ):
		""" #TODO: recvfrom
		Arguments
			nbytes -- #TODO
			flags -- #TODO
		"""
		return None



class Driver:
	def __init__(self, ctxt, vehicle, dev, args=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			vehicle -- Reference ot the simulation vehicle
			dev -- #TODO
			args -- List of arguments
		"""
		self.dev        = dev
		self.vehicle    = vehicle
		return



if __name__ == "__main__":
	test = MagneticCompass()


