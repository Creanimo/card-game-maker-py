
exampleFieldDict: list[dict[str, str | None | int]] = [
        {"type": "text", "label": "Title", "target": "title", "input": None},
        {"type": "text", "label": "Card Width", "target": "defaultPrintSize_width", "input": None},
        {"type": "text", "label": "Card Height", "target": "defaultPrintSize_height", "input": None},
        {"type": "text", "label": None, "target": "edition", "input": 1}
    ]

form = formAskParameters.FormAskFromDict("test Form", exampleFieldDict)


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
