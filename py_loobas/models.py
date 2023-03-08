from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Detection(BaseModel):
    source: str
    url: List[str]

class ExternalReference(BaseModel):
    name: str
    url: str

class Path(BaseModel):
    path: str

class Command(BaseModel):
    command: str
    description: str
    use_case: str

class LOOBASItem(BaseModel):
    name: str
    description: str
    author: str
    created: datetime.date
    commands: List[Command]
    full_path: List[Path]
    detections: List[Detection]
    external_references: Optional[List[ExternalReference]]