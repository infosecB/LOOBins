"""Model that represents a LOOBin and its various components"""
from datetime import date
from typing import List, Literal, Optional

import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
from pydantic import BaseModel, Field

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
        "This will display in the LOOBin card list and the LOOBins website search results.",
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
    )
    acknowledgements: Optional[List[str]] = Field(
        title="Acknowledgements", description="Acknowledgements for the LOOBin"
    )

    def combine_tactics(self) -> List[str]:
        """Returns a list of all tactics across all LOOBin example use cases"""
        return [t for euc in self.example_use_cases for t in euc.tactics]  # type: ignore

    def combine_tags(self) -> List[str]:
        """Returns a list of all tags across all LOOBin example use cases"""
        return [t for euc in self.example_use_cases for t in euc.tags]  # type: ignore

    def to_yaml(self, exclude_null: bool = True) -> str:
        """Convert a LOOBin object to a YAML string"""
        return yaml.dump(
            self.dict(exclude_none=exclude_null),
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

    def __str__(self) -> str:
        return self.to_yaml()

    def __repr__(self) -> str:
        return self.to_yaml()
