#!/usr/bin/python
# Filename: NuisanceExaminer.py
# Description: Implementation of the NuisanceExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from maritime.regulation.colreg import Classification
from cos.model.vehicle.Signal import Signal
from maritime.model.vessel.Vessel import Vessel
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

# REQUIREMENT (REQ.036):
# A vessel must not show manoeuvring or warning signals when there is no one to
# signal to. Each signal's class in $(CONFIG)/maritime/signals.yaml says when it
# may be shown:
#   navigation             never a nuisance (Rules 20-31 require it by status and time)
#   restricted_visibility  a nuisance in clear visibility outside an encounter (Rule 35)
#   encounter              a nuisance outside an encounter (Rule 34)
#
# A vessel is in an encounter from the first encounter message naming it until it
# has been named in none for encounter_release seconds (config/evaluator.yaml).


class NuisanceExaminer(ZoneAware, NavigationExaminer):
	EVENT		= 'signal.nuisance'

	# Once per (vessel, signal) for the run: the signal is the finding's subject
	FINDING		= {'scope': 'episode'}

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)

		self.engaged	= {}		# Vessel key -> simulated seconds it was last named in an encounter
		self.current	= None		# Time of this pass
		self.previous	= None		# Time of the pass before
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os'] )
		Vessel.load_signals( ctxt )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		return

	def on_encounter(self, ctxt:Context, evt):
		""" Records that both vessels of an encounter are engaged
		Arguments
			ctxt -- Simulation context
			evt -- (kind, own ship, target or EncounterEvent, ...)
		"""
		now		= ctxt.sim.seconds()
		target	= getattr( evt[2], 'TS', evt[2] )
		for vessel in ( evt[1], target ):
			if vessel is not None:
				self.engaged[ self.identify(vessel) ]	= now
		return

	def judge(self, ctxt:Context, rule_ctxt):
		""" Judges rule_ctxt.situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		now		= ctxt.sim.seconds()
		self.mark( now )

		vessel	= rule_ctxt.situation.os
		shown	= list( getattr(vessel, 'signal', None) or [] )
		if (len( shown ) == 0) or self.in_encounter( vessel, now ):
			return

		clear	= None
		for name in shown:
			kind	= Signal.category( name )
			if kind == 'restricted_visibility':
				clear	= self.clear_visibility( rule_ctxt ) if clear is None else clear
				if clear is not True:		# Fog, or visibility unknown
					continue
			elif kind != 'encounter':
				continue

			shapes, _rules, _depth	= self.survey( vessel )
			self.violate( ctxt, vessel, self.EVENT, shapes, detail=f'{name} shown outside an encounter',
						  subject=name )
		return

	def mark(self, now):
		""" Notes the time of each pass
		Arguments
			now -- Simulated seconds
		"""
		if now != self.current:
			self.previous, self.current	= self.current, now
		return

	def in_encounter(self, vessel, now)->bool:
		""" Whether a vessel was named in an encounter within the release time
		Arguments
			vessel -- Vessel
			now -- Simulated seconds
		"""
		last	= self.engaged.get( self.identify(vessel) )
		if last is None:
			return False

		# Measured from the previous pass, so messages delivered after this pass began still count
		since	= self.previous if self.previous is not None else now
		return last >= since - Classification.THRESHOLDS.release

	@staticmethod
	def clear_visibility(rule_ctxt)->bool:
		""" Whether visibility is clear, or None when it cannot be told
		Arguments
			rule_ctxt -- Rule context
		"""
		visibility	= rule_ctxt.resolve( '(OwnShip,TargetShip).Visibility' )
		restricted	= rule_ctxt.resolve( 'Vessel.RestrictedVisibility.Range' )
		if (visibility is None) or (restricted is None):
			return None

		return float( visibility ) >= float( restricted )


if __name__ == "__main__":
	test = NuisanceExaminer()
