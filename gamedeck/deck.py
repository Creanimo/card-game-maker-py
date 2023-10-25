from __future__ import annotations
from dataclasses import dataclass, field
from gamedeck import card, side
from tools import objectTools
import json

@dataclass
class Deck:
    defaultPrintSize_width: int
    defaultPrintSize_height: int
    title: str
    edition: int
    defaultBackside: side.Side
    cards: list[card.Card]
    id: str = field(default_factory=objectTools.generateID)

def importFromJson(filename: str):
        with open(filename, "r") as file:
            deck_data = json.load(file)

        for singleCard in deck_data["cards"]:
            singleCard["frontside"] = side.Side(**singleCard["frontside"])
            singleCard["backside"] = side.Side(**singleCard["backside"])

        importedCards = []
        for singleCard in deck_data["cards"]:
            singleCard = card.Card(**singleCard)
            importedCards.append(singleCard)
        deck_data["cards"] = importedCards
        
        deck_data["defaultBackside"] = side.Side(**deck_data["defaultBackside"])

        importedDeck = Deck(**deck_data)

        return importedDeck