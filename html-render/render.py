from jinja2 import Environment, FileSystemLoader
from gamedeck import card, side, deck

class Template:
    def __init__(self, templateFile: str, output: str | None = None):
        self.templateFile: str = templateFile
        self.output: str | None = output
        self.environment = Environment(loader=FileSystemLoader("templates/"))

class Render():
    def __init__(self, template: type[Template]):
        self.template = template

class RenderElement(Render):
    def __init__(self, template: type[Template], objectToRender: type[card.Card | side.Side | deck.Deck]):
        super().__init__(template)
        self.objectToRender: type[card.Card | side.Side | deck.Deck] = objectToRender

    def html(self):
        if isinstance(self.objectToRender, deck.Deck):
            html:str = self._renderDeck(self)
        elif isinstance(self.objectToRender, card.Card):
            html:str = self._renderCard(self)
        elif isinstance(self.objectToRender, side.Side):
            html:str = self._renderSide(self)
        return html


    def _renderDeck(self):
        pass

    def _renderCard(self):
        pass

    def _renderSide(self):
        pass