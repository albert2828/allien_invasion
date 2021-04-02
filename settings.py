class Settings:
    """A class that stores all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_speed = 1.5

        # Bullets Settings.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3

        # Aliens settings.
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        # Fleet_direction of 1 represetns right; -1 represetns left
        self.flee_direction = 1
