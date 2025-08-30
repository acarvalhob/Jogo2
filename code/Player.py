# Player.py

from .Entity import Entity
from .placeholders import Surface, Rect


class Player(Entity):
    def __init__(self, surf: Surface, rect: Rect):
        super().__init__("Player", surf, rect)

    def move(self) -> None:
        print(f"O {self.name} está se movendo.")
