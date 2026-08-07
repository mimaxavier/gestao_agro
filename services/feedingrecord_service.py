from models.feedingrecord import FeedingRecord
from repositories.feedingrecord_repository import FeedingRecordRepository
from datetime import date, datetime
import logging

logger = logging.getLogger(__name__)

class FeedingRecordService:
    def __init__(self, repository = None):
        self.repository = repository or FeedingRecordRepository()

    def _validate_if_feedingrecord_exists(self, id):
        feedingrecord_db = self.repository.get_by_id(id)

        if feedingrecord_db is None:
            raise ValueError("O registro não existe! Forneça um ID válido!")
        else:
            return id

    def _validate_feeding_date(self, feeding_date):
        if isinstance(feeding_date_date, str):
            feeding_date_date = datetime.strptime(feeding_date_date, r"%d/%m/%Y %H:%M")
            return feeding_date_date
                
        elif isinstance(feeding_date_date, datetime):
            return feeding_date_date
        
        elif isinstance(feeding_date_date, date):
            raise TypeError(
                "Insira um datetime com data e hora."
            )
        
        else:
            raise TypeError("A data de produção deve ser uma string ou datetime")

    def _validate_object_is_ready_for_register(self, feedingrecord):
        if feedingrecord.id is not None:
            raise ValueError("O registro já existe!")
