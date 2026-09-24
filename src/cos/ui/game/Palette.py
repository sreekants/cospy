#!/usr/bin/python
# Filename: Palette.py
# Description: Standard blue colour theme for sea shapes, chosen by type code

# Sea shapes are coloured by what they are, not by the colour stored with each shape, so every
# map reads the same way. The SeaBuilder type codes fall into three families:
#
#   1xxxxx  physical water (seabed, bathymetry)   opaque blues shaded by depth
#   2xxxxx  jurisdiction (EEZ ... internal waters) outline only, like a chart's boundary lines
#   3xxxxx  traffic and regulation                 translucent blue-family tints over the water
#
# Only physical water is opaque, so depth always shows through the zones. The stored colour is
# used only for a type this table does not know.

# Depth (metres) -> colour: pale shallows to deep navy
DEPTH_RAMP	= [
	(0.0,	(214, 236, 250)),
	(5.0,	(186, 222, 247)),
	(10.0,	(160, 206, 242)),
	(20.0,	(128, 186, 234)),
	(50.0,	(92, 158, 219)),
	(100.0,	(60, 126, 196)),
	(200.0,	(34, 92, 160)),
	(500.0,	(20, 62, 120)),
]

# Type code -> (fill RGBA or None, outline RGBA or None). Alpha is 0..255.
ZONE_STYLES	= {
	# Jurisdiction: boundaries, not areas
	201000: (None,					(70, 100, 140, 150)),	# EXCLUSIVE_ECONOMIC_ZONE
	202000: (None,					(70, 100, 140, 150)),	# CONTIGUOUS_ZONE
	203000: (None,					(55, 85, 150, 200)),	# TERRITORIAL_SEA
	204000: (None,					(40, 70, 130, 220)),	# INTERNAL_WATERS
	205000: ((90, 100, 130, 90),	(60, 70, 100, 220)),	# MARITIME_EXCLUSION_ZONE

	# Traffic and regulation
	301000: ((40, 150, 170, 70),	(20, 110, 140, 200)),	# HARBOUR: teal-blue
	302000: ((120, 210, 235, 45),	(80, 170, 210, 110)),	# WATERWAY / fairway: faintest cyan
	303000: ((90, 100, 220, 75),	(60, 70, 190, 200)),	# TRAFFIC_SEPARATION_SCHEME lanes: blue-violet
	304000: ((90, 100, 220, 75),	(60, 70, 190, 200)),	# TRAFFIC_LANE
	305000: ((60, 50, 160, 120),	(40, 30, 130, 220)),	# SEPARATION_ZONE: deeper indigo
	306000: ((60, 50, 160, 120),	(40, 30, 130, 220)),	# ROUNDABOUT
	307000: ((140, 170, 220, 45),	(100, 130, 200, 160)),	# INSHORE_TRAFFIC_ZONE
	308000: ((110, 180, 240, 60),	(60, 140, 220, 200)),	# RECOMMENDED_ROUTE: sky blue
	309000: ((110, 180, 240, 60),	(60, 140, 220, 200)),	# DEEP_WATER_ROUTE
	310000: ((170, 160, 230, 50),	(120, 110, 210, 230)),	# PRECAUTIONARY_AREA: pale lavender-blue
	311000: ((100, 120, 150, 110),	(70, 90, 120, 230)),	# AREA_TO_AVOID: grey steel-blue
}


def is_physical(code:int)->bool:
	return 100000 <= code < 200000


def depth_colour(depth)->tuple:
	""" Colour for a physical water shape of the given nominal depth
	Arguments
		depth -- Depth in metres
	"""
	try:
		d	= max( 0.0, float(depth) )
	except (TypeError, ValueError):
		d	= 0.0

	for (d0, c0), (d1, c1) in zip(DEPTH_RAMP, DEPTH_RAMP[1:]):
		if d <= d1:
			f	= (d - d0) / (d1 - d0)
			return tuple( int(round(a + (b - a) * f)) for a, b in zip(c0, c1) )

	return DEPTH_RAMP[-1][1]


def zone_style(code:int):
	""" (fill, outline) RGBA pair for a zone type code, or None if the type is not in the table
	Arguments
		code -- SeaBuilder type code
	"""
	return ZONE_STYLES.get( code )
