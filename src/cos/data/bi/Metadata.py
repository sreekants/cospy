#!/usr/bin/python
# Filename: Metadata.py
# Description: Implementation of the Metadata class

from cos.core.utilities.ActiveRecord import ActiveRecord

import re,sqlite3,os

class Metadata:
	def __init__(self):
		return

	@staticmethod
	def is_enumuration(tablename):
		# Capitalized tablenames are enumerations by convention
		if re.match('[A-Z_]+', tablename) == None:
			return False
		return True

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

