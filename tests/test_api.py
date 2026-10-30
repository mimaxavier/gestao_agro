from fastapi.testclient import TestClient
from main import app
from main import get_animal_service
from services.animal_service import AnimalService
from repositories.animal_repository import AnimalRepository
from database.init_database import init_database
import pytest

client = TestClient(app)

@pytest.fixture
def client(tmp_path):
    db_path = tmp_path/"farm_test.db"

    init_database(db_path)
    

def get_test_animal_service():
    repo_temp = AnimalRepository(db_path="database/temp_repository")

    service = AnimalService(repo_temp)

    return service


def test_health_check():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get():
    pass