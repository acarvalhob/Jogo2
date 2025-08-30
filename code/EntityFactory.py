# EntityFactory.py

from .Entity import Entity
from .Player import Player
from .Enemy import Enemy
from .Background import Background
from .placeholders import Surface, Rect


class EntityFactory:
    @staticmethod
    def get_entity(entity_type: str) -> Entity:
        temp_surf = Surface()
        temp_rect = Rect()

        if entity_type == "Player":
            return Player(temp_surf, temp_rect)
        elif entity_type == "Enemy":
            return Enemy(temp_surf, temp_rect)
        elif entity_type == "Background":
            return Background(temp_surf, temp_rect)
        else:
            raise ValueError(f"Tipo de entidade desconhecido: {entity_type}")
