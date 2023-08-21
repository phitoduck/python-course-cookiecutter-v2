import pytest


@pytest.fixture(scope="session")
def project():
    print("Setup")
    yield 1
    print("Teardown")


def test__linting_passes(project):
    print(project)
    assert False


def test__tests_pass():
    ...


def test__install_succeeds():
    ...


"""
Setup:
1. generate a project using cookiecutter
2. create a virtual environment and install project dependencies

Tests:
3. run tests
4. run linting

Cleanup/Teardown:
5. remove virtual environment
6. remove generated project
"""
