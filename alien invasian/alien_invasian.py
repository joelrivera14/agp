import pygame
import sys

class AlienInvasian:

    def __init__(self):
        #initialize game, create game resources
        pygame.init()

        #creates 1200X800 display window
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasian')

        self.bg_color=(230,230,230)

    def run_game(self):
        #starting main loop for the game
        while True:
            #watching keyboard/mouse events with an event loop
            #pygame.event.get() is a funct that returns a list of events
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                    
            #redrawing the game with each pass
            self.screen.fill(self.bg_color)

            #making most recently drawn screen visible
            pygame.display.flip()


if __name__=='__main__':
    #creating an instance of the object/class and running it
    ai = AlienInvasian()
    ai.run_game()
