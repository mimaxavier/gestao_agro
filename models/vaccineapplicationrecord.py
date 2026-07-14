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

    def __init__(self, animal_id, vaccine_name, apply_date, id = None):

        self.animal_id = self._validate_animalid(animal_id)
        self.vaccine_name = self._validate_names_vaccines(vaccine_name)
        self.apply_date = self._validate_apply_date(apply_date)
        self.id = id
        self.next_dose = self.calculate_next_dose()

    def _validate_animalid(self, animalid):
        if animalid is None:
            raise ValueError("ID do animal não pode estar vazio!")
       
        if not isinstance(animalid, int):
            raise TypeError("Animal ID precisa ser um número inteiro!")
        
        return animalid

    def _validate_names_vaccines(self, vaccine):
        if vaccine not in self.valid_names_vaccine:
            raise ValueError("Digite um nome de vacina válido!")
        
        return vaccine

    def _validate_apply_date(self, applydate):

        if isinstance(applydate, str):
           applydate = datetime.strptime(applydate, r"%d/%m/%Y").date()

        elif isinstance(applydate, date):
            self.apply_date = applydate

        else:
            raise TypeError("Precisa informar no formato date ou string!")

        return applydate

    def calculate_next_dose(self):
        interval_days = {
            "Brucelose": 100,
            "Raiva": 150,
        }

        interval = interval_days[self.vaccine_name]

        next_dose = self.apply_date + timedelta(days=interval)

        return next_dose

    