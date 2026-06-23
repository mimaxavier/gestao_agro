import pytest
from freezegun import freeze_time
import logging

@pytest.fixture(autouse=True)
def congelar_tempo():
    with freeze_time("2026-06-23"):
        yield

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)