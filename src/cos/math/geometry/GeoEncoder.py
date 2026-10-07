#!/usr/bin/python
# Filename: GeoEncoder.py
# Description: Encodes GPS positions as Morton codes and geohashes, and decodes them back to cells

import math

BITS		= 30					# Bits per axis
CODE_BITS	= 2*BITS				# Bits in a Morton code; equals a 12-character geohash
ALPHABET	= '0123456789bcdefghjkmnpqrstuvwxyz'
LATITUDE	= (-90.0, 90.0)
LONGITUDE	= (-180.0, 180.0)

class GeoEncoder:
	""" Morton codes interleave longitude (upper bit of each pair) with latitude, so a code's bits
	are the bits of a geohash and a code's leading bits name the cell that holds it.
	"""

	@staticmethod
	def scale(value:float, low:float, high:float, bits:int=BITS)->int:
		""" Maps a coordinate to a cell index on an axis
		Arguments
			value -- Coordinate, degrees; clamped to [low, high]
			low -- Lower bound of the axis
			high -- Upper bound of the axis
			bits -- Bits on the axis
		Returns
			Index in [0, 2^bits - 1]
		"""
		value	= min( max( float(value), low ), high )
		cells	= 1 << bits
		return min( int( math.floor( (value - low) / (high - low) * cells ) ), cells - 1 )

	@staticmethod
	def unscale(index:int, low:float, high:float, bits:int=BITS)->tuple:
		""" Bounds of a cell on an axis
		Arguments
			index -- Cell index on the axis
			low -- Lower bound of the axis
			high -- Upper bound of the axis
			bits -- Bits on the axis
		Returns
			(lower, upper) in degrees
		"""
		step	= (high - low) / (1 << bits)
		return low + index*step, low + (index + 1)*step

	@staticmethod
	def spread(value:int)->int:
		""" Moves bit i of a 32-bit value to bit 2i
		"""
		value	&= 0xFFFFFFFF
		value	= (value | (value << 16)) & 0x0000FFFF0000FFFF
		value	= (value | (value << 8)) & 0x00FF00FF00FF00FF
		value	= (value | (value << 4)) & 0x0F0F0F0F0F0F0F0F
		value	= (value | (value << 2)) & 0x3333333333333333
		value	= (value | (value << 1)) & 0x5555555555555555
		return value

	@staticmethod
	def compact(value:int)->int:
		""" Moves bit 2i of a 64-bit value to bit i; the inverse of spread()
		"""
		value	&= 0x5555555555555555
		value	= (value | (value >> 1)) & 0x3333333333333333
		value	= (value | (value >> 2)) & 0x0F0F0F0F0F0F0F0F
		value	= (value | (value >> 4)) & 0x00FF00FF00FF00FF
		value	= (value | (value >> 8)) & 0x0000FFFF0000FFFF
		value	= (value | (value >> 16)) & 0x00000000FFFFFFFF
		return value

	@staticmethod
	def interleave(upper:int, lower:int)->int:
		""" Interleaves two axis indices into one code
		Arguments
			upper -- Index whose bits take the odd (upper) positions; longitude
			lower -- Index whose bits take the even positions; latitude
		"""
		return (GeoEncoder.spread( upper ) << 1) | GeoEncoder.spread( lower )

	@staticmethod
	def deinterleave(code:int)->tuple:
		""" Splits a code into its two axis indices; the inverse of interleave()
		Returns
			(upper, lower), i.e. (longitude index, latitude index)
		"""
		return GeoEncoder.compact( code >> 1 ), GeoEncoder.compact( code )

	@staticmethod
	def morton(lat:float, lon:float)->int:
		""" Encodes a position as a Morton code
		Arguments
			lat -- Latitude, degrees; clamped to [-90, 90]
			lon -- Longitude, degrees; clamped to [-180, 180]
		Returns
			Code in [0, 2^60 - 1]
		"""
		return GeoEncoder.interleave( GeoEncoder.scale( lon, *LONGITUDE ), GeoEncoder.scale( lat, *LATITUDE ) )

	@staticmethod
	def geohash(lat:float, lon:float, precision:int=12)->str:
		""" Encodes a position as a geohash
		Arguments
			lat -- Latitude, degrees
			lon -- Longitude, degrees
			precision -- Characters, 1 to 12
		"""
		return GeoEncoder.morton_to_geohash( GeoEncoder.morton( lat, lon ), precision )

	@staticmethod
	def morton_to_geohash(code:int, precision:int=12)->str:
		""" Spells the leading bits of a Morton code as a geohash
		Arguments
			code -- Morton code
			precision -- Characters, 1 to 12
		"""
		GeoEncoder.check_code( code )
		if not 1 <= precision <= CODE_BITS // 5:
			raise ValueError( f'GeoEncoder: geohash precision must be 1 to {CODE_BITS // 5}, not {precision}' )
		return ''.join( ALPHABET[(code >> (CODE_BITS - 5*(i + 1))) & 31] for i in range(precision) )

	@staticmethod
	def geohash_to_morton(text:str)->int:
		""" Converts a geohash to a Morton code; unused low bits are zero (the cell's south-west corner)
		Arguments
			text -- Geohash, 1 to 12 characters
		"""
		text	= str( text ).lower()
		if not 1 <= len(text) <= CODE_BITS // 5:
			raise ValueError( f'GeoEncoder: geohash must have 1 to {CODE_BITS // 5} characters, not {len(text)}' )
		code	= 0
		for c in text:
			index	= ALPHABET.find( c )
			if index < 0:
				raise ValueError( f'GeoEncoder: {c!r} is not a geohash character' )
			code	= (code << 5) | index
		return code << (CODE_BITS - 5*len(text))

	@staticmethod
	def cell(code:int, bits:int=CODE_BITS)->int:
		""" The cell id of a code: its leading bits
		Arguments
			code -- Morton code
			bits -- Leading bits kept; 2L gives cells L bits per axis wide
		"""
		GeoEncoder.check_code( code )
		GeoEncoder.check_bits( bits )
		return code >> (CODE_BITS - bits)

	@staticmethod
	def bounds(code, bits:int=None)->tuple:
		""" The cell named by the leading bits of a Morton code, or by a geohash
		Arguments
			code -- Morton code (int) or geohash (str)
			bits -- Leading bits that name the cell; defaults to all 60, or 5 per geohash character
		Returns
			(south, west, north, east) in degrees
		"""
		if isinstance( code, str ):
			bits	= 5*len(code) if bits is None else bits
			code	= GeoEncoder.geohash_to_morton( code )
		bits	= CODE_BITS if bits is None else bits
		GeoEncoder.check_code( code )
		GeoEncoder.check_bits( bits )

		lon, lat	= GeoEncoder.deinterleave( code )
		lon_bits	= (bits + 1) // 2				# Longitude takes the first bit
		lat_bits	= bits // 2
		west, east	= GeoEncoder.unscale( lon >> (BITS - lon_bits), *LONGITUDE, lon_bits )
		south, north	= GeoEncoder.unscale( lat >> (BITS - lat_bits), *LATITUDE, lat_bits )
		return south, west, north, east

	@staticmethod
	def centre(code, bits:int=None)->tuple:
		""" The centre of the cell named by a Morton code or a geohash
		Arguments
			code -- Morton code (int) or geohash (str)
			bits -- Leading bits that name the cell; as for bounds()
		Returns
			(latitude, longitude) in degrees
		"""
		south, west, north, east	= GeoEncoder.bounds( code, bits )
		return (south + north) / 2, (west + east) / 2

	@staticmethod
	def check_code(code:int):
		""" Raises ValueError unless code is a Morton code
		"""
		if not isinstance( code, int ) or not 0 <= code < (1 << CODE_BITS):
			raise ValueError( f'GeoEncoder: a Morton code is an integer in [0, 2^{CODE_BITS}), not {code!r}' )

	@staticmethod
	def check_bits(bits:int):
		""" Raises ValueError unless bits is a valid count of leading bits
		"""
		if not 0 <= bits <= CODE_BITS:
			raise ValueError( f'GeoEncoder: bits must be 0 to {CODE_BITS}, not {bits}' )


if __name__ == "__main__":
	test = GeoEncoder.geohash( 57.64911, 10.40744, 11 )
