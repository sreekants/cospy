#!/usr/bin/python
# Filename: ControlBehavior.py
# Description: Implementation of the ControlBehavior class

from cos.core.simulation.Behavior import Behavior, ActorBehavior

class ControlBehavior(Behavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Behavior.__init__(self, ActorBehavior.CONTROL_MOTION)
		self.motion		= None
		return

	def intialize(self, ctxt, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			ctxt -- Simulation context
			actor -- Actor to initialize the behavior for
			vehicle -- Vehicle object to create the actor for
			config -- Configuration attributes
		"""
		Behavior.intialize(self, ctxt, actor, vehicle, config)
		
		self.motion		= actor.behaviors.get(ActorBehavior.MOTION, None)
		return

	def stop(self):
		""" Stops the behavior
		"""
		self.motion.movable	= False
		return

	def resume(self):
		""" Resumes the behavior
		"""
		self.motion.movable	= True
		return

	def notify(self, ctxt, method:str, arg:dict):
		""" Triggers a method
		Arguments
			ctxt -- Simulation context
			method -- Method name
			arg -- Message argumnt
		"""
		if method not in ['bridge.control']:
			return
		
		match arg.get('action', ''):
			case 'stop':
				self.stop()
			case 'resume':
				self.resume()
		return
	
if __name__ == "__main__":
	test = ControlBehavior()

