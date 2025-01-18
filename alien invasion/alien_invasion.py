import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        #initialize game, create game resources
        pygame.init()
        self.settings=Settings()

        #creates 1200X800 display window with set_mode()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship=Ship(self)

    def run_game(self):
        #starting main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    #moving the event loop from run_game into a helper function
    def _check_events(self):
        #watching keyboard/mouse events with an event loop
        #pygame.event.get() is a funct that returns a list of events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            #setting up L/R movement
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #moves ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type==pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    #moving updating the screen code from run_game
    def _update_screen(self):
        #redrawing the game with each pass
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #making most recently drawn screen visible
        pygame.display.flip()



if __name__=='__main__':
    #creating an instance of the object/class and running it
    ai = AlienInvasion()
    ai.run_game()
