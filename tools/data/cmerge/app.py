#!/usr/bin/python
# Filename: app.py
# Description: Implementation of the singleton CMergeApp application

from cos.data.bi.Builder import Builder
from cos.data.bi.Metadata import Metadata
from cos.core.utilities.ActiveRecord import ActiveRecord

import os, sys, shutil, sqlite3, tempfile

ROOT		= os.path.abspath( os.path.join(os.path.dirname(__file__), '..', '..', '..') )
TEMPLATE	= os.path.join( ROOT, 'config', 'data', 'maritime.s3db' )
OUTPUT		= 'maritime.consolidated.s3db'

class CMergeApp:
	def __init__(self):
		self.template	= TEMPLATE
		self.output		= OUTPUT
		self.force		= False
		return

	def run(self, listfile):
		""" Merges the run databases named in listfile into a fresh replica of the template
		Arguments
			listfile -- Text file, one run database path per line
		Returns
			0 on success, 1 when any file or table could not be merged
		"""
		files	= self.read_list( listfile )
		self.check( files )
		self.replicate()

		staging	= tempfile.mkdtemp( prefix='cmerge.', dir=os.path.dirname(os.path.abspath(self.output)) )
		try:
			staged	= self.stage( files, staging )
			tables	= self.tables( self.output )

			builder	= Builder()
			builder.process( staged )		# Renumbers the copies, never the sources
			outcomes	= builder.merge( self.output, staged, tables )
		finally:
			shutil.rmtree( staging, ignore_errors=True )

		return self.report( files, outcomes )

	def read_list(self, listfile):
		""" Run database paths from listfile, relative paths taken from its folder
		Arguments
			listfile -- Text file, one path per line; blank lines and # comments skipped
		"""
		base	= os.path.dirname( os.path.abspath(listfile) )
		files	= []
		with open( listfile ) as f:
			for line in f:
				line	= line.strip()
				if line == '' or line.startswith('#'):
					continue
				files.append( os.path.normpath(os.path.join(base, line)) )
		return files

	def check(self, files):
		""" Refuses an empty list, a missing or repeated file, or an output that exists
		Arguments
			files -- Run database paths
		"""
		if not files:
			self.fail( 'the list names no databases' )

		seen	= set()
		for f in files:
			if not os.path.isfile(f):
				self.fail( f'no such database: {f}' )
			real	= os.path.realpath(f)
			if real in seen:
				self.fail( f'listed twice: {f}' )
			seen.add( real )

		if not os.path.isfile(self.template):
			self.fail( f'no template database: {self.template}' )
		if os.path.exists(self.output) and not self.force:
			self.fail( f'{self.output} exists; use -f to replace it' )
		return

	def replicate(self):
		""" Creates the output as an empty replica of the template
		"""
		shutil.copyfile( self.template, self.output )

		conn	= sqlite3.connect( self.output )
		for table in self.tables( self.output ):
			conn.execute( f'DELETE FROM "{table}"' )
		conn.execute( 'DELETE FROM sqlite_sequence' )
		conn.commit()
		conn.execute( 'VACUUM' )
		conn.close()
		return

	def stage(self, files, staging):
		""" Copies each run database into staging, so the sources are never written
		Arguments
			files -- Run database paths
			staging -- Scratch folder
		"""
		staged	= []
		for index, f in enumerate(files, start=1):
			copy	= os.path.join( staging, f'{index:06d}.s3db' )
			shutil.copyfile( f, copy )
			staged.append( copy )
		return staged

	@staticmethod
	def tables(path):
		""" The data tables of a database: every table but enumerations
		Arguments
			path -- Database path
		"""
		conn	= sqlite3.connect( path )
		tables	= [ t for t in ActiveRecord.tables(conn) if not Metadata.is_enumuration(t) ]
		conn.close()
		return tables

	def report(self, files, outcomes):
		""" Prints one line per file and every note; returns the exit code
		Arguments
			files -- Run database paths, in the order merged
			outcomes -- (staged file, rows, notes) per file, from Builder.merge
		"""
		status	= 0
		total	= 0
		for source, (staged, rows, notes) in zip( files, outcomes ):
			count	= sum( rows.values() )
			total	+= count
			print( f'{count:>10} rows  {len(rows):>4} tables  {source}' )
			for note in notes:
				print( f'{"":>10}       {note}' )
				if 'absent from target' in note or 'not copied' in note:
					status	= 1

		print( f'{total:>10} rows from {len(files)} databases into {self.output}' )
		return status

	@staticmethod
	def fail(message):
		""" Stops with an error before anything is written
		Arguments
			message -- Reason
		"""
		print( f'cmerge: {message}', file=sys.stderr )
		sys.exit( 2 )


if __name__ == "__main__":
	test = CMergeApp()
