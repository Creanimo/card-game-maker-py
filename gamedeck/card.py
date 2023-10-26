
from dataclasses import dataclass, field
from tools import objectTools
from typing import Union
from gamedeck import side

@dataclass
class Card:
    name: str
    frontside: side.Side
    backside: Union[side.Side, None] = None
    customPrintSize_width: Union[int, None] = None
    customPrintSize_height: Union[int, None] = None
    cardType: str = "default"
    template: str = "card.html"
    id: str = field(default_factory=objectTools.generateID)