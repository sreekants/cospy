#!/usr/bin/python
# Filename: RiskExposure.py
# Description: Request to reset the RiskExaminer's exposure period T (P3 Appendix F)

class RiskExposure:
	""" A request from another faculty to reset the exposure period T, for one
	vessel or for every vessel, from the next assessment on. The RiskExaminer
	applies it and logs it to fact_sim_log.

	It travels as a plain dict (to_payload) so the message queue can carry it
	wherever it routes messages; the examiner rebuilds it with from_payload.
	"""

	TOPIC		= '/Faculty/Risk/Exposure'
	MESSAGE		= 'risk.exposure.reset'
	FIELDS		= ( 'reason', 'period', 'vessel', 'event', 'source' )

	def __init__(self, reason, period=None, vessel=None, event=None, source=None):
		""" Constructor
		Arguments
			reason -- Why T changes; required
			period -- New T in simulated seconds; None restores the model file's T
			vessel -- Guid of the vessel to reset; None resets every vessel
			event -- What prompted the reset, e.g. 'port.entry'
			source -- The requesting faculty
		"""
		self.reason		= str( reason or '' ).strip()
		self.period		= period
		self.vessel		= vessel
		self.event		= str( event or '' )
		self.source		= str( source or '' )
		return

	def refusal(self):
		""" Why the request cannot be applied, or None when it can. The examiner
		adds its own check: the exposure basis must have a period.
		"""
		if not self.reason:
			return 'no reason given'
		if self.period is None:
			return None
		try:
			period	= float( self.period )
		except (TypeError, ValueError):
			period	= 0.0
		if period <= 0:
			return f'period {self.period!r} is not a positive number of seconds'
		return None

	def to_payload(self):
		""" The request as the dict the message queue carries
		"""
		return { k: v for k, v in ( (f, getattr(self, f)) for f in self.FIELDS ) if v not in (None, '') }

	@staticmethod
	def from_payload(arg):
		""" Rebuilds a request from a queued message argument
		Arguments
			arg -- A RiskExposure, or the dict to_payload() produced; anything else
				gives a request without a reason, which is refused
		"""
		if isinstance( arg, RiskExposure ):
			return arg
		arg		= arg if isinstance( arg, dict ) else {}
		return RiskExposure( arg.get('reason'), arg.get('period'), arg.get('vessel'), arg.get('event'), arg.get('source') )

	def send(self, ctxt):
		""" Pushes the request to the RiskExaminer's exposure topic
		Arguments
			ctxt -- Simulation context of the requesting faculty
		"""
		return ctxt.ipc.push( self.TOPIC, self.MESSAGE, ctxt, self.to_payload() )

	def __repr__(self):
		period	= 'model T' if self.period is None else f'{float(self.period):g} s'
		return f'RiskExposure({period} for {self.vessel or "every vessel"}: {self.reason})'


if __name__ == "__main__":
	test = RiskExposure( 'test' )
