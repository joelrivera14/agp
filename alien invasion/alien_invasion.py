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
            #watching keyboard/mouse events with an event loop
            #pygame.event.get() is a funct that returns a list of events
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                    
            #redrawing the game with each pass
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #making most recently drawn screen visible
            pygame.display.flip()


if __name__=='__main__':
    #creating an instance of the object/class and running it
    ai = AlienInvasion()
    ai.run_game()
