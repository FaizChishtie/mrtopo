#!/usr/bin/env python3

from mrtopo.logger import log
from mrtopo.structures import config, Topology
from mrtopo.mutator import mutate
from mrtopo.translator import c_read, p_read, m_write, desc_write, list_write
from mrtopo.interpreter import interpret
from mrtopo.util.filetype import FileType
from mrtopo.validator.validator import validate
from mrtopo.tester.tester import test
import os

__version__ = "0.1.5"

def main_routine(args):

    log('MrTopo.v.' + __version__ + '>')

    _file, file_type = args

    if file_type == FileType.CONFIG:
        configuration = config.Config()  # initialize default config

        # translate
        if _file:
            configuration = c_read(_file)

        # interpret
        interpret(configuration)

    elif file_type == FileType.PYTHON:

        pyfile = None

        # translate
        if _file:
            pyfile = p_read(_file)

        network = None
        if pyfile:
            # interpret
            network = interpret(pyfile)

        mutant_networks = mutate(network)

        for mutant in mutant_networks:
            m_write(mutant, _file)

        desc_write(mutant_networks)


def validate_routine(args, name=None, long=False):
    log('MrTopo.v.' + __version__ + '-validator>')

    dest, file_type = args

    files = []

    if file_type == FileType.DIRECTORY:
        dir = os.listdir(dest)
        for _file in dir:
            n = len(_file)
            if _file[n-2] + _file[n-1] == "py":
                files.append(f'{dest}/{_file}')
    else:
        files.append(dest)

    descriptor = []

    for _file in files:
        descriptor.append(validate(_file, name, long))

    list_write(descriptor, "validator.txt")


def test_routine(dir, target_file, command_file):
    log('MrTopo.v.' + __version__ + '-tester>')

    results = test(dir, target_file, command_file)

    list_write(results, "MrTopoTest/test.txt")