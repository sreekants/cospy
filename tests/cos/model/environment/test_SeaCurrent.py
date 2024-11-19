#!/usr/bin/python
# Filename: SeaCurrent_test.py
# Description: Test cases for the SeaCurrent class

from cos.model.environment.Actors import ActorType
from cos.model.environment.SeaCurrent import SeaCurrent
from cos.core.kernel.Configuration import Configuration
from cos.core.utilities.ActiveRecord import ActiveRecord
import unittest

class SeaCurrentTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		path		= Configuration.resolve_path('$(COS_ROOT)/config/weather/alesund/clearsky/environment.s3db')
		profile		= (ActorType.SEA_CURRENT, "cos.model.environment.SeaCurrent", 'sea_current', 'sea_currents')
		db			= ActiveRecord.create(profile[2], path, profile[3])
		self.inst	= SeaCurrent( profile )
		self.inst.load( None, db.get_all(), path )
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_calculate_vector_atpos(self):
		for p in [(10,10),(150,200),(400,504)]:
			print( f'{p} = {self.inst.at(p[0],p[1])}' )


if __name__ == '__main__':
    unittest.main()
