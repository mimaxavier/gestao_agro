from fastapi import FastAPI, HTTPException, Depends
from services.animal_service import AnimalService
from schemas.animal import AnimalResponse
from schemas.animal import AnimalCreate
from schemas.animal import AnimalUpdate
from repositories.animal_repository import AnimalRepository
from datetime import date
from models.animal import Animal
from fastapi.testclient import TestClient
from fastapi import Path


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

@app.get("/animals/{animal_id}", response_model= AnimalResponse, status_code=200)
def get_animal(animal_id: int, animal_service = Depends(get_animal_service)):
        animal = animal_service.get_by_id(animal_id)

        if animal is None:
            raise HTTPException(
                status_code=404,
                detail="Animal não encontrado!"
            )

        return animal

@app.put("/animals/{animal_id}", status_code=200, response_model=AnimalResponse)
def update_animal(dados: AnimalUpdate, animal_id: int, animal_service = Depends(get_animal_service)):

    animal = Animal(
          species = dados.species,
          birth_date = dados.birth_date,
          weight = dados.weight,
          id = animal_id
    )

    try:
        animal_service.update(animal)
    except ValueError as erro:
        if str(erro) == "O registro não existe!":
            raise HTTPException(status_code=404, detail=str(erro))
        raise

    animal_updated = animal_service.get_by_id(animal_id)

    return animal_updated