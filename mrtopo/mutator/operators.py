from enum import Enum
from mrtopo.structures.mutantnetwork import MutantNetwork
from mrtopo.structures.network import Network
import random
import copy


class Operations(Enum):
    ADDLINK = 0
    ADDSWITCH = 1
    REMOVELINK = 2
    REMOVESWITCH = 3


def do(operation: Operations, network: Network, id: int):
    if operation == Operations.ADDLINK:
        return add_link(network, id)
    if operation == Operations.ADDSWITCH:
        return add_switch(network, id)
    if operation == Operations.REMOVELINK:
        return remove_link(network, id)
    if operation == Operations.REMOVESWITCH:
        return remove_switch(network, id)


def add_link(network: Network, id):
    description = "Added link"

    found = False

    s1 = None
    s2 = None

    attempts = 0

    not_attempted = copy.deepcopy(list(network.network.keys()))

    while not found:
        if attempts > len(network.switches):
            # ALL NODES LINKED TOGETHER
            # TODO ERROR
            return None

        s1 = random.choice(not_attempted)
        already_linked = network.network[s1]

        if len(already_linked) >= len(network.switches):
            not_attempted.remove(s1)
            continue
        else:
            not_attempted.remove(s1)

            tmp_arr = copy.deepcopy(not_attempted)

            for linked in already_linked:
                if linked in tmp_arr:
                    tmp_arr.remove(linked)

            s2 = random.choice(tmp_arr)

            if not network.link_exists(s1, s2):
                break

        attempts += 1

    network.add_link(s1, s2)

    description += " " + str([s1, s2])

    mn = MutantNetwork(network, id, description, Operations.ADDLINK)
    mn.add_modified_item([s1, s2])
    return mn


def add_switch(network: Network, id):
    description = "Added switch"

    added_switch = "MRTOPO_S"

    description += " " + added_switch

    random_switch = random.choice(list(network.network.keys()))  # choose switch to add link

    network.add_switch(added_switch)

    description += " and added link to " + random_switch

    network.add_link(added_switch, random_switch)  # add link

    mn = MutantNetwork(network, id, description, Operations.ADDSWITCH)
    mn.add_modified_item([added_switch, random_switch])
    return mn


def remove_link(network: Network, id):
    description = "Removed link"

    removed_link = random.choice(network.links)

    description += " " + str(removed_link)

    network.remove_link(removed_link[0], removed_link[1])

    mn = MutantNetwork(network, id, description, Operations.REMOVELINK)
    mn.add_modified_item(removed_link)
    return mn


def remove_switch(network: Network, id):
    description = "Removed switch"

    removed_switch = random.choice(network.switches)

    description += " " + str(removed_switch)

    network.remove_switch(removed_switch)

    mn = MutantNetwork(network, id, description, Operations.REMOVESWITCH)
    mn.add_modified_item(removed_switch)
    return mn
