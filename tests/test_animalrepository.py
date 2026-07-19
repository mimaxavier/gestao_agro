from repositories.animal_repository import AnimalRepository
from models.animal import Animal
from datetime import date
import pytest

def test_save():

    animal001 = Animal("bovine", "23/05/2024", 300)

    repositorio001 = AnimalRepository()

    animal_id = repositorio001.save(animal001)

    assert animal_id is not None


def test_get_by_id():
    animal002 = Animal("suine", "22/01/2025", 100)
    repositorio002 = AnimalRepository()

    animal_id = repositorio002.save(animal002)

    animal = repositorio002.get_by_id(animal_id)

    assert animal.especie == "suine"
    assert animal.birth_date == date(2025, 1, 22)
    assert animal.weight == 100
    assert animal.id == animal_id

def test_findall():
    # Create objects
    animal015 = Animal("bovine", "25/04/2022", 300)
    animal016 = Animal("caprine", "15/02/2024", 250)

    # Create a repository
    repository015 = AnimalRepository()

    # Save objects
    repository015.save(animal015)
    repository015.save(animal016)

    # Find all
    animals = repository015.find_all()

    # Result
    #assert len(animals) == 19
    assert isinstance(animals, list)
    assert animals[0].especie == "bovine"
    assert animals[1].birth_date == date(2025, 1, 22)

def test_update():
    animal = Animal("suine", "12/09/2020", 156)

    repo = AnimalRepository()

    animal_id = repo.save(animal)

    # altera algo
    animal.especie = "bovine"
    animal.id = animal_id

    repo.update(animal)

    updated = repo.get_by_id(animal_id)

    assert updated.especie == "bovine"

def test_delete():
    #criação
    animal = Animal("suine", "12/09/2020", 156)
    repo = AnimalRepository()

    #ação
    animal_id = repo.save(animal)
    repo.delete(animal_id)

    #resultado
    result = repo.get_by_id(animal_id)
    assert result is None