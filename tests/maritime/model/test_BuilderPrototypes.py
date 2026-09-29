#!/usr/bin/python
# Filename: test_BuilderPrototypes.py
# Description: Test cases for the prototype tables of the land, sea, sky and vessel builders (COS.019)

from cos.core.kernel.BootLoader import BootLoader
from cos.model.geography.LandBuilder import LandBuilder
from cos.model.geography.SkyBuilder import SkyBuilder
from cos.model.geography.Land import Land
from cos.model.geography.Sea import Sea
from cos.model.geography.Sky import Sky
from maritime.model.geography.SeaBuilder import SeaBuilder
from maritime.model.vessel.Builder import Builder as VesselBuilder
from maritime.model.vessel.Vessel import Vessel

import unittest


class BuilderPrototypesTestCase(unittest.TestCase):
	BUILDERS	= (
		(LandBuilder, 'MOUNTAIN', Land),
		(SeaBuilder, 'FJORD', Sea),
		(SkyBuilder, 'FOG', Sky),
		(VesselBuilder, 'POWER_DRIVEN', Vessel),
	)

	def test_subclass(self):
		for klass, type, base in self.BUILDERS:
			for name, (code, module) in klass({"Type": type}).prototypes.items():
				with self.subTest(builder=klass.__name__, prototype=name):
					_, cls	= BootLoader.load_class( module )
					self.assertTrue( issubclass(cls, base), f'{module} is not a {base.__name__}' )

	def test_unique_codes(self):
		for klass, type, _ in self.BUILDERS:
			with self.subTest(builder=klass.__name__):
				codes	= [ code for code, _ in klass({"Type": type}).prototypes.values() ]
				self.assertEqual( len(codes), len(set(codes)) )


if __name__ == '__main__':
    unittest.main()
