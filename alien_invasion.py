import sys
import pygame

class AlienInvasion:
    """Overall class that will manage game behavior."""

    def __init__(self):
        """Initialize the game and create needed resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Starts the main game loop."""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()