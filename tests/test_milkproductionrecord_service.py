from services.milkproductionrecord_service import MilkProductionService
from models.milkproductionrecord import MilkProductionRecord
from datetime import date, datetime

def test_register_milkproduction():
    milkproductionrecord001 = MilkProductionRecord(1, 30, "24/02/2026 12:30")
    service = MilkProductionService()

    service.register(milkproductionrecord001)

    assert milkproductionrecord001 is not None

def test_findall():
    # Create objects
    milkproduction001 = MilkProductionRecord(2, 200, "24/03/2026 15:30")
    milkproduction002 = MilkProductionRecord(3, 100, "28/05/2026 14:30")

    # Create service
    service001 = MilkProductionService()

    # Registering Objects
    service001.register(milkproduction001)
    service001.register(milkproduction002)

    # Finding all
    production = service001.findall()

    # Results
    assert len(production)
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
    milkproduction003 = MilkProductionRecord(4, 100, "23/07/2025 08:30")
    service002 = MilkProductionService()
    
    service002.register(milkproduction003)

    print(service002.get_by_id(milkproduction003.id))

    milkproduction003.quantity_production = 150
    milkproduction003.production_date = "24/07/2025 08:35"

    service002.update(milkproduction003)

    print(service002.get_by_id(milkproduction003.id))

    assert milkproduction003.quantity_production == 150
    assert milkproduction003.production_date == datetime(2025, 7, 24, 8, 35)

def test_remove_milkproduction():
    milkproduction003 = MilkProductionRecord(4, 100, "23/07/2025 08:30")
    service002 = MilkProductionService()
        
    service002.register(milkproduction003)
    print(milkproduction003)

    service002.remove(milkproduction003.id)

    milkproduction = service002.get_by_id(milkproduction003.id)

    assert milkproduction is None

