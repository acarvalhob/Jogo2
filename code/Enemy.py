# Enemy.py

from .Entity import Entity
from .placeholders import Surface, Rect


class Enemy(Entity):
    def __init__(self, surf: Surface, rect: Rect):
        super().__init__("Enemy", surf, rect)

    def move(self) -> None:
        print(f"O {self.name} está se movendo para atacar.")
