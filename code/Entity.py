# Entity.py

from .placeholders import Surface, Rect

class Entity:
    def __init__(self, name: str, surf: Surface, rect: Rect):
        self.name = name
        self.surf = surf
        self.rect = rect

    def move(self) -> None:
        raise NotImplementedError("Subclass must implement abstract method 'move'")