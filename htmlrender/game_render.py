from jinja2 import Environment, FileSystemLoader
from dataclasses import asdict
from gamedeck import card, side, deck

class RenderGame():
    def __init__(self, template: str, output: str | None = None):
        self.template: str = template
        self.output: str | None = output
        self.environment = Environment(loader=FileSystemLoader("templates/"))

class RenderGameElement(RenderGame):
    def __init__(self, template: str, objectToRender: object, output: str | None = None):
        super().__init__(template, output)
        self.objectToRender: object = objectToRender
        print(type(objectToRender))

    def html(self) -> str:
        print("Hello")
        if isinstance(self.objectToRender, deck.Deck):
            html:str = self._renderDeck()
        elif isinstance(self.objectToRender, card.Card):
            html:str = self._renderCard()
        elif isinstance(self.objectToRender, side.Side):
            html:str = self._renderSide()
        self.output = html


    def _renderDeck(self):
        env = self.environment
        tpl = env.get_template(self.template)
        print(tpl)
        objectAsDict = asdict(self.objectToRender)
        print(objectAsDict)
        html = tpl.render(deck=self.objectToRender)
        return html

    def _renderCard(self):
        pass

    def _renderSide(self):
        pass