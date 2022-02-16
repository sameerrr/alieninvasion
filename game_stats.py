class GameStats:
    """Tracking the statistics of Alien Invasion game"""

    def __init__(self, ai_game) -> None:
        """Initializing the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in active state
        self.game_active = False

    def reset_stats(self):
        """Initialize statsitics of the game that can change as game progresses"""
        self.ships_left = self.settings.ship_limit
        self.score = 0