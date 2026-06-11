from models.animal import Animal
from datetime import datetime

class FeedingRecord:
    valid_feed_types = [
            "Silagem",
            "Feno",
            "Capim",
            ]

    def __init__(self, animal_id, type_feeding, quantity_feeding, date_feeding):
        self._validate_types(type_feeding)
        self._validate_quantityfeeding(quantity_feeding)

        self.animal_id = animal_id
        self.typefeeding = type_feeding
        self.quantity_feeding = quantity_feeding
        self.date_feeding = datetime.strptime(date_feeding, r"%d/%m/%Y")

    def _validate_types(self, feedingtype):
            if feedingtype not in self.valid_feed_types:
                raise ValueError("Tipo de alimentação inválido!")
            
            
    def _validate_quantityfeeding(self, quantity_feeding):
            if quantity_feeding is None:
                  raise ValueError("A quantidade não pode estar vazia!")
            
            if not isinstance(quantity_feeding, (int, float)):
                  raise TypeError("Quantidade deve ter valor real! Digite um número real.")
            
            
    
            
    


