#!/usr/bin/python
# Filename: API.py
# Description: Simulation insitu API available to the environment

from maritime.model.resolver.VesselResolver import VesselResolver
from maritime.model.vessel.Vessel import Vessel, Status
from cos.model.rule.Context import Context as RuleContext
from cos.core.utilities.ArgList import ArgList
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.model.vehicle.Vehicle import Vehicle
from cos.math.geometry.Distance import Distance

class API:
	def __init__(self):
		self.vtbl	= {
			'set':API._set
		}
		return

	def __call__(self, ctxt, method, args):
		func	= self.vtbl.get(method, None)
		if func is None:
			raise RuntimeError(f'Failed to resolve API method [{method}].')
		
		return func(ctxt, args)

	@staticmethod
	def _set(ctxt:RuleContext, args):
		os:Vessel	= ctxt.situation.os
		if os is None:
			return None
		os.mode[args[0]]	= args[1]
		return None
		

if __name__ == "__main__":
	test = API()

