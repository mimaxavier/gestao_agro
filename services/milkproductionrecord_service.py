from models.milkproductionrecord import MilkProductionRecord
from repositories.milkproductionrecord_repository import MilkProductionRecordRepository
import logging

logger = logging.getLogger(__name__)

class MilkProductionService:
    def __init__(self, repository = None):
        self.repository = repository or MilkProductionRecordRepository()

    def register(self, milkproductionrecord):
        self.repository.save(milkproductionrecord)

        logger.info = {"Produção registrada!"}

    def findall(self):
        return self.repository.find_all()
        

    def get_by_id():
        pass

    def update():
        pass

    def remove():
        pass