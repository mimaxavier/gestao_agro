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

