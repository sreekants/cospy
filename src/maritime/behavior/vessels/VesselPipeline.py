#!/usr/bin/python
# Filename: VesselPipeline.py
# Description: Builds a planned vessel behaviour's ops, postops and syncops from its ship model's pipeline

from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from maritime.behavior.vessels.FishingVessel import FishingVessel
from maritime.behavior.vessels.VesselManeuvers import VesselManeuvers
from maritime.behavior.vessels.VesselActions import VesselActions
from maritime.behavior.vessels.VesselSignals import VesselSignals

LISTS	= ('ops', 'postops', 'syncops')

# Step name -> (function, list it runs in, behaviour class it needs)
STEPS	= {
	'tss_compliance'		: (VesselManeuvers.tss_compliance,		'ops',		None),
	'tss_avoidance'			: (VesselManeuvers.tss_avoidance,		'ops',		None),
	'stop_for_safety'		: (VesselManeuvers.stop_for_safety,		'ops',		None),
	'overtaking_distance'	: (VesselManeuvers.overtaking_distance,	'ops',		None),
	'apply_momentum'		: (VesselManeuvers.apply_momentum,		'ops',		None),
	'crossing_slowdown'		: (VesselManeuvers.crossing_slowdown,	'ops',		None),
	'fishing_slowdown'		: (VesselManeuvers.fishing_slowdown,	'ops',		FishingVessel),

	'restore_speed'			: (VesselManeuvers.restore_speed,		'postops',	None),
	'collision_avoidance'	: (VesselActions.collision_avoidance,	'postops',	None),
	'tss_lane'				: (VesselActions.tss_lane,				'postops',	None),
	'tss_crossing'			: (VesselActions.tss_crossing,			'postops',	None),

	'declare_operation'		: (FishingVessel.declare_operation,		'syncops',	FishingVessel),
	'navigation_lights'		: (VesselSignals.navigation_lights,		'syncops',	None),
	'day_shapes'			: (VesselSignals.day_shapes,			'syncops',	None),
	'fog_signals'			: (VesselSignals.fog_signals,			'syncops',	None),
}

SIGNALS	= ('navigation_lights', 'day_shapes', 'fog_signals')


class VesselPipeline:
	def __init__(self):
		return

	@staticmethod
	def configure(ctxt, b, pipeline, source:str):
		""" Sets a planned behaviour's step lists from a ship model's pipeline section
		Arguments
			ctxt -- Simulation context
			b -- Motion behaviour; only a PlannedVesselBehavior is configured
			pipeline -- The model's pipeline section, {list: [step names]}
			source -- Ship model file, for errors
		"""
		if not isinstance( b, PlannedVesselBehavior ):
			return

		kind	= type(b).__name__
		if not isinstance( pipeline, dict ):
			raise ValueError( f'{source}: a {kind} vessel needs a pipeline section' )

		unknown	= set( pipeline ) - set( LISTS )
		if unknown:
			raise ValueError( f'{source}: pipeline has unknown lists {sorted(unknown)}; expected {list(LISTS)}' )

		for name in LISTS:
			setattr( b, name, VesselPipeline.steps( b, name, pipeline.get(name) or [], source ) )

		if any( step in SIGNALS for step in (pipeline.get('syncops') or []) ):
			VesselSignals.configure( ctxt )
		return

	@staticmethod
	def steps(b, name:str, names, source:str)->list:
		""" Step functions for one list, checked against the step table
		Arguments
			b -- Motion behaviour
			name -- 'ops', 'postops' or 'syncops'
			names -- Step names, in order
			source -- Ship model file, for errors
		"""
		if not isinstance( names, list ):
			raise ValueError( f'{source}: pipeline.{name} must be a list of step names' )

		fns		= []
		for step in names:
			if step not in STEPS:
				raise ValueError( f'{source}: pipeline.{name} has unknown step {step!r}; known steps are {sorted(STEPS)}' )

			fn, where, needs	= STEPS[step]
			if where != name:
				raise ValueError( f'{source}: step {step!r} runs in pipeline.{where}, not pipeline.{name}' )
			if (needs is not None) and not isinstance( b, needs ):
				raise ValueError( f'{source}: step {step!r} needs a {needs.__name__} behaviour, not {type(b).__name__}' )
			fns.append( fn )
		return fns


if __name__ == "__main__":
	test = VesselPipeline()
