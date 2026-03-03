#!/usr/bin/python
# Filename: Analyzer.py
# Description: Implementation of the Analyzer class

from cos.data.bi.Metadata import Metadata
from cos.core.utilities.ActiveRecord import ActiveRecord
import re,sqlite3,os


class Analyzer:
	def __init__(self):
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



if __name__ == "__main__":
	test = Analyzer()

