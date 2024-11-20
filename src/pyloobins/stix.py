from stix2 import Tool, Bundle
from datetime import datetime, timezone
from pyloobins.models import LOOBin
from pyloobins.util import get_loobins


def convert_to_stix_tool(loobins: list[LOOBin]) -> list[Tool]:
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
    return stix_tools


def generate_loobin_tool_stix_bundle(stix_tools: list[Tool]) -> Bundle:
    return Bundle(objects=stix_tools)


if __name__ == "__main__":
    loobins = get_loobins("./")
    tools = convert_to_stix_tool(loobins)
    print(tools)
    bundle = generate_loobin_tool_stix_bundle(tools)
    print(bundle)
