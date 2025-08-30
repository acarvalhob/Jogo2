# Background.py

from .Entity import Entity
from .placeholders import Surface, Rect


class Background(Entity):
    def __init__(self, surf: Surface, rect: Rect):
        super().__init__("Background", surf, rect)

    def move(self) -> None:
        print(f"O {self.name} está rolando.")
