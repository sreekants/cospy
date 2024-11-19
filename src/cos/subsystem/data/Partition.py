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

	def add(self, data):
		""" Queues data for write
		Arguments
			data -- Data to be queued
		"""
		self.records.put( data )
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

	def serialize(self, db:TransactionalDatabase, data):
		""" Serializes a record into the database
		Arguments
			db -- Database to write to
			data -- Record to write
		"""
		db.addkv( self.topic, self.fields, map(str, data) )
		return

	def __len__(self):
		""" Returns the number of items in queue
		"""
		return len(self.records)

if __name__ == "__main__":
	#test = Partition()
	l = {x[0]:None for x in ['a','b']}
	print(l)


