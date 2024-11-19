#!/usr/bin/python
# Filename: ZMQFrame.py
# Description: Implementation of an COS network frame for ZMQ tranport

from cos.core.kernel.IPCMessage import IPCMessage
import struct, msgpack, socket, datetime

class ZMQFrame:
	@staticmethod
	def encode( objpath, seq, flag, ttl, payload ):
		""" Encodes a frame
		Arguments
			objpath -- Object path
			seq -- Sequence number of the frame
			flag -- Binary 32-bit flag
			ttl -- Time to live
			payload -- Payload of the frame
		"""
		props = struct.pack('iii',socket.htonl(seq),socket.htonl(flag),socket.htonl(ttl))

		return [b'', objpath.encode("ascii"), props, msgpack.packb(payload)]

	@staticmethod
	def decode( frame ):
		""" Decodes a frame
		Arguments
			frame -- Frame to decode
		"""
		objpath	= frame[1].decode('utf-8')
		props	= struct.unpack( 'iii', frame[2] )
		data	= msgpack.unpackb( frame[3] )

		# Encode the received packet to a message
		msg			= IPCMessage(objpath, '')
		now			= int(datetime.datetime.now(datetime.timezone.utc).timestamp())
		msg.id		= socket.ntohl(props[0])	# ID of the message
		msg.flag	= socket.ntohl(props[1])	# Message flags
		msg.ttl		= socket.ntohl(props[2])	# Time to live for the message

		msg.d		= data		# Payload of the message
		msg.p		= ''		# Properties of the payload
		msg.tc		= now		# Time the message was created
		msg.ts		= now		# Time the message was sent (UTC)
		msg.ta		= None		# Time the message arrived at the destination (UTC)

		return msg


if __name__ == '__main__':
	test = ZMQFrame()


