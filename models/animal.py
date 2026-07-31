from datetime import datetime
from datetime import date
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from models.vaccineapplicationrecord import VaccineApplication

class Animal:
    def __init__(self, species, birth_date, weight, id = None):
        self._validate_species(species)
        self._validate_weight(weight)
        
        self.species = species
        self.birth_date = self._validate_birthdate(birth_date)
        self.weight = weight
        self.id = id
     

    def _validate_species(self, especie):
        if especie is None:
            raise ValueError ("Precisa digitar uma espécie.")
            
        if not isinstance(especie, str):
            raise TypeError("O campo precisa ser uma string!")
        
        if not especie.strip():
            raise ValueError("O campo não pode estar vazio!")
        
    def _validate_weight(self, weight):
        if weight is None:
            raise ValueError ("Precisa digitar um peso.")

        if not isinstance(weight, (int, float)):
            raise TypeError("O campo precisa ser um número real!")
         
        if weight<=0:
            raise ValueError("Peso não pode ser menor ou igual a 0. Digite um peso válido!")
            
        
    def _validate_birthdate(self, birthdate):

        # Validate if birthdate is none
        if birthdate is None:
            raise ValueError("A data não pode estar vazia!")
        
        # Transform string for date
        if isinstance(birthdate, str):
         birthdate = datetime.strptime(birthdate, r"%d/%m/%Y").date()
        
        # Validate types
        if not isinstance(birthdate, date):
            raise TypeError("Não é um tipo date válido!")

    
        if birthdate > date.today():
            raise ValueError(
            "Data superior à data de hoje! Entre com uma data válida!"
        )

        return birthdate

    def calculate_age(self):
        current_date = date.today()
        return relativedelta(current_date, self.birth_date)

    def age_inmonths(self):
        age = self.calculate_age()
        return age.years * 12 + age.months

    def age_formatted(self):
        age = self.calculate_age()
        return f"{age.years} anos, {age.months} meses e {age.days} dias"

    def is_a_calf(self, animal):
            return animal.age_inmonths() < 13
        