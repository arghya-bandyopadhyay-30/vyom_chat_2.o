import os
import yaml

def load_yaml(config_path: str) -> dict:
    with open(config_path, "r") as file:
        try:
            return yaml.load(os.path.expandvars(file.read()), Loader=yaml.SafeLoader)
        except Exception:
            raise ValueError(f"Pipeline Yaml not found at {config_path}")