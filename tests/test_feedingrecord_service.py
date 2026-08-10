from services.feedingrecord_service import FeedingRecordService
from models.feedingrecord import FeedingRecord
from datetime import date, datetime
import pytest

def test_should_accept_valid_feeding_type():
    service = FeedingRecordService()
    with pytest.raises(ValueError) as exc_info:
        service._validate_if_feedingrecord_exists(10)
    assert str(exc_info.value) == "O registro não existe! Forneça um ID válido!"

def test_feedingdate_must_be_datetime_or_str():
    service = FeedingRecordService()
    with pytest.raises(TypeError) as exc_info:
        service._validate_feeding_date(date(2024, 3, 20))
    assert str(exc_info.value) == "Insira um datetime com data e hora."



    