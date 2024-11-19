#!/usr/bin/python
# Filename: WindCurrent_test.py
# Description: Test cases for the WindCurrent class

from cos.model.environment.Actors import ActorType
from cos.model.environment.WindCurrent import WindCurrent
from cos.core.kernel.Configuration import Configuration
from cos.core.utilities.ActiveRecord import ActiveRecord
import unittest

class WindCurrentTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		path		= Configuration.resolve_path('$(COS_ROOT)/config/weather/alesund/clearsky/environment.s3db')
		profile		= (ActorType.SEA_CURRENT, "cos.model.environment.WindCurrent", 'wind_current', 'wind_currents')
		db			= ActiveRecord.create(profile[2], path, profile[3])
		self.inst	= WindCurrent( profile )
		self.inst.load( None, db.get_all(), path )
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

if __name__ == '__main__':
    unittest.main()
