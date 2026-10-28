from fastapi import FastAPI, HTTPException, Depends
from services.animal_service import AnimalService
from schemas.animal import AnimalResponse
from schemas.animal import AnimalCreate
from repositories.animal_repository import AnimalRepository
from models.animal import Animal
from fastapi.testclient import TestClient

# Servidor: uvicorn main:app --reload
app = FastAPI()

def get_animal_service():
    repository = AnimalRepository()
    return AnimalService(repository=repository) 

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/animals", response_model=list[AnimalResponse])
def list_animals(animal_service = Depends(get_animal_service)):
    return animal_service.findall()

@app.post("/animals", response_model = AnimalResponse, status_code=201)
def create_animal(dados: AnimalCreate, animal_service = Depends(get_animal_service)):
    try:
        animal = Animal(
            species = dados.species,
            birth_date = dados.birth_date,
            weight = dados.weight
        )
    except ValueError as erro:
        raise HTTPException(
            status_code=422,
            detail=str(erro)
        )

    return animal_service.register(animal)