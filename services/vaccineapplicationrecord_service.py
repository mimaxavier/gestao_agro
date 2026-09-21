from repositories.vaccineapplicationrecord_repository import VaccineApplicationRepository
from enums.IntervalVaccines import IntervalVaccines
from enums.VaccineName import VaccineName
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

class VaccineApplicationService:
    def __init__(self, repository = None):
        self.repository = repository or VaccineApplicationRepository()


    #Validações
    def _validate_if_vaccineapplication_exists(self, id):
        vaccineapplication_db = self.repository.get_by_id(id)

        if vaccineapplication_db is None:
            raise ValueError("O registro não existe! Forneça um ID válido.")
        else:
            return id

    def _validate_object_is_ready_for_register(self, vaccineapplication):
        if vaccineapplication.id is not None:
            raise ValueError("O registro já existe!")

    #CRUD

    def register(self, vaccineapplication):
        self._validate_object_is_ready_for_register(vaccineapplication)

        self.repository.save(vaccineapplication)

        logger.info = ("Vacinação Registrada")

    def findall(self):
        return self.repository.find_all()

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def update(self, vaccineapplication):
        self._validate_if_vaccineapplication_exists(vaccineapplication.id)

        self.repository.update(vaccineapplication)

    def remove(self, id):
        self._validate_if_vaccineapplication_exists(id)

        self.repository.delete(id)

    def calculate_next_dose(self, vaccineapplication):
        interval = IntervalVaccines[vaccineapplication.vaccine_name.name].value

        return vaccineapplication.apply_date + timedelta(days=interval)
        