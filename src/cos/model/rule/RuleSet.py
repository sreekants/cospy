#!/usr/bin/python
# Filename: RuleSet.py
# Description: A coolection of rules

from cos.model.situation.Situation import Situation
from cos.core.simulation.Simulation import Simulation
from cos.core.kernel.Context import Context

import yaml

class RuleSet:
	def __init__(self, module_list=None):
		""" Constructor
		Arguments
			module_list -- #TODO
		"""
		self.modules = {}

		# To be loaded from a configuration file
		if module_list is not None:
			self.load_modules( module_list )
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		return

	def run(self, ctxt:Context, situation:Situation):
		""" #TODO: run
		Arguments
			ctxt -- Simulation context
			situation -- #TODO
		"""
		mq = ctxt.sim.ipc
		for v in self.modules.values():
			v.notify( ctxt, "evaluate", situation )
			v.notify( ctxt, "score", situation )

		return

	def load_file(self, ctxt:Context, file):
		""" #TODO: load_file
		Arguments
			ctxt -- Simulation context
			file -- File path
		"""
		config		= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(file) )
		self.load_modules( config["packages"]["rules"] )
		return

	def load_modules(self, module_list):
		""" #TODO: load_modules
		Arguments
			module_list -- #TODO
		"""
		for m in module_list:
			name = m
			klassname = name.split(".")[-1]
			pkg = name
			mod = __import__(pkg, fromlist=[''])
			klass = getattr(mod, klassname)
			self.modules[klassname] = klass()



if __name__ == "__main__":
	test = RuleSet( ["rules.colreg.rule1.Rule1",
					   	"rules.colreg.rule2.Rule2",
						"rules.colreg.rule3.Rule3"] )

	test.run( None, None )


