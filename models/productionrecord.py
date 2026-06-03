from datetime import datetime

class ProductionRecord:
    products_type = [
        "milk",
        "eggs",
        "lã"
    ]
    def __init__(self, production_type, unit, quantity_production, date_production):
        self.production_type = production_type
        self.unit = unit
        self.quantity_production = quantity_production
        self.date_production = datetime.strptime(date_production, r"%d/%m/%Y")
        self.validade_types = self.validate_products_type()

    def validate_products_type(self):
        if self.production_type not in self.products_type:
            raise ValueError("Tipo de Produção inválido!")
      



  
