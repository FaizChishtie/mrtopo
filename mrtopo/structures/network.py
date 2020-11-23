"""
    MrTopo Network - data structure repr networks
"""

from mininet.topolib import TreeTopo, TorusTopo
from mininet.topo import LinearTopo, MinimalTopo
from mrtopo.structures.networks.ring.ring import RingTopo
from mrtopo.structures import Topology
import copy


class Network:
    def __init__(self):
        self.raw = None  # dict lines
        self.topology = None  # used by mutator to generate networks following given topology's rules
        self.switches = []
        self.links = []
        self.hosts = []
        self.network = {}
        self.host_network = {}

    def init_network(self):
        for name in self.switches:
            self.network[name] = []

    def init_host_network(self):
        for name in self.hosts:
            self.host_network[name] = []

    def link_exists(self, s_1, s_2):
        return [s_1, s_2] in self.links

    def switch_exists(self, s):
        return s in self.switches

    def host_exists(self, h):
        return h in self.hosts

    def add_switch(self, s):
        if not self.switch_exists(s):
            host = s + "_host"
            self.switches.append(s)
            self.hosts.append(host)
            self.host_network[host] = [s]
            self.network[s] = [host]

    def remove_switch(self, s):
        if self.switch_exists(s):
            snet = None
            if s.__contains__("host"):
                snet = self.host_network
                self.hosts.remove(s)
            else:
                snet = self.network
                self.switches.remove(s)
            # TODO REMOVE FROM LINKS
            for key in list(snet.keys()):
                if snet[key].__contains__(s):
                    snet[key].remove(s)

    def add_link(self, s1, s2):
        if self.switch_exists(s1) and self.switch_exists(s2):
            if not self.link_exists(s1, s2):
                snet = None
                if s1.__contains__("host") or s2.__contains__("host"):
                    snet = self.host_network
                else:
                    snet = self.network

                self.add(s1, s2)
                self.add(s2, s1)
                self.links.append([s1, s2])
                self.links.append([s2, s1])

    def remove_link(self, s1: str, s2: str):
        if self.link_exists(s1, s2):
            snet = None
            if s1.__contains__("host") or s2.__contains__("host"):
                snet = self.host_network
            else:
                snet = self.network

            self.remove(s1, s2)
            self.remove(s2, s1)
            self.link_remove(s1, s2)

    def deep_copy(self):
        deep_copy = Network()
        deep_copy.raw = copy.deepcopy(self.raw)
        deep_copy.topology = copy.deepcopy(self.topology)
        deep_copy.switches = copy.deepcopy(self.switches)
        deep_copy.links = copy.deepcopy(self.links)
        deep_copy.hosts = copy.deepcopy(self.hosts)
        deep_copy.network = copy.deepcopy(self.network)
        deep_copy.host_network = copy.deepcopy(self.host_network)
        return deep_copy

    def remove(self, _from, switch):
        if _from.__contains__("host"):
            self.host_network[_from].remove(switch)
        else:
            self.network[_from].remove(switch)

    def link_remove(self, s1, s2):
        if [s1, s2] in self.links:
            self.links.remove([s1, s2])
        if [s2, s1] in self.links:
            self.links.remove([s2, s1])

    def add(self, _from, switch):
        if _from.__contains__("host"):
            self.host_network[_from].append(switch)
        else:
            self.network[_from].append(switch)

    def get_switches(self):
        return self.switches

    def get_hosts(self):
        return self.hosts

    def get_links(self):
        return self.links

    def __repr__(self):
        return "<Network Topology( " + str(self.topology.__class__) + " )>"

    def __eq__(self, other):
        return self.topology.__class__ == other.topology.__class__

    @staticmethod
    def build_links(links, n):

        network = n.network
        host_network = n.host_network
        for link in links:
            line = link["line_str"]
            start = line.find("(")

            var_count = 0
            _link = ["", ""]
            for i in range(start + 1, len(line) - 1):
                if var_count == 2:
                    break  # TODO add options later
                elif line[i] == ",":
                    var_count += 1
                else:
                    _link[var_count] += line[i]

            for i in range(len(_link)):
                _link[i] = _link[i].strip()

            for l in _link:
                _snet = None
                if l.__contains__("host"):
                    _snet = host_network
                else:
                    _snet = network

                for _l in _link:
                    if _l != l:
                        _snet[l].append(_l)

            n.links.append(_link)  # TODO SUPPORT LINKS FOR ALL

    @staticmethod
    def p_build(lines: dict):
        n = Network()
        n.raw = lines

        keys = list(lines.keys())

        n.switches = get_var_names(lines["switch_lines"])

        n.hosts = get_var_names(lines["host_lines"])

        n.init_network()
        n.init_host_network()

        Network.build_links(lines["link_lines"], n)

        return n

    @staticmethod
    def c_build(topology: Topology):
        n = Network()
        # TODO MODULARIZE
        if topology == Topology.DEFAULT:
            pass  # TODO
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


def get_var_names(coll):
    names = []
    for item in coll:
        name = ""
        for c in item['line_str']:
            if c == '=':
                break
            else:
                name += str(c)
        names.append(name.strip())
    return names
