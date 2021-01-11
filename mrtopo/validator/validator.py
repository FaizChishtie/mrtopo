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

    construct(file, name)

    test(file, name, long)

    if long:
        res_f = ['dmp', 'bch', 'pga']
    else:
        res_f = ['dmp', 'bch']

    results = []

    for f in res_f:
        try:
            results.append(f'\t* Command: {find_cmd(f, file, name)}\n>>> <{open(f, "r").read()}>')
        except:
            results.append(f'\t* Command: {find_cmd(f, file, name)} - failed')

    log(f"Success!")

    descriptor = "Details:"

    for res in results:
        if res != "":
            descriptor += f"\n{res}\n"

    del_all()

    return bundle(file, descriptor)


def construct(file, name):
    if os.geteuid() != 0:
        log(f"Root access is required to continue the execution of this script.")
    res = call(f'sudo mn --custom {file} --topo {name} --test dump > dmp')
    return res


def test(file, name, long):
    benchmark = f"Benchmark:\n{call(f'sudo mn --custom {file} --topo {name} --test none > bch')}"
    if long:
        pingall = f"Pingall:\n{call(f'sudo mn --custom {file} --topo {name} --test pingall > pga')}"
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


def del_all():
    all = ['bch', 'pga', 'dmp']
    for f in all:
        try:
            os.remove(f)
        except FileNotFoundError:
            log(f'{f} does not exist')


def find_cmd(fn, file, name):
    if fn == 'bch':
        return f'sudo mn --custom {file} --topo {name} --test none > bch'
    elif fn == 'pga':
        return f'sudo mn --custom {file} --topo {name} --test pingall > pga'
    elif fn == 'dmp':
        return f'sudo mn --custom {file} --topo {name} --test dump > dmp'