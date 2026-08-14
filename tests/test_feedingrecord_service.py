from services.feedingrecord_service import FeedingRecordService
from models.feedingrecord import FeedingRecord
from datetime import date, datetime
import pytest

def test_should_accept_valid_feeding_type():
    service = FeedingRecordService()
    with pytest.raises(ValueError) as exc_info:
        service._validate_if_feedingrecord_exists(10)
    assert str(exc_info.value) == "O registro não existe! Forneça um ID válido!"





    