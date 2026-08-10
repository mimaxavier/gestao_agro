from models.feedingrecord import FeedingRecord
from repositories.feedingrecord_repository import FeedingRecordRepository
from datetime import date, datetime
import logging

logger = logging.getLogger(__name__)

class FeedingRecordService:
    def __init__(self, repository = None):
        self.repository = repository or FeedingRecordRepository()

# Validações
    def _validate_if_feedingrecord_exists(self, id):
        feedingrecord_db = self.repository.get_by_id(id)

        if feedingrecord_db is None:
            raise ValueError("O registro não existe! Forneça um ID válido!")
        else:
            return id

    def _validate_object_is_ready_for_register(self, feedingrecord):
        if feedingrecord.id is not None:
            raise ValueError("O registro já existe!")

#CRUD

    def register(self, feedingrecord):
        self._validate_object_is_ready_for_register(feedingrecord)

        self.repository.save(feedingrecord)

        logger.info = {"Alimentação registrada!"}

    def findall(self):
        return self.repository.find_all()
        
    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def update(self, feedingrecord):
        self._validate_if_feedingrecord_exists(feedingrecord.id)

        self.repository.update(feedingrecord)

    def remove(self, id):
        self._validate_if_feedingrecord_exists(id)
        self.repository.delete(id)