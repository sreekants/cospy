#!/usr/bin/python
# Filename: test_VesselIdentity.py
# Description: Test cases for vessel identity in the shipped vessel databases (COS.029)

import glob, os, sqlite3, unittest

ROOT	= os.path.abspath( os.path.join(os.path.dirname(__file__), '..', '..', '..', '..') )
CONFIG	= os.path.join( ROOT, 'config' )


def checksum_valid(imo:str)->bool:
	""" Whether a 7-digit IMO satisfies its check digit
	Arguments
		imo -- IMO number as a string
	Returns
		True when the 7th digit matches the weighted sum of the first six
	"""
	if len(imo) != 7 or not imo.isdigit():
		return False
	return sum( int(d) * w for d, w in zip(imo[:6], range(7, 1, -1)) ) % 10 == int(imo[6])


class VesselIdentityTestCase(unittest.TestCase):
	def databases(self):
		files	= sorted( glob.glob(os.path.join(CONFIG, 'simulation', '*', '*', 'vessel.s3db')) )
		self.assertTrue( files, 'no vessel.s3db found' )
		return files

	def column(self, file, name):
		with sqlite3.connect( file ) as db:
			return [ str(r[0]) for r in db.execute(f'SELECT {name} FROM vessels') ]

	def test_guid_imo_and_mmsi_are_unique_per_location(self):
		for file in self.databases():
			for name in ( 'guid', 'imo', 'mmsi' ):
				values	= self.column( file, name )
				self.assertEqual( len(values), len(set(values)), f'{name} repeats in {file}' )

	def test_every_imo_is_an_integer_with_a_valid_check_digit(self):
		# Vessel.recid is int(imo), so a non-numeric IMO stops every vessel loading
		for file in self.databases():
			for imo in self.column( file, 'imo' ):
				self.assertTrue( checksum_valid(imo), f'{imo} in {file}' )

	def test_no_imo_is_shared_by_two_guids_across_locations(self):
		owner	= {}
		for file in self.databases():
			with sqlite3.connect( file ) as db:
				for guid, imo in db.execute( 'SELECT guid, imo FROM vessels' ):
					self.assertEqual( owner.setdefault(str(imo), guid), guid, f'{imo} in {file}' )


if __name__ == '__main__':
	unittest.main()
