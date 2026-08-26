from models.feedingrecord import FeedingRecord
from datetime import datetime
from datetime import date
from enums.FeedType import FeedType
import conftest
import pytest

def test_create_feedingrecord():
    feedingrecord = FeedingRecord(2, FeedType.SILAGE, 45, "25/03/2024 12:03", None)

    assert feedingrecord.animal_id == 2

    assert feedingrecord.feeding_type == FeedType.SILAGE

    assert feedingrecord.feeding_quantity == 45

    assert feedingrecord.feeding_date == datetime(2024, 3, 25, 12, 3)

def test_type_out_of_validtypes():
    with pytest.raises(TypeError) as exc_info:
        feedingrecord = FeedingRecord(2, "fen0", 45, "25/03/2024 08:30")

    assert str(exc_info.value) == "Tipo de alimentação inválido!"

def test_quantityfeeding_must_be_int_float():
    with pytest.raises(TypeError) as exc_info:

        feedingrecord2 = FeedingRecord(2, FeedType.PASTURE, "oi", "25/03/2024")

    assert str(exc_info.value) == "Quantidade deve ter valor real! Digite um número real."

def test_quantityfeeding_cannot_be_none():
    with pytest.raises(ValueError) as exc_info:

        feedingrecord3 = FeedingRecord(2, FeedType.PASTURE, None, "25/03/2024")

    assert str(exc_info.value) == "A quantidade não pode estar vazia!"

def test_date_must_be_string_or_date():
    with pytest.raises(TypeError) as exc_info:

        feedingrecord4 = FeedingRecord(3, FeedType.PASTURE, 100, "23/05/25")

    assert str(exc_info.value) == "feeding_date deve estar no formato DD/MM/YYYY HH:MM"