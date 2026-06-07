from datetime import datetime
from datetime import date
from models.vaccine import VaccineApplication

class Animal:
    def __init__(self, especie, birth_date, weight, id = None):
        self.especie = especie
        self.birth_date = birth_date.date()
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
        if weight<=0:
            raise ValueError("Peso não pode ser menor ou igual a 0. Digite um peso válido!")
        
        if weight is None:
            raise ValueError ("Precisa digitar um peso.")
            
        if not isinstance(weight, float):
            raise TypeError("O campo precisa ser um número real!")
        
    def _validate_birthdate(self, birthdate):
        if birthdate > date.today():
            raise ValueError("Data superior a data de hoje! Entre como uma data válida!")
        
        if birthdate is None:
            raise ValueError("A data não pode estar vazia!")
        
        if not isinstance(birthdate, date):
            raise TypeError("Não é um tipo date válido!")

    def calcular_idade(self, data_nascimento):
        datadenascimento = datetime.strptime(self.data_nascimento, r"%d/%m/%Y")
        hoje = datetime.today()

        return (hoje - datadenascimento).days/365

    def verificar_abate(self):
        idade = self.calcular_idade()

        return idade>3 or self.peso>=240
        
        