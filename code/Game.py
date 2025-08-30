# Game.py

from .Level import Level
from .EntityFactory import EntityFactory
from .placeholders import Surface


class Game:
    def __init__(self, window: Surface):
        self.window = window
        self.levels = []
        self.levels.append(Level(window, "Nível 1", EntityFactory()))
        self.levels.append(Level(window, "Nível 2", EntityFactory()))

    def run(self) -> None:
        print("Iniciando o jogo.")
        for level in self.levels:
            level.run()
