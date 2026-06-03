from models.animal import Animal
from datetime import datetime

class FeedingRecord:
    valid_feed_types = [
            "Silagem",
            "Feno",
            "Capim",
            ]

    def __init__(self, animal_id, type_feeding, quantity, date_feeding):
        self.animal_id = animal_id
        self.typefeeding = type_feeding
        self.quantity = quantity
        self.date_feeding = datetime.strptime(self.date_feeding, r"%d/%m/%Y")

    def _validate_types(self):
            productiontype = self.production_type

            if productiontype not in self.valid_feed_types:
                raise ValueError("Tipo de alimentação inválido!")


