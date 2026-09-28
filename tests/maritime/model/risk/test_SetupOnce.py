#!/usr/bin/python
# Filename: test_SetupOnce.py
# Description: Test cases for examiners being set up once per load (COS.032)

import ast, glob, os, unittest
from unittest import mock

from tests.maritime.model.risk.test_ConcernWeights import source_module, SRC

RiskExaminer	= source_module( 'rules.examiner.risk.RiskExaminer' ).RiskExaminer
Faculty			= source_module( 'cos.core.kernel.Faculty' ).Faculty


class SetupOnceTestCase(unittest.TestCase):
	def test_risk_examiner_sets_up_once(self):
		exam	= RiskExaminer()
		with mock.patch.object( RiskExaminer, 'setup' ) as setup, mock.patch.object( Faculty, 'on_init' ):
			exam.on_init( mock.Mock(), {'config': 'trace=true'} )
		self.assertEqual( setup.call_count, 1 )
		self.assertTrue( exam.trace )

	def test_no_examiner_calls_setup_after_its_base_on_init(self):
		""" Examiner.on_init() already calls setup(); a subclass that also calls it loads twice """
		offenders	= []
		for path in glob.glob( os.path.join(SRC, 'rules', 'examiner', '**', '*.py'), recursive=True ):
			tree	= ast.parse( open(path).read() )
			for fn in ast.walk( tree ):
				if not (isinstance(fn, ast.FunctionDef) and fn.name == 'on_init'):
					continue
				calls	= [ c.func for c in ast.walk(fn) if isinstance(c, ast.Call) and isinstance(c.func, ast.Attribute) ]
				base	= any( f.attr == 'on_init' and isinstance(f.value, ast.Name) and f.value.id != 'self' for f in calls )
				again	= any( f.attr == 'setup' and isinstance(f.value, ast.Name) and f.value.id == 'self' for f in calls )
				if base and again:
					offenders.append( os.path.relpath(path, SRC) )
		self.assertEqual( offenders, [] )


if __name__ == '__main__':
	unittest.main()
