#!/usr/bin/python
# Filename: Partition.py
# Description: Implementation of the Partition class

from cos.core.utilities.TransactionalDatabase import TransactionalDatabase
from cos.core.kernel.Context import Context

import queue

# Fields every fact table opens with, supplied by serialize()
AUDIT_FIELDS	= 4
AUDIT_REGISTER	= 1000

class Partition:
	def __init__(self, ctxt:Context, topic:str, fields:list):
		""" Constructor
		Arguments
			"""
		self.topic		= topic
		self.records	= queue.Queue()
		self.fields		= fields
		self.case_id	= ctxt.sim.case_id
		return

	@property
	def width(self)->int:
		""" Number of values a caller's payload must carry
		"""
		return len(self.fields) - AUDIT_FIELDS

	def add(self, at, tick, data):
		""" Queues data for write
		Arguments
			at -- Host time of the record, a timezone-aware datetime
			tick -- Simulation tick the record belongs to
			data -- Data to be queued
		"""
		self.records.put( [at, tick, data] )
		return

	def flush(self, db:TransactionalDatabase):
		""" Flushes data into the file system
		Arguments
			db -- Database to write to
		"""
		if self.records.empty():
			return 0

		count = 0
		with self.records.mutex:
			while self.records.queue:
				self.serialize( db, self.records.queue.popleft() )
				count	+= 1

		return count

	def serialize(self, db:TransactionalDatabase, rec):
		""" Serializes a record into the database
		Arguments
			db -- Database to write to
			rec -- Record to write
		"""
		at		= rec[0]
		tick	= rec[1]
		data	= rec[2]

		# creation_time, audit_status, case_id, tick
		values	= []
		values.append( at.isoformat(timespec='microseconds') )
		values.append( str(AUDIT_REGISTER) )
		values.append( str(self.case_id) )
		values.append( str(tick) )
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


