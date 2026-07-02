import json
from pathlib import Path
from typing import Any, List, Dict

CHARACTER_FILE = Path("data/characters.json")


def save_character(character: Dict[str, Any]) -> None:
    CHARACTER_FILE.parent.mkdir(parents=True, exist_ok=True)

    if CHARACTER_FILE.exists():
        with open(CHARACTER_FILE, "r") as f:
            characters: List[Dict] = json.load(f)
    else:
        characters = []

    characters.append(character)

    with open(CHARACTER_FILE, "w") as f:
        json.dump(characters, f, indent=2, ensure_ascii=False)


def load_characters() -> List[Dict]:
    if not CHARACTER_FILE.exists():
        return []
    with open(CHARACTER_FILE, "r") as f:
        return json.load(f)
