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
		""" The surrogate keys of a table: id and its dimension references
		Arguments
			conn -- Connection
			table -- Table name
		"""
		fields  = ['id']

		for f in ActiveRecord.fields(conn, table):
			fieldname   = f[1]
			if not Metadata.is_dimension_key(fieldname):
				continue

			fields.append( fieldname )

		return fields

	@staticmethod
	def is_dimension_key(fieldname):
		""" True for a reference to a dim_ table; case_id, vessel_id etc. are domain values
		Arguments
			fieldname -- Column name
		"""
		return fieldname.startswith('dim_') and fieldname.endswith('_id')


if __name__ == "__main__":
	test = Metadata()

