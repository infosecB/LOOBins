"""Model that represents a LOOBin and its various components"""
from typing import List, Optional, Union, Literal
from datetime import date
from pydantic import BaseModel, Field
import yaml


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
    url: Union[List[str], str]


class ExternalReference(BaseModel):
    """External reference base class"""

    name: str
    url: str


class ExampleUseCase(BaseModel):
    """Use case base class"""

    name: str
    description: str
    code: str
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
    created: date = Field(
        title="Created", description="Date the LOOBin was created"
    )
    example_use_cases: List[ExampleUseCase] = Field(
        title="Example Use Cases",
        description="A list of example use cases for the LOOBin",
    )
    paths: List[str] = Field(
        title="Paths", description="A list of paths to the LOOBin"
    )
    detections: List[Detection] = Field(
        title="Detections", description="A list of detections for the LOOBin"
    )
    external_references: Optional[List[ExternalReference]] = Field(
        title="External References",
        description="A list of useful external references for the LOOBin",
    )

    def yaml(self, exclude_null: bool = True) -> str:
        """Convert a LOOBin object to a YAML string"""
        return yaml.dump(
            self.dict(exclude_none=exclude_null),
            Dumper=yaml.Dumper,
            sort_keys=False,
        )
