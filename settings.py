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
        self.ship_limit = 3
        # Bullet setttings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        # Alien setting
        self.fleet_drop_speed = 10
        # How quickly the game speeds up
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        # Game settings
        self.pause = 1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the games settings that are changing throught the game"""
        self.ship_speed = .5
        self.bullet_speed = 3.0
        self.alien_speed = .1
        # Fleet direction of 1 is right and -1 is left
        self.fleet_direction = 1
        # Scoring 
        self.alien_points = 50

    def increase_speed(self):
        """Settings to increase the speed and alien points. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

