from models.milkproductionrecord import MilkProductionRecord
from datetime import datetime
from datetime import date
import pytest

#Validate animal_id
def test_animalid_must_be_int():
    with pytest.raises(TypeError) as exc_info:

        production001 = MilkProductionRecord("Um", 50, "24/05/24 05:25:01")

    assert str(exc_info.value) == "Animal ID precisa ser um número inteiro!" 

def test_animalid_cannot_be_empty():
    with pytest.raises(ValueError) as exc_info:

        pass

#Validate quantity_production
def test_quantityproduction_must_be_greater_than_zero():
    pass

def test_quantity_must_be_int_or_float():
    pass

def test_quantity_cannot_be_empty():
    pass

#Validate production date

def test():
    pass

