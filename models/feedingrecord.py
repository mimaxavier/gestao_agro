from models.animal import Animal

class FeedingRecord:
    def __init__(self, animal_id, typefeeding, quantity, date):
        self.animal_id = animal_id
        self.typefeeding = typefeeding
        self.quantity = quantity
        self.date = date

    