'''Module contains various utility functions'''
import yaml
from .models import LOOBin


def validate_loobin(yml_path: str) -> bool:
    """Validates LOOBin YAML file"""
    with open(yml_path, "r",encoding="utf-8") as stream:
        try:
            ycontent = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    try:
        LOOBin(**ycontent)
        print(f"LOOBin at {yml_path} is valid.")
        return True
    except Exception as exc:
        print(f"LOOBin at {yml_path} is NOT valid.")
        print(exc)
        return False
