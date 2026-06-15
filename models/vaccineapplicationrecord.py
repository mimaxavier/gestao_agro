from datetime import datetime
from datetime import timedelta
from datetime import date

class VaccineApplication:
    valid_names_vaccine = {
        "Brucelose",
        "Raiva",
        "Febre Aftosa"
        "Tuberculose Bovina"
    }

    def __init__(self, animal_id, vaccine_name, apply_date):
        self._validate_animalid(animal_id)
        self._validate_names_vaccines(vaccine_name)


        self.animal_id = animal_id
        self.vaccine_name = vaccine_name
        self.apply_date = datetime.strptime(apply_date, r"%d/%m/%Y").date()
        self.next_dose = self.calculate_next_dose()

    def _validate_animalid(self, animalid):
        if animalid is None:
            raise ValueError("ID do animal não pode estar vazio!")
       
        if not isinstance(animalid, int):
            raise TypeError("Animal ID precisa ser um número inteiro!")

    def _validate_names_vaccines(self, vaccine):
        if vaccine not in self.valid_names_vaccine:
            raise ValueError("Digite um nome de vacina válido!")

    def calculate_next_dose(self):
        interval_days = {
            "Brucelose": 100,
            "Raiva": 150,
        }

        interval = interval_days[self.vaccine_name]

        next_dose = self.apply_date + timedelta(days=interval)

        return next_dose

    