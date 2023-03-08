"""Models that represent a LOOBin and its various components"""
from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel


class Detection(BaseModel):
    """Detection model"""

    source: str
    url: Union[List[str], str]


class ExternalReference(BaseModel):
    """External reference model"""

    name: str
    url: str


class FullPath(BaseModel):
    """Full path model"""

    path: str


class Command(BaseModel):
    """Command model"""

    command: str
    description: str
    use_case: str


class LOOBin(BaseModel):
    """LOOBin model"""

    name: str
    description: str
    author: str
    created: datetime
    commands: List[Command]
    full_path: List[FullPath]
    detections: List[Detection]
    external_references: Optional[List[ExternalReference]]
