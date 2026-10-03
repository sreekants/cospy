#!/usr/bin/python
# Filename: test_Partition.py
# Description: Test cases for the audit fields a Partition writes (COS.024)

import datetime, types, unittest

from cos.subsystem.data.Partition import Partition, AUDIT_FIELDS, AUDIT_REGISTER
from cos.core.time.Clock import utcnow

FIELDS	= ['creation_time', 'audit_status', 'case_id', 'tick', 'report_time', 'value']


class DB:
	def __init__(self):
		self.rows	= []
	def addkv(self, table, fields, values):
		self.rows.append( dict(zip(fields, values)) )


class PartitionTestCase(unittest.TestCase):
	def setUp(self):
		ctxt			= types.SimpleNamespace( sim=types.SimpleNamespace(case_id=42) )
		self.partition	= Partition( ctxt, 'fact_test', FIELDS )
		self.db			= DB()

	def test_callers_leave_out_the_four_audit_fields(self):
		self.assertEqual( AUDIT_FIELDS, 4 )
		self.assertEqual( self.partition.width, 2 )

	def test_row_carries_the_tick_and_a_utc_creation_time(self):
		self.partition.add( utcnow(), 17, (17.0, 3.5) )
		self.partition.flush( self.db )

		row	= self.db.rows[0]
		self.assertEqual( row['tick'], '17' )
		self.assertEqual( row['case_id'], '42' )
		self.assertEqual( row['audit_status'], str(AUDIT_REGISTER) )
		self.assertEqual( row['report_time'], '17.0' )

		created	= datetime.datetime.fromisoformat( row['creation_time'] )
		self.assertEqual( created.utcoffset(), datetime.timedelta(0) )

	def test_none_is_written_as_null(self):
		self.partition.add( utcnow(), 3, (3.0, None) )
		self.partition.flush( self.db )
		self.assertIsNone( self.db.rows[0]['value'] )

if __name__ == '__main__':
    unittest.main()
