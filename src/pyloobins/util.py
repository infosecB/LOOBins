"""Utility functions that support the CLI and library"""

from __future__ import annotations

import pathlib
from datetime import date

import yaml

import pyloobins
from pyloobins.models import Detection, ExampleUseCase, LOOBin, Resource


def _discover_loobin_files() -> list[pathlib.Path]:
    """Locate the LOOBin YAML corpus for the default (no-path) case.

    Prefers a copy bundled inside the installed package (see the wheel
    ``force-include`` in ``pyproject.toml``), then falls back to walking up
    from the package directory to find a sibling ``LOOBins/`` folder, which
    covers editable installs and running from a source checkout.
    """
    package_dir = pathlib.Path(pyloobins.__file__).parent
    bundled = list((package_dir / "LOOBins").glob("**/*.yml"))
    if bundled:
        return bundled
    for parent in package_dir.parents[:5]:
        candidate = list((parent / "LOOBins").glob("**/*.yml"))
        if candidate:
            return candidate
    return []


def get_loobins(path: str = "") -> list[LOOBin]:
    """Returns a list of LOOBin objects"""
    loobins = []
    if path:
        yml_files = list(pathlib.Path(path).glob("**/*.yml"))
    else:
        yml_files = _discover_loobin_files()

    for yml_file in yml_files:
        with open(yml_file, "r", encoding="utf-8") as stream:
            try:
                yml_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(f"Error parsing {yml_file}: {exc}")
                continue
        try:
            loobins.append(LOOBin(**yml_content))
        except Exception as exc:
            print(f"Error loading {yml_file}: {exc}")
    return loobins


def validate_loobin(yml_path: str) -> bool:
    """Validates LOOBin YAML file"""
    with open(yml_path, "r", encoding="utf-8") as stream:
        try:
            yml_content = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(f"Error parsing {yml_path}: {exc}")
            return False
    try:
        LOOBin(**yml_content)
        return True
    except Exception as exc:
        print(f"Validation error in {yml_path}: {exc}")
        return False


def make_template(name: str = "") -> LOOBin:
    """Creates a template LOOBin object"""
    loobin_template = LOOBin(
        name=name if name else "Template",
        short_description="A short description of the binary goes here.",
        full_description="A full length description of the binary goes here.",
        author="Enter your name or alias here.",
        created=date.today(),
        example_use_cases=[
            ExampleUseCase(
                name="An Example Use Case",
                description="A description of the use case goes here.",
                code="A code snippet goes here.",
                tactics=["Discovery"],
                tags=["example_tag", "another_tag"],
            )
        ],
        paths=["/enter/binary/path/here"],
        detections=[
            Detection(
                name="A detection source (e.g. Sigma)",
                url="https://urltodetection.here",
            )
        ],
        resources=[
            Resource(
                name="Name of resources.",
                url="https://urlofexternalreference.here",
            )
        ],
        acknowledgements=["Enter any acknowledgements here."],
    )
    return loobin_template


def normalize_file_name(title: str) -> str:
    """Accepts a binary title and normalizes it for the file name"""
    return title.lower().replace(" ", "_")
