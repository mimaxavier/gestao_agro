from datetime import datetime
class ProductionRecord:
    production_type_list = {
        1: "milk",
        2: "eggs",
        3: "wool"
    }

    def __init__(self, production_type, unit, quantity_production, date_production):
        self._validate_production_type(production_type)
        self._validate_quantity_production(quantity_production)
        self._validate_unit(unit)

        self.production_type = production_type
        self.unit = unit
        self.quantity_production = quantity_production
        self.date_production = datetime.strptime(date_production, r"%d/%m/%Y")

    # Validate production
    def _validate_production_type(self, production):
        if production not in self.production_type_list:
            raise ValueError("Tipo de Produção inválido!")
        
        if not isinstance(production, str):
            raise TypeError("A unidade precisa ser uma string!")
        
        if production is None:
            raise ValueError("Precisa digitar um tipo de produção!")
        
        if not production.strip():
            raise ValueError("Tipo de Produção não pode estar vazia!")

    # Validate quantity
    def _validate_quantity_production(self, quantity_production):
        if quantity_production <= 0:
            raise ValueError("A quantidade não pode ser menor ou igual a 0!")
        
        if not isinstance(quantity_production, int):
            raise TypeError("A unidade precisa ser um inteiro!")
        
        if quantity_production is None:
            raise ValueError("A quantidade não pode estar vazia!")
        
    # Validate unit    
    def _validate_unit(self, unit: str):
        if unit is None:
            raise ValueError ("Precisa digitar uma unidade.")
        
        if not isinstance(unit, str):
            raise TypeError("A unidade precisa ser uma string!")
        
        if not unit.strip():
            raise ValueError("Unidade não pode estar vazia!")
        
       
      



  
