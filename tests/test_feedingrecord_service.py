from services.feedingrecord_service import FeedingRecordService
from models.feedingrecord import FeedingRecord
from enums.FeedType import FeedType
from datetime import date, datetime
import pytest

def test_should_accept_valid_feeding_type():
    service = FeedingRecordService()
    with pytest.raises(ValueError) as exc_info:
        service._validate_if_feedingrecord_exists(109)
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
    service = FeedingRecordService()
    feed001 = FeedingRecord(2, FeedType.SILAGE, 50, "12/03/2026 08:30")
    service.register(feed001)

    feedrecords = service.findall()

    assert isinstance(feedrecords, list)
    '''assert len(feedrecords) == 1'''

def test_get_by_id():
    #Arrange
    feed04 = FeedingRecord(3, FeedType.PASTURE, 80, "16/06/2025 07:30")
    service002 = FeedingRecordService()

    # Act
    service002.register(feed04)
    gettingbyid = service002.get_by_id(feed04.id)

    # Assert
    assert gettingbyid.feeding_type == FeedType.PASTURE
    assert gettingbyid.feeding_quantity == 80
    assert gettingbyid.feeding_date == datetime(2025, 6, 16, 7, 30)
    

def test_update():
    # Arrange
    feed04 = FeedingRecord(3, FeedType.PASTURE, 80, "16/06/2025 07:30")
    service002 = FeedingRecordService()

    service002.register(feed04)

    feed04.feeding_quantity = 40
    feed04.feeding_type = FeedType.HAY

    # Act
    service002.update(feed04)

    # Assert
    assert feed04.feeding_quantity == 40
    assert feed04.feeding_type == FeedType.HAY

    print(feed04.feeding_type)

def test_remove():
    # Arrange
    feed04 = FeedingRecord(3, FeedType.PASTURE, 80, "16/06/2025 07:30")
    service002 = FeedingRecordService()
     
    # Act
    service002.register(feed04)
    service002.remove(feed04.id)
    gettingbyid = service002.get_by_id(feed04.id)
    
    # Assert
    assert gettingbyid is None