"""
src/utils.py — Shared helpers.
"""

import yaml


def load_config(path: str) -> dict:
    """Load a YAML config file into a dict."""
    with open(path) as f:
        return yaml.safe_load(f)
