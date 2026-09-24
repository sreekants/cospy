#!/usr/bin/python
# Filename: World.py
# Description: Implementation of the virtual world.

from cos.tools.cviz.RPCAgent import RPCAgent
from cos.tools.cviz.Builder import Builder
from cos.tools.cviz.Dispatcher import Dispatcher
from cos.tools.cviz.Encoder import Encoder
from cos.tools.cviz.Keyboard import Keyboard
from cos.tools.cviz.Gamepad import Gamepad
from cos.ui.gui.Infobox import Infobox

from cos.core.api.World import World
from cos.core.kernel.ObjectManager import ObjectManager
from cos.core.kernel.ParameterManager import ParameterManager

import numpy as np
import math
import random
import pygame

from cos.ui.game.Config import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

from pygame.locals import (
    KEYDOWN,
    QUIT,
)

SEA_COLOR			= (135, 206, 250)

class VirtualWorld:
	def __init__(self):
		""" Constructor
		"""
		# Create groups to hold enemy sprites, cloud sprites, and all sprites
		# - self.vessel is used for collision detection and position updates
		# - self.terrains is used for position updates
		# - self.sprites isused for rendering
		self.groups = {}
		for type in ["vessel"]:
			self.groups[type] = []

		self.forces = {}
		for type in ["sea.current","sea.wave","wind.current"]:
			self.forces[type] = []

		self.reliefs	= []	# Traversable bodies (Sea)
		self.bodies		= []	# Obstructon bodies (Land)
		self.info		= Infobox()

		self.objects	= ObjectManager()
		self.parms		= ParameterManager()
		self.world		= World()
		self.dispatch	= Dispatcher(self)
		self.encoder	= Encoder()

		self.background	= None
		self.scaled		= None		# (scale, surface) cache of the background at the current zoom

		self.debug		= False
		self.show_zones	= True		# Ctrl+Z hides zone shapes (TSS, fairways, harbours...)
		self.zone_overlay	= None		# Translucent layer the zone shapes draw onto (Palette)
		self.relief_order	= None		# Draw order of self.reliefs, rebuilt when it changes
		return

	def run(self):
		""" Runs a simulation
		"""
		self.init()
		self.subscribe()
		self.loop()
		return

	def subscribe(self):
		""" Registrs for events on a remote simulation
		"""
		self.dispatch.subscribe("vessel.move", self.on_vessel_move)
		self.dispatch.subscribe("weather.update", self.on_weather_update)
		return

	def init(self):
		""" Initialize the simulation
		"""

		# Initialize pygame
		pygame.init()

		# Setup the clock for a decent framerate
		self.clock = pygame.time.Clock()

		# Create the screen object
		# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption("COS Simulation Vizualizer")

		# Create custom events for adding a new enemy and cloud
		self.ADD_VESSEL = pygame.USEREVENT + 1
		pygame.time.set_timer(self.ADD_VESSEL, 250)
		self.ADD_LAND = pygame.USEREVENT + 2
		pygame.time.set_timer(self.ADD_LAND, 1000)


		pygame.font.init()
		self.font = pygame.font.SysFont("helvetica", 12)

		# Initialize the infobox
		self.info.init()

		# Initialize I/O devices
		self.iodevice	= [Keyboard(self), Gamepad(self)]

		# Build the world
		builder	= Builder()
		builder.build( self )

		# Add the COS to the world
		bbox	= self.cos.rect
		rect	= [bbox.left, bbox.top, bbox.right-bbox.left, bbox.bottom-bbox.top]
		self.register( 'cos', self.cos )

		# Initialize communication
		self.ipc	= RPCAgent()
		self.ipc.connect()
		return


	def register(self, type, obj):
		""" Register an object on the object directory
		Arguments
			type -- Type of the object
			obj -- Object to register
		"""
		'''
			TODO: Some objects created in the client-side simulation needs to be initialized
			self.world.init({
				"guid": obj.guid,
				"type": type,
				"rect": rect
			})
		'''

		self.objects.register( f"/World/{type}", obj.guid, obj)
		return

	def handle_events(self):
		""" Handles simulation interaction events
		"""
		# Look at every event in the queue
		for event in pygame.event.get():
			# Did the user click the window close button? If so, stop the loop
			if event.type == QUIT:
				return False
			
			# Did the user hit a key?
			for dev in self.iodevice:
				handled, result	= dev.handle_event( event )
				if handled == False:
					continue

				return result
				
		return True


	def update(self):
		""" Updates the simulation UI
		"""
		# Update the position of our vessel and terrains if required
		# Remote updates are already sent asynchronously as events to on_event()

		return

	def render(self):
		""" Renders the screen
		"""

		# Clear the log
		self.info.clear()

		# Fill the screen with sky blue
		self.screen.fill(SEA_COLOR)

		# Zones draw onto one translucent overlay, blitted once below the vessels
		if (self.zone_overlay is None) or (self.zone_overlay.get_size() != self.screen.get_size()):
			self.zone_overlay	= pygame.Surface( self.screen.get_size(), pygame.SRCALPHA )
		self.zone_overlay.fill( (0, 0, 0, 0) )

		groups	= self.groups.values()
		# Prepare all the sprites (pre-rendering)
		for group in groups:
			for entity in group:
				entity.prepare(self, self.screen)

		# Painter's algorithm (render in layers)
		for layer in range(0,10):
			self.layer	= layer

			# Draw all our sprites
			for entity in self.draw_order():	# Background: water deepest first, then sky
				entity.render(self, self.screen)

			if layer == 0:						# Zones, over the water and under the vessels
				self.screen.blit( self.zone_overlay, (0, 0) )

			for group in self.forces.values():	# Physical forces
				for entity in group:
					entity.render(self, self.screen)

			for group in groups:				# Actors
				for entity in group:
					entity.render(self, self.screen)

			for entity in self.bodies:			# Foreground
				entity.render(self, self.screen)



		# Swap the screen
		self.cos.render(self, self.screen)

		# Prepare all the sprites (post-rendering)
		for group in groups:
			for entity in group:
				entity.commit(self, self.screen)


		# Overlay the map on top of all rendered artifacts, panned and zoomed with them
		if self.background:
			self.screen.blit( self.get_background(), self.encoder.transform_point((0, 0)) )

		for geography in [self.reliefs, self.bodies]:
			for entity in geography:
				entity.commit(self, self.screen)

		self.render_info()
		return

	def draw_order(self):
		""" Physical water from deepest to shallowest, so shallow bands stay visible, then the
		rest (zones draw onto the overlay, so their order does not matter), then sky
		"""
		if (self.relief_order is None) or (len(self.relief_order) != len(self.reliefs)):
			def key(entity):
				if getattr(entity, 'physical', False):
					return (0, -float(entity.depth or 0.0))
				if getattr(entity, 'zone', False):
					return (1, 0.0)
				return (2, float(getattr(entity, 'depth', 0.0) or 0.0))
			self.relief_order	= sorted( self.reliefs, key=key )
		return self.relief_order

	def get_background(self):
		""" Returns the background scaled to the current zoom, rescaling only when the zoom changes
		"""
		scale	= self.encoder.transform[0][0]
		if scale == 1.0:
			return self.background

		if (self.scaled is None) or (self.scaled[0] != scale):
			w, h		= self.background.get_size()
			surface		= pygame.transform.scale( self.background, (int(w*scale), int(h*scale)) )
			surface.set_colorkey( self.background.get_colorkey() )
			self.scaled	= (scale, surface)

		return self.scaled[1]

	def render_info(self):
		self.info.render(self)
		return
	

	def listen(self):
		""" Polls for events in the simulation
		"""
		# Pump simulation events
		self.ipc.pump( self.dispatch )

		# Process events in the queue
		if self.handle_events() == False:
			return False

		# Get the set of keys pressed and check for user input
		pressed_keys = pygame.key.get_pressed()
		self.cos.update(self, pressed_keys)

		# Continuous input (held keys)
		for dev in self.iodevice:
			if hasattr(dev, 'poll'):
				dev.poll(pressed_keys)
		return True

	def play(self):
		""" Runs the simulation logic
		"""
		if self.world.play() == False:
			# If so, remove the COS
			self.cos.kill()

			# Stop any moving sounds and play the collision sound
			self.forward_thrust.stop()
			self.reverse_thrust.stop()
			self.collision_sound.play()

			# Stop the loop
			return False

		return True

	def loop(self):
		""" Main simulation loop
		"""
		# Our main loop
		while True:
			# Listen and handle events
			if self.listen() == False:
				break

			# Update the animation
			self.update()

			# Render the sprites
			self.render()

			# Handle game logic
			if self.play() == False:
				break

			# Flip everything to the display
			pygame.display.flip()

			# Ensure we maintain a 30 frames per second rate
			self.clock.tick(30)

		# At this point, we're done, so we can stop and quit the mixer
		pygame.mixer.music.stop()
		pygame.mixer.quit()


	def on_vessel_move(self, args):
		""" Event handler for vessel_move
		Arguments
			args -- List of arguments
		"""
		guid	= args["guid"]

		groups	= self.groups.values()
		for group in groups:
			for entity in group:
				if entity.guid != guid:
					continue

				rect	= args["rect"]
				dx		= args["angle"]

				'''' Commented out (TODO: Remove the black background on BLIT)
				theta	= math.degrees(math.atan2(dx[1], -dx[0]))
				entity.rotate( theta )
				'''

				# Keep map coordinates; Sprite.render transforms them each frame, so a
				# vessel stays aligned with the map while panning or zooming
				entity.rect		= pygame.Rect( rect )
				entity.angle	= math.degrees( math.atan2(-dx[1],dx[0]) )
				entity.intent	= args["intent"]
				return

		return

	def on_weather_update(self, args):
		""" Event handler for weather_update
		Arguments
			args -- List of arguments
		"""
		guid	= args["guid"]
		ctxt	= None
		
		groups	= self.forces.values()
		for group in groups:
			for system in group:
				if system.guid != guid:
					continue

				system.update(self, args)
				return

		return


	def pan_up(self):
		self.encoder.translate(0.0, -5.0)
		return
	
	def pan_down(self):
		self.encoder.translate(0.0, +5.0)
		return
	
	def pan_left(self):
		self.encoder.translate(-5.0, 0.0)
		return
	
	def pan_right(self):
		self.encoder.translate(+5.0, 0.0)
		return

	def zoom(self, direction, step=1.2):
		match direction:
			case 1:
				self.encoder.zoom(step)

			case -1:
				self.encoder.zoom(1.0/step)

		return

	def toggle_zones(self):
		self.show_zones	= False if self.show_zones else True
		return

	def toggle_debug(self):
		self.debug	= False if self.debug else True
		
		self.info.show(self.debug)
		return

	def select(self, vessel):
		for dev in self.iodevice:
			dev.vessel	= vessel

		return

		

if __name__ == "__main__":
	test = World()


