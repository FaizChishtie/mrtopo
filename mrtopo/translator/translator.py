"""
    MrTopo Translator - translates user input to interpretable data
"""

import json, glob, re
from mrtopo.logger import log
from mrtopo.error import ErrorIdentities, handle_error
from mrtopo.translator.mrtopoio import find_file, read_json

# Read a config file
def read(file):
    return read_json(file) #TODO Validation

