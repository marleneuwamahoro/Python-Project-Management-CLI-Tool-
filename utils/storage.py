import json


def load_data(filename):
    """Load JSON data."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(filename, data):
    """Save JSON data."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)