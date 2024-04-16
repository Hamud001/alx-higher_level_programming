#!/usr/bin/python3
"""Creae object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create object from a JSON."""
    with open(filename) as f:
        return json.load(f)
