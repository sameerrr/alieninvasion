import pygame

class Ship:
    """ Managing the ship"""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position on game screen"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the ship image and gets its rect
        self.image = pygame.image.load('images/output-onlinepngtools.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
