"""Test that the cookiecutter template is valid."""
from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """Test that this cmd does not fail: `cookiecutter <template directory> ...`."""
    assert project_dir.exists()
