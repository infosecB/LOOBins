# PyLOOBins
PyLOOBins is a Python SDK and command-line utility for interacting with LOOBins.

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
  --help  Show this message and exit.

Commands:
  create    Create a YAML template file for a new LOOBin.
  get       Get a LOOBin object.
  validate  Validate a LOOBin YAML file.
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
