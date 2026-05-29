from datetime import datetime
from datetime import timedelta
from datetime import date

class VaccineApplication:
    def __init__(self, animal_id, vaccine_name, apply_date):
        self.animal_id = animal_id
        self.vaccine_name = vaccine_name
        self.apply_date = datetime.strptime(apply_date, r"%d/%m/%Y").date()
        self.next_dose = self.calculate_next_dose().date()
        self.status = self.display_info()


    def calculate_next_dose(self):
        interval_days = {
            "Brucelose": 100,
            "Raiva": 150,
        }

        interval = interval_days[self.vaccine_name]

        next_dose = self.apply_date + timedelta(days=interval)

        return next_dose


    def is_overdue(self):
       return date.today() > self.next_dose

    def display_info(self):
        dataformatada = self.apply_date.strftime(r"%d/%m/%Y")
        dataformatadanext = self.next_dose.strftime(r"%d/%m/%Y")

        status = { "Animal": self.animal_id,
            "Última Vacina": self.vaccine_name,
            "Data da Última vacina": dataformatada,
            "Data da Próxima dose": dataformatadanext
        }

        return status
    
    def add_notes(self, note):
        self.note = note
    
    def validate_apply_date(self):
        return self.apply_date > datetime.today().date()

    def register_booster(self):
        pass