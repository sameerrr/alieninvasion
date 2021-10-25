class Settings:
    """ A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.game_title = "Alien Invasion"
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.1