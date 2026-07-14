from repositories.vaccineapplicationrecord_repository import VaccineApplicationRepository
from models.vaccineapplicationrecord import VaccineApplication
from datetime import datetime, date
import pytest

def test_save_vaccine():
    # Create Objects
    vaccine001 = VaccineApplication(1, "Brucelose", "30/07/2025")

    repository001 = VaccineApplicationRepository()

    # Saving Object
    repository001.save(vaccine001)

    # Result
    assert vaccine001 is not None

def test_getbyid():
    # Create Objects
    vaccine002 = VaccineApplication(2, "Raiva", "31/07/2025")

    repository002 = VaccineApplicationRepository()

    # Saving Object
    repository002.save(vaccine002)

    # Search for id
    repository002.get_by_id(vaccine002.id)

    # Result
    assert vaccine002.animal_id == 2
    assert vaccine002.vaccine_name == "Raiva"
    assert vaccine002.apply_date == date(2025, 7, 31)



