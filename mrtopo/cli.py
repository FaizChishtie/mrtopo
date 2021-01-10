import click
from mrtopo.__main__ import main_routine, validate_routine
from mrtopo.util.filetype import FileType

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group()
def cli():
    '''
    MrTopo is a python application that generates mutant Mininet topology files for network testing purposes.
    To get information on specific subcommands, use `mrtopo [COMMAND] --help`.
    '''
    pass


@click.group()
def mutator():
    '''
    MrTopo mutator
    '''
    pass


@click.command()
@click.option('-f', '--file', type=str, required=True, help="Python file that MrTopo should mutate.")
def python_file(file):
    '''
    Mutate a Mininet python file.
    '''
    if file != "":
        main_routine((file, FileType.PYTHON))


@click.command()
@click.option('-f', '--file', type=str, required=True, help="MrTopo config file.")
def config_file(file):
    '''
    Generate mutations from a configuration file.
    '''
    if file != "":
        click.echo("This option has not been implemented yet!")


@click.group()
def validator():
    pass


@click.command()
@click.option('-f', '--file', type=str, help="Validate a Mininet topology python file.")
def validate_file(file):
    '''
    Validate a Mininet topology python file.
    '''
    if file != "":
        validate_routine((file, FileType.PYTHON))


@click.command()
@click.option('-d', '--dir', type=str, help="Validate a directory of Mininet topologies.")
def validate_dir(dir):
    '''
    Validate a directory of Mininet topologies.
    '''
    if dir != "":
        validate_routine((dir, FileType.DIRECTORY))


# build mutator
mutator.add_command(python_file)
mutator.add_command(config_file)

# build validator
validator.add_command(validate_file)
validator.add_command(validate_dir)

# build cli
cli = click.CommandCollection(sources=[mutator, validator])

# DEBUG

if __name__ == '__main__':
    cli()
