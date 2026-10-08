#!/usr/bin/python
# Filename: SignalExaminer.py
# Description: Implementation of the SignalExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from cos.model.examiner.Examination import ExaminationType
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.core.utilities.ArgList import ArgList
from cos.model.examiner.Precondition import PreconditionSet

# REQUIREMENT:
# Signals: collates what a vessel means to do with what is happening around it,
# and posts the pair where COLREG rule 34 can hear it.
#
# NOTE:
#   Rule 34 governs manoeuvring and warning signals, and it cannot be judged from
#   either half alone: a single short blast is correct when altering to starboard
#   and wrong when altering to port. So this examiner does not judge. It publishes
#   the tuple
#
#     (intent, signal, situation)
#
#   where signal is what the vessel is showing (REQ.036), so the rule can tell a
#   manoeuvre from the signal that accompanies it. It posts the tuple to the
#   topics listed in zones.yaml - by default /Faculty/Regulation/Rules,
#   where rule 34 listens - and lets rule 34 decide. Keeping the judgement there keeps implementation of the
#   rule in one place.
#
#   The tuple is only posted when it changes. Rule 34 is about the signal
#   accompanying a manoeuvre, so a steady state is not an event, and republishing
#   it every tick would drown the queue.



class SignalExaminer(ZoneAware, NavigationExaminer):
	EXAMINES	= ExaminationType.SIGNAL
	MESSAGE		= 'vessel.signal'
	TOPIC		= ['/Faculty/Regulation/Rules']

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)

		self.report_topic	= self.TOPIC
		self.message	= self.MESSAGE
		self.posted		= {}		# Vessel IMO -> last tuple posted
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os'] )

		settings		= self.rules.section( 'signal' )
		self.report_topic	= settings.get( 'topic', self.TOPIC )
		self.message	= settings.get( 'message', self.MESSAGE )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		return

	def resolvable(self, binding, rule_ctxt:RuleContext):
		return self.gate.holds( binding, rule_ctxt.situation )
	
	def judge(self, ctxt:Context, rule_ctxt):
		""" Judges rule_ctxt.situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		vessel		= rule_ctxt.situation.os
		intent		= self.intent( rule_ctxt )
		signal		= self.signal( rule_ctxt )
		situation	= self.situation( rule_ctxt )

		if (intent is None) and (signal is None) and (situation is None):
			return

		imo			= self.identify( vessel )
		posted		= ( intent, signal, situation )

		if self.posted.get( imo ) == posted:
			return			# Unchanged: not a signalling event

		self.posted[imo]	= posted
		self.post( ctxt, rule_ctxt, vessel, imo, intent, situation, signal )
		return

	def post(self, ctxt:Context, rule_ctxt:RuleContext, vessel, imo, intent, situation, signal=None):
		""" Posts the (intent, signal, situation) tuple for rule 34
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			vessel -- Own ship
			imo -- Own ship IMO
			intent -- Declared manoeuvring intent
			situation -- COLREG encounter classification
			signal -- Signals shown, as one token
		"""
		shapes, _rules, _depth	= self.survey( vessel )

		payload	= {
			'vessel'	: situation.os,
			'target'	: situation.ts,
			'time'		: ctxt.sim.now(),
			'zone'		: self.zone_name( shapes ),
			'intent'	: intent,
			'signal'	: signal,
			'situation'	: situation,
		}

		self.announce( ctxt, self.report_topic, self.message, payload )

		# The vessel is told as well, so a bridge model can raise the signal
		# without subscribing to the regulation topic.
		if vessel is not None:
			vessel.notify( ctxt, self.message, payload )

		return payload

	@staticmethod
	def intent(rule_ctxt:RuleContext):
		""" What the own ship means to do
		Arguments
			rule_ctxt -- Rule context
		"""
		return SignalExaminer.token( rule_ctxt.resolve('OwnShip.Intent') )

	@staticmethod
	def signal(rule_ctxt:RuleContext):
		""" What the own ship is showing: lights, shapes and sound signals (REQ.036)
		Arguments
			rule_ctxt -- Rule context
		"""
		return SignalExaminer.token( rule_ctxt.resolve('OwnShip.Signal') )

	@staticmethod
	def token(declared):
		""" A value set as one readable token, which is what rule 34 matches on
		Arguments
			declared -- Value set, a list, or None
		"""
		if declared is None:
			return None

		try:
			values	= [ str(v) for v in declared ]
		except TypeError:
			return str( declared )

		return ','.join( sorted(values) ) if values else None

	@staticmethod
	def situation(rule_ctxt:RuleContext):
		""" How the encounter is classified
		Arguments
			rule_ctxt -- Rule context
		"""
		if rule_ctxt.situation is None or rule_ctxt.situation.ts is None:
			return None
		
		classified	= rule_ctxt.resolve( '(OwnShip,TargetShip).EncounterSituation' )
		return None if classified is None else str( classified )


if __name__ == "__main__":
	test = SignalExaminer()
