"""
    MrTopo - Mutator - handles mutation of networks
"""
from mrtopo.logger import log
from mrtopo.structures.mutantnetwork import MutantNetwork
from mrtopo.mutator.operators import Operations, do
from shutil import copyfile
from math import floor
import random

GENERATIONS = 30


def mutate(network):
    log("Mutator - mutating network " + str(GENERATIONS) + " times")
    mutant_networks = []  # type MutantNetwork
    for i in range(GENERATIONS):
        operation = random.choice(list(Operations))
        mn = do(operation, network.deep_copy(), i)  # mutate deep copy of network
        if mn:
            mutant_networks.append(mn)
    log(mutant_networks)
    return mutant_networks


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
    deleted = []  # links to be removed

    for i in range(n_remove):
        deleted.append(random.choice(network_arr))

    return deleted
