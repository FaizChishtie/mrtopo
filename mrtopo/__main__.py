import sys
from src.logger.log import log
from . import __version__ as version

VERSION_NUMBER = version

def main():
    print('MrTopo.v.' + VERSION_NUMBER)

