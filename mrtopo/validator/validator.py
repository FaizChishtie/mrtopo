"""
    MrTopo Validator - validates MrTopo mutated topologies
"""

import os
from mrtopo.logger import log


def validate(file, name=None):
    log(f"Validating: {file}")

    if not name:
        name = extract_name(file)

    log(f"Topology name: {name}")

    construct(file, name)

    test(file)

    return bundle(file, "Some descriptor")


def construct(file, name):
    if os.geteuid() != 0:
        log(f"Root access is required to continue the execution of this script.")
    os.system(f'sudo mn --custom {file} --topo {name}')
    os.system('dump')
    os.system('exit')
    log(f"Success!")
    pass


def test(file):
    pass


def extract_name(file):
    with open(file, 'r') as f:
        _f = f.readlines()

    for line in _f:
        if line.__contains__('topos') and line.__contains__('{'):
            if line.__contains__("\'"):
                return line.split("\'")[1]
            elif line.__contains__('\"'):
                return line.split('\"')


def bundle(file, descriptor):
    return f"Bundle {file}:\n{descriptor}\n"
