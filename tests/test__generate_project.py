import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

import pytest

from tests.utils.project import generate_project


def test__can_generate_project(project_dir: Path):
    """

    execute: `cookiecutter <template directory> ...`
    """
    assert project_dir.exists()
