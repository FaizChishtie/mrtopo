import click
from mrtopo.__main__ import main_routine, validate_routine
from mrtopo.util.filetype import FileType

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group()
def cli():
    '''
        MrTopo is a python application that generates mutant Mininet topology files for network testing purposes.
    '''
    pass


@click.group()
def generator():
    pass


@click.command()
@click.option('-p', '--python-file', type=str, help="Python file that MrTopo should mutate.")
@click.option('-c', '--config-file', type=str, help="MrTopo config file.")
def params(python_file, config_file):
    if python_file != "":
        main_routine((python_file, FileType.PYTHON))
    elif config_file != "":
        click.echo("This option has not been implemented yet!")


@click.group()
def validator():
    pass


@click.command()
@click.option('-vf', '--validate-file', type=str, help="Validate a Mininet topology python file.")
def validate_file(validate_file):
    if validate_file != "":
        validate_routine((validate_file, FileType.PYTHON))


@click.command()
@click.option('-vd', '--validate-dir', type=str, help="Validate a directory of Mininet topologies.")
def validate_dir(validate_dir):
    if validate_dir != "":
        validate_routine((validate_dir, FileType.DIRECTORY))


# build generator
generator.add_command(params)

# build validator
validator.add_command(validate_file)
validator.add_command(validate_dir)

# build cli
cli = click.CommandCollection(sources=[generator, validator])

# DEBUG

if __name__ == '__main__':
    cli()
