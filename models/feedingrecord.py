from models.animal import Animal
from datetime import datetime, date

class FeedingRecord:
    valid_feed_types = [
            "Silagem",
            "Feno",
            "Capim"
            ]

    def __init__(self, animal_id, feeding_type, feeding_quantity, feeding_date, id = None):

        self.animal_id = animal_id
        self.feeding_type = self._validate_types(feeding_type)
        self.feeding_quantity = self._validate_feedingquantity(feeding_quantity)
        self.feeding_date = self._validate_feeding_date(feeding_date)
        self.id = id

    def _validate_types(self, feedingtype):
            if feedingtype not in self.valid_feed_types:
                raise ValueError("Tipo de alimentação inválido!")
            
            return feedingtype
            
            
    def _validate_feedingquantity(self, feeding_quantity):
            if feeding_quantity is None:
                  raise ValueError("A quantidade não pode estar vazia!")
            
            if not isinstance(feeding_quantity, (int, float)):
                  raise TypeError("Quantidade deve ter valor real! Digite um número real.")
            
            return feeding_quantity
    
    def _validate_feeding_date(self, feeding_date):
        if isinstance(feeding_date, str):
            return datetime.strptime(
            feeding_date,
            "%d/%m/%Y"
            ).date()
        elif isinstance(feeding_date, date):
            return feeding_date
        else: 
            raise TypeError(
        "A data de alimentação deve ser uma string ou um objeto date."
        )

    def __repr__(self):
        return (
            f"FeedingRecord("
            f"animal_id={self.animal_id}, "
            f"feeding_type='{self.feeding_type}', "
            f"feeding_quantity={self.feeding_quantity}, "
            f"feeding_date={self.feeding_date})"
        )