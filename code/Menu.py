# Menu.py

import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Game import Game
from const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, C_WHITE


class WiN_WIDTH:
    pass


class Menu:
    def __init__(self, window):
        self.window = window
        # Carrega a imagem original
        original_surf = pygame.image.load('./asset/MenuBg.png')
        # Redimensiona a imagem para 576x324
        self.surf = pygame.transform.scale(original_surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.game = Game(window=self.window)

        # Configuração e reprodução da música
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)  # O -1 faz com que a música toque em loop

    def run(self):
        running = True
        while running:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Montain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Exibe o menu
            pygame.display.flip()

        # Para parar a música quando sair do menu
        pygame.mixer.music.stop()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

        # O jogo não será iniciado, pois o loop foi quebrado com o QUIT.
        # Se você quiser que o jogo comece após o menu, adicione uma lógica de clique.
