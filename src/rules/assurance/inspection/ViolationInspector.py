#!/usr/bin/python
# Filename: ViolationInspector.py
# Description: Clearing house for violation costs; the only writer of Ro, Rl and Rw into fact_concern

from rules.assurance.inspection.Inspector import Inspector
from maritime.model.zone.Ledger import Ledger, CLEARING, VIOLATION
from cos.core.kernel.Context import Context
from cos.core.kernel.Object import TERM_CLEAR
from cos.core.utilities.ArgList import ArgList


class ViolationInspector(Inspector):
	TOPIC	= CLEARING

	def __init__(self):
		""" Constructor
		"""
		Inspector.__init__( self, 'Violation' )
		self.recorded	= 0
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Listens on the clearing topic that rules and examiners post their violations to
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Inspector.setup( self, ctxt, config )

		ctxt.sim.ipc.subscribe( self.TOPIC, self )
		self.subscribe( VIOLATION, self.on_violation )
		Ledger.clearing	= True
		return

	def on_violation(self, ctxt:Context, finding):
		""" Records a posted violation into fact_concern
		Arguments
			ctxt -- Simulation context of the poster
			finding -- Payload made by Ledger.post()
		"""
		Ledger.record( ctxt, finding )
		self.recorded	+= 1
		return

	def on_term(self, ctxt:Context, runlevel):
		""" Records the violations still queued, before the DataManager writes out
		Arguments
			ctxt -- Simulation context
			runlevel -- Termination run level; this acts at TERM_CLEAR
		"""
		if runlevel != TERM_CLEAR:
			return

		ctxt.ipc.pump_node( ctxt.ipc.get_node(self.TOPIC), throttle_rate=0x7fffffff )
		ctxt.log.info( self.id, f'{self.recorded} violation(s) recorded' )
		return


if __name__ == "__main__":
	test = ViolationInspector()
