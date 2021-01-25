"""
    MrTopo Tester - tests MrTopo mutated topologies
"""
import os
import shutil
import subprocess
from mrtopo.logger import log


def test(dir, target_file, command_file):

    mutated_file_paths = list_py_files(dir)

    made = False

    while not made:
        try:
            os.mkdir("MrTopoTest")
            made = True
        except OSError:
            log("MrTopoTest exists, removing")
            shutil.rmtree("MrTopoTest")

    f = open(f"MrTopoTest/original_topology.py", "x")
    f.close()
    shutil.copyfile(target_file, "MrTopoTest/original_topology.py")

    test_out = []

    for path in mutated_file_paths:
        out = log(f"Executing test with: {path}") + "\n"
        shutil.copyfile(path, target_file)
        out += call(f"sh {command_file}")
        test_out.append(out)

    shutil.copyfile("MrTopoTest/original_topology.py", target_file)
    return test_out


def list_py_files(dest):
    _dir = os.listdir(dest)
    py_file_paths = []
    for _file in _dir:
        n = len(_file)
        if _file[n - 2] + _file[n - 1] == "py":
            if dest[len(dest)-1] == "/":
                dest = dest[:-1]
            py_file_paths.append(f'{dest}/{_file}')
    return py_file_paths


def call(command):
    try:
        return log(subprocess.check_output(command, shell=True).decode('utf-8'))
    except subprocess.CalledProcessError:
        return log(f'Command: {command} - failed')