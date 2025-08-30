# Level.py

from .EntityFactory import EntityFactory
from .placeholders import Surface


class Level:
    def __init__(self, window: Surface, name: str, entity_factory: EntityFactory):
        self.window = window
        self.name = name
        self.entity_list = []
        self.entity_factory = entity_factory
        self._populate_entities()

    def _populate_entities(self):
        self.entity_list.append(self.entity_factory.get_entity("Player"))
        self.entity_list.append(self.entity_factory.get_entity("Enemy"))
        self.entity_list.append(self.entity_factory.get_entity("Background"))

    def run(self) -> None:
        print(f"\nRodando o nível: {self.name}")
        for entity in self.entity_list:
            entity.move()
