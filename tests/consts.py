"""Constant values used for tests."""

from pathlib import Path

THIS_DIR = Path(__file__).parent

TEST_ARTIFACTS_DIR = (THIS_DIR / "artifacts").resolve()
"""Directory where artifacts created at test time are stored."""
