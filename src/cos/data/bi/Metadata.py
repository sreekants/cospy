#!/usr/bin/python
# Filename: Metadata.py
# Description: Implementation of the Metadata class

from cos.core.utilities.ActiveRecord import ActiveRecord

import re,sqlite3,os

# Dimension columns holding natural keys (IMO, Morton code), never renumbered on merge
NATURAL_KEYS	= ('dim_gps_id', 'dim_vessel_id')

# Tables describing a single run; their values change across scenarios, so they are never merged
RUN_TABLES		= ('configs',)

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
	def is_run_table(tablename):
		""" True for a table that describes one run and is never merged
		Arguments
			tablename -- Table name
		"""
		return tablename in RUN_TABLES

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
		""" True for a surrogate reference to a dim_ table; case_id, vessel_id and NATURAL_KEYS are domain values
		Arguments
			fieldname -- Column name
		"""
		return fieldname.startswith('dim_') and fieldname.endswith('_id') and (fieldname not in NATURAL_KEYS)


if __name__ == "__main__":
	test = Metadata()

