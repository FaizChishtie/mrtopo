import click
from mrtopo.__main__ import main_routine
from mrtopo.util.filetype import FileType

@click.command()
@click.option('-p', '--pythonfile', default="", help="Python file that MrTopo should mutate.")
@click.option('-c', '--configfile', default="", help="MrTopo config file.")
def main(pythonfile, configfile):
    if pythonfile != "":
        main_routine((pythonfile, FileType.PYTHON))
    elif configfile != "":
        click.echo("This option has not been implemented yet!")
        pass