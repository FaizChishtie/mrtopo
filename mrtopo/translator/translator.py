"""
    MrTopo Translator - translates user input to interpretable data
"""

from mrtopo.logger import log
from mrtopo.error import ErrorIdentities, handle_error
from mrtopo.translator.mrtopoio import find_file, read_json, open_read
from mrtopo.mutator.operators import Operations
from mrtopo.structures import config, mutantnetwork, network
from shutil import copyfile
from datetime import date
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

    return configuration  # TODO Validation


# Read a py file
def p_read(file: str):  # TODO ADD TESTS
    log('Translator - Reading: ' + file)
    _p = find_file(file)
    _d = {
        "switch_lines": [],
        "link_lines": [],
        "host_lines": []
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
    return {"line_str": line.strip(), "line_no": number}


def make_folder(name="MrTopoGenerated"):
    if not os.path.isdir(name):
        os.mkdir(name)
    return name


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
        new_switch = modified[0]
        link_switch = modified[1]
        switch_string = add_switch_string(new_switch, n_switches + 1)
        host_string = add_host_string(new_switch + "_host", n_hosts + 1)
        host_link_string = add_host_link_string(new_switch + "_host", new_switch)
        switch_link_string = add_link_string(new_switch, link_switch)

        for i in range(len(line_list)):
            if line_list[i].__contains__("self.addSwitch"):
                whitespace_len = len(line_list[i]) - len(line_list[i].strip()) - 1
                line_list.insert(i, ' ' * whitespace_len + switch_string)
                line_list.insert(i + 1, ' ' * whitespace_len + host_string)
                break

        for i in range(len(line_list)):
            if line_list[i].__contains__("self.addLink"):
                whitespace_len = len(line_list[i]) - len(line_list[i].strip()) - 1
                line_list.insert(i, ' ' * whitespace_len + host_link_string)
                line_list.insert(i + 1, ' ' * whitespace_len + switch_link_string)  # add host and new switch link
                break

    if operation == Operations.ADDLINK:
        link_string = add_link_string(modified[0], modified[1])
        for i in range(len(line_list)):
            if line_list[i].__contains__("self.addLink"):
                whitespace_len = len(line_list[i]) - len(line_list[i].strip()) - 1
                line_list.insert(i, ' ' * whitespace_len + link_string)
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


def desc_write(mutants: mutantnetwork.MutantNetwork, outfile="desc.txt"):  # create description doc for all cases

    out_lines = []
    today = date.today().strftime("%d/%m/%Y")
    out_lines.append("MrTopo network mutation description file.\n")
    out_lines.append("Generated on {}\n{}\n".format(today, '-' * 10))

    for m in mutants:
        out_lines.append("Case {}: {}\n".format(m.get_id(), m.get_operation()))
        out_lines.append("{}\n".format(m.get_description()))
        out_lines.append("Modified item(s): {}\n".format(m.get_modified_item()))
        out_lines.append("{}\n".format('-' * 10))

    path = make_folder() + "/" + outfile

    list_write(out_lines, outfile, path)


def list_write(out, outfile, path=None):

    if not path:
        path = outfile

    write_file = open(path, "w")

    for line in out:
        write_file.write(line)

    write_file.close()


def add_switch_string(name, number):
    return name + " = " + "self.addSwitch(" + "\'s" + str(number) + "\' ) # MRTOPO GENERATED LINE\n"


def add_host_string(name, number):
    return name + " = " + "self.addHost(" + "\'h" + str(number) + "\' ) # MRTOPO GENERATED LINE\n"


def add_link_string(s1, s2):
    return "self.addLink({}, {}, bw=10, delay='0.345064487693ms') # MRTOPO GENERATED LINE\n".format(s1,s2)
    # TODO randomize opts


def add_host_link_string(s1, s2):
    return "self.addLink({}, {}) # MRTOPO GENERATED LINE\n".format(s1, s2)  # TODO randomize opts
