from models.vaccineapplicationrecord import VaccineApplication
from datetime import datetime
from datetime import date
from enums.VaccineName import VaccineName
import pytest

def test_animalid_vaccine_cannot_be_empty():
    with pytest.raises(ValueError) as exc_info:

        vaccine002 = VaccineApplication(None, VaccineName.BRUCELOSE, "24/05/2024")

    assert str(exc_info.value) == "ID do animal não pode estar vazio!"

def test_animalid_vaccine_must_be_int():
    with pytest.raises(TypeError) as exc_info:

        vaccine001 = VaccineApplication("Um", VaccineName.BRUCELOSE, "24/05/2024")

    assert str(exc_info.value) == "Animal ID precisa ser um número inteiro!" 

def test_name_vaccine_in_validnames():
    with pytest.raises(TypeError) as exc_info:

        vaccine003 = VaccineApplication(1, "dor", "24/05/2024")

    assert str(exc_info.value) == "Digite um nome de vacina válido!"

def test_apply_date_should_accept_valid_string():
    vaccine = VaccineApplication(
        1,
        VaccineName.RAIVA,
        "20/08/2026"
    )

    assert vaccine.apply_date == date(2026, 8, 20)


def test_apply_date_should_accept_date():
    apply_date = date(2026, 8, 20)

    vaccine = VaccineApplication(
        1,
        VaccineName.RAIVA,
        apply_date
    )

    assert vaccine.apply_date == apply_date


def test_apply_date_should_reject_invalid_type():
    with pytest.raises(TypeError) as exc_info:
        VaccineApplication(
            1,
            VaccineName.RAIVA,
            12345
        )

    assert str(exc_info.value) == (
        "Precisa informar no formato date ou string!"
    )


def test_apply_date_should_reject_invalid_format():
    with pytest.raises(ValueError):
        VaccineApplication(
            1,
            VaccineName.RAIVA,
            "20/08/2026 10:30"
        )

