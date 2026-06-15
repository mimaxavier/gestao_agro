from datetime import datetime
from models.animal import Animal
from models.vaccineapplicationrecord import VaccineApplication
from models.milkproductionrecord import MilkProductionRecord
from repositories.animal_repository import AnimalRepository
from models.feedingrecord import FeedingRecord

'''#Criando um animal
#animalzinho = Animal(2, "cow", "18/02/2025", 100)
pingo = Animal("horse", "02/12/2023", 250)
discoteca = Animal("cow", "03/02/2022", 356)

#Criando um repositório
repository = AnimalRepository()

#Usando o repositório pra salvar
#repository.save(animalzinho)
repository.save(pingo)
repository.save(discoteca)

producao1 = ProductionRecord("eggs", "kg", 15, "22/03/2026")'''

#animal5 = Animal("bovine", "20/03/2023", 450)

#animal5.verificar_abate()

#feedingrecord = FeedingRecord(2, "Pastagem", 45, "25/03/2024")

'''production001 = MilkProductionRecord(1, 52, "01/01/2025 05:25:01")

print(production001)
'''

vaccine001 = VaccineApplication(3, "Brucelose", "26/06/2025")

print(vaccine001.calculate_next_dose())