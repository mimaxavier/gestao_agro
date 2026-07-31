from datetime import datetime
from models.animal import Animal
from models.vaccineapplicationrecord import VaccineApplication
from models.milkproductionrecord import MilkProductionRecord
from repositories.animal_repository import AnimalRepository
from models.feedingrecord import FeedingRecord
from repositories.feedingrecord_repository import FeedingRecordRepository

animal = Animal("bovine", "22/12/2025", 90)

print(animal.is_a_calf(animal))





