from models.feedingrecord import FeedingRecord
from datetime import datetime
from enums.FeedType import FeedType
import sqlite3
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

def test_feeding_date_must_follow_expected_format():
    with pytest.raises(TypeError) as exc_info:

        feedingrecord4 = FeedingRecord(3, FeedType.PASTURE, 100, "23/05/25")

    assert str(exc_info.value) == "feeding_date deve estar no formato DD/MM/YYYY HH:MM"

def test_quantityfeeding_cannot_be_zero():
    with pytest.raises(ValueError) as exc_info:
        FeedingRecord(2, FeedType.PASTURE, 0, "25/03/2024 08:30")

    assert str(exc_info.value) == (
        "A quantidade de alimento não pode ser menor ou igual a 0. "
        "Digite um valor válido."
    )

def test_quantityfeeding_cannot_be_negative():
    with pytest.raises(ValueError) as exc_info:
        FeedingRecord(2, FeedType.PASTURE, -10, "25/03/2024 08:30")

    assert str(exc_info.value) == (
        "A quantidade de alimento não pode ser menor ou igual a 0. "
        "Digite um valor válido."
    )

def test_database_should_reject_null_feeding_quantity():

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
            INSERT INTO feedingrecord (
                animal_id,
                feeding_type,
                feeding_quantity,
                feeding_date
            )
            VALUES (?, ?, ?, ?)
            """,
            (animal_id, "pasture", None, "2024-03-25T08:30:00")
        )

    conn.close()


def test_quantityfeeding_accepts_float():
    feedingrecord = FeedingRecord(
        2, FeedType.PASTURE, 12.5, "25/03/2024 08:30"
    )

    assert feedingrecord.feeding_quantity == 12.5


def test_feeding_date_must_be_string_or_datetime():
    with pytest.raises(TypeError):
        FeedingRecord(
            2, FeedType.PASTURE, 100, 12345
        )
