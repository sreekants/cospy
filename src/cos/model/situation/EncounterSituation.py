#!/usr/bin/python
# Filename: EncounterSituation.py
# Description: Enumerations and states of encounter situations that occur in traffic

from cos.model.situation.Situation import Situation
from cos.model.rule.Situation import Situation as RuleSituation
from cos.model.rule.Context import Context as RuleContext
from cos.core.kernel.Context import Context


class EncounterSituation(Situation):
	def __init__(self, category, type):
		""" Constructor
		Arguments
			category -- Category of the object
			type -- Type of the object
		"""
		Situation.__init__(self, category, type)
		return

	def for_each_pair(self, ctxt:Context, rule_ctxt:RuleContext, list1, list2, fn, arg=None):
		""" #TODO: for_each_pair
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			list1 -- List of objects to match
			list2 -- List of objects to match against
			fn -- Function to call back when a vehicle is in range
			arg -- Opaque argument to pass to the callback
		"""
		if list1 is None or list2 is None:
			return

		for lhs in list1:
			for rhs in list2:
				fn( ctxt, rule_ctxt, (lhs, rhs), arg )

		return True

	def for_each_pair_if(self, ctxt:Context, rule_ctxt:RuleContext, fncmp, cmparg, list1, list2, fn, arg=None):
		""" #TODO: for_each_pair_if
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			fncmp -- Comparison function
			cmparg -- Comparison argument
			list1 -- List of objects to match
			list2 -- List of objects to match against
			fn -- Function to call back when a vehicle is in range
			arg -- Opaque argument to pass to the callback
		"""
		if list1 is None or list2 is None:
			return False

		for lhs in list1:
			for rhs in list2:
				if lhs.id == rhs.id:
					continue

				is_match, result = fncmp(lhs, rhs, cmparg)

				if is_match == False:
					continue

				fn( ctxt, rule_ctxt, (lhs, rhs, result), arg )

		return True

	def for_each_if(self, ctxt:Context, rule_ctxt:RuleContext, fncompare, list, fn, arg=None):
		""" #TODO: for_each_if
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			fncompare -- #TODO
			list -- #TODO
			fn -- #TODO
			arg -- #TODO
		"""
		for item in list:
			if fncompare(item, ctxt, rule_ctxt, arg) == False:
				continue

			fn( ctxt, rule_ctxt, (item), arg )

		return


	def post(self, ctxt:Context, namespaces:str, msg:str, arg ):
		""" #TODO: post
		Arguments
			ctxt -- Simulation context
			namespaces -- #TODO
			msg -- #TODO
			arg -- #TODO
		"""
		# Notify regulations
		for ns in namespaces:
			ctxt.ipc.push( ns, msg, ctxt, arg, 8 )
		return

if __name__ == "__main__":
	test = EncounterSituation()


