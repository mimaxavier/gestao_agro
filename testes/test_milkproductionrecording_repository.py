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

def test_update_milkproductionrepository():
    # Create objects
    milkproduction003 = MilkProductionRecord(3, 27, "14/03/2025")
    repositorio003 = MilkProductionRecordRepository()

    # Saving
    repositorio003.save(milkproduction003)

    # Creating new attributes
    milkproduction003.quantity_production = 28
    milkproduction003.date_production = "28/04/2025"

    # Updating 
    repositorio003.update(milkproduction003)

    # Result
    assert milkproduction003.quantity_production == 28
    assert milkproduction003.date_production == "28/04/2025"

def test_delete_milkproductionrepository():
    # Create objects
    milkproduction004 = MilkProductionRecord(4, 28, "15/03/2025")
    repositorio004 = MilkProductionRecordRepository()

    # Saving objects
    repositorio004.save(milkproduction004)

    # Delete object
    repositorio004.delete(milkproduction004.id)

    # Getbyid
    result = repositorio004.get_by_id(milkproduction004.id)

    # Results
    assert result is None
