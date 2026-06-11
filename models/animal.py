from datetime import datetime
from datetime import date
from datetime import date
from dateutil.relativedelta import relativedelta
from models.vaccine import VaccineApplication

class Animal:
    def __init__(self, especie, birth_date, weight, id = None):
        self._validate_species(especie)
        self._validate_weight(weight)
        self._validate_birthdate(birth_date)

        self.especie = especie
        self.birth_date = datetime.strptime(birth_date, r"%d/%m/%Y").date()
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

        if birthdate is None:
            raise ValueError("A data não pode estar vazia!")
        
        birthdate = datetime.strptime(birthdate, r"%d/%m/%Y").date()
        
        if birthdate >= date.today():
            raise ValueError(
                "Data superior a data de hoje! Entre como uma data válida!"
                )
        
        if not isinstance(birthdate, date):
            raise TypeError("Não é um tipo date válido!")

    def calculate_age(self, current_date=None):
        if current_date is None:
            current_date = date.today()

        difference = relativedelta(current_date, self.birth_date)

        return (
            f"{difference.years} anos, "
            f"{difference.months} meses e "
            f"{difference.days} dias"
        )

    def verificar_abate(self):
        return self.weight>450
        
        