#!/usr/bin/python
# Filename: TestInspector.py
# Description: Inspector conducting the test run; selects the vessels under test (REQ.024)

from rules.assurance.Inspector import Inspector, INSPECTORS
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList
from maritime.core.situation.VesselFilter import VesselFilter

DEFAULT		= '$(SIMULATION)/undertest.yaml'


class TestInspector(Inspector):
	def __init__(self):
		""" Constructor
		"""
		Inspector.__init__( self, 'Test' )
		self.filter		= VesselFilter()
		return

	def on_start(self, ctxt:Context, config):
		""" Selects the vessels under test from the list and resolves them against the fleet
		Arguments
			ctxt -- Simulation context
			config -- Module information
		Raises
			ValueError when an entry names no vessel or several
		"""
		args		= ArgList( (config or {}).get('config', '') )
		path		= ctxt.sim.config.resolve( args['file'] or DEFAULT )

		problems	= self.filter.load( path )
		vessels		= ctxt.sim.objects.get_all( "/World/Vehicle/Vessel" )
		problems	+= self.filter.resolve( vessels, (getattr(ctxt.sim, 'disabled_vessels', None) or {}).values() )

		for problem in problems:
			ctxt.log.error( self.id, problem )

		if problems:
			raise ValueError( f'{len(problems)} problem(s) in the vessels-under-test list {path}' )

		ctxt.log.info( self.id, self.filter.describe() )

		now		= ctxt.sim.seconds()
		for row in self.filter.records():
			ctxt.sim.data.push( 'fact_under_test', (now,) + row )

		for key, value in self.filter.ambiguous( vessels ):
			ctxt.log.warning( self.id, f'{key}={value} of a vessel under test is shared by another '
									   f'vessel; telemetry filtered on it may keep that vessel\'s rows' )
		return

	@staticmethod
	def find(ctxt:Context):
		""" The test inspector faculties report to, or None when none is loaded
		Arguments
			ctxt -- Simulation context
		"""
		for handle in ctxt.sim.objects.get_all( INSPECTORS ):
			if isinstance( handle, TestInspector ):
				return handle

		return None

	@staticmethod
	def under_test(ctxt:Context)->VesselFilter:
		""" The vessels-under-test filter, or None when no inspector is loaded
		Arguments
			ctxt -- Simulation context
		"""
		inspector	= TestInspector.find( ctxt )
		return inspector.filter if inspector is not None else None


if __name__ == "__main__":
	test = TestInspector()
