from jinja2 import Environment, FileSystemLoader

from gamedeck import deck as d

if __name__ == "__main__":
    
    cards = [
        {"text": "Hidden Agenda A"},
        {"text": "Hidden Agenda B"},
        {"text": "Hidden Agenda C"}
    ]

    game_name = "Hidden Agenda cardgame"
    
    environment = Environment(loader=FileSystemLoader("templates/"))
    results_filename = "web_game_all-cards.html"
    results_template = environment.get_template("game_all-cards.html")
    context = {
        "cards": cards,
        "game_name": game_name,
    }
    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")