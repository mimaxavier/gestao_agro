from datetime import datetime
from models.vaccine import VaccineApplication

class Animal:
    VALID_SPECIES = {
    "bovine",
    "equine",
    "swine",
    "ovine",
    "caprine",
    "poultry"
}

    def __init__(self, especie, birth_date, weight, id = None):
        self.especie = especie
        self.birth_date = birth_date
        self.weight = weight
        self.id = id

    def validate_species(self):
        if self.especie not in self.VALID_SPECIES:
            raise ValueError("Tipo de espécie inválido!")

    def calcular_idade(self, data_nascimento):
        datadenascimento = datetime.strptime(self.data_nascimento, r"%d/%m/%Y")
        hoje = datetime.today()

        return (hoje - datadenascimento).days/365

    def verificar_abate(self):
        idade = self.calcular_idade()

        return idade>3 or self.peso>=240
        
        