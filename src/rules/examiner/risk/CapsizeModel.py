#!/usr/bin/python
# Filename: CapsizeModel.py
# Description: Bayesian capsize network for the ExtremeWeatherExaminer

# A small network, built with the same toolchain as the ASV risk model so the
# two stay editable the same way: structure here, conditional probabilities as
# numpy matrices with their parent order declared beside them.
#
#     payload  ---\
#                  >--- stability ---\
#     size     ---/                   >--- capsize
#     waves    ------------------------/
#     visibility ----------------------/
#
# Stability is an intermediate rather than four arrows straight into capsize:
# payload and size determine how tender a hull is before any weather acts on
# it, and separating the two halves keeps the capsize table at eighteen rows
# instead of thirty-six.
#
# PROVENANCE. Every number below is a PLACEHOLDER. They are monotone and
# sign-correct - more sea, less freeboard and worse visibility never lower the
# risk - so the network propagates sensibly, but none of them is calibrated
# against casualty data and none should be cited. Replace them with elicited
# or fitted tables; the matrices are the only thing that needs to change.
#
# Run this module to write config/risk/capsize.model.xdsl.

import os
import sys

import numpy as np
import pyagrum as gum

from cos.math.risk.ConditionalProbabilityTable import CPT, apply_all, binary, uniform

TODO	= 'PLACEHOLDER - not calibrated'

NODES = {
	'wave_height':	(['calm', 'moderate', 'severe'],		'Significant wave height'),
	'visibility':	(['good', 'poor'],						'Visibility'),
	'payload':		(['light', 'laden', 'overladen'],		'Payload state'),
	'vessel_size':	(['small', 'large'],					'Vessel size'),
	'stability':	(['stable', 'marginal', 'unstable'],	'Stability'),
	'capsize':		(['yes', 'no'],							'Capsize'),
}

EDGES = [
	('payload', 'stability'),
	('vessel_size', 'stability'),
	('stability', 'capsize'),
	('wave_height', 'capsize'),
	('visibility', 'capsize'),
]

TABLES = [
	# Inputs are uniform: every one of them is supplied as evidence on each
	# assessment, so the prior never shows.
	CPT('wave_height', [], uniform(1, 3), 'uniform by design'),
	CPT('visibility', [], uniform(1, 2), 'uniform by design'),
	CPT('payload', [], uniform(1, 3), 'uniform by design'),
	CPT('vessel_size', [], uniform(1, 2), 'uniform by design'),

	# P(stability | payload, size). A small hull is more sensitive to loading
	# than a large one, and an overladen small vessel is the worst case.
	CPT('stability', ['payload', 'vessel_size'], np.array([
		[0.90, 0.09, 0.01],		# light,     small
		[0.96, 0.03, 0.01],		# light,     large
		[0.70, 0.25, 0.05],		# laden,     small
		[0.88, 0.10, 0.02],		# laden,     large
		[0.25, 0.45, 0.30],		# overladen, small
		[0.55, 0.33, 0.12],		# overladen, large
	]), TODO),

	# P(capsize | stability, waves, visibility). Poor visibility does not
	# capsize a vessel by itself; it raises the risk by delaying the response
	# to a sea that would otherwise be handled, so its effect grows with the
	# sea state rather than adding a constant.
	CPT('capsize', ['stability', 'wave_height', 'visibility'], binary([
		0.0005,		# stable,   calm,     good
		0.0010,		# stable,   calm,     poor
		0.0060,		# stable,   moderate, good
		0.0120,		# stable,   moderate, poor
		0.0400,		# stable,   severe,   good
		0.0750,		# stable,   severe,   poor
		0.0020,		# marginal, calm,     good
		0.0040,		# marginal, calm,     poor
		0.0300,		# marginal, moderate, good
		0.0550,		# marginal, moderate, poor
		0.1800,		# marginal, severe,   good
		0.2900,		# marginal, severe,   poor
		0.0080,		# unstable, calm,     good
		0.0150,		# unstable, calm,     poor
		0.0900,		# unstable, moderate, good
		0.1600,		# unstable, moderate, poor
		0.4200,		# unstable, severe,   good
		0.6000,		# unstable, severe,   poor
	]), TODO),
]


def build():
	""" Assembles the capsize network and applies every table
	"""
	bn	= gum.BayesNet('Capsize risk (placeholder tables)')

	for node, (states, label) in NODES.items():
		bn.add( gum.LabelizedVariable(node, label, states) )

	for parent, child in EDGES:
		bn.addArc( parent, child )

	problems	= apply_all( bn, TABLES )
	if problems:
		raise ValueError( 'capsize tables rejected:\n  ' + '\n  '.join(problems) )

	return bn


def main(argv=None):
	""" Writes the network beside the other risk models
	"""
	argv	= argv or sys.argv[1:]
	default	= os.path.join( os.path.dirname(os.path.abspath(__file__)),
							os.pardir, os.pardir, os.pardir, os.pardir,
							'config', 'risk', 'capsize.model.xdsl' )
	path	= argv[0] if argv else os.path.normpath( default )

	bn		= build()
	gum.saveBN( bn, path )

	print( f'nodes {bn.size()}  arcs {bn.sizeArcs()}  parameters {bn.dim()}' )
	print( f'wrote {path}' )
	return 0


if __name__ == "__main__":
	sys.exit( main() )
