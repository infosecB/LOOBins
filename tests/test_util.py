"""Tests for the pyloobins.util module."""
import os
from pathlib import Path

from pyloobins.util import get_loobins, make_template, validate_loobin


def test_get_loobins():
    """Test the get_loobins function."""
    assert get_loobins("../LOOBins")


def test_make_template():
    """Test the make_template function."""
    assert make_template()


def test_validate_loobin():
    """Test the validate_loobin function."""
    test_file = Path("./tests/test.yml")
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(make_template().to_yaml())
    assert validate_loobin(yml_path=str(test_file))
    os.remove(test_file)
