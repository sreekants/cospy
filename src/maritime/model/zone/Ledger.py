#!/usr/bin/python
# Filename: Ledger.py
# Description: The one write path for observed violations (Ro) into fact_concern

import datetime, yaml

from maritime.model.zone.ZoneRules import ZoneRules, SpatialZones
from cos.core.kernel.Context import Context

FACT		= 'fact_concern'

ZONES		= '$(CONFIG)/examiner/zones.yaml'
TERRITORY	= '$(SIMULATION)/risk.yaml'

# Who raised a finding
SOURCE_EXAMINER	= 'examiner'
SOURCE_COLREG	= 'colreg'
SOURCE_LOCAL	= 'local'


def seconds(now)->float:
	""" Simulation time as seconds
	Arguments
		now -- ctxt.sim.now(), a datetime or a number
	"""
	if isinstance( now, datetime.datetime ):
		return now.timestamp()

	try:
		return float( now )
	except (TypeError, ValueError):
		return 0.0


class FindingGuard:
	""" Counts a condition seen on every tick once per occurrence (REQ.019)
	"""
	SCOPES	= ('episode', 'change', 'interval')

	def __init__(self, scope='change', release=30.0, interval=None, dwell=0.0):
		""" Constructor
		Arguments
			scope -- One of SCOPES
			release -- Seconds unseen after which an occurrence has ended
			interval -- Seconds between repeats, 'interval' scope only
			dwell -- Seconds a condition must persist before it scores
		"""
		if scope not in self.SCOPES:
			raise ValueError( f'Unknown finding scope {scope!r}; expected one of {self.SCOPES}' )

		if (scope == 'interval') and not interval:
			raise ValueError( "Finding scope 'interval' needs an interval" )

		self.scope		= scope
		self.release	= float( release )
		self.interval	= float( interval ) if interval else None
		self.dwell		= float( dwell or 0.0 )
		self.entries	= {}		# key -> [first seen, last seen, last reported]
		self.pruned		= None
		return

	def admit(self, key, now)->bool:
		""" Records an observation and says whether it is a new finding
		Arguments
			key -- What the finding is about, e.g. (vessel, event, area)
			now -- Observation time, seconds
		"""
		self.prune( now )

		entry	= self.entries.get( key )
		if (entry is None) or self.ended( entry, now ):
			entry	= [now, now, None]
			self.entries[key]	= entry
		else:
			entry[1]	= now

		if entry[2] is None:
			if (now - entry[0]) < self.dwell:
				return False
			entry[2]	= now
			return True

		if (self.scope == 'interval') and ((now - entry[2]) >= self.interval):
			entry[2]	= now
			return True

		return False

	def clear(self, key):
		""" Ends an occurrence the examiner saw end
		Arguments
			key -- What the finding is about
		"""
		if self.scope != 'episode':
			self.entries.pop( key, None )
		return

	def ended(self, entry, now)->bool:
		""" Whether an occurrence has gone unseen long enough to have ended
		Arguments
			entry -- Guard entry
			now -- Current time, seconds
		"""
		if self.scope == 'episode':
			return False

		return (now - entry[1]) > self.release

	def prune(self, now):
		""" Drops ended occurrences so guard state stays bounded
		Arguments
			now -- Current time, seconds
		"""
		if self.scope == 'episode':
			return

		if (self.pruned is not None) and ((now - self.pruned) < self.release):
			return

		self.pruned		= now
		self.entries	= { k: e for k, e in self.entries.items()
							if not self.ended(e, now) }
		return

	def __len__(self):
		""" Number of occurrences being tracked
		"""
		return len( self.entries )


class Ledger:
	""" Records observed violations into fact_concern.
	"""
	_shared		= None

	@classmethod
	def shared(cls, ctxt:Context, owner:str):
		""" The ledger the rules share, loaded once from the default paths
		Arguments
			ctxt -- Simulation context
			owner -- Id of the first faculty asking, for the log
		"""
		if cls._shared is None:
			ledger	= cls()
			ledger.load( ctxt, owner )
			cls._shared	= ledger

		return cls._shared

	def __init__(self):
		""" Constructor
		"""
		self.rules		= ZoneRules()
		self.spatial	= SpatialZones()
		self.sea		= None
		return

	def load(self, ctxt:Context, owner:str, zones=None, territory=None):
		""" Loads the scorecard, the concern mapping and the spatial zones
		Arguments
			ctxt -- Simulation context
			owner -- Id of the faculty loading it, for the log
			zones -- Path to zones.yaml
			territory -- Path to the territory's risk.yaml
		Raises
			ValueError when a priced event maps to no concern
		"""
		self.rules.load( ctxt, zones or ZONES )

		problems	= self.rules.errors()
		for problem in problems:
			ctxt.log.error( owner, f'Concern mapping: {problem}' )

		if problems:
			raise ValueError( f'{owner}: {len(problems)} concern mapping problem(s) in {zones or ZONES}' )

		self.spatial	= self.load_spatial( ctxt, owner, territory or TERRITORY )
		return

	@staticmethod
	def load_spatial(ctxt:Context, owner:str, path:str)->SpatialZones:
		""" The territory's spatial zones - the i axis
		Arguments
			ctxt -- Simulation context
			owner -- Id of the faculty loading it, for the log
			path -- Path to the territory's risk.yaml
		"""
		try:
			resolved	= ctxt.sim.config.resolve( path )
			config		= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(resolved) )
		except Exception as e:
			ctxt.log.error( owner, f'No spatial zones from {path}: {e}' )
			return SpatialZones()

		risk		= (config or {}).get( 'risk', {} ) or {}
		spatial		= SpatialZones( risk.get('spatial_zones', {}) )

		for problem in spatial.errors():
			ctxt.log.error( owner, f'Spatial zones: {problem}' )

		return spatial

	def shapes(self, ctxt:Context, vessel):
		""" Map shapes enclosing a vessel
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel
		"""
		if self.sea is None:
			self.sea	= ctxt.sim.objects.get_all( "/World/Sea" )

		return ZoneRules.enclosing( self.sea, getattr(vessel, 'location', None) )

	def zone(self, shapes)->str:
		""" Spatial zone for a set of enclosing shapes - the i index
		Arguments
			shapes -- Map shapes enclosing the vessel
		"""
		return self.spatial.classify( shapes )

	@staticmethod
	def area(shapes)->str:
		""" A readable name for the innermost shape
		Arguments
			shapes -- Map shapes enclosing the vessel
		"""
		for shape in reversed( shapes or [] ):
			name	= getattr( shape, 'name', None )
			if name:
				return name

		return 'open water'

	@staticmethod
	def identify(vessel):
		""" The key a vessel's findings are attributed to: its guid
		Arguments
			vessel -- Vessel

		The guid, not the IMO (COS-029-02). Both are unique now, but the guid is
		unique by construction - it is what fleet membership already matches on
		- so attribution does not depend on the identity data staying repaired.

		The fallbacks matter as much as the preference. Every degradation here
		is to another value that still *distinguishes* vessels, because the
		failure this whole ticket is about is two vessels sharing one key. A
		fallback to a constant - '', or 0 - would recreate it exactly, and
		would do so silently, so there is none: an object carrying no
		distinguishing value at all yields its identity, which is unique per
		object.
		"""
		for attr in ( 'guid', 'recid', 'id' ):
			value	= getattr( vessel, attr, None )
			if value not in (None, '', 0):
				return str( value )

		for key in ( 'guid', 'id' ):
			try:
				value	= vessel.config[key]
			except (KeyError, TypeError, AttributeError):
				continue
			if value not in (None, '', 0):
				return str( value )

		# Nothing declared. The IMO is unique since COS-029-01, so it is a
		# usable last resort; failing that, the object's own identity keeps
		# distinct vessels distinct.
		imo	= Ledger.imo( vessel )
		return imo if imo else f'anon-{id(vessel):x}'

	@staticmethod
	def recid(vessel):
		""" Database id of a vessel: its IMO as an integer, as every fact table records it
		Arguments
			vessel -- Vessel
		Returns
			The IMO, or None when the vessel declares none
		"""
		value	= getattr( vessel, 'recid', None )
		if value is not None:
			return value

		try:
			return int( vessel.config['identifier']['imo'] )
		except (KeyError, TypeError, AttributeError, ValueError):
			return None

	@staticmethod
	def imo(vessel):
		""" IMO of a vessel as recorded, or '' when it declares none
		Arguments
			vessel -- Vessel

		A fleet controller carries FLEET-<hash8(guid)> rather than an IMO
		(COS-029-04), so this is a string in every case and is never parsed as
		a number.
		"""
		try:
			return str( vessel.config["identifier"]["imo"] )
		except (KeyError, TypeError, AttributeError):
			pass

		try:
			return str( vessel.imo )
		except (AttributeError, TypeError, ValueError):
			return ''

	def record(self, ctxt:Context, source:str, raiser:str, vessel, event:str,
			   shapes, penalty:float, value=0.0, concern=None)->bool:
		""" Writes one finding
		Arguments
			ctxt -- Simulation context
			source -- SOURCE_EXAMINER, SOURCE_COLREG or SOURCE_LOCAL
			raiser -- Id of the examiner or rule that raised it
			vessel -- Vessel in violation
			event -- Violation identifier
			shapes -- Map shapes enclosing the vessel
			penalty -- Penalty score; zero is not recorded
			value -- Quantity behind the violation
			concern -- Concern, when the caller knows it; else from the mapping
		Returns
			True when a row was written
		"""
		if not penalty:
			return False

		concern	= concern or self.rules.concern( event )
		if concern is None:
			ctxt.log.error( raiser, f'Violation {event!r} maps to no concern; not recorded' )
			return False

		# vessel_id is the vessel IMO, as in every fact table; field order matches fact_concern in maritime.xml
		ctxt.sim.data.push( FACT, (
			ctxt.sim.now(),
			self.recid( vessel ),
			source,
			raiser,
			event,
			self.area( shapes ),
			self.zone( shapes ),
			concern,
			float( penalty ),
			float( value ),
		) )

		return True


if __name__ == "__main__":
	test = FindingGuard()
