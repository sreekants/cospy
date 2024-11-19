#!/usr/bin/python
# Filename: KeyStore.py
# Description: Implementation of a key store database.

from cos.core.utilities.ActiveRecord import ActiveRecord
import os

class KeyStore:
	def __init__(self, table_name, dbpath):
		""" Constructor
		Arguments
			"""

		self.table	= table_name

		#If the value database does not exist, create it
		if os.path.isfile(dbpath) == True:
			self.model	= ActiveRecord.create(self.table, dbpath, self.table)
		else:
			self.model	= ActiveRecord.create(self.table, dbpath, self.table)
			self.model.ExecuteSQL( 'CREATE TABLE [{}] ('\
				'[id] INTEGER PRIMARY KEY AUTOINCREMENT NULL,'\
				'[key] VARCHAR(64) UNIQUE NULL,'\
				'[value] VARCHAR(64) NULL)'.format(self.table) )
		return

	def set(self, key, value):
		""" Saves the value with a matching key. Creates a new entry if the key does not exist
		Arguments
				key -- key to identify the value
			value -- value to save
		"""
		oid	= self.FindKey(key)
		if oid == None:
			values = {
				'key': key,
				'value': value }
			self.model.add( values )
			return

		self.model.set( oid, 'value', value)
		return

	def get(self, key):
		""" Gets the value identified with a matching key. Returns 'None' if the key does not exist
		Arguments
				key -- key to identify the value
		"""
		return self.model.get_unique_by( 'value', 'key', key)

	def remove(self, key):
		""" Removes value with a matching key
		Arguments
				key -- key to identify the value
		"""
		self.model.delete_by( 'key', key)
		return

	def find_key(self, key):
		""" Returns the record id with a matching key, or 'None' if no match is found
		Arguments
				key -- key to identify the value
		"""
		return self.model.get_unique_by( 'id', 'key', key)

	def clear(self):
		""" Removes all value from the cache:
		Arguments
			"""
		self.model.execute_sql( 'DELETE FROM [{}]'.format(self.table) )
		return

	def for_each(self, fn, ctxt):
		""" Iterates through each record in the keystore
		Arguments
			fn -- Callback to invoke for each callback
			ctxt -- Opaque context passed to the callback
		"""
		c		= self.model.conn.cursor()
		c.execute('SELECT id, key, value FROM {}'.format(self.table) )

		for row in c:
			fn(row[0], row[1], row[2], ctxt)

		c.close()
		return

	def __getitem__(self, key):
		""" Gets the value identified with a matching key. Returns 'None' if the key does not exist
		Arguments
				key -- key to identify the value
		"""
		return self.Get( key )

	def __setitem__(self, key, value):
		""" Saves the value with a matching key. Creates a new entry if the key does not exist
		Arguments
				key -- key to identify the value
			value -- value to save
		"""
		self.Set( key, value)
		return

	def has_key(self, key):
		""" Checks if a value with a matching key exists
		Arguments
				key -- key to identify the value
		"""
		return self.find_key(key)



if __name__ == "__main__":
	test = KeyStore()


