"""
    MrTopo Translator - translates user input to interpretable data
"""

from mrtopo.logger import log
from mrtopo.error import ErrorIdentities, handle_error
from mrtopo.translator.mrtopoio import find_file, read_json, open_read
from mrtopo.mutator.operators import Operations
from mrtopo.structures import config, mutantnetwork, network
from shutil import copyfile
import os

# Read a config file
def c_read(file: str):
    log('Translator - Reading: ' + file)
    _j = find_file(file)
    _d = None

    if len(_j) == 1:
        _d = read_json(_j[0])
    else:
        pass
        # TODO ERROR
    if _d:
        configuration = config.Config.build(_d)
    else:
        configuration = config.Config()

    return configuration #TODO Validation

# Read a py file
def p_read(file: str): #TODO ADD TESTS
    log('Translator - Reading: ' + file)
    _p = find_file(file)
    _d = {
        "switch_lines" : [],
        "link_lines" : [],
        "host_lines" : []
    }
    o_rf = open_read(file)
    line_no = 0
    for l in o_rf:
        if l.__contains__("self.addSwitch"):
            _d["switch_lines"].append(to_line_obj(l, line_no))
        if l.__contains__("self.addHost"):
            _d["host_lines"].append(to_line_obj(l, line_no))
        if l.__contains__("self.addLink"):
            _d["link_lines"].append(to_line_obj(l, line_no))
        line_no += 1

    o_rf.close()
    return _d

def to_line_obj(line, number):
    return { "line_str" : line.strip(), "line_no" : number }

def make_folder():
    dir = os.path.dirname(os.path.realpath(__file__))
    dir_name = "MrTopoGenerated"
    path = os.path.join(dir, dir_name)
    if not os.path.isdir(path):
        os.mkdir(path)
    return path

def m_write(mutant: mutantnetwork.MutantNetwork, original_file: str):
    filename = "mrtopo_gen_topo_" + str(mutant._id) + ".py"

    path = make_folder() + "/" + filename

    copyfile(original_file, path)

    operation = mutant.get_operation()
    modified = mutant.get_modified_item()

    read_file = open(path, "r")
    line_list = read_file.readlines()

    read_file.close()

    n_switches = len(mutant.network.get_switches())
    n_hosts = len(mutant.network.get_hosts())

    if operation == Operations.ADDSWITCH:
        switch_string = add_switch_string(modified, n_switches + 1)
        host_string = add_host_string(modified + "_host", n_hosts + 1)
        link_string = add_link_string(modified + "_host", modified)

        for i in range(len(line_list)):
            if line_list[i].__contains__("self.addSwitch"):
                whitespace_len = len(line_list[i]) - len(line_list[i].strip()) - 1
                line_list.insert(i, ' '*whitespace_len + switch_string)
                line_list.insert(i+1, ' ' * whitespace_len + host_string)
                break

        for i in range(len(line_list)):
            if line_list[i].__contains__("self.addLink"):
                whitespace_len = len(line_list[i]) - len(line_list[i].strip()) - 1
                line_list.insert(i, ' '*whitespace_len + link_string)
                break

    if operation == Operations.ADDLINK:
        link_string = add_link_string(modified[0], modified[1])
        for i in range(len(line_list)):
            if line_list[i].__contains__("self.addLink"):
                whitespace_len = len(line_list[i]) - len(line_list[i].strip()) - 1
                line_list.insert(i, ' '*whitespace_len + link_string)
                break

    if operation == Operations.REMOVELINK:
        for i in range(len(line_list)):
            if line_list[i].__contains__(modified[0]) and line_list[i].__contains__(modified[1]) \
                    and line_list[i].__contains__("self.addLink"):
                line_list[i] = "# " + line_list[i]
                break

    if operation == Operations.REMOVESWITCH:
        for i in range(len(line_list)):
            if line_list[i].__contains__(modified):
                line_list[i] = "# " + line_list[i]

    line_list.insert(0, "# MRTOPO MODIFICATION DESCRIPTION:\n# " + mutant.get_description() + "\n")

    write_file = open(path, "w")

    for line in line_list:
        write_file.write(line)

    write_file.close()

def add_switch_string(name, number):
    return name + " = " + "self.addSwitch(" +  "\'s" + str(number) + "\' ) # MRTOPO GENERATED LINE\n"

def add_host_string(name, number):
    return name + " = " + "self.addHost(" +  "\'h" + str(number) + "\' ) # MRTOPO GENERATED LINE\n"

def add_link_string(s1, s2):
    return "self.addLink({}, {}, bw=10, delay='0.345064487693ms') # MRTOPO GENERATED LINE\n".format(s1, s2) # TODO randomize opts
