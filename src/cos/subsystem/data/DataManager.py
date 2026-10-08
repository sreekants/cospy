#!/usr/bin/python
# Filename: DataManager.py
# Description: Implementation of the datamanager subsystem

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Subsystem import Subsystem
from cos.core.kernel.Context import Context
from cos.subsystem.data.Partition import Partition, AUDIT_FIELDS
from cos.core.utilities.ArgList import ArgList
from cos.core.utilities.TransactionalDatabase import TransactionalDatabase
import sqlite3, sys
from cos.core.utilities.ActiveRecord import ActiveRecord
from cos.core.time.Clock import utcnow

import os, time, shutil, threading
from xml.dom import minidom

# Where the test inspector owning the vessels-under-test filter is published, if one is loaded
FILTER_PATH	= '/Faculty/Practice/Inspectors'

BACKLOG			= 100000	# Records held in memory before a failed flush is reported as an error
FINAL_WAIT		= 60.0		# Seconds the last flush of a run waits for a reader to release the store

class DataManagerThread(SimulationThread):
	def __init__(self, sim):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
		"""
		SimulationThread.__init__(self, sim)
		self.running	= True
		self.ticktime	= 5		# Seconds between flushes
		self.wakeup		= threading.Event()		# Cuts the wait short on stop
		return

	def run(self):
		""" Runs the data manager loop
		"""
		self.wakeup.wait(self.ticktime)		# Delayed start

		while self.running:
			self.sim.data.flush()
			self.wakeup.wait(self.ticktime)
		return


	def stop(self):
		""" Stops the simulation
		"""
		self.running	= False
		self.wakeup.set()
		return

class DataManager(Subsystem):
	def __init__(self):
		""" Constructor
		"""
		Subsystem.__init__(self, "Kernel", "DataManager")
		self.thread		= None
		self.partitions	= {}
		self.storage	= None
		self.trace		= False
		self.filter		= None		# Telemetry filter, found at the first push
		self.filtered	= {}		# Topic -> rows withheld by the filter
		self.backlog	= BACKLOG	# Error threshold on records held after failed flushes
		self.over		= False		# The backlog is above the threshold
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		Subsystem.on_init(self, ctxt, module)

		config	= ArgList( module.get("config", "") )
		if 'backlog' in config:
			self.backlog	= int( config['backlog'] )
		self.__build_partitions( ctxt, config )
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Subsystem.on_timer( self, ctxt, unused )
		return

	def on_start(self, ctxt:Context, unused):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Subsystem.on_start( self, ctxt, unused )
		ctxt.sim.data	= self
		self.thread		= DataManagerThread(ctxt.sim)
		self.thread.start()
		return

	def on_stop(self, ctxt:Context, unused):
		""" Callback for simulation shutdown
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Subsystem.on_stop( self, ctxt, unused )
		self.thread.stop()
		self.thread.join()
		self.flush( final=True )

		for topic, count in sorted( self.filtered.items() ):
			ctxt.log.info( 'DataManager', f'{count} row(s) of {topic} withheld: no vessel under test' )
		return


	def abort(self):
		""" Stops the flush thread and writes out everything cached so far
		"""
		if self.thread is not None:
			self.thread.stop()
			self.thread.join()
		self.flush( final=True )
		return

	def push(self, topic, data, context=None):
		""" Posts amessage to an IPC topic
		Arguments
			topic -- IPC topic
			data -- Message payload
			context -- DataContext filling the table's dimension columns; None leaves them NULL
		"""
		partition	= self.partitions.get(topic, None)
		if partition is None:
			self.sim.log.error( 'DataManager', f'Failed to push data to topic {topic}: No such topic' )
			return

		# A wrong-width row would raise in the flush thread and stop all writes
		if len(data) != partition.width:
			self.sim.log.error( 'DataManager', f'Failed to push data to topic {topic}: '
								f'payload has {len(data)} values, schema expects {partition.width}' )
			return

		if self.keeps( topic, partition, data ) == False:
			self.filtered[topic]	= self.filtered.get( topic, 0 ) + 1
			return

		partition.add( utcnow(), self.sim.tickcount(), data, context )
		return

	def record_run(self, rows):
		""" Writes the run record into the working set's configs table, replacing rows of the same name
		Arguments
			rows -- List of (name, type, value)
		"""
		conn	= ActiveRecord.connect( self.storage )
		try:
			conn.executemany( 'DELETE FROM configs WHERE name = ?', [ (r[0],) for r in rows ] )
			conn.executemany( 'INSERT INTO configs (name, type, value) VALUES (?, ?, ?)', rows )
			conn.commit()
		finally:
			conn.close()
		return

	def keeps(self, topic, partition, data)->bool:
		""" Whether a row passes the vessels-under-test filter (REQ.024)
		Arguments
			topic -- Fact table
			partition -- Its partition
			data -- Payload
		"""
		if self.filter is None:
			self.filter	= False
			for handle in self.sim.objects.get_all( FILTER_PATH ):
				candidate	= getattr( handle, 'filter', None )
				if hasattr( candidate, 'keeps' ):
					self.filter	= candidate
					break

		if self.filter is False:
			return True

		return self.filter.keeps( topic, partition.fields[AUDIT_FIELDS:], data )

	def flush(self, final:bool=False):
		""" Writes every queued record in one transaction; on failure requeues them for the next flush
		Arguments
			final -- The run's last flush, which waits for a reader instead of requeueing
		"""
		if self.storage is None:
			return

		taken	= [ (p, recs) for p, recs in ((p, p.take()) for p in self.partitions.values()) if recs ]
		if not taken:
			return

		conn	= None
		try:
			conn	= sqlite3.connect( self.storage, timeout=FINAL_WAIT if final else 0.0 )	# never wait on a reader mid-run
			db		= TransactionalDatabase( txn_batch=sys.maxsize )	# one commit per flush, so a failure leaves nothing behind
			db.open( self.storage, conn )
			count	= sum( p.write(db, recs) for p, recs in taken )
			db.close()
		except Exception as e:
			if (conn is not None) and conn.in_transaction:
				conn.execute( 'ROLLBACK' )
			for p, recs in taken:
				p.restore( recs )
			self.report( e, final )
			return
		finally:
			if conn is not None:
				conn.close()

		if self.over and (self.queued() <= self.backlog):
			self.over	= False
			self.sim.log.info( 'DataManager', f'Backlog cleared; {self.queued()} record(s) queued' )
		if self.trace == True:
			self.sim.log.info( 'DataManager', f'Flushed {count} record(s) into {len(taken)} table(s).' )
		return

	def queued(self)->int:
		""" Records held in memory, waiting to be written
		"""
		return sum( p.records.qsize() for p in self.partitions.values() )

	def report(self, e, final:bool):
		""" Reports a failed flush once the backlog passes its threshold, and always at the end of a run
		Arguments
			e -- The exception
			final -- The run's last flush failed, so the queued records are lost
		"""
		held	= self.queued()
		if final:
			self.sim.log.error( 'DataManager', f'Last flush failed, {held} record(s) not written: {e}' )
		elif (held > self.backlog) and (self.over == False):
			self.over	= True
			self.sim.log.error( 'DataManager', f'{held} record(s) held in memory, above the backlog limit {self.backlog}: {e}' )
		return

	def __build_partitions(self, ctxt:Context, config):
		""" Builds partitions for the data streams
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		try:
			topics			= self.__build_topics(ctxt, config)
			self.storage	= ctxt.sim.config.resolve( config["storage"] )

			self.__init_database(config)

			for topic, (fields, dimensions) in topics.items():
				self.partitions[topic]	= Partition( ctxt, topic, fields, dimensions )
		except Exception as e:
			ctxt.log.error( 'DataManager', f'Failed to initialize: {str(e)}' )

		return

	def __init_database(self, config, startrow=None):
		""" Initializes the database
		Arguments
			config -- Configuration attributes
			startrow -- Sets the initial row index for each table.
		"""
		if startrow == None:
			startrow	= int(config['rowstart'])

		# Recreate the working set from the template every run so schema changes always reach it
		template = self.storage.replace( 'workingset.', '' )
		if template != self.storage:
			for path in (self.storage, self.storage + '-journal'):
				if os.path.exists(path):
					os.remove(path)
			shutil.copy( template, self.storage )

		conn	= ActiveRecord.connect(self.storage)

		tables	= ActiveRecord.tables(conn)

		for t in tables:
			if t.startswith('fact_') == False:
				continue

			c	= conn.cursor()
			c.execute(f"DELETE FROM {t}")
			c.execute(f"UPDATE SQLITE_SEQUENCE SET seq = {startrow} WHERE name = '{t}'")
			c.close()

		# Commit the deletion
		conn.commit()

		c	= conn.cursor()
		c.execute('VACUUM')
		conn.commit()
		c.close()
		return

	def __build_topics(self, ctxt:Context, config ):
		""" Builds topics for each data stream
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		file		= ctxt.sim.config.resolve(config["schema"])
		metadata	= ctxt.sim.fs.read_file(file)
		topics		= {}
		schema		= minidom.parseString( metadata )
		facts		= schema.getElementsByTagName('Facts')[0]
		columns		= DataManager.dimension_columns( schema )

		for f in facts.getElementsByTagName('Fact'):
			table		= f.getElementsByTagName('TableName')[0].childNodes[0].nodeValue
			measures	= f.getElementsByTagName('Measure')

			fields		= []
			for m in measures:
				field	= m.getElementsByTagName('FieldName')[0].childNodes[0].nodeValue
				type	= m.getElementsByTagName('Type')[0].childNodes[0].nodeValue
				fields.append(field)

			dimensions	= []
			for path in DataManager.declared_dimensions( f ):
				column	= columns.get( path )
				if column is None:
					ctxt.log.warning( 'DataManager', f'{table}: dimension {path} is not defined in the schema; not filled' )
					continue
				dimensions.append( (path.split('.')[-1], column) )

			topics[table]	= (fields, dimensions)

		'''
		#TODO: REMOVE
		table			= 'fact_call'
		fields			= ['dim_trader_id','audit_status','caller_id']
		topics[table]	= fields
		'''

		return topics

	@staticmethod
	def declared_dimensions(fact)->list:
		""" Dimension paths a fact declares, e.g. ['Location.gps', 'Fleet.vessel']
		Arguments
			fact -- <Fact> element
		"""
		for node in fact.childNodes:
			if (node.nodeType == node.ELEMENT_NODE) and (node.tagName == 'Dimensions'):
				text	= ''.join( c.nodeValue for c in node.childNodes if c.nodeType == c.TEXT_NODE )
				return [ p.strip() for p in text.split(';') if p.strip() ]
		return []

	@staticmethod
	def dimension_columns(schema)->dict:
		""" Maps every 'Root.leaf' dimension path to its fact column, e.g. 'Location.gps' -> 'dim_gps_id'
		Arguments
			schema -- Parsed schema document
		"""
		def child(node, tag):
			return next( (c for c in node.childNodes if c.nodeType == c.ELEMENT_NODE and c.tagName == tag), None )

		def text(node, tag):
			c	= child( node, tag )
			return c.firstChild.nodeValue.strip() if (c is not None) and (c.firstChild is not None) else ''

		def walk(root, node, out):
			out[f'{root}.{text(node, "Name")}']	= text( node, 'TableName' ) + '_id'
			leaves	= child( node, 'Leaves' )
			for d in ([] if leaves is None else leaves.childNodes):
				if (d.nodeType == d.ELEMENT_NODE) and (d.tagName == 'Dimension'):
					walk( root, d, out )

		out		= {}
		top		= child( schema.documentElement, 'Dimensions' )
		for d in ([] if top is None else top.childNodes):
			if (d.nodeType == d.ELEMENT_NODE) and (d.tagName == 'Dimension'):
				walk( text( d, 'Name' ), d, out )
		return out

if __name__ == "__main__":
	test = DataManager()


