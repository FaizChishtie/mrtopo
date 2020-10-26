"""
    MrTopo Topology - enum type for topologies
"""

from enum import Enum


# Enum for topologies
class Topology(Enum):
    DEFAULT = 0
    RING = 1
    ATT = 2
    CHORDAL = 3
    LEAF_SPINE = 4
