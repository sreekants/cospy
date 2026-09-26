#!/usr/bin/python
# Filename: CaseId.py
# Description: The case id that keys every recorded row, shared by the kernel and the scenario generator

import hashlib

BITS	= 52		# Exact in a float64, so tools that read ids as floats do not round them

def case_id(scenario)->int:
	""" The case id of a scenario key
	Arguments
		scenario -- The SCENARIO string, e.g. 'scenario-0:no/bergen/clearsky/ldta'
	Raises
		ValueError when the key is absent or empty
	"""
	if (scenario is None) or (str(scenario).strip() == ''):
		raise ValueError( 'SCENARIO is absent or empty; it identifies every recorded row (COS.003)' )

	digest	= hashlib.sha256( str(scenario).encode('utf-8') ).digest()
	return int.from_bytes( digest[:8], byteorder='big' ) >> (64 - BITS)


if __name__ == "__main__":
	print( case_id('scenario-0:tk/turkeli/clearsky/ldta,fleet') )
