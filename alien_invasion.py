import sys
import pygame

from settings import Settings

class AlienInvasion:
    """Overall class that will manage game behavior."""

    def __init__(self):
        """Initialize the game and create needed resources."""
        pygame.init()
        self.settings = Settings()

        # set the screen dimensions and caption (this is a surface)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.scren_height))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Starts the main game loop."""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()