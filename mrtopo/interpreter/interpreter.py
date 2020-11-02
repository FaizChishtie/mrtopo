"""
    MrTopo Interpreter - interprets translated input to mutable data structures
"""

from mrtopo.logger import log
from mrtopo.structures import config, network

def interpret(cfg: config.Config):
    log('Interpreter - Interpreting')
    networks = construct_networks(cfg.topologies)
    pass

def construct_networks(topologies: list):
    networks = []
    for t in topologies:
        networks.append(network.Network.build(t))
    return networks