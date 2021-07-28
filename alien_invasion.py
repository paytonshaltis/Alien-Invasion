import sys
import pygame.display, pygame.event
from pygame.locals import *

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class that will manage game behavior."""

    def __init__(self):
        """Initialize the game and create needed resources."""
        pygame.init()
        
        # create a settings attribute for this game instance
        self.settings = Settings('MacBook Pro')

        # set the screen dimensions and caption (this is a surface)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.scren_height))
        pygame.display.set_caption('Alien Invasion')

        # create a ship attribute for this game instance
        self.ship = Ship(self)

    def run_game(self):
        """Starts the main game loop."""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # redraw the ship during each pass through the loop
            self.ship.blitme()

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()