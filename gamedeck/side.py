from dataclasses import dataclass

@dataclass
class Side:
    text: str
    template: str = "side.html"