#!/usr/bin/python
# Filename: ColregResolver.py
# Description: Implementation of the ColregResolver class

from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

import numpy as np
import math

class ColregResolver(Resolver):
	def __init__(self, resolver):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
		""" 
		Resolver.__init__(self, '(OwnShip,TargetShip).COLREG.')


		self.tr			= resolver.get('target')
		self.situation	= None
		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		""" 
		self.tr.reset( ctxt, rulectxt )
		return

	@simproperty
	def Situation(self)->str:
		""" TODO: Situation
		""" 
		if self.tr is None:
			return None

		if self.tr.is_valid() == False:
			return None

		if self.situation is not None:
			return self.situation


		α		= self.tr.Approach()
		β		= self.tr.TargetApproach()

		uα		= self.tr.Velocity()
		uβ		= self.tr.TargetVelocity()

		situation = ''
		if abs(β)<13 and abs(α)<13:
			situation = 'HeadOn'			# Head On
		elif abs(β)<112.5 and abs(α)<45 and (uβ>uα):
			situation = 'Overtaken'			# Overtaken
		elif abs(α)<112.5 and abs(β)<45 and (uα<uβ):
			situation = 'Overtaking'		# Overtaking
		elif (-112.5 < β < 0.0) and (-10 < α < 112.5):
			situation = 'StandOn'			# Stand On
		elif (-112.5 <  α < 0.0) and ( -10 < β < 112.5):
			situation = 'GiveWay'			# Give Way

		self.situation	= situation
		return self.situation


if __name__ == "__main__":
	test = ColregResolver()

