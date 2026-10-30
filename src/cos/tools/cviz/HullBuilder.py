#!/usr/bin/python
# Filename: HullBuilder.py
# Description: Procedural 3D vessel models built from a ship class's principal dimensions

from .ShipClass import ShipClass
import threepp as tp
import math

# Accommodation layout by activity type: (centre, length) as fractions of the length, x forward
HOUSE_LAYOUT	= {
	"container":	(-0.38, 0.10),
	"bulk":			(-0.40, 0.10),
	"tanker":		(-0.40, 0.10),
	"gascarrier":	(-0.40, 0.10),
	"generalcargo":	(-0.35, 0.12),
	"carcarrier":	(-0.02, 0.92),
	"roro":			(-0.05, 0.75),
	"ferry":		( 0.00, 0.60),
	"fishing":		( 0.20, 0.25),
	"harbourcraft":	( 0.15, 0.35),
	"yacht":		( 0.05, 0.40),
	"motorboat":	(-0.05, 0.30),
	"auv":			None,
}
DEFAULT_LAYOUT	= (-0.10, 0.30)
EYE_HEIGHT		= 1.7		# Metres above the bridge deck
DECK_HEIGHT		= 2.8		# Metres per deck of the accommodation

class Vessel3D:
	def __init__(self, root:tp.Group, eye:tuple, ship:ShipClass):
		""" Constructor
		Arguments
			root -- Group holding the model, x forward, y up, origin at the waterline amidships
			eye -- Bridge eye point in the model frame
			ship -- Ship class the model was built from
		"""
		self.root	= root
		self.eye	= eye
		self.ship	= ship
		return

class HullBuilder:
	@staticmethod
	def build(ship:ShipClass, color:int):
		""" Builds a vessel model
		Arguments
			ship -- Ship class with the principal dimensions
			color -- Hull colour as 0xRRGGBB
		Returns
			A Vessel3D
		"""
		L, B, T		= ship.length, ship.width, ship.draft
		freeboard	= max( 1.0, 0.5*T + 0.01*L )

		root		= tp.Group()
		root.add( HullBuilder.mesh(HullBuilder.hull(L, B, T+freeboard), color, -T) )

		layout		= HOUSE_LAYOUT.get( ship.kind, DEFAULT_LAYOUT )
		if layout is None:			# Submerged craft: no accommodation, eye on the hull
			return Vessel3D( root, (0.3*L, freeboard+0.3, 0.0), ship )

		decks		= max( 1, min(8, round(L/40.0)) )
		height		= decks*DECK_HEIGHT
		centre, frac	= layout
		length		= frac*L
		house		= HullBuilder.mesh( tp.BoxGeometry(length, height, 0.8*B), 0xf2f2ee, 0.0 )
		house.position.set( centre*L, freeboard + height/2.0, 0.0 )
		root.add( house )

		# Bridge windows: a dark band across the front of the top deck
		band		= HullBuilder.mesh( tp.BoxGeometry(0.05, 0.4*DECK_HEIGHT, 0.78*B), 0x1a2430, 0.0 )
		band.position.set( centre*L + length/2.0 + 0.03, freeboard + height - 0.45*DECK_HEIGHT, 0.0 )
		root.add( band )

		# Eye just forward of the bridge front, so the house does not hide the bow
		eye			= ( centre*L + length/2.0 + 0.4, freeboard + height - DECK_HEIGHT + EYE_HEIGHT, 0.0 )
		return Vessel3D( root, eye, ship )

	@staticmethod
	def hull(L:float, B:float, H:float):
		""" Extrudes the waterplane outline of a hull: square transom, parallel body, pointed bow
		Arguments
			L -- Length overall
			B -- Breadth
			H -- Depth from keel to deck
		"""
		x0, x1, x2	= -L/2.0, L/2.0 - 0.3*L, L/2.0
		b			= B/2.0

		shape		= tp.Shape()
		shape.move_to( x0, -0.9*b )
		shape.line_to( x1, -b )
		shape.quadratic_curve_to( x2 - 0.05*L, -b, x2, 0.0 )
		shape.quadratic_curve_to( x2 - 0.05*L, b, x1, b )
		shape.line_to( x0, 0.9*b )
		shape.close_path()

		geometry	= tp.ExtrudeGeometry( [shape], depth=H, bevel_enabled=False, curve_segments=8 )
		geometry.rotate_x( -math.pi/2.0 )		# Outline in x/z, extruded up along y
		return geometry

	@staticmethod
	def mesh(geometry, color:int, y:float):
		""" Wraps a geometry in a lit mesh
		Arguments
			geometry -- Geometry
			color -- Colour as 0xRRGGBB
			y -- Height of the mesh origin
		"""
		material			= tp.MeshStandardMaterial()
		material.color		= color
		material.roughness	= 0.7
		mesh				= tp.Mesh( geometry, material )
		mesh.position.y		= y
		mesh.cast_shadow	= True
		return mesh


if __name__ == "__main__":
	test = HullBuilder()
