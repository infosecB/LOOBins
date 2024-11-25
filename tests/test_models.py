"""Test the models in the pyloobins.models module."""

from pyloobins.models import Detection, ExampleUseCase, LOOBin, LOOBinsGroup, Resource
from tests.test_data import DetectionFactory, ResourceFactory, LOOBinFactory, ExampleUseCaseFactory


def test_detection():
    """Test the AttackTactics model."""
    assert type(DetectionFactory.build()) == Detection


def test_resource():
    """Test the Resource model."""
    assert type(ResourceFactory.build()) == Resource


def test_example_use_case():
    """Test the ExampleUseCase model."""
    assert type(ExampleUseCaseFactory.build()) == ExampleUseCase


def test_loobin():
    """Test the LOOBin model."""
    assert type(LOOBinFactory.build()) == LOOBin


def test_loobin_group():
    """Test the LOOBin group model."""
    assert LOOBinsGroup(LOOBinFactory.batch(2))
