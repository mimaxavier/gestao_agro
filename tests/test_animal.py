from models.animal import Animal
from models.vaccineapplicationrecord import VaccineApplication
from datetime import datetime
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import pytest


def test_create_animal():
    animal = Animal("cow", '23/04/2024', 250)

    assert animal.species == "cow"

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

def test_birthdate_cannot_after_today():
    tomorrow = date.today() + timedelta(days=1)

    with pytest.raises(ValueError) as exc_info:
        Animal("bovine", tomorrow.strftime("%d/%m/%Y"), 250)

    assert str(exc_info.value) ==  "Data superior à data de hoje! Entre com uma data válida!"

def test_birthdate_cannot_be_none():
    with pytest.raises(ValueError) as exc_info:
        animal8 = Animal("bovine", None, 250)

        assert str(exc_info.value) == "A data não pode estar vazia!"

def test_birthdate_must_be_date():
    with pytest.raises(TypeError) as exc_info:
        animal9 = Animal("bovine", 23092026, 250)

        assert str(exc_info.value) == "Não é um tipo date válido!"

#Calcular idade
'''def test_calculate_age():
    animal10 = Animal("bovine", "26/01/1992", 250)
    
    assert (
        animal10.calculate_age() == "34 anos, 4 meses e 28 dias"
    )'''

def test_calculate_age():
    animal = Animal("bovine", "23/01/2025", 200)

    age = animal.calculate_age()
    age_in_months = animal.age_inmonths()
    age_formatted = animal.age_formatted()

    assert age == relativedelta(years=1, months=5, days=0)
    assert age_in_months == 17
    assert age_formatted == "1 anos, 5 meses e 0 dias"


