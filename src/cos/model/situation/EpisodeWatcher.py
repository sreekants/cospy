#!/usr/bin/python
# Filename: EpisodeWatcher.py
# Description: Watches a sampled value per key, and posts its total and peak once an epoch across a threshold ends

EPOCH	= 10		# Default epoch length, in ticks


def epoch_of(config)->int:
	""" Epoch length from a faculty's configuration
	Arguments
		config -- ArgList or dict; its 'epoch' in ticks
	Returns
		The epoch, or EPOCH when the configuration gives none
	"""
	value	= config['epoch'] if (config is not None) and ('epoch' in config) else None
	return int( value ) if value is not None else EPOCH


class Epoch:
	""" One span of time a watched value spent across its threshold
	"""
	def __init__(self, key, start):
		""" Constructor
		Arguments
			key -- What the value is about, e.g. a vessel guid or an (own, target) pair
			start -- Time of the first sample across the threshold
		"""
		self.key		= key
		self.start		= start
		self.end		= None		# Time the epoch was found to have ended
		self.last		= start		# Last sample across the threshold
		self.peak		= None		# Worst value: highest, or lowest when watching below a threshold
		self.peak_at	= None
		self.detail		= None		# What the caller gave with the peak sample
		self.total		= 0.0		# Sum of the samples in the epoch
		self.samples	= 0
		self.reason		= None		# 'released', 'lapsed', 'span' or 'stop'
		return

	@property
	def mean(self)->float:
		""" Mean of the samples in the epoch
		"""
		return self.total / self.samples if self.samples else 0.0

	@property
	def duration(self):
		""" Time from the first sample to the end of the epoch
		"""
		return (self.end - self.start) if self.end is not None else None

	def summary(self)->dict:
		""" The epoch's figures, for a message payload
		"""
		return { 'start': self.start, 'end': self.end, 'duration': self.duration, 'samples': self.samples,
				 'total': self.total, 'mean': self.mean, 'peak': self.peak, 'peak_at': self.peak_at, 'reason': self.reason }

	def add(self, value, now, below:bool, detail=None):
		""" Adds a sample to the epoch
		Arguments
			value -- Sampled value
			now -- Time of the sample
			below -- True when lower values are worse
			detail -- Caller's context for the sample, kept when it is the peak
		"""
		self.total		+= value
		self.samples	+= 1
		worse	= (self.peak is None) or ((value < self.peak) if below else (value > self.peak))
		if worse:
			self.peak, self.peak_at, self.detail	= value, now, detail
		return


class EpisodeWatcher:
	""" Opens an epoch per key when a sampled value crosses a threshold, accumulates the value and its
	peak while the epoch lasts, and posts the epoch when it ends.
	"""
	def __init__(self, threshold:float, post, every=1, release=0, span=None, below:bool=False):
		""" Constructor
		Arguments
			threshold -- Value at which an epoch begins; crossing is inclusive
			post -- Function called with each Epoch as it ends
			every -- Interval between samples of one key, in the unit of the times given to observe()
			release -- Time a value may stay back across the threshold before the epoch ends
			span -- Longest epoch; a value still across the threshold then opens the next one. None: no limit
			below -- True to watch for values at or below the threshold, e.g. under-keel clearance
		"""
		self.threshold	= float( threshold )
		self.post		= post
		self.every		= every
		self.release	= release
		self.span		= span
		self.below		= below
		self.open		= {}		# Key -> Epoch in progress
		self.sampled	= {}		# Key -> time of its last sample
		self.offered	= {}		# Key -> time a value was last offered
		return

	def crosses(self, value)->bool:
		""" Whether a value is across the threshold
		Arguments
			value -- Sampled value
		"""
		return (value <= self.threshold) if self.below else (value >= self.threshold)

	def due(self, key, now)->bool:
		""" Whether a key is due a sample, and takes it when it is
		Arguments
			key -- What the value is about
			now -- Current time
		"""
		last	= self.sampled.get( key )
		if (last is not None) and (now - last < self.every):
			return False
		self.sampled[key]	= now
		return True

	def observe(self, key, value, now, detail=None):
		""" Offers a value; it is sampled when the key is due, and may open, extend or end an epoch
		Arguments
			key -- What the value is about
			value -- Current value; None when it cannot be observed, which is ignored
			now -- Current time, e.g. the simulation tick
			detail -- Caller's context for the sample, returned on the epoch when it is the peak
		"""
		if value is None:
			return
		self.offered[key]	= now
		if self.due( key, now ) == False:
			return

		epoch	= self.open.get( key )
		if (epoch is not None) and (self.span is not None) and (now - epoch.start >= self.span):
			self.close( key, now, 'span' )
			epoch	= None

		if self.crosses( value ):
			if epoch is None:
				epoch	= self.open[key]	= Epoch( key, now )
			epoch.add( value, now, self.below, detail )
			epoch.last	= now
			return

		if epoch is None:
			return

		if now - epoch.last >= self.release:
			self.close( key, now, 'released' )
		else:
			epoch.add( value, now, self.below, detail )
		return

	def close(self, key, now, reason:str):
		""" Ends a key's epoch and posts it
		Arguments
			key -- What the value is about
			now -- Time the epoch ended
			reason -- 'released', 'span' or 'stop'
		"""
		epoch	= self.open.pop( key, None )
		if epoch is None:
			return None

		epoch.end, epoch.reason	= now, reason
		self.post( epoch )
		return epoch

	def lapse(self, now, after=0):
		""" Ends the epochs of keys no longer offered a value, e.g. a pair gone out of range
		Arguments
			now -- Current time
			after -- Time a key may go without a value before its epoch ends
		"""
		for key in [k for k in self.open if now - self.offered.get(k, now) > after]:
			self.close( key, now, 'lapsed' )
		return

	def flush(self, now):
		""" Ends and posts every epoch still open, e.g. when the simulation stops
		Arguments
			now -- Time of the stop
		"""
		for key in list( self.open ):
			self.close( key, now, 'stop' )
		return


if __name__ == "__main__":
	test = EpisodeWatcher( 0.5, print )
