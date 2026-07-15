from models.animal import Animal
from services.animal_service import AnimalService
from datetime import date, datetime

def test_register_animal():
      # Create a new object
    animal001 = Animal("bovine", "24/02/2025", 300)

    # Create a service 
    service001 = AnimalService()

    # Saving new object with service
    service001.register(animal001)

    print(animal001.id)

    # Result
    assert animal001 is not None

def test_getbyid_animal():
    # Create a new object
    animal003 = Animal("Bubaline", "28/03/2026", 81)

    # Create a service
    service003 = AnimalService()

    # Saving a new object with service
    service003.register(animal003)

    # Getting by id
    animal = service003.get_by_id(animal003.id)

    # Result
    assert animal.especie == "Bubaline"
    assert animal.birth_date == date(2026, 3, 28)
    assert animal.weight == 81

def test_update_animal():
        # Create a new object
        animal002 = Animal("Suine", "25/03/2026", 80)

        # Create a service
        service002 = AnimalService()

        # Saving a new object with service
        service002.register(animal002)

        # Create new attributes
        animal002.especie = "Caprine"
        animal002.birth_date = "27/03/2026"

        # Updating
        service002.update(animal002)

        # Getting by id
        animal = service002.get_by_id(animal002.id)

        # Result
        assert animal002.especie == "Caprine"
        assert animal002.birth_date == "27/03/2026"



def test_remove_animal():
    # Create a new object
    animal004 = Animal("Bovine", "30/03/2026", 100)
    
    # Create a service
    service004 = AnimalService()

    # Saving a new object with service
    service004.register(animal004)

    # Removing
    service004.remove(animal004.id)

    # Getting by id
    animal = service004.get_by_id(animal004.id)

    # Result
    assert animal is None