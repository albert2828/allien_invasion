import sys

import pygame

class AllienInvasion():
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1000,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Star the main loop for the game"""
        while True:
            # Watch for kearboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Make the most recently drawn screen visible.
                pygame.display.flip()

if __name__=='__main__':
    # Make a game instance, and run the game.
    ai = AllienInvasion()
    ai.run_game()
