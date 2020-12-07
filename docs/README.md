# Mr. Topo

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

![Upload Python Package](https://github.com/FaizChishtie/mrtopo/workflows/Upload%20Python%20Package/badge.svg)
