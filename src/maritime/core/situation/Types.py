#!/usr/bin/python
# Filename: Types.py
# Description: Enumerations and states of encounter situations that occur in shipping

from enum import Enum

class Encounter(Enum):
    """Enum for the different encountered situation types considered in the evaluation."""

    OP          = -3  # Other vessel/obstacle is passed by
    OTGW        = -2  # Overtaking situation - own ship is give way vessel
    CRGW        = -1  # Crossing situation - own ship is give way vessel
    NAR         = 0  # No applicable rules
    CRSO        = 1  # Crossing situation - own ship is stand on vessel
    OTSO        = 2  # Overtaking situation - own ship is stand on vessel
    HO          = 3  # Head on situation
    STAT        = 4  # Static obstacle

    CPA         = 1001  # Close-quarter approach


class EncounterStage(Enum):
    """Enum for the different COLREGS stages."""

    STAGE1 = -1  # No risk of collision
    STAGE2 = 0  # Risk of collision
    STAGE3 = 1  # Close-quarter situation
    STAGE4 = 2  # Immediate danger



if __name__ == "__main__":
	test = Types()


