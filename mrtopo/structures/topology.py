"""
    MrTopo Topology - enum type for topologies
"""

from enum import Enum


# Enum for topologies
class Topology(Enum):
    DEFAULT = 0
    MINIMAL = 1
    LINEAR = 2
    TREE = 3
    RING = 4
    TORUS = 5
