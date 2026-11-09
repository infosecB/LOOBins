from datetime import date

from pyloobins.models import Detection, ExampleUseCase, LOOBin
from tests.test_data import LOOBinFactory


def test_to_stix():
    loobins = LOOBinFactory.batch(5)
    tools = [loobin.to_stix() for loobin in loobins]

    assert len(tools) == len(loobins), "Mismatch in number of tools converted"

    for i, tool in enumerate(tools):
        assert tool.type == "tool", "Type field should always be 'tool'"
        assert tool.name == loobins[i].name, f"Tool name mismatch for index {i}"
        assert (
            tool.description == loobins[i].full_description
        ), f"Description mismatch for index {i}"


def _loobin(**overrides):
    fields = {
        "name": "Script Editor",
        "author": "tester",
        "short_description": "short",
        "full_description": "full",
        "created": date(2024, 1, 1),
        "example_use_cases": [
            ExampleUseCase(
                name="uc1",
                description="d",
                tactics=["Execution", "Stealth"],
                techniques=["T1059.002", "T1204.001"],
            ),
            ExampleUseCase(
                name="uc2",
                description="d",
                tactics=["Execution"],
                techniques=["T1059.002"],
            ),
        ],
        "paths": ["/usr/bin/x"],
        "detections": [Detection(name="none", url="N/A")],
    }
    fields.update(overrides)
    return LOOBin(**fields)


def test_to_stix_kill_chain_phases_follow_tactics():
    tool = _loobin().to_stix()
    assert [(p.kill_chain_name, p.phase_name) for p in tool.kill_chain_phases] == [
        ("mitre-attack", "execution"),
        ("mitre-attack", "stealth"),
    ]


def test_to_stix_references_techniques_and_page():
    refs = _loobin().to_stix().external_references
    assert refs[0].source_name == "LOOBins"
    assert refs[0].url == "https://loobins.io/binaries/script_editor/"
    attack = [(r.external_id, r.url) for r in refs if r.source_name == "mitre-attack"]
    assert attack == [
        ("T1059.002", "https://attack.mitre.org/techniques/T1059/002/"),
        ("T1204.001", "https://attack.mitre.org/techniques/T1204/001/"),
    ]


def test_to_stix_without_tactics_or_techniques():
    tool = _loobin(
        example_use_cases=[ExampleUseCase(name="uc", description="d")]
    ).to_stix()
    assert "kill_chain_phases" not in tool
    assert [r.source_name for r in tool.external_references] == ["LOOBins"]
