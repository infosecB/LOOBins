"""Test the models in the pyloobins.models module."""
from datetime import date

from pyloobins.models import Detection, ExampleUseCase, LOOBin, LOOBinsGroup, Resource


def test_detection():
    """Test the AttackTactics model."""
    assert Detection(name="Test Name", url="https://test.url")


def test_resource():
    """Test the Resource model."""
    assert Resource(name="Test Name", url="https://test.url")


def test_example_use_case():
    """Test the ExampleUseCase model."""
    assert ExampleUseCase(
        name="Test Name",
        description="Test description.",
        code="Test code.",
        tactics=["Discovery"],
        tags=["test_tag"],
    )


def test_loobin():
    """Test the LOOBin model."""
    assert LOOBin(
        name="Template",
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


def test_loobin_group():
    """Test the LOOBin group model."""
    loobin = LOOBin(
        name="Template",
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
    assert LOOBinsGroup(__root__=[loobin])
