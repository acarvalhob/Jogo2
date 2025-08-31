# main.py

import pygame
from code.Menu import Menu
from const import WIN_WIDTH, WIN_HEIGHT

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init() # Inicializa o mixer
    game_window = pygame.display.set_mode(size=[WIN_WIDTH, WIN_HEIGHT])
    main_menu = Menu(window=game_window)
    main_menu.run()