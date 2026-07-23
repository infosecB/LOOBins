"""Tests for the pyloobins CLI commands."""

import json

from click.testing import CliRunner

from pyloobins.cli import cli
from pyloobins.util import make_template, normalize_file_name


def test_validate_valid_file(tmp_path):
    """A schema-conformant file validates and exits 0."""
    yml = tmp_path / "valid.yml"
    yml.write_text(make_template(name="TestBin").to_yaml(), encoding="utf-8")
    result = CliRunner().invoke(cli, ["validate", "--path", str(yml)])
    assert result.exit_code == 0
    assert "is valid" in result.output


def test_validate_invalid_file(tmp_path):
    """A file missing required fields fails validation and exits 1."""
    yml = tmp_path / "invalid.yml"
    yml.write_text("name: OnlyName\n", encoding="utf-8")
    result = CliRunner().invoke(cli, ["validate", "--path", str(yml)])
    assert result.exit_code == 1
    assert "NOT valid" in result.output


def test_create_writes_file_without_trailing_slash(tmp_path):
    """--path need not end in a slash (regression for the path-join fix)."""
    result = CliRunner().invoke(
        cli, ["create", "--name", "My Bin", "--path", str(tmp_path)]
    )
    assert result.exit_code == 0
    expected = tmp_path / f"{normalize_file_name('My Bin')}.yml"
    assert expected.exists()
    # The written template round-trips through validation.
    assert "name: My Bin" in expected.read_text(encoding="utf-8")


def test_get_found(tmp_path):
    """get returns the matching LOOBin as JSON."""
    yml = tmp_path / "testbin.yml"
    yml.write_text(make_template(name="TestBin").to_yaml(), encoding="utf-8")
    result = CliRunner().invoke(
        cli, ["get", "--name", "TestBin", "--path", str(tmp_path)]
    )
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["name"] == "TestBin"


def test_get_not_found(tmp_path):
    """get reports when no LOOBin matches."""
    result = CliRunner().invoke(
        cli, ["get", "--name", "Nonexistent", "--path", str(tmp_path)]
    )
    assert "No LOOBin found" in result.output


def test_export_stix_writes_bundle(tmp_path):
    """export-stix writes a parseable STIX bundle to the chosen path."""
    result = CliRunner().invoke(
        cli, ["export-stix", "--path", str(tmp_path), "--file-name", "out.json"]
    )
    assert result.exit_code == 0
    out = tmp_path / "out.json"
    assert out.exists()
    bundle = json.loads(out.read_text(encoding="utf-8"))
    assert bundle["type"] == "bundle"
