class Settings:
    """A class to store the game's various settings."""

    def __init__(self, screen):
        """Initialize the game's static settings."""

        # determine multiplier for screen dimensions
        if screen == 'MacBook Pro':
            multiplier = 0.75
        elif screen == 'AOC':
            multiplier = 1.0

        self.screen_width = int(1200 * multiplier)
        self.screen_height = int(800 * multiplier)
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speed_up_scale = 1.1

        # how quickly the Alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # speed settings
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.5

        # scoring settings
        self.alien_points = 50
        
        # direction of 1 is right, direction of -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and Alien point values."""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)