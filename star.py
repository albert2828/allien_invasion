import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """A class to represent a single star"""

    def __init__(self, ai_game):
        """Initialize a star and set its (random) position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the star image and  its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position
        self.x = self.rect.x
