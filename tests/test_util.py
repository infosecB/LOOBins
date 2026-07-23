"""Tests for the pyloobins.util module."""

from pyloobins.util import (
    get_loobins,
    make_template,
    normalize_file_name,
    validate_loobin,
)


def test_get_loobins():
    """Test the get_loobins function."""
    assert len(get_loobins(path="./LOOBins")) > 0


def test_make_template():
    """Test the make_template function."""
    assert make_template()


def test_validate_loobin(tmp_path):
    """Test the validate_loobin function."""
    test_file = tmp_path / "test.yml"
    test_file.write_text(make_template().to_yaml(), encoding="utf-8")
    assert validate_loobin(yml_path=str(test_file))


def test_normalize_file_name():
    """Names are lowercased and spaces become underscores."""
    assert normalize_file_name("My Bin") == "my_bin"
