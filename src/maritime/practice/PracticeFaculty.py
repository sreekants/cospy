#!/usr/bin/python
# Filename: PracticeFaculty.py
# Description: Faculty that observes one continuous check's situations and posts each as an examination (REQ.051)

from maritime.core.situation.MaritimeSituation import MaritimeSituation
from cos.model.examiner.Examination import ExaminationType
from cos.model.rule.Situation import Situation
from cos.model.rule.Context import Context as RuleContext
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import queue

EXAMINERS			= '/Faculty/Practice/Examiners'		# Parent topic every examiner listens under
ENCOUNTER_MESSAGES	= ('vessel.approach', 'vessel.overtaking', 'vessel.crossing', 'vessel.headon')

ENCOUNTERS	= 'encounters'		# One situation per encounter reported since the last pass
SUBJECTS	= 'subjects'		# One situation per vessel under test


class PracticeFaculty(MaritimeSituation):
	TOPIC	= EXAMINERS

	def __init__(self):
		""" Constructor
		"""
		MaritimeSituation.__init__( self, 'Checks', scope='Situation/Practice' )

		self.examination	= None
		self.source			= SUBJECTS
		self.encounters		= queue.Queue()
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		# One instance per check, each under its configured name
		self.bind( 'Situation/Practice', 'Checks', module.get('name') )
		MaritimeSituation.on_init( self, ctxt, module )
		self.setup( ctxt, ArgList( module.get("config", "") ) )
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Reads the check this faculty serves
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes: examination=<ExaminationType name> situations=subjects|encounters
		"""
		self.examination	= ExaminationType[ config['examination'] ]
		self.source			= config['situations'] or SUBJECTS
		if self.source not in (SUBJECTS, ENCOUNTERS):
			raise ValueError( f'{self.id}: situations must be {SUBJECTS} or {ENCOUNTERS}, not {self.source}' )

		if self.source == ENCOUNTERS:
			for message in ENCOUNTER_MESSAGES:
				self.subscribe( message, self.on_encounter )
		return

	def on_encounter(self, ctxt:Context, evt):
		""" Queues an encounter reported by the conduct and situation faculties
		Arguments
			ctxt -- Simulation context
			evt -- (kind, own ship, target or EncounterEvent, ...)
		"""
		own		= evt[1]
		target	= getattr( evt[2], 'TS', evt[2] )
		self.encounters.put( Situation(own, target) )
		return

	def situations(self, rule_ctxt:RuleContext)->list:
		""" This pass's situations: each queued encounter once, or each subject alone
		Arguments
			rule_ctxt -- Rule context
		"""
		queued	= []
		while not self.encounters.empty():
			queued.append( self.encounters.get() )

		if self.source == SUBJECTS:
			subjects	= getattr( rule_ctxt, 'subjects', None ) or rule_ctxt.vessels or []
			return [ Situation(vessel, None) for vessel in subjects ]

		unique	= {}
		for situation in queued:
			unique.setdefault( (situation.os.id, situation.ts.id), situation )
		return list( unique.values() )

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Observes this pass's situations and posts each as an examination
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		for situation in self.situations( rule_ctxt ):
			if self.running == False:
				return
			situation.context	= rule_ctxt
			self.activate( situation.os, situation )
			self.conclude( ctxt, situation.os, self.examination, situation )
		return



if __name__ == "__main__":
	test = PracticeFaculty()
