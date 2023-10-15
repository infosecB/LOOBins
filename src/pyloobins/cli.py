"""Model for CLI functions"""
import os
import sys

import click

from .util import (
    get_entitlements,
    get_loobins,
    make_entitlement_template,
    make_template,
    normalize_file_name,
    validate_entitlement,
    validate_loobin,
)


@click.group()
def cli():
    """Create, validate, and view LOOBin objects."""


@cli.command()
@click.option(
    "--path",
    type=str,
    required=True,
    help="The path of the LOOBin YAML file to validate.",
)
@click.option(
    "--object-type",
    type=click.Choice(["LOOBin", "Entitlement"], case_sensitive=False),
)
def validate(path: str, object_type: str) -> None:
    """Validate a an object's YAML file."""
    object_type = object_type.lower()
    match object_type:
        case "loobin":
            if validate_loobin(yml_path=path):
                print(f"LOOBin at {path} is valid.")
                sys.exit(0)
            else:
                print(f"LOOBin at {path} is NOT valid.")
                sys.exit(1)
        case "entitlement":
            if validate_entitlement(yml_path=path):
                print(f"Entitlement at {path} is valid.")
                sys.exit(0)
            else:
                print(f"Entitlement at {path} is NOT valid.")
                sys.exit(1)


@cli.command()
@click.option("--name", type=str, required=False, help="Enter the name of the binary")
@click.option(
    "--path",
    type=str,
    required=False,
    help="Enter the path where you would like to create the template YAML file.",
)
@click.option(
    "--object-type", type=click.Choice(["LOOBin", "Entitlement"], case_sensitive=False)
)
def create(name: str, path: str, object_type: str) -> None:
    """Create a YAML template file for a new object."""
    object_type = object_type.lower()
    match object_type:
        case "loobin":
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
        case "entitlement":
            template = make_entitlement_template(name=name).to_yaml()
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
@click.option(
    "--object-type", type=click.Choice(["LOOBin", "Entitlement"], case_sensitive=False)
)
def get(name: str, object_type: str, path: str = "") -> None:
    """Get an object."""
    object_type = object_type.lower()
    match object_type:
        case "loobin":
            if path:
                loobins = get_loobins(path=path)
            else:
                loobins = get_loobins()

            res = [loobin for loobin in loobins if loobin.name == name]

            if len(res) == 0:
                print(f"No LOOBin found for {name}.")
            else:
                print(res[0].json(indent=True, exclude_none=True))
        case "entitlement":
            if path:
                entitlements = get_entitlements(path=path)
            else:
                entitlements = get_entitlements()

            res = [
                entitlement for entitlement in entitlements if entitlement.name == name
            ]

            if len(res) == 0:
                print(f"No Entitlement found for {name}.")
            else:
                print(res[0].json(indent=True, exclude_none=True))


if __name__ == "__main__":
    sys.exit(cli())
