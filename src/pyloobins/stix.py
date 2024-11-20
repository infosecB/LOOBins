from stix2 import Tool, Bundle
from datetime import datetime, timezone
from pyloobins.models import LOOBin
from pyloobins.util import get_loobins


def loobin_to_stix_tool(loobins: list[LOOBin]):
    """Takes in a LOOBin and Converts to STIX2 Tool
    https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_z4voa9ndw8v

    Required fields per STIX2 spec:
        - type: must be 'tool'
        - name: str

    Optional fields:
        - description (str)
        - tool_types (list of open-vocab -> tool-type-ov)
        - aliases (list of str)
        - kill_chain_phases (list of kill-chain-phase)
    """
    stix_tools = []

    for loobin in loobins:
        tool = Tool(
            name=loobin.name,
            description=loobin.full_description,
            created=datetime.now(timezone.utc)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z"),
        )
        stix_tools.append(tool)

    # Create a STIX bundle containing all tools
    stix_bundle = Bundle(objects=stix_tools)
    return stix_bundle


def test_stix_tool():
    from pyloobins.models import LOOBinsFactory

    test_loo = LOOBinsFactory.build()
    test_tools = loobin_to_stix_tool([test_loo])
    print(test_tools)


if __name__ == "__main__":
    """Retrieve all current LOOBin YML"""
    loobins = get_loobins("./")
    stix_bundle = loobin_to_stix_tool(loobins)
    print(stix_bundle)
