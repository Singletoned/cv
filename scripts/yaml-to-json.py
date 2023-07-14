import json
import pathlib

import yaml


def yaml_to_json(filepath):
    with filepath.open() as f:
        data = yaml.safe_load(f)

    json_output_path = filepath.with_suffix(".json")
    with json_output_path.open("w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    filepath = pathlib.Path("cv.yml")
    yaml_to_json(filepath)
