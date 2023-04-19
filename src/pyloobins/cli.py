"""Model for CLI functions"""
import os
import sys

import click

from .util import make_template, normalize_file_name, validate_loobin


@click.group()
def cli():
    """Create, manage, and validate LOOBin objects."""


@cli.command()
@click.option(
    "--file",
    type=str,
    required=True,
    help="File location of the LOOBin YAML file to validate.",
)
def validate(file: str) -> None:
    """Validate a LOOBin object."""
    if validate_loobin(yml_path=file):
        print(f"LOOBin at {file} is valid.")
        sys.exit(0)
    else:
        print(f"LOOBin at {file} is NOT valid.")
        sys.exit(1)


@cli.command()
@click.option("--name", type=str, required=False, help="Enter the name of the binary")
@click.option(
    "--path",
    type=str,
    required=False,
    help="Enter the path where you would like to create the template YAML file.",
)
def create_template(name: str, path: str) -> None:
    """Create a new LOOBin template file."""
    template = make_template().to_yaml()
    file_name = normalize_file_name(name) if name else "template"
    file_path = path if path and os.path.exists(path) else "./"
    if not os.path.exists(file_path):
        click.echo(
            f"The specified path did not exist. "
            f"Creating the {file_name}.yml file in the current directory."
        )
    with open(
        file=f"{file_path}{file_name}.yml", mode="w", encoding="utf-8"
    ) as out_file:
        out_file.write(template)
        out_file.close()


if __name__ == "__main__":
    sys.exit(cli())
