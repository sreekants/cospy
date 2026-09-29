#!/usr/bin/python
# Filename: test_Bindings.py
# Description: Test cases for the shipped evidence bindings against the network (COS.006)

import os, unittest

import yaml

from tests.maritime.model.risk.test_ConcernWeights import source_module, ROOT, CONFIG

RiskModel	= source_module( 'rules.examiner.risk.RiskModel' )
NETWORK		= os.path.join( CONFIG, 'risk', 'risk.model.xdsl' )
BINDINGS	= [ os.path.join(CONFIG, 'risk', 'risk.model.yaml'),
				os.path.join(ROOT, 'scenarios', 'config', 'risk', 'risk.model.yaml') ]


class BindingsTestCase(unittest.TestCase):
	def setUp(self):
		self.bn	= RiskModel.load( NETWORK, RiskModel.HAZARDS )[0]

	def test_every_bound_node_is_in_the_network(self):
		names	= set( self.bn.names() )
		for path in [p for p in BINDINGS if os.path.exists(p)]:
			with open( path ) as f:
				risk	= yaml.safe_load( f )['risk']
			bound	= { b['node'] for group in risk.values() if isinstance(group, list) for b in group }
			self.assertEqual( bound - names, set(), path )

	def test_threshold_states_are_node_states(self):
		for path in [p for p in BINDINGS if os.path.exists(p)]:
			with open( path ) as f:
				risk	= yaml.safe_load( f )['risk']
			for group in risk.values():
				for b in (group if isinstance(group, list) else []):
					if b.get('discretize') == 'threshold':
						self.assertTrue( set(b['states']) <= set(self.bn.variable(b['node']).labels()), (path, b['node']) )


if __name__ == '__main__':
	unittest.main()
