from enum import Enum

class FeedType(Enum):
    SILAGE = "silagem"
    HAY = "feno"
    PASTURE = "pasto"
    CONCENTRATE = "concentrado"