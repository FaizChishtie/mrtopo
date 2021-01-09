# Mr. Topo

[![PyPI version badge](https://img.shields.io/pypi/v/mrtopo)](https://pypi.org/project/mrtopo/)
[![PyPI Status Badge](https://img.shields.io/pypi/status/mrtopo)](https://pypi.org/project/mrtopo/)
[![License](https://img.shields.io/github/license/faizchishtie/mrtopo)](https://github.com/faizchishtie/mrtopo/blob/master/LICENSE)
[![Downloads per month](https://img.shields.io/pypi/dm/mrtopo)](https://pypi.org/project/mrtopo/)

* Author: Faizaan Chishtie

## Description

MrTopo is a python application that generates mutant Mininet topology files for network testing purposes.

MrTopo is developed in conjunction with the IoT research being conducted by [Dr. Shiva Nejati](https://engineering.uottawa.ca/people/nejati-shiva) at the University of Ottawa.

## Basic Usage

### Option 1: Install the package through `pip`:

```
$ pip install mrtopo
```

* Run the following:

```
$ mrtopo --help
Usage: mrtopo [OPTIONS]

Options:
  -p, --pythonfile TEXT  Python file that MrTopo should mutate.
  -c, --configfile TEXT  MrTopo config file.
  --help
```

### Option 2: Clone the repo:

* Clone this repository
* In the project directory run `$ sh set-test-env.sh`
    * This creates a temporary venv where mrtopo will be installed
* Run `$ mrtopo --help`
    * If this doesn't work try `$ source tmpenv/bin/activate` and retry `$ mrtopo --help`

## Examples

1. Copy the `/examples/temp_topo.py` code to a local python file named `temp_topo.py`
2. Run `mrtopo -p temp_topo.py`
3. This should create a `MrTopoGenerated` folder containing the mutated topology files generated from the `temp_topo.py` file.
4. Replace `temp_topo.py` with the path to your Mininet topology file.

## Further Notes

Further documentation is available on the [MrTopo GitHub pages site.](https://faizchishtie.github.io/mrtopo/)

## Links

* [PyPi MrTopo Package](https://pypi.org/project/mrtopo/)
