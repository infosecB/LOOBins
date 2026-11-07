"""Model that represents a LOOBin and its various components"""

from datetime import date, datetime, time, timezone
from typing import Annotated, Any, Dict, List, Literal, Optional

import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
from pydantic import BaseModel, Field, RootModel, StringConstraints
from stix2 import Bundle, Tool

# ATT&CK Enterprise v20 tactics. v20 replaced Defense Evasion (TA0005) with
# Stealth and added Defense Impairment (TA0112).
AttackTactics = Literal[
    "Reconnaissance",
    "Resource Development",
    "Initial Access",
    "Execution",
    "Persistence",
    "Privilege Escalation",
    "Stealth",
    "Defense Impairment",
    "Credential Access",
    "Discovery",
    "Lateral Movement",
    "Collection",
    "Exfiltration",
    "Command and Control",
    "Impact",
]

LOOBINS_SITE = "https://loobins.io"
# ATT&CK Enterprise major version the tactic list and technique IDs follow.
ATTACK_VERSION = "20"


def attack_technique_url(technique_id: str) -> str:
    """URL of an ATT&CK technique page, e.g. T1059.002 -> .../T1059/002/"""
    return f"https://attack.mitre.org/techniques/{technique_id.replace('.', '/')}/"


def attack_tactic_shortname(tactic: str) -> str:
    """ATT&CK tactic short name used in kill chains and layers, e.g. command-and-control"""
    return tactic.lower().replace(" ", "-")


# A MITRE ATT&CK Enterprise technique or sub-technique ID, e.g. T1059 or T1059.002
AttackTechnique = Annotated[str, StringConstraints(pattern=r"^T\d{4}(\.\d{3})?$")]


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
    techniques: Optional[List[AttackTechnique]] = Field(
        default=None,
        description="MITRE ATT&CK technique or sub-technique IDs (e.g. T1059.002)",
    )
    tags: Optional[List[str]] = None


class LOOBin(BaseModel):
    """LOOBin base class"""

    name: str = Field(title="Name", description="Name of the LOOBin")
    author: str = Field(title="Author", description="Author of the LOOBin")
    short_description: str = Field(
        title="Short Description",
        description="A short description of the LOOBin. "
        "This will display in the LOOBin card list and the "
        "LOOBins website search results.",
    )
    full_description: str = Field(
        title="Full Description",
        description="A full description of the LOOBin. "
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

    def combine_techniques(self) -> List[str]:
        """Returns a list of all ATT&CK technique IDs across all LOOBin example use cases"""
        return list(
            dict.fromkeys(
                technique
                for euc in self.example_use_cases
                if euc.techniques is not None
                for technique in euc.techniques
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

    @property
    def slug(self) -> str:
        """URL slug of the LOOBin's page on loobins.io (its normalized file name)"""
        return self.name.lower().replace(" ", "_")

    @property
    def url(self) -> str:
        """URL of the LOOBin's page on loobins.io"""
        return f"{LOOBINS_SITE}/binaries/{self.slug}/"

    def to_stix(self) -> Tool:
        """Convert a LOOBin to a STIX2 Tool object
        https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_z4voa9ndw8v

        The tool's kill_chain_phases are its ATT&CK tactics (kill chain
        "mitre-attack"), and each ATT&CK technique its use cases map to is an
        external reference with source_name "mitre-attack", the convention
        MITRE's own STIX data uses.
        """
        external_references: List[Dict[str, str]] = [
            {
                "source_name": "LOOBins",
                "description": "Living off the Orchard: macOS binaries.",
                "url": self.url,
            }
        ]
        external_references.extend(
            {
                "source_name": "mitre-attack",
                "external_id": technique,
                "url": attack_technique_url(technique),
            }
            for technique in self.combine_techniques()
        )
        kill_chain_phases = [
            {
                "kill_chain_name": "mitre-attack",
                "phase_name": attack_tactic_shortname(tactic),
            }
            for tactic in self.combine_tactics()
        ]
        return Tool(
            name=self.name,
            description=self.full_description,
            created=datetime.combine(self.created, time(0, 0, 0), timezone.utc)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z"),
            labels=["living-off-the-land", "loobins"],
            external_references=external_references,
            kill_chain_phases=kill_chain_phases or None,
        )

    def __str__(self) -> str:
        return self.to_yaml()

    def __repr__(self) -> str:
        return self.name


class LOOBinsGroup(RootModel):
    """LOOBin list base class"""

    root: List[LOOBin] = Field(title="LOOBins", description="A list of LOOBins")

    def to_stix_bundle(self) -> Bundle:
        """Bundle every LOOBin as a STIX2 Tool"""
        return Bundle(objects=[loobin.to_stix() for loobin in self.root])

    def to_navigator_layer(self) -> Dict[str, Any]:
        """Build an ATT&CK Navigator layer (format 4.5) of the techniques LOOBins cover.

        Each technique is scored by how many LOOBins map to it, and its comment
        and links name those LOOBins. Parents of covered sub-techniques are
        expanded so the sub-techniques show in the matrix.
        """
        binaries: Dict[str, List[LOOBin]] = {}
        for loobin in sorted(self.root, key=lambda lb: lb.name.lower()):
            for technique in loobin.combine_techniques():
                binaries.setdefault(technique, []).append(loobin)

        techniques: List[Dict[str, Any]] = []
        for technique_id in sorted(binaries):
            users = binaries[technique_id]
            techniques.append(
                {
                    "techniqueID": technique_id,
                    "score": len(users),
                    "comment": ", ".join(lb.name for lb in users),
                    "enabled": True,
                    "links": [{"label": lb.name, "url": lb.url} for lb in users],
                }
            )
        # showSubtechniques is only valid on techniques that have sub-techniques.
        parents = {t.split(".")[0] for t in binaries if "." in t}
        for entry in techniques:
            if entry["techniqueID"] in parents:
                entry["showSubtechniques"] = True
        techniques.extend(
            {"techniqueID": parent, "showSubtechniques": True}
            for parent in sorted(parents - set(binaries))
        )

        return {
            "name": "LOOBins",
            "versions": {
                "attack": ATTACK_VERSION,
                "navigator": "5.1.0",
                "layer": "4.5",
            },
            "domain": "enterprise-attack",
            "description": "ATT&CK techniques that built-in macOS binaries documented "
            "by LOOBins can perform. Score = number of LOOBins. "
            f"{LOOBINS_SITE}",
            "filters": {"platforms": ["macOS"]},
            "sorting": 3,
            "layout": {"layout": "side", "showID": True, "showName": True},
            "hideDisabled": False,
            "techniques": techniques,
            "gradient": {
                "colors": ["#fff3b0", "#e36414"],
                "minValue": 1,
                # The layer format requires maxValue > minValue.
                "maxValue": max([2, *(len(v) for v in binaries.values())]),
            },
            "legendItems": [],
            "metadata": [{"name": "source", "value": LOOBINS_SITE}],
            "links": [],
            "showTacticRowBackground": False,
            "selectTechniquesAcrossTactics": True,
            "selectSubtechniquesWithParent": False,
        }
