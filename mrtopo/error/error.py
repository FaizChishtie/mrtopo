"""
    MrTopo Error - identifies possible errors & handles output
"""

from enum import Enum
from mrtopo.logger import log

# Enum for error identities
class ErrorIdentities(Enum):
    UNDEFINED = -1
    BAD_JSON_INPUT = 1
    INVALID_CONFIG = 2
    

# Error handling method
def handle_error(e_type=ErrorIdentities.UNDEFINED, message=""):
    o_msg = "MrTopo Error - " + str(e_type.name) + "\n" + str(message)
    log(item=o_msg ,level=e_type.value)