"""Keep use-case tags consistent with the taxonomy in docs/tags.md.

The conventions in docs/tags.md are only useful if the corpus follows them,
so these tests enforce the mechanical ones: every tag is documented, uses
lowercase-hyphen form, isn't a MITRE tactic name, and doesn't just repeat the
LOOBin's own name.
"""

import re
from pathlib import Path
from typing import get_args

import pytest

from pyloobins.models import AttackTactics
from pyloobins.util import get_loobins

REPO_ROOT = Path(__file__).resolve().parents[1]
TAGS_DOC = REPO_ROOT / "docs" / "tags.md"
LOOBINS = get_loobins(str(REPO_ROOT / "LOOBins"))

TAG_ROW = re.compile(r"^\| `([^`]+)` \|", re.MULTILINE)
TAG_FORMAT = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TACTIC_TAGS = {t.lower().replace(" ", "-") for t in get_args(AttackTactics)}

DOCUMENTED_TAGS = set(TAG_ROW.findall(TAGS_DOC.read_text(encoding="utf-8")))


def _tagged_use_cases():
    for loobin in LOOBINS:
        for euc in loobin.example_use_cases:
            for tag in euc.tags or []:
                yield loobin, euc, tag


def test_tags_doc_is_parsed():
    """Guard against the regex silently matching nothing."""
    assert len(DOCUMENTED_TAGS) > 50


def test_corpus_is_loaded():
    assert LOOBINS


@pytest.mark.parametrize("tag", sorted(DOCUMENTED_TAGS))
def test_documented_tag_format(tag):
    assert TAG_FORMAT.match(tag), f"`{tag}` is not lowercase-hyphenated"
    assert tag not in TACTIC_TAGS, f"`{tag}` is a MITRE tactic; use `tactics`"


@pytest.mark.parametrize("loobin", LOOBINS, ids=lambda lb: lb.name)
def test_loobin_tags_follow_taxonomy(loobin):
    problems = []
    for euc in loobin.example_use_cases:
        tags = euc.tags or []
        for tag in tags:
            where = f"{euc.name!r}: `{tag}`"
            if tag not in DOCUMENTED_TAGS:
                problems.append(f"{where} is not documented in docs/tags.md")
            if not TAG_FORMAT.match(tag):
                problems.append(f"{where} is not lowercase-hyphenated")
            if tag in TACTIC_TAGS:
                problems.append(f"{where} is a MITRE tactic; use `tactics`")
            if tag == loobin.name.lower():
                problems.append(f"{where} repeats the LOOBin's own name")
        if len(tags) != len(set(tags)):
            problems.append(f"{euc.name!r} has duplicate tags")
    assert not problems, "\n".join(problems)
