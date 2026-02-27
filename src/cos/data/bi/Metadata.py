#!/usr/bin/python
# Filename: Metadata.py
# Description: Implementation of the Metadata class

from cos.core.utilities.ActiveRecord import ActiveRecord

import re,sqlite3,os

class Metadata:
	def __init__(self):
		print( "Hello" )
		return

	@staticmethod
	def get_databases(path):
		files = []
		for filename in os.listdir(path):
			if not filename.endswith('.s3db'):
				continue

			files.append(filename)

		return files

	@staticmethod
	def is_enumuration(tablename):
		# Capitalized tablenames are enumerations by convention
		if re.match('[A-Z_]+', tablename) == None:
			return False
		return True

	@staticmethod
	def get_rowrange(path):
		db      = sqlite3.connect(path)
		c       = db.cursor()

		minval  = 0
		maxval  = 0

		for table in ActiveRecord.tables(db):
			if Metadata.is_enumuration(table):
				continue

			c.execute( f'SELECT min(id) as minid, max(id) as maxid FROM {table}'  )
			row	= c.fetchone()
			if row[1] is None:
				continue

			# Handle initialization
			if minval == 0:
				minval  = row[0] 
				maxval  = row[1]
				print( f'{table}: {row[0]}-{row[1]}')
				continue

			if  row[0] < minval:
				minval  = row[0] 

			if  row[1] > maxval:
				maxval  = row[1]

			print( f'{table}: {row[0]}-{row[1]}')

		c.close()
		db.close()

		return (minval, maxval)

	@staticmethod
	def get_id_fields(conn, table):
		fields  = ['id']

		for f in ActiveRecord.fields(conn, table):
			fieldname   = f[1]
			if not fieldname.endswith('_id'):
				continue

			fields.append( fieldname )

		return fields

		

if __name__ == "__main__":
	test = Metadata()

