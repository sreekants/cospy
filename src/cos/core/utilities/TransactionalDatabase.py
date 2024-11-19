#!/usr/bin/python
# Filename: TransactionalDatabase.py
# Description: Utility class to process SQLite records in a transactional batches

from cos.core.utilities.ActiveRecord import ActiveRecord

class TransactionalDatabase:
	def __init__(self, txn_batch=400):
		""" Constructor
		Arguments
			txn_batch -- Records queued befor a commit
		"""
		self.pending_txn	= 0
		self.conn			= None
		self.cursor			= None
		self.batch_size		= txn_batch
		return


	def open(self, path, conn=None):
		""" Opens a database connection
		Arguments
			path -- Path of the database
			conn -- Reference to an open connection (optional)
		"""
		self.close()

		# Open the database and create a cursor
		self.pending_txn	= 0

		if conn is not None:
			self.conn	= conn
		else:
			self.conn	= ActiveRecord.connect(path)

		self.cursor		= self.conn.cursor()


		# Set isolation level to enable transactions
		# this impcoses the speed of addition to the
		# table.
		self.conn.isolation_level = None
		return

	def close(self):
		""" Closes the database connection
		Arguments
			self -- reference to this instance
		"""
		if self.cursor == None:
			return False

		# flush pending transactions
		self.flush()

		# Close the cursor
		self.cursor.close()

		self.pending_txn	= 0
		self.conn			= None
		self.cursor			= None
		return

	def is_open(self):
		""" Checks if the database is open
		Arguments
			self -- reference to this instance
		"""
		return (self.cursor is not None)

	@property
	def pending(self):
		""" Returns the number of pending bytes:
		Arguments
			self -- reference to this instance
		"""
		return (self.pending_txn != 0)


	def begin(self):
		""" Starts a transaction
		Arguments
			self -- reference to this instance
		"""
		self.cursor.execute( 'BEGIN TRANSACTION' )
		return

	def commit(self):
		""" Commits a transaction.
		Arguments
			self -- reference to this instance
		"""
		self.cursor.execute( 'COMMIT' )

		# Reset the queue txn count.
		self.pending_txn	= 0
		return

	def execute_sql(self, sql):
		""" Executes and SQL query on the database
		Arguments
			self -- reference to this instance
			sql -- Query to execute
		"""
		self.__sync()
		self.cursor.execute( sql )
		return

	def add( self, table, values ):
		""" Adds values to the database
		Arguments
			self -- reference to this instance
			values -- Map of key-values to add to the database
		"""
		self.__sync()

		fields	= ','.join(values)
		sql 	= 'INSERT INTO ' + table +' ('+fields+')' + ' VALUES('

		valargs	= []
		for value in values:
			valargs.append( ':'+value )

		sql += ','.join(valargs)
		sql += ')'

		self.cursor.execute(sql, values)
		return

	def addkv( self, table, keys, values ):
		""" Adds values to the database
		Arguments
			self -- reference to this instance
			keys -- Keys to add to the database
			values -- Values to add to the database
		"""
		self.__sync()

		fields	= ','.join(keys)
		sql 	= 'INSERT INTO ' + table +' ('+fields+')' + ' VALUES('

		sql += ','.join(values)
		sql += ')'

		self.cursor.execute(sql)
		return


	def flush(self):
		""" Flushes pending bytes into the storage system
		Arguments
			self -- reference to this instance
		"""
		if self.pending_txn == 0:
			return

		self.commit()
		return

	def __sync(self):
		""" Synchronizes the state of the queue
		Arguments
			self -- reference to this instance
		"""
		if self.pending_txn == 0:
			self.begin()

		self.pending_txn	+=1

		if self.pending_txn	> self.batch_size:
			self.flush()

		return

if __name__ == '__main__':
	test = TransactionalDatabase()


