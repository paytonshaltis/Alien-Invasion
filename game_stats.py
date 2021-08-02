import json

class GameStats:
    """Tracks statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # high score read in from json file
        self.scores_fname = 'highscores.json'
        with open(self.scores_fname, 'r') as fp:
            self.high_score = json.load(fp)

        # start Alien Invasion in an inactive state
        self.game_active = False

    def save_high_score(self):
        """Saves the high score to the json file"""
        with open(self.scores_fname, 'w') as fp:
                json.dump(self.high_score, fp)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1