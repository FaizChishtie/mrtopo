"""
    MrTopo Validator - validates MrTopo mutated topologies
"""

from mrtopo.logger import log

def validate(file):
    log(f"Validating: {file}")

    construct(file)

    test(file)

    return bundle(file, "Some descriptor")

def construct(file):
    pass

def test(file):
    pass

def bundle(file, descriptor):
    return f"Bundle {file}:\n{descriptor}\n"