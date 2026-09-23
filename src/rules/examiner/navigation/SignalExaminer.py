#!/usr/bin/python
# Filename: SignalExaminer.py
# Description: Implementation of the SignalExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.core.utilities.ArgList import ArgList

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
#     (intent, situation)
#
#   to the topic the rule set listens on - by default /Faculty/Regulation/Rules,
#   the same topic MaritimeSituation.regulate() posts regulation events to - and
#   lets rule 34 decide. Keeping the judgement there keeps implementation of the
#   rule in one place.
#
#   The tuple is only posted when it changes. Rule 34 is about the signal
#   accompanying a manoeuvre, so a steady state is not an event, and republishing
#   it every tick would drown the queue.



class SignalExaminer(ZoneAware, NavigationExaminer):
	MESSAGE		= 'vessel.signal'
	TOPIC		= '/Faculty/Regulation/Rules'

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

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		vessel		= rule_ctxt.situation.os
		intent		= self.intent( rule_ctxt )
		situation	= self.situation( rule_ctxt )

		if (intent is None) and (situation is None):
			return

		imo			= self.identify( vessel )
		pair		= ( intent, situation )

		if self.posted.get( imo ) == pair:
			return			# Unchanged: not a signalling event

		self.posted[imo]	= pair
		self.post( ctxt, rule_ctxt, vessel, imo, intent, situation )
		return

	def post(self, ctxt:Context, rule_ctxt:RuleContext, vessel, imo, intent, situation):
		""" Posts the (intent, situation) tuple for rule 34
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			vessel -- Own ship
			imo -- Own ship IMO
			intent -- Declared manoeuvring intent
			situation -- COLREG encounter classification
		"""
		shapes, _rules, _depth	= self.survey( vessel )

		payload	= {
			'vessel'	: imo,
			'target'	: self.identify( rule_ctxt.situation.ts ),
			'time'		: ctxt.sim.now(),
			'zone'		: self.zone_name( shapes ),
			'intent'	: intent,
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
		declared	= rule_ctxt.resolve( 'OwnShip.Intent' )
		if declared is None:
			return None

		# Intent is a ValueSet, which derives from list; a single readable
		# token is what rule 34 matches on.
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
