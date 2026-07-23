"""Test the models in the pyloobins.models module."""

from datetime import date

from pyloobins.models import (
    Detection,
    ExampleUseCase,
    LOOBin,
    LOOBinsGroup,
    Resource,
)
from tests.test_data import (
    DetectionFactory,
    ExampleUseCaseFactory,
    LOOBinFactory,
    ResourceFactory,
)


def _sample_loobin() -> LOOBin:
    """Build a deterministic LOOBin for behavioral assertions."""
    return LOOBin(
        name="sample",
        author="tester",
        short_description="short",
        full_description="full",
        created=date(2024, 1, 1),
        example_use_cases=[
            ExampleUseCase(
                name="uc1",
                description="d1",
                tactics=["Discovery", "Execution"],
                tags=["a", "b"],
            ),
            ExampleUseCase(
                name="uc2",
                description="d2",
                tactics=["Execution", "Persistence"],
                tags=["b", "c"],
            ),
        ],
        paths=["/usr/bin/sample"],
        detections=[
            Detection(name="no detection", url="N/A"),
            Detection(name="Sigma", url="https://example.com"),
        ],
    )


def test_detection():
    """The Detection factory builds a Detection."""
    assert isinstance(DetectionFactory.build(), Detection)


def test_resource():
    """The Resource factory builds a Resource."""
    assert isinstance(ResourceFactory.build(), Resource)


def test_example_use_case():
    """The ExampleUseCase factory builds an ExampleUseCase."""
    assert isinstance(ExampleUseCaseFactory.build(), ExampleUseCase)


def test_loobin():
    """The LOOBin factory builds a LOOBin."""
    assert isinstance(LOOBinFactory.build(), LOOBin)


def test_loobin_group():
    """A LOOBinsGroup can be built from a batch of LOOBins."""
    assert LOOBinsGroup(LOOBinFactory.batch(2))


def test_combine_tactics_dedupes_preserving_order():
    """combine_tactics unions use-case tactics, de-duped, in first-seen order."""
    assert _sample_loobin().combine_tactics() == [
        "Discovery",
        "Execution",
        "Persistence",
    ]


def test_combine_tags_dedupes_preserving_order():
    """combine_tags unions use-case tags, de-duped, in first-seen order."""
    assert _sample_loobin().combine_tags() == ["a", "b", "c"]


def test_to_md_renders_sections_and_na_detection():
    """to_md renders the core sections and handles the 'N/A' detection sentinel."""
    md = _sample_loobin().to_md()
    assert "# sample" in md
    assert "/usr/bin/sample" in md
    # A detection whose URL is "N/A" renders as plain text (no link).
    assert "- no detection" in md
    # A detection with a real URL renders as a Markdown link.
    assert "[Sigma](https://example.com)" in md
