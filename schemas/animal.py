from pydantic import BaseModel, ConfigDict
from datetime import date

model_config = ConfigDict(from_attributes=True)

class AnimalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    species: str
    birth_date: date
    weight: float

class AnimalCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    species: str
    birth_date: date
    weight: float

class AnimalUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    species: str
    birth_date: date
    weight: float
    