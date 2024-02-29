import sys
import pygame
from settings import Settings
from ship import Ship
from yiashur import Yiashur

class NibiruInvasion:
    "Class for managing resourses and game behaviour"

    def __init__(self):
        pygame.init()   # Game settings initialisisation to provide stable functioning
        self.clock = pygame.time.Clock() # frame rate setting
        self.settings = Settings() # Instance as an attribute
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Reptiloids're fucking invading us!")

        self.ship = Ship(self)
        self.yiashur = Yiashur(self)
    
    def run_game(self):
        "Main game cycle launching"
        
        while True:
            """Keyboard and numpad actions monitoring"""
            self._check_events() # вызов метода внутри класса
            self._update_screen() # 
            self.clock.tick(60)

    def _check_events(self): # вспомогательный метод
        for event in pygame.event.get(): # Event cycle to read events from a user
            if event.type == pygame.QUIT: # QUIT = close-button or else?
                sys.exit() # Response on close-button
    
    def _update_screen(self): # вспомогательный метод
        self.screen.fill(self.settings.bg_color) # Each sycle step a screen is filled with bg_color
        self.ship.blitme() # корабль рисуется на экране вызовом ship.blitme(), так что корабль выводится поверх фона
        self.yiashur.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    "Instance initialising and game start-up"
    ai = NibiruInvasion() # Instance
    ai.run_game()