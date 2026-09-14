from services.milkproductionrecord_service import MilkProductionService
from models.milkproductionrecord import MilkProductionRecord
from datetime import datetime, date
import pytest

def test_register_milkproduction():
    milkproductionrecord001 = MilkProductionRecord(
        1, 30, "24/02/2026 12:30"
    )

    service = MilkProductionService()

    service.register(milkproductionrecord001)

    result = service.get_by_id(milkproductionrecord001.id)

    assert result is not None
    assert result.animal_id == 1
    assert result.quantity_production == 30

def test_findall():
    milkproduction001 = MilkProductionRecord(
        2, 200, "24/03/2026 15:30"
    )
    milkproduction002 = MilkProductionRecord(
        3, 100, "28/05/2026 14:30"
    )

    service = MilkProductionService()

    service.register(milkproduction001)
    service.register(milkproduction002)

    production = service.findall()

    productions_by_id = {
        record.id: record
        for record in production
    }

    assert productions_by_id[milkproduction001.id].animal_id == 2
    assert productions_by_id[milkproduction001.id].quantity_production == 200
    assert productions_by_id[milkproduction001.id].production_date == datetime(
        2026, 3, 24, 15, 30
    )

    assert productions_by_id[milkproduction002.id].animal_id == 3
    assert productions_by_id[milkproduction002.id].quantity_production == 100
    assert productions_by_id[milkproduction002.id].production_date == datetime(
        2026, 5, 28, 14, 30
    )

    assert isinstance(production, list)

def test_get_by_id():
    milkproduction003 = MilkProductionRecord(4, 100, "23/07/2025 08:30")
    service002 = MilkProductionService()

    service002.register(milkproduction003)

    milkproductionrecord = service002.get_by_id(milkproduction003.id)

    assert milkproductionrecord.animal_id == 4
    assert milkproductionrecord.quantity_production == 100
    assert milkproductionrecord.production_date == datetime(2025, 7, 23, 8, 30)

def test_update_milkproduction():
    milkproduction003 = MilkProductionRecord(
        4, 100, "23/07/2025 08:30"
    )

    service = MilkProductionService()

    service.register(milkproduction003)

    milkproduction003.quantity_production = 150
    milkproduction003.production_date = "24/07/2025 08:35"

    service.update(milkproduction003)

    updated = service.get_by_id(milkproduction003.id)

    assert updated.quantity_production == 150
    assert updated.production_date == datetime(2025, 7, 24, 8, 35)

def test_remove_milkproduction():
    milkproduction003 = MilkProductionRecord(4, 100, "23/07/2025 08:30")
    service002 = MilkProductionService()
        
    service002.register(milkproduction003)
    print(milkproduction003)

    service002.remove(milkproduction003.id)

    milkproduction = service002.get_by_id(milkproduction003.id)

    assert milkproduction is None

def test_register_should_not_accept_object_already_registered():
    milkproduction = MilkProductionRecord(
        1, 30, "24/02/2026 12:30"
    )

    service = MilkProductionService()

    service.register(milkproduction)

    with pytest.raises(ValueError) as exc_info:
        service.register(milkproduction)

    assert str(exc_info.value) == "O registro já existe!"


def test_update_should_not_accept_nonexistent_id():
    milkproduction = MilkProductionRecord(
        1, 30, "24/02/2026 12:30", id=999999
    )

    service = MilkProductionService()

    with pytest.raises(ValueError) as exc_info:
        service.update(milkproduction)

    assert str(exc_info.value) == (
        "O registro não existe! Forneça um ID válido!"
    )


def test_remove_should_not_accept_nonexistent_id():
    service = MilkProductionService()

    with pytest.raises(ValueError) as exc_info:
        service.remove(999999)

    assert str(exc_info.value) == (
        "O registro não existe! Forneça um ID válido!"
    )


def test_update_should_not_accept_date_without_time():
    milkproduction = MilkProductionRecord(
        1, 30, "24/02/2026 12:30"
    )

    service = MilkProductionService()

    service.register(milkproduction)

    milkproduction.production_date = date(2026, 9, 14)

    with pytest.raises(TypeError) as exc_info:
        service.update(milkproduction)

    assert str(exc_info.value) == (
        "Insira um datetime com data e hora."
    )


def test_update_should_not_accept_invalid_date_format():
    milkproduction = MilkProductionRecord(
        1, 30, "24/02/2026 12:30"
    )

    service = MilkProductionService()

    service.register(milkproduction)

    milkproduction.production_date = "24/02/2026"

    with pytest.raises(ValueError):
        service.update(milkproduction)

