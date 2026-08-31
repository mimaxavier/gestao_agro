from services.vaccineapplicationrecord_service import VaccineApplicationService
from repositories.vaccineapplicationrecord_repository import VaccineApplicationRepository
from models.vaccineapplicationrecord import VaccineApplication
from enums.VaccineName import VaccineName
from datetime import datetime, date
import pytest

# ============================================================
# REGISTER
# ============================================================

def test_register_vaccine_application():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name= VaccineName.RAIVA,
        apply_date="20/08/2026"
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    # Act
    service.register(vaccine)

    # Assert
    assert vaccine.id is not None

    result = repository.get_by_id(vaccine.id)

    assert result is not None
    assert result.animal_id == 1
    assert result.vaccine_name == VaccineName.RAIVA
    assert result.apply_date == date(2026, 8, 20)


def test_register_should_raise_error_when_vaccine_application_already_exists():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name= VaccineName.RAIVA,
        apply_date="20/08/2026",
        id=1
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    # Act / Assert
    with pytest.raises(
        ValueError,
        match="O registro já existe!"
    ):
        service.register(vaccine)


# ============================================================
# FIND ALL
# ============================================================

def test_findall_should_return_vaccine_applications():

    # Arrange
    vaccine1 = VaccineApplication(
        animal_id=1,
        vaccine_name=VaccineName.RAIVA,
        apply_date="20/08/2026"
    )

    vaccine2 = VaccineApplication(
        animal_id=2,
        vaccine_name=VaccineName.BRUCELOSE,
        apply_date="21/08/2026"
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    service.register(vaccine1)
    service.register(vaccine2)

    print(vaccine1)
    print(vaccine2)

    # Act
    result = service.findall()

    print(result)

    # Assert
    assert result is not None
    assert len(result) >= 2


# ============================================================
# GET BY ID
# ============================================================

def test_get_by_id_should_return_vaccine_application():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name=VaccineName.RAIVA,
        apply_date="20/08/2026"
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    service.register(vaccine)

    # Act
    result = service.get_by_id(vaccine.id)

    # Assert
    assert result is not None
    assert result.id == vaccine.id
    assert result.animal_id == vaccine.animal_id
    assert result.vaccine_name == vaccine.vaccine_name
    assert result.apply_date == vaccine.apply_date


def test_get_by_id_should_return_none_when_id_does_not_exist():

    # Arrange
    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    # Act
    result = service.get_by_id(999999)

    # Assert
    assert result is None


# ============================================================
# UPDATE
# ============================================================

def test_update_vaccine_application():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name=VaccineName.BRUCELOSE,
        apply_date="20/08/2026"
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    service.register(vaccine)

    vaccine.animal_id = 2
    vaccine.vaccine_name = VaccineName.BRUCELOSE
    vaccine.apply_date = date(2026, 8, 25)

    # Act
    service.update(vaccine)

    # Assert
    result = service.get_by_id(vaccine.id)

    assert result is not None
    assert result.id == vaccine.id
    assert result.animal_id == 2
    assert result.vaccine_name == VaccineName.BRUCELOSE
    assert result.apply_date == date(2026, 8, 25)


def test_update_should_raise_error_when_id_does_not_exist():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name=VaccineName.RAIVA,
        apply_date="20/08/2026",
        id=999999
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    # Act / Assert
    with pytest.raises(
        ValueError,
        match="O registro não existe! Forneça um ID válido."
    ):
        service.update(vaccine)


# ============================================================
# REMOVE
# ============================================================

def test_remove_vaccine_application():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name=VaccineName.RAIVA,
        apply_date="20/08/2026"
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    service.register(vaccine)

    vaccine_id = vaccine.id

    # Act
    service.remove(vaccine_id)

    # Assert
    result = service.get_by_id(vaccine_id)

    assert result is None


def test_remove_should_raise_error_when_id_does_not_exist():

    # Arrange
    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    # Act / Assert
    with pytest.raises(
        ValueError,
        match="O registro não existe! Forneça um ID válido."
    ):
        service.remove(999999)


# ============================================================
# VALIDATE IF EXISTS
# ============================================================

def test_validate_if_vaccine_application_exists():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name=VaccineName.RAIVA,
        apply_date="20/08/2026"
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    service.register(vaccine)

    # Act
    result = service._validate_if_vaccineapplication_exists(
        vaccine.id
    )

    # Assert
    assert result == vaccine.id


def test_validate_if_vaccine_application_does_not_exist():

    # Arrange
    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    # Act / Assert
    with pytest.raises(
        ValueError,
        match="O registro não existe! Forneça um ID válido."
    ):
        service._validate_if_vaccineapplication_exists(999999)


# ============================================================
# VALIDATE OBJECT READY FOR REGISTER
# ============================================================

def test_validate_object_is_ready_for_register():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name=VaccineName.RAIVA,
        apply_date="20/08/2026"
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    # Act
    result = service._validate_object_is_ready_for_register(vaccine)

    # Assert
    assert result is None


def test_validate_object_is_not_ready_when_id_exists():

    # Arrange
    vaccine = VaccineApplication(
        animal_id=1,
        vaccine_name=VaccineName.RAIVA,
        apply_date="20/08/2026",
        id=1
    )

    repository = VaccineApplicationRepository()
    service = VaccineApplicationService(repository)

    # Act / Assert
    with pytest.raises(
        ValueError,
        match="O registro já existe!"
    ):
        service._validate_object_is_ready_for_register(vaccine)

