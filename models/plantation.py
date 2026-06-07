from datetime import datetime
from datetime import timedelta

class Plantation:

    def __init__(self, crop_type, field, planting_date, id_plantation = None):
        self.crop_type = crop_type
        self.field = field
        self.planting_date = datetime.strptime(planting_date, "%d/%m/%Y")
        self.id_plantation = id_plantation

        self.expected_harvest_date = self.calcular_colheita()

    def _validate_crop_type(self, crop_type):
        if crop_type is None:
            raise ValueError ("Precisa digitar um tipo de plantação.")
        
        if not isinstance(crop_type, str):
            raise TypeError("A plantação precisa ser uma string!")
        
        if not crop_type.strip():
            raise ValueError("O tipo de plantação não pode estar vazio!")

    def _validate_field(self, field):
        if field is None:
            raise ValueError ("Precisa digitar um campo de plantação.")
            
        if not isinstance(field, str):
            raise TypeError("O campo precisa ser uma string!")
        
        if not field.strip():
            raise ValueError("O campo não pode estar vazio!")

    def _validate_planting_date(self, plantingdate):
        pass

    def calcular_colheita(self):
        crop_cycles = {
            "Corn": 100,
            "Soybean": 250,
            "Sugarcane": 300
        }
        cropcycle = crop_cycles[self.crop_type]
        
        harvest_date = self.planting_date + timedelta(days=cropcycle)

        return harvest_date