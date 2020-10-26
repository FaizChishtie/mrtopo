import sys, getopt
from mrtopo.logger import log
from mrtopo.structures import config, Topology

# from . import __version__ as version

VERSION_NUMBER = "0.0.1"

CONFIGURATION = config.Config()  # initialize default config


def options(argv):
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
    log(config_file, "HIGH")


if __name__ == "__main__":
    main(sys.argv[1:])
