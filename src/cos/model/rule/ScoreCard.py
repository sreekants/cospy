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

		return
	
	def load(self, ctxt, path:str):
		path			= ctxt.sim.config.resolve(path)
		config			= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(path) )
		self.scores		= config["scores"]
		
		self.basescore["penalty"]	= config.get("basescore", 0)
		return
	
	def evaluate(self, event:str):
		return self.scores.get(event, self.basescore)

if __name__ == "__main__":
	test = ScoreCard()

