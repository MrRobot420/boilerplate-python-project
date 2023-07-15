from enum import Enum
from pydantic import BaseModel


class Sex(Enum):
    FEMALE = "female"
    MALE = "male"

    class Config:
        use_enum_values = True


class Person(BaseModel):
    name: str
    age: int
    sex: Sex
