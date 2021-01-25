# Mr. Topo

![Upload Python Package](https://github.com/FaizChishtie/mrtopo/workflows/Upload%20Python%20Package/badge.svg)
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
$ mrtopo
Usage: mrtopo [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  config-file        Generate mutations from a configuration file.
  mutate-and-test    Mutate and Test a Mininet Topology file.
  python-file        Mutate a Mininet python file.
  test-mutation-dir  Test a mutated set of networks (directory) against a...
  validate-dir       Validate a directory of Mininet topologies.
  validate-file      Validate a Mininet topology python file.
```

### Option 2: Clone the repo:

* Clone this repository
* In the project directory run `$ sh scripts/set-test-env.sh`
    * This creates a temporary venv where mrtopo will be installed
* Run `$ mrtopo --help`
    * If this doesn't work try `$ source tmpenv/bin/activate` and retry `$ mrtopo --help`

## Command-Line Options:

All MrTopo commands are executed in this format:

```
$ mrtopo [COMMAND] [OPTION] [ARGS]
```

To get help for any command, execute:

```
$ mrtopo [COMMAND] --help
```

MrTopo commands:
* `config-file`: *Not yet implemented* - Generate mutations from a configuration file.
* `python-file`: Mutate a Mininet python file.
* `mutate-and-test`: Mutate and Test a Mininet Topology file. 
* `test-mutation-dir`: Test a mutated set of networks (directory) against a given Mininet topology file.
* `validate-dir`: Validate a directory of Mininet topologies.
* `validate-file`:  Validate a Mininet topology python file.

Most `mrtopo` commands will use the option `-f` to specify (except for `validate-dir` which takes `-d` )

### Command: `python-file`

MrTopo command used to generate a folder of mutated mininet topologies.

#### Options:

* `-f, --file <path to python file>` [Required]: Accepts a Mininet topology file `.py`

#### Usage: 

> The topology file specified must be a [mininet topology](http://mininet.org/walkthrough/#custom-topologies).

```
$ mrtopo python-file -f some_topology.py
```

#### Help:
```
$ mrtopo python-file --help                                                                                                                              2 ↵  8209  22:19:58
Usage: mrtopo python-file [OPTIONS]

  Mutate a Mininet python file.

Options:
  -f, --file TEXT  Python file that MrTopo should mutate.  [required]
  --help           Show this message and exit.
```

#### Output:

* A `MrTopoGenerated` directory - containing:
    * Multiple `mrtopo_gen_topo_<#>.py` mutated topology files generated from the input python file.
    * A `desc.txt` file describing the mutation operation performed on each `mrtopo_gen_topo_<#>.py` file.

### Command: `config-file`

> Note: This option has **not yet been implemented**

#### Options:

* `-f, --file <path to configuration file>` [Required]: Accepts a MrTopo configuration file `.json`

#### Usage: 
```
mrtopo python-file -f some_config.json
```

#### Help:
```
$ mrtopo config-file --help                                                                                                                                ✔  8210  22:20:01
Usage: mrtopo config-file [OPTIONS]

  Generate mutations from a configuration file.

Options:
  -f, --file TEXT  MrTopo config file.  [required]
  --help           Show this message and exit.
```

----

### Command: `validate-file`

> Note: `validate-file` **will only run a [Mininet VM](http://mininet.org/download/#option-1-mininet-vm-installation-easy-recommended)**.

MrTopo command used to test the validity of a Mininet topology file. 

#### Options:

* `-f, --file <path to python file>` [Required]: Accepts a Mininet topology file `.py`
* `-t, --topology-name <string>` [Optional]: Name of topology found in python file.

Routine:

* `--not-long` [Optional] - *Default*: Execute short validation routine 
* `--long` [Optional]: Execute long validation routine 

#### Usage:

```
Base: 
$ mrtopo validate-file -f some_file.py

Base + Topology Name: 
$ mrtopo validate-file -f some_file.py -t 'att'

Base + Routine: 
$ mrtopo validate-file -f some_file.py --long

Base + Routine + Topology Name: 
$ mrtopo validate-file -f some_file.py -t 'att' --not-long
```

#### Help:
```
$ mrtopo validate-file --help
Usage: mrtopo validate-file [OPTIONS]

  Validate a Mininet topology python file.

Options:
  -f, --file TEXT           Validate a Mininet topology python file.   [required]
  -t, --topology-name TEXT  Name of topology found in python file. Example:
                            'topos = { 'someName': ... } - someName would be
                            the topology-name. Only use this option if you
                            know the topology name.

  --long / --not-long       Long test flag (i.e. pingall)
  --help                    Show this message and exit.
```

#### Output:

* A `validator.txt` file describing the validation operation performed on the specified mutation file.

### Command: `validate-dir`

> Note: `validate-dir` **will only run a [Mininet VM](http://mininet.org/download/#option-1-mininet-vm-installation-easy-recommended)**.

MrTopo command used to test the validity of a Mininet topology file. 

#### Options:

* `-d, --dir <path to directory of python files>` [Required]: Accepts directory of Mininet topology files 
  * Will only parse python files from given directory - folder can contain other files.
* `-t, --topology-name <string>` [Optional]: Name of topology found in python file.

Routine:

* `--not-long` [Optional] - *Default*: Execute short validation routine 
* `--long` [Optional]: Execute long validation routine 

#### Usage:

```
Base: 
$ mrtopo validate-dir -d some_dir/

Base + Topology Name: 
$ mrtopo validate-file -d some_dir/ -t 'att'

Base + Routine: 
$ mrtopo validate-file -d some_dir/ --long

Base + Routine + Topology Name: 
$ mrtopo validate-file -d some_dir/ -t 'att' --not-long
```

#### Help:
```
$ mrtopo validate-dir --help                                                                                                                               ✔  8213  22:40:45
Usage: mrtopo validate-dir [OPTIONS]

  Validate a directory of Mininet topologies.

Options:
  -d, --dir TEXT            Validate a directory of Mininet topologies.
                            [required]
  -t, --topology-name TEXT  Name of topology found in python file. Example:
                            'topos = { 'someName': ... } - someName would be
                            the topology-name. Only use this option if you
                            know that all python files in the specified
                            dirfollow the topology name given.
  --long / --not-long       Long test flag (i.e. pingall)
  --help                    Show this message and exit.
```

#### Output:

* A `validator.txt` file describing the validation operation performed on the each mutation file in the specified
directory.


----

### Command: `mutate-and-test`

MrTopo command used to mutate a Mininet topology and then execute a test on the outputs.

> Note: *depending on the command file provided* this command may only be able to execute on ONOS machines.

#### Options:

* `-f, --file <path to python file>` [Required]: Accepts a Mininet topology file `.py`
* `-cf, --command-file <path to bash file>` [Required]: Accepts a bash file

#### Usage: 

> The topology file specified must be a [mininet topology](http://mininet.org/walkthrough/#custom-topologies).

```
$ mrtopo mutate-and-test -f some_topology.py -cf some_commands.sh 
// note .sh is not required as long as the -cf file is a bash file
```

#### Help:
```
$ mrtopo mutate-and-test --help                                                                                                                              2 ↵  8209  22:19:58
Usage: mrtopo mutate-and-test [OPTIONS]

  Mutate and Test a Mininet Topology file.

Options:
  -f, --file TEXT           Python file that MrTopo should mutate.  [required]
  -cf, --command-file TEXT  Bash file that contains ONOS testing commands to
                            execute.  [required]

  --help                    Show this message and exit.
```

#### Output:

* A `MrTopoGenerated` directory - containing:
    * Multiple `mrtopo_gen_topo_<#>.py` mutated topology files generated from the input python file.
    * A `desc.txt` file describing the mutation operation performed on each `mrtopo_gen_topo_<#>.py` file.
* A `MrTopoTest` directory - containing:
    * A copy of the original topology should anything have gone wrong during testing.
    * A `test.txt` file detailing the output of each test

### Command: `test-mutation-dir`

MrTopo command used to test a mutated set of networks (directory) against a given Mininet topology file.

> Note: *depending on the command file provided* this command may only be able to execute on ONOS machines.

#### Options:

* `-f, --file <path to python file>` [Required]: Accepts a Mininet topology file `.py`
* `-cf, --command-file <path to bash file>` [Required]: Accepts a bash file

#### Usage: 

> The topology file specified must be a [mininet topology](http://mininet.org/walkthrough/#custom-topologies).

```
$ mrtopo mutate-and-test -d dir_of_mutated_files/ -tf original_topology -cf some_commands.sh 
// note .sh is not required as long as the -cf file is a bash file
```

#### Help:
```
$ mrtopo test-mutation-dir --help                                                                                                                              2 ↵  8209  22:19:58
Usage: mrtopo test-mutation-dir [OPTIONS]

  Test a mutated set of networks (directory) against a given Mininet
  topology file.

Options:
  -d, --dir TEXT            A directory of Mininet topologies.  [required]
  -tf, --target-file TEXT   Name of file that MrTopo mutated and should
                            substitute out during testing.  [required]

  -cf, --command-file TEXT  Bash file that contains ONOS testing commands to
                            execute.  [required]

  --help                    Show this message and exit.
```

#### Output:

* A `MrTopoTest` directory - containing:
    * A copy of the original topology should anything have gone wrong during testing.
    * A `test.txt` file detailing the output of each test

## Examples

1. Copy the `/examples/temp_topo.py` code to a local python file named `temp_topo.py`
2. Run `mrtopo python-file -f temp_topo.py`
3. This should create a `MrTopoGenerated` folder containing the mutated topology files generated from the `temp_topo.py` file.
4. Replace `temp_topo.py` with the path to your Mininet topology file.

## Further Notes

Further documentation is available on the [MrTopo GitHub pages site.](https://faizchishtie.github.io/mrtopo/)

## Links

* [PyPi MrTopo Package](https://pypi.org/project/mrtopo/)
* [Mininet Custom Topologies](http://mininet.org/walkthrough/#custom-topologies)
* [Mininet Downloads](http://mininet.org/download/)
