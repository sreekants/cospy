#!/usr/bin/python
# Filename: UnderTest.py
# Description: Monitors faculty owning the VesselFilter, published at /Faculty/Situation/Filter

from cos.model.situation.Situation import Situation
from maritime.core.situation.VesselFilter import VesselFilter
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

PATH		= '/Faculty/Situation/Filter'
DEFAULT		= '$(SIMULATION)/undertest.yaml'


class UnderTest(Situation):
	def __init__(self):
		""" Constructor
		"""
		Situation.__init__( self, 'Situation/Filter', 'Vessel' )
		self.filter		= VesselFilter()
		return

	def on_start(self, ctxt:Context, config):
		""" Loads the list and resolves it against the fleet
		Arguments
			ctxt -- Simulation context
			config -- Module information
		Raises
			ValueError when an entry names no vessel or several
		"""
		args		= ArgList( (config or {}).get('arg', '') )
		path		= ctxt.sim.config.resolve( args['file'] or DEFAULT )

		problems	= self.filter.load( path )
		vessels		= ctxt.sim.objects.get_all( "/World/Vehicle/Vessel" )
		problems	+= self.filter.resolve( vessels )

		for problem in problems:
			ctxt.log.error( self.id, problem )

		if problems:
			raise ValueError( f'{len(problems)} problem(s) in the vessels-under-test list {path}' )

		ctxt.log.info( self.id, self.filter.describe() )

		now		= ctxt.sim.now()
		for row in self.filter.records():
			ctxt.sim.data.push( 'fact_under_test', (now,) + row )

		for key, value in self.filter.ambiguous( vessels ):
			ctxt.log.warning( self.id, f'{key}={value} of a vessel under test is shared by another '
									   f'vessel; telemetry filtered on it may keep that vessel\'s rows' )
		return

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Nothing to evaluate; the filter is applied by its consumers
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		return

	@staticmethod
	def find(ctxt:Context)->VesselFilter:
		""" The shared filter, or None when no UnderTest monitor is loaded
		Arguments
			ctxt -- Simulation context
		"""
		found	= ctxt.sim.objects.get_all( PATH )
		for handle in found:
			if isinstance( handle, UnderTest ):
				return handle.filter

		return None


if __name__ == "__main__":
	test = UnderTest()
