from datetime import datetime
from models.animal import Animal
from models.vaccineapplicationrecord import VaccineApplication
from models.milkproductionrecord import MilkProductionRecord
from repositories.animal_repository import AnimalRepository
from models.feedingrecord import FeedingRecord
from repositories.feedingrecord_repository import FeedingRecordRepository

animal = Animal("bovine", "23/01/2025", 200)
print(animal.calculate_age())
print(animal.age_inmonths())
print(animal.age_formatted())



