#!/usr/bin/python
# Filename: EpochFaculty.py
# Description: Faculty that slices time into epoch episodes and posts each as an examination when it ends (REQ.051)

from maritime.practice.PracticeFaculty import PracticeFaculty
from maritime.core.episode.EpochEpisode import EpochEpisode
from cos.model.examiner.Examination import Examination, ExaminationType, EXAMINATION
from cos.model.rule.Context import Context as RuleContext
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList


class EpochFaculty(PracticeFaculty):
	LAST	= True		# Runs after the other practice faculties in a pass

	def __init__(self):
		""" Constructor
		"""
		PracticeFaculty.__init__( self )
		self.ticks		= 1
		self.episode	= None		# Open epoch episode
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Reads the length of an epoch
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes: ticks=<length of an epoch in ticks, default 1>
		"""
		self.ticks	= int( config['ticks'] or 1 )
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Adds this pass's active situations to the open epoch, posting it once it has lasted its ticks
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		tick	= ctxt.sim.tickcount()

		if (self.episode is not None) and self.episode.end( tick ):
			self.episode.context	= rule_ctxt
			self.post( ctxt, [self.TOPIC], EXAMINATION, Examination(ExaminationType.EPOCH_EPISODE, self.episode) )
			self.episode	= None

		if self.episode is None:
			self.episode	= EpochEpisode( self.ticks )
			self.episode.start( tick )

		for vessel in rule_ctxt.vessels or []:
			self.episode.observe( getattr(vessel, 'situations', None) or [] )
		return



if __name__ == "__main__":
	test = EpochFaculty()
