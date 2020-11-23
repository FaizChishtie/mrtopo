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
    return _enum.DEFAULT  # default must exist for enums passed in TODO


# Configuration for system
class Config:
    def __init__(self):
        self.plan = TestPlan.DEFAULT
        self.topologies = [TestPlan.DEFAULT]

    def __eq__(self, other):
        return other.plan == self.plan and other.topologies == self.topologies

    def __repr__(self):
        top = ""
        for t in self.topologies:
            top += str(t) + " "
        return "<Config Plan( " + str(self.plan) + " ) Topologies( " + top + ")>"

    # build config structure from json
    @staticmethod
    def build(_dict: dict):
        c = Config()

        if "plan" in _dict:
            c.plan = find_enum(_dict["plan"], TestPlan)

        if "topologies" in _dict:
            c.topologies.clear()
            topologies = _dict["topologies"]
            if type(topologies) is list:
                for t in topologies:
                    c.topologies.append(find_enum(t, Topology))
            elif type(topologies) is str:
                c.topologies.append(find_enum(topologies, Topology))
        return c
