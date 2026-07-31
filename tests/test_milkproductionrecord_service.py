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
