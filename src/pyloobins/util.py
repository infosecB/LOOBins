"""Utility functions that support the CLI and library"""
import pathlib
from datetime import date

import yaml

import pyloobins

from .models import Detection, Entitlement, ExampleUseCase, LOOBin, Resource


def get_loobins(path: str = "") -> list:
    """Returns a list of LOOBin objects"""
    loobins = []
    if path:
        yml_files = pathlib.Path(path).glob("**/*.yml")
    else:
        yml_files = (pathlib.Path(pyloobins.__file__).parents[1] / "LOOBins").glob(
            "**/*.yml"
        )
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


def get_entitlements(path: str = "") -> list:
    """Returns a list of Entitlement objects"""
    entitlements = []
    if path:
        yml_files = pathlib.Path(path).glob("**/*.yml")
    else:
        yml_files = (
            pathlib.Path(pyloobins.__file__).parents[1] / "LOOEntitlements"
        ).glob("**/*.yml")
    for yml_file in yml_files:
        with open(yml_file, "r", encoding="utf-8") as stream:
            try:
                yml_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        try:
            entitlements.append(Entitlement(**yml_content))  # type: ignore
        except Exception as exc:
            # TODO add more specific Exception handling
            print(exc)
    return entitlements


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


def validate_entitlement(yml_path: str) -> bool:
    """Validates Entitlement YAML file"""
    with open(yml_path, "r", encoding="utf-8") as stream:
        try:
            yml_content = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    try:
        Entitlement(**yml_content)  # type: ignore
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


def make_entitlement_template(name: str = "") -> Entitlement:
    """Creates a template LOOBin object"""
    entitlement_template = Entitlement(
        name=name if name else "Entitlement Template",
        short_description="A short description for the entitlement",
        full_description="A long description of how the entitlement can be abused by attackers.",
        tactics=["Execution"],
        tags=["Test"],
        resources=[Resource(name="Name of resource", url="https://google.com")],
    )
    return entitlement_template


def normalize_file_name(title: str) -> str:
    """Accepts an object title and normalizes it for the file name"""
    return title.lower().replace(" ", "_")
