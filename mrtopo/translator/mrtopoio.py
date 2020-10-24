"""
    MrTopo - translator.mrtopoio - io handling
"""

import json, glob, re
from src.logger import log
from mrtopo.util.iofunctor import vald_def

# gets and validates input based on validator output - default returns True on all input
# on None invalid
def get_input(message, validator=vald_def):
    u_in = input(message)

    log('Validating ~' + u_in)

    if validator(u_in):
        log('\n~' + u_in + ' valid')
        return u_in
    
    log('Invalid input ~' + u_in + ' try again...')
    return None

# Function to read files of the type json 
def read_json(file):
    _json = None
    with open(file) as jfile:
        _json = json.load(jfile)
    return _json

# looks for file in current directory
def find_file(file):
    return glob.glob('./' + file)