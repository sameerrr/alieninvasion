
# Importing libraries
import sys
import pygame

# Importing custom libraries
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        """ self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) """
        # Making screen full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption(self.settings.game_title)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            # Make the most recently drawn screen visible
            pygame.display.flip()

    def _check_events(self):
        """Watch for keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right=False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left=False

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Udpate the position of the bullets and get rid of the old bullets"""
        # Update bullet positions
        self.bullets.update()
        # Get rid of bullets that have disappered
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make and alien
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        """Update images on the sceen and flip to the new screen """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)


if __name__ == '__main__':
    # Make a game instance and run the game
    ai_game = AlienInvasion()
    ai_game.run_game()
                
