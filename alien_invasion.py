# importing external packages / modules
import sys
from time import sleep
import pygame, pygame.display, pygame.event, pygame.sprite
from pygame.locals import *

# importing my own modules from this project
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
    """Overall class that will manage game behavior."""

    def __init__(self, screen, full_screen=False):
        """Initialize the game and create needed resources."""
        pygame.init()
        
        # create a settings attribute for this game instance
        self.settings = Settings(screen)

        # if the game is to be played in fullscreen mode
        if full_screen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        
        # set the screen dimensions and caption (this is a surface)
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption('Alien Invasion')

        # create an instance to store game statistics
        self.stats = GameStats(self)

        # create a ship attribute for this game instance
        self.ship = Ship(self)

        # create a Group of live Bullet objects (from Sprite)
        self.bullets = pygame.sprite.Group()

        # create a Group of live Alien objects (from Sprite)
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """Starts the main game loop."""
        while True:
            self._check_events()

            if self.stats.game_active:    
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():

            # closing the window quits the game
            if event.type == QUIT:
                sys.exit()

            # check certain event pased on event.type
            elif event.type == KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == K_RIGHT:
            self.ship.moving_right = True
        elif event.key == K_LEFT:
            self.ship.moving_left = True
        elif event.key == K_SPACE:
            self._fire_bullet()
        elif event.key == K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        if event.key == K_RIGHT:
            self.ship.moving_right = False
        elif event.key == K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new Bullet and add it to the 'bullets' list."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # create an Alien and find the number of Aliens in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = int(available_space_x / (2 * alien_width))

        # determine the number of rows of Aliens that fit on the scree
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / (2 * alien_height))

        # create the full fleet of Aliens
        for row_number in range(number_rows):    
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an Alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # update the position of all Bullets
        self.bullets.update()

        # get rid of Bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to Bullet-Alien collisions."""
        # upon collision, get rid of the Bullet and the Alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # destroy existing Bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """Respond to the Ship being hit by an Alien."""
        if self.stats.ships_left > 0:
            # decrement ships_left
            self.stats.ships_left -= 1

            # get rid of any remaining Aliens and Bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the Ship
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
    
    def _check_aliens_bottom(self):
        """Check if any Aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
            # treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # look for Alien-Ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for alines hitting the bottom of the screen
        self._check_aliens_bottom()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = AlienInvasion(screen='AOC', full_screen=True)
    game.run_game()