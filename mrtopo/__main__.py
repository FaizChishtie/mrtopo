import sys, getopt
from mrtopo.logger import log
from mrtopo.structures import config, Topology
from mrtopo.mutator import mutate
from mrtopo.translator import c_read, p_read, m_write
from mrtopo.interpreter import interpret
from mrtopo.filetype import FileType

# from . import __version__ as version

VERSION_NUMBER = "0.0.1"


def options(argv: list):
    try:
        opts, args = getopt.getopt(argv, "hc:p", ["configfile="])
    except getopt.GetoptError:
        print('Usage: mrtopo -c <configfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: mrtopo -c <configfile>\n\t-p <pyfile>')
            sys.exit()
        elif opt in ("-p", "--pyfile"):
            return (args[0], FileType.PYTHON)
        elif opt in ("-c", "--configfile"):
            return (args[0], FileType.CONFIG)


def main(argv):
    log('MrTopo.v.' + VERSION_NUMBER + '>')

    _file, file_type = options(argv)

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

if __name__ == "__main__":
    main(sys.argv[1:])
