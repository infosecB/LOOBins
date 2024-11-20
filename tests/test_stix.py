from pyloobins.models import LOOBinsFactory
from pyloobins.stix import convert_to_stix_tool


def test_convert_to_stix_tool():
    loobins = LOOBinsFactory.batch(size=5)

    tools = convert_to_stix_tool(loobins)

    assert len(tools) == len(loobins), "Mismatch in number of tools converted"

    for i, tool in enumerate(tools):
        assert tool.type == "tool", "Type field should always be 'tool'"
        assert tool.name == loobins[i].name, f"Tool name mismatch for index {i}"
        assert (
            tool.description == loobins[i].full_description
        ), f"Description mismatch for index {i}"
