#!/usr/bin/python
# Filename: Builder_test.py
# Description: Test cases for the Builder class

from cos.data.bi.Builder import Builder
import unittest, os, sqlite3

issetup	= False

class BuilderTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		global issetup

		issetup	= False
		
		self.tables	= []
		for n in range(20):
			self.tables.append(f'tbl_{n+1}')

		self.dbs	= []
		for n in range(10):
			self.dbs.append(f'target{n+1}.s3db')
		self.count	= 1000

		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		global issetup
		if issetup is False:
			self.setup_dbs()
			issetup	= True
		return
		
	def tearDown(self):
		return
		
	def delete_db(self, path):
		if os.path.exists(path):
			os.remove(path)

		return

	def create_tables(self, conn, table, numrecords, startid):
		c = conn.cursor()

		c.execute(f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
		
		c.execute('BEGIN TRANSACTION')
		for n in range(numrecords):
			c.execute(f"INSERT INTO {table} VALUES ({n+1}, 'Alice', 'alice@example.com')")
		c.execute('COMMIT')
		return
	
	def create_db(self, path, count, startid):
		self.delete_db(path)
		conn_s = sqlite3.connect(path)
		for t in self.tables:
			self.create_tables( conn_s, t, count, startid)
			conn_s.commit()
		conn_s.close()

	def setup_dbs(self):
		# Create dummy databases and tables for the example
		# Source DB
		self.create_db('source.s3db', self.count, 1)

		# Target DB (create the table structure but no data yet)
		for tgt in self.dbs:
			self.create_db(tgt, 0, 1)
		return

	def test_01_copy_data(self):
		b = Builder()
		for tgt in self.dbs:
			b.copy_data('source.s3db', tgt, self.tables)
		return

	def test_02_partition(self):
		b = Builder()
		b.process(self.dbs)
		return

	def test_03_merge(self):
		self.create_db('merge.s3db', 0, 1)

		b = Builder()
		b.merge('merge.s3db', self.dbs, self.tables)
		return

if __name__ == '__main__':
    unittest.main()
