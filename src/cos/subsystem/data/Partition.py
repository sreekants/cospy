#!/usr/bin/python
# Filename: Partition.py
# Description: Implementation of the Partition class

from cos.core.utilities.TransactionalDatabase import TransactionalDatabase
import queue

class Partition:
	def __init__(self, topic:str, fields:list):
		""" Constructor
		Arguments
			"""
		self.topic		= topic
		self.records	= queue.Queue()
		self.fields		= fields
		return

	def add(self, at, data):
		""" Queues data for write
		Arguments
			at -- Time of record
			data -- Data to be queued
		"""
		self.records.put( [at, data] )
		return

	def flush(self, db:TransactionalDatabase):
		""" Flushes data into the file system
		Arguments
			db -- Database to write to
		"""
		if self.records.empty():
			return None

		with self.records.mutex:
			while self.records.queue:
				self.serialize( db, self.records.queue.popleft() )

		return

	def serialize(self, db:TransactionalDatabase, rec):
		""" Serializes a record into the database
		Arguments
			db -- Database to write to
			rec -- Record to write
		"""
		at		= rec[0]
		data	= rec[1]

		# If all the fields are provided
		AUDIT_REGISTER	= 1000

		values	= []
		values.append( str(at) )
		values.append( str(AUDIT_REGISTER) )
		values.extend( map(str, data) )

		db.addkv( self.topic, self.fields, values )		
		return

	def __len__(self):
		""" Returns the number of items in queue
		"""
		return len(self.records)

if __name__ == "__main__":
	#test = Partition()
	l = {x[0]:None for x in ['a','b']}
	print(l)


