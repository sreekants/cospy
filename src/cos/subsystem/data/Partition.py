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
	def __init__(self, ctxt:Context, topic:str, fields:list, dimensions:list=None):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			topic -- Fact table
			fields -- Audit and measure columns, in payload order
			dimensions -- (leaf, column) per declared dimension, filled from a DataContext
		"""
		self.topic		= topic
		self.records	= queue.Queue()
		self.fields		= fields
		self.dimensions	= dimensions or []
		self.case_id	= ctxt.sim.case_id
		return

	@property
	def width(self)->int:
		""" Number of values a caller's payload must carry
		"""
		return len(self.fields) - AUDIT_FIELDS

	def add(self, at, tick, data, context=None):
		""" Queues data for write
		Arguments
			at -- Host time of the record, a timezone-aware datetime
			tick -- Simulation tick the record belongs to
			data -- Data to be queued
			context -- DataContext supplying the dimension columns; None leaves them NULL
		"""
		dims	= [ context.value( leaf ) if context is not None else None for leaf, _ in self.dimensions ]
		self.records.put( [at, tick, data, dims] )
		return

	def take(self)->list:
		""" Removes and returns every queued record, oldest first
		"""
		with self.records.mutex:
			taken	= list( self.records.queue )
			self.records.queue.clear()
		return taken

	def write(self, db:TransactionalDatabase, records:list):
		""" Writes taken records into an open transaction
		Arguments
			db -- Database to write to
			records -- Records from take()
		"""
		for rec in records:
			self.serialize( db, rec )
		return len( records )

	def restore(self, records:list):
		""" Puts taken records back at the head of the queue, after a failed write
		Arguments
			records -- Records from take()
		"""
		with self.records.mutex:
			self.records.queue.extendleft( reversed(records) )
		return

	def serialize(self, db:TransactionalDatabase, rec):
		""" Serializes a record into the database
		Arguments
			db -- Database to write to
			rec -- Record to write
		"""
		at		= rec[0]
		tick	= rec[1]
		data	= rec[2]
		dims	= rec[3]

		# creation_time, audit_status, case_id, tick
		values	= []
		values.append( at.isoformat(timespec='microseconds') )
		values.append( str(AUDIT_REGISTER) )
		values.append( str(self.case_id) )
		values.append( str(tick) )
		values.extend( None if v is None else str(v) for v in data )	# None is NULL, not the text 'None'

		values.extend( None if v is None else str(v) for v in dims )

		db.addkv( self.topic, self.fields + [ column for _, column in self.dimensions ], values )		
		return

	def __len__(self):
		""" Returns the number of items in queue
		"""
		return len(self.records)

if __name__ == "__main__":
	#test = Partition()
	l = {x[0]:None for x in ['a','b']}
	print(l)


