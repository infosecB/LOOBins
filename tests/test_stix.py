from test_data import LOOBinFactory


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
