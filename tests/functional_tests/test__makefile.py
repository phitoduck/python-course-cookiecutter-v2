"""Test that generated makefile works."""

import subprocess
from pathlib import Path


def test__linting_passes(project_dir: Path):
    """Validate that the templatized project has no auto-fixable linting issues."""
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test__tests_pass(project_dir: Path):
    """Validate the the templatized tests pass when executed against a templatized project."""
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)
