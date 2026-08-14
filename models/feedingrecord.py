from models.animal import Animal
from datetime import datetime, date
from enums.FeedType import FeedType

class FeedingRecord:

    def __init__(self, animal_id, feeding_type, feeding_quantity, feeding_date, id = None):

        self.animal_id = animal_id
        self.feeding_type = self._validate_types(feeding_type)
        self.feeding_quantity = self._validate_feedingquantity(feeding_quantity)
        self.feeding_date = self._validate_feeding_date(feeding_date)
        self.id = id

    def _validate_types(self, feed_type):
            if not isinstance(feed_type, FeedType):
                raise TypeError("Tipo de alimentação inválido!")
            else:
                 return feed_type
            
    def _validate_feedingquantity(self, feeding_quantity):
            if feeding_quantity is None:
                  raise ValueError("A quantidade não pode estar vazia!")
            
            if not isinstance(feeding_quantity, (int, float)):
                  raise TypeError("Quantidade deve ter valor real! Digite um número real.")
            
            return feeding_quantity
    
    def _validate_feeding_date(self, feeding_date):
        try:
            return datetime.strptime(
            feeding_date,
            r"%d/%m/%Y %H:%M"
            )
        except ValueError:
             raise ValueError("Feeding datetime must contain date and time")

    def __repr__(self):
        return (
            f"FeedingRecord("
            f"animal_id={self.animal_id}, "
            f"feeding_type='{self.feeding_type}', "
            f"feeding_quantity={self.feeding_quantity}, "
            f"feeding_date={self.feeding_date})"
        )