from pydantic import BaseModel
import enum
from typing import List


class Gender(str, enum.Enum):
    male: str = "male"
    female: str = "female"
    other: str = "other"


class Author(BaseModel):
    id: str
    name: str
    country: str
    gender: Gender
    deceased: bool
    books: List[str]
