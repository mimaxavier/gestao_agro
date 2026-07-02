from repositories.feedingrecord_repository import FeedingRecordRepository
from models.feedingrecord import FeedingRecord
from datetime import date
import pytest

def test_save_feedingrecord():

    feed = FeedingRecord(4, "Silagem", 300, "23/04/2025")

    repositorio001 = FeedingRecordRepository()

    feedr = repositorio001.save(feed)

    assert feedr is not None


def test_get_by_id():
   
    feed2 = FeedingRecord(4, "Silagem", 300, "23/04/2025")

    repositorio002 = FeedingRecordRepository()

    feedr = repositorio002.save(feed2)

    feedrecord = repositorio002.get_by_id(feed2)

    assert feed2.animal_id == 4
    assert feed2.type_feeding == "Silagem"
    assert feed2.quantity_feeding == 300
    assert feed2.date_feeding == date(2025, 4, 23)

def test_update():
    animal = Animal("suine", "12/09/2020", 156)

    repo = AnimalRepository()

    animal_id = repo.save(animal)

    # altera algo
    animal.especie = "bovine"
    animal.id = animal_id

    repo.update(animal)

    updated = repo.get_by_id(animal_id)

    assert updated.especie == "bovine"

def test_delete():
    #criação
    animal = Animal("suine", "12/09/2020", 156)
    repo = AnimalRepository()

    #ação
    animal_id = repo.save(animal)
    repo.delete(animal_id)

    #resultado
    result = repo.get_by_id(animal_id)
    assert result is None