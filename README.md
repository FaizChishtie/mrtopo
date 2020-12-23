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

1. Clone the repository or install the package through `pip`:

```
git clone https://github.com/FaizChishtie/mrtopo.git
```
Or
```
pip install mrtopo
```

2. Run the following code in the project root directory.

```
python3 setup.py develop
python3 mrtopo -p ./examples/temp_topo.py
```

This should create a `MrTopoGenerated` folder containing the mutated topology files generated from the `temp_topo.py` file.

3. Replace `./examples/temp_topo.py` with the path to your Mininet topology file.

## Further Notes

Further documentation is available on the [MrTopo GitHub pages site.](https://faizchishtie.github.io/mrtopo/)

## Links

* [PyPi MrTopo Package](https://pypi.org/project/mrtopo/)
