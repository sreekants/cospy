#!/usr/bin/python
# Filename: Lexer_test.py
# Description: Test cases for the Lexer class

from cos.lang.legata.Lexer import Lexer

import unittest

class LexerTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.lexer = Lexer()
		self.lexer.build()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_tokenizer(self):
		self.lexer.test('''
# COLREG.Rule10:

define:{
    OS: OwnShip
    TS: TargetShip
    TSS: OwnShip.TrafficSeparationScheme
    "AAA"
    'BBB'
}

clause['COLREG.Rule10.l']:{
    : {
        condition: { 
            : (TSS is not empty) and 
              (OS.Status in [Vessel.RESTRICTED]) and
              (OS.Operation in ['Vessel.Operation.SERVICE'])
         }
        assure: { 
            : clear             # Clear all violations
            : abort             # No further processing
        }
    }
}

		''')


	def test_array(self):
		self.lexer.test('''
OS.Restriction in ['COLREG.Rule10.*', "COLREG.Rule11.*"]
			''')
		
if __name__ == '__main__':
    unittest.main()
