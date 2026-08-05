from models.feedingrecord import FeedingRecord
from repositories.feedingrecord_repository import FeedingRecordRepository
from datetime import date, datetime
import logging

logger = logging.getLogger(__name__)

'''class FeedingRecordService:
    def __init__(self, repository = None):
        self.repository = repository or FeedingRecordRepository()

    def _validate_if_feedingrecord_exists(self, id):
        feedingrecord_db = self.get_by_id(id)

        if feedingrecord_db is None:
            raise ValueError("O registro não existe! Forneça um ID válido!")
        else:
            return id

    def '''
