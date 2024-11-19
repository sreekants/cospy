#!/usr/bin/python
# Filename: ActiveRecord.py
# Description: Active record design pattern for ORM DB access


import re,sqlite3,os,shutil

rule_tuple = (
	('[ml]ouse$', '([ml])ouse$', '\\1ice'),
	('child$', 'child$', 'children'),
	('booth$', 'booth$', 'booths'),
	('foot$', 'foot$', 'feet'),
	('ooth$', 'ooth$', 'eeth'),
	('l[eo]af$', 'l([eo])af$', 'l\\1aves'),
	('sis$', 'sis$', 'ses'),
	('man$', 'man$', 'men'),
	('ife$', 'ife$', 'ives'),
	('eau$', 'eau$', 'eaux'),
	('lf$', 'lf$', 'lves'),
	('[sxz]$', '$', 'es'),
	('[^aeioudgkprt]h$', '$', 'es'),
	('(qu|[^aeiou])y$', 'y$', 'ies'),
	('$', '$', 's')
)


def regex_rules(rules=rule_tuple):
	""" Matches rules in a colleciton of regular expressions
	Arguments
		rules=rule_tuple -- Rule map
	"""
	for line in rules:
		pattern, search, replace = line
		yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)


def plural(noun):
	""" Pluralizes a noun
	Arguments
		noun -- Noun to pluralize
	"""
	for rule in regex_rules():
		result = rule(noun)
		if result:
			return result


class ActiveRecord:
	def __init__(self, model, conn, table=None):
		""" Constructor
		Arguments
				model -- Name of the model
			conn -- Database connection
		"""
		self.conn 	= conn
		self.model	= model

		if table is None:
			self.table	= plural(model)
		else:
			self.table	= table
		return

	def __exit__(self, exception_type, exception_value, exception_traceback):
		""" Called when exception occurs
		Arguments
			exception_type -- Type of exception
			exception_value -- Valie of the exception
			exception_traceback -- Exception stack
		"""
		if self.conn is not None:
			self.conn.close()

	@staticmethod
	def create(model, path, table=None):
		""" Creates an active record with an SQLite connection to a database file
		Arguments
			model -- Name of the model
			path -- Path to the file
		"""
		return ActiveRecord( model, sqlite3.connect(path), table )

	@staticmethod
	def connect(path):
		""" Creates an SQLite connection to a database file
		Arguments
			path -- Path to the database file
		"""
		return sqlite3.connect(path)

	@staticmethod
	def tables(conn):
		""" Returns the tables in a database
		Arguments
			conn -- Connection
		"""
		c		= conn.cursor()
		c.execute('SELECT name FROM sqlite_master WHERE type=\'table\''  )

		tables	= []
		for row in c:
			table	= row[0]

			# Skip internal sqlite tables
			if table.find('sqlite_') == 0:
				continue

			tables.append( table )

		c.close()
		return tables

	@staticmethod
	def fields(conn, table):
		""" Returns the fields of a table
		Arguments
			conn -- Connection
			table -- Table name
		"""
		c	= conn.cursor()
		c.execute('PRAGMA table_info({0})'.format(table))
		fields	= []
		for row in c:
			fields.append(row)

		c.close()
		return fields

	@staticmethod
	def backup(path):
		""" Creates a backup the database
		Arguments
			path -- Path to the database file
		"""
		backupFile = path+'.bak'

		# Delete the existing backup
		if os.path.exists(backupFile) == True:
			os.remove(backupFile)

		shutil.copyfile(path, backupFile)
		return

	def restore(path):
		""" Restores a database from a backup
		Arguments
			path -- Path to the database file
		"""
		backupFile = path+'.bak'

		if os.path.exists(backupFile) == True:
			if os.path.exists(path) == True:
				os.remove(path)

			shutil.copyfile(backupFile, path)
		else:
			raise Exception('No backup file to restore database from.')
		return

	@staticmethod
	def clear(path):
		""" Deletes all records and vacuum's the database
		Arguments
			path -- Path to the database file
		"""
		conn	= ActiveRecord.connect(path)

		tables	= ActiveRecord.tables(conn)

		for t in tables:
			query	= 'DELETE FROM {}'.format(t)
			c	= conn.cursor()
			c.execute(query)
			c.close()

		# Commit the deletion
		conn.commit()

		c	= conn.cursor()
		c.execute('VACUUM')
		conn.commit()
		c.close()
		return

	def execute_sql( self, sql ):
		""" Executes an SQL command with no result
		Arguments
				sql -- SQL command to execute
		"""
		c	= self.conn.cursor()
		c.execute( sql )
		self.conn.commit()
		c.close()

	def add( self, values ):
		""" Adds values to the database
		Arguments
				values -- Values to add ot the database
		"""
		c		= self.conn.cursor()
		fields	= ','.join(values)
		sql = 'INSERT INTO ' + self.table +' ('+fields+')' + 'VALUES('

		valargs	= []
		for value in values:
			valargs.append( ':'+value )

		sql += ','.join(valargs)
		sql += ')'

		c.execute(sql, values)
		self.conn.commit()
		lastrow = c.lastrowid
		c.close()
		return lastrow


	def update( self, oid, values ):
		""" Updates values of an object
		Arguments
				oid -- Object ID or key field value
			values -- Values to update on the table for the object
		"""
		c		= self.conn.cursor()
		sql = 'UPDATE {} SET '.format(self.table)

		valargs	= []
		for value in values:
			valargs.append( value+'=:'+value )

		sql += ','.join(valargs)
		sql += ' WHERE id=' + str(oid)

		c.execute(sql, values)
		self.conn.commit()
		c.close()

	def get_object_list( self, criteria ):
		""" Returns the ID of objects matching a criteria
		Arguments
				criteria -- Criteria to match for the objects
		"""
		c	= self.conn.cursor()
		c.execute('SELECT id FROM {} WHERE {}'.format(self.table, criteria)  )
		idList	= []
		for row in c:
			idList.append( row[0] )
		return idList

	def get_object_count( self, criteria=None ):
		""" Returns the number of objects matching a criteria
		Arguments
				criteria -- Criteria to match on all objects
		"""
		c	= self.conn.cursor()
		if criteria is None:
			c.execute('SELECT count(id) FROM {}'.format(self.table))
		else:
			c.execute('SELECT count(id) FROM {} WHERE {}'.format(self.table, criteria))

		row	= c.fetchone()
		c.close()
		return row[0]

	def get_object_list_by( self, field, criteria=None ):
		""" Returns the fields of objects matching a criteria
		Arguments
				criteria -- Criteria to match for the objects
		"""
		c	= self.conn.cursor()
		if criteria is None:
			c.execute('SELECT {} FROM {}'.format(field, self.table)  )
		else:
			c.execute('SELECT {} FROM {} WHERE {}'.format(field, self.table, criteria) )

		idList	= []
		for row in c:
			idList.append( row[0] )
		c.close()
		return idList

	def find( self, oid ):
		""" Finds an object with a matching ID
		Arguments
				oid -- Object ID or key field value
		"""
		return (len(self.FindBy('id', oid))!=0)

	def find_by( self, field, value ):
		""" Finds the first object with a matching field and value
		Arguments
				field -- Field to match
			value -- Value of the field to match
		"""
		t   = (value,)
		c	= self.conn.cursor()
		c.execute('SELECT id FROM {} WHERE {}=?'.format(self.table, field), t  )
		idList	= []
		for row in c:
			idList.append( row[0] )
		c.close()
		return idList

	def set( self, oid, field, value ):
		""" Sets the value of the object
		Arguments
				oid -- Object ID or key field value
			field -- Field name
			value -- Field value to update
		"""
		t   = (value,oid)
		c	= self.conn.cursor()
		c.execute('UPDATE {} SET {}=? WHERE id=?'.format(self.table, field), t)
		self.conn.commit()
		c.close()

	def get( self, oid, field ):
		""" Returns the field value of an object
		Arguments
				oid -- Object ID or key field value
			field -- Field to retrieve
		"""
		t   = (oid,)
		c	= self.conn.cursor()
		c.execute('SELECT {} FROM {} WHERE id=?'.format(field, self.table), t)
		row	= c.fetchone()
		if row is None:
			return None
		c.close()
		return row[0]

	def get_by( self, findfield, field, value ):
		""" Returns the list of field value of the all object matching a field an value
		Arguments
				findfield -- Field to retrieve
			field -- Field to match
			value -- Value of the matching field
		"""
		t   = (value,)
		c	= self.conn.cursor()
		c.execute('SELECT {} FROM {} WHERE {}=?'.format(findfield, self.table, field), t  )
		idList	= []
		for row in c:
			idList.append( row[0] )
		c.close()
		return idList

	def get_unique_by( self, findfield, field, value ):
		""" Returns the field value of the first object matching a field an value
		Arguments
				findfield -- Field to retrieve
			field -- Field to match
			value -- Value of the matching field
		"""
		t   = (value,)
		c	= self.conn.cursor()
		c.execute('SELECT {} FROM {} WHERE {}=?'.format(findfield, self.table, field), t  )
		row	= c.fetchone()
		if row is None:
			return None
		c.close()
		return row[0]

	def get_all( self, criteria=None ):
		""" Returns all fields of objects matching a criteria
		Arguments
				criteria -- Criteria to match for the objects
		"""
		c	= self.conn.cursor()
		if criteria is None:
			c.execute('SELECT * FROM {}'.format(self.table)  )
		else:
			c.execute('SELECT * FROM {} WHERE {}'.format(self.table, criteria)  )
		idList	= []
		for row in c:
			idList.append( row )
		c.close()
		return idList


	def delete( self, oid ):
		""" Deletes an object with a matching ID
		Arguments
				oid -- Object ID or key field value
		"""
		c	= self.conn.cursor()
		t = (oid,)
		c.execute('DELETE FROM '+ self.table +' WHERE id IN(?)', t )
		self.conn.commit()
		c.close()


	def delete_by( self, field, value ):
		""" Deletes all objects matching a field and value
		Arguments
				field -- Field to match
			value -- Value of the field to match
		"""
		c	= self.conn.cursor()
		t = (value,)
		c.execute('DELETE FROM {} WHERE {} IN(?)'.format(self.table, field), t )
		self.conn.commit()
		c.close()



if __name__ == '__main__':
    test = ActiveRecord()


