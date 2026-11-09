from fastapi.testclient import TestClient
from main import app
from main import get_animal_service
from services.animal_service import AnimalService
from repositories.animal_repository import AnimalRepository
from database.init_database import init_database
import pytest
from datetime import date
from models.animal import Animal

@pytest.fixture
def client(tmp_path):
    db_path = tmp_path/"farm_test.db"

    init_database(db_path)

    repository = AnimalRepository(db_path=db_path)

    service = AnimalService(repository=repository)

    original_override = app.dependency_overrides.get(get_animal_service)

    app.dependency_overrides[get_animal_service] = lambda: service

    try:
        yield TestClient(app), repository
    finally:
        if original_override is None:
            app.dependency_overrides.pop(get_animal_service, None)
        else:
            app.dependency_overrides[get_animal_service] = original_override
    

def get_test_animal_service():
    repo_temp = AnimalRepository(db_path="database/temp_repository")

    service = AnimalService(repo_temp)

    return service


def test_health_check(client):

    client, repository = client

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_list_animals(client):

    client, repository = client

    animal = Animal(
        species="Bovino",
        birth_date=date(2024, 5, 10),
        weight=350
    )

    repository.save(animal)

    response = client.get("/animals")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json() == [{'id': 1, 'species': 'Bovino', 'birth_date': '2024-05-10', 'weight': 350}]

def test_get_animal_by_id(client):
    client, repository = client

    animal = Animal(
        species="Caprino",
        birth_date=date(2024, 4, 11),
        weight=255
    )

    animal_id = repository.save(animal)

    response = client.get(f"/animals/{animal_id}")

    assert response.status_code == 200
    assert response.json() == ({
        'id': animal_id, 'species': 'Caprino', 'birth_date': '2024-04-11', 'weight': 255
    })
