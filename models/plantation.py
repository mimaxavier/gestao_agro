from datetime import datetime
from datetime import timedelta

class Plantation:
    def __init__(self, id, crop_type, planting_date):
        self.id = id
        self.crop_type = crop_type
        self.planting_date = datetime.strptime(planting_date, "%d/%m/%Y")

        self.expected_harvest_date = self.calcular_colheita()

    def calcular_colheita(self):
        crop_cycles = {
            "Corn": 100,
            "Soybean": 250,
            "Sugarcane": 300
        }
        cropcycle = crop_cycles[self.crop_type]
        
        harvest_date = self.planting_date + timedelta(days=cropcycle)

        return harvest_date