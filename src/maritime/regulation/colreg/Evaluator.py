#!/usr/bin/python
# Filename: Evaluator.py
# Description: Implementation of the Evaluator class for COLREG evaluation

from maritime.regulation.colreg.Resolver import Resolver
from maritime.regulation.colreg.API import API
from cos.model.rule.Context import Context as RuleContext
from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.core.utilities.ArgList import ArgList

class Evaluator(Service):
	def __init__(self):
		""" Constructor
		Arguments
		"""
		Service.__init__(self, "Regulation/COLREG", "Evaluator")

		self.timer			= None

		self.preprocessors	= None
		self.situations		= None
		self.rules			= None
		self.postprocessors	= None
		self.poll_at		= 1
		self.resolver		= Resolver()
		self.API			= API()

		self.monitor_timer	= Ticker( 0.5 )	# Monitor every half second
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Service.on_start(self, ctxt, config)

		self.init_config(ctxt, config)
		self.init_faculties(ctxt, config)
		self.init_objects(ctxt, config)

		# Pump events to the rules
		self.poll_ipc( ctxt, ['/Faculty/Regulation/Rules/COLREG'] )
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Service.on_timer(self, ctxt, unused)

		# Monitor all the time. So so we do not miss any events
  		# in between signaling
		if self.monitor_timer.signaled() == True:
			self.monitor(ctxt)

		if (self.timer is None) or (self.timer.signaled() == False):
			return

		self.evaluate(ctxt)
		return

	def init_config(self, ctxt, config):
		""" Initializes the configuration
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Parse configurations
		args				= ArgList(config["config"])

		self.poll_at		= args["sample.frequency"]

		# Initialize timer ticks
		if self.poll_at is not None:
			self.timer	= Ticker( int(self.poll_at) )
		else:
			self.timer	= None

		# Initialize resolvers from packages
		self.resolver.init(ctxt, args["resolvers"])
		return

	def init_faculties(self, ctxt:Context, config):
		""" Initializes the faculties
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Load all the relevant faculties for use later
		objmgr				= ctxt.sim.objects
		self.situations		= objmgr.get_all("/Faculty/Situation/Maritime")
		self.preprocessors	= objmgr.get_all("/Faculty/Situation/Incident")
		self.postprocessors	= objmgr.get_all("/Faculty/Situation/Processors")

		self.rules			= objmgr.get_all("/Faculty/Regulation")
		return

	def init_objects(self, ctxt:Context, config):
		""" Initializes the simulation objects
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Load all the actors in the simulation
		objmgr				= ctxt.sim.objects
		self.world			= ctxt.sim.world
		self.vessels		= objmgr.get_all("/World/Vehicle/Vessel")
		self.land			= objmgr.get_all("/World/Land")
		self.sea			= objmgr.get_all("/World/Sea")

		return


	def monitor(self, ctxt:Context):
		""" Monitors events on the simulation
		Arguments
			ctxt -- Simulation context
		"""
		rule_ctxt = RuleContext(ctxt, self.resolver, self.world, self.vessels, self.API)


		# Preprocess situations
		[s.evaluate(ctxt, rule_ctxt) for s in self.preprocessors]

		# Evaluate situations
		[s.evaluate(ctxt, rule_ctxt) for s in self.situations]

		# Postprocess situations
		[s.evaluate(ctxt, rule_ctxt) for s in self.postprocessors]

		return

	def evaluate(self, ctxt:Context):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""

		try:
			rule_ctxt = RuleContext(ctxt, self.resolver, self.world, self.vessels, self.API)

			# IMPORTANT: It is critical that
			# Initialize for rule evaluation.
			[r.begin(ctxt, rule_ctxt) for r in self.rules]

			# Evaluate the rules.
			[r.evaluate(ctxt, rule_ctxt) for r in self.rules]

			# Finalize the rules for scoring and bookkeeping.
			[r.end(ctxt, rule_ctxt) for r in self.rules]
		except Exception as e:
			ctxt.log.error( 'RuleEvaluator', f'Runtime error: {str(e)}' )
		

		return

if __name__ == "__main__":
	test = Evaluator()


