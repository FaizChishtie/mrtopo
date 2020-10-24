"""
    MrTopo Translator - translates user input to interpretable data
"""

import json, glob, re
from src.log import log
from mrtopo.error import ErrorIdentities, handle_error
from mrtopo.translator.mrtopoio import find_file, read_json

# Read a config file
def read(file):
    cfg = read_json(file)
    pass

