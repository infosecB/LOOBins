'''Model for CLI functions'''
import sys
import click
from .util import validate_loobin

@click.group()
def cli():
    '''Create, manage, and validate LOOBin objects.'''

@cli.command()
@click.option('--file', type=str, required=True, help='File location of the LOOBin YAML file to validate.')
def validate(file: str)->None:
    '''Validate a LOOBin object.'''
    if validate_loobin(yml_path=file):
        print(f"LOOBin at {file} is valid.")
    else:
        print(f"LOOBin at {file} is NOT valid.")

@cli.command()
def create():
    '''Create a new LOOBin object.'''
    click.echo('You ran the create command.')

if __name__=="__main__":
    sys.exit(cli())
