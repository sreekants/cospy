#!/usr/bin/python
# Filename: test_WorkingSet.py
# Description: Test cases for the working set being recreated from its template every run (COS.033)

from cos.subsystem.data.DataManager import DataManager

import unittest, os, sqlite3, tempfile, shutil


def columns(path, table):
	with sqlite3.connect( path ) as db:
		return [ r[1] for r in db.execute(f'PRAGMA table_info({table})') ]


class WorkingSetTestCase(unittest.TestCase):
	def setUp(self):
		self.dir		= tempfile.mkdtemp()
		self.template	= os.path.join( self.dir, 'maritime.s3db' )
		self.storage	= os.path.join( self.dir, 'maritime.workingset.s3db' )
		with sqlite3.connect( self.template ) as db:
			db.execute( 'CREATE TABLE fact_rb (id INTEGER PRIMARY KEY AUTOINCREMENT, case_id INTEGER, imo TEXT)' )
			db.execute( 'INSERT INTO fact_rb (case_id, imo) VALUES (1, "9627837")' )

	def tearDown(self):
		shutil.rmtree( self.dir )

	def init(self, storage=None):
		dm			= DataManager.__new__( DataManager )
		dm.storage	= storage or self.storage
		dm._DataManager__init_database( {'rowstart': '1000'} )

	def test_missing_working_set_is_created(self):
		self.init()
		self.assertEqual( columns(self.storage, 'fact_rb'), ['id', 'case_id', 'imo'] )

	def test_stale_working_set_takes_the_template_schema(self):
		with sqlite3.connect( self.storage ) as db:
			db.execute( 'CREATE TABLE fact_rb (id INTEGER PRIMARY KEY AUTOINCREMENT, case_id INTEGER)' )
		open( self.storage + '-journal', 'w' ).close()
		self.init()
		self.assertEqual( columns(self.storage, 'fact_rb'), ['id', 'case_id', 'imo'] )
		self.assertFalse( os.path.exists(self.storage + '-journal') )

	def test_fact_tables_start_empty(self):
		self.init()
		with sqlite3.connect( self.storage ) as db:
			self.assertEqual( db.execute('select count(*) from fact_rb').fetchone()[0], 0 )

	def test_template_is_never_its_own_working_set(self):
		self.init( self.template )
		self.assertTrue( os.path.exists(self.template) )
		self.assertEqual( columns(self.template, 'fact_rb'), ['id', 'case_id', 'imo'] )


if __name__ == '__main__':
	unittest.main()
