from datetime import datetime, date

class MilkProductionRecord:

    def __init__(self, animal_id, quantity_production, date_production, id = None):
        self._validate_animalid(animal_id)
        self._validate_quantity_production(quantity_production)
        self._validate_date_production(date_production)

        self.quantity_production = quantity_production
        self.date_production = datetime.strptime(date_production, r"%d/%m/%Y")
    
       
    # Validate animal_id
    def _validate_animalid(self, animalid):
        if animalid is None:
            raise ValueError("ID do animal não pode estar vazio!")

        if not isinstance(animalid, int):
            raise TypeError("Animal ID precisa ser um número inteiro!")
        
    # Validate quantity
    def _validate_quantity_production(self, quantity_production):
        if quantity_production is None:
            raise ValueError("A quantidade não pode estar vazia!")
        
        if not isinstance(quantity_production, (int, float)):
            raise TypeError("A unidade precisa ser um inteiro!")

        if quantity_production <= 0:
            raise ValueError("A quantidade não pode ser menor ou igual a 0!")
        
    # Validate production date
    def _validate_date_production(self, date_production):
        
        if isinstance(date_production, str):
            date_production = datetime.strptime(date_production, r"%d/%m/%Y").date()

        elif isinstance(date_production, date):
            date_production = date_production

        else:
            raise ValueError("Insira um tipo válido! Date ou String")
        
        return date_production
    
        
