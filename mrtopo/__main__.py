import sys, getopt
from mrtopo.logger import log
from mrtopo.structures import config, Topology
from mrtopo.mutator import mutate
from mrtopo.translator import c_read, p_read, m_write, desc_write
from mrtopo.interpreter import interpret
from mrtopo.util.filetype import FileType

__version__ = "0.0.8"

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
