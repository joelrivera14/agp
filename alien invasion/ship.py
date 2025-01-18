import pygame

class Ship:
    
    def __init__(self, ai_game):
        #initializing ship and setting starting position
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect= ai_game.screen.get_rect()

        #loading image and getting its rect
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        #starting each ship at the bottom center
        self.rect.midbottom=self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position. 
        self.x = float(self.rect.x)

        #moving flags
        self.moving_right= False
        self.moving_left = False

    def update(self):
        #Update the ship's position based on the movement flag
        if self.moving_right:
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x. 
        self.rect.x = self.x

    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)