"""Pytest configuration file; is executed before test collection."""

import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent
TESTS_DIR_PARENT = (THIS_DIR / "..").resolve()

# ensure that `from tests ...` import statements work within the tests/ dir
sys.path.insert(0, str(TESTS_DIR_PARENT))

# register fixtures so that they can be used in tests
pytest_plugins = ["tests.fixtures.project_dir"]
