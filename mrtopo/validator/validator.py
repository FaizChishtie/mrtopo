"""
    MrTopo Validator - validates MrTopo mutated topologies
"""

import os
import subprocess

from mrtopo.logger import log


def validate(file, name=None, long=False):
    log(f"Validating: {file}")

    if not name:
        name = extract_name(file)

    log(f"Topology name: {name}")

    build = construct(file, name)
    results = test(file, name, long)

    log(f"Success!")

    descriptor = f"Build Details:\n{build}\n"

    for res in results:
        descriptor += f"{res}\n"

    return bundle(file, descriptor)


def construct(file, name):
    if os.geteuid() != 0:
        log(f"Root access is required to continue the execution of this script.")
    res = call(f'sudo mn --custom {file} --topo {name}')
    call('exit')
    return res


def test(file, name, long):
    benchmark = f"Benchmark:\n{call(f'sudo mn --custom {file} --topo {name} --test none')}"
    if long:
        pingall = f"Pingall:\n{call(f'sudo mn --custom {file} --topo {name} --test pingall')}"
        return [benchmark, pingall]
    else:
        return [benchmark]


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

def call(command):
    try:
        return log(subprocess.check_output(command, shell=True).decode('utf-8'))
    except subprocess.CalledProcessError:
        return log(f'Command: {command} - failed')