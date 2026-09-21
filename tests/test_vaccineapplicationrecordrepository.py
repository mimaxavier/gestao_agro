from repositories.vaccineapplicationrecord_repository import VaccineApplicationRepository
from models.vaccineapplicationrecord import VaccineApplication
from datetime import datetime, date
from enums.VaccineName import VaccineName
import pytest

def test_save_vaccine():
    vaccine001 = VaccineApplication(
        1,
        VaccineName.BRUCELOSE,
        "30/07/2025"
    )

    repository = VaccineApplicationRepository()

    repository.save(vaccine001)

    assert vaccine001.id is not None

    result = repository.get_by_id(vaccine001.id)

    assert result is not None
    assert result.animal_id == 1
    assert result.vaccine_name == VaccineName.BRUCELOSE
    assert result.apply_date == date(2025, 7, 30)

def test_getbyid():
    vaccine002 = VaccineApplication(
        2,
        VaccineName.RAIVA,
        "31/07/2025"
    )

    repository002 = VaccineApplicationRepository()

    repository002.save(vaccine002)

    result = repository002.get_by_id(vaccine002.id)

    assert result is not None
    assert result.id == vaccine002.id
    assert result.animal_id == 2
    assert result.vaccine_name == VaccineName.RAIVA
    assert result.apply_date == date(2025, 7, 31)

def test_find_all():
    vaccine001 = VaccineApplication(
        1,
        VaccineName.BRUCELOSE,
        "30/07/2025"
    )

    vaccine002 = VaccineApplication(
        2,
        VaccineName.RAIVA,
        "31/07/2025"
    )

    repository = VaccineApplicationRepository()

    repository.save(vaccine001)
    repository.save(vaccine002)

    result = repository.find_all()

    vaccines_by_id = {
        vaccine.id: vaccine
        for vaccine in result
    }

    assert vaccines_by_id[vaccine001.id].animal_id == 1
    assert vaccines_by_id[vaccine001.id].vaccine_name == VaccineName.BRUCELOSE
    assert vaccines_by_id[vaccine001.id].apply_date == date(2025, 7, 30)

    assert vaccines_by_id[vaccine002.id].animal_id == 2
    assert vaccines_by_id[vaccine002.id].vaccine_name == VaccineName.RAIVA
    assert vaccines_by_id[vaccine002.id].apply_date == date(2025, 7, 31)

    assert isinstance(result, list)

def test_update():
    vaccine003 = VaccineApplication(
        3,
        VaccineName.BRUCELOSE,
        "01/08/2025"
    )

    repository003 = VaccineApplicationRepository()

    repository003.save(vaccine003)

    vaccine003.vaccine_name = VaccineName.RAIVA
    vaccine003.apply_date = date(2025, 8, 2)

    repository003.update(vaccine003)

    result = repository003.get_by_id(vaccine003.id)

    assert result is not None
    assert result.id == vaccine003.id
    assert result.animal_id == 3
    assert result.vaccine_name == VaccineName.RAIVA
    assert result.apply_date == date(2025, 8, 2)

def test_delete():
    # Create objects
    vaccine004 = VaccineApplication(1, VaccineName.RAIVA, "23/03/2026")
    repository004 = VaccineApplicationRepository()

    # Saving Objects
    repository004.save(vaccine004)

    # Deleting
    repository004.delete(vaccine004.id)

    # Get by id
    result = repository004.get_by_id(vaccine004.id)

    # Result
    assert result is None