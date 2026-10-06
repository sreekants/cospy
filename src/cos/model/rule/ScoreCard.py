#!/usr/bin/python
# Filename: ScoreCard.py
# Description: Implementation of a rule scorecard

import yaml

class ScoreCard:
	def __init__(self):
		self.reset()
		return

	def reset(self):
		self.scores		= {}
		self.basescore	= {
            "penalty": "0"        
        }
		self.weight		= 1.0		# Rw for every entry without a weight of its own (REQ.041 DOC-041-02)

		return
	
	def load(self, ctxt, path:str):
		path			= ctxt.sim.config.resolve(path)
		config			= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(path) )
		self.scores		= config["scores"]
		
		self.basescore["penalty"]	= config.get("basescore", 0)
		self.weight		= ScoreCard.number( config.get('weight', 1.0), f'{path}: weight' )
		return

	def weight_of(self, event:str)->float:
		""" Rw for an event: the entry's own weight, else the file's
		Arguments
			event -- Clause or event name
		"""
		entry	= self.scores.get( event, None ) or {}
		if entry.get( 'weight', None ) is None:
			return self.weight
		return ScoreCard.number( entry['weight'], f'{event}: weight' )

	@staticmethod
	def number(value, where:str)->float:
		""" A weight as a number, at least zero
		Arguments
			value -- Value as written in the score file
			where -- What declared it, for the message
		Raises
			ValueError when it is not a number or is negative
		"""
		try:
			weight	= float( value )
		except (TypeError, ValueError):
			raise ValueError( f'{where} is {value!r}, not a number' )
		if weight < 0.0:
			raise ValueError( f'{where} is {weight}, below zero' )
		return weight
	
	def evaluate(self, event:str):
		return self.scores.get(event, self.basescore)

	def lookup(self, event:str):
		""" The scorecard entry for an event, or None when it is unpriced
		Arguments
			event -- Clause or event name
		"""
		return self.scores.get(event, None)

if __name__ == "__main__":
	test = ScoreCard()

