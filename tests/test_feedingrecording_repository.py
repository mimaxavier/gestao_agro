from repositories.feedingrecord_repository import FeedingRecordRepository
from models.feedingrecord import FeedingRecord
from enums.FeedType import FeedType
from datetime import date, datetime
import pytest

def test_save_feedingrecord():

    feed = FeedingRecord(4, FeedType.PASTURE, 300, "23/04/2025 08:30")

    repositorio001 = FeedingRecordRepository()

    feedr = repositorio001.save(feed)

    assert feedr is not None


def test_get_by_id():
   
    feed2 = FeedingRecord(4, FeedType.PASTURE, 300, "23/04/2025 08:30")

    repositorio002 = FeedingRecordRepository()

    feedr = repositorio002.save(feed2)

    feedrecord = repositorio002.get_by_id(feedr.id)

    assert feedrecord.animal_id == 4
    assert feedrecord.feeding_type == FeedType.PASTURE
    assert feedrecord.feeding_quantity == 300
    assert feedrecord.feeding_date == datetime(2025, 4, 23, 8, 30)

def test_findall():
    feed2 = FeedingRecord(4, FeedType.SILAGE, 300, "23/04/2025 08:30")
    feed3 = FeedingRecord(2, FeedType.PASTURE, 150, "23/04/2025 06:30")

    repositorio = FeedingRecordRepository()

    repositorio.save(feed2)
    repositorio.save(feed3)

    feedingrecords = repositorio.find_all()

    feeds_by_id = {feed.id: feed for feed in feedingrecords}

    assert feeds_by_id[feed2.id].feeding_type == FeedType.SILAGE
    assert feeds_by_id[feed2.id].feeding_date == datetime(2025, 4, 23, 8, 30)
    
    assert feeds_by_id[feed3.id].feeding_type == FeedType.PASTURE
    assert feeds_by_id[feed3.id].feeding_date == datetime(2025, 4, 23, 6, 30)

    assert feeds_by_id[feed2.id].feeding_quantity == 300
    assert feeds_by_id[feed3.id].feeding_quantity == 150

    assert isinstance(feedingrecords, list)
    

def test_update():
    feed2 = FeedingRecord(4, FeedType.PASTURE, 300, "23/04/2025 08:30")
    repo = FeedingRecordRepository()

    repo.save(feed2)
    
    # altera algo
    feed2.feeding_type = FeedType.HAY
    feed2.feeding_quantity = 50

    repo.update(feed2)

    updated = repo.get_by_id(feed2.id)

    assert updated.feeding_type == FeedType.HAY
    assert updated.feeding_quantity == 50

def test_delete():
    #criação
    feed4 = FeedingRecord(2, FeedType.PASTURE, 100, "10/02/2024 12:10")
    repo = FeedingRecordRepository()

    #ação
    repo.save(feed4)
    repo.delete(feed4.id)

    #resultado
    result = repo.get_by_id(feed4.id)

    assert result is None