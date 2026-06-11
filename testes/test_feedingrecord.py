from models.feedingrecord import FeedingRecord
from datetime import datetime
from datetime import date
import pytest

def test_create_feedingrecord():
    feedingrecord = FeedingRecord(2, "Silagem", 45, "25/03/2024")

    assert feedingrecord.animal_id == 2

    assert feedingrecord.typefeeding == "Silagem"

    assert feedingrecord.quantity_feeding == 45

    assert feedingrecord.date_feeding == datetime(2024, 3, 25, 0, 0)

def test_type_out_of_validtypes():
    with pytest.raises(ValueError) as exc_info:
        feedingrecord = FeedingRecord(2, "Pastagem", 45, "25/03/2024")

    assert str(exc_info.value) == "Tipo de alimentação inválido!"

def test_quantityfeeding_must_be_int_float():
    with pytest.raises(TypeError) as exc_info:

        feedingrecord2 = FeedingRecord(2, "Silagem", "oi", "25/03/2024")

    assert str(exc_info.value) == "Quantidade deve ter valor real! Digite um número real."

def test_quantityfeeding_cannot_be_none():
    with pytest.raises(ValueError) as exc_info:

        feedingrecord3 = FeedingRecord(2, "Silagem", None, "25/03/2024")

    assert str(exc_info.value) == "A quantidade não pode estar vazia!"


    


