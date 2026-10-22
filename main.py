from fastapi import FastAPI
from services.animal_service import AnimalService
from schemas.animal import AnimalResponse

app = FastAPI()

animal_service = AnimalService()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/animals", response_model=list[AnimalResponse])
def list_animals():
    return animal_service.findall()