import sys, getopt
from mrtopo.logger import log
from mrtopo.structures import config, Topology
from mrtopo.translator import c_read
from mrtopo.interpreter import interpret

# from . import __version__ as version

VERSION_NUMBER = "0.0.1"


def options(argv: list):
    try:
        opts, args = getopt.getopt(argv, "hc:", ["configfile="])
    except getopt.GetoptError:
        print('Usage: mrtopo -c <configfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: mrtopo -c <configfile>')
            sys.exit()
        elif opt in ("-c", "--configfile"):
            return arg


def main(argv):
    config_file = options(argv)
    log('MrTopo.v.' + VERSION_NUMBER + '>')

    configuration = config.Config()  # initialize default config

    # translate
    if config_file:
        configuration = c_read(config_file)

    # interpret
    interpret(configuration)



if __name__ == "__main__":
    main(sys.argv[1:])
