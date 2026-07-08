from datetime import datetime
from models.animal import Animal
from models.vaccineapplicationrecord import VaccineApplication
from models.milkproductionrecord import MilkProductionRecord
from repositories.animal_repository import AnimalRepository
from models.feedingrecord import FeedingRecord
from repositories.feedingrecord_repository import FeedingRecordRepository


# Criação dos Objetos 
feed002 = FeedingRecord(35, "Capim", 40, "10/03/2026")
repositorio001 = FeedingRecordRepository()

# Salvar o Objeto no banco
repositorio001.save(feed002)

print(feed002.id)

repositorio001 = FeedingRecordRepository()

# Trazer o Objeto do banco
repositorio001.get_by_id(feed002.id)

# Criação da atualização do objeto
feed002.type_feeding = "Feno"
feed002.quantity_feeding = 38

print(feed002.id)
# Atualização do Objeto no banco
repositorio001.update(feed002)

# Trazer o Objeto atualizado do banco
repositorio001.get_by_id(feed002.id)


