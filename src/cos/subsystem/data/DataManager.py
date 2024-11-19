#!/usr/bin/python
# Filename: DataManager.py
# Description: Implementation of the datamanager subsystem

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Subsystem import Subsystem
from cos.core.kernel.Context import Context
from cos.subsystem.data.Partition import Partition
from cos.core.utilities.ArgList import ArgList
from cos.core.utilities.TransactionalDatabase import TransactionalDatabase
from cos.core.utilities.ActiveRecord import ActiveRecord

import os, time
from xml.dom import minidom

class DataManagerThread(SimulationThread):
	def __init__(self, sim):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
		"""
		SimulationThread.__init__(self, sim)
		self.running	= True
		self.ticktime	= 5		# Ticks every .3 seconds
		return

	def run(self):
		""" Runs the data manager loop
		"""
		# sim.objects.dump()
		time.sleep(self.ticktime)		# Delayed start

		while self.running:
			self.sim.data.flush()
			time.sleep(self.ticktime)
		return


	def stop(self):
		""" Stops the simulation
		"""
		self.running	= False
		return

class DataManager(Subsystem):
	def __init__(self):
		""" Constructor
		"""
		Subsystem.__init__(self, "Kernel", "DataManager")
		self.thread		= None
		self.partitions	= {}
		self.storage	= None
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		Subsystem.on_init(self, ctxt, module)

		config	= ArgList( module.get("config", "") )
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
		self.flush()
		return


	def push(self, topic, data):
		""" Posts amessage to an IPC topic
		Arguments
			topic -- IPC topic
			data -- Message payload
		"""
		partition	= self.partitions.get(topic, None)
		if partition is not None:
			partition.add( data )
		return

	def flush(self):
		""" Flushes all the cached data to the file system.
		"""
		if self.storage is None:
			return

		db		= TransactionalDatabase()
		db.open( self.storage )

		for p in self.partitions.values():
			p.flush(db)

		db.flush()
		db.close()
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

			for topic, fields in topics.items():
				self.partitions[topic]	= Partition( topic, fields )
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

		for f in facts.getElementsByTagName('Fact'):
			table		= f.getElementsByTagName('TableName')[0].childNodes[0].nodeValue
			measures	= f.getElementsByTagName('Measure')

			fields		= []
			for m in measures:
				field	= m.getElementsByTagName('FieldName')[0].childNodes[0].nodeValue
				type	= m.getElementsByTagName('Type')[0].childNodes[0].nodeValue
				fields.append(field)

			topics[table]	= fields

		'''
		#TODO: REMOVE
		table			= 'fact_call'
		fields			= ['dim_trader_id','audit_status','caller_id']
		topics[table]	= fields
		'''

		return topics

if __name__ == "__main__":
	test = DataManager()


