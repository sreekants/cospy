#!/usr/bin/python
# Filename: Gamepad.py
# Description: Implementation of the Gamepad class

from cos.core.api.Vessel import Vessel

import pygame

class Gamepad:
	def __init__(self, world):
		self.world		= world
		self.joysticks	= {}
		self.vessel		= None
		self.rpc		= Vessel()
		return

	def handle_event(self, event:pygame.event.Event):
		# Poll events on active joysticks
		self.poll()

		if event.type == pygame.JOYBUTTONDOWN:
			if event.button == 0:
				joystick = self.joysticks[event.instance_id]
				if joystick.rumble(0, 0.7, 500):
					print(f"Rumble effect played on joystick {event.instance_id}")
			return True, True

		if event.type == pygame.JOYBUTTONUP:
			print("Joystick button released.")
			return True, True

		# Handle hotplugging
		if event.type == pygame.JOYDEVICEADDED:
			# This event will be generated when the program starts for every
			# joystick, filling up the list without needing to create them manually.
			joy = pygame.joystick.Joystick(event.device_index)
			self.joysticks[joy.get_instance_id()] = joy
			print(f"Joystick {joy.get_instance_id()} connencted")
			return True, True

		if event.type == pygame.JOYDEVICEREMOVED:
			del self.joysticks[event.instance_id]
			print(f"Joystick {event.instance_id} disconnected")
			return True, True

		return False, False
		

	def poll(self):
		self.thrust(100)
		# For each joystick:
		for joystick in self.joysticks.values():
			jid = joystick.get_instance_id()

			power_level = joystick.get_power_level()
			#print(f"Joystick's power level: {power_level}")

			# Usually axis run in pairs, up/down for one, and left/right for
			# the other. Triggers count as axes.
			axes = joystick.get_numaxes()
			#print(f"Number of axes: {axes}")

			for i in range(axes):
				axis = joystick.get_axis(i)
				#print(f" Axis {i} value: {axis:>6.3f}")

			self.handle_buttons(joystick)
			self.handle_hats(joystick)
			return

	def handle_buttons(self, joystick):

			buttons = joystick.get_numbuttons()

			for i in range(buttons):
				button = joystick.get_button(i)
				match i:
					case 0:
						if button == 1:
							self.world.zoom(-1)
						continue

					case 3:
						if button == 1:
							self.world.zoom(+1)
						continue
					
			return
	
	def handle_hats(self, joystick):
			# Hat position. All or nothing for direction, not a float like
			# get_axis(). Position is a tuple of int values (x, y).
			hats = joystick.get_numhats()
			#print(f" Number of hats: {hats}")
			for i in range(hats):
				hat = joystick.get_hat(i)
				horiz	= hat[0]
				vert	= hat[1]

				if horiz<0:
					self.world.pan_left()
					return

				if horiz>0:
					self.world.pan_right()
					return

				if vert<0:
					self.world.pan_down()
					return

				if vert>0:
					self.world.pan_up()
					return
				
				return	# Handle only the first active hat
			
			return
	def thrust(self, value):
		if self.vessel is None:
			return
		
		self.rpc.ioctl( self.vessel, 'motion.thrust', {
			'value': value
			})
		return
	
	def bearing(self, value):
		if self.vessel is None:
			return
		
		self.rpc.ioctl( self.vessel, 'motion.bearing', {
			'value': value
			})
		return
		

if __name__ == "__main__":
	test = Gamepad()

