#!/usr/bin/python
# Filename: ExtremeWeatherExaminer.py
# Description: Implementation of the ExtremeWeatherExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from rules.examiner.risk.RiskModel import load
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import numpy as np
import yaml

# REQUIREMENT:
# Extreme weather: the probability that a vessel capsizes, given the sea she is
# in and the hull she is.
#
# This is an inference, not a threshold test, because the four inputs (sea condition, 
# vessel characteristic, visibility,  are not
# independent in their effect. A severe sea is survivable in a large vessel in
# ballast and lethal in a small overladen one; poor visibility contributes
# nothing on its own but compounds a sea that would otherwise be handled. 
# 
# A state machine identifies those interactions once, in CapsizeModel, instead 
# of spreading them through nested conditionals here.
#
# TODO:
# Three of the four inputs have no Legata resolver term, so they are gathered
# directly: sea state by sampling the SEA_WAVE force field at the vessel, and
# payload and size off the vessel itself. Only visibility comes from a term.
# config/risk/capsize.model.yaml holds the state boundaries.



class ExtremeWeatherExaminer(ZoneAware, NavigationExaminer):
	TOPIC		= '/Faculty/Concern/Weather'
	MESSAGE		= 'vessel.capsize.risk'
	EVENT		= 'weather.capsize_risk'

	WAVE_FIELD	= '/World/Weather/SEA_WAVE'

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)

		self.bn			= None
		self.engine		= None
		self.bands		= {}		# Input node -> state boundaries
		self.waves		= []		# SEA_WAVE force fields
		self.threshold	= 1.0
		self.report_topic	= self.TOPIC
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os'] )

		settings		= self.rules.section( 'weather' )
		self.threshold	= float( settings.get('alarm_threshold', 1.0) )
		self.report_topic	= settings.get( 'report_topic', self.TOPIC )

		self.__load_network( ctxt, config["network"] or settings.get('network') )
		self.__load_bands( ctxt, config["bindings"] or settings.get('bindings') )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		self.waves	= ctxt.sim.objects.get_all( self.WAVE_FIELD )
		return

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if (self.engine is None) or (self.applicable(rule_ctxt) == False):
			return

		vessel		= rule_ctxt.situation.os
		evidence	= self.observe( ctxt, rule_ctxt, vessel )
		if len( evidence ) == 0:
			return

		self.engine.setEvidence( evidence )
		self.engine.makeInference()

		capsize		= float( self.engine.posterior('capsize')[{'capsize': 'yes'}] )

		self.report( ctxt, vessel, evidence, capsize )
		return

	def observe(self, ctxt:Context, rule_ctxt, vessel):
		""" Gathers the four inputs as network states
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			vessel -- Own ship
		Returns
			A dictionary of node name -> state label
		"""
		evidence	= {}

		sea			= self.sea_state( vessel )
		if sea is not None:
			evidence['wave_height']		= self.band( 'wave_height', sea )

		evidence['visibility']		= self.visibility( rule_ctxt )
		evidence['payload']			= self.payload( vessel )
		evidence['vessel_size']		= self.size( rule_ctxt, vessel )

		return { k: v for k, v in evidence.items() if v is not None }

	def report(self, ctxt:Context, vessel, evidence, capsize):
		""" Records the assessment and scores it when it crosses the threshold
		Arguments
			ctxt -- Simulation context
			vessel -- Own ship
			evidence -- Evidence used
			capsize -- P(capsize)
		"""
		shapes, _rules, _depth	= self.survey( vessel )
		zone	= self.zone_name( shapes )
		penalty	= 0.0

		if capsize >= self.threshold:
			penalty	= self.violate( ctxt, vessel, self.EVENT, shapes, value=capsize,
									detail=f'P(capsize) {capsize:.3f} from {evidence}' )

		self.announce( ctxt, self.report_topic, self.MESSAGE, {
			'vessel'	: self.identify( vessel ),
			'time'		: ctxt.sim.now(),
			'zone'		: zone,
			'capsize'	: capsize,
			'threshold'	: self.threshold,
			'evidence'	: evidence,
			'penalty'	: penalty,
		} )

		return capsize

	def sea_state(self, vessel):
		""" Magnitude of the sea wave field at the vessel
		Arguments
			vessel -- Own ship
		Returns
			Magnitude, or None when no wave field covers the position
		"""
		position	= getattr( vessel, 'location', None )
		if position is None:
			return None

		strongest	= None
		for field in self.waves:
			try:
				vector	= field.at( position[0], position[1] )
			except Exception:
				continue

			if vector is None:
				continue

			magnitude	= float( np.linalg.norm(vector) )
			strongest	= magnitude if strongest is None else max( strongest, magnitude )

		return strongest

	def visibility(self, rule_ctxt):
		""" Visibility state
		Arguments
			rule_ctxt -- Rule context
		"""
		band	= self.bands.get( 'visibility', {} )

		if rule_ctxt.situation.ts is not None:
			reported	= rule_ctxt.resolve( '(OwnShip,TargetShip).Visibility' )
			if reported is not None:
				try:
					poor, good	= band.get( 'states', ['poor', 'good'] )
					return poor if float(reported) < float(band.get('edge', 1.0)) else good
				except (TypeError, ValueError):
					pass

		return band.get( 'default' )

	def payload(self, vessel):
		""" Payload state, as a fraction of declared capacity
		Arguments
			vessel -- Own ship
		"""
		band		= self.bands.get( 'payload', {} )
		config		= getattr( vessel, 'config', None ) or {}
		args		= ArgList( config.get('settings', None) )

		capacity	= args['capacity'] or args['deadweight']
		weight		= getattr( vessel, 'weight', None )

		if (capacity is None) or (weight is None):
			return band.get( 'default' )

		try:
			return self.band( 'payload', float(weight) / float(capacity) )
		except (TypeError, ValueError, ZeroDivisionError):
			return band.get( 'default' )

	def size(self, rule_ctxt, vessel):
		""" Size state, from length overall
		Arguments
			rule_ctxt -- Rule context
			vessel -- Own ship
		"""
		band	= self.bands.get( 'vessel_size', {} )
		length	= rule_ctxt.resolve( 'OwnShip.Length' )

		if length is None:
			return band.get( 'default' )

		try:
			small, large	= band.get( 'states', ['small', 'large'] )
			return small if float(length) < float(band.get('edge', 50.0)) else large
		except (TypeError, ValueError):
			return band.get( 'default' )

	def band(self, node:str, value):
		""" Maps a value onto a network state using the configured edges
		Arguments
			node -- Network node name
			value -- Observed value
		"""
		band	= self.bands.get( node )
		if band is None:
			return None

		states	= band.get( 'states', [] )
		edges	= band.get( 'edges', [] )

		if len( states ) != (len(edges) + 1):
			return band.get( 'default' )

		index	= 0
		while (index < len(edges)) and (float(value) >= float(edges[index])):
			index	+= 1

		return states[index]

	def __load_network(self, ctxt:Context, file):
		""" Loads the capsize network
		Arguments
			ctxt -- Simulation context
			file -- File path
		"""
		if file is None:
			ctxt.log.error( self.id, 'No capsize network specified' )
			return

		path	= ctxt.sim.config.resolve( file )
		ctxt.log.info( self.id, f'Loading capsize network : {file}' )

		# Only one hazard here, so the joint machinery of RiskModel.load is not
		# needed; the marginal on 'capsize' is the whole answer.
		self.bn, self.engine	= load( path, ('capsize',) )
		return

	def __load_bands(self, ctxt:Context, file):
		""" Loads the evidence state boundaries
		Arguments
			ctxt -- Simulation context
			file -- File path
		"""
		if file is None:
			return

		path		= ctxt.sim.config.resolve( file )
		config		= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(path) )
		self.bands	= (config or {}).get( 'capsize', {} ) or {}
		return


if __name__ == "__main__":
	test = ExtremeWeatherExaminer()
