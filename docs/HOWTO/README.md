# How To Use MrTopo

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


