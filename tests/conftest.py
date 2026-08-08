"""Pytest fixtures shared across all test modules."""

import pytest
from pathlib import Path


@pytest.fixture
def project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def sample_data_dir(project_root: Path) -> Path:
    """Return the path to the sample raw data directory."""
    return project_root / "data" / "raw"


@pytest.fixture
def taxonomy_dir(project_root: Path) -> Path:
    """Return the path to the taxonomy directory."""
    return project_root / "data" / "taxonomy"


@pytest.fixture
def output_dir(project_root: Path) -> Path:
    """Return the path to the output directory."""
    output = project_root / "data" / "output"
    output.mkdir(parents=True, exist_ok=True)
    return output
