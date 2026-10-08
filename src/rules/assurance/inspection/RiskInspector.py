#!/usr/bin/python
# Filename: RiskInspector.py
# Description: Clearing house for risk records; the only writer of Rr, the risk assessments and the capsize log

from rules.assurance.inspection.Inspector import Inspector
from maritime.model.risk.RiskLog import RiskLog, CLEARING, RECORD, ASSESSMENT, RR
from cos.core.kernel.Context import Context
from cos.core.kernel.Object import TERM_CLEAR
from cos.core.utilities.ArgList import ArgList

# Field positions in maritime.xml, after the audit fields
VESSEL		= 3		# vessel_id, in fact_risk_assessment and fact_rr
RR_TOTAL	= 11	# rr, in fact_risk_assessment
RR_VALUE	= 6		# value, in fact_rr


class RiskInspector(Inspector):
	TOPIC	= CLEARING

	def __init__(self):
		""" Constructor
		"""
		Inspector.__init__( self, 'Risk' )
		self.written	= {}		# Table -> rows written
		self.totals		= {}		# Vessel id -> Cr, the sum of its Rr, USD
		self.unbalanced	= 0			# Assessments whose concern rows do not sum to Rr
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Listens on the clearing topic that examiners post their risk records to
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Inspector.setup( self, ctxt, config )

		ctxt.sim.ipc.subscribe( self.TOPIC, self )
		self.subscribe( RECORD, self.on_record )
		RiskLog.clearing	= True
		return

	def on_record(self, ctxt:Context, entry):
		""" Writes a posted risk record and keeps each vessel's Cr
		Arguments
			ctxt -- Simulation context of the poster
			entry -- Payload made by RiskLog.post()
		"""
		RiskLog.record( ctxt, entry )

		concerns	= 0.0
		for table, values in entry['rows']:
			self.written[table]	= self.written.get( table, 0 ) + 1
			if table == RR:
				concerns	+= values[RR_VALUE]
			elif table == ASSESSMENT:
				vessel		= values[VESSEL]
				rr			= values[RR_TOTAL]
				self.totals[vessel]	= self.totals.get( vessel, 0.0 ) + rr

		if any( t == ASSESSMENT for t, _ in entry['rows'] ) and (abs(concerns - rr) > 1e-6 * max(1.0, abs(rr))):
			self.unbalanced	+= 1
			if self.unbalanced == 1:
				ctxt.log.error( self.id, f'Concern rows sum to {concerns:g}, not Rr {rr:g}, from {entry["raiser"]}' )
		return

	def on_term(self, ctxt:Context, runlevel):
		""" Writes the records still queued, before the DataManager writes out
		Arguments
			ctxt -- Simulation context
			runlevel -- Termination run level; this acts at TERM_CLEAR
		"""
		if runlevel != TERM_CLEAR:
			return

		ctxt.ipc.pump_node( ctxt.ipc.get_node(self.TOPIC), throttle_rate=0x7fffffff )
		counts	= ', '.join( f'{n} {t}' for t, n in sorted(self.written.items()) ) or 'none'
		ctxt.log.info( self.id, f'Risk records written: {counts}; Cr kept for {len(self.totals)} vessel(s)' )
		if self.unbalanced:
			ctxt.log.error( self.id, f'{self.unbalanced} assessment(s) whose concern rows do not sum to Rr' )
		return


if __name__ == "__main__":
	test = RiskInspector()
