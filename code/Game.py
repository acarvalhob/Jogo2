# Game.py
import pygame

from code.EntityFactory import EntityFactory
from code.Level import Level
from code.placeholders import Surface


class Game:
    def __init__(self, window: Surface):
        # O Game recebe a janela do Pygame do Menu
        self.window = window
        self.levels = []
        # O Game possui e gerência os níveis
        self.levels.append(Level(window, "Nível 1", EntityFactory()))
        self.levels.append(Level(window, "Nível 2", EntityFactory()))

    def run(self) -> None:
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        """Lógica de execução do jogo."""
        print("Iniciando o jogo.")
        for level in self.levels:
            # O Game executa os níveis
            level.run()
