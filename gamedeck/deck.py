from __future__ import annotations
from dataclasses import dataclass, field, asdict
from gamedeck import card, side
from tools import objectTools
import json

@dataclass
class Deck:
    defaultPrintSize_width: int
    defaultPrintSize_height: int
    title: str
    edition: int
    cards: list[card.Card]
    template: str = "deck.html"
    id: str = field(default_factory=objectTools.generateID)

    def exportFromJson(self, filename: str = "deck.json"):
        deck_data: dict[str, object] = asdict(self)

        with open(filename, "w") as file:
            json.dump(deck_data, file)

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