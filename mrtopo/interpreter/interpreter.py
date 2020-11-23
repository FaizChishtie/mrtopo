"""
    MrTopo Interpreter - interprets translated input to mutable data structures
"""

from mrtopo.logger import log
from mrtopo.structures import config, network


def interpret(cfg: config.Config):
    log('Interpreter - interpreting config')
    return c_construct_networks(cfg.topologies)


def interpret(py: dict):
    log('Interpreter - interpreting py file')
    return p_construct_networks(py)


def p_construct_networks(py: dict):
    return network.Network.p_build(py)


def c_construct_networks(topologies: list):
    networks = []
    for t in topologies:
        networks.append(network.Network.c_build(t))
    return networks
