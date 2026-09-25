#!/usr/bin/python
# Filename: test_VesselFilter.py
# Description: Test cases for the vessels-under-test filter (REQ.024)

import os, tempfile, unittest

from maritime.core.situation.VesselFilter import VesselFilter


class Vessel:
	def __init__(self, guid, recid, imo, name, mmsi=0):
		self.id		= guid
		self.recid	= recid
		self.imo	= imo
		self.mmsi	= mmsi
		self.name	= name


# As in tk/turkeli/vessel.s3db: IMO 9627837 is carried by two vessels
FLEET	= [ Vessel('bedc897f-512b-45a2-aea4-bcfc248d2a86', 101, '9627837', 'True North'),
			Vessel('bedc897f-512b-45a2-aea4-bcfc248d2a8e', 102, '9930064', 'MSC NICOLA MASTRO'),
			Vessel('bedc897f-512b-45a2-aea4-bcfc248d2a84', 108, '9627837', 'BERGE ODEL') ]


class VesselFilterTestCase(unittest.TestCase):
	def write(self, text):
		f	= tempfile.NamedTemporaryFile( 'w', suffix='.yaml', delete=False )
		f.write( text )
		f.close()
		self.addCleanup( os.unlink, f.name )
		return f.name

	def loaded(self, text):
		vf	= VesselFilter()
		self.assertEqual( vf.load(self.write(text)), [] )
		return vf

	def test_no_file_filters_nothing(self):
		vf	= VesselFilter()
		self.assertEqual( vf.load('/nonexistent/undertest.yaml'), [] )
		self.assertEqual( vf.resolve(FLEET), [] )
		self.assertFalse( vf.active )
		self.assertEqual( vf.select(FLEET), FLEET )
		self.assertTrue( vf.keeps('fact_collision', ['own_ship'], [999]) )

	def test_empty_list_filters_nothing(self):
		vf	= self.loaded( 'under_test: []\n' )
		self.assertEqual( vf.select(FLEET), FLEET )

	def test_select_by_guid(self):
		vf	= self.loaded( 'under_test:\n  - guid: bedc897f-512b-45a2-aea4-bcfc248d2a86\n' )
		self.assertEqual( vf.resolve(FLEET), [] )
		self.assertEqual( [v.name for v in vf.select(FLEET)], ['True North'] )
		self.assertTrue( vf.under_test(FLEET[0]) )
		self.assertFalse( vf.under_test(FLEET[1]) )

	def test_select_by_name_and_recid(self):
		vf	= self.loaded( 'under_test:\n  - name: MSC NICOLA MASTRO\n  - recid: 108\n' )
		self.assertEqual( vf.resolve(FLEET), [] )
		self.assertEqual( [v.recid for v in vf.select(FLEET)], [102, 108] )

	def test_misspelt_entry_is_an_error(self):
		vf	= self.loaded( 'under_test:\n  - name: True Nort\n' )
		problems	= vf.resolve( FLEET )
		self.assertEqual( len(problems), 1 )
		self.assertIn( 'True Nort', problems[0] )
		self.assertIn( 'matches 0 vessels', problems[0] )

	def test_ambiguous_entry_is_an_error(self):
		vf	= self.loaded( 'under_test:\n  - imo: 9627837\n' )
		self.assertIn( 'matches 2 vessels', vf.resolve(FLEET)[0] )

	def test_malformed_entry_is_an_error(self):
		vf	= VesselFilter()
		self.assertEqual( len(vf.load(self.write('under_test:\n  - colour: red\n'))), 1 )

	def test_shared_identifier_is_reported(self):
		vf	= self.loaded( 'under_test:\n  - guid: bedc897f-512b-45a2-aea4-bcfc248d2a86\n' )
		vf.resolve( FLEET )
		self.assertIn( ('imo', '9627837'), vf.ambiguous(FLEET) )

	def test_telemetry_keeps_rows_about_a_vessel_under_test(self):
		vf	= self.loaded( 'under_test:\n  - recid: 101\n'
						   'telemetry:\n  fact_collision: [own_ship, target_ship]\n' )
		vf.resolve( FLEET )
		fields	= ['own_ship', 'target_ship', 'report_time', 'distance']
		self.assertTrue( vf.keeps('fact_collision', fields, [101, 102, 0.0, 5.0]) )
		self.assertTrue( vf.keeps('fact_collision', fields, [102, 101, 0.0, 5.0]) )
		self.assertFalse( vf.keeps('fact_collision', fields, [102, 108, 0.0, 5.0]) )

	def test_unlisted_table_is_not_filtered(self):
		vf	= self.loaded( 'under_test:\n  - recid: 101\n'
						   'telemetry:\n  fact_collision: [own_ship]\n' )
		vf.resolve( FLEET )
		self.assertTrue( vf.keeps('fact_crossing', ['own_ship'], [108]) )

	def test_records_name_the_vessels_and_source(self):
		vf	= self.loaded( 'under_test:\n  - name: True North\n'
						   'telemetry:\n  fact_collision: [own_ship]\n  fact_approach: [own_ship]\n' )
		vf.resolve( FLEET )
		self.assertEqual( vf.records(), [ (1, '9627837', FLEET[0].id, 'True North', 'name=True North',
										   vf.source, 'fact_approach,fact_collision') ] )

	def test_records_say_when_nothing_is_filtered(self):
		vf	= VesselFilter()
		vf.load( '/nonexistent/undertest.yaml' )
		vf.resolve( FLEET )
		self.assertEqual( vf.records(), [ (0, 0, '', '', '', '/nonexistent/undertest.yaml', '') ] )


if __name__ == '__main__':
	unittest.main()
