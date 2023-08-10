"""Tests for `example_pkg.states_info`."""

from pathlib import Path

import pytest

from example_pkg.states_info import (
    is_city_capitol_of_state,
    slow_add,
)


@pytest.mark.parametrize(
    argnames=("city_name", "state", "is_capitol"),
    argvalues=[
        ("Montgomery", "Alabama", True),
        ("Oklahoma City", "Oklahoma", True),
        ("Salem", "Oregon", True),
        ("Salt Lake City", "Alabama", False),
    ],
)
def test__is_city_capitol_of_state(city_name: str, state: str, is_capitol: bool):
    """Test `is_city_capitol_of_state()`."""
    assert is_city_capitol_of_state(city_name=city_name, state=state) == is_capitol


def test__demonstrate_fixture_use(json_file: Path):
    """
    Demonstrate how to use a fixture.

    The fact that `json_file` is used as an argument means that the
    setup/teardown logic in tests/fixtures/example_fixture.py::json_file() will
    be executed before/after this test, and it's yielded value will be passed to
    this function as the `json_file` argument.
    """
    assert json_file.read_text() == '{"example": "json"}'


@pytest.mark.slow
def test__slow_add():
    """Test `slow_add()`."""
    assert slow_add(1, 2) == 3
