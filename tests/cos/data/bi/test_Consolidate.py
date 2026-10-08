#!/usr/bin/python
# Filename: test_Consolidate.py
# Description: Test cases for Builder's partition and merge, and the cmerge tool (REQ.021)

from cos.data.bi.Builder import Builder
from cos.data.bi.Metadata import Metadata

import unittest, os, sys, sqlite3, tempfile, shutil, hashlib

ROOT	= os.path.abspath( os.path.join(os.path.dirname(__file__), '..', '..', '..', '..') )
sys.path.insert( 0, os.path.join(ROOT, 'tools', 'data', 'cmerge') )
from app import CMergeApp

SCHEMA	= [
	'CREATE TABLE dim_vessel (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)',
	'CREATE TABLE fact_concern (dim_gps_id INTEGER, dim_vessel_id INTEGER, dim_port_id INTEGER, id INTEGER PRIMARY KEY AUTOINCREMENT, case_id INTEGER, vessel_id INTEGER, penalty REAL)',
	'CREATE TABLE CONCERN_KIND (id INTEGER PRIMARY KEY, name TEXT)',
	'CREATE TABLE configs (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(64), type VARCHAR(32), value VARCHAR(128))',
	"INSERT INTO CONCERN_KIND VALUES (1, 'safety')",
]

MORTON	= 1152921504606846975 - 12345		# Near the top of the 60-bit range

def create(path, rows, case, extra=None):
	""" A run database with the given fact_concern rows
	Arguments
		path -- Database path
		rows -- Number of rows
		case -- case_id written into every row
		extra -- Optional extra column added to fact_concern
	"""
	conn	= sqlite3.connect( path )
	for sql in SCHEMA:
		conn.execute( sql )
	if extra:
		conn.execute( f'ALTER TABLE fact_concern ADD COLUMN {extra} TEXT' )
	conn.execute( "INSERT INTO configs (name, type, value) VALUES ('run.case', 'run', ?)", (str(case),) )
	for n in range(rows):
		conn.execute( 'INSERT INTO fact_concern (dim_gps_id, dim_vessel_id, dim_port_id, case_id, vessel_id, penalty) VALUES (?,?,?,?,?,?)',
					  (MORTON, 9713076, 1, case, 9713076, float(n)) )
	conn.commit()
	conn.close()
	return path

def digest(path):
	with open(path, 'rb') as f:
		return hashlib.md5( f.read() ).hexdigest()


class ConsolidateTestCase(unittest.TestCase):
	def setUp(self):
		self.dir	= tempfile.mkdtemp()
		self.template	= create( os.path.join(self.dir, 'template.s3db'), 0, 0 )
		self.runs	= [ create(os.path.join(self.dir, f'run{k}.s3db'), 5, 1000+k) for k in range(3) ]
		self.list	= os.path.join( self.dir, 'runs.txt' )
		with open(self.list, 'w') as f:
			f.write( '# sweep\n' + '\n'.join(os.path.basename(r) for r in self.runs) + '\n\n' )
		return

	def tearDown(self):
		shutil.rmtree( self.dir, ignore_errors=True )
		return

	def app(self):
		app	= CMergeApp()
		app.template	= self.template
		app.output	= os.path.join( self.dir, 'out.s3db' )
		return app

	def test_only_surrogate_keys_are_renumbered(self):
		conn	= sqlite3.connect( self.runs[0] )
		self.assertEqual( Metadata.get_id_fields(conn, 'fact_concern'), ['id', 'dim_port_id'] )
		conn.close()

	def test_merge_keeps_natural_dimension_keys(self):
		self.assertEqual( self.app().run(self.list), 0 )
		out		= sqlite3.connect( os.path.join(self.dir, 'out.s3db') )
		rows	= set( out.execute('SELECT dim_gps_id, dim_vessel_id FROM fact_concern') )
		ports	= { r[0] for r in out.execute('SELECT DISTINCT dim_port_id FROM fact_concern') }
		out.close()
		self.assertEqual( rows, {(MORTON, 9713076)} )
		self.assertEqual( len(ports), 3 )			# surrogate keys are still renumbered per run

	def test_merge_keeps_identity_and_sources(self):
		before	= [ digest(r) for r in self.runs ]
		self.assertEqual( self.app().run(self.list), 0 )
		self.assertEqual( before, [digest(r) for r in self.runs] )

		out		= sqlite3.connect( os.path.join(self.dir, 'out.s3db') )
		n, ids	= out.execute( 'SELECT count(*), count(DISTINCT id) FROM fact_concern' ).fetchone()
		self.assertEqual( (n, ids), (15, 15) )
		self.assertEqual( {r[0] for r in out.execute('SELECT DISTINCT case_id FROM fact_concern')}, {1000, 1001, 1002} )
		self.assertEqual( {r[0] for r in out.execute('SELECT DISTINCT vessel_id FROM fact_concern')}, {9713076} )
		self.assertEqual( out.execute('SELECT count(*) FROM CONCERN_KIND').fetchone()[0], 1 )
		out.close()

	def test_configs_are_not_merged(self):
		self.assertEqual( self.app().run(self.list), 0 )
		out		= sqlite3.connect( os.path.join(self.dir, 'out.s3db') )
		rows	= out.execute( 'SELECT name, type, value FROM configs' ).fetchall()
		out.close()
		self.assertEqual( rows, [('run.case', 'run', '0')] )		# the template's row, no run's

	def test_copies_by_column_name(self):
		create( os.path.join(self.dir, 'wide.s3db'), 2, 7, extra='note' )
		with open(self.list, 'a') as f:
			f.write( 'wide.s3db\n' )
		self.assertEqual( self.app().run(self.list), 1 )		# the dropped column is reported

	def test_refuses_existing_output_and_repeats(self):
		app	= self.app()
		open( app.output, 'w' ).close()
		with self.assertRaises( SystemExit ):
			app.run( self.list )

		os.remove( app.output )
		with open(self.list, 'a') as f:
			f.write( os.path.basename(self.runs[0]) + '\n' )
		with self.assertRaises( SystemExit ):
			app.run( self.list )


if __name__ == '__main__':
	unittest.main()
