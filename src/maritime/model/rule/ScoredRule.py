#!/usr/bin/python
# Filename: ScoredRule.py
# Description: Mixin recording a rule's violations into Ro through the shared Ledger

from maritime.model.zone.Ledger import Ledger, FindingGuard, seconds
from cos.core.kernel.Context import Context

ANONYMOUS	= 'def'		# Name the Legata parser gives an unnamed ':{...}' body


class ScoredRule:
	""" Violation recording for a rule.
	"""
	SOURCE		= None		# Ledger.SOURCE_COLREG or Ledger.SOURCE_LOCAL

	def init_scoring(self, ctxt:Context):
		""" Joins the shared ledger and builds the finding guard
		Arguments
			ctxt -- Simulation context
		"""
		self.ledger		= Ledger.shared( ctxt, self.id )

		findings		= self.ledger.rules.section( 'findings' )
		settings		= dict( findings.get('default', {}) or {} )
		settings.update( findings.get('rules', {}) or {} )

		self.findings	= FindingGuard( scope=settings.get('scope', 'change'),
										release=settings.get('release', 10.0),
										interval=settings.get('interval'),
										dwell=settings.get('dwell', 0.0) )
		self.unpriced	= set()
		return

	def note_unpriced(self, ctxt:Context, clause:str):
		""" Logs a failed unpriced clause, once per clause
		Arguments
			ctxt -- Simulation context
			clause -- The failed clause
		"""
		if clause in self.unpriced:
			return

		self.unpriced.add( clause )
		ctxt.log.warning( self.id, f'Unpriced clause {clause} failed; not recorded in Ro' )
		return

	def record_violation(self, ctxt:Context, raiser:str, vessel, event:str, subject,
						 penalty:float, concern=None)->bool:
		""" Records a priced violation once per occurrence
		Arguments
			ctxt -- Simulation context
			raiser -- Id of the rule, as it should appear in the row
			vessel -- Vessel in violation
			event -- The violated clause
			subject -- What else the finding is about, e.g. the target ship
			penalty -- Penalty score
			concern -- A concern, or an event id that maps to one; None maps the clause
		Returns
			True when a row was written
		"""
		key		= ( Ledger.identify(vessel), event, subject )
		if self.findings.admit( key, seconds(ctxt.sim.now()) ) == False:
			return False

		rules	= self.ledger.rules
		if (concern is not None) and (concern not in rules.vocabulary):
			concern	= rules.concern( concern )

		shapes	= self.ledger.shapes( ctxt, vessel )
		return self.ledger.record( ctxt, self.SOURCE, raiser, vessel, event, shapes,
								   penalty, 0.0, concern )

	@staticmethod
	def clause_name(err)->str:
		""" The name of the clause a failed decision belongs to
		Arguments
			err -- The failed Decision
		"""
		node	= err
		while node is not None:
			name	= getattr( node, 'name', None )
			if name and (name != ANONYMOUS):
				return name
			node	= getattr( node, 'parent', None )

		return str( err )


if __name__ == "__main__":
	test = ScoredRule()
