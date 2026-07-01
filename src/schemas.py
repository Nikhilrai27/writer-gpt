from pydantic import BaseModel
from typing import List


class CharacterMemory(BaseModel):
    name: str
    role: str
    summary: str
    facts: List[str]
