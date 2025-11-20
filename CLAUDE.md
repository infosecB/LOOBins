# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LOOBins (Living Off the Orchard: macOS Binaries) is a cybersecurity resource that documents macOS built-in binaries that can be abused by threat actors. The project consists of:

1. **YAML Database**: Collection of LOOBin definitions in `/LOOBins/` directory
2. **Python SDK**: PyLOOBins package in `/src/pyloobins/` for programmatic access
3. **Static Site Generator**: Generates browsable HTML documentation from YAML files
4. **Web Application**: Data consumed at https://loobins.io

**Important**: This project does NOT include Unix binaries covered by GTFOBins unless they have macOS-specific use cases (e.g., sqlite3).

## Development Commands

### Python Development (PyLOOBins SDK)
```bash
# Install dependencies with Poetry
poetry install

# Run all tests
poetry run pytest

# Run specific test file
poetry run pytest tests/test_data.py
poetry run pytest tests/test_models.py -v

# Lint and format code
poetry run black src/
poetry run isort src/ --profile black
poetry run pylint src/pyloobins/

# Run pre-commit hooks
pre-commit run --all-files

# Validate LOOBin YAML files
poetry run pyloobins validate --path LOOBins/example.yml

# Create new LOOBin template
poetry run pyloobins create --name "BinaryName"
poetry run pyloobins create --name "BinaryName" --path LOOBins/

# Get LOOBin data as JSON
poetry run pyloobins get --name "osascript"

# Export STIX bundle
poetry run pyloobins export-stix --file-name loobins_stix.json --path .

# Generate static website
poetry run pyloobins generate-site --output-dir docs
poetry run pyloobins generate-site --output-dir site --loobins-path LOOBins/
```

## LOOBin YAML Schema

Each LOOBin must follow the schema defined in `/docs/schema.md`:

**Required fields:**
- `name`: Binary name
- `author`: Author of the LOOBin entry
- `short_description`: Brief description for card display (used in search results and cards)
- `full_description`: Detailed description (displays on LOOBin's page)
- `created`: Date in YYYY-MM-DD format
- `example_use_cases`: Array of use cases with name, description, optional code, tactics, and tags
- `paths`: Array of binary paths on macOS (e.g., `/usr/bin/osascript`)
- `detections`: Array of detection sources with name and URL

**Optional fields:**
- `resources`: External references (name and URL)
- `acknowledgements`: Array of acknowledgement strings

**MITRE ATT&CK Tactics** (use exact spelling):
- Reconnaissance, Resource Development, Initial Access, Execution
- Persistence, Privilege Escalation, Defense Evasion, Credential Access
- Discovery, Lateral Movement, Collection, Exfiltration
- Command and Control, Impact

## Architecture

### Core Components

1. **Models** (`src/pyloobins/models.py`):
   - Pydantic v2 models: `LOOBin`, `ExampleUseCase`, `Detection`, `Resource`, `LOOBinsGroup`
   - Methods: `to_yaml()`, `to_md()`, `to_stix()`, `combine_tactics()`, `combine_tags()`
   - STIX2 integration for exporting threat intelligence data

2. **Utilities** (`src/pyloobins/util.py`):
   - `get_loobins(path="")`: Loads LOOBins from YAML files (searches parent directories if no path)
   - `validate_loobin(yml_path)`: Validates YAML against schema
   - `make_template(name)`: Creates template LOOBin object
   - `normalize_file_name(title)`: Converts binary name to lowercase with underscores

3. **CLI** (`src/pyloobins/cli.py`):
   - Click-based command interface with commands: `validate`, `create`, `get`, `export-stix`, `generate-site`

4. **Static Site Generator** (`src/pyloobins/static_site.py`):
   - `StaticSiteGenerator` class generates complete HTML site
   - Generates: homepage (index.html), binaries.html, individual LOOBin pages, tactics.html, about.html
   - Uses Jinja2 templates from `src/pyloobins/templates/`
   - Calculates statistics: total LOOBins, tactics, tags, use cases, detections

### Data Flow

1. **Loading**: `get_loobins()` searches for `/LOOBins/*.yml` files up to 5 parent directories
2. **Parsing**: YAML files parsed and validated against Pydantic models
3. **Processing**: LOOBin objects can be exported as JSON, YAML, Markdown, or STIX2
4. **Generation**: Static site generator creates browsable HTML documentation

### Validation Pipeline

- **CI/CD**: `.github/workflows/validate_loobins.yml` validates changed YAML files on PRs
- **Pre-commit hooks**: Enforce code quality with black, isort, pylint
- **Schema validation**: Pydantic models ensure YAML files match schema
- **VS Code integration**: SchemaStore provides YAML validation in VS Code (requires YAML extension)

## Contributing Guidelines

Follow `/CONTRIBUTING.md` for adding new LOOBins. Key steps:
1. Check existing issues to avoid duplicate work
2. Create issue using "New LOOBin" template
3. Fork repository and create branch
4. Create YAML file in `/LOOBins/` directory following schema
5. Validate with `pyloobins validate --path filename.yml`
6. Submit PR with descriptive message