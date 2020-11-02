"""
    MrTopo Translator - translates user input to interpretable data
"""

from mrtopo.logger import log
from mrtopo.error import ErrorIdentities, handle_error
from mrtopo.translator.mrtopoio import find_file, read_json
from mrtopo.structures import config


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

    return configuration #TODO Validation

def m_write(networks):
    pass