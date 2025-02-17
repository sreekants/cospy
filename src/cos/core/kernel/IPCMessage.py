#!/usr/bin/python
# Filename: IPCMessage.py
# Description: Message used for inter-process communication

import json, datetime

class IPCFlags:
	IPC_MESSAGE_PRIORITY_MASK		= 0x0000000F
	IPC_MESSAGE_STATUS_MASK			= 0x000000F0
	IPC_MESSAGE_CONTENT_MASK		= 0xF0000000
	IPC_MESSAGE_AUTH_FLAG			= 0x00010000
	IPC_MESSAGE_URGENT_FLAG			= 0x00020000
	IPC_MESSAGE_JOURNAL_FLAG		= 0x00040000
	IPC_MESSAGE_PRIVATE_FLAG		= 0x00080000
	IPC_MESSAGE_NEED_ACK_FLAG		= 0x00100000
	IPC_MESSAGE_EXCEPTION			= 0x00200000

class IPCMessage:
	def __init__(self, target=None, evt=None, payload=None, flag=0):
		""" Constructor
		Arguments
			target -- Target of the message
			evt -- Event data
			payload -- Additional payload for the message
			flag -- Binary 32-bit flag
		"""
		now			= int(datetime.datetime.now(datetime.timezone.utc).timestamp())

		if target!=None and evt != None:
			self.h 		= f"to=/{target},evt={evt}"
		else:
			self.h		= None

		self.id		= 0			# ID of the message
		self.flag	= flag		# Message flags
		self.ttl	= 0			# Time to live for the message
		self.d		= payload	# Payload of the message
		self.p		= ""		# Properties of the payload
		self.tc		= now		# Time the message was created
		self.ts		= now		# Time the message was sent (UTC)
		self.ta		= None		# Time the message arrived at the destination (UTC)
		return

	def isset(self, flag):
		""" Checsks if all flags are set
		Arguments
			flag -- Binary 32-bit flag
		"""
		return ((self.flag & flag) == flag)

	def isanyset(self, flag):
		""" Checks if any flag is set
		Arguments
			flag -- Binary 32-bit flag
		"""
		return ((self.flag & flag) != 0)

	def set(self, flag):
		""" Sets a flag
		Arguments
			flag -- Binary 32-bit flag
		"""
		self.flag = (self.flag | flag)
		return self.flag

	def reset(self, flag):
		""" Resets a flag
		Arguments
			flag -- Binary 32-bit flag
		"""
		self.flag = (self.flag & ~ flag)
		return self.flag

	def failed(self):
		""" Checks if the message is an exception
		"""
		return self.isset( IPCFlags.IPC_MESSAGE_EXCEPTION )

	def encode(self):
		""" Encodes the message for transmission
		"""
		return self.__str__().encode("ASCII")

	def decode(self, data):
		""" Decodes the message for transmission
		Arguments
			data -- Data of the message to decode
		"""
		message = json.loads(data)

		self.h		= message["h"]
		self.id		= message["id"]
		self.flag	= message["flg"]
		self.d		= message["d"]
		self.p		= message["p"]
		self.tc		= message["tc"]
		self.ts		= message["ts"]

		return self

	def __str__(self):
		""" Displays the message in a string format:
		"""
		message = {
			"h": self.h,
			"id": self.id,
			"flg": self.flag,
			"d": self.d,
			"p": self.p,
			"tc": self.tc,
			"ts": self.ts
		}

		return IPCMessage.__Stringify(message, exclude_null=False)

	@staticmethod
	def __Stringify(obj, exclude_null = False):
		""" Helper function to encode the message to a string
		Arguments
			obj -- The message objects
			exclude_null  -- Flag to exclude nulls
		"""
		if(exclude_null == True):
			obj = IPCMessage.RemoveNulls(obj)
		print(obj)
		return json.dumps(obj)

	@staticmethod
	def RemoveNulls(obj):
		""" Compact the mesage removing nulls
		Arguments
			obj -- The message objects
		"""
		return {k: v for k, v in obj.items() if v is not None}

if __name__ == "__main__":
	msg = IPCMessage('/$Kernel','0x01000011')
	print(msg)

