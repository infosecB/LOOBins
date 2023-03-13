"""Model that represents a LOOBin and its various components"""
from typing import List, Optional, Union
from datetime import date
from pydantic import BaseModel


class Detection(BaseModel):
    """Detection model"""

    Source: str
    URL: Union[List[str], str]


class ExternalReference(BaseModel):
    """External reference model"""

    Name: str
    URL: str


class FullPath(BaseModel):
    """Full path model"""

    Path: str


class Shell(BaseModel):
    """Shell model"""

    Code: str
    Description = (
        "It can be used to break out from restricted environments by spawning"
        " an interactive system shell."
    )


class Command(BaseModel):
    """Command model"""

    Code: str
    Description = (
        "It can be used to break out from restricted environments by running"
        " non-interactive system commands."
    )


class ReverseShell(BaseModel):
    """Reverse Shell model"""

    Code: str
    Description = (
        "It can send back a reverse shell to a listening attacker to open a"
        " remote network access."
    )


class NonInteractiveReverseShell(BaseModel):
    """Non-interactive Reverse Shell model"""

    Code: str
    Description = (
        "It can send back a non-interactive reverse shell to a listening"
        " attacker to open a remote network access."
    )


class BindShell(BaseModel):
    """Bind Shell model"""

    Code: str
    Description = (
        "It can bind a shell to a local port to allow remote network access."
    )


class NonInteractiveBindShell(BaseModel):
    """Non-interactive Bind Shell model"""

    Code: str
    Description = (
        "It can bind a non-interactive shell to a local port to allow remote"
        " network access."
    )


class FileUpload(BaseModel):
    """File Upload model"""

    Code: str
    Description = "It can exfiltrate files on the network."


class FileDownload(BaseModel):
    """File Download model"""

    Code: str
    Description = "It can download remote files."


class FileWrite(BaseModel):
    """File Write model"""

    Code: str
    Description = (
        "It writes data to files, it may be used to do privileged writes or"
        " write files outside a restricted file system."
    )


class FileRead(BaseModel):
    """File Read model"""

    Code: str
    Description = (
        "It reads data from files, it may be used to do privileged reads or"
        " disclose files outside a restricted file system."
    )


class LibraryLoad(BaseModel):
    """Library Load model"""

    Code: str
    Description = (
        "It loads shared libraries that may be used to run code in the binary"
        " execution context."
    )


class SUID(BaseModel):
    """SUID model"""

    Code: str
    Description = (
        "If the binary has the SUID bit set, it does not drop the elevated"
        " privilegesand may be abused to access the file system, escalate or"
        " maintain privilegedaccess as a SUID backdoor. If it is used to run"
        " `sh -p`, omit the `-p` argumenton systems like Debian (<= Stretch)"
        " that allow the default `sh` shell to run withSUID privileges.\n\nThis"
        " example creates a local SUID copy of the binary and runsit to"
        " maintain elevated privileges. To interact with an existing SUID"
        " binary skipthe first command and run the program using its original"
        " path."
    )


class Sudo(BaseModel):
    """Sudo model"""

    Code: str
    Description = (
        "If the binary is allowed to run as superuser by `sudo`,"
        "it does not drop the elevated privileges and may be used to access"
        "the file system, escalate or maintain privileged access."
    )


class Capabilities(BaseModel):
    """Capabilities model"""

    Code: str
    Description = (
        "If the binary has the Linux `CAP_SETUID` capability set or it is"
        " executedby another binary with the capability set, it can be used as"
        " a backdoor to maintainprivileged access by manipulating its own"
        " process UID."
    )


class LimitedSUID(BaseModel):
    """LimitedSUID model"""

    Code: str
    Description = (
        "If the binary has the SUID bit set, it may be abused to access the"
        " file system, escalate or maintain access with elevated privileges"
        " working as a SUID backdoor. If it is used to run commands (e.g., via"
        " `system()`-like invocations) it only works on systems like Debian (<="
        " Stretch) that allow the default `sh` shell to run with SUID"
        " privileges.\n\nThis example creates a local SUID copy of the binary"
        " and runs it to maintain elevated privileges. To interact with an"
        " existing SUID binary skip the first command and run the program using"
        " its original path."
    )


class Functions(BaseModel):
    """Defines the function base class"""

    Shell: Optional[Shell]
    LimitedSUID: Optional[LimitedSUID]


class LOOBin(BaseModel):
    """LOOBin model"""

    Name: str
    Description: str
    Author: str
    Created: date
    Functions: Functions
    Full_Path: List[FullPath]
    Detections: List[Detection]
    External_References: Optional[List[ExternalReference]]
