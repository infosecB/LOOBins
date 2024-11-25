"""Model that represents a LOOBin and its various components"""

from datetime import date, datetime, timezone, time
from typing import List, Literal, Optional

import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
from pydantic import BaseModel, Field, RootModel
from stix2 import Tool, Bundle

AttackTactics = Literal[
    "Reconnaissance",
    "Resource Development",
    "Initial Access",
    "Execution",
    "Persistence",
    "Privilege Escalation",
    "Defense Evasion",
    "Credential Access",
    "Discovery",
    "Lateral Movement",
    "Collection",
    "Exfiltration",
    "Command and Control",
    "Impact",
]


class Detection(BaseModel):
    """Detection base class"""

    name: str
    url: str


class Resource(BaseModel):
    """External reference base class"""

    name: str
    url: str


class ExampleUseCase(BaseModel):
    """Use case base class"""

    name: str
    description: str
    code: Optional[str] = None
    tactics: Optional[List[AttackTactics]] = None
    tags: Optional[List[str]] = None


class LOOBin(BaseModel):
    """LOOBin base class"""

    name: str = Field(title="Name", description="Name of the LOOBin")
    author: str = Field(title="Author", description="Author of the LOOBin")
    short_description: str = Field(
        title="Short Description",
        description="A short description of the LOOBin."
        "This will display in the LOOBin card list and the"
        "LOOBins website search results.",
    )
    full_description: str = Field(
        title="Full Description",
        description="A full description of the LOOBin."
        "This will display on the LOOBin's single page.",
    )
    created: date = Field(title="Created", description="Date the LOOBin was created")
    example_use_cases: List[ExampleUseCase] = Field(
        title="Example Use Cases",
        description="A list of example use cases for the LOOBin",
    )
    paths: List[str] = Field(title="Paths", description="A list of paths to the LOOBin")
    detections: List[Detection] = Field(
        title="Detections", description="A list of detections for the LOOBin"
    )
    resources: Optional[List[Resource]] = Field(
        title="Resource",
        description="A list of useful resources for the LOOBin",
        default=None,
    )
    acknowledgements: Optional[List[str]] = Field(
        title="Acknowledgements",
        description="Acknowledgements for the LOOBin",
        default=None,
    )

    def combine_tactics(self) -> List[str]:
        """Returns a list of all tactics across all LOOBin example use cases"""
        return list(
            dict.fromkeys(
                tactic
                for euc in self.example_use_cases
                if euc.tactics is not None
                for tactic in euc.tactics
            )
        )

    def combine_tags(self) -> List[str]:
        """Returns a list of all tags across all LOOBin example use cases"""
        return list(
            dict.fromkeys(
                tag
                for euc in self.example_use_cases
                if euc.tags is not None
                for tag in euc.tags
            )
        )

    def to_yaml(self, exclude_null: bool = True) -> str:
        """Convert a LOOBin object to a YAML string"""
        return yaml.dump(
            self.model_dump(exclude_none=exclude_null),
            Dumper=yaml.Dumper,
            sort_keys=False,
        )

    def to_md(self) -> str:
        """Convert a LOOBin object to a Markdown string"""
        env = Environment(
            loader=PackageLoader("pyloobins", "templates"),
            autoescape=select_autoescape(),
        )

        template = env.get_template("loobin.md.j2").render(
            loobin=self,
            tactics=self.combine_tactics(),
            tags=self.combine_tags(),
        )
        return template

    def to_stix(self) -> Tool:
        """Convert a LOOBin to a STIX2 Tool object
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
        return Tool(
            name=self.name,
            description=self.full_description,
            created=datetime.combine(self.created, time(0,0,0),timezone.utc)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z"),
            labels=['living-off-the-land','loobins'],
            external_references=[{"source_name":"LOOBins","description":"Living off the Orchard: macOS binaries.","url":f"https://www.loobins.io/binaries/{self.name}/"}]
        )

    def __str__(self) -> str:
        return self.to_yaml()

    def __repr__(self) -> str:
        return self.name


class LOOBinsGroup(RootModel):
    """LOOBin list base class"""

    root: List[LOOBin] = Field(title="LOOBins", description="A list of LOOBins")

    def to_stix_bundle(self) -> Bundle:
        return Bundle(objects=[loobin.to_stix() for loobin in self.root])
