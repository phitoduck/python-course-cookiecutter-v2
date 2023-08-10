"""Example pytest fixture."""

from pathlib import Path
from typing import Generator

import pytest

from tests.consts import TEST_ARTIFACTS_DIR


@pytest.fixture(scope="function")
def json_file() -> Generator[Path, None, None]:
    """Demonstrate the usage of pytest fixtures."""
    # setup logic before yield; create a json file
    TEST_ARTIFACTS_DIR.mkdir(exist_ok=True, parents=True)
    json_fpath = TEST_ARTIFACTS_DIR / "example-artifact.json"
    json_fpath.write_text('{"example": "json"}')

    yield json_fpath

    # teardown logic after yield; delete the json file
    json_fpath.unlink()
