"""
    MrTopo Network - data structure repr networks
"""

from mininet.topolib import TreeTopo, TorusTopo
from mininet.topo import LinearTopo, MinimalTopo
from mrtopo.structures.networks.ring.ring import RingTopo
from mrtopo.structures import Topology

class Network:
    def __init__(self):
        self.topology = None # used by mutator to generate networks following given topology's rules

    def __repr__(self):
        return "<Network Topology( " + str(self.topology.__class__) + " )>"

    def __eq__(self, other):
        return self.topology.__class__ == other.topology.__class__

    @staticmethod
    def build(topology: Topology):
        n = Network()
        # TODO MODULARIZE
        if topology == Topology.DEFAULT:
            pass # TODO
        elif topology == Topology.MINIMAL:
            n.topology = MinimalTopo()
        elif topology == Topology.LINEAR:
            n.topology = LinearTopo()
        elif topology == Topology.RING:
            n.topology = RingTopo()
        elif topology == Topology.TREE:
            n.topology = TreeTopo()
        elif topology == Topology.TORUS:
            n.topology = TorusTopo()
        return n