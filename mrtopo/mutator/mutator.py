"""
    MrTopo - Mutator - handles mutation of networks
"""

from mrtopo.translator import find_file
from mrtopo.logger import log
from shutil import copyfile
from math import floor
import random

LINKS_TO_REMOVE = 0

PATH_TO_TEMP = "./temp_topo.py"

def mutate(file):
    # copy file first

    generated_file_name = "./generated.py"

    copyfile(file, generated_file_name)

    # OPEN FILE STR
    # TODO MAKE MORE MODULAR

    switches = []
    links = []
    hosts = []

    # SORT
    _f = open(file, "r")
    i = 0
    for l in _f:
        if l.__contains__("self.addSwitch"):
            switches.append([l.strip(), i])
        if l.__contains__("self.addHost"):
            hosts.append([l.strip(), i])
        if l.__contains__("self.addLink"):
            links.append([l.strip(), i])
        i += 1

    _f.close()

    log("Number of Switches: " + str(len(switches)))
    log("Number of Links: " + str(len(links)))
    log("Number of Hosts: " + str(len(hosts)))

    switch_names = get_var_names(switches)
    host_names = get_var_names(hosts)

    log(switch_names)
    log(host_names)

    network = {}
    host_network = {}

    for name in switch_names:
        network[name] = []

    for name in host_names:
        host_network[name] = []

    for link in links:
        line = link[0]
        start = line.find("(")

        var_count = 0
        _link = ["", ""]
        for i in range(start + 1, len(line) - 1):
            if var_count == 2:
                break # TODO add options later
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

    log(network)
    log(host_network)

    # NETWORK HAS BEEN CONSTRUCTED

    # TIME TO RANDOMIZE

    n_switches_removed = floor(random.random()*(len(switches) - 5))

    log("Number of switches to remove: " + str(n_switches_removed))

    deleted = []

    for i in range(n_switches_removed):
        deleted.append(random.choice(switch_names))

    log("Deleted switches: " + str(deleted))

    commented_out_lines = []

    for del_switch in deleted:
        for switch in switches:
            line = switch[0]
            if line.__contains__(del_switch):
                commented_out_lines.append(switch)

        for host in hosts:
            line = host[0]
            if line.__contains__(del_switch):
                commented_out_lines.append(host)

        for link in links:
            line = link[0]
            if line.__contains__(del_switch):
                commented_out_lines.append(link)

        for switch in network[del_switch]:
            if not switch.__contains__("host"):
                if network[switch].__contains__(del_switch):
                    network[switch].remove(del_switch)

    for del_switch in deleted:
        if network.__contains__(del_switch):
            del network[del_switch]

    log("UPDATED NETWORK")
    log(network)

    # WRITE CHANGES TO ACTUAL

    log(commented_out_lines)

    generated_file_actual = open(generated_file_name, "r")
    g_file_line = generated_file_actual.readlines()

    generated_file_actual.close()

    for line in commented_out_lines:
        if not g_file_line[line[1]][0] == "#":
            g_file_line[line[1]] = "# " + g_file_line[line[1]]

    generated_file_actual = open(generated_file_name, "w")

    for line in g_file_line:
        generated_file_actual.write(line)

    generated_file_actual.close()

def get_var_names(coll):
    names = []
    for item in coll:
        name = ""
        for c in item[0]:
            if c == "=":
                break
            else:
                name += str(c)
        names.append(name.strip())
    return names

def mutated_lines(n_remove, network_arr):
    deleted = [] # links to be removed

    for i in range(n_remove):
        deleted.append(random.choice(network_arr))

    return deleted

def get_hosts_list(_file):
    py_file = open(_file)
    try:
        pass
    finally:
        py_file.close()
    return []

if __name__ == "__main__":
    mutate(PATH_TO_TEMP)