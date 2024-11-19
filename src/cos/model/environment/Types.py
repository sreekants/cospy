#!/usr/bin/python
# Filename: Types.py
# Description: Implementation of the Types class

from enum import Enum

class DynamicForce(Enum):
    SEA_CURRENT     = 1
    WIND_CURRENT    = 2
    SEA_WAVE        = 3



if __name__ == "__main__":
	test = DynamicForce()


