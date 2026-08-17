from services.feedingrecord_service import FeedingRecordService
from models.feedingrecord import FeedingRecord
from enums.FeedType import FeedType
from datetime import date, datetime
import pytest

def test_should_accept_valid_feeding_type():
    service = FeedingRecordService()
    with pytest.raises(ValueError) as exc_info:
        service._validate_if_feedingrecord_exists(10)
    assert str(exc_info.value) == "O registro não existe! Forneça um ID válido!"

def test_should_not_accept_object_already_registered():
    service = FeedingRecordService()
    feed001 = FeedingRecord(2, FeedType.SILAGE, 50, "12/03/2026 08:30")
    service.register(feed001)

    with pytest.raises(ValueError) as exc_info:
        service.register(feed001)
    assert str(exc_info.value) == "O registro já existe!"

def test_register_feed():
    service = FeedingRecordService()
    feed001 = FeedingRecord(2, FeedType.SILAGE, 50, "12/03/2026 08:30")
    service.register(feed001)

    assert feed001.animal_id == 2
    assert feed001.feeding_type == FeedType.SILAGE
    assert feed001.feeding_quantity == 50
    assert feed001.feeding_date == datetime(2026, 3, 12, 8, 30)

def test_findall():
    ''service = FeedingRecordService()

    service.findall()

    assert isinstance(list, str)
    assert len(list) == 9'''

def test_get_by_id():
    pass

def test_update():
    pass

def test_remove():
    pass

    