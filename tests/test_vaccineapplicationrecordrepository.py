from repositories.vaccineapplicationrecord_repository import VaccineApplicationRepository
from models.vaccineapplicationrecord import VaccineApplication
from datetime import datetime, date
from enums.VaccineName import VaccineName
import pytest

def test_save_vaccine():
    # Create Objects
    vaccine001 = VaccineApplication(1, VaccineName.BRUCELOSE, "30/07/2025")

    repository001 = VaccineApplicationRepository()

    # Saving Object
    repository001.save(vaccine001)

    # Result
    assert vaccine001 is not None

def test_getbyid():
    # Create Objects
    vaccine002 = VaccineApplication(2, VaccineName.RAIVA, "31/07/2025")

    repository002 = VaccineApplicationRepository()

    # Saving Object
    repository002.save(vaccine002)

    # Search for id
    repository002.get_by_id(vaccine002.id)

    # Result
    assert vaccine002.animal_id == 2
    assert vaccine002.vaccine_name == VaccineName.RAIVA
    assert vaccine002.apply_date == date(2025, 7, 31)

def test_update():
    # Create objects
    vaccine003 = VaccineApplication(3, VaccineName.BRUCELOSE, "01/08/2025")
    repository003 = VaccineApplicationRepository()

    # Saving object
    repository003.save(vaccine003)

    # new values attributs
    vaccine003.vaccine_name = VaccineName.RAIVA
    vaccine003.apply_date = "02/08/2025"
    
    # Updating
    repository003.update(vaccine003)

    # Result
    assert vaccine003.vaccine_name == VaccineName.RAIVA
    assert vaccine003.apply_date == "02/08/2025"

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