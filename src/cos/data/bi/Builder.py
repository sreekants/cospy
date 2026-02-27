#!/usr/bin/python
# Filename: Builder.py
# Description: Implementation of the Builder class

from cos.data.bi.Metadata import Metadata
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
		for f in files:
			self.copy_data(f, tgt, tables)
		return
	
	def calculate_maxrange(self, files:list):
		maxid		= 0			
		for f in files:
			idrange		= Metadata.get_rowrange(f)
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
		"""
		Copies all records for a given table from a source database to a target database.

		Args:
			src (str): The file path of the source SQLite database.
			tgt (str): The file path of the target SQLite database.
			table_name (str): The name of the table to copy.
		"""
		# Ensure the target table exists in the target database before inserting.
		# The schema must match exactly.
		# You might want to add a check here to create the table if it doesn't exist.

		try:
			# Connect to the source database
			conn = sqlite3.connect(src)
			c = conn.cursor()

			# Attach the target database to the source connection with an alias
			attach_query = f"ATTACH DATABASE '{tgt}' AS target_db"
			c.execute(attach_query)
			for table_name in tables:
				# Copy data from the source table (main.table_name) to the target table (target_db.table_name)
				# Use INSERT OR REPLACE if you want to overwrite existing records with the same primary key
				copy_query = f"INSERT INTO target_db.{table_name} SELECT * FROM main.{table_name}"
				c.execute('BEGIN TRANSACTION')
				c.execute(copy_query)
				c.execute('COMMIT')

				# Commit the changes to the target database
				conn.commit()

				print(f"Data successfully copied from '{src}' table '{table_name}' to '{tgt}'")

		except sqlite3.Error as e:
			print(f"SQLite error: {e}")

		finally:
			# Detach the database and close the connection
			if conn:
				c.execute("DETACH DATABASE target_db")
				conn.close()



if __name__ == "__main__":
	test = Builder()

	for n in range(0,11):
		n			= 100*n
		exponent	= 1 if n==0 else int(math.log10(n))+1
		print( f'{n} -> {10**exponent}' )




