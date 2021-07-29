class Settings:
    """A class to store the game's various settings."""

    def __init__(self, screen):
        """Initialize the game's settings. Screen determines
           the resolution of the game based on screentype."""
        
        # determine multiplier for screen dimensions
        if screen == 'MacBook Pro':
            multiplier = 0.75
        elif screen == 'AOC':
            multiplier = 1.0

        self.screen_width = int(1200 * multiplier)
        self.scren_height = int(800 * multiplier)
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5