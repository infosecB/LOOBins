"""Model for CLI functions"""
import sys
import click
import yaml
from .util import validate_loobin, make_template


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
    else:
        print(f"LOOBin at {file} is NOT valid.")


@cli.command()
def create_template():
    """Create a new LOOBin template file."""
    template = make_template()
    with open(file="template.yml", mode="w", encoding="utf-8") as f:
        f.write(yaml.dump(template.dict(), Dumper=yaml.Dumper))
        f.close()


if __name__ == "__main__":
    sys.exit(cli())
