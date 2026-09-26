from repositories.vaccineapplicationrecord_repository import VaccineApplicationRepository
from enums.IntervalVaccines import IntervalVaccines
from enums.VaccineName import VaccineName
from datetime import timedelta
from datetime import datetime, date
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

    def _validate_apply_date(self, apply_date):

        if isinstance(apply_date, str):
            try:
                return datetime.strptime(apply_date, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError(
                "Data de aplicação inválida!"
            )

        if isinstance(apply_date, date):
            return apply_date

        raise TypeError(
            "A data de aplicação deve ser uma string ou date."
    )

    def _validate_animal_id(self, animal_id):

        if animal_id is None:
            raise ValueError("ID do animal não pode estar vazio!")

        if not isinstance(animal_id, int):
            raise TypeError("Animal ID precisa ser um número inteiro!")

        return animal_id

    def _validate_vaccine_name(self, vaccine_name):

        if not isinstance(vaccine_name, VaccineName):
            raise TypeError("Digite um nome de vacina válido!")

        return vaccine_name

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

        vaccineapplication.animal_id = self._validate_animal_id(
        vaccineapplication.animal_id
    )
        vaccineapplication.vaccine_name = self._validate_vaccine_name(
        vaccineapplication.vaccine_name
    )

        vaccineapplication.apply_date = self._validate_apply_date(
        vaccineapplication.apply_date
    )

        self.repository.update(vaccineapplication)

    def remove(self, id):
        self._validate_if_vaccineapplication_exists(id)

        self.repository.delete(id)

    def calculate_next_dose(self, vaccineapplication):
        interval = IntervalVaccines[vaccineapplication.vaccine_name.name].value

        return vaccineapplication.apply_date + timedelta(days=interval)
        