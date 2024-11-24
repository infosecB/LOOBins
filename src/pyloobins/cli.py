"""Model for CLI functions"""

import os
import sys

import click

from .util import get_loobins, make_template, normalize_file_name, validate_loobin
from .models import LOOBinsGroup


@click.group()
@click.version_option(prog_name="PyLOOBins")
def cli():
    """Create, validate, and view LOOBin objects."""


@cli.command()
@click.option(
    "--path",
    type=str,
    required=True,
    help="The path of the LOOBin YAML file to validate.",
)
def validate(path: str) -> None:
    """Validate a LOOBin YAML file."""
    if validate_loobin(yml_path=path):
        print(f"LOOBin at {path} is valid.")
        sys.exit(0)
    else:
        print(f"LOOBin at {path} is NOT valid.")
        sys.exit(1)


@cli.command()
@click.option("--name", type=str, required=False, help="Enter the name of the binary")
@click.option(
    "--path",
    type=str,
    required=False,
    help="Enter the path where you would like to create the template YAML file.",
)
def create(name: str, path: str) -> None:
    """Create a YAML template file for a new LOOBin."""
    template = make_template(name=name).to_yaml()
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


@cli.command()
@click.option("--name", type=str, required=True, help="Enter the name of the binary")
@click.option(
    "--path",
    type=str,
    required=False,
    help="Enter the path where you would like to create the template YAML file.",
)
def get(name: str, path: str = "") -> None:
    """Get a LOOBin object."""
    if path:
        loobins = get_loobins(path=path)
    else:
        loobins = get_loobins()

    res = [loobin for loobin in loobins if loobin.name == name]

    if len(res) == 0:
        print(f"No LOOBin found for {name}.")
    else:
        print(res[0].model_dump_json(indent=True, exclude_none=True))


@cli.command()
@click.option(
    "--path",
    type=str,
    required=False,
    help="Enter the path where you would like to create the template YAML file.",
    default=".",
)
@click.option(
    "--file-name",
    type=str,
    required=False,
    help="Enter the path where you would like to create the template YAML file.",
    default="loobins_stix.json",
)
def export_stix(file_name: str, path: str) -> None:
    """Export the LOOBins STIX bundle file."""
    all_loobins = get_loobins()
    stix_bundle = LOOBinsGroup(all_loobins)
    path = path if path and os.path.exists(path) else "./"
    if not os.path.exists(path):
        click.echo(
            f"The specified path did not exist. "
            f"Creating the {file_name}.yml file in the current directory."
        )
    with open(f"{path}/{file_name}", mode="w+", encoding="utf-8") as f:
        f.write(stix_bundle.to_stix_bundle().serialize(pretty=True))


if __name__ == "__main__":
    sys.exit(cli())
