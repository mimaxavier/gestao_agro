from datetime import datetime
from models.animal import Animal
from models.plantation import Plantation

corn = Plantation(1, "Corn", "24/01/2026")

print(corn.expected_harvest_date)

Soybean = Plantation(2, "Soybean", "22/05/2026")

print(Soybean.expected_harvest_date)

