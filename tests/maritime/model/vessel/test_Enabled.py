#!/usr/bin/python
# Filename: test_Enabled.py
# Description: Test cases for switching vessel instances off with vessels.enabled (REQ.035)

import os, shutil, sqlite3, tempfile, unittest
from unittest import mock

from cos.core.simulation.Builder import Builder as BaseBuilder
from cos.core.utilities.ActiveRecord import ActiveRecord
from cos.behavior.motion.FleetBehavior import FleetBehavior
from maritime.model.vessel.Builder import Builder
from maritime.core.situation.VesselFilter import VesselFilter

ROOT	= os.path.abspath( os.path.join(os.path.dirname(__file__), '..', '..', '..', '..') )
SOURCE	= os.path.join( ROOT, 'config', 'simulation', 'tk', 'turkeli', 'vessel.s3db' )
POWER	= (100000, 'maritime.model.vessel.PowerDrivenVessel')


def context():
	ctxt	= mock.Mock()
	ctxt.sim	= mock.Mock( spec=['log', 'fs', 'config', 'objects'] )
	ctxt.sim.config.resolve.side_effect	= lambda p: p
	return ctxt


class EnabledTestCase(unittest.TestCase):
	def setUp(self):
		self.dir	= tempfile.mkdtemp()
		self.path	= os.path.join( self.dir, 'vessel.s3db' )
		shutil.copy( SOURCE, self.path )
		self.db		= sqlite3.connect( self.path )
		Builder.audited.discard( self.path )

	def tearDown(self):
		self.db.close()
		shutil.rmtree( self.dir )

	def disable(self, *names):
		self.db.executemany( 'update vessels set enabled=0 where name=?', [(n,) for n in names] )
		self.db.commit()

	def test_base_builder_keeps_the_plain_type_filter(self):
		b	= BaseBuilder( 'Builder/Land', 'MOUNTAIN', 'land', 'isohypses', {'MOUNTAIN': (100000, 'x')} )
		self.assertEqual( b.criteria((100000, 'x')), 'type=100000' )

	def test_vessel_builder_loads_only_enabled_rows(self):
		self.disable( 'True North' )
		criteria	= Builder( {'Type': 'POWER_DRIVEN'} ).criteria( POWER )
		self.assertEqual( criteria, 'type=100000 AND enabled=1' )
		names		= [ r[1] for r in ActiveRecord.create('vessel', self.path, 'vessels').get_all(criteria) ]
		self.assertNotIn( 'True North', names )
		self.assertIn( 'MSC NICOLA MASTRO', names )
		self.assertEqual( len(names), self.db.execute('select count(*) from vessels where type=100000').fetchone()[0] - 1 )

	def test_audit_records_and_logs_disabled_vessels(self):
		self.disable( 'X100', 'X101' )
		ctxt	= context()
		Builder.audit( ctxt, self.path )
		self.assertEqual( sorted(v.name for v in ctxt.sim.disabled_vessels.values()), ['X100', 'X101'] )
		self.assertTrue( all(v.recid is not None for v in ctxt.sim.disabled_vessels.values()) )
		self.assertIn( '2 vessel(s) disabled: X100, X101', ctxt.log.info.call_args[0][1] )

	def test_disabled_controller_warns_about_its_members(self):
		self.disable( 'PATROL 1' )
		guids	= [ r[0] for r in self.db.execute("select guid from vessels where name in ('FLEET100','FLEET101')") ]
		ctxt	= context()
		ctxt.sim.fs.read_file.return_value	= 'id,guid,type\n' + ''.join( f'1,{g},100000,\n' for g in guids )
		Builder.audit( ctxt, self.path )
		warning	= ' '.join( c[0][1] for c in ctxt.log.warning.call_args_list )
		self.assertIn( 'fleet controller PATROL 1 is disabled', warning )
		self.assertIn( 'FLEET100', warning )

	def test_database_without_the_column_is_reported(self):
		self.db.execute( 'alter table vessels drop column enabled' )
		self.db.commit()
		ctxt	= context()
		Builder.audit( ctxt, self.path )
		self.assertIn( 'no enabled column', ctxt.log.error.call_args[0][1] )
		with self.assertRaises( sqlite3.OperationalError ):
			ActiveRecord.create( 'vessel', self.path, 'vessels' ).get_all( 'type=100000 AND enabled=1' )

	def test_enabled_accepts_only_zero_and_one(self):
		with self.assertRaises( sqlite3.IntegrityError ):
			self.db.execute( "update vessels set enabled=2 where name='X100'" )

	def test_disabled_fleet_member_is_logged_as_info_not_error(self):
		sim		= mock.Mock()
		sim.objects.find.return_value	= None
		sim.disabled_vessels	= {'guid-off': mock.Mock()}
		fleet	= FleetBehavior( None, {} )
		fleet.vehicle	= mock.Mock()
		fleet.members	= [ ('guid-off', 100000), ('guid-missing', 100000) ]
		fleet.resolve( sim )
		self.assertIn( 'disabled', sim.log.info.call_args[0][1] )
		self.assertIn( 'guid-missing', sim.log.error.call_args[0][1] )
		self.assertEqual( sim.log.error.call_count, 1 )

	def test_disabled_vessel_under_test_gets_a_clear_problem(self):
		f	= VesselFilter()
		f.source, f.entries	= 'undertest.yaml', [ {'name': 'X100'} ]
		off	= mock.Mock( id='g', recid=1, imo='1', mmsi='1' )
		off.name	= 'X100'
		problems	= f.resolve( [], [off] )
		self.assertEqual( len(problems), 1 )
		self.assertIn( 'names X100, which is disabled', problems[0] )


if __name__ == '__main__':
	unittest.main()
