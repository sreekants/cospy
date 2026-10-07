#!/usr/bin/python
# Filename: RiskLog.py
# Description: Posts risk records from examiners to the RiskInspector, which alone writes them

from cos.core.kernel.Context import Context

CLEARING	= '/Faculty/Practice/Inspectors/RiskInspector'		# Topic the RiskInspector clears risk records from
RECORD		= 'risk.record'

# Tables only the RiskInspector writes
ASSESSMENT	= 'fact_risk_assessment'
RR			= 'fact_rr'
CAPSIZE		= 'fact_capsize'
SIM_LOG		= 'fact_sim_log'
TABLES		= (ASSESSMENT, RR, CAPSIZE, SIM_LOG)


class RiskLog:
	clearing	= False		# A RiskInspector is loaded
	_warned		= False

	@staticmethod
	def post(ctxt:Context, raiser:str, rows:list, context=None)->bool:
		""" Posts the rows of one risk record to the RiskInspector
		Arguments
			ctxt -- Simulation context
			raiser -- Id of the examiner that produced them
			rows -- (table, values) pairs, written together; values in maritime.xml field order
			context -- DataContext for the rows' dimension columns
		Returns
			True when the record was posted
		"""
		for table, _ in rows:
			if table not in TABLES:
				raise ValueError( f'RiskLog: {table} is not a risk table; expected one of {TABLES}' )

		if (RiskLog.clearing == False) and (RiskLog._warned == False):
			RiskLog._warned	= True
			ctxt.log.error( raiser, 'No RiskInspector loaded: risk records are not written; add it to rules.assurance.yaml' )

		ctxt.ipc.push( CLEARING, RECORD, ctxt, {
			'raiser'	: raiser,
			'rows'		: list( rows ),
			'context'	: context,
		} )
		return True

	@staticmethod
	def record(ctxt:Context, entry:dict):
		""" Writes the rows of one posted record; only the RiskInspector calls this
		Arguments
			ctxt -- Simulation context
			entry -- Payload made by post()
		"""
		for table, values in entry['rows']:
			ctxt.sim.data.push( table, values, entry.get('context') )
		return


if __name__ == "__main__":
	test = RiskLog()
