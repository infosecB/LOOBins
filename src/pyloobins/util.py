"""Utility functions that support the CLI and library"""

import pathlib
from datetime import date

import yaml

import pyloobins
from pyloobins.models import Detection, ExampleUseCase, LOOBin, Resource


def get_loobins(path: str = "") -> list[LOOBin]:
    """Returns a list of LOOBin objects"""
    loobins = []
    yml_files_count = 0
    parent_folder = 0
    if path:
        yml_files = pathlib.Path(path).glob("**/*.yml")
    else:
        while yml_files_count == 0 and parent_folder < 5:
            yml_files = [
                yaml_file
                for yaml_file in (
                    pathlib.Path(pyloobins.__file__).parents[parent_folder] / "LOOBins"
                ).glob("**/*.yml")
            ]
            yml_files_count = len(yml_files)
            parent_folder += 1

    for yml_file in yml_files:
        with open(yml_file, "r", encoding="utf-8") as stream:
            try:
                yml_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        try:
            loobins.append(LOOBin(**yml_content))  # type: ignore
        except Exception as exc:
            # TODO add more specific Exception handling
            print(exc)
    return loobins


def validate_loobin(yml_path: str) -> bool:
    """Validates LOOBin YAML file"""
    with open(yml_path, "r", encoding="utf-8") as stream:
        try:
            yml_content = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    try:
        LOOBin(**yml_content)  # type: ignore
        return True
    except Exception as exc:
        # TODO add more specific Exception handling
        print(exc)
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
