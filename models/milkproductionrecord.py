from datetime import datetime, date

class MilkProductionRecord:

    def __init__(self, animal_id, quantity_production, production_date, id = None):

        self.animal_id = self._validate_animalid(animal_id)
        self.quantity_production = self._validate_quantity_production(quantity_production)
        self.production_date = self._validate_production_date(production_date)
        self.id = id
    
       
    # Validate animal_id
    def _validate_animalid(self, animalid):
        if animalid is None:
            raise ValueError("ID do animal não pode estar vazio!")

        if not isinstance(animalid, int):
            raise TypeError("Animal ID precisa ser um número inteiro!")
        
        return animalid
        
    # Validate quantity
    def _validate_quantity_production(self, quantity_production):
        if quantity_production is None:
            raise ValueError("A quantidade não pode estar vazia!")
        
        if not isinstance(quantity_production, (int, float)):
            raise TypeError("A unidade precisa ser um inteiro!")

        if quantity_production <= 0:
            raise ValueError("A quantidade não pode ser menor ou igual a 0!")
        
        return quantity_production
        
    # Validate production date
    def _validate_production_date(self, production_date):
        
        if isinstance(production_date, str):
            production_date = datetime.strptime(production_date, r"%d/%m/%Y %H:%M")

            return production_date

        elif isinstance(production_date, datetime):
            return production_date

        else:
            raise TypeError("Insira um tipo válido!")
