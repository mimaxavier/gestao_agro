from models.milkproductionrecord import MilkProductionRecord
from datetime import datetime
from datetime import date
import pytest

#Validate animal_id
def test_animalid_must_be_int():
    with pytest.raises(TypeError) as exc_info:

        production001 = MilkProductionRecord("Um", 50, "24/05/2024 05:25:01")

    assert str(exc_info.value) == "Animal ID precisa ser um número inteiro!" 

def test_animalid_cannot_be_empty():
    with pytest.raises(ValueError) as exc_info:

        production002 = MilkProductionRecord(None, 50, "24/05/24 05:25:01")

    assert str(exc_info.value) == "ID do animal não pode estar vazio!"

#Validate quantity_production
def test_quantityproduction_must_be_greater_than_zero():
    with pytest.raises(ValueError) as exc_info:

        production003 = MilkProductionRecord(3, -5, "24/05/24 05:25:01")

    assert str(exc_info.value) == "A quantidade não pode ser menor ou igual a 0!"

def test_quantity_must_be_int_or_float():
    with pytest.raises(TypeError) as exc_info:

        production003 = MilkProductionRecord(3, "cinco", "24/05/2024 05:25:01")

    assert str(exc_info.value) == "A unidade precisa ser um inteiro!"

def test_quantity_cannot_be_empty():
    with pytest.raises(ValueError) as exc_info:

        production004 = MilkProductionRecord(2, None, "24/05/24 05:25:01")

    assert str(exc_info.value) == "A quantidade não pode estar vazia!"

#Validate production date

def test_dateproduction_must_be_datetime():
    with pytest.raises(TypeError) as exc_info:
        
        production005 = MilkProductionRecord(2, 50, 249839)

    assert str(exc_info.value) == "A data precisa ser informada em dia, mês, ano e horário!"
    

