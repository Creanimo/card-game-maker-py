from dataclasses import dataclass

@dataclass
class Side:
    text: str | None = None
    logoimage: str | None = None
    image: str | None = None
    header: str | None = None
    footer: str | None = None
    template: str = "side.html"