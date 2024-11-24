# PyLOOBins
PyLOOBins is a Python SDK and command-line utility for programmatically interacting with [LOOBins](https://loobins.io).

You can download PyLOOBins from PyPI by running the following command:
`pip install pyloobins`

PyLOOBins requires Python 3.8 or later.

## Usage
### Command-line

You can run `pyloobins --help` to see the available commands and options.

```
>>> pyloobins --help

Usage: pyloobins [OPTIONS] COMMAND [ARGS]...

  Create, validate, and view LOOBin objects.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  create       Create a YAML template file for a new LOOBin.
  export-stix  Export the LOOBins STIX bundle file.
  get          Get a LOOBin object.
  validate     Validate a LOOBin YAML file.
```

You can run `pyloobins <command> --help` to see the available options for a specific command.
```
>>> pyloobins validate --help
Usage: pyloobins validate [OPTIONS]

  Validate a LOOBin YAML file.

Options:
  --path TEXT  The path of the LOOBin YAML file to validate.  [required]
  --help       Show this message and exit.
```

### SDK

You can use pyloobins as a Python SDK to programmatically interact with LOOBins.

#### pyloobins.util
The util module can be used to get LOOBin objects from the LOOBins API, validate LOOBin YAML files, and create LOOBin YAML templates.

**Example:** get all LOOBins and print a list of the use case code.

```
from pyloobins import util

loobins = util.get_loobins()

for loobin in loobins:
  for uc in loobin.example_use_cases:
    print(f"{loobin.name}: {uc.code}")
```

#### pyloobins.models
The models module contains the classes that represent a LOOBin and its various components. 

**Example:** programmitcally create a LOOBin object.

```
from pyloobins.models import Detection, ExampleUseCase, LOOBin, Resource

l = LOOBin(
        name="",
        short_description="A short description of the binary goes here.",
        full_description="A full length description of the binary goes here.",
        author="Enter your name or alias here.",
        created=date.today(),
        example_use_cases=[
            ExampleUseCase(
                name="An Example Use Case",
                description="A description of the use case goes here.",
                code="A code snippet goes here.",
                tactics=["Discovery"],
                tags=["example_tag", "another_tag"],
            )
        ],
        paths=["/enter/binary/path/here"],
        detections=[
            Detection(
                name="A detection source (e.g. Sigma)",
                url="https://urltodetection.here",
            )
        ],
        resources=[
            Resource(
                name="Name of resources.",
                url="https://urlofexternalreference.here",
            )
        ],
        acknowledgements=["Enter any acknowledgements here."],
    )

with open ("loobin.yaml", "w") as f:
  f.write(l.to_yaml())
```
