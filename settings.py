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
        self.ship_speed = 1.5

        # Bullet setttings
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # Alien setting
        self.alien_speed = 0.1
        self.fleet_drop_speed = 30
        # Fleet direction of 1 is right and -1 is left
        self.fleet_direction = 1
