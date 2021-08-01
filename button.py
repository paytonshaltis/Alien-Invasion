import pygame.font

class Button:
    """Class for creating Buttons in Pygame."""

    def __init__(self, ai_game, message):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)