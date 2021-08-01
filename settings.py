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
        self.screen_height = int(800 * multiplier)
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # direction of 1 is right, direction of -1 is left
        self.fleet_direction = 1