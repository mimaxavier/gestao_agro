from models.vaccineapplicationrecord import VaccineApplication
from datetime import datetime
from datetime import date
import pytest

def test_animalid_vaccine_cannot_be_empty():
    with pytest.raises(ValueError) as exc_info:

        vaccine002 = VaccineApplication(None, "Brucelose", "24/05/2024")

    assert str(exc_info.value) == "ID do animal não pode estar vazio!"

def test_animalid_vaccine_must_be_int():
    with pytest.raises(TypeError) as exc_info:

        vaccine001 = VaccineApplication("Um", "Brucelose", "24/05/2024")

    assert str(exc_info.value) == "Animal ID precisa ser um número inteiro!" 

def test_name_vaccine_in_validnames():
    with pytest.raises(ValueError) as exc_info:

        vaccine003 = VaccineApplication(1, "dor", "24/05/2024")

    assert str(exc_info.value) == "Digite um nome de vacina válido!"

def test_calculate_next_dose():

    vaccine004 = VaccineApplication(3, "Raiva", "26/06/2025")

    assert vaccine004.calculate_next_dose == date(2025, 11, 23)


