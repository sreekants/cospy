#!/usr/bin/python
# Filename: VirtualWorld3D.py
# Description: 3D view of a running COS simulation, rendered with threepp

from cos.tools.cviz.RPCAgent import RPCAgent
from cos.tools.cviz.Dispatcher import Dispatcher
from cos.tools.cviz.ShipClass import ShipClass
from cos.tools.cviz.HullBuilder import HullBuilder
from cos.ui.game import Palette

from cos.core.api.World import World
from cos.core.network.ZMQTransport import ZMQTransport
from cos.core.utilities.ArgList import ArgList

import threepp as tp
import datetime, math, time

SKY_COLOR		= 0xa9c8de
SEA_COLOR		= 0x1f5873
LAND_HEIGHT		= 12.0		# Metres; the map has no elevation
ZONE_HEIGHT		= 0.3		# Metres above the sea a zone outline is drawn at
SMOOTHING		= 0.25		# Seconds for a vessel to settle on a vessel.move update
MIN_SPEED		= 0.05		# m/s below which the heading is held
LOOK_RATE		= 1.2		# Radians per second the deck view turns while an arrow key is held
RETRY_INTERVAL	= 3.0		# Seconds between attempts to reach a lost simulation
PROBE_TIMEOUT	= 1000		# Milliseconds a connection attempt waits for the simulation
PROBE_INTERVAL	= 1.0		# Seconds between checks that the simulation still answers
VESSEL_TYPES	= (100000, 200000, 300000, 400000)	# Fleet controllers (800000) have no hull
CAMERA_MODES	= ("orbit", "chase", "deck")

class Ship:
	def __init__(self, config:dict, model):
		""" Constructor
		Arguments
			config -- Vessel configuration from describe("world")
			model -- Vessel3D built for it
		"""
		self.guid		= config["guid"]
		self.name		= config.get("name", self.guid)
		self.model		= model
		pose			= (config.get("pose", None) or {}).get("position", None) or (0.0, 0.0)
		self.target		= [float(pose[0]), float(pose[1])]		# Map x, y in metres
		self.position	= list(self.target)
		self.heading	= 0.0		# Radians, the model's yaw
		self.target_heading	= 0.0
		self.speed		= 0.0
		self.intent		= ""
		return

	def move(self, args:dict):
		""" Takes a vessel.move update
		Arguments
			args -- Event arguments
		"""
		rect			= args["rect"]
		dx				= args["angle"]
		self.target		= [rect[0] + rect[2]/2.0, rect[1] + rect[3]/2.0]
		self.speed		= math.hypot( dx[0], dx[1] )
		intent			= args.get("intent", None) or []
		self.intent		= ", ".join( intent ) if isinstance(intent, (list, tuple)) else str( intent )
		if self.speed > MIN_SPEED:
			self.target_heading	= math.atan2( -dx[1], dx[0] )		# Map y is world z
		return

	def update(self, dt:float):
		""" Eases the model towards the last reported pose
		Arguments
			dt -- Seconds since the last frame
		"""
		k	= 1.0 - math.exp( -dt/SMOOTHING )
		for i in (0, 1):
			self.position[i]	+= k*(self.target[i] - self.position[i])
		turn			= (self.target_heading - self.heading + math.pi) % (2*math.pi) - math.pi
		self.heading	+= k*turn

		self.model.root.position.set( self.position[0], 0.0, self.position[1] )
		self.model.root.rotation.y	= self.heading
		return

	def to_world(self, local):
		""" Transforms a point in the model frame to the world
		Arguments
			local -- (x, y, z) in the model frame
		"""
		c, s	= math.cos(self.heading), math.sin(self.heading)
		return ( self.position[0] + local[0]*c + local[2]*s,
				 local[1],
				 self.position[1] - local[0]*s + local[2]*c )

class VirtualWorld3D:
	def __init__(self):
		""" Constructor
		"""
		self.world		= World()
		self.dispatch	= Dispatcher(self)

		self.mode		= "orbit"
		self.selected	= 0			# Index into self.order
		self.look		= [0.0, 0.0]	# Deck view yaw and pitch relative to the bow
		self.show_zones	= True
		self.keys		= {}		# Key -> held last frame, for edge detection

		self.connected		= False
		self.next_attempt	= 0.0
		self.next_probe		= 0.0
		self.attempts		= 0
		self.sim_time		= None
		self.content		= None
		self.reset()
		return

	def reset(self):
		""" Discards the world built from a simulation
		"""
		if self.content is not None:
			self.scene.remove( self.content )
		self.content	= None
		self.zones		= None
		self.ships		= {}		# guid -> Ship
		self.order		= []		# guids in selection order
		self.centre		= (0.0, 0.0)
		self.extent		= 1000.0
		return

	def run(self):
		""" Runs the viewer until its window closes
		"""
		self.init()
		self.dispatch.subscribe( "vessel.move", self.on_vessel_move )
		self.loop()
		return

	def init(self):
		""" Creates the window, the scene and the event socket
		"""
		self.canvas		= tp.Canvas( "COS 3D Visualizer", width=1280, height=720, antialiasing=4 )
		self.renderer	= tp.GLRenderer( self.canvas )

		self.scene		= tp.Scene()
		self.scene.background	= SKY_COLOR
		self.scene.add( tp.HemisphereLight(0xdfefff, 0x203040, 1.2) )
		sun				= tp.DirectionalLight( 0xfff4e0, 2.0 )
		sun.position.set( 3000.0, 4000.0, -2000.0 )
		self.scene.add( sun )

		material		= tp.MeshStandardMaterial()
		material.color	= SEA_COLOR
		material.roughness	= 0.35
		self.sea		= tp.Mesh( tp.PlaneGeometry(1.0, 1.0), material )
		self.sea.rotation.x	= -math.pi/2.0
		self.scene.add( self.sea )

		self.camera		= tp.PerspectiveCamera( 55.0, self.canvas.aspect(), 0.3, 60000.0 )
		self.controls	= tp.OrbitControls( self.camera, self.canvas )
		self.controls.enable_damping	= True

		self.font		= tp.FontLoader().default_font()
		self.hud		= tp.Scene()
		self.hud_camera	= tp.OrthographicCamera( 0, 1, 1, 0, -10, 10 )
		self.hud_text	= tp.Text2D( self.font, "", size=15 )
		self.hud_text.set_color( 0x10202c )
		self.hud.add( self.hud_text )
		self.resize( *self.canvas.size() )
		self.canvas.on_window_resize( self.resize )

		self.ipc		= RPCAgent()
		self.ipc.connect()
		return

	def resize(self, width, height):
		""" Fits the cameras to the window
		"""
		self.camera.aspect	= width/max(1, height)
		self.camera.update_projection_matrix()
		self.hud_camera.right	= width
		self.hud_camera.top		= height
		self.hud_camera.update_projection_matrix()
		self.hud_text.position.set( 16, height - 28, 0 )
		self.renderer.set_size( width, height )
		return

	def connect(self):
		""" Tries to reach the simulation and build its world
		Returns
			True if the world was built
		"""
		self.next_attempt	= time.time() + RETRY_INTERVAL
		self.attempts		= self.attempts + 1
		try:
			self.probe()
			self.reset()
			self.build()
		except Exception as e:
			if not isinstance(e, TimeoutError):
				print( f'Could not build the world: {e}' )
			self.reset()
			return False

		host, port		= ZMQTransport.get_host()
		print( f'Connected to the simulation on {host}:{port}: {len(self.ships)} vessels' )
		self.connected	= True
		self.attempts	= 0
		self.frame_all()
		return True

	def probe(self):
		""" Checks that the simulation answers, raising TimeoutError if it does not
		"""
		timeout	= self.world.transport.timeout
		self.world.transport.set_timeout( PROBE_TIMEOUT )
		try:
			self.world.play()
		finally:
			self.world.transport.set_timeout( timeout )
		self.next_probe	= time.time() + PROBE_INTERVAL
		return

	def disconnect(self):
		""" Drops the world of a simulation that stopped answering
		"""
		host, port		= ZMQTransport.get_host()
		print( f'Lost the simulation on {host}:{port}; retrying every {RETRY_INTERVAL:g} s' )
		self.connected		= False
		self.next_attempt	= time.time()
		self.reset()
		return

	def build(self):
		""" Builds the scene from the simulation's world description
		"""
		self.content	= tp.Group()
		self.zones		= tp.Group()
		self.content.add( self.zones )

		desc		= self.world.describe("world")
		objects		= desc.get("objects", None) or {}
		geography	= objects.get("geography", None) or {}

		bounds		= [math.inf, math.inf, -math.inf, -math.inf]
		for land in geography.get("land", None) or []:
			self.add_land( land, bounds )
		for sea in geography.get("sea", None) or []:
			self.add_zone( sea, bounds )

		for config in objects.get("vessels", None) or []:
			if config.get("type", None) not in VESSEL_TYPES:
				continue
			self.add_ship( config, bounds )

		if bounds[0] < bounds[2]:
			self.centre	= ( (bounds[0]+bounds[2])/2.0, (bounds[1]+bounds[3])/2.0 )
			self.extent	= max( bounds[2]-bounds[0], bounds[3]-bounds[1], 100.0 )

		size	= 6.0*self.extent		# Sea well past the map, so the horizon is water
		self.sea.scale.set( size, size, 1.0 )
		self.sea.position.set( self.centre[0], 0.0, self.centre[1] )
		self.scene.set_fog( SKY_COLOR, 0.5*self.extent, 3.0*self.extent )
		self.scene.add( self.content )
		return

	@staticmethod
	def points(config:dict):
		""" Returns the outline of a map shape as (x, y) points in metres
		"""
		points	= []
		for item in config["path"].split(' '):
			pt	= item.split(',')
			if len(pt) >= 2:
				points.append( (float(pt[0]), float(pt[1])) )
		return points

	@staticmethod
	def grow(bounds, points):
		""" Grows a [xmin, ymin, xmax, ymax] box to hold points
		"""
		for x, y in points:
			bounds[0], bounds[1]	= min(bounds[0], x), min(bounds[1], y)
			bounds[2], bounds[3]	= max(bounds[2], x), max(bounds[3], y)
		return

	@staticmethod
	def color(text, default:int):
		""" Converts #RRGGBB or 0xRRGGBB to an int
		"""
		if not text:
			return default
		try:
			return int( str(text).lstrip('#').replace('0x', ''), 16 )
		except ValueError:
			return default

	def add_land(self, config:dict, bounds):
		""" Extrudes a land polygon
		Arguments
			config -- Land shape configuration
			bounds -- Map bounds to grow
		"""
		points	= self.points( config )
		if len(points) < 3:
			return
		self.grow( bounds, points )

		shape		= tp.Shape( [tp.Vector2(x, y) for x, y in points] )
		geometry	= tp.ExtrudeGeometry( [shape], depth=LAND_HEIGHT, bevel_enabled=False )
		geometry.rotate_x( math.pi/2.0 )		# Map y to world z, extruded downwards

		material			= tp.MeshStandardMaterial()
		material.color		= self.color( config.get("color", None), 0x8a9a6a )
		material.roughness	= 0.95
		mesh				= tp.Mesh( geometry, material )
		mesh.position.y		= LAND_HEIGHT
		self.content.add( mesh )
		return

	def add_zone(self, config:dict, bounds):
		""" Outlines a maritime zone (harbour, fairway, TSS lane) on the water
		Arguments
			config -- Sea shape configuration
			bounds -- Map bounds to grow
		"""
		points	= self.points( config )
		if len(points) < 2:
			return
		self.grow( bounds, points )

		style	= Palette.zone_style( int(config.get("type", 0) or 0) )
		if (style is None) or (style[1] is None):
			return

		r, g, b	= style[1][:3]
		ring	= [tp.Vector3(x, ZONE_HEIGHT, y) for x, y in points]
		ring.append( ring[0] )
		material		= tp.LineBasicMaterial()
		material.color	= (r << 16) | (g << 8) | b
		self.zones.add( tp.Line(tp.BufferGeometry().set_from_points(ring), material) )
		return

	def add_ship(self, config:dict, bounds):
		""" Builds the model of a vessel
		Arguments
			config -- Vessel configuration
			bounds -- Map bounds to grow
		"""
		ship	= ShipClass.of( config )
		color	= self.color( ArgList(config.get("settings", None))['color'], 0x39c4f2 )
		model	= HullBuilder.build( ship, color )
		entry	= Ship( config, model )
		entry.update( 0.0 )
		self.grow( bounds, [tuple(entry.position)] )

		self.content.add( model.root )
		self.ships[entry.guid]	= entry
		self.order.append( entry.guid )
		return

	def on_vessel_move(self, args):
		""" Event handler for vessel.move
		Arguments
			args -- Event arguments
		"""
		if "time" in args:
			self.sim_time	= datetime.datetime.fromisoformat( args["time"] )
		ship	= self.ships.get( args["guid"], None )
		if ship is not None:
			ship.move( args )
		return

	def pressed(self, key:str):
		""" True on the frame a key goes down
		"""
		down			= self.canvas.is_key_down( key )
		was				= self.keys.get( key, False )
		self.keys[key]	= down
		return down and not was

	def handle_keys(self, dt:float):
		""" Camera mode, vessel selection, zones and the deck view's head
		Arguments
			dt -- Seconds since the last frame
		"""
		if self.pressed("ESCAPE"):
			self.canvas.close()

		if self.pressed("C"):
			self.mode	= CAMERA_MODES[ (CAMERA_MODES.index(self.mode)+1) % len(CAMERA_MODES) ]
			self.enter_mode()

		if self.order:
			step	= (1 if self.pressed("N") or self.pressed("TAB") else 0) - (1 if self.pressed("P") else 0)
			if step != 0:
				self.selected	= (self.selected + step) % len(self.order)
				self.look		= [0.0, 0.0]
				self.enter_mode()

		if self.pressed("Z") and self.zones is not None:
			self.show_zones		= not self.show_zones
			self.zones.visible	= self.show_zones

		if self.mode == "deck":
			yaw		= (1 if self.canvas.is_key_down("LEFT") else 0) - (1 if self.canvas.is_key_down("RIGHT") else 0)
			pitch	= (1 if self.canvas.is_key_down("UP") else 0) - (1 if self.canvas.is_key_down("DOWN") else 0)
			self.look[0]	+= yaw*LOOK_RATE*dt
			self.look[1]	= max( -1.2, min(1.2, self.look[1] + pitch*LOOK_RATE*dt) )
			if self.pressed("SPACE"):
				self.look	= [0.0, 0.0]
		return

	def selection(self):
		""" Returns the selected Ship, or None
		"""
		if not self.order:
			return None
		return self.ships[ self.order[self.selected % len(self.order)] ]

	def frame_all(self):
		""" Points the orbit camera at the whole map
		"""
		cx, cz	= self.centre
		self.camera.position.set( cx - 0.15*self.extent, 0.45*self.extent, cz + 0.6*self.extent )
		self.controls.target	= tp.Vector3( cx, 0.0, cz )
		self.controls.update()
		return

	def enter_mode(self):
		""" Places the camera for the current mode
		"""
		ship	= self.selection()
		self.controls.enabled	= self.mode != "deck"
		if self.mode == "orbit" or ship is None:
			self.frame_all()
		elif self.mode == "chase":
			L	= ship.model.ship.length
			x, y, z	= ship.to_world( (-1.6*L, 0.5*L, 0.6*L) )
			self.camera.position.set( x, y, z )
			self.chase_anchor	= list(ship.position)
		return

	def update_camera(self):
		""" Follows the selected vessel in the chase and deck modes
		"""
		ship	= self.selection()
		if ship is None or self.mode == "orbit":
			self.controls.update()
			return

		if self.mode == "chase":
			dx, dz	= ship.position[0] - self.chase_anchor[0], ship.position[1] - self.chase_anchor[1]
			self.chase_anchor	= list(ship.position)
			p	= self.camera.position
			self.camera.position.set( p.x + dx, p.y, p.z + dz )
			self.controls.target	= tp.Vector3( ship.position[0], 0.3*ship.model.ship.draft, ship.position[1] )
			self.controls.update()
			return

		ex, ey, ez	= ship.to_world( ship.model.eye )
		yaw			= ship.heading + self.look[0]
		pitch		= self.look[1]
		self.camera.position.set( ex, ey, ez )
		self.camera.look_at( ex + math.cos(yaw)*math.cos(pitch), ey + math.sin(pitch), ez - math.sin(yaw)*math.cos(pitch) )
		return

	def status(self):
		""" Text of the heads-up display
		"""
		clock	= self.sim_time.strftime('%d %H:%M:%S') if self.sim_time else '--'
		ship	= self.selection()
		if ship is None:
			return f'{clock}   [{self.mode}]   no vessels'

		course	= math.degrees( math.pi/2.0 - ship.heading ) % 360.0		# Clockwise from map north (-z)
		knots	= ship.speed*3600.0/1852.0
		return (f'{clock}   [{self.mode}]   {ship.name} ({ship.model.ship.name}, {ship.model.ship.length:.0f} m)'
				f'   {knots:.1f} kn   {course:03.0f} deg   {ship.intent}')

	def render(self, text:str):
		""" Draws the scene and the heads-up display
		"""
		self.hud_text.set_text( text )
		self.renderer.auto_clear	= True
		self.renderer.render( self.scene, self.camera )
		self.renderer.auto_clear	= False
		self.renderer.clear( False, True, False )
		self.renderer.render( self.hud, self.hud_camera )
		return

	def loop(self):
		""" Main loop
		"""
		clock	= tp.Clock()

		def frame():
			dt	= min( clock.get_delta(), 0.1 )
			if not self.connected:
				if time.time() >= self.next_attempt:
					self.ipc.drain()		# Events still queued from the previous run
					self.connect()
				host, port	= ZMQTransport.get_host()
				self.handle_keys( dt )
				self.render( f'Waiting for a simulation on {host}:{port} (attempt {self.attempts + 1})' )
				return

			try:
				self.ipc.pump( self.dispatch )
				if time.time() >= self.next_probe:
					self.probe()
			except TimeoutError:
				self.disconnect()
				return

			self.handle_keys( dt )
			for ship in self.ships.values():
				ship.update( dt )
			self.update_camera()
			self.render( self.status() )
			return

		self.canvas.animate( frame )
		return


if __name__ == "__main__":
	test = VirtualWorld3D()
