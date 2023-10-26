from gamedeck import deck, card, side
from htmlrender import game_render

if __name__ == "__main__":

    defaultBackside = side.Side(logoimage="logo.png")

    # Creating an example deck object with 3 cards
    card1 = card.Card("Card 1", side.Side("Frontside 1"), defaultBackside)
    card2 = card.Card("Card 2", side.Side("Frontside 2"), defaultBackside)
    card3 = card.Card("Card 3", side.Side("Frontside 3"), defaultBackside)

    wholeDeck = deck.Deck(148, 105, "Example Deck", 1, [card1, card2, card3])

    renderThis = game_render.RenderGameElement(wholeDeck.template, wholeDeck)
    renderThis.html()

    with open("export/card-deck.html", "w") as file:
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
    
        