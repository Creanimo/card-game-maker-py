from gamedeck import deck, card, side
from htmlrender import game_render

if __name__ == "__main__":

    defaultBackside = side.Side(logoimage="logo.png")

    cards: list[card.Card] = [
        card.Card(side.Side("Bringe eine Person dazu mit dir den Platz zu tauschen, ohne dass sie Verdacht schöpft."), defaultBackside),
        card.Card(side.Side("Mache der gleichen Person 3 Komplimente."), defaultBackside),
        card.Card(side.Side("Verabrede dich mit jemandem zum Tanzen, Bowling, Klettern oder Wandern."), defaultBackside),
        card.Card(side.Side("Rede über eine Berühmtheit aus deiner Kinder-/Jugendzeit."), defaultBackside),
        card.Card(side.Side('Kratz dich an der Nase, wenn jemand das Wort "lecker" sagt.'), defaultBackside)
    ]

    cardNumber = 1
    for singleCard in cards:
        singleCard.frontside.header = "Geheime Mission"
        singleCard.frontside.footer = f"{cardNumber}"
        cardNumber += 1


    wholeDeck = deck.Deck(148, 104, "Example Deck", 1, cards)

    renderThis = game_render.RenderGameElement(wholeDeck.template, wholeDeck)
    renderThis.html()

    with open("export/card-deck.html", "w", encoding='utf-8') as file:
        file.write(renderThis.output)

    # print(wholeDeck)

    # print(deck.importFromJson("deck.json").__dict__)
    # print(wholeDeck.__dict__)


    '''
    deck_data = asdict(wholeDeck)

    # Write the deck data to a JSON file
    with open("deck.json", "w") as file:
        json.dump(deck_data, file, indent=4)

    


    
    # Assuming your JSON data is stored in a file named "deck.json"
    with open("deck.json", "r") as file:
        deck_data = json.load(file)

    # Create Card objects from the JSON data
    cardstack = []
    for card_data in deck_data["cards"]:
        acard = card.Card(**card_data)
        cardstack.append(acard)

    # Create a Deck object from the JSON data
    deck = deck.Deck(**deck_data)

    print(deck) 
    '''
    
        