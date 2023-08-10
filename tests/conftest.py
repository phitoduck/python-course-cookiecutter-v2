"""
Register pytest plugins, fixtures, and hooks to be used during test execution.

Docs: https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files
"""

# module import paths to python files containing fixtures
pytest_plugins = [
    # e.g. "tests/fixtures/example_fixture.py" should be registered as:
    "tests.fixtures.example_fixture",
]
