from models.animal import Animal
from datetime import datetime, date

class FeedingRecord:
    valid_feed_types = [
            "Silagem",
            "Feno",
            "Capim"
            ]

    def __init__(self, animal_id, type_feeding, quantity_feeding, date_feeding, id = None):
        '''self._validate_types(type_feeding)
        self._validate_quantityfeeding(quantity_feeding)
        self._validate_date_feeding(date_feeding)'''

        self.animal_id = animal_id
        self.type_feeding = self._validate_types(type_feeding)
        self.quantity_feeding = self._validate_quantityfeeding(quantity_feeding)
        self.date_feeding = self._validate_date_feeding(date_feeding)
        
        '''datetime.strptime(date_feeding, r"%d/%m/%Y").date()'''
        self.id = id

    def _validate_types(self, feedingtype):
            if feedingtype not in self.valid_feed_types:
                raise ValueError("Tipo de alimentação inválido!")
            
            return feedingtype
            
            
    def _validate_quantityfeeding(self, quantity_feeding):
            if quantity_feeding is None:
                  raise ValueError("A quantidade não pode estar vazia!")
            
            if not isinstance(quantity_feeding, (int, float)):
                  raise TypeError("Quantidade deve ter valor real! Digite um número real.")
            
            return quantity_feeding
    
    def _validate_date_feeding(self, date_feeding):
        if isinstance(date_feeding, str):
            return datetime.strptime(
            date_feeding,
            "%d/%m/%Y"
            ).date()
        elif isinstance(date_feeding, date):
            return date_feeding
        else: 
            raise TypeError(
        "date_feeding deve ser uma string ou um objeto date."
        )

    def __repr__(self):
        return (
            f"FeedingRecord("
            f"animal_id={self.animal_id}, "
            f"type_feeding='{self.type_feeding}', "
            f"quantity_feeding={self.quantity_feeding}, "
            f"date_feeding={self.date_feeding})"
        )