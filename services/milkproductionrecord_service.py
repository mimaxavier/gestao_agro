from models.milkproductionrecord import MilkProductionRecord
from repositories.milkproductionrecord_repository import MilkProductionRecordRepository
from datetime import date, datetime
import logging

logger = logging.getLogger(__name__)

class MilkProductionService:
    def __init__(self, repository = None):
        self.repository = repository or MilkProductionRecordRepository()

    def _validate_production_date(self, production_date):
        if isinstance(production_date, str):
            return datetime.strptime(production_date, r"%d/%m/%Y %H:%M")
        
        elif isinstance(production_date, datetime):
            return production_date

        elif isinstance(production_date, date):
            raise TypeError(
                "Insira um datetime com data e hora."
            )

        else:
            raise TypeError("A data de produção deve ser uma string ou datetime")
        
    def register(self, milkproductionrecord):
        self.repository.save(milkproductionrecord)

        logger.info = {"Produção registrada!"}

    def findall(self):
        return self.repository.find_all()
        

    def get_by_id():
        pass

    def update(self, milkproductionrecord):
        self._validate_production_date(milkproductionrecord)

    def remove():
        pass