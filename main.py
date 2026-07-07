from datetime import datetime
from models.animal import Animal
from models.vaccineapplicationrecord import VaccineApplication
from models.milkproductionrecord import MilkProductionRecord
from repositories.animal_repository import AnimalRepository
from models.feedingrecord import FeedingRecord
from repositories.feedingrecord_repository import FeedingRecordRepository


# Criação dos Objetos 
feed001 = FeedingRecord(1, "Silagem", 40, "25/03/2026")
repositorio001 = FeedingRecordRepository()

# Salvar o Objeto no banco
repositorio001.save(feed001)

print(feed001.id)

# Trazer o Objeto do banco
repositorio001.get_by_id(feed001.id)

# Criação da atualização do objeto
feed001.type_feeding = "Feno"
feed001.quantity_feeding = 500

print(feed001.id)
# Atualização do Objeto no banco
repositorio001.update(feed001)

# Trazer o Objeto atualizado do banco
repositorio001.get_by_id(feed001.id)


