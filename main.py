from datetime import datetime
from models.animal import Animal
from models.plantation import Plantation
from models.vaccine import VaccineApplication
from models.productionrecord import ProductionRecord
from repositories.animal_repository import AnimalRepository

#Criando um animal
#animalzinho = Animal(2, "cow", "18/02/2025", 100)
pingo = Animal("horse", "02/12/2023", 250)
discoteca = Animal("cow", "03/02/2022", 356)

#Criando um repositório
repository = AnimalRepository()

#Usando o repositório pra salvar
#repository.save(animalzinho)
repository.save(pingo)
repository.save(discoteca)

producao1 = ProductionRecord("eggs", "kg", 15, "22/03/2026")
