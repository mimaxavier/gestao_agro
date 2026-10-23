from pydantic import BaseModel, ConfigDict
from datetime import date

model_config = ConfigDict(from_attributes=True)

class AnimalResponse(BaseModel):
    id: int
    species: str
    birth_date: date
    weight: float

class AnimalCreate(BaseModel):
    species: str
    birth_date: date
    weight: float
    