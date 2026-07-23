"""Validate every committed LOOBin YAML file against the schema.

This guards the whole corpus (not just files changed in a PR) so a
schema/model change that breaks a pre-existing entry fails fast.
"""

from pathlib import Path

import pytest

from pyloobins.util import validate_loobin

LOOBINS_DIR = Path(__file__).resolve().parents[1] / "LOOBins"
LOOBIN_FILES = sorted(LOOBINS_DIR.glob("*.yml"))


def test_loobins_dir_is_populated():
    """Guard against the glob silently matching nothing."""
    assert LOOBIN_FILES, f"No LOOBin YAML files found in {LOOBINS_DIR}"


@pytest.mark.parametrize("yml_file", LOOBIN_FILES, ids=lambda p: p.name)
def test_loobin_file_validates(yml_file):
    """Each committed LOOBin YAML file must satisfy the schema."""
    assert validate_loobin(
        yml_path=str(yml_file)
    ), f"{yml_file.name} failed schema validation"
