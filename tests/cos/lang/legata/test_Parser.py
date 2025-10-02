#!/usr/bin/python
# Filename: Parser_test.py
# Description: Test cases for the Parser class

from cos.lang.legata.Parser import Parser
from cos.core.kernel.Configuration import Configuration

import unittest

class ParserTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.parser 	= Parser(None)
		self.parser.build()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_expression(self):
		self.parser.parse('condition: {: Map.Sea@TrafficSeparationScheme.Distance in Area.Near.ProximityRange }')
		self.parser.parse('condition: {: OS.Restriction in [\'COLREG.Rule10.*\', \'COLREG.Rule10.*\', \'COLREG.Rule10.*\'] }')
		return

	def test_definitions(self):
		self.parser.parse('''
			# COLREG.Rule10:

			define:{
				OS: OwnShip
				TS: TargetShip
				TSS: OwnShip.TrafficSeparationScheme
			}

		''')


	def test_condition(self):
		self.parser.parse('''
			condition: {
				: Map.Sea@TrafficSeparationScheme.Distance in Area.Near.ProximityRange
				: Map.Sea@TrafficSeparationScheme.Distance in range(10.33, 5)
			}
		''')

	def test_clause(self):
		self.parser.parse('''
			clause['COLREG.Rule10.b.i']:{
				: {
					condition: {
								:TSS is not empty
								:(TSS is empty) and (
								(OS.Intent in [TrafficSeparationScheme.Enter]) or 
								(OS.Intent in [TrafficSeparationScheme.Enter]))
						}
								
					assure: { 
						:[OS.Position, TSS.ExitZone].Distance in TSS.SafeDistance
						:OS.Heading in any TSS.SafeExitHeading
						:OS.Position in TSS.Area
						:OS.Heading in TSS.Heading
						:OS.Velocity in TSS.Velocity
						:(OS,TS).Distance in TSS.SafeDistance
						:[OS.Position, TSS.SeparationZone].Distance in TSS.SafeDistance
						:(OS, TSS).Gradient in range(87.5,92.5)  # 5 degree margin of error  
						:abs((OS.Heading, TSS.SafeHeading).Gradient) in range(87.5,92.5) 
						}
				}
			}
		''')

	def test_Compile(self):
		path	= Configuration.resolve_path('$(COS_ROOT)/config/maritime/regulation/colreg/test.k')
		with open(path, 'rt') as f:
			codepage = f.read()
			self.parser.parse(codepage, path)
		return

if __name__ == '__main__':
    unittest.main()
