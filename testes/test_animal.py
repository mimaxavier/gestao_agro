from models.animal import Animal
from models.vaccine import VaccineApplication
from datetime import datetime
from datetime import date
import pytest



def test_create_animal():
    animal = Animal("cow", '23/04/2024', 250)

    assert animal.especie == "cow"

    assert animal.birth_date == datetime.strptime('23/04/2024', r"%d/%m/%Y").date()

    assert animal.weight == 250

    assert animal.id == None

# Validate species
def test_cannot_be_none():
    with pytest.raises(ValueError) as exc_info:

        Animal(None, "24/03/2025", 480)

    assert str(exc_info.value) == "Precisa digitar uma espécie."

def test_must_be_string():
    with pytest.raises(TypeError) as exc_info:

        animal2 = Animal(23, "24/03/2025", 480)

    assert str(exc_info.value) == "O campo precisa ser uma string!"

def test_cannot_be_empty():
    with pytest.raises(ValueError) as exc_info:

        animal3 = Animal(" ", "24/03/2025", 480)

    assert str(exc_info.value) == "O campo não pode estar vazio!"

# Validate weight
def test_weight_cannot_be_zero_or_negative():
    with pytest.raises(ValueError) as exc_info:
        animal4 = Animal("bovine", "20/03/2024", -4)

    assert str(exc_info.value) == "Peso não pode ser menor ou igual a 0. Digite um peso válido!"

def test_weight_cannot_be_empty():
    with pytest.raises(ValueError) as exc_info:
        animal5 = Animal("bovine", "12/12/2023", None)

    assert str(exc_info.value) == "Precisa digitar um peso."

def test_must_be_int():
    with pytest.raises(TypeError) as exc_info:
        animal6 = Animal("bovine", "12/12/2023", "oi")

    assert str(exc_info.value) == "O campo precisa ser um número real!"

# Validate birthdate

def test_validate_birthdate():
    pass

def test_calcular_idade():
    pass