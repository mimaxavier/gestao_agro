from repositories.milkproductionrecord_repository import MilkProductionRecordRepository
from models.milkproductionrecord import MilkProductionRecord
from datetime import datetime, date
import pytest

def test_save_milkproductionrecord():
    # Create objects
    milkproduction001 = MilkProductionRecord(1, 25, "12/03/2025")

    repositorio001 = MilkProductionRecordRepository()

    # Saving
    repositorio001.save(milkproduction001)

    # Result
    assert milkproduction001 is not None


def test_getbyid_milkproductionrepository():
    # Create objects
    milkproduction002 = MilkProductionRecord(2, 26, "13/03/2025")

    repositorio002 = MilkProductionRecordRepository()

    # Saving
    repositorio002.save(milkproduction002)

    # Get by id
    repositorio002.get_by_id(milkproduction002.id)

    # Result
    assert milkproduction002.animal_id == 2
    assert milkproduction002.quantity_production == 26
    assert milkproduction002.date_production == datetime(2025, 3, 13)
