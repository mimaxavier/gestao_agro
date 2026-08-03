from models.milkproductionrecord import MilkProductionRecord
from repositories.milkproductionrecord_repository import MilkProductionRecordRepository
from datetime import date, datetime
import logging

logger = logging.getLogger(__name__)

class MilkProductionService:
    def __init__(self, repository = None):
        self.repository = repository or MilkProductionRecordRepository()

    def _validate_if_milkproductionrecord_exists(self, id):
        milkproduction_db = self.get_by_id(id)

        if milkproduction_db is None:
            raise ValueError("O registro não existe! Forneça um ID válido!")
        else:
            return id

    def _validate_production_date(self, production_date):
        if isinstance(production_date, str):
            production_date = datetime.strptime(production_date, r"%d/%m/%Y %H:%M")
            return production_date
        
        elif isinstance(production_date, datetime):
            return production_date

        elif isinstance(production_date, date):
            raise TypeError(
                "Insira um datetime com data e hora."
            )

        else:
            raise TypeError("A data de produção deve ser uma string ou datetime")

    def _validate_object_is_ready_for_register(self, milkproductionrecord):
        if milkproductionrecord.id is not None:
            raise ValueError("O registro já existe!")
      
        
    def register(self, milkproductionrecord):
        self._validate_object_is_ready_for_register(milkproductionrecord)

        self.repository.save(milkproductionrecord)

        logger.info = {"Produção registrada!"}

    def findall(self):
        return self.repository.find_all()
        

    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def update(self, milkproductionrecord):
        self._validate_if_milkproductionrecord_exists(milkproductionrecord.id)
        self._validate_production_date(milkproductionrecord.production_date)

        self.repository.update(milkproductionrecord)

    def remove(self, id):
        self._validate_if_milkproductionrecord_exists(id)
        self.repository.delete(id)
