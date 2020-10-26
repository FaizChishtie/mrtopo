"""
    MrTopo Config - data structure for config files
"""
from mrtopo.structures.topology import Topology
from enum import Enum
from mrtopo.logger import log
import json

# Following https://wiki.onosproject.org/display/ONOS/Test+Plans
class TestPlan(Enum):
    DEFAULT = 0
    # CORE
    CHO = 1
    HA = 2
    FUNC = 3
    SPCF = 4
    PLAT = 5
    SAMP = 6
    USECASE = 7

    def __str__(self):
        return self.name

def find_enum(name, _enum):
    for item in _enum:
        if name == item.name:
            return item
    return _enum.DEFAULT # default must exist for enums passed in TODO


# Configuration for system
class Config():

    def __init__(self):
        plan = TestPlan.DEFAULT
        topologies = [Topology.DEFAULT]

    # build config structure from json
    @staticmethod
    def build(_dict):
        c = Config()
        c.plan = find_enum(_dict["plan"], TestPlan)
        c.topologies = []

    