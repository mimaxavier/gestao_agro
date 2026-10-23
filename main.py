from fastapi import FastAPI
from services.animal_service import AnimalService
from schemas.animal import AnimalResponse
from schemas.animal import AnimalCreate
from models.animal import Animal

# Servidor: uvicorn main:app --reload
app = FastAPI()

animal_service = AnimalService()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/animals", response_model=list[AnimalResponse])
def list_animals():
    return animal_service.findall()

@app.post("/animals", response_model = AnimalResponse)
def create_animal(dados: AnimalCreate):
    animal = Animal(
        species = dados.species,
        birth_date = dados.birth_date,
        weight = dados.weight
    )
    return animal_service.register(animal)