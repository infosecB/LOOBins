"""Test the ATT&CK Navigator layer export."""

import re
from datetime import date

from pyloobins.models import Detection, ExampleUseCase, LOOBin, LOOBinsGroup
from pyloobins.util import get_loobins
from tests.test_corpus import LOOBINS_DIR

TECHNIQUE_ID = re.compile(r"^T\d{4}(\.\d{3})?$")


def _loobin(name, techniques):
    return LOOBin(
        name=name,
        author="tester",
        short_description="short",
        full_description="full",
        created=date(2024, 1, 1),
        example_use_cases=[
            ExampleUseCase(name="uc", description="d", techniques=techniques)
        ],
        paths=["/usr/bin/x"],
        detections=[Detection(name="none", url="N/A")],
    )


def _layer():
    return LOOBinsGroup(
        [
            _loobin("osascript", ["T1059.002", "T1115"]),
            _loobin("Script Editor", ["T1059.002"]),
            _loobin("ditto", ["T1560.001", "T1560"]),
        ]
    ).to_navigator_layer()


def _by_id(layer):
    return {t["techniqueID"]: t for t in layer["techniques"]}


def test_layer_metadata():
    layer = _layer()
    assert layer["domain"] == "enterprise-attack"
    assert layer["versions"]["layer"] == "4.5"
    assert layer["filters"]["platforms"] == ["macOS"]


def test_layer_scores_and_comments_count_binaries():
    techniques = _by_id(_layer())
    assert techniques["T1059.002"]["score"] == 2
    assert techniques["T1059.002"]["comment"] == "osascript, Script Editor"
    assert techniques["T1115"]["score"] == 1
    assert [link["url"] for link in techniques["T1059.002"]["links"]] == [
        "https://loobins.io/binaries/osascript/",
        "https://loobins.io/binaries/script_editor/",
    ]
    assert _layer()["gradient"]["maxValue"] == 2


def test_layer_expands_parents_of_subtechniques():
    techniques = _by_id(_layer())
    # Parent not mapped itself: added unscored, only to show its sub-techniques.
    assert techniques["T1059"] == {"techniqueID": "T1059", "showSubtechniques": True}
    # Parent mapped itself: keeps its score and is expanded.
    assert techniques["T1560"]["score"] == 1
    assert techniques["T1560"]["showSubtechniques"] is True
    assert "showSubtechniques" not in techniques["T1115"]


def test_corpus_layer_is_well_formed():
    loobins = get_loobins(str(LOOBINS_DIR))
    layer = LOOBinsGroup(loobins).to_navigator_layer()
    ids = [t["techniqueID"] for t in layer["techniques"]]
    assert ids and len(ids) == len(set(ids))
    assert all(TECHNIQUE_ID.match(t) for t in ids)
    covered = {t for lb in loobins for t in lb.combine_techniques()}
    assert covered <= set(ids)


def test_gradient_max_exceeds_min_even_when_every_score_is_one():
    layer = LOOBinsGroup([_loobin("osascript", ["T1115"])]).to_navigator_layer()
    assert layer["gradient"]["maxValue"] > layer["gradient"]["minValue"]


def test_empty_group_layer():
    layer = LOOBinsGroup([]).to_navigator_layer()
    assert layer["techniques"] == []
    assert layer["gradient"]["maxValue"] > layer["gradient"]["minValue"]
