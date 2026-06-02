#character database
import json
from pathlib import Path


CHARACTER_FILE = Path("characters.json")


def save_character(character):
    
    if not CHARACTER_FILE.exists():
        with open(CHARACTER_FILE, "w") as f:
            json.dump([], f)

    with open(CHARACTER_FILE, "r") as f:
        characters = json.load(f)

    characters.append(character)

    with open(CHARACTER_FILE, "w") as f:
        json.dump(
            characters,
            f,
            indent=4
        )

