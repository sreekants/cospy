#!/usr/bin/python
# Filename: Precondition.py
# Description: Situation preconditions for grouped examiner bindings

# REQUIREMENT:
# An examiner reads terms that are only meaningful in certain situations.
# '(OwnShip,TargetShip).DCPA' is not a fact about the world, it is a fact about
# an encounter, and asking for it when no target ship is in scope is a category
# error rather than a missing observation.
#
# A Precondition names the situation attributes a group of terms needs, either
# directly ('os') or as a dotted path through them ('ts.fleet'). Groups
# whose precondition does not hold are skipped whole, so an unresolved term
# always means "applicable but unobserved" and never "not applicable here".
#
# Declaring the requirement as data rather than as a chain of if-branches keeps
# it beside the group it guards; a misspelt group name is then a load-time
# error instead of a group that silently never fires.

from cos.model.rule.Situation import Situation

SITUATION	= set( vars(Situation()) )		# Attributes a precondition path may start from

class Precondition:
	""" The situation attributes a group of bindings requires.
	"""

	def __init__(self, group, requires=None):
		""" Constructor
		Arguments
			group -- Name of the binding group being guarded
			requires -- Situation attribute names or dotted paths that must all be present
		"""
		self.group		= group
		self.requires	= list( requires or [] )

		for name in self.requires:
			head	= name.split('.')[0]
			if head not in SITUATION:
				hint	= "; use 'os.fleet' or 'ts.fleet'" if head == 'fleet' else ''
				raise ValueError( f'Precondition {group}: {name!r} is not a situation attribute{hint}' )
		return

	def holds(self, situation)->bool:
		""" Checks the precondition against a situation
		Arguments
			situation -- Situation reference, may be None
		"""
		if situation is None:
			return False

		for name in self.requires:
			if Precondition.resolve( situation, name ) is None:
				return False

		return True

	@staticmethod
	def resolve(situation, path):
		""" Follows a dotted attribute path from the situation
		Arguments
			situation -- Situation reference
			path -- Attribute name or dotted path, e.g. 'ts.fleet'
		Returns
			The attribute value, or None if any step along the path is absent
		"""
		value	= situation
		for name in path.split('.'):
			value	= getattr( value, name, None )
			if value is None:
				return None

		return value

	def __repr__(self):
		return f'Precondition({self.group} requires {self.requires})'


class PreconditionSet:
	""" The preconditions for every binding group an examiner declares.
	"""

	def __init__(self, groups=None):
		""" Constructor
		Arguments
			groups -- Mapping of group name -> list of situation attributes
		"""
		self.groups	= {}
		for group, requires in (groups or {}).items():
			self.groups[group]	= Precondition( group, requires )
		return

	def load(self, config, known):
		""" Reads 'requires' declarations out of a bindings configuration
		Arguments
			config -- Mapping of group name -> group configuration
			known -- Situation attribute names that may be required, or begin a dotted path
		Returns
			A list of problems, empty when every declaration is usable
		"""
		problems	= []

		for group, body in config.items():
			if isinstance( body, dict ) == False:
				continue

			requires	= body.get( 'requires', [] )
			unknown		= [ r for r in requires if r.split('.')[0] not in known ]
			if unknown:
				problems.append( f'{group}: unknown situation attribute {unknown}' )
				continue

			self.groups[group]	= Precondition( group, requires )

		return problems

	def holds(self, group, situation)->bool:
		""" Checks one group's precondition
		Arguments
			group -- Name of the binding group
			situation -- Situation reference
		Note
			An undeclared group never holds. Skipping it is safer than reading
			terms whose applicability nothing has vouched for.
		"""
		precondition	= self.groups.get( group )
		if precondition is None:
			return False

		return precondition.holds( situation )

	def undeclared(self, groups):
		""" Names the groups that have no precondition, so a caller can refuse
		to run rather than silently skipping them
		Arguments
			groups -- Group names the examiner holds bindings for
		"""
		return sorted( set(groups) - set(self.groups) )


if __name__ == "__main__":
	test = PreconditionSet()
