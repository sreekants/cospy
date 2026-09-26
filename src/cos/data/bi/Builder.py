#!/usr/bin/python
# Filename: Builder.py
# Description: Implementation of the Builder class

from cos.data.bi.Metadata import Metadata
from cos.data.bi.Analyzer import Analyzer
from cos.core.utilities.ActiveRecord import ActiveRecord

import sqlite3,os, math

class Builder:
	def __init__(self):
		return

	def process( self, files:list):
		# Calculate the maximum range
		maxid	= self.calculate_maxrange(files)

		# Calculate the optimal partition size as a power of 10
		span	= self.calculate_partition_size(maxid)

		self.partition( files, span )
		return


	def merge(self, tgt, files:list, tables:list):
		""" Copies every file's tables into tgt
		Arguments
			tgt -- Path of the target database
			files -- Partitioned source databases
			tables -- Table names to copy
		Returns
			A list of (file, rows, notes), one per file
		"""
		outcomes	= []
		for f in files:
			rows, notes	= self.copy_data(f, tgt, tables)
			outcomes.append( (f, rows, notes) )
		return outcomes
	
	def calculate_maxrange(self, files:list):
		maxid		= 0			
		for f in files:
			idrange		= Analyzer.get_rowrange(f)
			if idrange[1] > maxid:
				maxid	= idrange[1]

		return maxid
	
	def calculate_partition_size(self, maxid):
		exponent	= 1 if maxid==0 else int(math.log10(maxid))+1
		return 10**exponent


	def partition(self, files, increment):
		index	= 1

		# Partition each database with my multiples 
		# of the increment so record-ids do not collide
		for f in files:
			conn    = sqlite3.connect(f)
			self.increment_ids(conn, index*increment)
			conn.close()
			index	= index+1
		return

	def increment_ids(self, conn, increment):
		c       = conn.cursor()

		for table in ActiveRecord.tables(conn):
			if Metadata.is_enumuration(table):
				continue

			# Extract all the fields of the table. This will include 
			# the 'id' field and all fields with the suffix '_id' that
			# marks foreign key references.
			idfields  = Metadata.get_id_fields(conn, table)

			# Increment all primary keys and foreign keys to
			# assure integrity of the transaction
			c.execute( 'BEGIN TRANSACTION' )
			for f in idfields:
				sql = f'UPDATE {table} SET {f}={f}+{increment}'
				c.execute(sql)

			c.execute( 'COMMIT' )
		conn.commit()

		return

	def copy_data(self, src, tgt, tables):
		""" Copies every row of the given tables from src into tgt, by column name
		Arguments
			src -- Path of the source database
			tgt -- Path of the target database
			tables -- Table names to copy
		Returns
			(rows, notes) - rows copied per table, and one note per table skipped or narrowed
		"""
		rows	= {}
		notes	= []

		conn	= sqlite3.connect(src)
		c		= conn.cursor()
		c.execute( 'ATTACH DATABASE ? AS target_db', (tgt,) )
		try:
			for table in tables:
				source	= Builder.columns( c, 'main', table )
				target	= Builder.columns( c, 'target_db', table )
				if not source:
					notes.append( f'{table}: absent from source' )
					continue
				if not target:
					notes.append( f'{table}: absent from target' )
					continue

				dropped	= [col for col in source if col not in target]
				if dropped:
					notes.append( f'{table}: source columns not in target, not copied: {", ".join(dropped)}' )

				shared	= ', '.join( f'"{col}"' for col in source if col in target )
				c.execute( 'BEGIN TRANSACTION' )
				c.execute( f'INSERT INTO target_db."{table}" ({shared}) SELECT {shared} FROM main."{table}"' )
				rows[table]	= c.rowcount
				c.execute( 'COMMIT' )
		finally:
			conn.commit()
			c.execute( 'DETACH DATABASE target_db' )
			conn.close()

		return rows, notes

	@staticmethod
	def columns(cursor, schema, table):
		""" Column names of a table in an attached schema, empty when the table is absent
		Arguments
			cursor -- Cursor
			schema -- 'main' or an attached alias
			table -- Table name
		"""
		cursor.execute( f'PRAGMA {schema}.table_info("{table}")' )
		return [ row[1] for row in cursor.fetchall() ]


if __name__ == "__main__":
	test = Builder()

	for n in range(0,11):
		n			= 100*n
		exponent	= 1 if n==0 else int(math.log10(n))+1
		print( f'{n} -> {10**exponent}' )




