import json
import subprocess
from pathlib import Path

THIS_DIR = Path(__file__).parent
PROJECT_DIR = (THIS_DIR / "../").resolve()

def test__can_generate_project():
    """
    
    execute: `cookiecutter <template directory> ...`
    """
    cookiecutter_config = {
        "default_context": {"repo_name": "test-repo"}
    }
    cookiecutter_config_fpath = PROJECT_DIR / "tests/cookiecutter.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
        "--verbose"
    ]
    print("COMMAND:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    generated_project_dir = PROJECT_DIR / "sample" / cookiecutter_config["default_context"]["repo_name"]
    assert generated_project_dir.exists()
