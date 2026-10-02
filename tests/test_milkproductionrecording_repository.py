from repositories.milkproductionrecord_repository import MilkProductionRecordRepository
from models.milkproductionrecord import MilkProductionRecord
from datetime import datetime, date
import sqlite3
import pytest

def test_save_milkproductionrecord():
    milkproduction001 = MilkProductionRecord(
        1, 25, "12/03/2025 12:30"
    )

    repository = MilkProductionRecordRepository()
    saved = repository.save(milkproduction001)

    assert saved.id is not None

    result = repository.get_by_id(saved.id)

    assert result.animal_id == 1
    assert result.quantity_production == 25
    assert result.production_date == datetime(2025, 3, 12, 12, 30)


def test_getbyid_milkproductionrepository():
    milkproduction002 = MilkProductionRecord(
        2, 26, "13/03/2025 12:30"
    )

    repository = MilkProductionRecordRepository()
    repository.save(milkproduction002)

    result = repository.get_by_id(milkproduction002.id)

    assert result is not None
    assert result.animal_id == 2
    assert result.quantity_production == 26
    assert result.production_date == datetime(2025, 3, 13, 12, 30)

def test_findall_milkproductionrepository():
    milkproduction001 = MilkProductionRecord(
        1, 25, "12/03/2025 12:30"
    )
    milkproduction002 = MilkProductionRecord(
        2, 30, "13/03/2025 13:30"
    )

    repository = MilkProductionRecordRepository()

    repository.save(milkproduction001)
    repository.save(milkproduction002)

    results = repository.find_all()

    records_by_id = {record.id: record for record in results}

    assert records_by_id[milkproduction001.id].animal_id == 1
    assert records_by_id[milkproduction001.id].quantity_production == 25
    assert records_by_id[milkproduction001.id].production_date == datetime(
        2025, 3, 12, 12, 30
    )

    assert records_by_id[milkproduction002.id].animal_id == 2
    assert records_by_id[milkproduction002.id].quantity_production == 30
    assert records_by_id[milkproduction002.id].production_date == datetime(
        2025, 3, 13, 13, 30
    )

    assert isinstance(results, list)

def test_update_milkproductionrepository():
    milkproduction003 = MilkProductionRecord(
        3, 27, "14/03/2025 12:30"
    )

    repository = MilkProductionRecordRepository()
    repository.save(milkproduction003)

    milkproduction003.quantity_production = 28
    milkproduction003.production_date = datetime(2025, 4, 28, 13, 50)

    repository.update(milkproduction003)

    result = repository.get_by_id(milkproduction003.id)

    assert result.quantity_production == 28
    assert result.production_date == datetime(2025, 4, 28, 13, 50)

def test_delete_milkproductionrepository():
    # Create objects
    milkproduction004 = MilkProductionRecord(4, 28, "15/03/2025 12:30")
    repositorio004 = MilkProductionRecordRepository()

    # Saving objects
    repositorio004.save(milkproduction004)

    # Delete object
    repositorio004.delete(milkproduction004.id)

    # Getbyid
    result = repositorio004.get_by_id(milkproduction004.id)

    # Results
    assert result is None

def test_database_should_reject_invalid_animal_id():

    milkproduction = MilkProductionRecord(
        999999,
        50,
        "28/09/2026 08:00"
    )

    repository = MilkProductionRecordRepository()

    with pytest.raises(sqlite3.IntegrityError):
        repository.save(milkproduction)

def test_database_should_reject_zero_milk_production():

    conn = sqlite3.connect("database/farm.db")
    conn.execute("PRAGMA foreign_keys = ON")

    conn.execute(
        """
        INSERT INTO animals (species, birth_date, weight)
        VALUES (?, ?, ?)
        """,
        ("Bovino", "2024-01-20", 450)
    )

    animal_id = conn.execute(
        "SELECT last_insert_rowid()"
    ).fetchone()[0]

    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            """
            INSERT INTO milkproductionrecord (
                animal_id,
                quantity_production,
                production_date
            )
            VALUES (?, ?, ?)
            """,
            (animal_id, 0, "2026-09-28T08:00:00")
        )

    conn.close()   
